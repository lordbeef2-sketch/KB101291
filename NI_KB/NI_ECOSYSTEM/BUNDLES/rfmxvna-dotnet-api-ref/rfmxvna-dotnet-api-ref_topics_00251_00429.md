# NI DOCUMENT BUNDLE: rfmxvna-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxvna-dotnet-api-ref start=251 end=429 -->
<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodulatorwidth__string-double.html language=enus -->
## TOPIC 00251: SetPulseModulatorWidth(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodulatorwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodulatorwidth__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the duration for which the pulse is in ON state when you set the PulseModeEnabled method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulseModulatorWidth(string selectorString, double value)RemarksThis method sets the value of PulseMo

### SetPulseModulatorWidth(string, double)

Sets the duration for which the pulse is in ON state when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseModulatorWidth(string selectorString, double value)

#### Remarks

This method sets the value of [PulseModulatorWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.0001s.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the duration for which the pulse is in ON state when you set the PulseModeEnabled method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseperiod__string-double.html language=enus -->
## TOPIC 00252: SetPulsePeriod(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseperiod__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseperiod__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulsePeriod(string selectorString, double value)RemarksThis method sets the value of PulsePeriod attribut

### SetPulsePeriod(string, double)

Sets the interval after which the pulse repeats when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulsePeriod(string selectorString, double value)

#### Remarks

This method sets the value of [PulsePeriod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.001s.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsetriggertype__string-rfmxvnamxpulsetriggertype.html language=enus -->
## TOPIC 00253: SetPulseTriggerType(string, RFmxVnaMXPulseTriggerType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsetriggertype__string-rfmxvnamxpulsetriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsetriggertype__string-rfmxvnamxpulsetriggertype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the pulse trigger type. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulseTriggerType(string selectorString, RFmxVnaMXPulseTriggerType value)RemarksThis method sets the value of PulseTriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStringstrin

### SetPulseTriggerType(string, RFmxVnaMXPulseTriggerType)

Sets the pulse trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseTriggerType(string selectorString, RFmxVnaMXPulseTriggerType value)

#### Remarks

This method sets the value of [PulseTriggerType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsetriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXPulseTriggerType | Specifies the pulse trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setreadyfortriggereventoutputterminal__string-string.html language=enus -->
## TOPIC 00254: SetReadyForTriggerEventOutputTerminal(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setreadyfortriggereventoutputterminal__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setreadyfortriggereventoutputterminal__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the destination terminal for the Ready For Trigger event. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetReadyForTriggerEventOutputTerminal(string selectorString, string value)RemarksThis method sets the value of ReadyForTriggerEventOutputTerminal attribute.The default value is ""

### SetReadyForTriggerEventOutputTerminal(string, string)

Sets the destination terminal for the Ready For Trigger event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetReadyForTriggerEventOutputTerminal(string selectorString, string value)

#### Remarks

This method sets the value of [ReadyForTriggerEventOutputTerminal](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "" (empty string).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the destination terminal for exported Ready For Trigger event. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setresultfetchtimeout__string-double.html language=enus -->
## TOPIC 00255: SetResultFetchTimeout(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setresultfetchtimeout__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setresultfetchtimeout__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetResultFetchTimeo

### SetResultFetchTimeout(string, double)

Sets the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetResultFetchTimeout(string selectorString, double value)

#### Remarks

This method sets the value of [ResultFetchTimeout](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentdwelltime__string-double.html language=enus -->
## TOPIC 00256: SetSegmentDwellTime(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentdwelltime__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentdwelltime__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, r

### SetSegmentDwellTime(string, double)

Sets the dwell time for the selected segment when Segment Dwell Time Enabled method is set to *True*. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentDwellTime(string selectorString, double value)

#### Remarks

This method sets the value of [SegmentDwellTime](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | double | Specifies the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentifbandwidth__string-double.html language=enus -->
## TOPIC 00257: SetSegmentIFBandwidth(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentifbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentifbandwidth__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 70

### SetSegmentIFBandwidth(string, double)

Sets the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to *True*. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentIFBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [SegmentIFBandwidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 100kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | double | Specifies the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentifbandwidthenabled__string-rfmxvnamxsegmentifbandwidthenabled.html language=enus -->
## TOPIC 00258: SetSegmentIFBandwidthEnabled(string, RFmxVnaMXSegmentIFBandwidthEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentifbandwidthenabled__string-rfmxvnamxsegmentifbandwidthenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentifbandwidthenabled__string-rfmxvnamxsegmentifbandwidthenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSegmentIF

### SetSegmentIFBandwidthEnabled(string, RFmxVnaMXSegmentIFBandwidthEnabled)

Sets whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to [False](nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentifbandwidthenabled.html), a common value will be used across all segments specified by IF Bandwidth (Hz) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentIFBandwidthEnabled(string selectorString, RFmxVnaMXSegmentIFBandwidthEnabled value)

#### Remarks

This method sets the value of [SegmentIFBandwidthEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSegmentIFBandwidthEnabled | Specifies whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentnumberoffrequencypoints__string-int.html language=enus -->
## TOPIC 00259: SetSegmentNumberOfFrequencyPoints(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentnumberoffrequencypoints__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentnumberoffrequencypoints__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of frequency points of the segment at which the measurement needs to be performed. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSegmentNumberOfFrequencyPoints(string selectorString, int value)RemarksThis method sets the value of SegmentNumberOfFrequencyPoints attribut

### SetSegmentNumberOfFrequencyPoints(string, int)

Sets the number of frequency points of the segment at which the measurement needs to be performed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentNumberOfFrequencyPoints(string selectorString, int value)

#### Remarks

This method sets the value of [SegmentNumberOfFrequencyPoints](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 21.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | int | Specifies the number of frequency points of the segment at which the measurement needs to be performed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentpowerlevel__string-double.html language=enus -->
## TOPIC 00260: SetSegmentPowerLevel(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentpowerlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentpowerlevel__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to True. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSegmentPowerLevel(string selectorString, double value)RemarksThis method sets the val

### SetSegmentPowerLevel(string, double)

Sets the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to *True*. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentPowerLevel(string selectorString, double value)

#### Remarks

This method sets the value of [SegmentPowerLevel](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is -10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number, signal number and port number. Example: "segment0" or "" or "port0" or "segment0/port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to True. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentpowerlevelenabled__string-rfmxvnamxsegmentpowerlevelenabled.html language=enus -->
## TOPIC 00261: SetSegmentPowerLevelEnabled(string, RFmxVnaMXSegmentPowerLevelEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentpowerlevelenabled__string-rfmxvnamxsegmentpowerlevelenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentpowerlevelenabled__string-rfmxvnamxsegmentpowerlevelenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSegm

### SetSegmentPowerLevelEnabled(string, RFmxVnaMXSegmentPowerLevelEnabled)

Sets whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to [False](nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentpowerlevelenabled.html), a common value will be used across all segments specified by Power Level(dBm) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentPowerLevelEnabled(string selectorString, RFmxVnaMXSegmentPowerLevelEnabled value)

#### Remarks

This method sets the value of [SegmentPowerLevelEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSegmentPowerLevelEnabled | Specifies whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentstartfrequency__string-double.html language=enus -->
## TOPIC 00262: SetSegmentStartFrequency(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentstartfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentstartfrequency__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSegmentStartFrequency(string selectorString, double value)RemarksThis method sets the value of SegmentStartFrequency at

### SetSegmentStartFrequency(string, double)

Sets the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentStartFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [SegmentStartFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1G.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | double | Specifies the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentstopfrequency__string-double.html language=enus -->
## TOPIC 00263: SetSegmentStopFrequency(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentstopfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmentstopfrequency__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSegmentStopFrequency(string selectorString, double value)RemarksThis method sets the value of SegmentStopFrequency att

### SetSegmentStopFrequency(string, double)

Sets the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentStopFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [SegmentStopFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 2G.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | double | Specifies the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmenttestreceiverattenuation__string-double.html language=enus -->
## TOPIC 00264: SetSegmentTestReceiverAttenuation(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmenttestreceiverattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmenttestreceiverattenuation__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to True. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver.

### SetSegmentTestReceiverAttenuation(string, double)

Sets the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to *True*. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentTestReceiverAttenuation(string selectorString, double value)

#### Remarks

This method sets the value of [SegmentTestReceiverAttenuation](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number, signal number and port number. Example: "segment0" or "" or "port0" or "segment0/port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to True. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmenttestreceiverattenuationenabled__string-rfmxvnamxsegmenttestreceiverattenuationenabled.html language=enus -->
## TOPIC 00265: SetSegmentTestReceiverAttenuationEnabled(string, RFmxVnaMXSegmentTestReceiverAttenuationEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmenttestreceiverattenuationenabled__string-rfmxvnamxsegmenttestreceiverattenuationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsegmenttestreceiverattenuationenabled__string-rfmxvnamxsegmenttestreceiverattenuationenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. SyntaxNamespace: NationalInstru

### SetSegmentTestReceiverAttenuationEnabled(string, RFmxVnaMXSegmentTestReceiverAttenuationEnabled)

Sets whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to [False](nationalinstruments-rfmx-vnamx-rfmxvnamxsegmenttestreceiverattenuationenabled.html), a common value will be used across all segments specified by Test Receiver Attenuation (dB) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSegmentTestReceiverAttenuationEnabled(string selectorString, RFmxVnaMXSegmentTestReceiverAttenuationEnabled value)

#### Remarks

This method sets the value of [SegmentTestReceiverAttenuationEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSegmentTestReceiverAttenuationEnabled | Specifies whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setsourcepowermode__string-rfmxvnamxsourcepowermode.html language=enus -->
## TOPIC 00266: SetSourcePowerMode(string, RFmxVnaMXSourcePowerMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setsourcepowermode__string-rfmxvnamxsourcepowermode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setsourcepowermode__string-rfmxvnamxsourcepowermode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to make VNA measurements with source turned off. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSourcePowerMode(string selectorString, RFmxVnaMXSourcePowerMode value)RemarksThis method sets the value of SourcePowerMode attribute.The default value is (format type="bold")RFM

### SetSourcePowerMode(string, RFmxVnaMXSourcePowerMode)

Sets whether to make VNA measurements with source turned off.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSourcePowerMode(string selectorString, RFmxVnaMXSourcePowerMode value)

#### Remarks

This method sets the value of [SourcePowerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is (format type="bold")RFMXVNA_VAL_Auto(/format).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSourcePowerMode | Specifies whether to make VNA measurements with source turned off. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setstartfrequency__string-double.html language=enus -->
## TOPIC 00267: SetStartFrequency(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setstartfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setstartfrequency__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetStartFrequency(string selectorString, double value)RemarksThis method sets the value of StartFrequency attribute.The default value is

### SetStartFrequency(string, double)

Sets the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetStartFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [StartFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1G.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setstopfrequency__string-double.html language=enus -->
## TOPIC 00268: SetStopFrequency(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setstopfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setstopfrequency__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the highest frequency at which the measurement needs to be performed. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetStopFrequency(string selectorString, double value)RemarksThis method sets the value of StopFrequency attribute.The default value is 2

### SetStopFrequency(string, double)

Sets the highest frequency at which the measurement needs to be performed. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetStopFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [StopFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 2G.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the highest frequency at which the measurement needs to be performed. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-settestreceiverattenuation__string-double.html language=enus -->
## TOPIC 00269: SetTestReceiverAttenuation(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-settestreceiverattenuation__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-settestreceiverattenuation__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Te

### SetTestReceiverAttenuation(string, double)

Sets the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetTestReceiverAttenuation(string selectorString, double value)

#### Remarks

This method sets the value of [TestReceiverAttenuation](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number, signal number and port number. Example: "segment0" or "" or "port0" or "segment0/port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-settriggermode__string-rfmxvnamxtriggermode.html language=enus -->
## TOPIC 00270: SetTriggerMode(string, RFmxVnaMXTriggerMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-settriggermode__string-rfmxvnamxtriggermode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-settriggermode__string-rfmxvnamxtriggermode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger mode. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetTriggerMode(string selectorString, RFmxVnaMXTriggerMode value)RemarksThis method sets the value of TriggerMode attribute.The default value is Signal.ParametersNameTypeDescriptionselectorStringstringPass an empty stri

### SetTriggerMode(string, RFmxVnaMXTriggerMode)

Sets the trigger mode.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetTriggerMode(string selectorString, RFmxVnaMXTriggerMode value)

#### Remarks

This method sets the value of [TriggerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Signal](nationalinstruments-rfmx-vnamx-rfmxvnamxtriggermode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXTriggerMode | Specifies the trigger mode. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-settriggertype__string-rfmxvnamxtriggertype.html language=enus -->
## TOPIC 00271: SetTriggerType(string, RFmxVnaMXTriggerType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-settriggertype__string-rfmxvnamxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-settriggertype__string-rfmxvnamxtriggertype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetTriggerType(string selectorString, RFmxVnaMXTriggerType value)RemarksThis method sets the value of TriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStringstringPass an empty string

### SetTriggerType(string, RFmxVnaMXTriggerType)

Sets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetTriggerType(string selectorString, RFmxVnaMXTriggerType value)

#### Remarks

This method sets the value of [TriggerType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-vnamx-rfmxvnamxtriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXTriggerType | Specifies the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-signalconfigurationname.html language=enus -->
## TOPIC 00272: SignalConfigurationName

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-signalconfigurationname.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-signalconfigurationname.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the signal configuration name. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic string SignalConfigurationName { get; }RemarksReturns a string representing the signal configuration name

### SignalConfigurationName

Gets the signal configuration name.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public string SignalConfigurationName { get; }

#### Remarks

Returns a string representing the signal configuration name

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-signalconfigurationtype.html language=enus -->
## TOPIC 00273: SignalConfigurationType

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-signalconfigurationtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-signalconfigurationtype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Type object for RFmxVnaMX. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic Type SignalConfigurationType { get; }RemarksReturns the type of signal configuration object.

### SignalConfigurationType

Gets the Type object for RFmxVnaMX.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public Type SignalConfigurationType { get; }

#### Remarks

Returns the type of signal configuration object.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-waitformeasurementcomplete__string-double.html language=enus -->
## TOPIC 00274: WaitForMeasurementComplete(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-waitformeasurementcomplete__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-waitformeasurementcomplete__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int WaitForMeasurementComplete(string selectorString, double timeout)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the r

### WaitForMeasurementComplete(string, double)

Waits for the specified number for seconds for all the measurements to complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int WaitForMeasurementComplete(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildSParameterString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the method waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-waves.html language=enus -->
## TOPIC 00275: Waves

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-waves.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-waves.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxVnaMXWaves instance that represents the Waves measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic RFmxVnaMXWaves Waves { get; }

### Waves

Gets the [RFmxVnaMXWaves](nationalinstruments-rfmx-vnamx-rfmxvnamxwaves.html) instance that represents the Waves measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public [RFmxVnaMXWaves](nationalinstruments-rfmx-vnamx-rfmxvnamxwaves.html) Waves { get; }

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx.html language=enus -->
## TOPIC 00276: RFmxVnaMX Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines a root class which is used to identify and control Vna signal configuration. Derives fromISignalConfigurationIDisposableSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMX : ISignalConfiguration, IDisposablePropertiesNameDescriptionIsDisposedGets a value that indicates whet

### RFmxVnaMX Class

Defines a root class which is used to identify and control Vna signal configuration.

#### Derives from

- ISignalConfiguration
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMX : ISignalConfiguration, IDisposable

#### Properties

| Name | Description |
| --- | --- |
| IsDisposed | Gets a value that indicates whether the signal has been disposed. |
| Marker | Gets the RFmxVnaMXMarker instance that represents the Marker measurement. |
| SignalConfigurationName | Gets the signal configuration name. |
| SignalConfigurationType | Gets the Type object for RFmxVnaMX. |
| SParams | Gets the RFmxVnaMXSParams instance that represents the SParams measurement. |
| Waves | Gets the RFmxVnaMXWaves instance that represents the Waves measurement. |

#### Methods

| Name | Description |
| --- | --- |
| AbortMeasurements(string) | Stops acquisition and measurements associated with signal instance that you specify in the selectorString parameter, which were previously initiated by the Initiate(string, string) or measurement read methods. Calling this method is optional, unless you want to stop a measurement before it is complete. This method executes even if there is an incoming error. |
| AutoDetectvCalOrientation(string) | Automatically detects the vCal ports connected to the VNA ports and writes the CorrectionCalibrationCalkitElectronicOrientation property. Call this function before calling the CalibrationInitiate(string) method. Auto detection of vCal orientation initially occurs at the midpoint of the frequency range specified for the calibration. If the connection is not detected, it retries at the lowest frequnecy in the configured range. The auto detection may fail if the power level at the vCal module is too low. If it fails, use the CorrectionCalibrationCalkitElectronicOrientation property to configure the orientation manually. |
| AutoPortExtensionMeasure(string, RFmxVnaMXCorrectionPortExtensionAutoStandard, string) | Automatically determine the fixture delay and loss (optional) values by measuring the standard at the configured port. The calculated delay and loss values are used to set the SetCorrectionPortExtensionDelay(string, double), SetCorrectionPortExtensionLossDCLoss(string, double), SetCorrectionPortExtensionLoss1(string, double) and SetCorrectionPortExtensionLoss2(string, double) methods. Call this method after calibrating the VNA port, where port extension is required, to obtain more accurate delay and loss estimates. An ideal OPEN and SHORT standard, with zero loss and delay, is assumed. Therefore, the accuracy depends on the quality of the standard. To measure either OPEN or SHORT, call AutoPortExtensionReset(string) before measuring the standard. When both OPEN and SHORT standards are measured, the average of the calculated delay and loss values are entered. You must call Initiate(string, string) afterwards to obtain the compensated measurement results. |
| AutoPortExtensionReset(string) | Resets the measured standard data used for automatic port extension. Before measuring an OPEN or SHORT standard, you must reset any previously measured standard data. |
| CalibrationAbort(string) | Stops the calibration, which was previously initiated by CalibrationInitiate(string) method, for the signal instance that you specify in the selectorString parameter. Calling this method is optional, unless you want to stop a calibration before it is complete. This method executes even if there is an incoming error. |
| CalibrationAcquire(string, double) | Measures one or more calibration standards for the specified calibration step. You can call this method only after required calibration steps are determined by RFmx when you call CalibrationInitiate(string). One successful call to CalibrationInitiate(string) is sufficient for all subsequent calls to this method. When CorrectionCalibrationCalkitType is Electronic, RFmx uses all relevant 1-port and 2-port calibration standards in the selected electronic calibration module. A single call to this method measures all such cal standards in the electronic calibration module. For example, if you use NI CAL-5501 electronic calkit to calibrate NI PXIe-5633 by using SOLT calibration method, you only need to perform 1 manual connection to connect the 2 cal module ports to 2 VNA ports. After setting up the required connection, a single call to this method measures all relevant cal standards automatically. When CorrectionCalibrationCalkitType is Mechanical, RFmx can measure for only one cal standard for each cal step. Specify the active cal step in the Selector String. Use BuildCalstepString(string, int) method to build cal step string. For example, if you calibrate the NI PXIe-5633 using a mechanical calkit containing a Short, Open, Load and Thru discrete cal standards, then you must perform 7 distinct manual connections, call this method once per cal step, which in-turn instructs you to connect an appropriate 1 or 2-port cal standard to the VNA port(s). You must call this method at least once for each cal step to measure corresponding calibration standard. If you call this method more than once for a given cal step, the cal standard measurement data for the latest call overwrites the previously measured data for the same standard. RFmx stores the cal standard measurement data which is later used to compute error correction terms when you call RFmxVNA Calibration Save method. |
| CalibrationInitiate(string) | Determines the set of calibration standard measurements required for performing calibration with the sweep and calibration settings that you configure. Call this method after configuring all the appropriate sweep and calibration settings such as Frequency Settings, Power Level and Test Receiver attenuation settings, IF Bandwidth, Calkit and Cal Method related settings etc. After you call this method, you can query number of distinct physical connection steps using CorrectionCalibrationStepCount. To understand the physical connection required in a given cal step, query CorrectionCalibrationStepDescription method. You can refer to following sequence of operations to better understand the usage of this method in a typical calibration routine. [START] -> ... -> [Select Measurement] -> [Configure Sweep Settings] -> [Configure Calibration Settings] -> [Call RFmxVNA Calibration Initiate method] -> [Query CorrectionCalibrationStepCount] -> [Query and make connection as per CorrectionCalibrationStepDescription for Step(m)] -> [Call CalibrationAcquire(string, double) method for Step(m)] -> [Query and make connection as per CorrectionCalibrationStepDescription for Step(n)] -> [Call CalibrationAcquire(string, double) method for Step(n)] -> [Call CalibrationSave(string, string) method] -> [Call CalsetSaveToFile(string, string, string) method] -> ...-> [END]. You must select SParams or Wave measurement before calling this method. After calling this method, if you change any sweep and calibration setting, you must call this method again to commit the change(s) to said sweep and calibration setting(s). |
| CalibrationSave(string, string) | Computes error-correction terms and saves the calset in memory. Call this method after all calibration standards have been measured using CalibrationAcquire(string, double) method. If you do not specify Calset Name input parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. To perform another calibration after you call this method, you must call RFmxVNA Calibration Initiate method again. |
| CalkitManagerCalkitAddCalibrationElement(string, string) | Adds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit. |
| CalkitManagerCalkitAddConnector(string, string) | Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit. |
| CalkitManagerCalkitCalibrationElementDelayModelGetDelay(string, out double) | Returns the Delay of a Calibration Element defined by the Delay Model. |
| CalkitManagerCalkitCalibrationElementDelayModelSetDelay(string, double) | Defines the Delay of a Calibration Element defined by the Delay Model. |
| CalkitManagerCalkitCalibrationElementGetDescription(string, out string) | Returns the description for a Calibration Element of a specific Calkit. |
| CalkitManagerCalkitCalibrationElementGetMaximumFrequency(string, out double) | Returns the Maximum Frequency of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementGetMinimumFrequency(string, out double) | Returns the Minimum Frequency of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementGetPortConnectors(string, ref string[]) | Returns the array of Connectors associated with the Calibration Element. |
| CalkitManagerCalkitCalibrationElementGetSParameterDefinition(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition) | Returns the S-Parameter definition of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementGetTypes(string, ref RFmxVnaMXCalkitManagerCalkitCalibrationElementType[]) | Returns the type(s) of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementReflectModelGetC0(string, out double) | Returns the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| CalkitManagerCalkitCalibrationElementReflectModelGetC1(string, out double) | Returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| CalkitManagerCalkitCalibrationElementReflectModelGetC2(string, out double) | Returns the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| CalkitManagerCalkitCalibrationElementReflectModelGetC3(string, out double) | Returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| CalkitManagerCalkitCalibrationElementReflectModelGetModelType(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType) | Returns the model type of of the 1-port reflect standard. |
| CalkitManagerCalkitCalibrationElementReflectModelGetOffsetDelay(string, out double) | Returns the offset delay. |
| CalkitManagerCalkitCalibrationElementReflectModelGetOffsetLoss(string, out double) | Returns the offset loss. |
| CalkitManagerCalkitCalibrationElementReflectModelGetReferenceImpedance(string, out double) | Returns the reference impedance. |
| CalkitManagerCalkitCalibrationElementReflectModelGetSParamAvailability(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability) | Returns the S-Parameter availability. |
| CalkitManagerCalkitCalibrationElementReflectModelSetC0(string, double) | Specifies the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| CalkitManagerCalkitCalibrationElementReflectModelSetC1(string, double) | Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| CalkitManagerCalkitCalibrationElementReflectModelSetC2(string, double) | Specifies the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| CalkitManagerCalkitCalibrationElementReflectModelSetC3(string, double) | Specifies the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| CalkitManagerCalkitCalibrationElementReflectModelSetModelType(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType) | Specifies the model type of the 1-port reflect standard. |
| CalkitManagerCalkitCalibrationElementReflectModelSetOffsetDelay(string, double) | Specifies the offset delay. |
| CalkitManagerCalkitCalibrationElementReflectModelSetOffsetLoss(string, double) | Specifies the offset loss. |
| CalkitManagerCalkitCalibrationElementReflectModelSetOffsetZ0(string, double) | Specifies the impedance of the offset. |
| CalkitManagerCalkitCalibrationElementReflectModelSetReferenceImpedance(string, double) | Specifies the reference impedance. |
| CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability) | Specifies the S-Parameter availability. |
| CalkitManagerCalkitCalibrationElementSetDescription(string, string) | Sets the description for a Calibration Element of a specific Calkit. |
| CalkitManagerCalkitCalibrationElementSetMaximumFrequency(string, double) | Sets the Maximum Frequency of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementSetMinimumFrequency(string, double) | Sets the Minimum Frequency of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementSetPortConnectors(string, string[]) | Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementSetSParameterDefinition(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition) | Defines the way how the S-Parameters of the Calibration Element are specified. |
| CalkitManagerCalkitCalibrationElementSetTypes(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementType[]) | Sets the type(s) of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementSParameterGetFrequency(string, ref double[]) | Returns the frequency array for the S-Parameter definition of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementSParameterGetS11(string, ref ComplexDouble[]) | Returns the S11 S-Parameter for the calibration element. |
| CalkitManagerCalkitCalibrationElementSParameterGetS12(string, ref ComplexDouble[]) | Returns the S12 S-Parameter for the calibration element. |
| CalkitManagerCalkitCalibrationElementSParameterGetS21(string, ref ComplexDouble[]) | Returns the S21 S-Parameter for the calibration element. |
| CalkitManagerCalkitCalibrationElementSParameterGetS22(string, ref ComplexDouble[]) | Returns the S22 S-Parameter for the calibration element. |
| CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability) | Returns the S-Parameter availability. |
| CalkitManagerCalkitCalibrationElementSParameterSetFrequency(string, double[]) | Defines the frequency array for the S-Parameter definition of the Calibration Element. |
| CalkitManagerCalkitCalibrationElementSParameterSetFromFile(string, string) | Defines the touchstone file name from which the S-Parameter shall be read and assigned to the Calibration Element. |
| CalkitManagerCalkitCalibrationElementSParameterSetS11(string, ComplexDouble[]) | Sets the S11 S-Parameter for the calibration element. |
| CalkitManagerCalkitCalibrationElementSParameterSetS12(string, ComplexDouble[]) | Sets the S12 S-Parameter for the calibration element. |
| CalkitManagerCalkitCalibrationElementSParameterSetS21(string, ComplexDouble[]) | Sets the S21 S-Parameter for the calibration element. |
| CalkitManagerCalkitCalibrationElementSParameterSetS22(string, ComplexDouble[]) | Sets the S22 S-Parameter for the calibration element. |
| CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability) | Defines the S-Parameter availability. |
| CalkitManagerCalkitConnectorGetDescription(string, out string) | Returns the description of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorGetGender(string, out RFmxVnaMXCalkitManagerCalkitConnectorGender) | Returns the Gender of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorGetImpedance(string, out double) | Returns the Impedance of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorGetMaximumFrequency(string, out double) | Returns the Maximum Frequency of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorGetMinimumFrequency(string, out double) | Returns the Minimum Frequency of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorGetType(string, out string) | Returns the Type of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorSetDescription(string, string) | Sets the description for a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorSetGender(string, RFmxVnaMXCalkitManagerCalkitConnectorGender) | Sets the Gender of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorSetImpedance(string, double) | Sets the Impedance of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorSetMaximumFrequency(string, double) | Sets the Maximum Frequency of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorSetMinimumFrequency(string, double) | Sets the Minimum Frequency of a Connector of a specific Calkit. |
| CalkitManagerCalkitConnectorSetType(string, string) | Sets the Type of a Connector of a specific Calkit. Connector type is a user defined string (for example 'SMA', '1.8mm', etc.). |
| CalkitManagerCalkitGetCalibrationElementIDs(string, ref string[]) | Returns a list of Calibration Element IDs of all Calibration Elements of the Calkit. |
| CalkitManagerCalkitGetConnectorIDs(string, ref string[]) | Returns the list of Connector IDs for all connectors in the Calkit. |
| CalkitManagerCalkitGetDescription(string, out string) | Returns the description of the Calkit. |
| CalkitManagerCalkitGetLrlLineAutoChar(string, out bool) | Returns whether line parameters are automatically characterized during LRL calibration. |
| CalkitManagerCalkitGetTrlReferencePlane(string, out RFmxVnaMXCalkitManagerCalkitTrlReferencePlane) | Returns the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration. |
| CalkitManagerCalkitGetVersion(string, out string) | Returns the version string of the Calkit. |
| CalkitManagerCalkitRemoveCalibrationElement(string, string) | Removes the Calibration Element identified by its Calibration Element ID from the Calkit. |
| CalkitManagerCalkitRemoveConnector(string, string) | Removes a Connector element from the Calkit. |
| CalkitManagerCalkitSetDescription(string, string) | Sets the description for the Calkit. |
| CalkitManagerCalkitSetLrlLineAutoChar(string, bool) | Configures whether line parameters are automatically characterized during LRL calibration. LRL line auto characterization is applicable only when the Line standards have the same characteristic impedance. |
| CalkitManagerCalkitSetTrlReferencePlane(string, RFmxVnaMXCalkitManagerCalkitTrlReferencePlane) | Sets the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration. Use Reflect, if the Thru standard is uncertainly known and the Reflect standard is well defined. Otherwise use the Thru standard to define the reference plane. |
| CalkitManagerCalkitSetVersion(string, string) | Sets the version string for the Calkit. |
| CalkitManagerCreateCalkit(string, string) | Creates a new empty Calkit with the user defined Calkit ID in Calkit Manager. The user defined Calkit ID has to be unique among all Calkits in Calkit Manager. |
| CalkitManagerExportCalkit(string, string, string) | Exports a Calkit to file. |
| CalkitManagerGetCalkitIDs(string, ref string[]) | Returns a list of Calkit IDs for all Calkits currently loaded in Calkit Manager. |
| CalkitManagerImportCalkit(string, string) | Imports a Calkit file into the Calkit Manager. |
| CalkitManagerRemoveCalkit(string, string) | Removes a Calkit from Calkit Manager. |
| CalkitManagerValidateCalkit(string, string) | Validates the consistency of a Calkit definition and returns the status of the validation. |
| CalsetEmbedFixtureS2p(string, string, string, string, RFmxVnaMXSParameterOrientation, string) | Embeds the inverse of a given fixture network into a specified calset.The typical use case for this utility is to remove the effect of an adapter that was present during calibration but is not present during later measurements from the Calset itself such that corrected measurements can be performed without considering the calibration adapter in the measurement de-embedding. |
| CalsetGetErrorTerm(string, string, RFmxVnaMXCalErrorTerm, string, string, ref ComplexSingle[]) | Returns values for a specific error term from either the default calset of the specified signal or a named calset accessible across all signals. |
| CalsetGetFrequencyGrid(string, string, RFmxVnaMXCalFrequencyGrid, ref double[]) | Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals. |
| CalsetLoadFromFile(string, string, string) | Loads calset from a calset file (*.ncst), either to the default calset of the specified signal or to a named calset accessible across all signals. |
| CalsetSaveToFile(string, string, string) | Saves to a calset file (*.ncst), either the default calset of the specified signal or a named calset accessible across all signals and corresponding relevant stimulus settings that were used to perform calibration. |
| CheckMeasurementStatus(string, out bool) | Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| ClearAllNamedResults(string) | Clears all results for the current signal instance. |
| ClearCalset(string, string) | Clears either the default calset of the specified signal or a named calset accessible across all signals. |
| ClearMeasurementMemoryNames(string) | Clears the measurement memory for the measurement number specified by the Selector String. If Measurement memory name is "" (empty string): RFmx clears all the measurement memories associated with the measurement number. If measurement memory name is non-empty string: RFmx clears the specified measurement memory. |
| ClearNamedResult(string) | Clears a result instance specified by the result name in the Selector String parameter. |
| CloneSignalConfiguration(string, out RFmxVnaMX) | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| Commit(string) | Commits settings to the hardware. Calling this method is optional. RFmxVNA commits settings to the hardware when you call the Initiate(string, string) method. |
| ConfigureCalFixtureData(string, double[], ComplexDouble[], ComplexDouble[], ComplexDouble[], ComplexDouble[], RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation) |  |
| ConfigureCorrectionPortSubset(string, string[]) | Configures the subset of ports, that are selected for correction when you set CorrectionEnabled method to True and CorrectionPortSubsetEnabled method to True. |
| CopyCalset(string, string, string) | Copies into a new calset either from the default calset of the specified signal or a named calset accessible across all signals. |
| CopyDataToMeasurementMemory(string, string) | Copies data into specified measurement memory from measurement result specified by the selector string. This method will overwrite the contents of the measurement memory if it already exists. |
| DeleteSignalConfiguration() | Deletes an instance of a signal. |
| DeselectActiveCalset(string) | Deselects the active calset of the specified signal. You can select an active calset again using SelectActiveCalset(string, string, RFmxVnaMXRestoreConfiguration) method. |
| Dispose() | Deletes the signal configuration if it is not the default signal configuration and clears any trace of the current signal configuration, if any. |
| GetAcquisitionChunkSize(string, out int) |  |
| GetAllCalsetNames(string, ref string[]) | Returns an array of calset names of all the available named calsets which are accessible across all signals. |
| GetAllNamedResultNames(string, out string[], out bool) | Gets the named result names of the signal that you specify in the selectorString parameter. |
| GetAttributeBool(string, int, out bool) | Gets the value of a Bool attribute. |
| GetAttributeComplexDoubleArray(string, int, ref ComplexDouble[]) | Gets the value of a ComplexDouble array attribute. |
| GetAttributeDouble(string, int, out double) | Gets the value of a Double attribute. |
| GetAttributeDoubleArray(string, int, ref double[]) | Gets the value of a double array attribute. |
| GetAttributeInt(string, int, out int) | Gets the value of an RFmx 32-bit integer (int32) attribute. |
| GetAttributeString(string, int, out string) | Gets the value of a of an RFmx string. |
| GetAutoIFBandwidthScalingEnabled(string, out RFmxVnaMXAutoIFBandwidthScalingEnabled) | Gets whether IF Bandwidth is scaled down at low frequencies. |
| GetAveragingCount(string, out int) | Gets the number of times each measurement is repeated and averaged-over. This method is used only when you set the AveragingEnabled method to True. |
| GetAveragingEnabled(string, out RFmxVnaMXAveragingEnabled) | Gets whether to enable averaging for the VNA measurement. |
| GetCorrectionCalibrationCalkitElectronicOrientation(string, out string) | Gets the orientation of the vCal fixture ports with respect to vCal ports. |
| GetCorrectionCalibrationCalkitElectronicResourceName(string, out string) | Gets the resource name of the electronic calibration module (vCal) used for calibration. |
| GetCorrectionCalibrationCalkitMechanicalName(string, out string) | Gets the name of the mechanical calkit used for measurement calibration when you set CorrectionCalibrationCalkitType method to Mechanical. |
| GetCorrectionCalibrationCalkitType(string, out RFmxVnaMXCorrectionCalibrationCalkitType) | Gets the type of calkit used for calibration. |
| GetCorrectionCalibrationConnectorType(string, out string) | Gets the connector type of the DUT. The specified connector type must match be same as that of the selected calkit. |
| GetCorrectionCalibrationEstimatedThruDelay(string, out double) | Gets the estimated Thru Delay when Thru Method is set to Undefined Thru or Undefined Thru Using Defined Thru. |
| GetCorrectionCalibrationFixtureS11(string, ref ComplexDouble[]) |  |
| GetCorrectionCalibrationFixtureS12(string, ref ComplexDouble[]) |  |
| GetCorrectionCalibrationFixtureS21(string, ref ComplexDouble[]) |  |
| GetCorrectionCalibrationFixtureS22(string, ref ComplexDouble[]) |  |
| GetCorrectionCalibrationFixtureSParameterOrientation(string, out RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation) |  |
| GetCorrectionCalibrationMethod(string, out RFmxVnaMXCorrectionCalibrationMethod) | Gets the calibration method. |
| GetCorrectionCalibrationPorts(string, out string[]) | Gets the ports requested for calibration. Use comma-separated list of ports to specify multiple ports. |
| GetCorrectionCalibrationStepCount(string, out int) | Gets the number of steps required to perform calibration. |
| GetCorrectionCalibrationStepDescription(string, out string) | Gets the description the calibration step. |
| GetCorrectionCalibrationStepPortAssignment(string, out string) |  |
| GetCorrectionCalibrationStepVCalOrientation(string, out string) |  |
| GetCorrectionCalibrationThruCoaxDelay(string, out double) | Gets the delay of the Thru mechanical standard when CorrectionCalibrationCalkitType method is set to Mechanical and Thru Method method is set to Auto or Undefined Thru. This value is expressed in seconds. |
| GetCorrectionCalibrationThruMethod(string, out RFmxVnaMXCorrectionCalibrationThruMethod) | Gets the Thru calibration method when Calibration Method method is set to SOLT. |
| GetCorrectionEnabled(string, out RFmxVnaMXCorrectionEnabled) | Gets whether to enable error correction for VNA measurement. |
| GetCorrectionInterpolationEnabled(string, out RFmxVnaMXCorrectionInterpolationEnabled) | Gets whether to enable interpolation of error terms for corrected VNA measurement. This method is used only when you set the CorrectionEnabled method to True. |
| GetCorrectionPortExtensionAutoFrequencyMode(string, out RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) | Gets the frequency mode over which the delay and loss (optional) values are determined. |
| GetCorrectionPortExtensionAutoLossEnabled(string, out RFmxVnaMXCorrectionPortExtensionAutoLossEnabled) | Gets whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. |
| GetCorrectionPortExtensionAutoRegularizationEnabled(string, out RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled) | Gets whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled) method to True. |
| GetCorrectionPortExtensionAutoStartFrequency(string, out double) | Gets the start frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |
| GetCorrectionPortExtensionAutoStopFrequency(string, out double) | Gets the stop frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |
| GetCorrectionPortExtensionDCLossEnabled(string, out RFmxVnaMXCorrectionPortExtensionDCLossEnabled) | Gets whether to compensate for the frequency-independent loss when Port Extension Enabled is set to True. |
| GetCorrectionPortExtensionDelay(string, out double) | Gets the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds. |
| GetCorrectionPortExtensionDelayDomain(string, out RFmxVnaMXCorrectionPortExtensionDelayDomain) | Gets the delay domain of the port extension when the Port Extension Enabled is set to True. |
| GetCorrectionPortExtensionDistance(string, out double) | Gets the port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is expressed in unit specified by CorrectionPortExtensionDistanceUnit. |
| GetCorrectionPortExtensionDistanceUnit(string, out RFmxVnaMXCorrectionPortExtensionDistanceUnit) | Gets the unit of port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. |
| GetCorrectionPortExtensionEnabled(string, out RFmxVnaMXCorrectionPortExtensionEnabled) | Gets whether to enable port extension for the VNA port. |
| GetCorrectionPortExtensionLoss1(string, out double) | Gets the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension. If the DC loss and one additional frequency loss, Loss1 at the frequency f1 is known, the total loss at frequency f can be approximated by: Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^0.5) This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. This value is expressed in dB. |
| GetCorrectionPortExtensionLoss1Enabled(string, out RFmxVnaMXCorrectionPortExtensionLoss1Enabled) | Gets whether to compensate for the frequency-dependent loss, Loss1, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True. |
| GetCorrectionPortExtensionLoss1Frequency(string, out double) | Gets the frequency at which Loss1 is applied and compensated. This method is used only when the CorrectionPortExtensionEnabled method is set to True and the CorrectionPortExtensionLoss1Enabled method is set to True. This value is expressed in Hz. |
| GetCorrectionPortExtensionLoss2(string, out double) | Gets the frequency-dependent loss, Loss2 in dB, to compensate as part of port extension. If in addition to the DC loss and frequency-dependent loss at one frequency (Loss1 at the frequency f1), the loss at a second frequency, Loss2 at frequency f2 is also known, the total loss at frequency f can be approximated by: Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^b) , where b = log[(abs((Loss1 - DC Loss) / (Loss2 - DC Loss)))] / log(f1 / f2) This method is used only when you set the CorrectionPortExtensionEnabled method to True, the CorrectionPortExtensionLoss1Enabled method is set to True and the CorrectionPortExtensionLoss2Enabled method is set to True. This value is expressed in dB. |
| GetCorrectionPortExtensionLoss2Enabled(string, out RFmxVnaMXCorrectionPortExtensionLoss2Enabled) | Gets whether to compensate for the frequency-dependent loss, Loss2, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. |
| GetCorrectionPortExtensionLoss2Frequency(string, out double) | Gets the frequency at which Loss2 is applied and compensated. This method is used only when the CorrectionPortExtensionEnabled method is set to True, the CorrectionPortExtensionLoss1Enabled method is set to True and the CorrectionPortExtensionLoss2Enabled method is set to True. This value is expressed in Hz. |
| GetCorrectionPortExtensionLossDCLoss(string, out double) | Gets the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB. |
| GetCorrectionPortExtensionVelocityFactor(string, out double) | Gets the velocity factor of port extension medium when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is unitless. |
| GetCorrectionPortSubsetEnabled(string, out RFmxVnaMXCorrectionPortSubsetEnabled) | Gets whether correction enabled for a subset of ports for which calibration data is avaialble in the calset. This property is used only when you set the CorrectionEnabled property to True. |
| GetCorrectionPortSubsetFullPorts(string, out string) | Gets the subset of ports, that are selected for full N-Port correction, where N is the number of ports specified in this property. Use comma-separated list of ports to specify multiple ports. The configured measurement is full N-Port corrected if both the measurement receiver and source port are specified using this property. The configured measurement is one-path two-port corrected if one of the measurement ports is specified using this property and another is specified using CorrectionPortSubsetResponsePorts. Measurements involving the ports outside CorrectionPortSubsetFullPorts and CorrectionPortSubsetResponsePorts return error. |
| GetCorrectionPortSubsetResponsePorts(string, out string) | Gets the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also one-path two-port corrected if one of the measurement port is specified using this property and another is specified using CorrectionPortSubsetFullPorts. Measurements involving the ports outside the CorrectionPortSubsetResponsePorts and CorrectionPortSubsetFullPorts return error. |
| GetCorrectionSwitchPortsMultipathCalibration(string, out RFmxVnaMXCorrectionSwitchPortsMultipathCalibration) |  |
| GetCWFrequency(string, out double) | Gets the CW frequency. This value is expressed in Hz. |
| GetDigitalEdgeTriggerEdge(string, out RFmxVnaMXDigitalEdgeTriggerEdge) | Gets the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| GetDigitalEdgeTriggerSource(string, out string) | Gets the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| GetDwellTime(string, out double) | Gets the dwell time. This value is expressed in seconds. |
| GetError(out int, out string) | Gets the latest error code and description. |
| GetErrorString(int, out string) | Converts the status code returned by an RFmxVna function into a string. |
| GetFrequencyList(string, ref double[]) | Gets the list of frequencies at which VNA calibration or measurement (OR just 'VNA measurement') is performed. The frequencies must be in increasing order and must not contain duplicates. This value is expressed in Hz. |
| GetGroundTerminatedPorts(string, out string) | Get the instrument port to be ground terminated in case of SM2 devices. |
| GetIFBandwidth(string, out double) | Gets the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth. |
| GetIndexEventLevel(string, out RFmxVnaMXIndexEventLevel) |  |
| GetIndexEventOutputTerminal(string, out string) | Gets the destination terminal for the Index event. |
| GetIndexEventTerminalName(string, out string) | Gets the fully qualified signal name as a string. |
| GetLimitedConfigurationChange(string, out RFmxVnaMXLimitedConfigurationChange) | Gets the set of properties that are considered by NI-RFmx in the locked signal configuration state. |
| GetMeasurementMemoryNames(string, ref string[]) | returns an array of measurement memory names for the given signal and the measurement number. |
| GetMeasurementMemoryXData(string, ref double[]) | Returns the X Data from the measurement memory specified by the selector string. |
| GetMeasurementMemoryYData(string, ref float[], ref float[]) | Returns the Y Data from the measurement memory specified by the selector string. |
| GetNumberOfPoints(string, out int) | Gets the number of points at which measurements are performed. This method is used only when you set the SweepType method to Linear or CWTime. |
| GetNumberOfSegments(string, out int) | Gets the number of segments. |
| GetPowerLevel(string, out double) | Gets the source power level for the VNA port. This value is expressed in dBm. |
| GetPulseAcquisitionAuto(string, out RFmxVnaMXPulseAcquisitionAuto) | Gets whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. |
| GetPulseAcquisitionDelay(string, out double) | Gets the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True . This value is expressed in seconds. |
| GetPulseAcquisitionWidth(string, out double) | Gets the width of pulse acquisition when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True. This value is expressed in seconds. |
| GetPulseDigitalEdgeTriggerSource(string, out string) | Gets the source of the digital edge pulse trigger. |
| GetPulseGeneratorDelay(string, out double) | Gets the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the PulsePeriod method or derived from an external pulse trigger that you specify using the PulseDigitalEdgeTriggerSource method. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |
| GetPulseGeneratorEnabled(string, out RFmxVnaMXPulseGeneratorEnabled) | Gets whether to enable a pulse generator. |
| GetPulseGeneratorExportOutputTerminal(string, out string) | Gets the destination terminal for an exported pulse generator. |
| GetPulseGeneratorTerminalName(string, out string) | Gets the fully qualified signal name as a string. |
| GetPulseGeneratorWidth(string, out double) | Gets the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |
| GetPulseModeEnabled(string, out RFmxVnaMXPulseModeEnabled) | Gets whether to enable pulse mode for VNA measurement. |
| GetPulseModulatorDelay(string, out double) | Gets the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| GetPulseModulatorWidth(string, out double) | Gets the duration for which the pulse is in ON state when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| GetPulsePeriod(string, out double) | Gets the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| GetPulseTriggerType(string, out RFmxVnaMXPulseTriggerType) | Gets the pulse trigger type. |
| GetReadyForTriggerEventLevel(string, out RFmxVnaMXReadyForTriggerEventLevel) | Gets the trigger level for the Ready For Trigger event. |
| GetReadyForTriggerEventOutputTerminal(string, out string) | Gets the destination terminal for the Ready For Trigger event. |
| GetReadyForTriggerEventTerminalName(string, out string) | Gets the fully qualified signal name as a string. |
| GetResultFetchTimeout(string, out double) | Gets the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. |
| GetSegmentDwellTime(string, out double) | Gets the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. |
| GetSegmentDwellTimeEnabled(string, out RFmxVnaMXSegmentDwellTimeEnabled) | Gets whether to enable individual Dwell Time value configured for each segment by Segment Dwell Time (s) method. If this is set to False, a common value will be used across all segments specified by Dwell Time (s) method. |
| GetSegmentEnabled(string, out RFmxVnaMXSegmentEnabled) | Gets whether to enable the selected segment for the sweep. |
| GetSegmentIFBandwidth(string, out double) | Gets the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. |
| GetSegmentIFBandwidthEnabled(string, out RFmxVnaMXSegmentIFBandwidthEnabled) | Gets whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. |
| GetSegmentNumberOfFrequencyPoints(string, out int) | Gets the number of frequency points of the segment at which the measurement needs to be performed. |
| GetSegmentPowerLevel(string, out double) | Gets the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to True. This value is expressed in dBm. |
| GetSegmentPowerLevelEnabled(string, out RFmxVnaMXSegmentPowerLevelEnabled) | Gets whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. |
| GetSegmentStartFrequency(string, out double) | Gets the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |
| GetSegmentStopFrequency(string, out double) | Gets the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |
| GetSegmentTestReceiverAttenuation(string, out double) | Gets the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to True. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |
| GetSegmentTestReceiverAttenuationEnabled(string, out RFmxVnaMXSegmentTestReceiverAttenuationEnabled) | Gets whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. |
| GetSourcePowerMode(string, out RFmxVnaMXSourcePowerMode) | Gets whether to make VNA measurements with source turned off. |
| GetStartFrequency(string, out double) | Gets the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz. |
| GetStopFrequency(string, out double) | Gets the highest frequency at which the measurement needs to be performed. This value is expressed in Hz. |
| GetSweepDelay(string, out double) | Gets the sweep delay. This value is expressed in seconds. |
| GetSweepSequence(string, out RFmxVnaMXSweepSequence) | Gets the sequence of acquisitions for various frequency points and source ports. |
| GetSweepType(string, out RFmxVnaMXSweepType) | Gets the sweep type for the measurement. |
| GetTestReceiverAttenuation(string, out double) | Gets the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |
| GetTriggerDelay(string, out double) | Gets the trigger delay. This value is expressed in seconds. |
| GetTriggerMode(string, out RFmxVnaMXTriggerMode) | Gets the trigger mode. |
| GetTriggerType(string, out RFmxVnaMXTriggerType) | Gets the trigger type. |
| GetWarning(out int, out string) | Gets the latest warning code and description. |
| GetXAxisValues(string, ref double[]) | Gets the the X-Axis Values (Stimulus) at which VNA calibration or VNA measurement is performed. These values correspond to frequency in Hz for frequency sweeps like List, Linear and Segment sweep. |
| Initiate(string, string) | Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the WaitForMeasurementComplete(string, double) method or CheckMeasurementStatus(string, out bool) method. |
| LoadDataToMeasurementMemoryFromFile(string, string, string, string) | Loads the data from the input file to the measurement memory specified by the Selector String. This method will overwrite the contents of the measurement memory if it already exists. |
| ResetAttribute(string, RFmxVnaMXPropertyId) | Resets the attribute to its default value. |
| ResetToDefault(string) | Resets a signal to the default values. |
| SelectActiveCalset(string, string, RFmxVnaMXRestoreConfiguration) | Selects either the default calset of the specified signal or a named calset accessible across all signals as active calset for the specified signal. |
| SelectMeasurements(string, RFmxVnaMXMeasurementTypes, bool) | Specifies the measurements that you want to enable. |
| SendSoftwareEdgeTrigger() | Sends a trigger to the device when you set TriggerType to Software and the device is waiting for the trigger to be sent. RFmxVNA ignores Software Edge Trigger when performing calibration. |
| SetAcquisitionChunkSize(string, int) |  |
| SetAttributeBool(string, int, bool) | Sets the value of a Bool attribute. |
| SetAttributeComplexDoubleArray(string, int, ComplexDouble[]) | Sets the value of a ComplexDouble array attribute. |
| SetAttributeDouble(string, int, double) | Sets the value of a Double attribute. |
| SetAttributeDoubleArray(string, int, double[]) | Set the value of a double array attribute. |
| SetAttributeInt(string, int, int) | Sets the value of a Int attribute. |
| SetAttributeString(string, int, string) | Sets the value of a String attribute. |
| SetAutoIFBandwidthScalingEnabled(string, RFmxVnaMXAutoIFBandwidthScalingEnabled) | Sets whether IF Bandwidth is scaled down at low frequencies. |
| SetAveragingCount(string, int) | Sets the number of times each measurement is repeated and averaged-over. This method is used only when you set the AveragingEnabled method to True. |
| SetAveragingEnabled(string, RFmxVnaMXAveragingEnabled) | Sets whether to enable averaging for the VNA measurement. |
| SetCorrectionCalibrationCalkitElectronicOrientation(string, string) | Sets the orientation of the vCal fixture ports with respect to vCal ports. |
| SetCorrectionCalibrationCalkitElectronicResourceName(string, string) | Sets the resource name of the electronic calibration module (vCal) used for calibration. |
| SetCorrectionCalibrationCalkitMechanicalName(string, string) | Sets the name of the mechanical calkit used for measurement calibration when you set CorrectionCalibrationCalkitType method to Mechanical. |
| SetCorrectionCalibrationCalkitType(string, RFmxVnaMXCorrectionCalibrationCalkitType) | Sets the type of calkit used for calibration. |
| SetCorrectionCalibrationConnectorType(string, string) | Sets the connector type of the DUT. The specified connector type must match be same as that of the selected calkit. |
| SetCorrectionCalibrationFixtureS11(string, ComplexDouble[]) |  |
| SetCorrectionCalibrationFixtureS12(string, ComplexDouble[]) |  |
| SetCorrectionCalibrationFixtureS21(string, ComplexDouble[]) |  |
| SetCorrectionCalibrationFixtureS22(string, ComplexDouble[]) |  |
| SetCorrectionCalibrationFixtureSParameterOrientation(string, RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation) |  |
| SetCorrectionCalibrationMethod(string, RFmxVnaMXCorrectionCalibrationMethod) | Sets the calibration method. |
| SetCorrectionCalibrationPorts(string, string[]) | Sets the ports requested for calibration. Use comma-separated list of ports to specify multiple ports. |
| SetCorrectionCalibrationStepCount(string, int) |  |
| SetCorrectionCalibrationStepPortAssignment(string, string) |  |
| SetCorrectionCalibrationStepVCalOrientation(string, string) |  |
| SetCorrectionCalibrationThruCoaxDelay(string, double) | Sets the delay of the Thru mechanical standard when CorrectionCalibrationCalkitType method is set to Mechanical and Thru Method method is set to Auto or Undefined Thru. This value is expressed in seconds. |
| SetCorrectionCalibrationThruMethod(string, RFmxVnaMXCorrectionCalibrationThruMethod) | Sets the Thru calibration method when Calibration Method method is set to SOLT. |
| SetCorrectionEnabled(string, RFmxVnaMXCorrectionEnabled) | Sets whether to enable error correction for VNA measurement. |
| SetCorrectionInterpolationEnabled(string, RFmxVnaMXCorrectionInterpolationEnabled) | Sets whether to enable interpolation of error terms for corrected VNA measurement. This method is used only when you set the CorrectionEnabled method to True. |
| SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) | Sets the frequency mode over which the delay and loss (optional) values are determined. |
| SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled) | Sets whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. |
| SetCorrectionPortExtensionAutoRegularizationEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled) | Sets whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled) method to True. |
| SetCorrectionPortExtensionAutoStartFrequency(string, double) | Sets the start frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |
| SetCorrectionPortExtensionAutoStopFrequency(string, double) | Sets the stop frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |
| SetCorrectionPortExtensionDCLossEnabled(string, RFmxVnaMXCorrectionPortExtensionDCLossEnabled) | Sets whether to compensate for the frequency-independent loss when Port Extension Enabled is set to True. |
| SetCorrectionPortExtensionDelay(string, double) | Sets the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds. |
| SetCorrectionPortExtensionDelayDomain(string, RFmxVnaMXCorrectionPortExtensionDelayDomain) | Sets the delay domain of the port extension when the Port Extension Enabled is set to True. |
| SetCorrectionPortExtensionDistance(string, double) | Sets the port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is expressed in unit specified by CorrectionPortExtensionDistanceUnit. |
| SetCorrectionPortExtensionDistanceUnit(string, RFmxVnaMXCorrectionPortExtensionDistanceUnit) | Sets the unit of port extension delay in physical length (distance) when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. |
| SetCorrectionPortExtensionEnabled(string, RFmxVnaMXCorrectionPortExtensionEnabled) | Sets whether to enable port extension for the VNA port. |
| SetCorrectionPortExtensionLoss1(string, double) | Sets the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension. If the DC loss and one additional frequency loss, Loss1 at the frequency f1 is known, the total loss at frequency f can be approximated by: Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^0.5) This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. This value is expressed in dB. |
| SetCorrectionPortExtensionLoss1Enabled(string, RFmxVnaMXCorrectionPortExtensionLoss1Enabled) | Sets whether to compensate for the frequency-dependent loss, Loss1, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True. |
| SetCorrectionPortExtensionLoss1Frequency(string, double) | Sets the frequency at which Loss1 is applied and compensated. This method is used only when the CorrectionPortExtensionEnabled method is set to True and the CorrectionPortExtensionLoss1Enabled method is set to True. This value is expressed in Hz. |
| SetCorrectionPortExtensionLoss2(string, double) | Sets the frequency-dependent loss, Loss2 in dB, to compensate as part of port extension. If in addition to the DC loss and frequency-dependent loss at one frequency (Loss1 at the frequency f1), the loss at a second frequency, Loss2 at frequency f2 is also known, the total loss at frequency f can be approximated by: L (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^b) , where b = log[(abs((Loss1 - DC Loss) / (Loss2 - DC Loss)))] / log(f1 / f2) This method is used only when you set the CorrectionPortExtensionEnabled method to True, the CorrectionPortExtensionLoss1Enabled method is set to True and the CorrectionPortExtensionLoss2Enabled method is set to True. This value is expressed in dB. |
| SetCorrectionPortExtensionLoss2Enabled(string, RFmxVnaMXCorrectionPortExtensionLoss2Enabled) | Sets whether to compensate for the frequency-dependent loss, Loss2, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. |
| SetCorrectionPortExtensionLoss2Frequency(string, double) | Sets the frequency at which Loss2 is applied and compensated. This method is used only when the CorrectionPortExtensionEnabled method is set to True, the CorrectionPortExtensionLoss1Enabled method is set to True and the CorrectionPortExtensionLoss2Enabled method is set to True. This value is expressed in Hz. |
| SetCorrectionPortExtensionLossDCLoss(string, double) | Sets the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB. |
| SetCorrectionPortExtensionVelocityFactor(string, double) | Sets the velocity factor of port extension medium when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is unitless. |
| SetCorrectionPortSubsetEnabled(string, RFmxVnaMXCorrectionPortSubsetEnabled) | Sets whether to enable correction for a subset of ports for which calibration data is avaialble in the calset. This property is used only when you set the CorrectionEnabled property to True. |
| SetCorrectionPortSubsetFullPorts(string, string) | Sets the subset of ports, that are selected for full N-Port correction, where N is the number of ports specified in this property. Use comma-separated list of ports to specify multiple ports. The configured measurement is full N-Port corrected if both the measurement receiver and source port are specified using this property. The configured measurement is one-path two-port corrected if one of the measurement ports is specified using this property and another is specified using CorrectionPortSubsetResponsePorts. Measurements involving the ports outside CorrectionPortSubsetFullPorts and CorrectionPortSubsetResponsePorts return error. |
| SetCorrectionPortSubsetResponsePorts(string, string) | Sets the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also one-path two-port corrected if one of the measurement port is specified using this property and another is specified using CorrectionPortSubsetFullPorts. Measurements involving the ports outside the CorrectionPortSubsetResponsePorts and CorrectionPortSubsetFullPorts return error. |
| SetCorrectionSwitchPortsMultipathCalibration(string, RFmxVnaMXCorrectionSwitchPortsMultipathCalibration) |  |
| SetCWFrequency(string, double) | Sets the CW frequency. This value is expressed in Hz. |
| SetDigitalEdgeTriggerEdge(string, RFmxVnaMXDigitalEdgeTriggerEdge) | Sets the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| SetDigitalEdgeTriggerSource(string, string) | Sets the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| SetDwellTime(string, double) | Sets the dwell time. This value is expressed in seconds. |
| SetFrequencyList(string, double[]) | Sets the list of frequencies at which VNA calibration or measurement (OR just 'VNA measurement') is performed. The frequencies must be in increasing order and must not contain duplicates. This value is expressed in Hz. |
| SetGroundTerminatedPorts(string, string) | Sets the instrument port to be ground terminated in case of SM2 devices. The ports passed to this method are mutually exclusive to the ports passed to Selected Ports attribute. |
| SetIFBandwidth(string, double) | Sets the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth. |
| SetIndexEventLevel(string, RFmxVnaMXIndexEventLevel) |  |
| SetIndexEventOutputTerminal(string, string) | Sets the destination terminal for the Index event. |
| SetLimitedConfigurationChange(string, RFmxVnaMXLimitedConfigurationChange) | Sets the set of properties that are considered by NI-RFmx in the locked signal configuration state. |
| SetNumberOfPoints(string, int) | Sets the number of points at which measurements are performed. This method is used only when you set the SweepType method to Linear or CWTime. |
| SetNumberOfSegments(string, int) | Sets the number of segments. |
| SetPowerLevel(string, double) | Sets the source power level for the VNA port. This value is expressed in dBm. |
| SetPulseAcquisitionAuto(string, RFmxVnaMXPulseAcquisitionAuto) | Sets whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. |
| SetPulseAcquisitionDelay(string, double) | Sets the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True . This value is expressed in seconds. |
| SetPulseAcquisitionWidth(string, double) | Sets the width of pulse acquisition when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True. This value is expressed in seconds. |
| SetPulseDigitalEdgeTriggerSource(string, string) | Sets the source of the digital edge pulse trigger. |
| SetPulseGeneratorDelay(string, double) | Sets the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the PulsePeriod method or derived from an external pulse trigger that you specify using the PulseDigitalEdgeTriggerSource method. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |
| SetPulseGeneratorEnabled(string, RFmxVnaMXPulseGeneratorEnabled) | Sets whether to enable a pulse generator. |
| SetPulseGeneratorExportOutputTerminal(string, string) | Sets the destination terminal for an exported pulse generator. |
| SetPulseGeneratorWidth(string, double) | Sets the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |
| SetPulseModeEnabled(string, RFmxVnaMXPulseModeEnabled) | Sets whether to enable pulse mode for VNA measurement. |
| SetPulseModulatorDelay(string, double) | Sets the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| SetPulseModulatorWidth(string, double) | Sets the duration for which the pulse is in ON state when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| SetPulsePeriod(string, double) | Sets the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| SetPulseTriggerType(string, RFmxVnaMXPulseTriggerType) | Sets the pulse trigger type. |
| SetReadyForTriggerEventLevel(string, RFmxVnaMXReadyForTriggerEventLevel) | Sets the trigger level for the Ready For Trigger event. |
| SetReadyForTriggerEventOutputTerminal(string, string) | Sets the destination terminal for the Ready For Trigger event. |
| SetResultFetchTimeout(string, double) | Sets the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. |
| SetSegmentDwellTime(string, double) | Sets the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. |
| SetSegmentDwellTimeEnabled(string, RFmxVnaMXSegmentDwellTimeEnabled) | Sets whether to enable individual Dwell Time value configured for each segment by Segment Dwell Time (s) method. If this is set to False, a common value will be used across all segments specified by Dwell Time (s) method. |
| SetSegmentEnabled(string, RFmxVnaMXSegmentEnabled) | Sets whether to enable the selected segment for the sweep. |
| SetSegmentIFBandwidth(string, double) | Sets the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. |
| SetSegmentIFBandwidthEnabled(string, RFmxVnaMXSegmentIFBandwidthEnabled) | Sets whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. |
| SetSegmentNumberOfFrequencyPoints(string, int) | Sets the number of frequency points of the segment at which the measurement needs to be performed. |
| SetSegmentPowerLevel(string, double) | Sets the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to True. This value is expressed in dBm. |
| SetSegmentPowerLevelEnabled(string, RFmxVnaMXSegmentPowerLevelEnabled) | Sets whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. |
| SetSegmentStartFrequency(string, double) | Sets the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |
| SetSegmentStopFrequency(string, double) | Sets the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |
| SetSegmentTestReceiverAttenuation(string, double) | Sets the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to True. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |
| SetSegmentTestReceiverAttenuationEnabled(string, RFmxVnaMXSegmentTestReceiverAttenuationEnabled) | Sets whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. |
| SetSourcePowerMode(string, RFmxVnaMXSourcePowerMode) | Sets whether to make VNA measurements with source turned off. |
| SetStartFrequency(string, double) | Sets the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz. |
| SetStopFrequency(string, double) | Sets the highest frequency at which the measurement needs to be performed. This value is expressed in Hz. |
| SetSweepDelay(string, double) | Sets the sweep delay. This value is expressed in seconds. |
| SetSweepSequence(string, RFmxVnaMXSweepSequence) | Sets the sequence of acquisitions for various frequency points and source ports. |
| SetSweepType(string, RFmxVnaMXSweepType) | Sets the sweep type for the measurement. |
| SetTestReceiverAttenuation(string, double) | Sets the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |
| SetTriggerDelay(string, double) | Sets the trigger delay. This value is expressed in seconds. |
| SetTriggerMode(string, RFmxVnaMXTriggerMode) | Sets the trigger mode. |
| SetTriggerType(string, RFmxVnaMXTriggerType) | Sets the trigger type. |
| WaitForMeasurementComplete(string, double) | Waits for the specified number for seconds for all the measurements to complete. |
| BuildCalibrationElementString(string, string) | Creates a selector string specifying the Calibration Element within the Calkit. |
| BuildCalkitString(string, string) | Creates a selector string specifying the Calkit. |
| BuildCalstepString(string, int) | Creates the calibration step string to use as the selector string with the CalibrationAcquire(string, double) method. |
| BuildConnectorString(string, string) | Creates a selector string specifying the Connector within the Calkit. |
| BuildMarkerString(string, int) | Creates selector string for use with marker configuration or fetch methods and methods. |
| BuildMeasurementMemoryString(string, string) | Creates selector string specifying the measurement memory name for use with the get methods. |
| BuildPortString(string, string) | Creates selector string specifying the port(s) for use with configuration or fetch methods and methods. |
| BuildPulseGeneratorString(string, int) | Creates the selector string specifying the Pulse Generator for use with configuration or fetch properties. |
| BuildResultString(string) | Creates selector string for use with configuration or fetch. |
| BuildSegmentString(string, int) | Creates a selector string specifying the segment number for use with configuration or fetch methods and methods. |
| BuildSParameterString(string, int) | Creates the selector string to use with S-Parameter configuration or fetch methods and methods. |
| BuildWaveString(string, int) | Creates the selector string to use with Wave configuration or fetch methods and methods. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxautoifbandwidthscalingenabled.html language=enus -->
## TOPIC 00277: RFmxVnaMXAutoIFBandwidthScalingEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxautoifbandwidthscalingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxautoifbandwidthscalingenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether IF Bandwidth is scaled down at low frequencies. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXAutoIFBandwidthScalingEnabledMembersNameValueDescriptionFalse0Disables IFBW scaling at low frequencies. The IF Bandwidth specified by you using IF Bandwidth method is

### RFmxVnaMXAutoIFBandwidthScalingEnabled Enumeration

Specifies whether IF Bandwidth is scaled down at low frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXAutoIFBandwidthScalingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables IFBW scaling at low frequencies. The IF Bandwidth specified by you using IF Bandwidth method is used for all the frequencies. |
| True | 1 | Enables scaling of IF Bandwidth at low frequencies. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxaveragingenabled.html language=enus -->
## TOPIC 00278: RFmxVnaMXAveragingEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxaveragingenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxaveragingenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the VNA measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXAveragingEnabledMembersNameValueDescriptionFalse0The measurement is performed on a single acquisition. True1Enables measurement averaging. You can set number of times ea

### RFmxVnaMXAveragingEnabled Enumeration

Specifies whether to enable averaging for the VNA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXAveragingEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement is performed on a single acquisition. |
| True | 1 | Enables measurement averaging. You can set number of times each measurement is repeated and averaged-over using the AveragingCount method. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalerrorterm.html language=enus -->
## TOPIC 00279: RFmxVnaMXCalErrorTerm Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalerrorterm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalerrorterm.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the type of error term in the calset. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalErrorTermMembersNameValueDescriptionDirectivity0Directivity measured at Measurement Port (Source Port ignored). SourceMatch1Source Match measured at Measurement Port (Source Port ig

### RFmxVnaMXCalErrorTerm Enumeration

specifies the type of error term in the calset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalErrorTerm

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Directivity | 0 | Directivity measured at Measurement Port (Source Port ignored). |
| SourceMatch | 1 | Source Match measured at Measurement Port (Source Port ignored). |
| ReflectionTracking | 2 | Reflection Tracking measured at Measurement Port (Source Port ignored). |
| TransmissionTracking | 3 | Transmission Tracking measured at Measurement Port with Source Port being the source port. |
| LoadMatch | 4 | Load Match measured at Measurement Port with Source Port being the source port. |
| K | 5 | K measured at Measurement Port (Source Port ignored). |
| alpha | 6 | alpha measured at Measurement Port (Source Port ignored). |
| beta | 7 | beta measured at Measurement Port (Source Port ignored). |
| gamma | 8 | gamma measured at Measurement Port (Source Port ignored). |
| delta | 9 | detla measured at Measurement Port (Source Port ignored). |
| SwitchTerm | 10 | Switch term measured at Measurement Port (Source Port ignored). |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalfrequencygrid.html language=enus -->
## TOPIC 00280: RFmxVnaMXCalFrequencyGrid Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalfrequencygrid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalfrequencygrid.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the type of error term in the calset. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalFrequencyGridMembersNameValueDescriptionDirectivity0Directivity measured at Measurement Port (Source Port ignored). SourceMatch1Source Match measured at Measurement Port (Source Por

### RFmxVnaMXCalFrequencyGrid Enumeration

specifies the type of error term in the calset.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalFrequencyGrid

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Directivity | 0 | Directivity measured at Measurement Port (Source Port ignored). |
| SourceMatch | 1 | Source Match measured at Measurement Port (Source Port ignored). |
| ReflectionTracking | 2 | Reflection Tracking measured at Measurement Port (Source Port ignored). |
| TransmissionTracking | 3 | Transmission Tracking measured at Measurement Port with Source Port being the source port. |
| LoadMatch | 4 | Load Match measured at Measurement Port with Source Port being the source port. |
| K | 5 | K measured at Measurement Port (Source Port ignored). |
| alpha | 6 | alpha measured at Measurement Port (Source Port ignored). |
| beta | 7 | beta measured at Measurement Port (Source Port ignored). |
| gamma | 8 | gamma measured at Measurement Port (Source Port ignored). |
| delta | 9 | delta measured at Measurement Port (Source Port ignored). |
| SwitchTerm | 10 | Switch term measured at Measurement Port (Source Port ignored). |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodelsparameteravailability.html language=enus -->
## TOPIC 00281: RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodelsparameteravailability.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodelsparameteravailability.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the S-Parameter availability. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailabilityMembersNameValueDescriptionEstimate0S-Parameters treated as roughly known. Known1S-Parameters treated as exactly known.

### RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability Enumeration

specifies the S-Parameter availability.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Estimate | 0 | S-Parameters treated as roughly known. |
| Known | 1 | S-Parameters treated as exactly known. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodeltype.html language=enus -->
## TOPIC 00282: RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodeltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodeltype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the model type of of the 1-port reflect standard. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelTypeMembersNameValueDescriptionReflectOpen0Models an Offset Open by specifying the offset parameters and the parameters of

### RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType Enumeration

specifies the model type of of the 1-port reflect standard.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ReflectOpen | 0 | Models an Offset Open by specifying the offset parameters and the parameters of the Open (3rd order polynomial model of the capacitance). |
| ReflectShort | 1 | Models an Offset Short by specifying the offset parameters and the parameters of the short (3rd order polynomial model of the inductance). |
| Load | 2 | Models an Offset Load by specifying the offset parameters. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameteravailability.html language=enus -->
## TOPIC 00283: RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameteravailability.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameteravailability.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the S-Parameter availability. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailabilityMembersNameValueDescriptionEstimate0S-Parameters treated as roughly known. Known1S-Parameters treated as exactly known.

### RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability Enumeration

Specifies the S-Parameter availability.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Estimate | 0 | S-Parameters treated as roughly known. |
| Known | 1 | S-Parameters treated as exactly known. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameterdefinition.html language=enus -->
## TOPIC 00284: RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameterdefinition.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameterdefinition.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the S-Parameter definition of the Calibration Element. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinitionMembersNameValueDescriptionReflectModel0S-Parameters defined by the Reflect model (1-port). Sparameter1S-Param

### RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition Enumeration

specifies the S-Parameter definition of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ReflectModel | 0 | S-Parameters defined by the Reflect model (1-port). |
| Sparameter | 1 | S-Parameters defined by a S-Parameter list (1-port and 2-port). |
| DelayModel | 2 | S-Parameters defined by a delay model (2-port). |
| Unknown | 3 | S-Parameters not further specified. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementtype.html language=enus -->
## TOPIC 00285: RFmxVnaMXCalkitManagerCalkitCalibrationElementType Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementtype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitcalibrationelementtype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the type(s) of the Calibration Element. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalkitManagerCalkitCalibrationElementTypeMembersNameValueDescriptionLoad0Valid for SOL(T/R) calibration types. Open1Valid for SOL(T/R) calibration types. Short2Valid for SOL(T/R) cal

### RFmxVnaMXCalkitManagerCalkitCalibrationElementType Enumeration

specifies the type(s) of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalkitManagerCalkitCalibrationElementType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Load | 0 | Valid for SOL(T/R) calibration types. |
| Open | 1 | Valid for SOL(T/R) calibration types. |
| Short | 2 | Valid for SOL(T/R) calibration types. |
| Thru | 3 | Valid for SOL(T/R) calibration types. |
| Line | 4 | Valid for TRL/LRL calibration types. |
| Reflect | 5 | Valid for TRL/LRL calibration types. |
| Termination | 6 | Use instead of Short/Open/Load, if multiple such elements are present. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitconnectorgender.html language=enus -->
## TOPIC 00286: RFmxVnaMXCalkitManagerCalkitConnectorGender Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitconnectorgender.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkitconnectorgender.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the Gender of a Connector of a specific Calkit. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalkitManagerCalkitConnectorGenderMembersNameValueDescriptionMale0Female1NoGender2

### RFmxVnaMXCalkitManagerCalkitConnectorGender Enumeration

specifies the Gender of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalkitManagerCalkitConnectorGender

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Male | 0 |  |
| Female | 1 |  |
| NoGender | 2 |  |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkittrlreferenceplane.html language=enus -->
## TOPIC 00287: RFmxVnaMXCalkitManagerCalkitTrlReferencePlane Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkittrlreferenceplane.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcalkitmanagercalkittrlreferenceplane.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCalkitManagerCalkitTrlReferencePlaneMembersNameValueDescriptionThru0Use the Thru standard to define the

### RFmxVnaMXCalkitManagerCalkitTrlReferencePlane Enumeration

Specifies the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCalkitManagerCalkitTrlReferencePlane

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Thru | 0 | Use the Thru standard to define the reference plane. |
| Reflect | 1 | Use Reflect, if the Thru standard is uncertainly known and the Reflect standard is well defined. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pfi0.html language=enus -->
## TOPIC 00288: Pfi0

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pfi0.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PFI 0. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string Pfi0

### Pfi0

The signal is exported to the PFI 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string Pfi0

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pfi1.html language=enus -->
## TOPIC 00289: Pfi1

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pfi1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI 1. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string Pfi1

### Pfi1

The signal is exported to the PXI 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string Pfi1

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxiedstarbline.html language=enus -->
## TOPIC 00290: PxieDStarBLine

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxiedstarbline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxiedstarbline.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxieDStarBLine

### PxieDStarBLine

The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxieDStarBLine

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxistarline.html language=enus -->
## TOPIC 00291: PxiStarLine

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxistarline.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxistarline.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI star trigger line. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiStarLine

### PxiStarLine

The signal is exported to the PXI star trigger line.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiStarLine

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline0.html language=enus -->
## TOPIC 00292: PxiTriggerLine0

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline0.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiTriggerLine0

### PxiTriggerLine0

The signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiTriggerLine0

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline1.html language=enus -->
## TOPIC 00293: PxiTriggerLine1

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 1. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiTriggerLine1

### PxiTriggerLine1

The signal is exported to the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiTriggerLine1

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline2.html language=enus -->
## TOPIC 00294: PxiTriggerLine2

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline2.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 2. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiTriggerLine2

### PxiTriggerLine2

The signal is exported to the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiTriggerLine2

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline3.html language=enus -->
## TOPIC 00295: PxiTriggerLine3

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline3.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 3. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiTriggerLine3

### PxiTriggerLine3

The signal is exported to the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiTriggerLine3

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline4.html language=enus -->
## TOPIC 00296: PxiTriggerLine4

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline4.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 4. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiTriggerLine4

### PxiTriggerLine4

The signal is exported to the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiTriggerLine4

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline5.html language=enus -->
## TOPIC 00297: PxiTriggerLine5

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline5.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 5. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiTriggerLine5

### PxiTriggerLine5

The signal is exported to the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiTriggerLine5

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline6.html language=enus -->
## TOPIC 00298: PxiTriggerLine6

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline6.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 6. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiTriggerLine6

### PxiTriggerLine6

The signal is exported to the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiTriggerLine6

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline7.html language=enus -->
## TOPIC 00299: PxiTriggerLine7

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants-pxitriggerline7.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The signal is exported to the PXI trigger line 7. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic const string PxiTriggerLine7

### PxiTriggerLine7

The signal is exported to the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public const string PxiTriggerLine7

Parent topic:

RFmxVnaMXConstants Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxconstants.html language=enus -->
## TOPIC 00300: RFmxVnaMXConstants Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxconstants.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxconstants.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies constants for I/O terminals. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMXConstantsFieldsNameDescriptionPfi0The signal is exported to the PFI 0. Pfi1The signal is exported to the PXI 1. PxieDStarBLineThe signal is exported to the PXIe DStar B trigger

### RFmxVnaMXConstants Class

Specifies constants for I/O terminals.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMXConstants

#### Fields

| Name | Description |
| --- | --- |
| Pfi0 | The signal is exported to the PFI 0. |
| Pfi1 | The signal is exported to the PXI 1. |
| PxieDStarBLine | The signal is exported to the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5840/5841. |
| PxiStarLine | The signal is exported to the PXI star trigger line. |
| PxiTriggerLine0 | The signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | The signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | The signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | The signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | The signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | The signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | The signal is exported to the PXI trigger line 6. |
| PxiTriggerLine7 | The signal is exported to the PXI trigger line 7. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html language=enus -->
## TOPIC 00301: RFmxVnaMXCorrectionCalibrationCalkitType Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of calkit used for calibration. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionCalibrationCalkitTypeMembersNameValueDescriptionElectronic0Use electronic calkit module for calibration. Supported device: NI-5501. Mechanical1Use mechanical calkit standa

### RFmxVnaMXCorrectionCalibrationCalkitType Enumeration

Specifies the type of calkit used for calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionCalibrationCalkitType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Electronic | 0 | Use electronic calkit module for calibration. Supported device: NI-5501. |
| Mechanical | 1 | Use mechanical calkit standards for calibration. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationfixturesparameterorientation.html language=enus -->
## TOPIC 00302: RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationfixturesparameterorientation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationfixturesparameterorientation.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientationMembersNameValueDescriptionPort1TowardsvCal0Port2TowardsvCal1

### RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation Enumeration

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Port1TowardsvCal | 0 |  |
| Port2TowardsvCal | 1 |  |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationmethod.html language=enus -->
## TOPIC 00303: RFmxVnaMXCorrectionCalibrationMethod Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationmethod.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the calibration method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionCalibrationMethodMembersNameValueDescriptionSol0Full 1-port calibration using atleast three distinct reflection standards, typically named Short, Open and Load. Solt1Full 2-port calibratio

### RFmxVnaMXCorrectionCalibrationMethod Enumeration

Specifies the calibration method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionCalibrationMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Sol | 0 | Full 1-port calibration using atleast three distinct reflection standards, typically named Short, Open and Load. |
| Solt | 1 | Full 2-port calibration by performing two SOL calibrations on the two ports using atleast three distinct reflection standards, and a Thru cal using a transmission standard connecting the two ports. |
| Trl | 2 | Full 2-port calibration using a Thru, at least one Line, and one Reflect standard (Thru-Reflect-Line). The Thru standard can be an flush Thru or can have non-zero length (LRL, Line-Reflect-Line). The Reflect standard has to be identical for both ports. If multiple lines with different lengths are defined, the measurement automatically splits the measurement frequency range into segments and picks the line standard with appropriate length for each segment. The reference impedance of the calibration is the characteristic impedance of the Line(s). |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationthrumethod.html language=enus -->
## TOPIC 00304: RFmxVnaMXCorrectionCalibrationThruMethod Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationthrumethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationthrumethod.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Thru calibration method when Calibration Method method is set to SOLT. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionCalibrationThruMethodMembersNameValueDescriptionAuto0Measurement selects the appropriate Thru calibration method based on the value of Co

### RFmxVnaMXCorrectionCalibrationThruMethod Enumeration

Specifies the Thru calibration method when Calibration Method method is set to *SOLT*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionCalibrationThruMethod

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | 0 | Measurement selects the appropriate Thru calibration method based on the value of CorrectionCalibrationCalkitType method specified by you. If CorrectionCalibrationCalkitType is Electronic, then Delay Thru Using Defined Thru is selected. If CorrectionCalibrationCalkitType is Mechanical, then Undefined Thru is selected. |
| DefinedThru | 1 | The Thru definition from calkit definition is used based on the value of CorrectionCalibrationCalkitType method specified by you. If CorrectionCalibrationCalkitType is Electronic, the Thru definition from the electronic calkit EPROM is used. If CorrectionCalibrationCalkitType is Mechanical, the Thru definition from the calkit definition file is used. |
| FlushThru | 2 | Indicates a direct connection of the test ports when CorrectionCalibrationCalkitType is Mechanical. The measured Thru is treated as flush Thru ignoring the Thru definition from the Calkit file. This method is not supported when CorrectionCalibrationCalkitType is Electronic. |
| UndefinedThru | 3 | Indicates connection of a Thru without a stored definition when CorrectionCalibrationCalkitType is Mechanical. The measured Thru is treated as unknown Thru ignoring the Thru definition from the Calkit file. If a delay is configured, the delay will be utilized for the calibration. This method is not supported when CorrectionCalibrationCalkitType is Electronic. |
| vCalThruAsUnknownThru | 5 | The Thru from the electronical Calkit is used for Thru measurement during calibration. The Thru definirion from vCal EPROM is used as a phase reference for the Thru characterization during calibration. This method is not supported when Calkit Type is Mechanical. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionenabled.html language=enus -->
## TOPIC 00305: RFmxVnaMXCorrectionEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable error correction for VNA measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionEnabledMembersNameValueDescriptionFalse0The measurement disables error corection. True1The measurement enables error correction.

### RFmxVnaMXCorrectionEnabled Enumeration

Specifies whether to enable error correction for VNA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement disables error corection. |
| True | 1 | The measurement enables error correction. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioninterpolationenabled.html language=enus -->
## TOPIC 00306: RFmxVnaMXCorrectionInterpolationEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioninterpolationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioninterpolationenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable interpolation of error terms for corrected VNA measurement. This method is used only when you set the CorrectionEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionInterpolationEnabledMembersNameValueDescriptionFalse0The m

### RFmxVnaMXCorrectionInterpolationEnabled Enumeration

Specifies whether to enable interpolation of error terms for corrected VNA measurement. This method is used only when you set the [CorrectionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionInterpolationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement disables interpolation of error terms for error correction. |
| True | 1 | The measurement enables interpolation of error terms for error correction. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautofrequencymode.html language=enus -->
## TOPIC 00307: RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautofrequencymode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautofrequencymode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency mode over which the delay and loss (optional) values are determined. The default is Sweep. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionPortExtensionAutoFrequencyModeMembersNameValueDescriptionSweep0Sets the frequency mode to Sweep. Configured

### RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode Enumeration

Specifies the frequency mode over which the delay and loss (optional) values are determined. The default is Sweep.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Sweep | 0 | Sets the frequency mode to Sweep. Configured sweep range is used to determine the phase and loss values. |
| User | 1 | Sets the frequency mode to User Span. User-defined span is used to determine the phase and loss values. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautolossenabled.html language=enus -->
## TOPIC 00308: RFmxVnaMXCorrectionPortExtensionAutoLossEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautolossenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautolossenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. Synt

### RFmxVnaMXCorrectionPortExtensionAutoLossEnabled Enumeration

Specifies whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionAutoLossEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disable the loss estimation in automatic port extension. |
| True | 1 | Enable the loss estimation in automatic port extension. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautoregularizationenabled.html language=enus -->
## TOPIC 00309: RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautoregularizationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautoregularizationenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the

### RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled Enumeration

Specifies whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the [SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautolossenabled__string-rfmxvnamxcorrectionportextensionautolossenabled.html) method to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disable the regularization of the compensated trace in automatic port extension. |
| True | 1 | Enable the regularization of the compensated trace in automatic port extension. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautostandard.html language=enus -->
## TOPIC 00310: RFmxVnaMXCorrectionPortExtensionAutoStandard Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautostandard.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautostandard.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measured standard as part of automatic port extension. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionPortExtensionAutoStandardMembersNameValueDescriptionOpen0Open standard is measured. Short1Short standard is measured.

### RFmxVnaMXCorrectionPortExtensionAutoStandard Enumeration

Specifies the measured standard as part of automatic port extension.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionAutoStandard

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Open | 0 | Open standard is measured. |
| Short | 1 | Short standard is measured. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondclossenabled.html language=enus -->
## TOPIC 00311: RFmxVnaMXCorrectionPortExtensionDCLossEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondclossenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondclossenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compensate for the frequency independent loss when Port Extension Enabled is set to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionPortExtensionDCLossEnabledMembersNameValueDescriptionFalse0The measurement disables the compensation of DC Loss

### RFmxVnaMXCorrectionPortExtensionDCLossEnabled Enumeration

Specifies whether to compensate for the frequency independent loss when Port Extension Enabled is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionDCLossEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement disables the compensation of DC Loss of the port extension. |
| True | 1 | The measurement compensates for the DC loss based on the value of Port Extension DC Loss (dB) specified by you. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondelaydomain.html language=enus -->
## TOPIC 00312: RFmxVnaMXCorrectionPortExtensionDelayDomain Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondelaydomain.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondelaydomain.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delay domain of the port extension when Port Extension Enabled is set to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionPortExtensionDelayDomainMembersNameValueDescriptionDelay0The delay domain of the port extension for the VNA port is set to electr

### RFmxVnaMXCorrectionPortExtensionDelayDomain Enumeration

Specifies the delay domain of the port extension when Port Extension Enabled is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionDelayDomain

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Delay | 0 | The delay domain of the port extension for the VNA port is set to electrical delay. |
| Distance | 1 | The delay domain of the port extension for the VNA port is set to distance. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html language=enus -->
## TOPIC 00313: RFmxVnaMXCorrectionPortExtensionEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable port extension for the VNA port. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionPortExtensionEnabledMembersNameValueDescriptionFalse0The measurement disables port extension for the VNA port. True1The measurement enables port extension for th

### RFmxVnaMXCorrectionPortExtensionEnabled Enumeration

Specifies whether to enable port extension for the VNA port.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement disables port extension for the VNA port. |
| True | 1 | The measurement enables port extension for the VNA port. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html language=enus -->
## TOPIC 00314: RFmxVnaMXCorrectionPortExtensionLoss1Enabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compensate for the frequency dependent loss, Loss1, as part of port extention. This method is used only when you set the CorrectionPortExtensionEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionPortExtensionLoss1EnabledMembersN

### RFmxVnaMXCorrectionPortExtensionLoss1Enabled Enumeration

Specifies whether to compensate for the frequency dependent loss, Loss1, as part of port extention. This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionLoss1Enabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement disables the compensation of Loss1 of the port extension. |
| True | 1 | The measurement compensates for the Loss1 based on the configured value of Port Extension Loss1 (dB). |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss2enabled.html language=enus -->
## TOPIC 00315: RFmxVnaMXCorrectionPortExtensionLoss2Enabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss2enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss2enabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compensate for the frequency dependent loss, Loss2, as part of port extention. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. SyntaxNamespace: NationalInstruments.RFmx.Vna

### RFmxVnaMXCorrectionPortExtensionLoss2Enabled Enumeration

Specifies whether to compensate for the frequency dependent loss, Loss2, as part of port extention. This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to True and the [CorrectionPortExtensionLoss1Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortExtensionLoss2Enabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement disables the compensation of Loss2 of the port extension. |
| True | 1 | The measurement compensates for the Loss2 based on the configured value of Port Extension Loss2 (dB). |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportsubsetenabled.html language=enus -->
## TOPIC 00316: RFmxVnaMXCorrectionPortSubsetEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportsubsetenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportsubsetenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable correction for a subset of set of ports for which calibration data is avaialble. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionPortSubsetEnabledMembersNameValueDescriptionFalse0The measurement disables port-subsetting for error correction.

### RFmxVnaMXCorrectionPortSubsetEnabled Enumeration

Specifies whether to enable correction for a subset of set of ports for which calibration data is avaialble.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionPortSubsetEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The measurement disables port-subsetting for error correction. |
| True | 1 | The measurement enabes port-subsetting for error correction. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionswitchportsmultipathcalibration.html language=enus -->
## TOPIC 00317: RFmxVnaMXCorrectionSwitchPortsMultipathCalibration Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionswitchportsmultipathcalibration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionswitchportsmultipathcalibration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXCorrectionSwitchPortsMultipathCalibrationMembersNameValueDescriptionAuto0Disabled1Enabled2

### RFmxVnaMXCorrectionSwitchPortsMultipathCalibration Enumeration

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXCorrectionSwitchPortsMultipathCalibration

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | 0 |  |
| Disabled | 1 |  |
| Enabled | 2 |  |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxdigitaledgetriggeredge.html language=enus -->
## TOPIC 00318: RFmxVnaMXDigitalEdgeTriggerEdge Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxdigitaledgetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxdigitaledgetriggeredge.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXDigitalEdgeTriggerEdgeMembersNameValueDescriptionRising0The trigger asserts on the rising edge of the signal. Fa

### RFmxVnaMXDigitalEdgeTriggerEdge Enumeration

Specifies the active edge for the trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [DigitalEdge](nationalinstruments-rfmx-vnamx-rfmxvnamxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXDigitalEdgeTriggerEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 0 | The trigger asserts on the rising edge of the signal. |
| Falling | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxlimitedconfigurationchange.html language=enus -->
## TOPIC 00319: RFmxVnaMXLimitedConfigurationChange Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxlimitedconfigurationchange.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxlimitedconfigurationchange.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of properties that are considered by NI-RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXLimitedConfigurationChangeMembersNameValueDescriptionDisabled0This is the normal mode of RFmx operation. All configuration chan

### RFmxVnaMXLimitedConfigurationChange Enumeration

Specifies the set of properties that are considered by NI-RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXLimitedConfigurationChange

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| NoChange | 1 | Signal configuration and RFmxInstr configuration are locked after the first Commit or Initiate of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarker-configuration.html language=enus -->
## TOPIC 00320: Configuration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarker-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarker-configuration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxVnaMXMarkerConfiguration instance that provides methods to configure the Marker measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic RFmxVnaMXMarkerConfiguration Configuration { get; }

### Configuration

Gets the [RFmxVnaMXMarkerConfiguration](nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration.html) instance that provides methods to configure the Marker measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public [RFmxVnaMXMarkerConfiguration](nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration.html) Configuration { get; }

Parent topic:

RFmxVnaMXMarker Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarker-results.html language=enus -->
## TOPIC 00321: Results

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarker-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarker-results.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxVnaMXMarkerResults instance that provides methods to fetch and read the Marker measurement results. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic RFmxVnaMXMarkerResults Results { get; }

### Results

Gets the [RFmxVnaMXMarkerResults](nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults.html) instance that provides methods to fetch and read the Marker measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public [RFmxVnaMXMarkerResults](nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults.html) Results { get; }

Parent topic:

RFmxVnaMXMarker Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarker.html language=enus -->
## TOPIC 00322: RFmxVnaMXMarker Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarker.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarker.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Marker measurement. Derives fromRFmxVnaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMXMarker : RFmxVnaMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxVnaMXMarkerConfiguration instance that provides methods to configure the Marker measurem

### RFmxVnaMXMarker Class

Represents the Marker measurement.

#### Derives from

- RFmxVnaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMXMarker : RFmxVnaMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxVnaMXMarkerConfiguration instance that provides methods to configure the Marker measurement. |
| Results | Gets the RFmxVnaMXMarkerResults instance that provides methods to fetch and read the Marker measurement results. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuredatasource__string-string.html language=enus -->
## TOPIC 00323: ConfigureDataSource(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuredatasource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuredatasource__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the data source on which marker operations are performed. Use "marker(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ConfigureDataSource(string selectorString, string dataSource)ParametersNameTypeDescriptionselectorStringstrin

### ConfigureDataSource(string, string)

Configures the data source on which marker operations are performed. 
Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureDataSource(string selectorString, string dataSource)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example: "marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| dataSource | string | Specifies the measurement or memory data on which markers are placed. If you want to place markers on SParams measurement data, then specify this parameter as sparam<n>". If you want to place markers on <em>SParams</em> measurement memory data, then specify this parameter as "sparam<n>/measmem::<measMemoryName>". Similarly, if you want to place markers on data from <em>Wave</em> measurement data, then specify this parameter as wave<<i>n</i>>". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuremode__string-rfmxvnamxmarkermode.html language=enus -->
## TOPIC 00324: ConfigureMode(string, RFmxVnaMXMarkerMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuremode__string-rfmxvnamxmarkermode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuremode__string-rfmxvnamxmarkermode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker mode. Use "marker(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ConfigureMode(string selectorString, RFmxVnaMXMarkerMode markerMode)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string compr

### ConfigureMode(string, RFmxVnaMXMarkerMode)

Configures the marker mode. 
Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureMode(string selectorString, RFmxVnaMXMarkerMode markerMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example:"marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| markerMode | RFmxVnaMXMarkerMode | Specifies the mode for placing the marker. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurenumberofmarkers__string-int.html language=enus -->
## TOPIC 00325: ConfigureNumberOfMarkers(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurenumberofmarkers__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurenumberofmarkers__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of markers.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ConfigureNumberOfMarkers(string selectorString, int numberOfMarkers)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration

### ConfigureNumberOfMarkers(string, int)

Configures the number of markers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureNumberOfMarkers(string selectorString, int numberOfMarkers)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| numberOfMarkers | int | Specifies the number of markers. If you increase number of markers from N to N+K, then existing N markers are not affected but K new markers are added. If you reduce number of markers from N to N-K, then last K markers are deleted without affecting the remaining N-K markers. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurepeaksearchexcursion__string-rfmxvnamxmarkerpeaksearchexcursionenabled-double.html language=enus -->
## TOPIC 00326: ConfigurePeakSearchExcursion(string, RFmxVnaMXMarkerPeakSearchExcursionEnabled, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurepeaksearchexcursion__string-rfmxvnamxmarkerpeaksearchexcursionenabled-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurepeaksearchexcursion__string-rfmxvnamxmarkerpeaksearchexcursionenabled-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search method finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value. Use "marker(n)" as the selector string to configure this method.SyntaxNam

### ConfigurePeakSearchExcursion(string, RFmxVnaMXMarkerPeakSearchExcursionEnabled, double)

Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search method finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value. 
 Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigurePeakSearchExcursion(string selectorString, RFmxVnaMXMarkerPeakSearchExcursionEnabled peakExcursionEnabled, double peakExcursion)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example: "marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| peakExcursionEnabled | RFmxVnaMXMarkerPeakSearchExcursionEnabled | Specifies whether Marker Search method finds a peak such that the data value rises and falls around the peak by atleast the specified peak excursion value or finds a peak without considering any peak excursion constraint. |
| peakExcursion | double | Specifies the peak excursion value that Marker Search method uses to find a peak such that the data value rises and falls around the peak by atleast the specified peak excursion value. The threshold is expressed in the same units as the source data. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurepeaksearchthreshold__string-rfmxvnamxmarkerpeaksearchthresholdenabled-double.html language=enus -->
## TOPIC 00327: ConfigurePeakSearchThreshold(string, RFmxVnaMXMarkerPeakSearchThresholdEnabled, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurepeaksearchthreshold__string-rfmxvnamxmarkerpeaksearchthresholdenabled-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurepeaksearchthreshold__string-rfmxvnamxmarkerpeaksearchthresholdenabled-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search method in peak search mode finds the peaks that exceed this value and discards all other peaks. Use "marker(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic

### ConfigurePeakSearchThreshold(string, RFmxVnaMXMarkerPeakSearchThresholdEnabled, double)

Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search method in peak search mode finds the peaks that exceed this value and discards all other peaks. 
 Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigurePeakSearchThreshold(string selectorString, RFmxVnaMXMarkerPeakSearchThresholdEnabled thresholdEnabled, double threshold)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example: "marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| thresholdEnabled | RFmxVnaMXMarkerPeakSearchThresholdEnabled | Specifies whether Marker Search method finds a peak above specified Threshold or finds a peak without considering any Threshold constraint. |
| threshold | double | Specifies the threshold value that a valid peak must exceed when you use Marker Search method to find peaks. The threshold is expressed in the same units as the source data. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurereferencemarker__string-int.html language=enus -->
## TOPIC 00328: ConfigureReferenceMarker(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurereferencemarker__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurereferencemarker__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an associated reference marker for a delta marker. Markers with Marker Type method set to Delta must be associated with a reference marker. You cannot associate a reference marker for other markers whose Marker Type is not Delta. Use "marker(n)" as the selector string to configure this me

### ConfigureReferenceMarker(string, int)

Configures an associated reference marker for a delta marker. Markers with Marker Type method set to Delta must be associated with a reference marker. You cannot associate a reference marker for other markers whose Marker Type is not Delta. 
 Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureReferenceMarker(string selectorString, int referenceMarker)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example: "marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| referenceMarker | int | Specifies the marker index to be used as reference for the specified delta marker. All types of markers including normal, delta and fixed can be used as a reference marker. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuretargetvalue__string-double.html language=enus -->
## TOPIC 00329: ConfigureTargetValue(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuretargetvalue__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuretargetvalue__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the target value for the specified marker when performing Target search using Marker Search method. Use "marker(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ConfigureTargetValue(string selectorString, double targetValue)Para

### ConfigureTargetValue(string, double)

Configures the target value for the specified marker when performing Target search using Marker Search method. 
 Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureTargetValue(string selectorString, double targetValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example:"marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| targetValue | double | Configures the target value for the specified marker when performing Target search using Marker Search VI |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuretype__string-rfmxvnamxmarkertype.html language=enus -->
## TOPIC 00330: ConfigureType(string, RFmxVnaMXMarkerType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuretype__string-rfmxvnamxmarkertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configuretype__string-rfmxvnamxmarkertype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker type. Use "marker(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ConfigureType(string selectorString, RFmxVnaMXMarkerType markerType)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string compr

### ConfigureType(string, RFmxVnaMXMarkerType)

Configures the marker type. 
Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureType(string selectorString, RFmxVnaMXMarkerType markerType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example: "marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| markerType | RFmxVnaMXMarkerType | Specifies whether the marker is disabled (Off) or is enabled (On) as a normal marker, delta marker or a fixed marker. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurex__string-double.html language=enus -->
## TOPIC 00331: ConfigureX(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurex__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurex__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the X value of the marker. You must configure the X value of reference marker or perform any marker search operation on the reference marker before configuring the X value for the delta marker. Use "marker(n)" as the selector string to configure this method.SyntaxNamespace: NationalInstru

### ConfigureX(string, double)

Configures the X value of the marker. You must configure the X value of reference marker or perform any marker search operation on the reference marker before configuring the X value for the *delta* marker. 
 Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureX(string selectorString, double markerX)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example: "marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| markerX | double | Specifies the X value of the marker on the trace when you set the Marker Type to normal or fixed. The X value of the delta marker is relative to the X value of the reference marker when you set the Marker Type to delta. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurey__string-double-double.html language=enus -->
## TOPIC 00332: ConfigureY(string, double, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurey__string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration-configurey__string-double-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Y value of the marker. You can configure the Y location of fixed markers only. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y

### ConfigureY(string, double, double)

Configures the Y value of the marker. You can configure the Y location of *fixed* markers only. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number. 
 If Y value is a complex number, use Marker Y1 and Marker Y2 to set its real and imaginary components respectively. If Y value is a real number, use Marker Y1 to set the Y location and set Marker Y2 to 0. 
 When you want to use a *fixed* marker as a reference marker for a Delta marker, then you must configure the Y value of the *fixed* reference marker by calling this method or by performing any marker search operation on the reference marker before configuring the X value of the *delta* marker. 
 Use "marker(n)" as the selector string to configure this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureY(string selectorString, double markerY1, double markerY2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of marker number. Example: "marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| markerY1 | double | Specifies the Y1 component of the marker's Y value. |
| markerY2 | double | Specifies the Y2 component of the marker's Y value.. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration.html language=enus -->
## TOPIC 00333: RFmxVnaMXMarkerConfiguration Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerconfiguration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the Marker measurement. Derives fromRFmxVnaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMXMarkerConfiguration : RFmxVnaMXSubObjectMethodsNameDescriptionConfigureDataSource(string, string)Configures the data source on which marker operati

### RFmxVnaMXMarkerConfiguration Class

Provides methods to configure the Marker measurement.

#### Derives from

- RFmxVnaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMXMarkerConfiguration : RFmxVnaMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureDataSource(string, string) | Configures the data source on which marker operations are performed.Use "marker(n)" as the selector string to configure this method. |
| ConfigureMode(string, RFmxVnaMXMarkerMode) | Configures the marker mode.Use "marker(n)" as the selector string to configure this method. |
| ConfigureNumberOfMarkers(string, int) | Configures the number of markers. |
| ConfigurePeakSearchExcursion(string, RFmxVnaMXMarkerPeakSearchExcursionEnabled, double) | Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search method finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value. Use "marker(n)" as the selector string to configure this method. |
| ConfigurePeakSearchThreshold(string, RFmxVnaMXMarkerPeakSearchThresholdEnabled, double) | Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search method in peak search mode finds the peaks that exceed this value and discards all other peaks. Use "marker(n)" as the selector string to configure this method. |
| ConfigureReferenceMarker(string, int) | Configures an associated reference marker for a delta marker. Markers with Marker Type method set to Delta must be associated with a reference marker. You cannot associate a reference marker for other markers whose Marker Type is not Delta. Use "marker(n)" as the selector string to configure this method. |
| ConfigureTargetValue(string, double) | Configures the target value for the specified marker when performing Target search using Marker Search method. Use "marker(n)" as the selector string to configure this method. |
| ConfigureType(string, RFmxVnaMXMarkerType) | Configures the marker type.Use "marker(n)" as the selector string to configure this method. |
| ConfigureX(string, double) | Configures the X value of the marker. You must configure the X value of reference marker or perform any marker search operation on the reference marker before configuring the X value for the delta marker. Use "marker(n)" as the selector string to configure this method. |
| ConfigureY(string, double, double) | Configures the Y value of the marker. You can configure the Y location of fixed markers only. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number. If Y value is a complex number, use Marker Y1 and Marker Y2 to set its real and imaginary components respectively. If Y value is a real number, use Marker Y1 to set the Y location and set Marker Y2 to 0. When you want to use a fixed marker as a reference marker for a Delta marker, then you must configure the Y value of the fixed reference marker by calling this method or by performing any marker search operation on the reference marker before configuring the X value of the delta marker. Use "marker(n)" as the selector string to configure this method. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkermode.html language=enus -->
## TOPIC 00334: RFmxVnaMXMarkerMode Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkermode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkermode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the mode for placing the marker. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXMarkerModeMembersNameValueDescriptionContinuous0Marker can be placed at any point and its response value is obtained by interpolation of actual measured data points. Discrete1Marker can be

### RFmxVnaMXMarkerMode Enumeration

specifies the mode for placing the marker.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXMarkerMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Continuous | 0 | Marker can be placed at any point and its response value is obtained by interpolation of actual measured data points. |
| Discrete | 1 | Marker can be placed only at actual measured data points. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerpeaksearchexcursionenabled.html language=enus -->
## TOPIC 00335: RFmxVnaMXMarkerPeakSearchExcursionEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerpeaksearchexcursionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerpeaksearchexcursionenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies the threshold value that a valid peak must exceed when you use Marker Search method to find peaks. The threshold is expressed in the same units as the source data. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXMarkerPeakSearchExcursionEnabledMembersNameValueDescriptio

### RFmxVnaMXMarkerPeakSearchExcursionEnabled Enumeration

specifies the threshold value that a valid peak must exceed when you use Marker Search method to find peaks. The threshold is expressed in the same units as the source data.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXMarkerPeakSearchExcursionEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the peak excursion. |
| True | 1 | Enables the peak excursion. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerpeaksearchthresholdenabled.html language=enus -->
## TOPIC 00336: RFmxVnaMXMarkerPeakSearchThresholdEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerpeaksearchthresholdenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerpeaksearchthresholdenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies whether Marker Search method finds a peak above specified Threshold or finds a peak without considering any Threshold constraint. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXMarkerPeakSearchThresholdEnabledMembersNameValueDescriptionFalse0Disables peak-thresholding.

### RFmxVnaMXMarkerPeakSearchThresholdEnabled Enumeration

specifies whether Marker Search method finds a peak above specified Threshold or finds a peak without considering any Threshold constraint.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXMarkerPeakSearchThresholdEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables peak-thresholding. |
| True | 1 | Enables peak-thresholding. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchgraphicaly__string-double-out-out.html language=enus -->
## TOPIC 00337: FetchGraphicalY(string, double, out double, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchgraphicaly__string-double-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchgraphicaly__string-double-out-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int FetchGraphicalY(string selectorString, double timeout, out double markerY1, out double markerY2)

### FetchGraphicalY(string, double, out double, out double)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchGraphicalY(string selectorString, double timeout, out double markerY1, out double markerY2)

Parent topic:

RFmxVnaMXMarkerResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchx__string-out.html language=enus -->
## TOPIC 00338: FetchX(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchx__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchx__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the X value of the marker. X value of the delta marker is relative to its reference marker.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int FetchX(string selectorString, out double markerX)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the

### FetchX(string, out double)

Returns the X value of the marker. X value of the *delta* marker is relative to its reference marker.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchX(string selectorString, out double markerX)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name and marker number. Example: "marker0" "result::r1/marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| markerX | out double | Upon return, contains the marker X value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchy__string-out-out.html language=enus -->
## TOPIC 00339: FetchY(string, out double, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchy__string-out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-fetchy__string-out-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Y value of the marker. Y value of the delta marker is relative to its reference marker. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other form

### FetchY(string, out double, out double)

Returns the Y value of the marker. Y value of the *delta* marker is relative to its reference marker. 
Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number. 
If Y value is a complex number, Marker Y1 and Marker Y2 return its real and imaginary components respectively. If Y value is a real number, Marker Y1 returns the Y location and Marker Y2 returns 0.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchY(string selectorString, out double markerY1, out double markerY2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name and marker number. Example: "marker0" "result::r1/marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| markerY1 | out double | Upon return, contains the marker Y1 value. |
| markerY2 | out double | Upon return, contains the marker Y2 value. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-markersearch__string-rfmxvnamxmarkersearchmode.html language=enus -->
## TOPIC 00340: MarkerSearch(string, RFmxVnaMXMarkerSearchMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-markersearch__string-rfmxvnamxmarkersearchmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults-markersearch__string-rfmxvnamxmarkersearchmode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the marker search operation that you specify using Search Mode. Marker search operation is performed on real-valued data only. No search operation is performed on complex-valued data. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int MarkerSearch(string selectorString, RFmxVnaMXMark

### MarkerSearch(string, RFmxVnaMXMarkerSearchMode)

Performs the marker search operation that you specify using Search Mode. 
 Marker search operation is performed on real-valued data only. No search operation is performed on complex-valued data.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int MarkerSearch(string selectorString, RFmxVnaMXMarkerSearchMode searchMode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name and marker number. Example: "marker0" "result::r1/marker0" You can use the BuildMarkerString(string, int) method to build the selector string. |
| searchMode | RFmxVnaMXMarkerSearchMode | Specifies the search-target. If search is successful, RFmx updates the marker X and Y values to the location at which search-target is found. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXMarkerResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults.html language=enus -->
## TOPIC 00341: RFmxVnaMXMarkerResults Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkerresults.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the Marker measurement results. Derives fromRFmxVnaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMXMarkerResults : RFmxVnaMXSubObjectMethodsNameDescriptionFetchGraphicalY(string, double, out double, out double)FetchX(string, out doub

### RFmxVnaMXMarkerResults Class

Provides methods to fetch and read the Marker measurement results.

#### Derives from

- RFmxVnaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMXMarkerResults : RFmxVnaMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchGraphicalY(string, double, out double, out double) |  |
| FetchX(string, out double) | Returns the X value of the marker. X value of the delta marker is relative to its reference marker. |
| FetchY(string, out double, out double) | Returns the Y value of the marker. Y value of the delta marker is relative to its reference marker.Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number.If Y value is a complex number, Marker Y1 and Marker Y2 return its real and imaginary components respectively. If Y value is a real number, Marker Y1 returns the Y location and Marker Y2 returns 0. |
| MarkerSearch(string, RFmxVnaMXMarkerSearchMode) | Performs the marker search operation that you specify using Search Mode. Marker search operation is performed on real-valued data only. No search operation is performed on complex-valued data. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkersearchmode.html language=enus -->
## TOPIC 00342: RFmxVnaMXMarkerSearchMode Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkersearchmode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkersearchmode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the search-target. If search is successful, RFmx updates the marker X and Y values to the location at which search-target is found. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXMarkerSearchModeMembersNameValueDescriptionNone0No search operation is performed. Max1Move

### RFmxVnaMXMarkerSearchMode Enumeration

Specifies the search-target. If search is successful, RFmx updates the marker X and Y values to the location at which search-target is found.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXMarkerSearchMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No search operation is performed. |
| Max | 1 | Moves the marker to the highest measured value on the configured data source. |
| Min | 2 | Moves the marker to the lowest measured value on the configured data source. |
| Peak | 3 | Moves the marker to the highest peak that satisfies peak threshold and peak excursion criteria. |
| NextPeak | 4 | Moves the marker to the next peak that satisfies peak threshold and peak excursion criteria. |
| NextLeftPeak | 5 | Moves the marker to the next left peak that satisfies peak threshold and peak excursion criteria. |
| NextRightPeak | 6 | Moves the marker to the next right peak that satisfies peak threshold and peak excursion criteria. |
| Target | 7 | Moves the marker to the first right target encountered from the current marker position, wraps around if no target found. If marker mode is Discrete, marker moves to the data point closest to the first right target. |
| NextLeftTarget | 8 | Moves the marker to the next left target encountered from the current marker position. If marker mode is Discrete, marker moves to the data point closest to the next left target. |
| NextRightTarget | 9 | Moves the marker to the next right target encountered from the current marker position. If marker mode is Discrete, marker moves to the data point closest to the next right target. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmarkertype.html language=enus -->
## TOPIC 00343: RFmxVnaMXMarkerType Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmarkertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmarkertype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the marker is disabled (Off) or is enabled (On) as a normal marker, delta marker or a fixed marker. The default value is Off. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXMarkerTypeMembersNameValueDescriptionOff0The marker is disabled. Normal1The marker is en

### RFmxVnaMXMarkerType Enumeration

Specifies whether the marker is disabled (Off) or is enabled (On) as a normal marker, delta marker or a fixed marker. The default value is *Off*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXMarkerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | The marker is disabled. |
| Normal | 1 | The marker is enabled as a normal marker. |
| Delta | 2 | The marker is enabled as a delta marker. |
| Fixed | 3 | The marker is enabled as a fixed marker. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxmeasurementtypes.html language=enus -->
## TOPIC 00344: RFmxVnaMXMeasurementTypes Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxmeasurementtypes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxmeasurementtypes.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXMeasurementTypesMembersNameValueDescriptionSParams0x1Selects SParams measurement. Waves0x2Selects Waves measurement. IQ0x4This enum value has been deprecated.

### RFmxVnaMXMeasurementTypes Enumeration

Specifies the type of measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXMeasurementTypes

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SParams | 0x1 | Selects SParams measurement. |
| Waves | 0x2 | Selects Waves measurement. |
| IQ | 0x4 | This enum value has been deprecated. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html language=enus -->
## TOPIC 00345: RFmxVnaMXPropertyId Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies all the attribute identifiers. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXPropertyIdMembersNameValueDescriptionTriggerType13631554Specifies the trigger type. DigitalEdgeTriggerSource13631555Specifies the source terminal for the digital edge trigger. This method is

### RFmxVnaMXPropertyId Enumeration

Specifies all the attribute identifiers.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXPropertyId

#### Members

| Name | Value | Description |
| --- | --- | --- |
| TriggerType | 13631554 | Specifies the trigger type. |
| DigitalEdgeTriggerSource | 13631555 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| DigitalEdgeTriggerEdge | 13631556 | Specifies the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| TriggerMode | 13631557 | Specifies the trigger mode. |
| TriggerDelay | 13631600 | Specifies the delay between the instance when the analyzer receives a trigger and the instance when it starts acquiring. This value is expressed in seconds. |
| ReadyForTriggerEventOutputTerminal | 13631587 | Specifies the destination terminal for the Ready For Trigger event. This event indicates to an external device responsible for sending triggers that the VNA is ready to receive the trigger. Use ReadyForTriggerEventLevel to define the polarity. |
| ReadyForTriggerEventTerminalName | 13631588 | Returns the fully qualified terminal name as a string. |
| ReadyForTriggerEventLevel | 13631589 | Specifies the trigger level for the Ready For Trigger event. This event indicates to an external device responsible for sending triggers that the VNA is ready to receive the trigger. |
| IndexEventOutputTerminal | 13631590 | Specifies the destination terminal for the Index event. This event indicates the analyzer has completed all the acquisitions for the signal. Use Index Event Level to define the polarity. |
| IndexEventTerminalName | 13631591 | Returns the fully qualified terminal name as a string. |
| IndexEventLevel | 13631592 | Specifies the trigger level for the Index event. This event indicates the analyzer has completed all the acquisitions for the signal. |
| SweepType | 13631534 | Specifies the sweep type for the measurement. |
| FrequencyList | 13631490 | Specifies the list of frequencies at which VNA calibration or measurement (OR just 'VNA measurement') is performed. The frequencies must be in increasing order and must not contain duplicates. This value is expressed in Hz. |
| StartFrequency | 13631569 | Specifies the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz. |
| StopFrequency | 13631570 | Specifies the highest frequency at which the measurement needs to be performed. This value is expressed in Hz. |
| CWFrequency | 13631594 | Specifies the frequency at which measurements are performed. This property is used only when you set the SweepType property to CWTime. This value is expressed in Hz. |
| NumberOfPoints | 13631571 | Specifies the number of points at which measurements are performed. This method is used only when you set the SweepType method to Linear or CWTime. |
| PowerLevel | 13631491 | Specifies the source power level for the VNA port. This value is expressed in dBm. |
| TestReceiverAttenuation | 13631498 | Specifies the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |
| IFBandwidth | 13631492 | Specifies the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth. |
| AutoIFBandwidthScalingEnabled | 13631558 | Specifies whether IF Bandwidth is scaled down at low frequencies. |
| SweepSequence | 13631533 | Specifies the sequence of acquisitions for various frequency points and source ports. |
| SweepDelay | 13631493 | Specifies the sweep delay. This value is expressed in seconds. |
| DwellTime | 13631494 | Specifies the time for which the analyzer waits before acquiring the signal for each measurement point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. |
| NumberOfSegments | 13631489 | Specifies the number of segments. |
| SegmentEnabled | 13631535 | Specifies whether to enable the selected segment for the sweep. |
| SegmentStartFrequency | 13631572 | Specifies the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |
| SegmentStopFrequency | 13631573 | Specifies the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |
| SegmentNumberOfFrequencyPoints | 13631574 | Specifies the number of frequency points of the segment at which the measurement needs to be performed. |
| SegmentPowerLevelEnabled | 13631560 | Specifies whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. |
| SegmentPowerLevel | 13631561 | Specifies the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to True. This value is expressed in dBm. |
| SegmentIFBandwidthEnabled | 13631562 | Specifies whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. |
| SegmentIFBandwidth | 13631563 | Specifies the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. |
| SegmentTestReceiverAttenuationEnabled | 13631564 | Specifies whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. |
| SegmentTestReceiverAttenuation | 13631565 | Specifies the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to True. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |
| SegmentDwellTimeEnabled | 13631566 | Specifies whether to enable individual Dwell Time value configured for each segment by Segment Dwell Time (s) method. If this is set to False, a common value will be used across all segments specified by Dwell Time (s) method. |
| SegmentDwellTime | 13631567 | Specifies the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. |
| PulseModeEnabled | 13631537 | Specifies whether to enable pulse mode for VNA measurement. |
| PulseTriggerType | 13631539 | Specifies the pulse trigger type. |
| PulseDigitalEdgeTriggerSource | 13631540 | Specifies the source terminal for the digital edge trigger. This method is used only when you set the PulseTriggerType method to DigitalEdge. |
| PulsePeriod | 13631541 | Specifies the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| PulseModulatorDelay | 13631543 | Specifies the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| PulseModulatorWidth | 13631544 | Specifies the duration for which the pulse is in ON state when you set the PulseModeEnabled method to True. This value is expressed in seconds. |
| PulseAcquisitionAuto | 13631545 | Specifies whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. |
| PulseAcquisitionDelay | 13631546 | Specifies the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True . This value is expressed in seconds. |
| PulseAcquisitionWidth | 13631547 | Specifies the width of pulse acquisition when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True. This value is expressed in seconds. |
| PulseGeneratorEnabled | 13631550 | Specifies whether to enable a pulse generator. |
| PulseGeneratorExportOutputTerminal | 13631551 | Specifies the destination terminal for an exported pulse generator. |
| PulseGeneratorTerminalName | 13631568 | Returns the fully qualified terminal name as a string. |
| PulseGeneratorDelay | 13631552 | Specifies the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the PulsePeriod method or derived from an external pulse trigger that you specify using the PulseDigitalEdgeTriggerSource method. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |
| PulseGeneratorWidth | 13631553 | Specifies the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |
| XAxisValues | 13631575 | Returns the the X-Axis Values (Stimulus) at which VNA calibration or VNA measurement is performed. These values correspond to frequency in Hz for sweep type set to List, Linear or Segment. They correspond to time in s for sweep type set to CW Time. |
| AveragingEnabled | 13631495 | Specifies whether to enable averaging for the VNA measurement. |
| AveragingCount | 13631496 | Specifies the number of times each measurement is repeated and averaged-over. This method is used only when you set the AveragingEnabled method to True. |
| CorrectionEnabled | 13631499 | Specifies whether to enable error correction for VNA measurement. |
| CorrectionInterpolationEnabled | 13631576 | Specifies whether to enable interpolation of error terms for corrected VNA measurement. This method is used only when you set the CorrectionEnabled method to True. |
| CorrectionPortSubsetEnabled | 13631502 | Specifies whether to enable correction for a subset of ports for which calibration data is avaialble in the calset. This property is used only when you set the CorrectionEnabled property to True. |
| CorrectionPortSubsetFullPorts | 13631503 | Specifies the subset of ports, that are selected for full N-Port correction, where N is the number of ports specified in this property. Use comma-separated list of ports to specify multiple ports. The configured measurement is full N-Port corrected if both the measurement receiver and source port are specified using this property. The configured measurement is one-path two-port corrected if one of the measurement ports is specified using this property and another is specified using CorrectionPortSubsetResponsePorts. Measurements involving the ports outside CorrectionPortSubsetFullPorts and CorrectionPortSubsetResponsePorts return error. |
| CorrectionPortSubsetResponsePorts | 13631609 | Specifies the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also one-path two-port corrected if one of the measurement port is specified using this property and another is specified using CorrectionPortSubsetFullPorts. Measurements involving the ports outside the CorrectionPortSubsetResponsePorts and CorrectionPortSubsetFullPorts return error. |
| CorrectionPortExtensionEnabled | 13631526 | Specifies whether to enable port extension for the VNA port. |
| CorrectionPortExtensionDelayDomain | 13631583 | Specifies whether port extension utilizes delay-based or distance-velocity factor-based definition when Port Extension Enabled is set to True. |
| CorrectionPortExtensionDelay | 13631527 | Specifies the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds. |
| CorrectionPortExtensionDistance | 13631584 | Specifies the port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is expressed in unit specified by Port Extension Distance Unit. |
| CorrectionPortExtensionDistanceUnit | 13631585 | Specifies the unit of port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. |
| CorrectionPortExtensionVelocityFactor | 13631586 | Specifies the speed of light in the port extension medium relative to speed of light in vacuum when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. |
| CorrectionPortExtensionDCLossEnabled | 13631528 | Specifies whether to compensate for the frequency independent loss when Port Extension Enabled is set to True. |
| CorrectionPortExtensionLossDCLoss | 13631529 | Specifies the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB. |
| CorrectionPortExtensionLoss1Enabled | 13631577 | Specifies whether to compensate for the frequency dependent loss, Loss1, as part of port extention. This method is used only when you set the CorrectionPortExtensionEnabled method to True. |
| CorrectionPortExtensionLoss1Frequency | 13631578 | Specifies the frequency at which Loss1 is applied and compensated when Port Extension Enabled is set to True and Port Extension Loss1 Enabled is set to True. This value is expressed in Hz. |
| CorrectionPortExtensionLoss1 | 13631579 | Specifies the frequency dependent loss to compensate when Port Extension Enabled is set to True and Port Extension Loss1 Enabled is set to True. This value is expressed in dB. |
| CorrectionPortExtensionLoss2Enabled | 13631580 | Specifies whether to compensate for the frequency dependent loss, Loss2, as part of port extention. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. |
| CorrectionPortExtensionLoss2Frequency | 13631581 | Specifies the frequency at which Loss2 is applied and compensated when Port Extension Enabled is set to True and Port Extension Loss2 Enabled is set to True. This value is expressed in Hz. |
| CorrectionPortExtensionLoss2 | 13631582 | Specifies the frequency dependent loss to compensate when Port Extension Enabled is set to True and Port Extension Loss2 Enabled is set to True. This value is expressed in dB. |
| CorrectionPortExtensionAutoLossEnabled | 13631610 | Specifies whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. |
| CorrectionPortExtensionAutoRegularizationEnabled | 13631611 | Specifies whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled) method to True. |
| CorrectionPortExtensionAutoFrequencyMode | 13631612 | Specifies the frequency mode over which the delay and loss (optional) values are determined. The default is Sweep. |
| CorrectionPortExtensionAutoStartFrequency | 13631613 | Specifies the start frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |
| CorrectionPortExtensionAutoStopFrequency | 13631614 | Specifies the stop frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |
| CorrectionCalibrationPorts | 13631504 | Specifies the ports requested for calibration. Use comma-separated list of ports to specify multiple ports. |
| CorrectionCalibrationConnectorType | 13631505 | Specifies the connector type of the DUT. The specified connector type must match be same as that of the selected calkit. |
| CorrectionCalibrationCalkitType | 13631506 | Specifies the type of calkit used for calibration. |
| CorrectionCalibrationCalkitElectronicResourceName | 13631507 | Specifies the resource name of the electronic calibration module (vCal) used for calibration. |
| CorrectionCalibrationCalkitElectronicOrientation | 13631518 | Specifies the orientation of the vCal fixture ports with respect to vCal ports. |
| CorrectionCalibrationCalkitMechanicalName | 13631508 | Specifies the name of the mechanical calkit used for measurement calibration when you set CorrectionCalibrationCalkitType method to Mechanical. |
| CorrectionCalibrationMethod | 13631509 | Specifies the calibration method. |
| CorrectionCalibrationThruMethod | 13631511 | Specifies the Thru calibration method when Calibration Method method is set to SOLT. |
| CorrectionCalibrationThruCoaxDelay | 13631512 | Specifies the delay of the Thru mechanical standard when CorrectionCalibrationCalkitType method is set to Mechanical and Thru Method method is set to Auto or Undefined Thru. This value is expressed in seconds. |
| CorrectionCalibrationStepCount | 13631513 | Returns the number of steps required to perform calibration. |
| CorrectionCalibrationStepDescription | 13631514 | Returns the description the calibration step. |
| CorrectionCalibrationEstimatedThruDelay | 13633536 | Returns the estimated Thru Delay when Thru Method is set to Undefined Thru or Undefined Thru Using Defined Thru. |
| SParamsMeasurementEnabled | 13635584 | Specifies whether to enable the Sparams measurement. |
| SParamsNumberOfSParameters | 13635586 | Specifies the number of S-Parameters to measure. |
| SParamsReceiverPort | 13635587 | Specifies the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2". |
| SParamsSourcePort | 13635588 | Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port1". |
| SParamsFormat | 13635589 | Specifies the format of S-Parameter measurement. |
| SParamsMagnitudeUnits | 13635590 | Specifies the magnitude units for all S-Parameters for which you set SParamsFormat method to Magnitude. |
| SParamsPhaseTraceType | 13635591 | Specifies the phase type for all S-Parameters for which SParamsFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |
| SParamsGroupDelayApertureMode | 13635612 | Specifies the aperture mode to be used for the computation of group delay for all S-Parameters for which SParamsFormat method is set to Group Delay. |
| SParamsGroupDelayAperturePoints | 13635613 | Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Points. You must set the value of this method between 2 and the total number of frequency points in the measurement frequency range. |
| SParamsGroupDelayAperturePercentage | 13635614 | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Percentage. |
| SParamsGroupDelayApertureFrequencySpan | 13635615 | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Frequency Span. |
| SParamsMathFunction | 13635610 | Specifies the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted. |
| SParamsMathActiveMeasurementMemory | 13635611 | Specifies the active measurement memory for performing mathematical operations when several measurement memories are associated with the configured S-Parameter. If only one measurement memory is associated with the configured S-Parameter, that measurement memory will be used for mathematical operations. |
| SParamsResultsCorrectionState | 13635608 | Returns the error correction state of the VNA S-Parameter measurement. |
| SParamsResultsCorrectionLevel | 13635616 | Returns the level of error correction applied to the specified S-Parameter measurement. |
| SParamsSnPDataFormat | 13635603 | Specifies the SParams Data Format of the S-parameter measurement to be saved. |
| SParamsSnPUserComment | 13635604 | Specifies user-specific additional information passed as SParams User Comment to write to SnP file. |
| SParamsSnPPorts | 13635605 | Specifies the Ports for which the S-parameter measurement is saved to file. |
| WavesMeasurementEnabled | 13639680 | Specifies whether to enable the Waves measurement. |
| WavesNumberOfWaves | 13639682 | Specifies the number of waves to be measured. |
| WavesReceiver | 13639683 | Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to Test (0), WavesReceiverPort to "port2" and WavesSourcePort to "port1". |
| WavesReceiverPort | 13639684 | Specifies the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), set this method to "port2" and WavesSourcePort to "port1". |
| WavesSourcePort | 13639685 | Specifies the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), WavesReceiverPort to "port2" and set this method to "port1". |
| WavesFormat | 13639686 | Specifies the format for wave measurement. |
| WavesMagnitudeUnits | 13639687 | Specifies the magnitude units for all waves for which WavesFormat method is set to Magnitude. |
| WavesPhaseTraceType | 13639688 | Specifies the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |
| WavesGroupDelayApertureMode | 13639701 | Specifies the aperture mode to be used for the computation of group delay for all waves for which WavesFormat method is set to Group Delay. |
| WavesGroupDelayAperturePoints | 13639702 | Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Points. You must set the value of this method between 2 and the total number of frequency points in the measurement frequency range. |
| WavesGroupDelayAperturePercentage | 13639703 | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Percentage. |
| WavesGroupDelayApertureFrequencySpan | 13639704 | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Frequency Span. |
| WavesResultsCorrectionState | 13639699 | Returns the error correction state of the VNA Waves measurement. |
| WavesResultsCorrectionLevel | 13639705 | Returns the level of error correction applied to the specified wave measurement. |
| IQMeasurementEnabled | 13635594 | This enum value has been deprecated. |
| IQAcquisitionTime | 13635597 | This enum value has been deprecated. |
| IQReceiverPort | 13635599 | This enum value has been deprecated. |
| IQSourcePort | 13635600 | This enum value has been deprecated. |
| IQResultsCorrectionState | 13635609 | This enum value has been deprecated. |
| LimitedConfigurationChange | 13639691 | Specifies the set of properties that are considered by NI-RFmx in the locked signal configuration state. |
| SourcePowerMode | 13639692 | Specifies whether to make VNA measurements with source turned off. |
| GroundTerminatedPorts | 13639693 | Specifies the instrument port to be ground terminated in case of SM2 devices. The ports passed to this property will be mutually exclusive to the ports passed to Selected Ports attribute. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |
| ResultFetchTimeout | 13680640 | Specifies the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. |
| SParamsParameter | 13635607 | Specifies the S-Parameter to be measured in format denoted by "S_(receiver port number)_(source port number)".For example, to measure S-Parameter for receiver port 2 and source port 1, set this method to "S21". |
| WavesParameter | 13639698 | Specifies the incident or scattered Wave Parameter to be measured in format denoted by "a_(receiver port number)_(source port number)" and "b_(receiver port number)_(source port number)" respectively. For example, to measure scattering wave parameter of receiver port 2 and source port 1, set this method to "b21". |
| NumberOfFrequencyPoints | 13631571 | This enum value has been deprecated. |
| CorrectionPortSubsetPorts | 13631503 | This enum value has been deprecated. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxpulseacquisitionauto.html language=enus -->
## TOPIC 00346: RFmxVnaMXPulseAcquisitionAuto Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxpulseacquisitionauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxpulseacquisitionauto.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXPulseAcquisitionAutoMembersNameValueDescriptionFalse0The PulseAcquisitionDelay and

### RFmxVnaMXPulseAcquisitionAuto Enumeration

Specifies whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXPulseAcquisitionAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | The PulseAcquisitionDelay and PulseAcquisitionWidth properties are not automatically set by the measurement. The values that you set for these properties are used by the measurement. |
| True | 1 | The measurement uses the PulseModulatorWidth method to compute pulse acquisition delay and pulse acquisition width. Pulse Acquisition Delay is set as the sum of Pulse Modulator Delay and approximately 20% of the Pulse Modulator Width, and Pulse Acquisition Width is set to approximately 75% of the Pulse Modulator Width.. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxpulsegeneratorenabled.html language=enus -->
## TOPIC 00347: RFmxVnaMXPulseGeneratorEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxpulsegeneratorenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxpulsegeneratorenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable a pulse generator. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXPulseGeneratorEnabledMembersNameValueDescriptionFalse0Disables the selected pulse generator. True1Enables the selected pulse generator.

### RFmxVnaMXPulseGeneratorEnabled Enumeration

Specifies whether to enable a pulse generator.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXPulseGeneratorEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the selected pulse generator. |
| True | 1 | Enables the selected pulse generator. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxreadyfortriggereventlevel.html language=enus -->
## TOPIC 00348: RFmxVnaMXReadyForTriggerEventLevel Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxreadyfortriggereventlevel.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxreadyfortriggereventlevel.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger level for the Ready For Trigger event.This event indicates to an external device responsible for sending triggers that the VNA is ready to receive the trigger. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXReadyForTriggerEventLevelRemarksThe TriggerMode yo

### RFmxVnaMXReadyForTriggerEventLevel Enumeration

Specifies the trigger level for the Ready For Trigger event.This event indicates to an external device responsible for sending triggers that the VNA is ready to receive the trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXReadyForTriggerEventLevel

#### Remarks

The [TriggerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) you configure determines the number of triggers needed for the VNA to complete the measurement. It also affects how often the *ready for trigger* event changes polarity. For example, when measuring S11 and S22 using a 2-port VNA with [TriggerType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) set to *Digital* or *Software*, and the *ready for trigger* event polarity set to *Active Low*, the polarity behavior for various [TriggerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) will be as follows: 
 1. [TriggerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is *Signal*: the VNA waits for only one instance of the trigger to be asserted before acquiring all data points. When VNA is ready to receive the trigger, the ready event polarity is LOW and switches to HIGH after a trigger is asserted. 
 2. [TriggerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is *Sweep*: the VNA waits for one instance of the trigger to be asserted before acquiring all data points that share a source port. When VNA is ready to receive the first trigger, the ready event polarity is LOW and switches to HIGH after the first trigger is asserted. The polarity remains HIGH until VNA completes all the acquisitions that require VNA port 1 as the source. When VNA is ready to receive the second trigger, the ready event polarity switches to LOW. Upon assertion of the second trigger, the polarity switches to HIGH. 
 3. [TriggerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is *Point*: the VNA waits for one instance of the trigger to be asserted before acquiring each data point. When VNA is ready to acquire a data point, the ready event polarity is LOW, and switches to HIGH after a trigger is asserted. The polarity remains HIGH until VNA is ready to acquire the next data point. 
 4. [TriggerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is *Segment* with segmented sweep across two frequency segments: the VNA waits for one instance of the trigger to be asserted before acquiring all data points within a segment that share a source port. When VNA is ready to receive the first trigger, the ready event polarity is LOW and switches to HIGH after the first trigger is asserted. The polarity remains HIGH until the VNA completes all the acquisitions for the first segment that require VNA port 1 as the source, and until the VNA is ready to receive the second trigger. When VNA is ready to receive the second trigger, the ready event polarity switches to LOW. Upon assertion of the second trigger, the polarity switches to HIGH. The polarity remains HIGH until VNA completes all the acquisitions for the second segment that require VNA port 1 as the source. The VNA is then ready to receive the second trigger, at which point the ready event polarity switches to LOW. Upon assertion of the second trigger, the polarity switches to HIGH and remains HIGH until the VNA completes all acquisitions for the second segment that require VNA port 1 as the source. The ready event polarity follows the same behavior for the third and fourth trigger instances, which are required to complete all acquisitions for the first and second segments that require VNA port 2 as the source, respectively.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 0 | Event level is HIGH when analyzer is ready to receive trigger. |
| ActiveLow | 1 | Event level is LOW when analyzer is ready to receive trigger. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxrestoreconfiguration.html language=enus -->
## TOPIC 00349: RFmxVnaMXRestoreConfiguration Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxrestoreconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxrestoreconfiguration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: specifies whether the stimulus settings from the specified calset should be applied to the signal. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXRestoreConfigurationMembersNameValueDescriptionNone0Do not apply the stimulus settings from the calset. Stimulus1Applies the stimulus

### RFmxVnaMXRestoreConfiguration Enumeration

specifies whether the stimulus settings from the specified calset should be applied to the signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXRestoreConfiguration

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | Do not apply the stimulus settings from the calset. |
| Stimulus | 1 | Applies the stimulus settings from the calset. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentenabled.html language=enus -->
## TOPIC 00350: RFmxVnaMXSegmentEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the selected segment for the sweep. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXSegmentEnabledMembersNameValueDescriptionFalse0Disables the selected segment. True1Enables the selected segment.

### RFmxVnaMXSegmentEnabled Enumeration

Specifies whether to enable the selected segment for the sweep.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXSegmentEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables the selected segment. |
| True | 1 | Enables the selected segment. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentifbandwidthenabled.html language=enus -->
## TOPIC 00351: RFmxVnaMXSegmentIFBandwidthEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentifbandwidthenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentifbandwidthenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVn

### RFmxVnaMXSegmentIFBandwidthEnabled Enumeration

Specifies whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXSegmentIFBandwidthEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables individual IF Bandwidth value configured for each segment. |
| True | 1 | Enables individual IF Bandwidth value configured for each segment. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentpowerlevelenabled.html language=enus -->
## TOPIC 00352: RFmxVnaMXSegmentPowerLevelEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentpowerlevelenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentpowerlevelenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum R

### RFmxVnaMXSegmentPowerLevelEnabled Enumeration

Specifies whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXSegmentPowerLevelEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables individual Power Level value configured for each segment. |
| True | 1 | Enables individual Power Level value configured for each segment. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsegmenttestreceiverattenuationenabled.html language=enus -->
## TOPIC 00353: RFmxVnaMXSegmentTestReceiverAttenuationEnabled Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsegmenttestreceiverattenuationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsegmenttestreceiverattenuationenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. SyntaxNamespace: NationalI

### RFmxVnaMXSegmentTestReceiverAttenuationEnabled Enumeration

Specifies whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXSegmentTestReceiverAttenuationEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| False | 0 | Disables individual Test Receiver Attenuation value configured for each segment. |
| True | 1 | Enables individual Test Receiver Attenuation value configured for each segment. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparams-configuration.html language=enus -->
## TOPIC 00354: Configuration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparams-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparams-configuration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxVnaMXSParamsConfiguration instance that provides methods to configure the SParams measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic RFmxVnaMXSParamsConfiguration Configuration { get; }

### Configuration

Gets the [RFmxVnaMXSParamsConfiguration](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration.html) instance that provides methods to configure the SParams measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public [RFmxVnaMXSParamsConfiguration](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration.html) Configuration { get; }

Parent topic:

RFmxVnaMXSParams Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparams.html language=enus -->
## TOPIC 00355: RFmxVnaMXSParams Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparams.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparams.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SParams measurement. Derives fromRFmxVnaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMXSParams : RFmxVnaMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxVnaMXSParamsConfiguration instance that provides methods to configure the SParams meas

### RFmxVnaMXSParams Class

Represents the SParams measurement.

#### Derives from

- RFmxVnaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMXSParams : RFmxVnaMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxVnaMXSParamsConfiguration instance that provides methods to configure the SParams measurement. |
| Results | Gets the RFmxVnaMXSParamsResults instance that provides methods to fetch and read the SParams measurement results. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-configuresparameter__string-string.html language=enus -->
## TOPIC 00356: ConfigureSParameter(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-configuresparameter__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-configuresparameter__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the S-Parameter to be measured in format S(receiver port number)(source port number) Use "sparam(n)" as the selector string to configure this method. This method sets SParamsSourcePort and SParamsReceiverPort methods.Supported Devices: NI PXIe-5633SyntaxNamespace: NationalInstruments.RFmx

### ConfigureSParameter(string, string)

Configures the S-Parameter to be measured in format S(receiver port number)(source port number) 
 Use "sparam(n)" as the selector string to configure this method. 
 This method sets [SParamsSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) and [SParamsReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) methods.*Supported Devices*: NI PXIe-5633

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureSParameter(string selectorString, string sParameter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sParameter | string | Specifies the S-Parameter to be measured. The default value is S11 |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getformat__string-out.html language=enus -->
## TOPIC 00357: GetFormat(string, out RFmxVnaMXSParamsFormat)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getformat__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getformat__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the format of S-Parameter measurement. Use 'sparam(n)' as the selector string to configure or read this attribute. Use RFmxVNA SParams Fetch Y Data to fetch the S-Parameters. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetFormat(string selectorString, out RFmxVnaMXSParamsFormat va

### GetFormat(string, out RFmxVnaMXSParamsFormat)

Gets the format of S-Parameter measurement. Use 'sparam(n)' as the selector string to configure or read this attribute. 
Use RFmxVNA SParams Fetch Y Data to fetch the S-Parameters.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetFormat(string selectorString, out RFmxVnaMXSParamsFormat value)

#### Remarks

This method gets the value of [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is (format type="bold")RFMXVNA_VAL_Magnitude(/format).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSParamsFormat | Upon return, contains the format of S-Parameter measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getgroupdelayaperturefrequencyspan__string-out.html language=enus -->
## TOPIC 00358: GetGroupDelayApertureFrequencySpan(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getgroupdelayaperturefrequencyspan__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getgroupdelayaperturefrequencyspan__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Frequency Span. SyntaxNamespace: N

### GetGroupDelayApertureFrequencySpan(string, out double)

Gets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all S-Parameters for which [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Group Delay* and SParams Group Delay Aperture Mode method is set to *Frequency Span*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetGroupDelayApertureFrequencySpan(string selectorString, out double value)

#### Remarks

This method gets the value of [SParamsGroupDelayApertureFrequencySpan](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 50 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Frequency Span. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getgroupdelayaperturepercentage__string-out.html language=enus -->
## TOPIC 00359: GetGroupDelayAperturePercentage(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getgroupdelayaperturepercentage__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getgroupdelayaperturepercentage__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which SParamsFormat method is set to Group Delay a

### GetGroupDelayAperturePercentage(string, out double)

Gets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Group Delay* and SParams Group Delay Aperture Mode method is set to *Percentage*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetGroupDelayAperturePercentage(string selectorString, out double value)

#### Remarks

This method gets the value of [SParamsGroupDelayAperturePercentage](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 5 %.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmagnitudeunits__string-out.html language=enus -->
## TOPIC 00360: GetMagnitudeUnits(string, out RFmxVnaMXSParamsMagnitudeUnits)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmagnitudeunits__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmagnitudeunits__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the magnitude units for all S-Parameters for which you set SParamsFormat method to Magnitude. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetMagnitudeUnits(string selectorString, out RFmxVnaMXSParamsMagnitudeUnits value)RemarksThis method gets the value of SParamsMagnitudeUnits at

### GetMagnitudeUnits(string, out RFmxVnaMXSParamsMagnitudeUnits)

Gets the magnitude units for all S-Parameters for which you set [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to *Magnitude*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetMagnitudeUnits(string selectorString, out RFmxVnaMXSParamsMagnitudeUnits value)

#### Remarks

This method gets the value of [SParamsMagnitudeUnits](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [dB](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsmagnitudeunits.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSParamsMagnitudeUnits | Upon return, contains the magnitude units for all S-Parameters for which you set SParamsFormat method to Magnitude. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmathactivemeasurementmemory__string-out.html language=enus -->
## TOPIC 00361: GetMathActiveMeasurementMemory(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmathactivemeasurementmemory__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmathactivemeasurementmemory__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the active measurement memory for performing mathematical operation when several measurement memories are associated with the configured S-Parameter. If only one measurement memory is associated with the configured S-Parameter, that measurement memory will be used for mathematical operations. S

### GetMathActiveMeasurementMemory(string, out string)

Gets the active measurement memory for performing mathematical operation when several measurement memories are associated with the configured S-Parameter. If only one measurement memory is associated with the configured S-Parameter, that measurement memory will be used for mathematical operations.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetMathActiveMeasurementMemory(string selectorString, out string value)

#### Remarks

This method gets the value of [SParamsMathActiveMeasurementMemory](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the sparam number and signal number. Example: "signal0" or "signal0/sparam0". You can use the BuildSParameterString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the active measurement memory for performing mathematical operation when several memories are associated with the configured S-Parameter. If only one memory is associated with the configured S-Parameter, that memory will be used for mathematical operations. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmathfunction__string-out.html language=enus -->
## TOPIC 00362: GetMathFunction(string, out RFmxVnaMXSParamsMathFunction)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmathfunction__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getmathfunction__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetMathFunction(string selectorString, out RFmxVnaMXSParamsM

### GetMathFunction(string, out RFmxVnaMXSParamsMathFunction)

Gets the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetMathFunction(string selectorString, out RFmxVnaMXSParamsMathFunction value)

#### Remarks

This method gets the value of [SParamsMathFunction](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Off](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsmathfunction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the sparam number and signal number. Example: "signal0" or "signal0/sparam0". You can use the BuildSParameterString(string, int) method to build the selector string. |
| value | out RFmxVnaMXSParamsMathFunction | Upon return, contains the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getreceiverport__string-out.html language=enus -->
## TOPIC 00363: GetReceiverPort(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getreceiverport__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getreceiverport__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2". SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetReceiverPort(string selectorString, out string value

### GetReceiverPort(string, out string)

Gets the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetReceiverPort(string selectorString, out string value)

#### Remarks

This method gets the value of [SParamsReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "port1".

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getsnpdataformat__string-out.html language=enus -->
## TOPIC 00364: GetSnPDataFormat(string, out RFmxVnaMXSParamsSnPDataFormat)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getsnpdataformat__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-getsnpdataformat__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SParams Data Format of the S-parameter measurement to be saved. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSnPDataFormat(string selectorString, out RFmxVnaMXSParamsSnPDataFormat value)RemarksThis method gets the value of SParamsSnPDataFormat attribute.The default value is

### GetSnPDataFormat(string, out RFmxVnaMXSParamsSnPDataFormat)

Gets the SParams Data Format of the S-parameter measurement to be saved.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSnPDataFormat(string selectorString, out RFmxVnaMXSParamsSnPDataFormat value)

#### Remarks

This method gets the value of [SParamsSnPDataFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamssnpdataformat.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSParamsSnPDataFormat | Upon return, contains the SParams Data Format of the S-parameter measurement to be saved. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setformat__string-rfmxvnamxsparamsformat.html language=enus -->
## TOPIC 00365: SetFormat(string, RFmxVnaMXSParamsFormat)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setformat__string-rfmxvnamxsparamsformat.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setformat__string-rfmxvnamxsparamsformat.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the format of S-Parameter measurement. Use 'sparam(n)' as the selector string to configure or read this attribute. Use RFmxVNA SParams Fetch Y Data to fetch the S-Parameters. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetFormat(string selectorString, RFmxVnaMXSParamsFormat value)

### SetFormat(string, RFmxVnaMXSParamsFormat)

Sets the format of S-Parameter measurement. Use 'sparam(n)' as the selector string to configure or read this attribute. 
Use RFmxVNA SParams Fetch Y Data to fetch the S-Parameters.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetFormat(string selectorString, RFmxVnaMXSParamsFormat value)

#### Remarks

This method sets the value of [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is (format type="bold")RFMXVNA_VAL_Magnitude(/format).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSParamsFormat | Specifies the format of S-Parameter measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturemode__string-rfmxvnamxsparamsgroupdelayaperturemode.html language=enus -->
## TOPIC 00366: SetGroupDelayApertureMode(string, RFmxVnaMXSParamsGroupDelayApertureMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturemode__string-rfmxvnamxsparamsgroupdelayaperturemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturemode__string-rfmxvnamxsparamsgroupdelayaperturemode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the group delay aperture mode used for the computation of group delay for all S-Parameters for which SParamsFormat method is set to Group Delay. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetGroupDelayApertureMode(string selectorString, RFmxVnaMXSParamsGroupDelayApertureMode valu

### SetGroupDelayApertureMode(string, RFmxVnaMXSParamsGroupDelayApertureMode)

Sets the group delay aperture mode used for the computation of group delay for all S-Parameters for which [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Group Delay*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetGroupDelayApertureMode(string selectorString, RFmxVnaMXSParamsGroupDelayApertureMode value)

#### Remarks

This method sets the value of [SParamsGroupDelayApertureMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Points](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsgroupdelayaperturemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSParamsGroupDelayApertureMode | Specifies the group delay aperture mode used for the computation of group delay for all S-Parameters for which SParamsFormat method is set to Group Delay. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturepercentage__string-double.html language=enus -->
## TOPIC 00367: SetGroupDelayAperturePercentage(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturepercentage__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturepercentage__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which SParamsFormat method is set to Group Delay a

### SetGroupDelayAperturePercentage(string, double)

Sets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Group Delay* and SParams Group Delay Aperture Mode method is set to *Percentage*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetGroupDelayAperturePercentage(string selectorString, double value)

#### Remarks

This method sets the value of [SParamsGroupDelayAperturePercentage](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 5 %.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturepoints__string-double.html language=enus -->
## TOPIC 00368: SetGroupDelayAperturePoints(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturepoints__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setgroupdelayaperturepoints__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the group delay aperture in terms of the number of frequency points that separates the two frequency points for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Points. You must set the value of this method between 2 an

### SetGroupDelayAperturePoints(string, double)

Sets the group delay aperture in terms of the number of frequency points that separates the two frequency points for all S-Parameters for which [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Group Delay* and SParams Group Delay Aperture Mode method is set to *Points*. You must set the value of this method between 2 and the total number of frequency points in the measurement frequency range.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetGroupDelayAperturePoints(string selectorString, double value)

#### Remarks

This method sets the value of [SParamsGroupDelayAperturePoints](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 11.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all S-Parameters for which SParamsFormat method is set to Group Delay and SParams Group Delay Aperture Mode method is set to Points. You must set the value of this method between 2 and the total number of frequency points in the measurement frequency range. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmagnitudeunits__string-rfmxvnamxsparamsmagnitudeunits.html language=enus -->
## TOPIC 00369: SetMagnitudeUnits(string, RFmxVnaMXSParamsMagnitudeUnits)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmagnitudeunits__string-rfmxvnamxsparamsmagnitudeunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmagnitudeunits__string-rfmxvnamxsparamsmagnitudeunits.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the magnitude units for all S-Parameters for which you set SParamsFormat method to Magnitude. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetMagnitudeUnits(string selectorString, RFmxVnaMXSParamsMagnitudeUnits value)RemarksThis method sets the value of SParamsMagnitudeUnits attrib

### SetMagnitudeUnits(string, RFmxVnaMXSParamsMagnitudeUnits)

Sets the magnitude units for all S-Parameters for which you set [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to *Magnitude*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetMagnitudeUnits(string selectorString, RFmxVnaMXSParamsMagnitudeUnits value)

#### Remarks

This method sets the value of [SParamsMagnitudeUnits](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [dB](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsmagnitudeunits.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSParamsMagnitudeUnits | Specifies the magnitude units for all S-Parameters for which you set SParamsFormat method to Magnitude. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmathfunction__string-rfmxvnamxsparamsmathfunction.html language=enus -->
## TOPIC 00370: SetMathFunction(string, RFmxVnaMXSParamsMathFunction)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmathfunction__string-rfmxvnamxsparamsmathfunction.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmathfunction__string-rfmxvnamxsparamsmathfunction.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetMathFunction(string selectorString, RFmxVnaMXSParamsMathF

### SetMathFunction(string, RFmxVnaMXSParamsMathFunction)

Sets the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetMathFunction(string selectorString, RFmxVnaMXSParamsMathFunction value)

#### Remarks

This method sets the value of [SParamsMathFunction](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Off](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsmathfunction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the sparam number and signal number. Example: "signal0" or "signal0/sparam0". You can use the BuildSParameterString(string, int) method to build the selector string. |
| value | RFmxVnaMXSParamsMathFunction | Specifies the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00371: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the Sparams measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of SParamsMeasurementEnabled attribute.The default value is False.ParametersNameTypeDescriptionselectorS

### SetMeasurementEnabled(string, bool)

Sets whether to enable the Sparams measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [SParamsMeasurementEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is False.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the Sparams measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setparameter__string-string.html language=enus -->
## TOPIC 00372: SetParameter(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setparameter__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setparameter__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the measured S-Parameter denoted by "S_(receiver port number)_(source port number)". For example, to measure S-Parameter for receiver port 2 and source port 1, set this method to "S21". SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetParameter(string selectorString, string value)Re

### SetParameter(string, string)

Sets the measured S-Parameter denoted by "S_(receiver port number)_(source port number)". For example, to measure S-Parameter for receiver port 2 and source port 1, set this method to "S21".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetParameter(string selectorString, string value)

#### Remarks

This method sets the value of [SParamsParameter](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "S11".

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the measured S-Parameter denoted by "S_(receiver port number)_(source port number)". For example, to measure S-Parameter for receiver port 2 and source port 1, set this method to "S21". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setphasetracetype__string-rfmxvnamxsparamsphasetracetype.html language=enus -->
## TOPIC 00373: SetPhaseTraceType(string, RFmxVnaMXSParamsPhaseTraceType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setphasetracetype__string-rfmxvnamxsparamsphasetracetype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setphasetracetype__string-rfmxvnamxsparamsphasetracetype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the phase type for all S-Parameters for which SParamsFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. SyntaxNamespace: NationalInstruments.

### SetPhaseTraceType(string, RFmxVnaMXSParamsPhaseTraceType)

Sets the phase type for all S-Parameters for which [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Phase*. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPhaseTraceType(string selectorString, RFmxVnaMXSParamsPhaseTraceType value)

#### Remarks

This method sets the value of [SParamsPhaseTraceType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Wrapped](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsphasetracetype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSParamsPhaseTraceType | Specifies the phase type for all S-Parameters for which SParamsFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setreceiverport__string-string.html language=enus -->
## TOPIC 00374: SetReceiverPort(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setreceiverport__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setreceiverport__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2". SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetReceiverPort(string selectorString, string value)Rem

### SetReceiverPort(string, string)

Sets the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetReceiverPort(string selectorString, string value)

#### Remarks

This method sets the value of [SParamsReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "port1".

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the receiver port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port2". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsnpdataformat__string-rfmxvnamxsparamssnpdataformat.html language=enus -->
## TOPIC 00375: SetSnPDataFormat(string, RFmxVnaMXSParamsSnPDataFormat)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsnpdataformat__string-rfmxvnamxsparamssnpdataformat.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsnpdataformat__string-rfmxvnamxsparamssnpdataformat.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SParams Data Format of the S-parameter measurement to be saved. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSnPDataFormat(string selectorString, RFmxVnaMXSParamsSnPDataFormat value)RemarksThis method sets the value of SParamsSnPDataFormat attribute.The default value is Auto

### SetSnPDataFormat(string, RFmxVnaMXSParamsSnPDataFormat)

Sets the SParams Data Format of the S-parameter measurement to be saved.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSnPDataFormat(string selectorString, RFmxVnaMXSParamsSnPDataFormat value)

#### Remarks

This method sets the value of [SParamsSnPDataFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamssnpdataformat.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXSParamsSnPDataFormat | Specifies the SParams Data Format of the S-parameter measurement to be saved. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsnpusercomment__string-string.html language=enus -->
## TOPIC 00376: SetSnPUserComment(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsnpusercomment__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsnpusercomment__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets user-specific additional information passed as SParams User Comment to write to SnP file. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSnPUserComment(string selectorString, string value)RemarksThis method sets the value of SParamsSnPUserComment attribute.ParametersNameTypeDescri

### SetSnPUserComment(string, string)

Sets user-specific additional information passed as SParams User Comment to write to SnP file.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSnPUserComment(string selectorString, string value)

#### Remarks

This method sets the value of [SParamsSnPUserComment](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies user-specific additional information passed as SParams User Comment to write to SnP file. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsourceport__string-string.html language=enus -->
## TOPIC 00377: SetSourcePort(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsourceport__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsconfiguration-setsourceport__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port1". SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetSourcePort(string selectorString, string value)Remarks

### SetSourcePort(string, string)

Sets the source port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port1".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSourcePort(string selectorString, string value)

#### Remarks

This method sets the value of [SParamsSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "port1".

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_(receiver port name)_(receiver port name)".For example, to measure S_port2_port1, set this method to "port1". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsgroupdelayaperturemode.html language=enus -->
## TOPIC 00378: RFmxVnaMXSParamsGroupDelayApertureMode Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsgroupdelayaperturemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsgroupdelayaperturemode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the aperture mode to be used for the computation of group delay for all S-Parameters for which SParamsFormat method is set to Group Delay. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXSParamsGroupDelayApertureModeMembersNameValueDescriptionPoints0Sets group delay ape

### RFmxVnaMXSParamsGroupDelayApertureMode Enumeration

Specifies the aperture mode to be used for the computation of group delay for all S-Parameters for which [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Group Delay*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXSParamsGroupDelayApertureMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Points | 0 | Sets group delay aperture mode to Points. Specify the aperture in terms of the number of frequency points by configuring SParamsGroupDelayAperturePoints method. |
| Percentage | 1 | Sets group delay aperture mode to Percentage. Specify the aperture in terms of the frequency separation expressed in percentage by configuring SParamsGroupDelayAperturePercentage method. |
| FrequencySpan | 2 | Sets group delay aperture mode to Frequency Span. Specify the aperture in terms of the frequency separation by configuring SParamsGroupDelayApertureFrequencySpan method. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsmathfunction.html language=enus -->
## TOPIC 00379: RFmxVnaMXSParamsMathFunction Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsmathfunction.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsmathfunction.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXSParamsMathFunctionMembersNameValueDescriptio

### RFmxVnaMXSParamsMathFunction Enumeration

Specifies the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXSParamsMathFunction

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | No mathematical operation is performed. |
| Add | 1 | Data in measurement memory is added to S-Parameter data. |
| Subtract | 2 | Data in measurement memory is subtracted from S-Parameter data. |
| Multiply | 3 | S-Parameter data is multiplied by the data in measurement memory. |
| Divide | 4 | S-Parameter data is divided by the data in measurement memory. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsphasetracetype.html language=enus -->
## TOPIC 00380: RFmxVnaMXSParamsPhaseTraceType Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsphasetracetype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsphasetracetype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase type for all S-Parameters for which SParamsFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. SyntaxNamespace: NationalInstrum

### RFmxVnaMXSParamsPhaseTraceType Enumeration

Specifies the phase type for all S-Parameters for which [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Phase*. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXSParamsPhaseTraceType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Wrapped | 0 | The reported S-Parameter phase is wrapped between -180 degress to +180 degrees. |
| Unwrapped | 1 | The reported S-Parameter phase is unwrapped. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-fetchcomplexdata__string-double-ref.html language=enus -->
## TOPIC 00381: FetchComplexData(string, double, ref ComplexSingle[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-fetchcomplexdata__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-fetchcomplexdata__string-double-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the S-Parameter data for the S-Parameters whose SParamsFormat is Complex. Use "sparam(n)" as the selector string to read results from this method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int FetchComplexData(string selectorString, double timeout, ref ComplexSingle[] complexData

### FetchComplexData(string, double, ref ComplexSingle[])

Fetches the S-Parameter data for the S-Parameters whose [SParamsFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is [Complex](nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsformat.html). 
 Use "sparam(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchComplexData(string selectorString, double timeout, ref ComplexSingle[] complexData)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and S-Parameter number. If you do not specify the result name, the default result instance is used. Example: "sparam0" "result::r1/sparam0" You can use the BuildSParameterString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the method waits until the measurement is complete. |
| complexData | ref ComplexSingle[] | Upon return, contains the measured S-Parameter complex array corresponding to the FrequencyList. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-fetchxdata__string-double-ref.html language=enus -->
## TOPIC 00382: FetchXData(string, double, ref double[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-fetchxdata__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-fetchxdata__string-double-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of frequency values when you perform S-Parameter measurement with SweepType method set to List or Linear or Segment. It fetches an array of time values when you perform S-Parameter measurement with SweepType method set to CWTime.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic

### FetchXData(string, double, ref double[])

Fetches an array of frequency values when you perform S-Parameter measurement with [SweepType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method set to [List](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html) or [Linear](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html) or [Segment](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html). It fetches an array of time values when you perform S-Parameter measurement with [SweepType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method set to [CWTime](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchXData(string selectorString, double timeout, ref double[] x)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the method waits until the measurement is complete. |
| x | ref double[] | Upon return, contains the frequencies at which measurements have been made for all the supported values of SweepType. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-getcorrectioneffectivelevel__string-out.html language=enus -->
## TOPIC 00383: GetCorrectionEffectiveLevel(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-getcorrectioneffectivelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-getcorrectioneffectivelevel__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionEffectiveLevel(string selectorString, out string value)

### GetCorrectionEffectiveLevel(string, out string)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionEffectiveLevel(string selectorString, out string value)

Parent topic:

RFmxVnaMXSParamsResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-getcorrectionlevel__string-out.html language=enus -->
## TOPIC 00384: GetCorrectionLevel(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-getcorrectionlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsparamsresults-getcorrectionlevel__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the correction level of the VNA S-Parameter measurement.Use 'sparam(n)' as the selector string to read this attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionLevel(string selectorString, out string value)RemarksThis method gets the value of SParamsResultsCorrecti

### GetCorrectionLevel(string, out string)

Gets the correction level of the VNA S-Parameter measurement.Use 'sparam(n)' as the selector string to read this attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionLevel(string selectorString, out string value)

#### Remarks

SParamsResultsCorrectionLevel

| Correction Level | Description |
| --- | --- |
| Uncorrected | Correction is not applied to the configured S-Parameter. |
| N-Port | Full N-Port correction is applied to the configured S-Parameter, where N refers to the number of VNA ports involved in the correction. |
| 1-Path | One Path Two Port correction is applied to the configured transmission measurement. Refer to CorrectionPortSubsetResponsePorts property for more information about one-path two-port correction. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the correction level of the VNA S-Parameter measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXSParamsResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxsweepsequence.html language=enus -->
## TOPIC 00385: RFmxVnaMXSweepSequence Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxsweepsequence.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxsweepsequence.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sequence of acquisitions for various frequency points and source ports. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXSweepSequenceMembersNameValueDescriptionStandard0Acquisitions for all frequency points are completed with the first source port before moving to t

### RFmxVnaMXSweepSequence Enumeration

Specifies the sequence of acquisitions for various frequency points and source ports.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXSweepSequence

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Standard | 0 | Acquisitions for all frequency points are completed with the first source port before moving to the next source port. For example, if there are three frequency points f1, f2 and f3 and two source ports, port1 and port2, then the sweep sequence will be (f1, port1), (f2, port1), (f3, port1), (f1, port2), (f2, port2), (f3, port2). |
| Point | 1 | All acquisitions for a frequency point are completed with all required source ports, before moving to the next frequency point. For example, if there are three frequency points f1, f2 and f3 and two source ports, port1 and port2, then the sweep sequence will be (f1, port1), (f1, port2), (f2, port1), (f2, port2), (f3, port1), (f3, port2). |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxtriggertype.html language=enus -->
## TOPIC 00386: RFmxVnaMXTriggerType Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxtriggertype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxtriggertype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXTriggerTypeMembersNameValueDescriptionNone0No trigger is configured. DigitalEdge1The trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital

### RFmxVnaMXTriggerType Enumeration

Specifies the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXTriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No trigger is configured. |
| DigitalEdge | 1 | The trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the DigitalEdgeTriggerSource method. |
| Software | 2 | The trigger is not asserted until a software trigger occurs. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwaves-configuration.html language=enus -->
## TOPIC 00387: Configuration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwaves-configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwaves-configuration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxVnaMXWavesConfiguration instance that provides methods to configure the Waves measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic RFmxVnaMXWavesConfiguration Configuration { get; }

### Configuration

Gets the [RFmxVnaMXWavesConfiguration](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration.html) instance that provides methods to configure the Waves measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public [RFmxVnaMXWavesConfiguration](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration.html) Configuration { get; }

Parent topic:

RFmxVnaMXWaves Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwaves-results.html language=enus -->
## TOPIC 00388: Results

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwaves-results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwaves-results.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxVnaMXWavesResults instance that provides methods to fetch and read the Waves measurement results. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic RFmxVnaMXWavesResults Results { get; }

### Results

Gets the [RFmxVnaMXWavesResults](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults.html) instance that provides methods to fetch and read the Waves measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public [RFmxVnaMXWavesResults](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults.html) Results { get; }

Parent topic:

RFmxVnaMXWaves Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwaves.html language=enus -->
## TOPIC 00389: RFmxVnaMXWaves Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwaves.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwaves.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Waves measurement. Derives fromRFmxVnaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMXWaves : RFmxVnaMXSubObjectPropertiesNameDescriptionConfigurationGets the RFmxVnaMXWavesConfiguration instance that provides methods to configure the Waves measurement.

### RFmxVnaMXWaves Class

Represents the Waves measurement.

#### Derives from

- RFmxVnaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMXWaves : RFmxVnaMXSubObject

#### Properties

| Name | Description |
| --- | --- |
| Configuration | Gets the RFmxVnaMXWavesConfiguration instance that provides methods to configure the Waves measurement. |
| Results | Gets the RFmxVnaMXWavesResults instance that provides methods to fetch and read the Waves measurement results. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-configurewave__string-string.html language=enus -->
## TOPIC 00390: ConfigureWave(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-configurewave__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-configurewave__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the wave to be measured in format a(receiver port number)(source port number) or b(receiver port number)(source port number), where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. Use "wave(n)" as the selector string to configure

### ConfigureWave(string, string)

Configures the wave to be measured in format a(receiver port number)(source port number) or b(receiver port number)(source port number), where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. 
 Use "wave(n)" as the selector string to configure this method.*Supported Devices*: NI PXIe-5633

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureWave(string selectorString, string wave)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the signal name, result name, and wave number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. |
| wave | string | Specifies the wave to be measured. The default value is b11. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getformat__string-out.html language=enus -->
## TOPIC 00391: GetFormat(string, out RFmxVnaMXWavesFormat)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getformat__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getformat__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the format for wave measurement. Use 'wave(n)' as the selector string to configure or read this attribute. Use RFmxVNA Waves Fetch Y Data to fetch the waves. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetFormat(string selectorString, out RFmxVnaMXWavesFormat value)RemarksThis met

### GetFormat(string, out RFmxVnaMXWavesFormat)

Gets the format for wave measurement. Use 'wave(n)' as the selector string to configure or read this attribute. 
 Use RFmxVNA Waves Fetch Y Data to fetch the waves.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetFormat(string selectorString, out RFmxVnaMXWavesFormat value)

#### Remarks

This method gets the value of [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is (format type="bold")RFMXVNA_VAL_Magnitude(/format).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXWavesFormat | Upon return, contains the format for wave measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getgroupdelayaperturepercentage__string-out.html language=enus -->
## TOPIC 00392: GetGroupDelayAperturePercentage(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getgroupdelayaperturepercentage__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getgroupdelayaperturepercentage__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which WavesFormat method is set to GroupDelay and Waves G

### GetGroupDelayAperturePercentage(string, out double)

Gets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [GroupDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html) and Waves Group Delay Aperture Mode method is set to *Percentage*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetGroupDelayAperturePercentage(string selectorString, out double value)

#### Remarks

This method gets the value of [WavesGroupDelayAperturePercentage](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 5 %.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getgroupdelayaperturepoints__string-out.html language=enus -->
## TOPIC 00393: GetGroupDelayAperturePoints(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getgroupdelayaperturepoints__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getgroupdelayaperturepoints__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Points. You must set the value of this method between 2 and the total

### GetGroupDelayAperturePoints(string, out double)

Gets the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [GroupDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html) and Waves Group Delay Aperture Mode method is set to *Points*. You must set the value of this method between 2 and the total number of frequency points in the measurement frequency range.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetGroupDelayAperturePoints(string selectorString, out double value)

#### Remarks

This method gets the value of [WavesGroupDelayAperturePoints](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 11.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Points. You must set the value of this method between 2 and the total number of frequency points in the measurement frequency range. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getmagnitudeunits__string-out.html language=enus -->
## TOPIC 00394: GetMagnitudeUnits(string, out RFmxVnaMXWavesMagnitudeUnits)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getmagnitudeunits__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getmagnitudeunits__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the magnitude units for all waves for which WavesFormat method is set to Magnitude. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetMagnitudeUnits(string selectorString, out RFmxVnaMXWavesMagnitudeUnits value)RemarksThis method gets the value of WavesMagnitudeUnits attribute.The de

### GetMagnitudeUnits(string, out RFmxVnaMXWavesMagnitudeUnits)

Gets the magnitude units for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [Magnitude](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetMagnitudeUnits(string selectorString, out RFmxVnaMXWavesMagnitudeUnits value)

#### Remarks

This method gets the value of [WavesMagnitudeUnits](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [dBmV](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesmagnitudeunits.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXWavesMagnitudeUnits | Upon return, contains the magnitude units for all waves for which WavesFormat method is set to Magnitude. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getmeasurementenabled__string-out.html language=enus -->
## TOPIC 00395: GetMeasurementEnabled(string, out bool)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getmeasurementenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getmeasurementenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the Waves measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetMeasurementEnabled(string selectorString, out bool value)RemarksThis method gets the value of WavesMeasurementEnabled attribute.The default value is False.ParametersNameTypeDescriptionselectorS

### GetMeasurementEnabled(string, out bool)

Gets whether to enable the Waves measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetMeasurementEnabled(string selectorString, out bool value)

#### Remarks

This method gets the value of [WavesMeasurementEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is False.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out bool | Upon return, contains whether to enable the Waves measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getnumberofwaves__string-out.html language=enus -->
## TOPIC 00396: GetNumberOfWaves(string, out int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getnumberofwaves__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getnumberofwaves__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of waves to be measured. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetNumberOfWaves(string selectorString, out int value)RemarksThis method gets the value of WavesNumberOfWaves attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringPass an e

### GetNumberOfWaves(string, out int)

Gets the number of waves to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetNumberOfWaves(string selectorString, out int value)

#### Remarks

This method gets the value of [WavesNumberOfWaves](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of waves to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getparameter__string-out.html language=enus -->
## TOPIC 00397: GetParameter(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getparameter__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getparameter__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetParameter(string selectorString, out string value)

### GetParameter(string, out string)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetParameter(string selectorString, out string value)

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getphasetracetype__string-out.html language=enus -->
## TOPIC 00398: GetPhaseTraceType(string, out RFmxVnaMXWavesPhaseTraceType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getphasetracetype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getphasetracetype__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. SyntaxNamespace: NationalInstruments.RFmx.VnaM

### GetPhaseTraceType(string, out RFmxVnaMXWavesPhaseTraceType)

Gets the phase type for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [Phase](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html). Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPhaseTraceType(string selectorString, out RFmxVnaMXWavesPhaseTraceType value)

#### Remarks

This method gets the value of [WavesPhaseTraceType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Wrapped](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesphasetracetype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXWavesPhaseTraceType | Upon return, contains the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getreceiver__string-out.html language=enus -->
## TOPIC 00399: GetReceiver(string, out RFmxVnaMXWavesReceiver)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getreceiver__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getreceiver__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are m

### GetReceiver(string, out RFmxVnaMXWavesReceiver)

Gets whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to *Test (0)*, [WavesReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port2" and [WavesSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port1".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetReceiver(string selectorString, out RFmxVnaMXWavesReceiver value)

#### Remarks

This method gets the value of [WavesReceiver](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Test](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesreceiver.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the wave number. Example: "" or "wave0". You can use the BuildWaveString(string, int) method to build the selector string. |
| value | out RFmxVnaMXWavesReceiver | Upon return, contains whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to Test (0), WavesReceiverPort to "port2" and WavesSourcePort to "port1". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getreceiverport__string-out.html language=enus -->
## TOPIC 00400: GetReceiverPort(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getreceiverport__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getreceiverport__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respec

### GetReceiverPort(string, out string)

Gets the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set [WavesReceiver](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to *Test (0)*, set this method to "port2" and [WavesSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port1".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetReceiverPort(string selectorString, out string value)

#### Remarks

This method gets the value of [WavesReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "port1".

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the wave number. Example: "" or "wave0". You can use the BuildWaveString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), set this method to "port2" and WavesSourcePort to "port1". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getsourceport__string-out.html language=enus -->
## TOPIC 00401: GetSourcePort(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getsourceport__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getsourceport__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respecti

### GetSourcePort(string, out string)

Gets the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set [WavesReceiver](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to *Test (0)*, [WavesReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port2" and set this method to "port1".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSourcePort(string selectorString, out string value)

#### Remarks

This method gets the value of [WavesSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "port1".

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the wave number. Example: "" or "wave0". You can use the BuildWaveString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), WavesReceiverPort to "port2" and set this method to "port1". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getwave__string-out.html language=enus -->
## TOPIC 00402: GetWave(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getwave__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-getwave__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the wave being measured in format a(receiver port number)(source port number) or b(receiver port number)(source port number), where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. Use "wave(n)" as the selector string for this method

### GetWave(string, out string)

Returns the wave being measured in format a(receiver port number)(source port number) or b(receiver port number)(source port number), where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. 
 Use "wave(n)" as the selector string for this method.*Supported Devices*: NI PXIe-5633

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetWave(string selectorString, out string wave)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and wave number. If you do not specify the result name, the default result instance is used."wave0""result::r1/wave0"You can use the BuildWaveString(string, int) method to build the selector string. |
| wave | out string | Upon return, contains the wave being measured in format a(receiver port number)(source port number) or b(receiver port number)(source port number), where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setformat__string-rfmxvnamxwavesformat.html language=enus -->
## TOPIC 00403: SetFormat(string, RFmxVnaMXWavesFormat)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setformat__string-rfmxvnamxwavesformat.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setformat__string-rfmxvnamxwavesformat.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the format for wave measurement. Use 'wave(n)' as the selector string to configure or read this attribute. Use RFmxVNA Waves Fetch Y Data to fetch the waves. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetFormat(string selectorString, RFmxVnaMXWavesFormat value)RemarksThis method

### SetFormat(string, RFmxVnaMXWavesFormat)

Sets the format for wave measurement. Use 'wave(n)' as the selector string to configure or read this attribute. 
 Use RFmxVNA Waves Fetch Y Data to fetch the waves.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetFormat(string selectorString, RFmxVnaMXWavesFormat value)

#### Remarks

This method sets the value of [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is (format type="bold")RFMXVNA_VAL_Magnitude(/format).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXWavesFormat | Specifies the format for wave measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturefrequencyspan__string-double.html language=enus -->
## TOPIC 00404: SetGroupDelayApertureFrequencySpan(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturefrequencyspan__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturefrequencyspan__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Frequency Span. SyntaxNamespace: NationalInstr

### SetGroupDelayApertureFrequencySpan(string, double)

Sets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [GroupDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html) and Waves Group Delay Aperture Mode method is set to *Frequency Span*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetGroupDelayApertureFrequencySpan(string selectorString, double value)

#### Remarks

This method sets the value of [WavesGroupDelayApertureFrequencySpan](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 50 MHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Frequency Span. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturemode__string-rfmxvnamxwavesgroupdelayaperturemode.html language=enus -->
## TOPIC 00405: SetGroupDelayApertureMode(string, RFmxVnaMXWavesGroupDelayApertureMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturemode__string-rfmxvnamxwavesgroupdelayaperturemode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturemode__string-rfmxvnamxwavesgroupdelayaperturemode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the group delay aperture mode used for the computation of group delay for all waves for which WavesFormat method is set to Group Delay. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetGroupDelayApertureMode(string selectorString, RFmxVnaMXWavesGroupDelayApertureMode value)RemarksTh

### SetGroupDelayApertureMode(string, RFmxVnaMXWavesGroupDelayApertureMode)

Sets the group delay aperture mode used for the computation of group delay for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to *Group Delay*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetGroupDelayApertureMode(string selectorString, RFmxVnaMXWavesGroupDelayApertureMode value)

#### Remarks

This method sets the value of [WavesGroupDelayApertureMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Points](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesgroupdelayaperturemode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXWavesGroupDelayApertureMode | Specifies the group delay aperture mode used for the computation of group delay for all waves for which WavesFormat method is set to Group Delay. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturepercentage__string-double.html language=enus -->
## TOPIC 00406: SetGroupDelayAperturePercentage(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturepercentage__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setgroupdelayaperturepercentage__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which WavesFormat method is set to GroupDelay and Waves G

### SetGroupDelayAperturePercentage(string, double)

Sets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [GroupDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html) and Waves Group Delay Aperture Mode method is set to *Percentage*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetGroupDelayAperturePercentage(string selectorString, double value)

#### Remarks

This method sets the value of [WavesGroupDelayAperturePercentage](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 5 %.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Percentage. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setmagnitudeunits__string-rfmxvnamxwavesmagnitudeunits.html language=enus -->
## TOPIC 00407: SetMagnitudeUnits(string, RFmxVnaMXWavesMagnitudeUnits)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setmagnitudeunits__string-rfmxvnamxwavesmagnitudeunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setmagnitudeunits__string-rfmxvnamxwavesmagnitudeunits.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the magnitude units for all waves for which WavesFormat method is set to Magnitude. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetMagnitudeUnits(string selectorString, RFmxVnaMXWavesMagnitudeUnits value)RemarksThis method sets the value of WavesMagnitudeUnits attribute.The defaul

### SetMagnitudeUnits(string, RFmxVnaMXWavesMagnitudeUnits)

Sets the magnitude units for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [Magnitude](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetMagnitudeUnits(string selectorString, RFmxVnaMXWavesMagnitudeUnits value)

#### Remarks

This method sets the value of [WavesMagnitudeUnits](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [dBmV](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesmagnitudeunits.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXWavesMagnitudeUnits | Specifies the magnitude units for all waves for which WavesFormat method is set to Magnitude. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setmeasurementenabled__string-bool.html language=enus -->
## TOPIC 00408: SetMeasurementEnabled(string, bool)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setmeasurementenabled__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setmeasurementenabled__string-bool.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable the Waves measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetMeasurementEnabled(string selectorString, bool value)RemarksThis method sets the value of WavesMeasurementEnabled attribute.The default value is False.ParametersNameTypeDescriptionselectorStrin

### SetMeasurementEnabled(string, bool)

Sets whether to enable the Waves measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetMeasurementEnabled(string selectorString, bool value)

#### Remarks

This method sets the value of [WavesMeasurementEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is False.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | bool | Specifies whether to enable the Waves measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setnumberofwaves__string-int.html language=enus -->
## TOPIC 00409: SetNumberOfWaves(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setnumberofwaves__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setnumberofwaves__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of waves to be measured. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetNumberOfWaves(string selectorString, int value)RemarksThis method sets the value of WavesNumberOfWaves attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringPass an empty

### SetNumberOfWaves(string, int)

Sets the number of waves to be measured.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetNumberOfWaves(string selectorString, int value)

#### Remarks

This method sets the value of [WavesNumberOfWaves](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of waves to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setparameter__string-string.html language=enus -->
## TOPIC 00410: SetParameter(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setparameter__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setparameter__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetParameter(string selectorString, string value)

### SetParameter(string, string)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetParameter(string selectorString, string value)

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setphasetracetype__string-rfmxvnamxwavesphasetracetype.html language=enus -->
## TOPIC 00411: SetPhaseTraceType(string, RFmxVnaMXWavesPhaseTraceType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setphasetracetype__string-rfmxvnamxwavesphasetracetype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setphasetracetype__string-rfmxvnamxwavesphasetracetype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. SyntaxNamespace: NationalInstruments.RFmx.VnaM

### SetPhaseTraceType(string, RFmxVnaMXWavesPhaseTraceType)

Sets the phase type for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [Phase](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html). Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPhaseTraceType(string selectorString, RFmxVnaMXWavesPhaseTraceType value)

#### Remarks

This method sets the value of [WavesPhaseTraceType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Wrapped](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesphasetracetype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXWavesPhaseTraceType | Specifies the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setreceiver__string-rfmxvnamxwavesreceiver.html language=enus -->
## TOPIC 00412: SetReceiver(string, RFmxVnaMXWavesReceiver)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setreceiver__string-rfmxvnamxwavesreceiver.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setreceiver__string-rfmxvnamxwavesreceiver.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are m

### SetReceiver(string, RFmxVnaMXWavesReceiver)

Sets whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to *Test (0)*, [WavesReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port2" and [WavesSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port1".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetReceiver(string selectorString, RFmxVnaMXWavesReceiver value)

#### Remarks

This method sets the value of [WavesReceiver](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Test](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesreceiver.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the wave number. Example: "" or "wave0". You can use the BuildWaveString(string, int) method to build the selector string. |
| value | RFmxVnaMXWavesReceiver | Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to Test (0), WavesReceiverPort to "port2" and WavesSourcePort to "port1". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setreceiverport__string-string.html language=enus -->
## TOPIC 00413: SetReceiverPort(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setreceiverport__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setreceiverport__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respec

### SetReceiverPort(string, string)

Sets the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set [WavesReceiver](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to *Test (0)*, set this method to "port2" and [WavesSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port1".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetReceiverPort(string selectorString, string value)

#### Remarks

This method sets the value of [WavesReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "port1".

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the wave number. Example: "" or "wave0". You can use the BuildWaveString(string, int) method to build the selector string. |
| value | string | Specifies the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), set this method to "port2" and WavesSourcePort to "port1". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setsourceport__string-string.html language=enus -->
## TOPIC 00414: SetSourcePort(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setsourceport__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration-setsourceport__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respecti

### SetSourcePort(string, string)

Sets the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set [WavesReceiver](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to *Test (0)*, [WavesReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port2" and set this method to "port1".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetSourcePort(string selectorString, string value)

#### Remarks

This method sets the value of [WavesSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "port1".

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the wave number. Example: "" or "wave0". You can use the BuildWaveString(string, int) method to build the selector string. |
| value | string | Specifies the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), WavesReceiverPort to "port2" and set this method to "port1". |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesConfiguration Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration.html language=enus -->
## TOPIC 00415: RFmxVnaMXWavesConfiguration Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesconfiguration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure the Waves measurement. Derives fromRFmxVnaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMXWavesConfiguration : RFmxVnaMXSubObjectMethodsNameDescriptionConfigureWave(string, string)Configures the wave to be measured in format a(receiver po

### RFmxVnaMXWavesConfiguration Class

Provides methods to configure the Waves measurement.

#### Derives from

- RFmxVnaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMXWavesConfiguration : RFmxVnaMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| ConfigureWave(string, string) | Configures the wave to be measured in format a(receiver port number)(source port number) or b(receiver port number)(source port number), where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. Use "wave(n)" as the selector string to configure this method.Supported Devices: NI PXIe-5633 |
| GetFormat(string, out RFmxVnaMXWavesFormat) | Gets the format for wave measurement. Use 'wave(n)' as the selector string to configure or read this attribute. Use RFmxVNA Waves Fetch Y Data to fetch the waves. |
| GetGroupDelayApertureFrequencySpan(string, out double) | Gets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Frequency Span. |
| GetGroupDelayApertureMode(string, out RFmxVnaMXWavesGroupDelayApertureMode) | Gets the group delay aperture mode used for the computation of group delay for all waves for which WavesFormat method is set to Group Delay. |
| GetGroupDelayAperturePercentage(string, out double) | Gets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Percentage. |
| GetGroupDelayAperturePoints(string, out double) | Gets the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Points. You must set the value of this method between 2 and the total number of frequency points in the measurement frequency range. |
| GetMagnitudeUnits(string, out RFmxVnaMXWavesMagnitudeUnits) | Gets the magnitude units for all waves for which WavesFormat method is set to Magnitude. |
| GetMeasurementEnabled(string, out bool) | Gets whether to enable the Waves measurement. |
| GetNumberOfWaves(string, out int) | Gets the number of waves to be measured. |
| GetParameter(string, out string) |  |
| GetPhaseTraceType(string, out RFmxVnaMXWavesPhaseTraceType) | Gets the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |
| GetReceiver(string, out RFmxVnaMXWavesReceiver) | Gets whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to Test (0), WavesReceiverPort to "port2" and WavesSourcePort to "port1". |
| GetReceiverPort(string, out string) | Gets the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), set this method to "port2" and WavesSourcePort to "port1". |
| GetSourcePort(string, out string) | Gets the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), WavesReceiverPort to "port2" and set this method to "port1". |
| GetWave(string, out string) | Returns the wave being measured in format a(receiver port number)(source port number) or b(receiver port number)(source port number), where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. Use "wave(n)" as the selector string for this method.Supported Devices: NI PXIe-5633 |
| SetFormat(string, RFmxVnaMXWavesFormat) | Sets the format for wave measurement. Use 'wave(n)' as the selector string to configure or read this attribute. Use RFmxVNA Waves Fetch Y Data to fetch the waves. |
| SetGroupDelayApertureFrequencySpan(string, double) | Sets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Frequency Span. |
| SetGroupDelayApertureMode(string, RFmxVnaMXWavesGroupDelayApertureMode) | Sets the group delay aperture mode used for the computation of group delay for all waves for which WavesFormat method is set to Group Delay. |
| SetGroupDelayAperturePercentage(string, double) | Sets the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Percentage. |
| SetGroupDelayAperturePoints(string, double) | Sets the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which WavesFormat method is set to GroupDelay and Waves Group Delay Aperture Mode method is set to Points. You must set the value of this method between 2 and the total number of frequency points in the measurement frequency range. |
| SetMagnitudeUnits(string, RFmxVnaMXWavesMagnitudeUnits) | Sets the magnitude units for all waves for which WavesFormat method is set to Magnitude. |
| SetMeasurementEnabled(string, bool) | Sets whether to enable the Waves measurement. |
| SetNumberOfWaves(string, int) | Sets the number of waves to be measured. |
| SetParameter(string, string) |  |
| SetPhaseTraceType(string, RFmxVnaMXWavesPhaseTraceType) | Sets the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |
| SetReceiver(string, RFmxVnaMXWavesReceiver) | Sets whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to Test (0), WavesReceiverPort to "port2" and WavesSourcePort to "port1". |
| SetReceiverPort(string, string) | Sets the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), set this method to "port2" and WavesSourcePort to "port1". |
| SetSourcePort(string, string) | Sets the source port name for wave measurement. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set WavesReceiver to Test (0), WavesReceiverPort to "port2" and set this method to "port1". |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavescorrectionstate.html language=enus -->
## TOPIC 00416: RFmxVnaMXWavesCorrectionState Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavescorrectionstate.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavescorrectionstate.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the error correction state of the VNA Waves measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXWavesCorrectionStateMembersNameValueDescriptionNone0Error correction is not applied. Corrected1Error correction is applied without interpolation using the error terms

### RFmxVnaMXWavesCorrectionState Enumeration

Returns the error correction state of the VNA Waves measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXWavesCorrectionState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | Error correction is not applied. |
| Corrected | 1 | Error correction is applied without interpolation using the error terms from the calset. |
| Interpolated | 2 | Error correction is applied with error terms for at least one sweep point interpolated from the calset error terms. |
| SettingsModified | 3 | Settings during the measurment differ from those used during calibration. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html language=enus -->
## TOPIC 00417: RFmxVnaMXWavesFormat Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the format for wave measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXWavesFormatMembersNameValueDescriptionMagnitude0The magnitude of the wave is reported. Specify the magnitude unit by configuring Wave Magnitude Units method. Phase1The phase of the wave is

### RFmxVnaMXWavesFormat Enumeration

Specifies the format for wave measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXWavesFormat

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Magnitude | 0 | The magnitude of the wave is reported. Specify the magnitude unit by configuring Wave Magnitude Units method. |
| Phase | 1 | The phase of the wave is reported in degrees. Specify the phase type by configuring Wave Phase Trace Type method. |
| Complex | 2 | The complex wave value is reported in Real-Imaginary format. |
| Swr | 3 | The standing wave ratio computed from wave is reported. It is a unitless quantity. |
| SmithImpedance | 4 | The impedance value computed from wave is reported in ohms. |
| SmithAdmittance | 5 | The admittance value computed from wave is reported in siemens. |
| Polar | 6 | The complex wave is reported in magnitude-phase format, where the magnitude is always in linear scale and the wrapped phase is represented in degrees. |
| GroupDelay | 7 | The group delay of wave is reported in seconds. Group delay represents the time it takes for the signal to pass through a device under test. Group delay vs. frequency is derived from phase vs. frequency response. At a given frequency point, group delay is computed by selecting two nearby frequency points and taking the ratio of the phase difference to the frequency separation between them. The frequency separation between the two selected points is called the group delay aperture. The aperture can be controlled by first configuring WavesGroupDelayApertureMode method and once the mode is selected, you can set the aperture by configuring WavesGroupDelayAperturePoints or WavesGroupDelayAperturePercentage or WavesGroupDelayApertureFrequencySpan. For example, if the number of aperture points is equal to 3, then group delay at a nth frequency point is computed by selecting the (n-1)th frequency point and (n+1)th frequency point. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesmagnitudeunits.html language=enus -->
## TOPIC 00418: RFmxVnaMXWavesMagnitudeUnits Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesmagnitudeunits.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesmagnitudeunits.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the magnitude units for all waves for which WavesFormat method is set to Magnitude. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic enum RFmxVnaMXWavesMagnitudeUnitsMembersNameValueDescriptiondBm0Wave magnitude is reported in dBm. dBmV1Wave magnitude is reported in dBmV. dBuV2Wave ma

### RFmxVnaMXWavesMagnitudeUnits Enumeration

Specifies the magnitude units for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [Magnitude](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXWavesMagnitudeUnits

#### Members

| Name | Value | Description |
| --- | --- | --- |
| dBm | 0 | Wave magnitude is reported in dBm. |
| dBmV | 1 | Wave magnitude is reported in dBmV. |
| dBuV | 2 | Wave magnitude is reported in dBuV. |
| dBmA | 3 | Wave magnitude is reported in dBmA. |
| W | 4 | Wave magnitude is reported in watts. |
| V | 5 | Wave magnitude is reported in volts. |
| A | 6 | Wave magnitude is reported in ampere. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesphasetracetype.html language=enus -->
## TOPIC 00419: RFmxVnaMXWavesPhaseTraceType Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesphasetracetype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesphasetracetype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. SyntaxNamespace: NationalInstruments.RFmx

### RFmxVnaMXWavesPhaseTraceType Enumeration

Specifies the phase type for all waves for which [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [Phase](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html). Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXWavesPhaseTraceType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Wrapped | 0 | The reported wave phase is wrapped between -180 degress to +180 degrees. |
| Unwrapped | 1 | The reported wave phase is unwrapped. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesreceiver.html language=enus -->
## TOPIC 00420: RFmxVnaMXWavesReceiver Enumeration

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesreceiver.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesreceiver.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves

### RFmxVnaMXWavesReceiver Enumeration

Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to *Test (0)*, [WavesReceiverPort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port2" and [WavesSourcePort](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) to "port1".

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public enum RFmxVnaMXWavesReceiver

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Test | 0 | Measures the wave on the test receiver. |
| Reference | 1 | Measures the wave on the test receiver. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchcomplexdata__string-double-ref.html language=enus -->
## TOPIC 00421: FetchComplexData(string, double, ref ComplexSingle[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchcomplexdata__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchcomplexdata__string-double-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the Wave data for the Waves whose WavesFormat is Complex. Use "wave(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int FetchComplexData(string selectorString, double timeout, ref ComplexSingle[] complexData)ParametersNameType

### FetchComplexData(string, double, ref ComplexSingle[])

Fetches the Wave data for the Waves whose [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is [Complex](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html). 
 Use "wave(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchComplexData(string selectorString, double timeout, ref ComplexSingle[] complexData)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and wave number. If you do not specify the result name, the default result instance is used. "wave0" "result::r1/wave0" You can use the BuildWaveString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the method waits until the measurement is complete. |
| complexData | ref ComplexSingle[] | Upon return, contains the measured wave complex array corresponding to the FrequencyList. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchrealdata__string-double-ref.html language=enus -->
## TOPIC 00422: FetchRealData(string, double, ref float[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchrealdata__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchrealdata__string-double-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the wave data for the waves whose WavesFormat is Magnitude or Phase. Use "wave(n)" as the selector string to read results from this method.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int FetchRealData(string selectorString, double timeout, ref float[] realData)ParametersNameTypeDes

### FetchRealData(string, double, ref float[])

Fetches the wave data for the waves whose [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is [Magnitude](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html) or [Phase](nationalinstruments-rfmx-vnamx-rfmxvnamxwavesformat.html). 
 Use "wave(n)" as the selector string to read results from this method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchRealData(string selectorString, double timeout, ref float[] realData)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and wave number. If you do not specify the result name, the default result instance is used. "wave0" "result::r1/wave0" You can use the BuildWaveString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the method waits until the measurement is complete. |
| realData | ref float[] | Upon return, contains the measured wave real array corresponding to the FrequencyList. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchxdata__string-double-ref.html language=enus -->
## TOPIC 00423: FetchXData(string, double, ref double[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchxdata__string-double-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchxdata__string-double-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of frequency values when you perform wave measurement with SweepType method set to List or Linear or Segment. It fetches an array of time values when you perform wave measurement with SweepType method set to CWTime.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int FetchXData

### FetchXData(string, double, ref double[])

Fetches an array of frequency values when you perform wave measurement with [SweepType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method set to [List](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html) or [Linear](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html) or [Segment](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html). It fetches an array of time values when you perform wave measurement with [SweepType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method set to [CWTime](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchXData(string selectorString, double timeout, ref double[] x)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the method waits until the measurement is complete. |
| x | ref double[] | Upon return, contains the frequencies at which measurements have been made for all the supported values of SweepType. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchydata__string-double-ref-ref.html language=enus -->
## TOPIC 00424: FetchYData(string, double, ref float[], ref float[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchydata__string-double-ref-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-fetchydata__string-double-ref-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the wave data for all WavesFormat types. Use "wave(n)" as the selector string to read results from this method. For different WavesFormat, the data is returned as follows:SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int FetchYData(string selectorString, double timeout, ref float[] y

### FetchYData(string, double, ref float[], ref float[])

Fetches the wave data for all [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) types. 
 Use "wave(n)" as the selector string to read results from this method. 
 For different [WavesFormat](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html), the data is returned as follows:

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int FetchYData(string selectorString, double timeout, ref float[] y1, ref float[] y2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name, and S-Parameter number. If you do not specify the result name, the default result instance is used. Example: "sparam0" "result::r1/sparam0" You can use the BuildSParameterString(string, int) method to build the selector string. |
| timeout | double | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the method waits until the measurement is complete. |
| y1 | ref float[] | Upon return, contains the measured wave real data array corresponding to the FrequencyList. |
| y2 | ref float[] | Upon return, contains the measured wave real data array corresponding to the FrequencyList. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectioneffectivelevel__string-out.html language=enus -->
## TOPIC 00425: GetCorrectionEffectiveLevel(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectioneffectivelevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectioneffectivelevel__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionEffectiveLevel(string selectorString, out string value)

### GetCorrectionEffectiveLevel(string, out string)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionEffectiveLevel(string selectorString, out string value)

Parent topic:

RFmxVnaMXWavesResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectionlevel__string-out.html language=enus -->
## TOPIC 00426: GetCorrectionLevel(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectionlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectionlevel__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the error correction level of the VNA Waves measurement.Use 'wave(n)' as the selector string to read this attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionLevel(string selectorString, out string value)RemarksThis method gets the value of WavesResultsCorrectionLe

### GetCorrectionLevel(string, out string)

Gets the error correction level of the VNA Waves measurement.Use 'wave(n)' as the selector string to read this attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionLevel(string selectorString, out string value)

#### Remarks

WavesResultsCorrectionLevel

| Correction Level | Description |
| --- | --- |
| Uncorrected | Correction is not applied to the configured wave. |
| Wave | 1-Port correction is applied to the configured Wave. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the correction level of the VNA Waves measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectionstate__string-out.html language=enus -->
## TOPIC 00427: GetCorrectionState(string, out RFmxVnaMXWavesCorrectionState)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectionstate__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults-getcorrectionstate__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the error correction state of the VNA Waves measurement.Use 'wave(n)' as the selector string to read this attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionState(string selectorString, out RFmxVnaMXWavesCorrectionState value)RemarksThis method gets the value of W

### GetCorrectionState(string, out RFmxVnaMXWavesCorrectionState)

Gets the error correction state of the VNA Waves measurement.Use 'wave(n)' as the selector string to read this attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionState(string selectorString, out RFmxVnaMXWavesCorrectionState value)

#### Remarks

This method gets the value of [WavesResultsCorrectionState](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXWavesCorrectionState | Upon return, contains the error correction state of the VNA Waves measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMXWavesResults Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults.html language=enus -->
## TOPIC 00428: RFmxVnaMXWavesResults Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamxwavesresults.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to fetch and read the Waves measurement results. Derives fromRFmxVnaMXSubObjectSyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic class RFmxVnaMXWavesResults : RFmxVnaMXSubObjectMethodsNameDescriptionFetchComplexData(string, double, ref ComplexSingle[])Fetches the Wave data for t

### RFmxVnaMXWavesResults Class

Provides methods to fetch and read the Waves measurement results.

#### Derives from

- RFmxVnaMXSubObject

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public class RFmxVnaMXWavesResults : RFmxVnaMXSubObject

#### Methods

| Name | Description |
| --- | --- |
| FetchComplexData(string, double, ref ComplexSingle[]) | Fetches the Wave data for the Waves whose WavesFormat is Complex. Use "wave(n)" as the selector string to read results from this method. |
| FetchRealData(string, double, ref float[]) | Fetches the wave data for the waves whose WavesFormat is Magnitude or Phase. Use "wave(n)" as the selector string to read results from this method. |
| FetchXData(string, double, ref double[]) | Fetches an array of frequency values when you perform wave measurement with SweepType method set to List or Linear or Segment. It fetches an array of time values when you perform wave measurement with SweepType method set to CWTime. |
| FetchYData(string, double, ref float[], ref float[]) | Fetches the wave data for all WavesFormat types. Use "wave(n)" as the selector string to read results from this method. For different WavesFormat, the data is returned as follows: |
| GetCorrectionEffectiveLevel(string, out string) |  |
| GetCorrectionLevel(string, out string) | Gets the error correction level of the VNA Waves measurement.Use 'wave(n)' as the selector string to read this attribute. |
| GetCorrectionState(string, out RFmxVnaMXWavesCorrectionState) | Gets the error correction state of the VNA Waves measurement.Use 'wave(n)' as the selector string to read this attribute. |

Parent topic:

NationalInstruments.RFmx.VnaMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx.html language=enus -->
## TOPIC 00429: NationalInstruments.RFmx.VnaMX

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxVnaMXDefines a root class which is used to identify and control Vna signal configuration. RFmxVnaMXConstantsSpecifies constants for I/O terminals. RFmxVnaMXMarkerRepresents the Marker measurement. RFmxVnaMXMarkerConfigurationProvides methods to configure the Marker measurem

### NationalInstruments.RFmx.VnaMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxVnaMX | Defines a root class which is used to identify and control Vna signal configuration. |
| RFmxVnaMXConstants | Specifies constants for I/O terminals. |
| RFmxVnaMXMarker | Represents the Marker measurement. |
| RFmxVnaMXMarkerConfiguration | Provides methods to configure the Marker measurement. |
| RFmxVnaMXMarkerResults | Provides methods to fetch and read the Marker measurement results. |
| RFmxVnaMXSParams | Represents the SParams measurement. |
| RFmxVnaMXSParamsConfiguration | Provides methods to configure the SParams measurement. |
| RFmxVnaMXSParamsResults | Provides methods to fetch and read the SParams measurement results. |
| RFmxVnaMXSubObject | Represents members that are common to all sub-object of RFmxVnaMX classes. |
| RFmxVnaMXWaves | Represents the Waves measurement. |
| RFmxVnaMXWavesConfiguration | Provides methods to configure the Waves measurement. |
| RFmxVnaMXWavesResults | Provides methods to fetch and read the Waves measurement results. |

#### Interfaces

None

#### Structures

None

#### Enumerations

| Name | Description |
| --- | --- |
| RFmxVnaMXAutoIFBandwidthScalingEnabled | Specifies whether IF Bandwidth is scaled down at low frequencies. |
| RFmxVnaMXAveragingEnabled | Specifies whether to enable averaging for the VNA measurement. |
| RFmxVnaMXCalErrorTerm | specifies the type of error term in the calset. |
| RFmxVnaMXCalFrequencyGrid | specifies the type of error term in the calset. |
| RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability | specifies the S-Parameter availability. |
| RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType | specifies the model type of of the 1-port reflect standard. |
| RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability | Specifies the S-Parameter availability. |
| RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition | specifies the S-Parameter definition of the Calibration Element. |
| RFmxVnaMXCalkitManagerCalkitCalibrationElementType | specifies the type(s) of the Calibration Element. |
| RFmxVnaMXCalkitManagerCalkitConnectorGender | specifies the Gender of a Connector of a specific Calkit. |
| RFmxVnaMXCalkitManagerCalkitTrlReferencePlane | Specifies the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration. |
| RFmxVnaMXCorrectionCalibrationCalkitType | Specifies the type of calkit used for calibration. |
| RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation |  |
| RFmxVnaMXCorrectionCalibrationMethod | Specifies the calibration method. |
| RFmxVnaMXCorrectionCalibrationThruMethod | Specifies the Thru calibration method when Calibration Method method is set to SOLT. |
| RFmxVnaMXCorrectionEnabled | Specifies whether to enable error correction for VNA measurement. |
| RFmxVnaMXCorrectionInterpolationEnabled | Specifies whether to enable interpolation of error terms for corrected VNA measurement. This method is used only when you set the CorrectionEnabled method to True. |
| RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode | Specifies the frequency mode over which the delay and loss (optional) values are determined. The default is Sweep. |
| RFmxVnaMXCorrectionPortExtensionAutoLossEnabled | Specifies whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. |
| RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled | Specifies whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled) method to True. |
| RFmxVnaMXCorrectionPortExtensionAutoStandard | Specifies the measured standard as part of automatic port extension. |
| RFmxVnaMXCorrectionPortExtensionDCLossEnabled | Specifies whether to compensate for the frequency independent loss when Port Extension Enabled is set to True. |
| RFmxVnaMXCorrectionPortExtensionDelayDomain | Specifies the delay domain of the port extension when Port Extension Enabled is set to True. |
| RFmxVnaMXCorrectionPortExtensionDistanceUnit | Specifies the unit of the port extension delay in physical length (distance) when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. |
| RFmxVnaMXCorrectionPortExtensionEnabled | Specifies whether to enable port extension for the VNA port. |
| RFmxVnaMXCorrectionPortExtensionLoss1Enabled | Specifies whether to compensate for the frequency dependent loss, Loss1, as part of port extention. This method is used only when you set the CorrectionPortExtensionEnabled method to True. |
| RFmxVnaMXCorrectionPortExtensionLoss2Enabled | Specifies whether to compensate for the frequency dependent loss, Loss2, as part of port extention. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. |
| RFmxVnaMXCorrectionPortSubsetEnabled | Specifies whether to enable correction for a subset of set of ports for which calibration data is avaialble. |
| RFmxVnaMXCorrectionSwitchPortsMultipathCalibration |  |
| RFmxVnaMXDigitalEdgeTriggerEdge | Specifies the active edge for the trigger. This method is used only when you set the TriggerType method to DigitalEdge. |
| RFmxVnaMXIndexEventLevel | Specifies the trigger level for the Index event. This event indicates the analyzer has completed all the acquisitions for the signal. |
| RFmxVnaMXLimitedConfigurationChange | Specifies the set of properties that are considered by NI-RFmx in the locked signal configuration state. |
| RFmxVnaMXMarkerMode | specifies the mode for placing the marker. |
| RFmxVnaMXMarkerPeakSearchExcursionEnabled | specifies the threshold value that a valid peak must exceed when you use Marker Search method to find peaks. The threshold is expressed in the same units as the source data. |
| RFmxVnaMXMarkerPeakSearchThresholdEnabled | specifies whether Marker Search method finds a peak above specified Threshold or finds a peak without considering any Threshold constraint. |
| RFmxVnaMXMarkerSearchMode | Specifies the search-target. If search is successful, RFmx updates the marker X and Y values to the location at which search-target is found. |
| RFmxVnaMXMarkerType | Specifies whether the marker is disabled (Off) or is enabled (On) as a normal marker, delta marker or a fixed marker. The default value is Off. |
| RFmxVnaMXMeasurementTypes | Specifies the type of measurement. |
| RFmxVnaMXPropertyId | Specifies all the attribute identifiers. |
| RFmxVnaMXPulseAcquisitionAuto | Specifies whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. |
| RFmxVnaMXPulseGeneratorEnabled | Specifies whether to enable a pulse generator. |
| RFmxVnaMXPulseModeEnabled | Specifies whether to enable pulse mode for VNA measurement. |
| RFmxVnaMXPulseTriggerType | Specifies the pulse trigger type. |
| RFmxVnaMXReadyForTriggerEventLevel | Specifies the trigger level for the Ready For Trigger event.This event indicates to an external device responsible for sending triggers that the VNA is ready to receive the trigger. |
| RFmxVnaMXRestoreConfiguration | specifies whether the stimulus settings from the specified calset should be applied to the signal. |
| RFmxVnaMXSParameterOrientation | specifies the orientation of the configured fixture network with respect to VNA port. |
| RFmxVnaMXSParamsCorrectionState | Returns the error correction state of the VNA S-Parameter measurement. |
| RFmxVnaMXSParamsFormat | Specifies the format of S-Parameter measurement. |
| RFmxVnaMXSParamsGroupDelayApertureMode | Specifies the aperture mode to be used for the computation of group delay for all S-Parameters for which SParamsFormat method is set to Group Delay. |
| RFmxVnaMXSParamsMagnitudeUnits | Specifies the magnitude units for all S-Parameters for which you set SParamsFormat method to Magnitude. |
| RFmxVnaMXSParamsMathFunction | Specifies the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted. |
| RFmxVnaMXSParamsPhaseTraceType | Specifies the phase type for all S-Parameters for which SParamsFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |
| RFmxVnaMXSParamsSnPDataFormat | Specifies the SParams Data Format of the S-parameter measurement to be saved. |
| RFmxVnaMXSegmentDwellTimeEnabled | Specifies whether to enable individual Dwell Time value configured for each segment by Segment Dwell Time (s) method. If this is set to False, a common value will be used across all segments specified by Dwell Time (s) method. |
| RFmxVnaMXSegmentEnabled | Specifies whether to enable the selected segment for the sweep. |
| RFmxVnaMXSegmentIFBandwidthEnabled | Specifies whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. |
| RFmxVnaMXSegmentPowerLevelEnabled | Specifies whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. |
| RFmxVnaMXSegmentTestReceiverAttenuationEnabled | Specifies whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. |
| RFmxVnaMXSourcePowerMode | Specifies whether to make VNA measurements with source turned off. |
| RFmxVnaMXSweepSequence | Specifies the sequence of acquisitions for various frequency points and source ports. |
| RFmxVnaMXSweepType | Specifies the sweep type for the measurement. |
| RFmxVnaMXTriggerMode | Specifies the trigger mode. |
| RFmxVnaMXTriggerType | Specifies the trigger type. |
| RFmxVnaMXWavesCorrectionState | Returns the error correction state of the VNA Waves measurement. |
| RFmxVnaMXWavesFormat | Specifies the format for wave measurement. |
| RFmxVnaMXWavesGroupDelayApertureMode | Specifies the aperture mode to be used for the computation of group delay for all waves for which WavesFormat method is set to Group Delay. |
| RFmxVnaMXWavesMagnitudeUnits | Specifies the magnitude units for all waves for which WavesFormat method is set to Magnitude. |
| RFmxVnaMXWavesPhaseTraceType | Specifies the phase type for all waves for which WavesFormat method is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. |
| RFmxVnaMXWavesReceiver | Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_(receiver port name)_(source port name)" and "b_(receiver port name)_(source port name)" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure "b21", set this method to Test (0), WavesReceiverPort to "port2" and WavesSourcePort to "port1". |

#### Delegates

None
