# NI DOCUMENT BUNDLE: ni-switch-19.0-net-framework-40-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-switch-19.0-net-framework-40-api-ref start=1 end=182 -->
<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchchannel.htm language=enus -->
## TOPIC 00001: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchchannel.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchChannel](t_nationalinstruments_modularinstruments_niswitch_switchchannel.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | AnalogBusSharingEnable | Gets or sets a value that indicates whether an analog bus line is shared, so that multiple NI SwitchBlock devices may connect to it simultaneously. To enable multiple NI SwitchBlock devices to share an analog bus line, set this attribute to trueTruetruetrue (True in Visual Basic) for each device on the channel that corresponds with the shared analog bus line. The default value for all devices is falseFalsefalsefalse (False in Visual Basic), which disables sharing of the analog bus. |
|  | Characteristics | Gets a NISwitch.SwitchCharacteristics object which defines the specific characteristics of a channel. |
|  | IsConfigurationChannel | Gets or sets a value that specifies whether to reserve the channel for creating an internal path. A channel that is available for creating the internal path is called a configuration channel. The driver may use configuration channels to create paths between two channels which you specify in the SwitchPath.Connect method. Configuration channels are not available for external connections. Set this attribute to trueTruetruetrue (True in Visual Basic) to mark the channel as a configuration channel. Set this attribute to falseFalsefalsefalse (False in Visual Basic) to mark the channel as available for external connections. After you identify a channel as a configuration channel, you cannot use that channel for external connections. The SwitchPath.Connect method returns the exception when you attempt to establish a connection between a configuration channel and any other channel. |
|  | IsSourceChannel | Gets or sets a value that specifies whether you want to identify the channel as a source channel. Typically, you set this attribute to trueTruetruetrue (True in Visual Basic) when you attach the channel to a power supply, a function generator, or an active measurement point on the unit under test, and you do not want to connect the channel to another source. The driver prevents source channels from connecting to each other. The SwitchPath.Connect function returns the when you attempt to connect two channels that you identify as source channels. |
|  | Name | Gets the name of the channel as defined in the NI-SWITCH device. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannel Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm language=enus -->
## TOPIC 00002: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchRevisionQueryResult Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchRevisionQueryResult](t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Overloaded. Determines whether the current instance of SwitchRevisionQueryResult and the SwitchRevisionQueryResult object that you specify are equal. |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Returns the hash code for SwitchRevisionQueryResult. (Overrides ValueType..::.GetHashCode()()().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Checks whether the two instances of SwitchRevisionQueryResult are equal. |
|  | Inequality | Checks whether the two instances of SwitchRevisionQueryResult are unequal. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | FirmwareRevision | Gets a string that contains the firmware revision information for the NI-SWITCH instrument that you are currently using. |
|  | InstrumentRevision | Gets a string that contains version information about the NI-SWITCH driver. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscan.htm language=enus -->
## TOPIC 00003: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscan.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscan.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScan Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScan](t_nationalinstruments_modularinstruments_niswitch_switchscan.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Abort | Aborts the scan in progress. Initiate a scan with SwitchScan.Initiate. If the switch module is not scanning, exception is returned. |
|  | Commit | Downloads the configured SwitchScan.List and trigger settings to hardware. |
|  | ConfigureList | Configures the SwitchScan.List and SwitchScan.Mode used for scanning. Refer to Switch Device Help to determine if the switch module supports scanning. The SwitchScan.List is comprised of a list of channel connections separated by semicolons. For example, the following scan list will scan the first three channels of a multiplexer: com0->ch0; com0->ch1; com0->ch2; Refer to SwitchScan.List for more information on scan list syntax. To see the status of the scan, call either SwitchScan.IsScanning or SwitchScan.WaitForScanComplete. Use the SwitchScan.ConfigureTrigger method to configure the scan trigger. Use the SwitchScan.Initiate method to start the scan. |
|  | ConfigureTrigger | Configures the scan triggers for the scan list established with SwitchScan.ConfigureList. Refer to Device Help to determine if the switch module supports scanning. SwitchScan.ConfigureTrigger sets the location that the switch expects to receive an input trigger to advance through the SwitchScan.List. This method also sets the location where it outputs a scan advanced signal after it completes an entry in the scan list. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | Initiate | Commits the configured SwitchScan.List and trigger settings to hardware and initiates the scan. If SwitchScan.Commit was called earlier, SwitchScan.Initiate only initiates the scan and returns immediately. Once the scanning operation begins, you cannot perform any other operation other than GetAttribute, SwitchScan.Abort, or SwitchScan.SendSoftwareTrigger. All other functions return the Exception. To stop the scanning operation, call SwitchScan.Abort. |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RouteScanAdvancedOutput | Routes the SwitchScan.AdvancedOutput from a trigger bus line (TTLx) to the front or rear connector. |
|  | RouteTriggerInput | Routes the SwitchScan.TriggerInput from the front or rear connector to a trigger bus line (TTLx). To disconnect the route, call this function again and specify SwitchScanTriggerInputBusLine.None for trigger bus line parameter. |
|  | Scan | Takes the SwitchScan.List provided, programs the switching hardware and initiates the scan. Once initiation is complete, the operation will return. |
|  | SendSoftwareTrigger | Sends a software trigger to the switch specified in the NI-SWITCH session. When the SwitchScan.TriggerInput is set to SwitchScanTriggerInput.SoftwareTrigger through either the SwitchScan.ConfigureTrigger function or the SwitchScan.TriggerInput attribute, the scan does not proceed from a semicolon (wait for trigger) until SwitchScan.SendSoftwareTrigger is called. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForScanComplete | Pauses until the switch stops scanning or until the maximum time has elapsed, when NI-SWITCH returns a timeout error. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | AdvancedOutput | Gets or sets a value which specifies the method you want to use to notify another instrument that all signals going through the switch have settled following the processing of one entry in the SwitchScan.List. |
|  | AdvancedPolarity | Gets or sets the advance polarity for the scan. |
|  | Continuous | Gets or sets a value that indicates whether a switch device stops scanning at the end of the scan, or continues scanning from the top of the scan list. Notice that if you set the scan to continuous trueTruetruetrue (True in Visual Basic), the SwitchScan.WaitForScanComplete method will always time out and you must call SwitchScan.Abort to stop the scan. |
|  | Delay | Gets or sets a value which indicates the minimum amount of time, in seconds, the Switch device waits before it asserts the SwitchScan.AdvancedOutput trigger after opening or closing the switch. The switch always SwitchPath.WaitForDebounce before asserting the trigger. |
|  | DigitalFilterEnable | Gets or sets a value which indicates whether to apply the pulse width to the SwitchScan.TriggerInput. Set the property to trueTruetruetrue (True in Visual Basic) to prevent the switch module from being triggered by pulses that are less than 150 ns on PXI trigger lines 0-7. When this property is set to falseFalsefalsefalse (False in Visual Basic), noise on the PXI trigger lines might trigger the switch module. If the device triggering the switch module can send pulses greater than 150 ns, do not disable this property. |
|  | HandshakingInitiation | Gets or sets a value which specifies how to start handshaking with a measurement device. |
|  | IsScanning | Gets or sets a value which indicates whether the switch has completed the scan operation. The value trueTruetruetrue (True in Visual Basic) indicates that the scan is complete. |
|  | IsWaitingForTrigger | In a SwitchScan.List, a semicolon (;) is used to indicate that at that point in the SwitchScan.List, the scan engine should pause until a trigger is received from the SwitchScan.TriggerInput. If that trigger is user generated through either a hardware pulse or the SwitchScan.SendSoftwareTrigger method, it is necessary for the user to know when the scan engine has reached such a state. |
|  | List | This property contains a SwitchScan.List, which is a string that specifies channel connections and trigger conditions. The SwitchScan.Initiate function makes or breaks connections and waits for triggers according to the instructions in the SwitchScan.List. The SwitchScan.List is comprised of channel names that you separate with special characters. These special characters determine the operations the scanner performs on the channels when it executes this scan list. To create a path between two channels, use the following character between the two channel names: -> (a dash followed by a '>' sign) Example: "CH1->CH2" tells the switch to make a path from channel CH1 to channel CH2. To break or clear a path, use the following character as a prefix before the path: ~ (tilde) Example: "~CH1->CH2" tells the switch to break the path from channel CH1 to channel CH2. To create a path between two channels, use the following character between the two channel names: -> (a dash followed by a '>' sign) Example: "CH1->CH2" tells the switch to make a path from channel CH1 to channel CH2. To tell the switch device to create multiple paths simultaneously, use the following character as a separator between the paths: , (comma) Example: "A->B;CH1->CH2,CH3->CH4" instructs the scanner to make the path between channels A and B, wait for a trigger, and then simultaneously make the paths between channels CH1 and CH2 and between channels CH3 and CH4. |
|  | Mode | Specifies what happens to existing connections that conflict with the connections you make in a SwitchScan.List. For example, if CH1 is already connected to CH2 and the SwitchScan.List instructs the switch to connect CH1 to CH3, this attribute specifies what happens to the connection between CH1 and CH2. If the value of this attribute is SwitchScanMode.None, the switch takes no action on existing paths. If the value is SwitchScanMode.BreakBeforeMake, the switch breaks conflicting paths before making new ones. If the value is SwitchScanMode.BreakBeforeMake, the switch breaks conflicting paths after making new ones. Most switches support only one of the possible values. In such cases, this attribute serves as an indicator of the device's behavior. |
|  | TriggerInput | Gets or sets a value which specifies the source of the trigger for which the switch can wait when processing a SwitchScan.List. The switch waits for a trigger when it encounters a semicolon in a SwitchScan.List. When the trigger occurs, the switch advances to the next entry in the SwitchScan.List. |
|  | TriggerInputPolarity | Gets or sets a value which determines the behavior of the trigger input. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScan Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutput.htm language=enus -->
## TOPIC 00004: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutput.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutput.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanAdvancedOutput Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScanAdvancedOutput](t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutput.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | External | Gets a value for the external trigger. The switch waits until it receives a trigger from an external source through the external trigger input before processing the next entry in the scan list. |
|  | FrontConnector | Gets a value corresponding to the FrontConnector trigger. The switch waits until it receives a trigger on the front connector. |
|  | FrontConnectorModule1 | Gets a value corresponding to the FrontConnectorModule1 trigger. The switch waits until it receives a trigger on the front connector module 1. |
|  | FrontConnectorModule10 | Gets a value corresponding to the FrontConnectorModule10 trigger. The switch waits until it receives a trigger on the front connector module 10. |
|  | FrontConnectorModule11 | Gets a value corresponding to the FrontConnectorModule11 trigger. The switch waits until it receives a trigger on the front connector module 11. |
|  | FrontConnectorModule12 | Gets a value corresponding to the FrontConnectorModule12 trigger. The switch waits until it receives a trigger on the front connector module 12. |
|  | FrontConnectorModule2 | Gets a value corresponding to the FrontConnectorModule2 trigger. The switch waits until it receives a trigger on the front connector module 2. |
|  | FrontConnectorModule3 | Gets a value corresponding to the FrontConnectorModule3 trigger. The switch waits until it receives a trigger on the front connector module 3. |
|  | FrontConnectorModule4 | Gets a value corresponding to the FrontConnectorModule4 trigger. The switch waits until it receives a trigger on the front connector module 4. |
|  | FrontConnectorModule5 | Gets a value corresponding to the FrontConnectorModule5 trigger. The switch waits until it receives a trigger on the front connector module 5. |
|  | FrontConnectorModule6 | Gets a value corresponding to the FrontConnectorModule6 trigger. The switch waits until it receives a trigger on the front connector module 6. |
|  | FrontConnectorModule7 | Gets a value corresponding to the FrontConnectorModule10 trigger. The switch waits until it receives a trigger on the front connector module 7. |
|  | FrontConnectorModule8 | Gets a value corresponding to the FrontConnectorModule8 trigger. The switch waits until it receives a trigger on the front connector module 8. |
|  | FrontConnectorModule9 | Gets a value corresponding to the FrontConnectorModule10 trigger. The switch waits until it receives a trigger on the front connector module 9. |
|  | None | Gets a value that indicates no implicit action on scanning connections. |
|  | PxiStar | Gets a value corresponding to a trigger on the PXI star trigger bus before processing the next entry in the scan list. |
|  | RearConnector | Gets a value corresponding to the RearConnector trigger. The switch waits until it receives a trigger on the rear connector. |
|  | RearConnectorModule1 | Gets a value corresponding to the RearConnectorModule1 trigger. The switch waits until it receives a trigger on the rear connector module 1. |
|  | RearConnectorModule10 | Gets a value corresponding to the RearConnectorModule10 trigger.The switch waits until it receives a trigger on the rear connector module 10. |
|  | RearConnectorModule11 | Gets a value corresponding to the RearConnectorModule11 trigger.The switch waits until it receives a trigger on the rear connector module 11. |
|  | RearConnectorModule12 | Gets a value corresponding to the RearConnectorModule12 trigger. The switch waits until it receives a trigger on the rear connector module 12. |
|  | RearConnectorModule2 | Gets a value corresponding to the RearConnectorModule2 trigger.The switch waits until it receives a trigger on the rear connector module 2. |
|  | RearConnectorModule3 | Gets a value corresponding to the RearConnectorModule3 trigger. The switch waits until it receives a trigger on the rear connector module 3. |
|  | RearConnectorModule4 | Gets a value corresponding to the RearConnectorModule4 trigger. The switch waits until it receives a trigger on the rear connector module 4. |
|  | RearConnectorModule5 | Gets a value corresponding to the RearConnectorModule5 trigger. The switch waits until it receives a trigger on the rear connector module 5. |
|  | RearConnectorModule6 | Gets a value corresponding to the RearConnectorModule6 trigger. The switch waits until it receives a trigger on the rear connector module 6. |
|  | RearConnectorModule7 | Gets a value corresponding to the RearConnectorModule7 trigger. The switch waits until it receives a trigger on the rear connector module 7. |
|  | RearConnectorModule8 | Gets a value corresponding to the RearConnectorModule8 trigger. The switch waits until it receives a trigger on the rear connector module 8. |
|  | RearConnectorModule9 | Gets a value corresponding to the RearConnectorModule9 trigger. The switch waits until it receives a trigger on the rear connector module 9. |
|  | Ttl0 | Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list. |
|  | Ttl1 | Gets a value corresponding to a trigger on the PXI_TRIG1 line. The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list. |
|  | Ttl2 | Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list. |
|  | Ttl3 | Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list. |
|  | Ttl4 | Gets a value corresponding to a trigger on the PXI_TRIG4 line. The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list. |
|  | Ttl5 | Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. |
|  | Ttl6 | Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list. |
|  | Ttl7 | Gets a value corresponding to a trigger on the PXI_TRIG7 line. The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the scan list. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanAdvancedOutput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline.htm language=enus -->
## TOPIC 00005: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanAdvancedOutputBusLine Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScanAdvancedOutputBusLine](t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | None | Gets a value that indicates no implicit action on scanning connections. |
|  | Ttl0 | Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list. |
|  | Ttl1 | Gets a value corresponding to a trigger on the PXI_TRIG1 line. The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list. |
|  | Ttl2 | Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list. |
|  | Ttl3 | Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list. |
|  | Ttl4 | Gets a value corresponding to a trigger on the PXI_TRIG4 line. The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list. |
|  | Ttl5 | Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. |
|  | Ttl6 | Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list. |
|  | Ttl7 | Gets a value corresponding to a trigger on the PXI_TRIG7 line. The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the scan list. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanAdvancedOutputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputconnector.htm language=enus -->
## TOPIC 00006: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputconnector.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputconnector.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanAdvancedOutputConnector Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScanAdvancedOutputConnector](t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputconnector.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | FrontConnector | Gets a value corresponding to a trigger on the front connector. |
|  | RearConnector | Gets a value corresponding to a trigger on the rear connector. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanAdvancedOutputConnector Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput.htm language=enus -->
## TOPIC 00007: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanTriggerInput Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScanTriggerInput](t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | External | Gets a value corresponding to a trigger from an external source through the external trigger input before processing the next entry in the scan list. |
|  | FrontConnector | Gets a value corresponding to a trigger on the front connector. |
|  | FrontConnectorModule1 | Gets a value corresponding to a trigger on the front connector module 1. |
|  | FrontConnectorModule10 | Gets a value corresponding to a trigger on the front connector module 10. |
|  | FrontConnectorModule11 | Gets a value corresponding to a trigger on the front connector module 11. |
|  | FrontConnectorModule12 | Gets a value corresponding to a trigger on the front connector module 12. |
|  | FrontConnectorModule2 | Gets a value corresponding to a trigger on the front connector module 2. |
|  | FrontConnectorModule3 | Gets a value corresponding to a trigger on the front connector module 3. |
|  | FrontConnectorModule4 | Gets a value corresponding to a trigger on the front connector module 4. |
|  | FrontConnectorModule5 | Gets a value corresponding to a trigger on the front connector module 5. |
|  | FrontConnectorModule6 | Gets a value corresponding to a trigger on the front connector module 6. |
|  | FrontConnectorModule7 | Gets a value corresponding to a trigger on the front connector module 7. |
|  | FrontConnectorModule8 | Gets a value corresponding to a trigger on the front connector module 8. |
|  | FrontConnectorModule9 | Gets a value corresponding to a trigger on the front connector module 9. |
|  | Immediate | Gets a value corresponding to an immediate trigger. The switch does not wait for a trigger before processing the next entry in the scan list. |
|  | PxiStar | Gets a value corresponding to a trigger on the PXI star trigger bus before processing the next entry in the scan list. |
|  | RearConnector | Gets a value corresponding to a trigger on the rear connector. |
|  | RearConnectorModule1 | Gets a value corresponding to a trigger on the rear connector module 1. |
|  | RearConnectorModule10 | Gets a value corresponding to a trigger on the rear connector module 10. |
|  | RearConnectorModule11 | Gets a value corresponding to a trigger on the rear connector module 11. |
|  | RearConnectorModule12 | Gets a value corresponding to a trigger on the rear connector module 12. |
|  | RearConnectorModule2 | Gets a value corresponding to a trigger on the rear connector module 2. |
|  | RearConnectorModule3 | Gets a value corresponding to a trigger on the rear connector module 3. |
|  | RearConnectorModule4 | Gets a value corresponding to a trigger on the rear connector module 4. |
|  | RearConnectorModule5 | Gets a value corresponding to a trigger on the rear connector module 5. |
|  | RearConnectorModule6 | Gets a value corresponding to a trigger on the rear connector module 6. |
|  | RearConnectorModule7 | Gets a value corresponding to a trigger on the rear connector module 7. |
|  | RearConnectorModule8 | Gets a value corresponding to a trigger on the rear connector module 8. |
|  | RearConnectorModule9 | Gets a value corresponding to a trigger on the rear connector module 9. |
|  | SoftwareTrigger | Gets a value which indicates that the switch waits until you call the SwitchScan.SendSoftwareTrigger method before processing the next entry in the scan list. |
|  | Ttl0 | Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list. |
|  | Ttl1 | Gets a value corresponding to a trigger on the PXI_TRIG1 line. The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list. |
|  | Ttl2 | Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list. |
|  | Ttl3 | Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list. |
|  | Ttl4 | Gets a value corresponding to a trigger on the PXI_TRIG4line. The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list. |
|  | Ttl5 | Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. |
|  | Ttl6 | Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list. |
|  | Ttl7 | Gets a value corresponding to a trigger on the PXI_TRIG7 line. The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the scan list. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline.htm language=enus -->
## TOPIC 00008: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanTriggerInputBusLine Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScanTriggerInputBusLine](t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | None | Gets a value which indicates no implicit action on connections when scanning. |
|  | Ttl0 | Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list. |
|  | Ttl1 | Gets a value corresponding to a trigger on the PXI_TRIG1 line. The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list. |
|  | Ttl2 | Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list. |
|  | Ttl3 | Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list. |
|  | Ttl4 | Gets a value corresponding to a trigger on the PXI_TRIG4 line. The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list. |
|  | Ttl5 | Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. |
|  | Ttl6 | Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list. |
|  | Ttl7 | Gets a value corresponding to a trigger on the PXI_TRIG7 line. The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the scan list. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputconnector.htm language=enus -->
## TOPIC 00009: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputconnector.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputconnector.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanTriggerInputConnector Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScanTriggerInputConnector](t_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputconnector.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | FrontConnector | Gets a value corresponding to a trigger on the front connector. |
|  | RearConnector | Gets a value corresponding to a trigger on the rear connector. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInputConnector Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchsubobject.htm language=enus -->
## TOPIC 00010: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchsubobject.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchsubobject.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchSubObject Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchSubObject](t_nationalinstruments_modularinstruments_niswitch_switchsubobject.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchSubObject Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchwarning.htm language=enus -->
## TOPIC 00011: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchwarning.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchwarning.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchWarning Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchWarning](t_nationalinstruments_modularinstruments_niswitch_switchwarning.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Overloaded. Determines whether the current instance of NISwitch.SwitchWarning and the NISwitch.SwitchWarning object that you specify are equal. |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Returns the hash code for the current instance of NISwitch.SwitchWarning. (Overrides Object..::.GetHashCode()()().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Converts the current instance of NISwitch.SwitchWarning to string. (Overrides Object..::.ToString()()().) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Checks whether the two instances of NISwitch.SwitchWarning are equal. |
|  | Inequality | Checks whether the two instances of NISwitch.SwitchWarning are unequal. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Code | Gets the GUID code assigned to the warning. |
|  | ImplicitConnectionExistsWarningCode | Gets the warning code if the path between the channels is not available, the channels are not explicitly connected, but the implicit connection exists between them. |
|  | Message | Gets the message related to the warning. |
|  | PathRemainsWarningCode | Gets the warning code if the card is not capable of removing all paths and always leaves at least one connected. |
|  | UnexpectedDriverWarningCode | Gets the warning code for an unexpected driver warning. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchWarning Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs.htm language=enus -->
## TOPIC 00012: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/allmembers_t_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchWarningEventArgs Members

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchWarningEventArgs](t_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Code | Gets the Warning Event Args code. |
|  | Message | Gets the Warning Event Args message. |
|  | Warning | Gets the warning set in the Warning Event Args. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchWarningEventArgs Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_coercion.htm language=enus -->
## TOPIC 00013: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_coercion.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_coercion.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Coercion Event

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Occurs when the NI-SWITCH driver creates a coercion warning.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Event Coercion As EventHandler(Of SwitchCoercionWarningEventArgs) |

| C# |
| --- |
| public event EventHandler<SwitchCoercionWarningEventArgs> Coercion |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_interchangecheckwarning.htm language=enus -->
## TOPIC 00014: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_interchangecheckwarning.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_interchangecheckwarning.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

InterchangeCheckWarning Event

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Occurs when the NI-SWITCH driver creates a interchange warning.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Event InterchangeCheckWarning As EventHandler(Of SwitchInterchangeCheckWarningEventArgs) |

| C# |
| --- |
| public event EventHandler<SwitchInterchangeCheckWarningEventArgs> InterchangeCheckWarning |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_coercion.htm language=enus -->
## TOPIC 00015: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_coercion.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_coercion.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IIviDriverOperation.Coercion Event

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Coercion record event.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Private Event Coercion As EventHandler(Of CoercionEventArgs) Implements IIviDriverOperation.Coercion |

| C# |
| --- |
| event EventHandler<CoercionEventArgs> IIviDriverOperation.Coercion |

###### Implements

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_interchangecheckwarning.htm language=enus -->
## TOPIC 00016: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_interchangecheckwarning.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_interchangecheckwarning.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IIviDriverOperation.InterchangeCheckWarning Event

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Interchange check warning event.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Private Event InterchangeCheckWarning As EventHandler(Of InterchangeCheckWarningEventArgs) Implements IIviDriverOperation.InterchangeCheckWarning |

| C# |
| --- |
| event EventHandler<InterchangeCheckWarningEventArgs> IIviDriverOperation.InterchangeCheckWarning |

###### Implements

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_warning.htm language=enus -->
## TOPIC 00017: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_warning.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_ivi_driver_iividriveroperation_warning.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IIviDriverOperation.Warning Event

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Warning event.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Private Event Warning As EventHandler(Of WarningEventArgs) Implements IIviDriverOperation.Warning |

| C# |
| --- |
| event EventHandler<WarningEventArgs> IIviDriverOperation.Warning |

###### Implements

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_warning.htm language=enus -->
## TOPIC 00018: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_warning.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/e_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_warning.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Warning Event

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Occurs when the NI-SWITCH driver creates a driver warning.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Event Warning As EventHandler(Of SwitchWarningEventArgs) |

| C# |
| --- |
| public event EventHandler<SwitchWarningEventArgs> Warning |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/events_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm language=enus -->
## TOPIC 00019: Events

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/events_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/events_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchDriverOperation Events

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchDriverOperation](t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Events

|  | Name | Description |
| --- | --- | --- |
|  | Coercion | Occurs when the NI-SWITCH driver creates a coercion warning. |
|  | InterchangeCheckWarning | Occurs when the NI-SWITCH driver creates a interchange warning. |
|  | Warning | Occurs when the NI-SWITCH driver creates a driver warning. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Explicit Interface Implementations

|  | Name | Description |
| --- | --- | --- |
|  | IIviDriverOperation..::.Coercion | Coercion record event. |
|  | IIviDriverOperation..::.InterchangeCheckWarning | Interchange check warning event. |
|  | IIviDriverOperation..::.Warning | Warning event. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor.htm language=enus -->
## TOPIC 00020: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

NISwitch Constructor (IntPtr)

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Creates a new instrument driver session from an existing instrument handle.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ instrumentHandle As IntPtr _ ) |

| C# |
| --- |
| public NISwitch( IntPtr instrumentHandle ) |

###### Parameters

- **instrumentHandle**
  - Type: System..::.IntPtrSpecifies the pre-existing instrument handle used to create a new instrument driver session.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_1.htm language=enus -->
## TOPIC 00021: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_1.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

NISwitch Constructor (String, Boolean, Boolean)

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Creates a new instrument driver session.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ resourceName As String, _ idQuery As Boolean, _ resetDevice As Boolean _ ) |

| C# |
| --- |
| public NISwitch( string resourceName, bool idQuery, bool resetDevice ) |

###### Parameters

- **resourceName**
  - Type: System..::.String Specifies the name of the device in which the session is opened.

- **idQuery**
  - Type: System..::.Boolean Valid Values: trueTruetruetrue (True in Visual Basic) - (default value) falseFalsefalsefalse (False in Visual Basic) - Currently unsupported.

- **resetDevice**
  - Type: System..::.Boolean trueTruetruetrue (True in Visual Basic) - Reset device (default value) falseFalsefalsefalse (False in Visual Basic) - Currently unsupported. The device will not reset.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_2.htm language=enus -->
## TOPIC 00022: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_2.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

NISwitch Constructor (String, Boolean, Boolean, String)

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Creates a new instrument driver session and sets the initial state of session properties.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ resourceName As String, _ idQuery As Boolean, _ resetDevice As Boolean, _ optionString As String _ ) |

| C# |
| --- |
| public NISwitch( string resourceName, bool idQuery, bool resetDevice, string optionString ) |

###### Parameters

- **resourceName**
  - Type: System..::.String Specifies the name of the device in which the session is opened.

- **idQuery**
  - Type: System..::.Boolean Valid Values: trueTruetruetrue (True in Visual Basic) - (Default Value) falseFalsefalsefalse (False in Visual Basic) - Currently unsupported.

- **resetDevice**
  - Type: System..::.Boolean trueTruetruetrue (True in Visual Basic) - Reset Device (Default Value) falseFalsefalsefalse (False in Visual Basic) - Currently unsupported. The device will not reset.

- **optionString**
  - Type: System..::.String Sets the initial state of the following session properties: SwitchDriverOperation.RangeCheck, SwitchDriverOperation.QueryInstrumentStatus, SwitchDriverOperation.Cache , SwitchDriverOperation.Simulate , SwitchDriverOperation.RecordCoercions , SwitchDriverOperation.DriverSetup.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_3.htm language=enus -->
## TOPIC 00023: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch__ctor_3.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

NISwitch Constructor (String, String, Boolean, Boolean)

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Creates a new instrument driver session and sets the topology of device.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ resourceName As String, _ topology As String, _ simulate As Boolean, _ resetDevice As Boolean _ ) |

| C# |
| --- |
| public NISwitch( string resourceName, string topology, bool simulate, bool resetDevice ) |

###### Parameters

- **resourceName**
  - Type: System..::.String Specifies the name of the device in which the session is opened.

- **topology**
  - Type: System..::.String Pass the topology name you want to use for the switch you specify with the resourceName parameter. All the valid values are defined in NISwitch.SwitchDeviceTopology.

- **simulate**
  - Type: System..::.Boolean Enables simulation of the switch module specified in the resourceName parameter. trueTruetruetrue (True in Visual Basic) Simulate. falseFalsefalsefalse (False in Visual Basic)(default) Do not simulate.

- **resetDevice**
  - Type: System..::.Boolean Specifies whether to reset the switch module during the initialization process. trueTruetruetrue (True in Visual Basic) (default) Reset device. falseFalsefalsefalse (False in Visual Basic) The device will not reset.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_close.htm language=enus -->
## TOPIC 00024: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_close.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_close.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Close Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Closes the session to the device.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Close |

| C# |
| --- |
| public void Close() |

###### Implements

.

.

::

.

()

()

()

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_dangerousgetinstrumenthandle.htm language=enus -->
## TOPIC 00025: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_dangerousgetinstrumenthandle.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_dangerousgetinstrumenthandle.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DangerousGetInstrumentHandle Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the value of the underlying instrument handle.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function DangerousGetInstrumentHandle As IntPtr |

| C# |
| --- |
| public IntPtr DangerousGetInstrumentHandle() |

###### Return Value

.

.

::

.

IntPtr

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The DangerousGetInstrumentHandle method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_dispose.htm language=enus -->
## TOPIC 00026: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_dispose.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Dispose Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Closes the specified session and deallocates the reserved resources, if not already disposed.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Dispose |

| C# |
| --- |
| public void Dispose() |

###### Implements

.

.

::

.

()

()

()

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

A call to this method disposes the **SafeHandle** class used to hold the instrument handle. If the call to this method fails due to some reason, like the session being closed by some external means, you will not be notified about the failure.
 To help you identify failures in the **ReleaseHandle** method of the **SafeHandle** class, managed debugging assistant (MDA) is activated.

For details refer to [http://msdn.microsoft.com/en-us/library/85eak4a0.aspx](http://msdn.microsoft.com/en-us/library/85eak4a0.aspx).

The call to this method fails when you externally close a session by:

- Initializing a session with a resource name for which the session is already open, within the same process. This causes the instrument handle held by the existing session to become invalid.
- Getting the instrument handle out using the DangerousGetInstrumentHandle method and closing this handle directly.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_getservice.htm language=enus -->
## TOPIC 00027: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_getservice.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_niswitch_getservice.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

GetService Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns a service object on the basis of the type mentioned in the serviceType parameter.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetService ( _ serviceType As Type _ ) As Object |

| C# |
| --- |
| public Object GetService( Type serviceType ) |

###### Parameters

- **serviceType**
  - Type: System..::.Type The type of the object to be retrieved.

###### Return Value

.

.

::

.

###### Implements

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The NISwitch.GetService method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveridentity_getsupportedinstrumentmodels.htm language=enus -->
## TOPIC 00028: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveridentity_getsupportedinstrumentmodels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveridentity_getsupportedinstrumentmodels.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

GetSupportedInstrumentModels Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns a list of names of instrument models with which the IVI-specific driver is compatible.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetSupportedInstrumentModels As String() |

| C# |
| --- |
| public string[] GetSupportedInstrumentModels() |

###### Return Value

array<

.

.

::

.

>

[]

()

[]

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The GetSupportedInstrumentModels method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverIdentity Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverlock_system_idisposable_dispose.htm language=enus -->
## TOPIC 00029: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverlock_system_idisposable_dispose.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverlock_system_idisposable_dispose.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IDisposable.Dispose Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Private Sub Dispose Implements IDisposable.Dispose |

| C# |
| --- |
| void IDisposable.Dispose() |

###### Implements

.

.

::

.

()

()

()

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverLock Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverlock_unlock.htm language=enus -->
## TOPIC 00030: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverlock_unlock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverlock_unlock.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Unlock Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Releases a driver synchronization lock.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Unlock |

| C# |
| --- |
| public void Unlock() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverLock Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_invalidateallattributes.htm language=enus -->
## TOPIC 00031: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_invalidateallattributes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_invalidateallattributes.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

InvalidateAllAttributes Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Invalidates all properties.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub InvalidateAllAttributes |

| C# |
| --- |
| public void InvalidateAllAttributes() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The InvalidateAllAttributes method was accessed after the associated NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_resetinterchangecheck.htm language=enus -->
## TOPIC 00032: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_resetinterchangecheck.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_resetinterchangecheck.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ResetInterchangeCheck Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Determines whether the test module has dependencies on the operation of previously executed test modules.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub ResetInterchangeCheck |

| C# |
| --- |
| public void ResetInterchangeCheck() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The ResetInterchangeCheck method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

The interchangeability checking algorithms in the specific driver ignore all previous configuration operations, after calling the function.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_errorquery.htm language=enus -->
## TOPIC 00033: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_errorquery.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_errorquery.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ErrorQuery Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Reads an error code and a message from the instrument error queue.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function ErrorQuery As ErrorQueryResult |

| C# |
| --- |
| public ErrorQueryResult ErrorQuery() |

###### Return Value

.

.

::

.

ErrorQueryResult

###### Implements

.

.

::

.

()

()

()

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The ErrorQuery method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

NI-SWITCH does not have an error queue, so this method never returns any errors.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverUtility Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_reset.htm language=enus -->
## TOPIC 00034: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_reset.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_reset.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Reset Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Disconnects all created paths and returns the switch module to the initialization state.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Reset |

| C# |
| --- |
| public void Reset() |

###### Implements

.

.

::

.

()

()

()

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The Reset method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Configuration channel and source channel settings remain unchanged.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverUtility Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_resetwithdefaults.htm language=enus -->
## TOPIC 00035: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_resetwithdefaults.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchdriverutility_resetwithdefaults.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ResetWithDefaults Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Reset

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub ResetWithDefaults |

| C# |
| --- |
| public void ResetWithDefaults() |

###### Implements

.

.

::

.

()

()

()

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The ResetWithDefaults method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverUtility Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchpath_waitfordebounce.htm language=enus -->
## TOPIC 00036: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchpath_waitfordebounce.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchpath_waitfordebounce.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

WaitForDebounce Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Pauses until all created paths have settled.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub WaitForDebounce ( _ maximumTime As PrecisionTimeSpan _ ) |

| C# |
| --- |
| public void WaitForDebounce( PrecisionTimeSpan maximumTime ) |

###### Parameters

- **maximumTime**
  - Type: NationalInstruments..::.PrecisionTimeSpan Specifies the maximum length of time to wait for all relays in the switch module to activate or deactivate.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| Ivi.Driver.MaxTimeExceededException | maximumTime parameter elapses before the switch paths settle |
| ObjectDisposedException | The WaitForDebounce was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchPath Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrelayoperations_getrelaycount.htm language=enus -->
## TOPIC 00037: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrelayoperations_getrelaycount.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrelayoperations_getrelaycount.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

GetRelayCount Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the number of times the relay has changed from closed to open.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetRelayCount ( _ relayName As String _ ) As Integer |

| C# |
| --- |
| public int GetRelayCount( string relayName ) |

###### Parameters

- **relayName**
  - Type: System..::.String The name of the relay.

###### Return Value

.

.

::

.

Int32

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The GetRelayCount method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

WaitForDebounce

GetRelayCount

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRelayOperations Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrelayoperations_getrelayname.htm language=enus -->
## TOPIC 00038: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrelayoperations_getrelayname.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrelayoperations_getrelayname.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

GetRelayName Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns the relay name string that is in the relay list at the specified index.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetRelayName ( _ index As Integer _ ) As String |

| C# |
| --- |
| public string GetRelayName( int index ) |

###### Parameters

- **index**
  - Type: System..::.Int32 A 1-based index into the channel table. The default value is 1. The maximum value is the value of the NumberOfRelays property.

###### Return Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The GetRelayName method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRelayOperations Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_equals.htm language=enus -->
## TOPIC 00039: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_equals.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Equals Method (SwitchRevisionQueryResult)

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SwitchRevisionQueryResult

SwitchRevisionQueryResult

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Equals ( _ result As SwitchRevisionQueryResult _ ) As Boolean |

| C# |
| --- |
| public bool Equals( SwitchRevisionQueryResult result ) |

###### Parameters

- **result**
  - Type: NationalInstruments.ModularInstruments.NISwitch..::.SwitchRevisionQueryResultThe SwitchRevisionQueryResult object to be compared to the current instance of SwitchRevisionQueryResult to be compared.

###### Return Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_gethashcode.htm language=enus -->
## TOPIC 00040: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_gethashcode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_gethashcode.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

GetHashCode Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SwitchRevisionQueryResult

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function GetHashCode As Integer |

| C# |
| --- |
| public override int GetHashCode() |

###### Return Value

.

.

::

.

Int32

SwitchRevisionQueryResult

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_op_equality.htm language=enus -->
## TOPIC 00041: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_op_equality.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_op_equality.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Equality Operator

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SwitchRevisionQueryResult

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared Operator = ( _ result1 As SwitchRevisionQueryResult, _ result2 As SwitchRevisionQueryResult _ ) As Boolean |

| C# |
| --- |
| public static bool operator ==( SwitchRevisionQueryResult result1, SwitchRevisionQueryResult result2 ) |

###### Parameters

- **result1**
  - Type: NationalInstruments.ModularInstruments.NISwitch..::.SwitchRevisionQueryResultA SwitchRevisionQueryResult object.

- **result2**
  - Type: NationalInstruments.ModularInstruments.NISwitch..::.SwitchRevisionQueryResult A SwitchRevisionQueryResult object.

###### Return Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_op_inequality.htm language=enus -->
## TOPIC 00042: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_op_inequality.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_op_inequality.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Inequality Operator

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SwitchRevisionQueryResult

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared Operator <> ( _ result1 As SwitchRevisionQueryResult, _ result2 As SwitchRevisionQueryResult _ ) As Boolean |

| C# |
| --- |
| public static bool operator !=( SwitchRevisionQueryResult result1, SwitchRevisionQueryResult result2 ) |

###### Parameters

- **result1**
  - Type: NationalInstruments.ModularInstruments.NISwitch..::.SwitchRevisionQueryResultA SwitchRevisionQueryResult object.

- **result2**
  - Type: NationalInstruments.ModularInstruments.NISwitch..::.SwitchRevisionQueryResultA SwitchRevisionQueryResult object.

###### Return Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_abort.htm language=enus -->
## TOPIC 00043: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_abort.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_abort.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Abort Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SwitchScan.Initiate

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Abort |

| C# |
| --- |
| public void Abort() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| Ivi.Swtch.NoScanInProgressException | This exception is used when the driver expects that the switch is currently scanning through the scan list, but it is not. |
| ObjectDisposedException | The Abort method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScan Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_commit.htm language=enus -->
## TOPIC 00044: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_commit.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_commit.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Commit Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SwitchScan.List

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Commit |

| C# |
| --- |
| public void Commit() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The Commit method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Calling this method is optional.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScan Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_waitforscancomplete.htm language=enus -->
## TOPIC 00045: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_waitforscancomplete.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/m_nationalinstruments_modularinstruments_niswitch_switchscan_waitforscancomplete.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

WaitForScanComplete Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Pauses until the switch stops scanning or until the maximum time has elapsed, when NI-SWITCH returns a timeout error.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub WaitForScanComplete ( _ maximumTime As PrecisionTimeSpan _ ) |

| C# |
| --- |
| public void WaitForScanComplete( PrecisionTimeSpan maximumTime ) |

###### Parameters

- **maximumTime**
  - Type: NationalInstruments..::.PrecisionTimeSpanSpecifies the maximum length of time to wait for the switch module to stop scanning. If the specified time elapses before the scan ends, a MaxTimeExceededException is returned. The default value is 5000 ms.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| Ivi.Driver.MaxTimeExceededException | The operation implemented by the method did not complete within the maximum time allowed. |
| ObjectDisposedException | The WaitForScanComplete method was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScan Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_niswitch.htm language=enus -->
## TOPIC 00046: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_niswitch.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_niswitch.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

NISwitch Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [NISwitch](t_nationalinstruments_modularinstruments_niswitch_niswitch.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Close | Closes the session to the device. |
|  | DangerousGetInstrumentHandle | Returns the value of the underlying instrument handle. |
|  | Dispose | Closes the specified session and deallocates the reserved resources, if not already disposed. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetService | Returns a service object on the basis of the type mentioned in the serviceType parameter. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchchannel.htm language=enus -->
## TOPIC 00047: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchchannel.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchChannel](t_nationalinstruments_modularinstruments_niswitch_switchchannel.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannel Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchchannelcollection.htm language=enus -->
## TOPIC 00048: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchchannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchchannelcollection.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannelCollection Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchChannelCollection](t_nationalinstruments_modularinstruments_niswitch_switchchannelcollection.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannelCollection Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchcharacteristics.htm language=enus -->
## TOPIC 00049: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchcharacteristics.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchcharacteristics.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchCharacteristics Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchCharacteristics](t_nationalinstruments_modularinstruments_niswitch_switchcharacteristics.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchCharacteristics Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs.htm language=enus -->
## TOPIC 00050: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchCoercionWarningEventArgs Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchCoercionWarningEventArgs](t_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchCoercionWarningEventArgs Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriveridentity.htm language=enus -->
## TOPIC 00051: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriveridentity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriveridentity.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchDriverIdentity Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchDriverIdentity](t_nationalinstruments_modularinstruments_niswitch_switchdriveridentity.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetGroupCapabilities | Returns a list of names of class capability groups that the IVI-specific driver implements. |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetSupportedInstrumentModels | Returns a list of names of instrument models with which the IVI-specific driver is compatible. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverIdentity Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriverlock.htm language=enus -->
## TOPIC 00052: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriverlock.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriverlock.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchDriverLock Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchDriverLock](t_nationalinstruments_modularinstruments_niswitch_switchdriverlock.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | Unlock | Releases a driver synchronization lock. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Explicit Interface Implementations

|  | Name | Description |
| --- | --- | --- |
|  | IDisposable..::.Dispose | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverLock Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm language=enus -->
## TOPIC 00053: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchDriverOperation Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchDriverOperation](t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Dispose | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InvalidateAllAttributes | Invalidates all properties. |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ResetInterchangeCheck | Determines whether the test module has dependencies on the operation of previously executed test modules. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriverutility.htm language=enus -->
## TOPIC 00054: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriverutility.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchdriverutility.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchDriverUtility Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchDriverUtility](t_nationalinstruments_modularinstruments_niswitch_switchdriverutility.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Disable | Places the instrument in a quiescent state as quickly as possible. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | ErrorQuery | Reads an error code and a message from the instrument error queue. |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | Lock | Overloaded. Acquires a synchronization lock on this instance of the NI-SWITCH driver. |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | Reset | Disconnects all created paths and returns the switch module to the initialization state. |
|  | ResetWithDefaults | Resets the switch module and applies initial settings from the logical name which you used to initialize the session. If the session was created without a logical name, this method is equivalent to Reset. |
|  | RevisionQuery | Returns the revision number of the NI-SWITCH driver. |
|  | SelfTest | Verifies that NI-SWITCH device can communicate with the switch. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverUtility Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switcherrorqueryresult.htm language=enus -->
## TOPIC 00055: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switcherrorqueryresult.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switcherrorqueryresult.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchErrorQueryResult Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchErrorQueryResult](t_nationalinstruments_modularinstruments_niswitch_switcherrorqueryresult.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Overloaded. Determines whether the current instance of NISwitch.SwitchErrorQueryResult and the user specified NISwitch.SwitchErrorQueryResult object are equal. |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Returns the hash code for the current instance of NISwitch.SwitchErrorQueryResult. (Overrides ValueType..::.GetHashCode()()().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Checks whether the two instances of NISwitch.SwitchErrorQueryResult are equal. |
|  | Inequality | Checks whether the two instances of NISwitch.SwitchErrorQueryResult are unequal. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchErrorQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchinterchangecheckwarningeventargs.htm language=enus -->
## TOPIC 00056: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchinterchangecheckwarningeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchinterchangecheckwarningeventargs.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchInterchangeCheckWarningEventArgs Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchInterchangeCheckWarningEventArgs](t_nationalinstruments_modularinstruments_niswitch_switchinterchangecheckwarningeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchInterchangeCheckWarningEventArgs Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics.htm language=enus -->
## TOPIC 00057: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchModuleCharacteristics Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchModuleCharacteristics](t_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchModuleCharacteristics Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchpath.htm language=enus -->
## TOPIC 00058: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchpath.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchpath.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchPath Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchPath](t_nationalinstruments_modularinstruments_niswitch_switchpath.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | CanConnect | Verifies that you can create a path between channel1 and channel2. |
|  | Connect | Creates a path between channel1 and channel2. |
|  | ConnectMultiple | Creates connections between the channels that you specify in connectionList. Specify connections with two endpoints only or the explicit path between two endpoints. |
|  | Disconnect | Destroys the path between two channels that you create using the Connect or SetPath methods. |
|  | DisconnectAll | Breaks all existing paths. |
|  | DisconnectMultiple | Breaks the connections between channels specified in disconnection list. If no connections exist between channels, NI-SWITCH returns an error. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetPath | Returns a String that identifies the explicit path created with Connect. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | SetPath | Connects two channels by specifying an explicit path in the pathList parameter, which is an array of String with the source channel as the first element and the destination channel as the next element. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForDebounce | Pauses until all created paths have settled. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchPath Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchrelayoperations.htm language=enus -->
## TOPIC 00059: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchrelayoperations.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchrelayoperations.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchRelayOperations Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchRelayOperations](t_nationalinstruments_modularinstruments_niswitch_switchrelayoperations.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetRelayCount | Returns the number of times the relay has changed from closed to open. |
|  | GetRelayName | Returns the relay name string that is in the relay list at the specified index. |
|  | GetRelayPosition | Returns the relay position for the relay specified in the relayName parameter. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RelayControl | Controls individual relays of the switch. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRelayOperations Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm language=enus -->
## TOPIC 00060: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchRevisionQueryResult Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchRevisionQueryResult](t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Overloaded. Determines whether the current instance of SwitchRevisionQueryResult and the SwitchRevisionQueryResult object that you specify are equal. |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Returns the hash code for SwitchRevisionQueryResult. (Overrides ValueType..::.GetHashCode()()().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Checks whether the two instances of SwitchRevisionQueryResult are equal. |
|  | Inequality | Checks whether the two instances of SwitchRevisionQueryResult are unequal. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchscan.htm language=enus -->
## TOPIC 00061: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchscan.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchscan.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScan Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScan](t_nationalinstruments_modularinstruments_niswitch_switchscan.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Abort | Aborts the scan in progress. Initiate a scan with SwitchScan.Initiate. If the switch module is not scanning, exception is returned. |
|  | Commit | Downloads the configured SwitchScan.List and trigger settings to hardware. |
|  | ConfigureList | Configures the SwitchScan.List and SwitchScan.Mode used for scanning. Refer to Switch Device Help to determine if the switch module supports scanning. The SwitchScan.List is comprised of a list of channel connections separated by semicolons. For example, the following scan list will scan the first three channels of a multiplexer: com0->ch0; com0->ch1; com0->ch2; Refer to SwitchScan.List for more information on scan list syntax. To see the status of the scan, call either SwitchScan.IsScanning or SwitchScan.WaitForScanComplete. Use the SwitchScan.ConfigureTrigger method to configure the scan trigger. Use the SwitchScan.Initiate method to start the scan. |
|  | ConfigureTrigger | Configures the scan triggers for the scan list established with SwitchScan.ConfigureList. Refer to Device Help to determine if the switch module supports scanning. SwitchScan.ConfigureTrigger sets the location that the switch expects to receive an input trigger to advance through the SwitchScan.List. This method also sets the location where it outputs a scan advanced signal after it completes an entry in the scan list. |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | Initiate | Commits the configured SwitchScan.List and trigger settings to hardware and initiates the scan. If SwitchScan.Commit was called earlier, SwitchScan.Initiate only initiates the scan and returns immediately. Once the scanning operation begins, you cannot perform any other operation other than GetAttribute, SwitchScan.Abort, or SwitchScan.SendSoftwareTrigger. All other functions return the Exception. To stop the scanning operation, call SwitchScan.Abort. |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | RouteScanAdvancedOutput | Routes the SwitchScan.AdvancedOutput from a trigger bus line (TTLx) to the front or rear connector. |
|  | RouteTriggerInput | Routes the SwitchScan.TriggerInput from the front or rear connector to a trigger bus line (TTLx). To disconnect the route, call this function again and specify SwitchScanTriggerInputBusLine.None for trigger bus line parameter. |
|  | Scan | Takes the SwitchScan.List provided, programs the switching hardware and initiates the scan. Once initiation is complete, the operation will return. |
|  | SendSoftwareTrigger | Sends a software trigger to the switch specified in the NI-SWITCH session. When the SwitchScan.TriggerInput is set to SwitchScanTriggerInput.SoftwareTrigger through either the SwitchScan.ConfigureTrigger function or the SwitchScan.TriggerInput attribute, the scan does not proceed from a semicolon (wait for trigger) until SwitchScan.SendSoftwareTrigger is called. |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |
|  | WaitForScanComplete | Pauses until the switch stops scanning or until the maximum time has elapsed, when NI-SWITCH returns a timeout error. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScan Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchsubobject.htm language=enus -->
## TOPIC 00062: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchsubobject.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchsubobject.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchSubObject Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchSubObject](t_nationalinstruments_modularinstruments_niswitch_switchsubobject.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchSubObject Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchwarning.htm language=enus -->
## TOPIC 00063: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchwarning.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchwarning.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchWarning Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchWarning](t_nationalinstruments_modularinstruments_niswitch_switchwarning.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Overloaded. Determines whether the current instance of NISwitch.SwitchWarning and the NISwitch.SwitchWarning object that you specify are equal. |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Returns the hash code for the current instance of NISwitch.SwitchWarning. (Overrides Object..::.GetHashCode()()().) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Converts the current instance of NISwitch.SwitchWarning to string. (Overrides Object..::.ToString()()().) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Checks whether the two instances of NISwitch.SwitchWarning are equal. |
|  | Inequality | Checks whether the two instances of NISwitch.SwitchWarning are unequal. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchWarning Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs.htm language=enus -->
## TOPIC 00064: Methods

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/methods_t_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchWarningEventArgs Methods

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchWarningEventArgs](t_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified Object is equal to the current Object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as a hash function for a particular type. (Inherited from Object.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchWarningEventArgs Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/overload_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_equals.htm language=enus -->
## TOPIC 00065: Overload List

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/overload_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_equals.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/overload_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_equals.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Equals Method

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

### [IMAGE alt='image' src='../icons/collapse_all.gif']Overload List

|  | Name | Description |
| --- | --- | --- |
|  | Equals(SwitchRevisionQueryResult) | Determines whether the current instance of SwitchRevisionQueryResult and the SwitchRevisionQueryResult object that you specify are equal. |
|  | Equals(Object) | Determines whether this instance of SwitchRevisionQueryResult and the object that you specify are equal. (Overrides ValueType..::.Equals(Object).) |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

SwitchRevisionQueryResult Members

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_channels.htm language=enus -->
## TOPIC 00066: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_channels.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_channels.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Channels Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

NISwitch.SwitchChannelCollection

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property Channels As SwitchChannelCollection |

| C# |
| --- |
| public SwitchChannelCollection Channels { get; } |

###### Property Value

.

.

::

.

NISwitch.SwitchChannelCollection

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_isdisposed.htm language=enus -->
## TOPIC 00067: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_isdisposed.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_isdisposed.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IsDisposed Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates whether the session has been disposed.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property IsDisposed As Boolean |

| C# |
| --- |
| public bool IsDisposed { get; } |

###### Property Value

.

.

::

.

true

True

true

true

True

NISwitch.NISwitch

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_ivi_driver_iividriver_utility.htm language=enus -->
## TOPIC 00068: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_ivi_driver_iividriver_utility.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_niswitch_ivi_driver_iividriver_utility.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IIviDriver.Utility Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

NISwitch.SwitchDriverUtility

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Private ReadOnly Property Utility As IIviDriverUtility Implements IIviDriver.Utility |

| C# |
| --- |
| IIviDriverUtility IIviDriver.Utility { get; } |

###### Property Value

.

.

::

.

NISwitch.SwitchDriverUtility

###### Implements

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_analogbussharingenable.htm language=enus -->
## TOPIC 00069: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_analogbussharingenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_analogbussharingenable.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

AnalogBusSharingEnable Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

true

True

true

true

True

false

False

false

false

False

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property AnalogBusSharingEnable As Boolean |

| C# |
| --- |
| public bool AnalogBusSharingEnable { get; set; } |

###### Property Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The AnalogBusSharingEnable was accessed after the associated NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannel Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_isconfigurationchannel.htm language=enus -->
## TOPIC 00070: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_isconfigurationchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_isconfigurationchannel.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IsConfigurationChannel Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SwitchPath.Connect

true

True

true

true

True

false

False

false

false

False

SwitchPath.Connect

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property IsConfigurationChannel As Boolean |

| C# |
| --- |
| public bool IsConfigurationChannel { get; set; } |

###### Property Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The IsConfigurationChannel was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannel Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_issourcechannel.htm language=enus -->
## TOPIC 00071: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_issourcechannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannel_issourcechannel.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IsSourceChannel Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

true

True

true

true

True

SwitchPath.Connect

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property IsSourceChannel As Boolean |

| C# |
| --- |
| public bool IsSourceChannel { get; set; } |

###### Property Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The IsSourceChannel was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannel Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannelcollection_count.htm language=enus -->
## TOPIC 00072: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannelcollection_count.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannelcollection_count.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Count Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the number of channels supported by the specified device.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property Count As Integer |

| C# |
| --- |
| public int Count { get; } |

###### Property Value

.

.

::

.

Int32

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The Count was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannelCollection Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannelcollection_item_1.htm language=enus -->
## TOPIC 00073: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannelcollection_item_1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchchannelcollection_item_1.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Item Property (String)

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

NISwitch.SwitchChannel

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property Item ( _ name As String _ ) As SwitchChannel |

| C# |
| --- |
| public SwitchChannel Item[ string name ] { get; } |

###### Parameters

- **name**
  - Type: System..::.String Represents the name of the channel in the NI-SWITCH device.

###### Property Value

.

.

::

.

NISwitch.SwitchChannel

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ArgumentNullException | Returns the exception when the paramenter name passed is null. |
| ArgumentOutOfRangeException | Returns the exception when the name is not a valid channel name. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannelCollection Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcharacteristics_accurrentswitchingmax.htm language=enus -->
## TOPIC 00074: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcharacteristics_accurrentswitchingmax.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcharacteristics_accurrentswitchingmax.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ACCurrentSwitchingMax Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the maximum AC current that the channel can switch.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property ACCurrentSwitchingMax As Double |

| C# |
| --- |
| public double ACCurrentSwitchingMax { get; } |

###### Property Value

.

.

::

.

Double

###### Return Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The ACCurrentSwitchingMax was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchCharacteristics Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcharacteristics_acpowerswitchingmax.htm language=enus -->
## TOPIC 00075: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcharacteristics_acpowerswitchingmax.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcharacteristics_acpowerswitchingmax.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

ACPowerSwitchingMax Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the maximum AC power the channel can switch.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property ACPowerSwitchingMax As Double |

| C# |
| --- |
| public double ACPowerSwitchingMax { get; } |

###### Property Value

.

.

::

.

Double

###### Return Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The ACPowerSwitchingMax was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchCharacteristics Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs_text.htm language=enus -->
## TOPIC 00076: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs_text.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs_text.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Text Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the string containing the description of the coercion event.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property Text As String |

| C# |
| --- |
| public string Text { get; } |

###### Property Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchCoercionWarningEventArgs Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11284wire16x1mux.htm language=enus -->
## TOPIC 00077: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11284wire16x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11284wire16x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11284Wire16x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1128 as a 4-wire 16x1 matrix, while connecting your signals using the NI SCXI-1331 terminal block.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11284Wire16x1Mux As String |

| C# |
| --- |
| public static string Device11284Wire16x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1128independent.htm language=enus -->
## TOPIC 00078: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1128independent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1128independent.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1128Independent Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that uses the independent topology, while connecting your signals using the NI SCXI-1331 terminal block.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1128Independent As String |

| C# |
| --- |
| public static string Device1128Independent { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wire16x16matrix.htm language=enus -->
## TOPIC 00079: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wire16x16matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wire16x16matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11292Wire16x16Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the SCXI-1129 containing a 16x16 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11292Wire16x16Matrix As String |

| C# |
| --- |
| public static string Device11292Wire16x16Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wiredual4x32matrix.htm language=enus -->
## TOPIC 00080: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wiredual4x32matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wiredual4x32matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11292WireDual4x32Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the SCXI-1129 containing two 4x32 matrices.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11292WireDual4x32Matrix As String |

| C# |
| --- |
| public static string Device11292WireDual4x32Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wiredual8x16matrix.htm language=enus -->
## TOPIC 00081: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wiredual8x16matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11292wiredual8x16matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11292WireDual8x16Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the SCXI-1129 containing two banks of 8x16 matrices.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11292WireDual8x16Matrix As String |

| C# |
| --- |
| public static string Device11292WireDual8x16Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire256x1mux.htm language=enus -->
## TOPIC 00082: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire256x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire256x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11301Wire256x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 256x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11301Wire256x1Mux As String |

| C# |
| --- |
| public static string Device11301Wire256x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire4x64matrix.htm language=enus -->
## TOPIC 00083: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire4x64matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire4x64matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11301Wire4x64Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 4x64 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11301Wire4x64Matrix As String |

| C# |
| --- |
| public static string Device11301Wire4x64Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire8x32matrix.htm language=enus -->
## TOPIC 00084: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire8x32matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wire8x32matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11301Wire8x32Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 8x32 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11301Wire8x32Matrix As String |

| C# |
| --- |
| public static string Device11301Wire8x32Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wiredual128x1mux.htm language=enus -->
## TOPIC 00085: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wiredual128x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wiredual128x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11301WireDual128x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 128x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11301WireDual128x1Mux As String |

| C# |
| --- |
| public static string Device11301WireDual128x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wireoctal32x1mux.htm language=enus -->
## TOPIC 00086: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wireoctal32x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wireoctal32x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11301WireOctal32x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire octal 32x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11301WireOctal32x1Mux As String |

| C# |
| --- |
| public static string Device11301WireOctal32x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wirequad64x1mux.htm language=enus -->
## TOPIC 00087: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wirequad64x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wirequad64x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11301WireQuad64x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire quad 64x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11301WireQuad64x1Mux As String |

| C# |
| --- |
| public static string Device11301WireQuad64x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wiresixteen16x1mux.htm language=enus -->
## TOPIC 00088: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wiresixteen16x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11301wiresixteen16x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11301WireSixteen16x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as sixteen independent 1-wire 16x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11301WireSixteen16x1Mux As String |

| C# |
| --- |
| public static string Device11301WireSixteen16x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wire128x1mux.htm language=enus -->
## TOPIC 00089: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wire128x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wire128x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11302Wire128x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire 128x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11302Wire128x1Mux As String |

| C# |
| --- |
| public static string Device11302Wire128x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wire4x32matrix.htm language=enus -->
## TOPIC 00090: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wire4x32matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wire4x32matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11302Wire4x32Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire 4x32 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11302Wire4x32Matrix As String |

| C# |
| --- |
| public static string Device11302Wire4x32Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wireoctal16x1mux.htm language=enus -->
## TOPIC 00091: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wireoctal16x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wireoctal16x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11302WireOctal16x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire octal 16x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11302WireOctal16x1Mux As String |

| C# |
| --- |
| public static string Device11302WireOctal16x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wirequad32x1mux.htm language=enus -->
## TOPIC 00092: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wirequad32x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11302wirequad32x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11302WireQuad32x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire quad 32x1 multiplexer.
 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11302WireQuad32x1Mux As String |

| C# |
| --- |
| public static string Device11302WireQuad32x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11304wire64x1mux.htm language=enus -->
## TOPIC 00093: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11304wire64x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11304wire64x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11304Wire64x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 4-wire quad 64x1 multiplexer.
 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11304Wire64x1Mux As String |

| C# |
| --- |
| public static string Device11304Wire64x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11304wirequad16x1mux.htm language=enus -->
## TOPIC 00094: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11304wirequad16x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11304wirequad16x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11304WireQuad16x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1130 as a 4-wire quad 16x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11304WireQuad16x1Mux As String |

| C# |
| --- |
| public static string Device11304WireQuad16x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1130independent.htm language=enus -->
## TOPIC 00095: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1130independent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1130independent.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1130Independent Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1130 in the independent topology, while connecting your signals using the NI SCXI-1377 terminal block.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1130Independent As String |

| C# |
| --- |
| public static string Device1130Independent { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116016spdt.htm language=enus -->
## TOPIC 00096: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116016spdt.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116016spdt.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device116016Spdt Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a the NI SCXI-1160 in the 16-SPDT general purpose topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device116016Spdt As String |

| C# |
| --- |
| public static string Device116016Spdt { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11618spdt.htm language=enus -->
## TOPIC 00097: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11618spdt.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device11618spdt.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device11618Spdt Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1161 in the 8-SPDT general purpose topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device11618Spdt As String |

| C# |
| --- |
| public static string Device11618Spdt { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1163roctal4x1mux.htm language=enus -->
## TOPIC 00098: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1163roctal4x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1163roctal4x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1163ROctal4x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1163R in the octal 4x1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1163ROctal4x1Mux As String |

| C# |
| --- |
| public static string Device1163ROctal4x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116616dpdt.htm language=enus -->
## TOPIC 00099: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116616dpdt.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116616dpdt.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device116616Dpdt Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1166 in the 16-DPDT topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device116616Dpdt As String |

| C# |
| --- |
| public static string Device116616Dpdt { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116632spdt.htm language=enus -->
## TOPIC 00100: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116632spdt.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116632spdt.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device116632Spdt Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI SCXI-1166 in the 32-SPDT topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device116632Spdt As String |

| C# |
| --- |
| public static string Device116632Spdt { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1167independent.htm language=enus -->
## TOPIC 00101: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1167independent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1167independent.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1167Independent Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1167 in the independent topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1167Independent As String |

| C# |
| --- |
| public static string Device1167Independent { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1169100spst.htm language=enus -->
## TOPIC 00102: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1169100spst.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1169100spst.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1169100Spst Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1169 in the 100-SPST topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1169100Spst As String |

| C# |
| --- |
| public static string Device1169100Spst { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116950dpst.htm language=enus -->
## TOPIC 00103: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116950dpst.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device116950dpst.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device116950Dpst Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1169 in the 50-SPST topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device116950Dpst As String |

| C# |
| --- |
| public static string Device116950Dpst { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device119332x1mux.htm language=enus -->
## TOPIC 00104: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device119332x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device119332x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device119332x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1193 in the 32x1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device119332x1Mux As String |

| C# |
| --- |
| public static string Device119332x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193dual16x1mux.htm language=enus -->
## TOPIC 00105: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193dual16x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193dual16x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1193Dual16x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1193 in the dual 16x1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1193Dual16x1Mux As String |

| C# |
| --- |
| public static string Device1193Dual16x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193dual8x1terminatedmux.htm language=enus -->
## TOPIC 00106: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193dual8x1terminatedmux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193dual8x1terminatedmux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1193Dual8x1TerminatedMux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1193 in the dual 8x1 terminated multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1193Dual8x1TerminatedMux As String |

| C# |
| --- |
| public static string Device1193Dual8x1TerminatedMux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193quad4x1terminatedmux.htm language=enus -->
## TOPIC 00107: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193quad4x1terminatedmux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193quad4x1terminatedmux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1193Quad4x1TerminatedMux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1193 in the quad 4x1 terminated multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1193Quad4x1TerminatedMux As String |

| C# |
| --- |
| public static string Device1193Quad4x1TerminatedMux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193quad8x1mux.htm language=enus -->
## TOPIC 00108: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193quad8x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device1193quad8x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device1193Quad8x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI SCXI-1193 in the quad 8x1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device1193Quad8x1Mux As String |

| C# |
| --- |
| public static string Device1193Quad8x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25012wiredual12x1mux.htm language=enus -->
## TOPIC 00109: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25012wiredual12x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25012wiredual12x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25012WireDual12x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire dual 12x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25012WireDual12x1Mux As String |

| C# |
| --- |
| public static string Device25012WireDual12x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25014wire12x1mux.htm language=enus -->
## TOPIC 00110: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25014wire12x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25014wire12x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25014Wire12x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2501 as a 4-wire 12x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25014Wire12x1Mux As String |

| C# |
| --- |
| public static string Device25014Wire12x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25032wire24x1mux.htm language=enus -->
## TOPIC 00111: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25032wire24x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25032wire24x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25032Wire24x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire 24x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25032Wire24x1Mux As String |

| C# |
| --- |
| public static string Device25032Wire24x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25034wire12x1mux.htm language=enus -->
## TOPIC 00112: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25034wire12x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25034wire12x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25034Wire12x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2503 as a 4-wire 12x1 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25034Wire12x1Mux As String |

| C# |
| --- |
| public static string Device25034Wire12x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2510independent.htm language=enus -->
## TOPIC 00113: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2510independent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2510independent.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device2510Independent Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2510 in the independent topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device2510Independent As String |

| C# |
| --- |
| public static string Device2510Independent { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2512independent.htm language=enus -->
## TOPIC 00114: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2512independent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2512independent.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device2512Independent Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2512 in the independent topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device2512Independent As String |

| C# |
| --- |
| public static string Device2512Independent { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25252wire64x1mux.htm language=enus -->
## TOPIC 00115: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25252wire64x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25252wire64x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25252Wire64x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the value that indicates the NI PXIe-2525 2 wire 64x1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25252Wire64x1Mux As String |

| C# |
| --- |
| public static string Device25252Wire64x1Mux { get; } |

###### Property Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25252wirequad16x1mux.htm language=enus -->
## TOPIC 00116: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25252wirequad16x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25252wirequad16x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25252WireQuad16x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the value that indicates the NI PXIe-2525 2 wire quad 16x1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25252WireQuad16x1Mux As String |

| C# |
| --- |
| public static string Device25252WireQuad16x1Mux { get; } |

###### Property Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25292wire4x32matrix.htm language=enus -->
## TOPIC 00117: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25292wire4x32matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25292wire4x32matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25292Wire4x32Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2529 as a 2-wire 4x32 matrix topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25292Wire4x32Matrix As String |

| C# |
| --- |
| public static string Device25292Wire4x32Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wire4x32matrix.htm language=enus -->
## TOPIC 00118: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wire4x32matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wire4x32matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25301Wire4x32Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2530 as a 1-wire 4x32 matrix topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25301Wire4x32Matrix As String |

| C# |
| --- |
| public static string Device25301Wire4x32Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wire8x16matrix.htm language=enus -->
## TOPIC 00119: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wire8x16matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wire8x16matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25301Wire8x16Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2530 as a 1-wire 8x16
 matrix topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25301Wire8x16Matrix As String |

| C# |
| --- |
| public static string Device25301Wire8x16Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wireoctal16x1mux.htm language=enus -->
## TOPIC 00120: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wireoctal16x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25301wireoctal16x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25301WireOctal16x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire octal 16x1
 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25301WireOctal16x1Mux As String |

| C# |
| --- |
| public static string Device25301WireOctal16x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25302wire64x1mux.htm language=enus -->
## TOPIC 00121: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25302wire64x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25302wire64x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25302Wire64x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire 64x1
 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25302Wire64x1Mux As String |

| C# |
| --- |
| public static string Device25302Wire64x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25302wiredual32x1mux.htm language=enus -->
## TOPIC 00122: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25302wiredual32x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25302wiredual32x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25302WireDual32x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire dual 32×1
 multiplexer.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25302WireDual32x1Mux As String |

| C# |
| --- |
| public static string Device25302WireDual32x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25311wire4x128matrix.htm language=enus -->
## TOPIC 00123: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25311wire4x128matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25311wire4x128matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25311Wire4x128Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire 4×128
 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25311Wire4x128Matrix As String |

| C# |
| --- |
| public static string Device25311Wire4x128Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25321wire4x128matrix.htm language=enus -->
## TOPIC 00124: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25321wire4x128matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25321wire4x128matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25321Wire4x128Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 4×128
 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25321Wire4x128Matrix As String |

| C# |
| --- |
| public static string Device25321Wire4x128Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25322wire8x32matrix.htm language=enus -->
## TOPIC 00125: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25322wire8x32matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25322wire8x32matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25322Wire8x32Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 8×32
 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25322Wire8x32Matrix As String |

| C# |
| --- |
| public static string Device25322Wire8x32Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25322wiredual4x32matrix.htm language=enus -->
## TOPIC 00126: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25322wiredual4x32matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25322wiredual4x32matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25322WireDual4x32Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire dual 4×32
 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25322WireDual4x32Matrix As String |

| C# |
| --- |
| public static string Device25322WireDual4x32Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25331wire4x64matrix.htm language=enus -->
## TOPIC 00127: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25331wire4x64matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25331wire4x64matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25331Wire4x64Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2533 as a 1-wire 4×64
 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25331Wire4x64Matrix As String |

| C# |
| --- |
| public static string Device25331Wire4x64Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25411wire8x12matrix.htm language=enus -->
## TOPIC 00128: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25411wire8x12matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25411wire8x12matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25411Wire8X12Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates a topology which uses the NI PXI-2541 as a 1-wire 8x12 matrix.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25411Wire8X12Matrix As String |

| C# |
| --- |
| public static string Device25411Wire8X12Matrix { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2542quad2x1terminatedmux.htm language=enus -->
## TOPIC 00129: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2542quad2x1terminatedmux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2542quad2x1terminatedmux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device2542Quad2x1TerminatedMux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI/PXIe-2542 in the quad 2×1 terminated multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device2542Quad2x1TerminatedMux As String |

| C# |
| --- |
| public static string Device2542Quad2x1TerminatedMux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2543dual4x1terminatedmux.htm language=enus -->
## TOPIC 00130: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2543dual4x1terminatedmux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2543dual4x1terminatedmux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device2543Dual4x1TerminatedMux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2543 in the dual 4×1 terminated multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device2543Dual4x1TerminatedMux As String |

| C# |
| --- |
| public static string Device2543Dual4x1TerminatedMux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25478x1mux.htm language=enus -->
## TOPIC 00131: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25478x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25478x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25478x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2547 in the 8×1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25478x1Mux As String |

| C# |
| --- |
| public static string Device25478x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2593independent.htm language=enus -->
## TOPIC 00132: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2593independent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2593independent.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device2593Independent Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) in the independent topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device2593Independent As String |

| C# |
| --- |
| public static string Device2593Independent { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25944x1mux.htm language=enus -->
## TOPIC 00133: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25944x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25944x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25944x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2594 in the 4×1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25944x1Mux As String |

| C# |
| --- |
| public static string Device25944x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25954x1mux.htm language=enus -->
## TOPIC 00134: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25954x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25954x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25954x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2595 in the 4×1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25954x1Mux As String |

| C# |
| --- |
| public static string Device25954x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2596dual6x1mux.htm language=enus -->
## TOPIC 00135: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2596dual6x1mux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2596dual6x1mux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device2596Dual6x1Mux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2596 in the dual 6×1 multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device2596Dual6x1Mux As String |

| C# |
| --- |
| public static string Device2596Dual6x1Mux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25976x1terminatedmux.htm language=enus -->
## TOPIC 00136: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25976x1terminatedmux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device25976x1terminatedmux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device25976x1TerminatedMux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2597 in the 6×1 terminated multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device25976x1TerminatedMux As String |

| C# |
| --- |
| public static string Device25976x1TerminatedMux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2720independent.htm language=enus -->
## TOPIC 00137: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2720independent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2720independent.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device2720Independent Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2720 in the independent topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device2720Independent As String |

| C# |
| --- |
| public static string Device2720Independent { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2725independent.htm language=enus -->
## TOPIC 00138: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2725independent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device2725independent.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device2725Independent Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2725
 in the independent topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device2725Independent As String |

| C# |
| --- |
| public static string Device2725Independent { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27372wire4x64matrix.htm language=enus -->
## TOPIC 00139: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27372wire4x64matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27372wire4x64matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device27372Wire4x64matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the value that indicates the NI PXIe-2737 2 wire 4x64 matrix topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device27372Wire4x64matrix As String |

| C# |
| --- |
| public static string Device27372Wire4x64matrix { get; } |

###### Property Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27382wire8x32matrix.htm language=enus -->
## TOPIC 00140: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27382wire8x32matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27382wire8x32matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device27382Wire8x32Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the value that indicates the NI PXIe-2738 2 wire 8x32 matrix topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device27382Wire8x32Matrix As String |

| C# |
| --- |
| public static string Device27382Wire8x32Matrix { get; } |

###### Property Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27392wire16x16matrix.htm language=enus -->
## TOPIC 00141: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27392wire16x16matrix.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27392wire16x16matrix.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device27392Wire16x16Matrix Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the value that indicates the NI PXIe-2739 2 wire 16x16 matrix topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device27392Wire16x16Matrix As String |

| C# |
| --- |
| public static string Device27392Wire16x16Matrix { get; } |

###### Property Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27976x1terminatedmux.htm language=enus -->
## TOPIC 00142: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27976x1terminatedmux.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27976x1terminatedmux.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device27976x1TerminatedMux Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2797 in the 6x1 terminated multiplexer topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device27976x1TerminatedMux As String |

| C# |
| --- |
| public static string Device27976x1TerminatedMux { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27992spdt.htm language=enus -->
## TOPIC 00143: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27992spdt.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_device27992spdt.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Device27992Spdt Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the NI PXI-2799 in the 2-SPDT topology.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Device27992Spdt As String |

| C# |
| --- |
| public static string Device27992Spdt { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_deviceconfiguredtopology.htm language=enus -->
## TOPIC 00144: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_deviceconfiguredtopology.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdevicetopology_deviceconfiguredtopology.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DeviceConfiguredTopology Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value that indicates the last topology that was configured for the device in MAX.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property DeviceConfiguredTopology As String |

| C# |
| --- |
| public static string DeviceConfiguredTopology { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveridentity_description.htm language=enus -->
## TOPIC 00145: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveridentity_description.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveridentity_description.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Description Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

String

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property Description As String |

| C# |
| --- |
| public string Description { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The Descriptionwas accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverIdentity Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_cache.htm language=enus -->
## TOPIC 00146: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_cache.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_cache.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Cache Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets or sets whether to cache the value of properties.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property Cache As Boolean |

| C# |
| --- |
| public bool Cache { get; set; } |

###### Property Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

true

True

true

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The Cache was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

true

True

true

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_interchangecheck.htm language=enus -->
## TOPIC 00147: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_interchangecheck.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchdriveroperation_interchangecheck.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

InterchangeCheck Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets or sets whether to perform interchangeability checking and retrieve interchangeability warnings.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property InterchangeCheck As Boolean |

| C# |
| --- |
| public bool InterchangeCheck { get; set; } |

###### Property Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The InterchangeCheck was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

NI-SWITCH does not support interchangeability check.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchinterchangecheckwarningeventargs_text.htm language=enus -->
## TOPIC 00148: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchinterchangecheckwarningeventargs_text.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchinterchangecheckwarningeventargs_text.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Text Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the string which provides a description of the InterChangeCheck warning.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property Text As String |

| C# |
| --- |
| public string Text { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchInterchangeCheckWarningEventArgs Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_numberofrows.htm language=enus -->
## TOPIC 00149: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_numberofrows.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_numberofrows.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

NumberOfRows Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the number of channels on a row of a matrix or scanner. If the switch is a scanner, this value is the number of output channels.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property NumberOfRows As Integer |

| C# |
| --- |
| public int NumberOfRows { get; } |

###### Property Value

.

.

::

.

Int32

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The NumberOfRows property was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

WireMode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchModuleCharacteristics Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_powerdownlatchingrelaysafterdebounce.htm language=enus -->
## TOPIC 00150: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_powerdownlatchingrelaysafterdebounce.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_powerdownlatchingrelaysafterdebounce.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PowerDownLatchingRelaysAfterDebounce Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets or sets a value which indicates whether to power down latching relays after waiting for the relays to settle.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property PowerDownLatchingRelaysAfterDebounce As Boolean |

| C# |
| --- |
| public bool PowerDownLatchingRelaysAfterDebounce { get; set; } |

###### Property Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The PowerDownLatchingRelaysAfterDebounce property was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchModuleCharacteristics Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_serialnumber.htm language=enus -->
## TOPIC 00151: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_serialnumber.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchmodulecharacteristics_serialnumber.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SerialNumber Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the serial number for the switch controlled by NI-SWITCH.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property SerialNumber As String |

| C# |
| --- |
| public string SerialNumber { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The SerialNumber was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

If the device does not return a serial number, NI-SWITCH returns the Invalid Attribute error.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchModuleCharacteristics Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchpath_isdebounced.htm language=enus -->
## TOPIC 00152: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchpath_isdebounced.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchpath_isdebounced.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

IsDebounced Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value which indicates whether the entire NI-SWITCH device has settled since the last switching command.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property IsDebounced As Boolean |

| C# |
| --- |
| public bool IsDebounced { get; } |

###### Property Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The IsDebounced property was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchPath Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_instrumentrevision.htm language=enus -->
## TOPIC 00153: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_instrumentrevision.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult_instrumentrevision.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

InstrumentRevision Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a string that contains version information about the NI-SWITCH driver.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public ReadOnly Property InstrumentRevision As String |

| C# |
| --- |
| public string InstrumentRevision { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscan_digitalfilterenable.htm language=enus -->
## TOPIC 00154: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscan_digitalfilterenable.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscan_digitalfilterenable.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalFilterEnable Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SwitchScan.TriggerInput

true

True

true

true

True

false

False

false

false

False

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property DigitalFilterEnable As Boolean |

| C# |
| --- |
| public bool DigitalFilterEnable { get; set; } |

###### Property Value

.

.

::

.

true

True

true

true

True

false

False

false

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The DigitalFilterEnable was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScan Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscan_handshakinginitiation.htm language=enus -->
## TOPIC 00155: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscan_handshakinginitiation.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscan_handshakinginitiation.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakingInitiation Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets or sets a value which specifies how to start handshaking with a measurement device.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property HandshakingInitiation As Integer |

| C# |
| --- |
| public int HandshakingInitiation { get; set; } |

###### Property Value

.

.

::

.

NISwitch.SwitchScanInitiation

### [IMAGE alt='image' src='../icons/collapse_all.gif']Exceptions

| Exception | Condition |
| --- | --- |
| ObjectDisposedException | The HandshakingInitiation was accessed after the associated NISwitch.NISwitch object was disposed. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScan Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutput_rearconnectormodule1.htm language=enus -->
## TOPIC 00156: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutput_rearconnectormodule1.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutput_rearconnectormodule1.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

RearConnectorModule1 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to the RearConnectorModule1 trigger. The switch waits until it receives a trigger on the rear connector module 1.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property RearConnectorModule1 As String |

| C# |
| --- |
| public static string RearConnectorModule1 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanAdvancedOutput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline_ttl3.htm language=enus -->
## TOPIC 00157: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline_ttl3.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline_ttl3.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Ttl3 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Ttl3 As String |

| C# |
| --- |
| public static string Ttl3 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanAdvancedOutputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule12.htm language=enus -->
## TOPIC 00158: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule12.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule12.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

RearConnectorModule12 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the rear connector module 12.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property RearConnectorModule12 As String |

| C# |
| --- |
| public static string RearConnectorModule12 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule2.htm language=enus -->
## TOPIC 00159: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule2.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

RearConnectorModule2 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the rear connector module 2.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property RearConnectorModule2 As String |

| C# |
| --- |
| public static string RearConnectorModule2 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule5.htm language=enus -->
## TOPIC 00160: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule5.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule5.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

RearConnectorModule5 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the rear connector module 5.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property RearConnectorModule5 As String |

| C# |
| --- |
| public static string RearConnectorModule5 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule6.htm language=enus -->
## TOPIC 00161: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule6.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule6.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

RearConnectorModule6 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the rear connector module 6.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property RearConnectorModule6 As String |

| C# |
| --- |
| public static string RearConnectorModule6 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule8.htm language=enus -->
## TOPIC 00162: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule8.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule8.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

RearConnectorModule8 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the rear connector module 8.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property RearConnectorModule8 As String |

| C# |
| --- |
| public static string RearConnectorModule8 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule9.htm language=enus -->
## TOPIC 00163: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule9.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_rearconnectormodule9.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

RearConnectorModule9 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the rear connector module 9.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property RearConnectorModule9 As String |

| C# |
| --- |
| public static string RearConnectorModule9 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_ttl6.htm language=enus -->
## TOPIC 00164: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_ttl6.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinput_ttl6.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Ttl6 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Ttl6 As String |

| C# |
| --- |
| public static string Ttl6 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInput Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl0.htm language=enus -->
## TOPIC 00165: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl0.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl0.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Ttl0 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Ttl0 As String |

| C# |
| --- |
| public static string Ttl0 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl2.htm language=enus -->
## TOPIC 00166: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl2.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl2.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Ttl2 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Ttl2 As String |

| C# |
| --- |
| public static string Ttl2 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl5.htm language=enus -->
## TOPIC 00167: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl5.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl5.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Ttl5 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Ttl5 As String |

| C# |
| --- |
| public static string Ttl5 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl6.htm language=enus -->
## TOPIC 00168: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl6.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl6.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Ttl6 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Ttl6 As String |

| C# |
| --- |
| public static string Ttl6 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl7.htm language=enus -->
## TOPIC 00169: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl7.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchscantriggerinputbusline_ttl7.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Ttl7 Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a value corresponding to a trigger on the PXI_TRIG7 line. The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the scan list.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property Ttl7 As String |

| C# |
| --- |
| public static string Ttl7 { get; } |

###### Property Value

.

.

::

.

String

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanTriggerInputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarning_code.htm language=enus -->
## TOPIC 00170: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarning_code.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarning_code.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Code Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the GUID code assigned to the warning.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property Code As Guid |

| C# |
| --- |
| public Guid Code { get; private set; } |

###### Property Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchWarning Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarning_pathremainswarningcode.htm language=enus -->
## TOPIC 00171: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarning_pathremainswarningcode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarning_pathremainswarningcode.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

PathRemainsWarningCode Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the warning code if the card is not capable of removing all paths and always leaves at least one connected.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Shared ReadOnly Property PathRemainsWarningCode As Guid |

| C# |
| --- |
| public static Guid PathRemainsWarningCode { get; } |

###### Property Value

.

.

::

.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchWarning Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs_warning.htm language=enus -->
## TOPIC 00172: Syntax

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs_warning.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/p_nationalinstruments_modularinstruments_niswitch_switchwarningeventargs_warning.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

Warning Property

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the warning set in the Warning Event Args.

Namespace:

NationalInstruments.ModularInstruments.NISwitch

Assembly:

NationalInstruments.ModularInstruments.NISwitch.Fx40

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Property Warning As SwitchWarning |

| C# |
| --- |
| public SwitchWarning Warning { get; private set; } |

###### Property Value

.

.

::

.

NISwitch.SwitchWarning

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchWarningEventArgs Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_niswitch.htm language=enus -->
## TOPIC 00173: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_niswitch.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_niswitch.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

NISwitch Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [NISwitch](t_nationalinstruments_modularinstruments_niswitch_niswitch.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Channels | Gets a NISwitch.SwitchChannelCollection object which represents the Channel Collection and their properties in NI-SWITCH. |
|  | DriverOperation | Gets a NISwitch.SwitchDriverOperation object that defines methods and properties for common operations on the NI-SWITCH driver. |
|  | Identity | Gets a NISwitch.SwitchDriverIdentity object which defines the methods and properties for identifying the NI-SWITCH driver. |
|  | IsDisposed | Gets a value that indicates whether the session has been disposed. |
|  | ModuleCharacteristics | Gets a NISwitch.SwitchModuleCharacteristics object that defines the inherent characteristics of the NI-SWITCH driver. |
|  | Path | Gets a NISwitch.SwitchPath object which is used to build a channel path in the NI-SWITCH driver. |
|  | RelayOperations | Gets a NISwitch.SwitchRelayOperations object which represent the methods and properties related to the relay operation in the NI-SWITCH driver. |
|  | Scan | Gets a NISwitch.SwitchScan object which contains methods and properties used to configure a NI-SWITCH device using a scan list. |
|  | Utility | Gets a NISwitch.SwitchDriverUtility object to access the utility features on the NI-SWITCH driver. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Explicit Interface Implementations

|  | Name | Description |
| --- | --- | --- |
|  | IIviDriver..::.DriverOperation | Gets a NISwitch.SwitchDriverOperation object that defines methods and properties for common operations on the NI-SWITCH driver. |
|  | IIviDriver..::.Identity | Gets a NISwitch.SwitchDriverIdentity object which defines the methods and properties for identifying the NI-SWITCH driver. |
|  | IIviDriver..::.Utility | Gets a NISwitch.SwitchDriverUtility object to access the utility features on the NI-SWITCH driver. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

NISwitch Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchchannelcollection.htm language=enus -->
## TOPIC 00174: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchchannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchchannelcollection.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannelCollection Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchChannelCollection](t_nationalinstruments_modularinstruments_niswitch_switchchannelcollection.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Count | Gets the number of channels supported by the specified device. |
|  | Item | Overloaded. Gets the NISwitch.SwitchChannel object which corresponds to the channel index used in the index parameter. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchChannelCollection Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchcharacteristics.htm language=enus -->
## TOPIC 00175: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchcharacteristics.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchcharacteristics.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchCharacteristics Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchCharacteristics](t_nationalinstruments_modularinstruments_niswitch_switchcharacteristics.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | ACCurrentCarryMax | Gets the maximum AC current that the channel can carry. |
|  | ACCurrentSwitchingMax | Gets the maximum AC current that the channel can switch. |
|  | ACPowerCarryMax | Gets the maximum AC power that the channel can carry. |
|  | ACPowerSwitchingMax | Gets the maximum AC power the channel can switch. |
|  | ACVoltageMax | Gets the maximum AC voltage the channel can switch. |
|  | Bandwidth | Gets the bandwidth for the channel. |
|  | DCCurrentCarryMax | Gets the maximum DC current the channel can carry. |
|  | DCCurrentSwitchingMax | Gets the maximum DC current that the channel can switch. |
|  | DCPowerCarryMax | Gets the maximum DC power that the channel can carry. |
|  | DCPowerSwitchingMax | Gets the maximum DC power that the channel can switch. |
|  | DCVoltageMax | Gets the maximum DC voltage the channel can switch. |
|  | Impedance | Gets the characteristic impedance for the channel. |
|  | SettlingTime | Gets or sets the maximum length of time from after you make a connection until the signal flowing through the channel settles. The units are seconds. NOTE: If you use PXI-2501/2503/2565/2590/2591 the actual delay will always be the greater value of the SwitchCharacteristics.SettlingTime and the value you specify as the SwitchScan.Delay. |
|  | WireMode | Gets the wire mode of the switch device. This property affects the values of the SwitchModuleCharacteristics.NumberOfRows and SwitchModuleCharacteristics.NumberOfColumns attributes. The actual number of input and output lines on the switch device is fixed, but the number of channels depends on how many lines constitute each channel. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchCharacteristics Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs.htm language=enus -->
## TOPIC 00176: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchCoercionWarningEventArgs Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchCoercionWarningEventArgs](t_nationalinstruments_modularinstruments_niswitch_switchcoercionwarningeventargs.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Text | Gets the string containing the description of the coercion event. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchCoercionWarningEventArgs Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdevicetopology.htm language=enus -->
## TOPIC 00177: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdevicetopology.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdevicetopology.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchDeviceTopology Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchDeviceTopology](t_nationalinstruments_modularinstruments_niswitch_switchdevicetopology.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Device11271Wire64x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1127 as a 1-wire 64x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. |
|  | Device11272Wire32x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1127 as a 2-wire 32x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. |
|  | Device11272Wire4x8Matrix | Gets a value that indicates a topology which uses the NI SCXI-1127 containing a 2-wire 4x8 matrix, while connecting your signals using the NI SCXI-1332 terminal block. |
|  | Device11274Wire16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1127 containing a 4-wire 16x1 matrix, while connecting your signals using the NI SCXI-1331 terminal block. |
|  | Device1127Independent | Gets a value that indicates the NI SCXI-1127 in the independent topology, while connecting your signals using the NI SCXI-1331 terminal block. |
|  | Device11281Wire64x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1128 as a 1-wire 64x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. |
|  | Device11282Wire32x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1128 as a 2-wire 32x1 multiplexer, while connecting your signals using the NI SCXI-1331 terminal block. |
|  | Device11282Wire4x8Matrix | Gets a value that indicates a topology which uses the NI SCXI-1128 containing a 2-wire 4x8 matrix, while connecting your signals using the NI SCXI-1332 terminal block. |
|  | Device11284Wire16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1128 as a 4-wire 16x1 matrix, while connecting your signals using the NI SCXI-1331 terminal block. |
|  | Device1128Independent | Gets a value that uses the independent topology, while connecting your signals using the NI SCXI-1331 terminal block. |
|  | Device11292Wire16x16Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing a 16x16 matrix. |
|  | Device11292Wire4x64Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing a 4x64 matrix. |
|  | Device11292Wire8x32Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing a 8x32 matrix. |
|  | Device11292WireDual4x32Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing two 4x32 matrices. |
|  | Device11292WireDual8x16Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing two banks of 8x16 matrices. |
|  | Device11292WireQuad4x16Matrix | Gets a value that indicates a topology which uses the SCXI-1129 containing four banks of 4x16 matrices. |
|  | Device11301Wire256x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 256x1 multiplexer. |
|  | Device11301Wire4x64Matrix | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 4x64 matrix. |
|  | Device11301Wire8x32Matrix | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 8x32 matrix. |
|  | Device11301WireDual128x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire 128x1 multiplexer. |
|  | Device11301WireOctal32x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire octal 32x1 multiplexer. |
|  | Device11301WireQuad64x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 1-wire quad 64x1 multiplexer. |
|  | Device11301WireSixteen16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as sixteen independent 1-wire 16x1 multiplexer. |
|  | Device11302Wire128x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire 128x1 multiplexer. |
|  | Device11302Wire4x32Matrix | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire 4x32 matrix. |
|  | Device11302WireOctal16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire octal 16x1 multiplexer. |
|  | Device11302WireQuad32x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 2-wire quad 32x1 multiplexer. multiplexer. |
|  | Device11304Wire64x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 4-wire quad 64x1 multiplexer. multiplexer. |
|  | Device11304WireQuad16x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1130 as a 4-wire quad 16x1 multiplexer. |
|  | Device1130Independent | Gets a value that indicates the NI SCXI-1130 in the independent topology, while connecting your signals using the NI SCXI-1377 terminal block. |
|  | Device116016Spdt | Gets a value that indicates a the NI SCXI-1160 in the 16-SPDT general purpose topology. |
|  | Device11618Spdt | Gets a value that indicates the NI SCXI-1161 in the 8-SPDT general purpose topology. |
|  | Device1163ROctal4x1Mux | Gets a value that indicates a topology which uses the NI SCXI-1163R in the octal 4x1 multiplexer topology. |
|  | Device116616Dpdt | Gets a value that indicates a topology which uses the NI SCXI-1166 in the 16-DPDT topology. |
|  | Device116632Spdt | Gets a value that indicates a topology which uses the NI SCXI-1166 in the 32-SPDT topology. |
|  | Device1167Independent | Gets a value that indicates the NI SCXI-1167 in the independent topology. |
|  | Device1169100Spst | Gets a value that indicates the NI SCXI-1169 in the 100-SPST topology. |
|  | Device116950Dpst | Gets a value that indicates the NI SCXI-1169 in the 50-SPST topology. |
|  | Device11751Wire196x1Mux | Gets a value that indicates the NI SCXI-1175 in the 1-wire 196x1 multiplexer topology. |
|  | Device11752Wire95x1Mux | Gets a value that indicates the NI SCXI-1175 in the 2-wire 95x1 multiplexer topology. |
|  | Device11752Wire98x1Mux | Gets a value that indicates the NI SCXI-1175 in the 2-wire 98x1 multiplexer topology. |
|  | Device1190Quad4x1Mux | Gets a value that indicates the NI SCXI-1190 in the quad 4x1 multiplexer topology. |
|  | Device1191Quad4x1Mux | Gets a value that indicates the NI SCXI-1191 in the quad 4x1 multiplexer topology. |
|  | Device11928Spdt | Gets a value that indicates the NI SCXI-1192 in the 8-SPDT general-purpose topology. |
|  | Device119316x1TerminatedMux | Gets a value that indicates the NI SCXI-1193 16x1 in the terminated multiplexer topology. |
|  | Device119332x1Mux | Gets a value that indicates the NI SCXI-1193 in the 32x1 multiplexer topology. |
|  | Device1193Dual16x1Mux | Gets a value that indicates the NI SCXI-1193 in the dual 16x1 multiplexer topology. |
|  | Device1193Dual8x1TerminatedMux | Gets a value that indicates the NI SCXI-1193 in the dual 8x1 terminated multiplexer topology. |
|  | Device1193Independent | Gets a value that indicates the NI SCXI-1193 in the independent topology. |
|  | Device1193Quad4x1TerminatedMux | Gets a value that indicates the NI SCXI-1193 in the quad 4x1 terminated multiplexer topology. |
|  | Device1193Quad8x1Mux | Gets a value that indicates the NI SCXI-1193 in the quad 8x1 multiplexer topology. |
|  | Device1194Quad4x1Mux | Gets a value that indicates the NI SCXI-1194 in the quad 4x1 multiplexer topology. |
|  | Device1195Quad4x1Mux | Gets a value that indicates the NI SCXI-1195 in the quad 4x1 multiplexer topology. |
|  | Device25011Wire48x1AmplifiedMux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 1-wire 48x1 amplified multiplexer. |
|  | Device25011Wire48x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 1-wire 48x1 multiplexer. |
|  | Device25012Wire24x1AmplifiedMux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire 24x1 amplified multiplexer. |
|  | Device25012Wire24x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire 24x1 multiplexer. |
|  | Device25012Wire4x6Matrix | Use this topology, when using the NI PXI-2501 as a 2-wire 4x6 matrix. |
|  | Device25012WireDual12x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire dual 12x1 multiplexer. |
|  | Device25012WireQuad6x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 2-wire quad 6x1 multiplexer. |
|  | Device25014Wire12x1Mux | Gets a value that indicates a topology which uses the NI PXI-2501 as a 4-wire 12x1 multiplexer. |
|  | Device25031Wire48x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 1-wire 48x1 multiplexer. |
|  | Device25032Wire24x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire 24x1 multiplexer. |
|  | Device25032Wire4x6Matrix | Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire 4x6 matrix. |
|  | Device25032WireDual12x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire dual 12x1 multiplexer. |
|  | Device25032WireQuad6x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 2-wire quad 6x1 multiplexer. |
|  | Device25034Wire12x1Mux | Gets a value that indicates a topology which uses the NI PXI-2503 as a 4-wire 12x1 multiplexer. |
|  | Device2510Independent | Gets a value that indicates the NI PXI-2510 in the independent topology. |
|  | Device2512Independent | Gets a value that indicates the NI PXI-2512 in the independent topology. |
|  | Device2514Independent | Gets a value that indicates the NI PXI-2514 in the independent topology. |
|  | Device2515Independent | Gets a value that indicates the NI PXI-2515 in the independent topology. |
|  | Device252080Spst | Gets a value that indicates the NI PXI-2520 in the 80 SPST topology. |
|  | Device252140Dpst | Gets a value that indicates the NI PXI-2521 in the 40 DPST topology. |
|  | Device252253Spdt | Gets a value that indicates the NI PXI-2522 in the 53 SPDT topology. |
|  | Device252326Dpdt | Gets a value that indicates the NI PXI-2523 in the 26 DPDT topology. |
|  | Device25241Wire128x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire 128x1 multiplexer topology. |
|  | Device25241WireDual64x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire dual 64x1 multiplexer topology. |
|  | Device25241WireOctal16x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire octal 16x1 multiplexer topology. |
|  | Device25241WireQuad32x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire quad 32x1 multiplexer topology. |
|  | Device25241WireSixteen8x1Mux | Gets the value that indicates the NI PXIe-2524 1 wire sixteen 8x1 multiplexer topology. |
|  | Device25252Wire64x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire 64x1 multiplexer topology. |
|  | Device25252WireDual32x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire dual 32x1 multiplexer topology. |
|  | Device25252WireOctal8x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire octal 8x1 multiplexer topology. |
|  | Device25252WireQuad16x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire quad 16x1 multiplexer topology. |
|  | Device25252WireSixteen4x1Mux | Gets the value that indicates the NI PXIe-2525 2 wire sixteen 4x1 multiplexer topology. |
|  | Device25261Wire158x1Mux | Gets the value that indicates the NI PXIe-2526 1 wire 158x1 multiplexer topology. |
|  | Device25262Wire79x1Mux | Gets the value that indicates the NI PXIe-2526 2 wire 79x1 multiplexer topology. |
|  | Device25271Wire64x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 1-wire 64x1 multiplexer. |
|  | Device25271WireDual32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 1-wire dual 32x1 multiplexer. |
|  | Device25272Wire32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 2-wire 32x1 multiplexer. |
|  | Device25272WireDual16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 2-wire dual 16x1 multiplexer. |
|  | Device25274Wire16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2527 as a 4-wire 16x1 multiplexer. |
|  | Device2527Independent | Gets a value that indicates the NI PXI-2527 in the independent topology. |
|  | Device25292Wire4x32Matrix | Gets a value that indicates the NI PXI-2529 as a 2-wire 4x32 matrix topology. |
|  | Device25292Wire8x16Matrix | Gets a value that indicates the NI PXI-2529 as a 2-wire 8x16 matrix topology. |
|  | Device25292WireDual4x16Matrix | Gets a value that indicates the NI PXI-2529 as a 2-wire dual 4x16 matrix topology. |
|  | Device25301Wire128x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire 128x1 multiplexer. |
|  | Device25301Wire4x32Matrix | Gets a value that indicates the NI PXI-2530 as a 1-wire 4x32 matrix topology. |
|  | Device25301Wire8x16Matrix | Gets a value that indicates the NI PXI-2530 as a 1-wire 8x16 matrix topology. |
|  | Device25301WireDual64x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire dual 64x1 multiplexer. |
|  | Device25301WireOctal16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire octal 16x1 multiplexer. |
|  | Device25301WireQuad32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 1-wire quad 32x1 multiplexer. |
|  | Device25302Wire4x16Matrix | Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire 4×16 matrix topology. |
|  | Device25302Wire64x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire 64x1 multiplexer. |
|  | Device25302WireDual32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire dual 32×1 multiplexer. |
|  | Device25302WireQuad16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 2-wire quad 16×1 multiplexer. |
|  | Device25304Wire32x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 4-wire 32x1 multiplexer. |
|  | Device25304WireDual16x1Mux | Gets a value that indicates a topology which uses the NI PXI-2530 as a 4-wire dual 16×1 multiplexer. |
|  | Device2530Independent | Gets a value that uses the NI PXI-2530 in the independent topology. |
|  | Device25311Wire4x128Matrix | Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire 4×128 matrix. |
|  | Device25311Wire8x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire 8×64 matrix. |
|  | Device25311WireDual4x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire dual 4×64 matrix. |
|  | Device25311WireDual8x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2531 as a 1-wire dual 8×32 matrix. |
|  | Device25311WireSixteen2x16Matrix | Gets the value that indicates the NI PXI/PXIe-2531 1 wire sixteen 2x16 matrix topology. |
|  | Device25321Wire16x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 16×32 matrix. |
|  | Device25321Wire4x128Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 4×128 matrix. |
|  | Device25321Wire8x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire 8×64 matrix. |
|  | Device25321WireDual16x16Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire dual 16×16 matrix. |
|  | Device25321WireDual4x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire dual 4×64 matrix. |
|  | Device25321WireDual8x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire dual 8×32 matrix. |
|  | Device25321WireQuad4x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire quad 4×32 matrix. |
|  | Device25321WireSixteen2x16Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 1-wire sixteen 2×16 matrix. |
|  | Device25322Wire16x16Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 16×16 matrix. |
|  | Device25322Wire4x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 4×64 matrix. |
|  | Device25322Wire8x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire 8×32 matrix. |
|  | Device25322WireDual4x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2532 as a 2-wire dual 4×32 matrix. |
|  | Device25331Wire4x64Matrix | Gets a value that indicates a topology which uses the NI PXI-2533 as a 1-wire 4×64 matrix. |
|  | Device25341Wire8x32Matrix | Gets a value that indicates a topology which uses the NI PXI-2534 as a 1-wire 8×32 matrix. |
|  | Device25351Wire4x136Matrix | Gets a value that indicates a topology which uses the NI PXI-2535 as a 1-wire 4×136 matrix. |
|  | Device25361Wire8x68Matrix | Gets a value that indicates a topology which uses the NI PXI-2536 as a 1-wire 8×68 matrix. |
|  | Device25401Wire8X9Matrix | Gets a value that indicates a topology which uses the NI PXI-2540 as a 1-wire 8x9 matrix. |
|  | Device25411Wire8X12Matrix | Gets a value that indicates a topology which uses the NI PXI-2541 as a 1-wire 8x12 matrix. |
|  | Device2542Quad2x1TerminatedMux | Gets a value that indicates the NI PXI/PXIe-2542 in the quad 2×1 terminated multiplexer topology. |
|  | Device2543Dual4x1TerminatedMux | Gets a value that indicates the NI PXI-2543 in the dual 4×1 terminated multiplexer topology. |
|  | Device25448x1TerminatedMux | Gets a value that indicates the NI PXI/PXIe-2544 in the 8×1 terminated multiplexer topology. |
|  | Device25454x1TerminatedMux | Gets a value that indicates the NI PXI-2545 in the terminated 4×1 multiplexer topology. |
|  | Device2546Dual4x1Mux | Gets a value that indicates the NI PXI-2546 in the dual 4×1 multiplexer topology. |
|  | Device25478x1Mux | Gets a value that indicates the NI PXI-2547 in the 8×1 multiplexer topology. |
|  | Device25484Spdt | Gets a value that indicates the NI PXI-2548 in the quad SPDT general-purpose topology. |
|  | Device2549Terminated2Spdt | Gets a value that indicates the NI PXI-2549 in the dual terminated SPDT general-purpose topology. |
|  | Device25544x1Mux | Gets a value that indicates the NI PXI-2554 in the 4×1 multiplexer topology. |
|  | Device25554x1TerminatedMux | Gets a value that indicates the NI PXI-2555 in the 4×1 terminated multiplexer topology. |
|  | Device2556Dual4x1Mux | Gets a value that indicates the NI PXI-2556 in the dual 4×1 multiplexer topology. |
|  | Device25578x1Mux | Gets a value that indicates the NI PXI-2557 in the dual 8×1 multiplexer topology. |
|  | Device25584Spdt | Gets a value that indicates the NI PXI-2558 in the quad SPDT general-purpose topology. |
|  | Device2559Terminated2Spdt | Gets a value that indicates the NI PXI-2559 in the dual terminated SPDT general-purpose topology. |
|  | Device256416Spst | Gets a value that indicates the NI PXI-2564 in the 16-SPST topology. |
|  | Device25648Dpst | Gets a value that indicates the NI PXI-2564 in the 8-DPST topology. |
|  | Device256516Spst | Gets a value that indicates the NI PXI-2565 in the 16-SPST topology. |
|  | Device256616Spdt | Gets a value that indicates the NI PXI-2566 in the 16-SPDT topology. |
|  | Device25668Dpdt | Gets a value that indicates the NI PXI-2566 in the 8-DPDT topology. |
|  | Device2567Independent | Gets a value that indicates the NI PXI-2567 in the independent topology. |
|  | Device256815Dpst | Gets a value that indicates the NI PXI-2568 in the 15-DPST topology. |
|  | Device256831Spst | Gets a value that indicates the NI PXI-2568 in the 31-SPST topology. |
|  | Device2569100Spst | Gets a value that indicates the NI PXI-2569 in the 100-SPST topology. |
|  | Device256950Dpst | Gets a value that indicates the NI PXI-2569 in the 50-DPST topology. |
|  | Device257020Dpdt | Gets a value that indicates the NI PXI-2570 in the 20-DPDT topology. |
|  | Device257040Spdt | Gets a value that indicates the NI PXI-2570 in the 40-SPDT topology. |
|  | Device257166Spdt | Gets a value that indicates the NI PXI-2571 in the 66-SPDT topology. |
|  | Device25751Wire196x1Mux | Gets a value that indicates the NI PXI/PXIe-2575 (NI 2575) in the 1-wire 196×1 multiplexer topology. |
|  | Device25752Wire95x1Mux | Gets a value that indicates the NI PXI/PXIe-2575 (NI 2575) in the 2-wire 95×1 multiplexer topology. |
|  | Device25752Wire98x1Mux | Gets a value that indicates the NI PXI/PXIe-2575 (NI 2575) in the 2-wire 98×1 multiplexer topology. |
|  | Device25762Wire64x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire 64×1 multiplexer topology. |
|  | Device25762WireDual32x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire dual 32×1 multiplexer topology. |
|  | Device25762WireOctal8x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire octal 8×1 multiplexer topology. |
|  | Device25762WireQuad16x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire quad 16×1 multiplexer topology. |
|  | Device25762WireSixteen4x1Mux | Gets a value that indicates the NI PXI-2576 in the 2-wire sixteen 4×1 multiplexer topology. |
|  | Device2576Independent | Gets a value that indicates the NI PXI-2576 in the independent topology. |
|  | Device25841Wire12x1Mux | Gets a value that indicates the NI PXI-2584 in the 1-wire 12×1 multiplexer topology. |
|  | Device25841WireDual6x1Mux | Gets a value that indicates the NI PXI-2584 in the 1-wire dual 6×1 multiplexer topology. |
|  | Device25842Wire6x1Mux | Gets a value that indicates the NI PXI-2584 in the 2-wire 6×1 multiplexer topology. |
|  | Device2584Independent | Gets a value that indicates the NI PXI-2584 in the independent topology. |
|  | Device25851Wire10x1Mux | Gets a value that indicates the NI PXI-2585 in the 1-wire 10×1 multiplexer topology. |
|  | Device258610Spst | Gets a value that indicates the NI PXI-2586 in the 10-SPST topology. |
|  | Device25865Dpst | Gets a value that indicates the NI PXI-2586 in the 5-DPST topology. |
|  | Device25904x1Mux | Gets a value that indicates the NI PXI-2590 in the 4×1 multiplexer topology. |
|  | Device25914x1Mux | Gets a value that indicates the NI PXI-2591 in the 4×1 multiplexer topology. |
|  | Device259316x1Mux | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) as a 16×1 multiplexer topology. |
|  | Device25938x1TerminatedMux | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) as a 8×1 terminated multiplexer topology. |
|  | Device2593Dual4x1TerminatedMux | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) as a dual 4×1 terminated multiplexer topology. |
|  | Device2593Dual8x1Mux | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) as a dual 8×1 multiplexer topology. |
|  | Device2593Independent | Gets a value that indicates the NI PXI/PXIe-2593 (NI 2593) in the independent topology. |
|  | Device25944x1Mux | Gets a value that indicates the NI PXI-2594 in the 4×1 multiplexer topology. |
|  | Device25954x1Mux | Gets a value that indicates the NI PXI-2595 in the 4×1 multiplexer topology. |
|  | Device2596Dual6x1Mux | Gets a value that indicates the NI PXI-2596 in the dual 6×1 multiplexer topology. |
|  | Device25976x1TerminatedMux | Gets a value that indicates the NI PXI-2597 in the 6×1 terminated multiplexer topology. |
|  | Device2598DualTransfer | Gets a value that indicates the NI PXI-2598 in the dual transfer switch topology. |
|  | Device25992Spdt | Gets a value that indicates the NI PXI-2599 in the 2-SPDT general-purpose topology. |
|  | Device2720Independent | Gets a value that indicates the NI PXI-2720 in the independent topology. |
|  | Device2722Independent | Gets a value that indicates the NI PXI-2722 in the independent topology. |
|  | Device2725Independent | Gets a value that indicates the NI PXI-2725 in the independent topology. |
|  | Device2727Independent | Gets a value that indicates the NI PXI-2727 in the independent topology. |
|  | Device27372Wire4x64matrix | Gets the value that indicates the NI PXIe-2737 2 wire 4x64 matrix topology. |
|  | Device27382Wire8x32Matrix | Gets the value that indicates the NI PXIe-2738 2 wire 8x32 matrix topology. |
|  | Device27392Wire16x16Matrix | Gets the value that indicates the NI PXIe-2739 2 wire 16x16 matrix topology. |
|  | Device2746Quad4x1Mux | Gets the value that indicates the NI PXIe-2746 quad 4x1 multiplexer topology. |
|  | Device2747Dual8x1Mux | Gets the value that indicates the NI PXIe-2747 dual 8x1 multiplexer topology. |
|  | Device274816x1Mux | Gets the value that indicates the NI PXIe-2748 16x1 multiplexer topology. |
|  | Device2790Independent | Gets a value that indicates the NI PXI-2790 in the independent topology. |
|  | Device2796Dual6x1Mux | Gets a value that indicates the NI PXI-2796 in the dual 6×1 multiplexer topology. |
|  | Device27976x1TerminatedMux | Gets a value that indicates the NI PXI-2797 in the 6x1 terminated multiplexer topology. |
|  | Device2798DualTransfer | Gets a value that indicates the NI PXI-2798 in the dual transfer topology. |
|  | Device27992Spdt | Gets a value that indicates the NI PXI-2799 in the 2-SPDT topology. |
|  | Device28651Wire4x84Matrix | Gets a value that indicates the NI 2865 in the 4×84 terminated matrix topology. |
|  | DeviceConfiguredTopology | Gets a value that indicates the last topology that was configured for the device in MAX. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDeviceTopology Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdriveridentity.htm language=enus -->
## TOPIC 00178: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdriveridentity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdriveridentity.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchDriverIdentity Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchDriverIdentity](t_nationalinstruments_modularinstruments_niswitch_switchdriveridentity.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Gets a String that contains a brief description of the specific driver. |
|  | Identifier | Gets the String that contains an identifier for NI-Switch .NET API. |
|  | InstrumentFirmwareRevision | Gets a string that contains the firmware revision information for the NI-SWITCH device that is currently in use. |
|  | InstrumentManufacturer | Gets the name of the instrument manufacturer of the NI-SWITCH device that is currently in use. |
|  | InstrumentModel | Gets the model number or name of the NI-SWITCH device that is currently in use. |
|  | Revision | Gets a string which contains additional version information about the NI-SWITCH instrument driver. |
|  | SpecificationMajorVersion | Gets the major version number of the IviSwtch class specification. |
|  | SpecificationMinorVersion | Gets the minor version number of the class specification with which NI-SWITCH driver is compliant. |
|  | Vendor | Gets the the name of the vendor that supplies the NI-SWITCH driver. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverIdentity Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm language=enus -->
## TOPIC 00179: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchDriverOperation Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchDriverOperation](t_nationalinstruments_modularinstruments_niswitch_switchdriveroperation.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | Cache | Gets or sets whether to cache the value of properties. |
|  | DriverSetup | Gets the driver setup string used to set the initial values for properties that are specific to NI-SWITCH. |
|  | InterchangeCheck | Gets or sets whether to perform interchangeability checking and retrieve interchangeability warnings. |
|  | IOResourceDescriptor | Gets the resource name that the NI-SWITCH uses to identify the physical device. |
|  | LogicalName | Gets the logical name that you specified when opening the current IVI session. |
|  | QueryInstrumentStatus | Gets or sets whether NI-SWITCH queries the NI-SWITCH device status after each operation. |
|  | RangeCheck | Gets or sets whether to validate proper values and method parameters. If you enable this property, NI-SWITCH validates the parameter values that you pass to NI-SWITCH methods. |
|  | RecordCoercions | Gets or sets whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. |
|  | Simulate | Gets or sets a value which indicates whether to simulate NI-SWITCH I/O operations. |
|  | SynchronizeCallbacks | Gets or sets how events and callback delegates are invoked. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchDriverOperation Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm language=enus -->
## TOPIC 00180: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchRevisionQueryResult Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchRevisionQueryResult](t_nationalinstruments_modularinstruments_niswitch_switchrevisionqueryresult.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | FirmwareRevision | Gets a string that contains the firmware revision information for the NI-SWITCH instrument that you are currently using. |
|  | InstrumentRevision | Gets a string that contains version information about the NI-SWITCH driver. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchRevisionQueryResult Structure

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline.htm language=enus -->
## TOPIC 00181: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanAdvancedOutputBusLine Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScanAdvancedOutputBusLine](t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputbusline.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | None | Gets a value that indicates no implicit action on scanning connections. |
|  | Ttl0 | Gets a value corresponding to a trigger on the PXI_TRIG0 line. The switch waits until it receives a trigger on the PXI_TRIG0 line before processing the next entry in the scan list. |
|  | Ttl1 | Gets a value corresponding to a trigger on the PXI_TRIG1 line. The switch waits until it receives a trigger on the PXI_TRIG1 line before processing the next entry in the scan list. |
|  | Ttl2 | Gets a value corresponding to a trigger on the PXI_TRIG2 line. The switch waits until it receives a trigger on the PXI_TRIG2 line before processing the next entry in the scan list. |
|  | Ttl3 | Gets a value corresponding to a trigger on the PXI_TRIG3 line. The switch waits until it receives a trigger on the PXI_TRIG3 line before processing the next entry in the scan list. |
|  | Ttl4 | Gets a value corresponding to a trigger on the PXI_TRIG4 line. The switch waits until it receives a trigger on the PXI_TRIG4 line before processing the next entry in the scan list. |
|  | Ttl5 | Gets a value corresponding to a trigger on the PXI_TRIG5 line. The switch waits until it receives a trigger on the PXI_TRIG5 line before processing the next entry in the scan list. |
|  | Ttl6 | Gets a value corresponding to a trigger on the PXI_TRIG6 line. The switch waits until it receives a trigger on the PXI_TRIG6 line before processing the next entry in the scan list. |
|  | Ttl7 | Gets a value corresponding to a trigger on the PXI_TRIG7 line. The switch waits until it receives a trigger on the PXI_TRIG7 line before processing the next entry in the scan list. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanAdvancedOutputBusLine Class

NationalInstruments.ModularInstruments.NISwitch Namespace

<!--NI_TOPIC bundle=ni-switch-19.0-net-framework-40-api-ref path=ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputconnector.htm language=enus -->
## TOPIC 00182: Properties

- bundle_id: `ni-switch-19.0-net-framework-40-api-ref`
- source_path: `ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputconnector.htm`
- source_url: https://docs-be.ni.com/bundle/ni-switch-19.0-net-framework-40-api-ref/raw/resource/enus/ninetswitchfx40ref/html/properties_t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputconnector.htm
- document_id: `ni-switch-19.0-net-framework-40-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanAdvancedOutputConnector Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The [SwitchScanAdvancedOutputConnector](t_nationalinstruments_modularinstruments_niswitch_switchscanadvancedoutputconnector.htm) type exposes the following members.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Properties

|  | Name | Description |
| --- | --- | --- |
|  | FrontConnector | Gets a value corresponding to a trigger on the front connector. |
|  | RearConnector | Gets a value corresponding to a trigger on the rear connector. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SwitchScanAdvancedOutputConnector Class

NationalInstruments.ModularInstruments.NISwitch Namespace
