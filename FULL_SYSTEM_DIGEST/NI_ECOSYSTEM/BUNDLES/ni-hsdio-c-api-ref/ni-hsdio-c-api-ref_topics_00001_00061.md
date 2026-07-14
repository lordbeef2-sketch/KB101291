# NI DOCUMENT BUNDLE: ni-hsdio-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-hsdio-c-api-ref start=1 end=61 -->
<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_abort.html language=enus -->
## TOPIC 00001: niHSDIO_Abort

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_abort.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_Abort

ViStatus = niHSDIO_Abort (
 ViSession vi);

#### Purpose

Stops a running dynamic session. This function is generally not required on finite data operations, as these operations complete after the last data point is generated or acquired. This function is generally required for continuous operations or if you wish to interrupt a finite operation before it is completed.

This function is valid only for dynamic operations (acquisition or generation). It is not valid for static operations.

|  | Note To avoid receiving hardware clocking errors when reconfiguring an external clock, explicitly call the niHSDIO_Abort function after your finite operation has completed before performing any clocking reconfiguration. An external clock that stops sending pulses to the device (even after a finite operation has completed) may cause NI-HSDIO to return an error, stating that the clock became unlocked, if the device has not aborted yet. |
| --- | --- |

#### Related topics:

- Initialize Your Session

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_adjustsampleclockrelativedelay.html language=enus -->
## TOPIC 00002: niHSDIO_AdjustSampleClockRelativeDelay

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_adjustsampleclockrelativedelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_adjustsampleclockrelativedelay.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_AdjustSampleClockRelativeDelay

ViStatus = niHSDIO_AdjustSampleClockRelativeDelay (
 ViSession vi, 
 ViReal64 adjustmentTime);

#### Purpose

Delays the Sample clock relative to the Reference clock. Use this function to align the Sample clock of your device to the Sample clock of another device in your system.

Only call this function after your session is committed. The effect of this function is immediate.

This function generates an error if the [NIHSDIO_ATTR_REF_CLOCK_SOURCE](/csh?topicname=hsdiocref/nihsdio_attr_ref_clock_source.html) attribute is set to NIHSDIO_VAL_NONE_STR.

This function can only align the device Sample clock to another Sample clock if the other device uses the same Reference clock source.

#### Related topics:

- Clocks
- Data and Clock Position

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Adjustment Time | ViReal64 | Specifies the time in seconds to delay the Sample clock. Values range between 0 and the Sample clock period (1/NIHSDIO_ATTR_SAMPLE_CLOCK_RATE). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_assigndynamicchannels.html language=enus -->
## TOPIC 00003: niHSDIO_AssignDynamicChannels

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_assigndynamicchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_assigndynamicchannels.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_AssignDynamicChannels

ViStatus = niHSDIO_AssignDynamicChannels (
 ViSession vi, 
 ViConstString channelList);

#### Purpose

Configures channels for dynamic acquisition (if **vi** is an acquisition session) or dynamic generation (if **vi** is a generation session).

|  | Note A channel cannot be assigned to static generation and dynamic generation at the same time. |
| --- | --- |

#### Related topics:

- Dynamic Acquisition
- Dynamic Generation

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Channel List | ViConstString | Identifies which channels are reserved for dynamic operation. Valid Syntax 0-19 or 0-15,16-19 or 0-18,19"" (empty string) or VI_NULL to specify all channels"none" to unassign all channels Channels cannot be configured for both static generation and dynamic generation. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_configureidlestateu32.html language=enus -->
## TOPIC 00004: niHSDIO_ConfigureIdleStateU32

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_configureidlestateu32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_configureidlestateu32.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_ConfigureIdleStateU32

ViStatus = niHSDIO_ConfigureIdleStateU32 (
 ViSession vi, 
 ViUInt32 idleState);

#### Purpose

Sets the [Idle state](/csh?topicname=/) for a dynamic generation operation. The idle state may be active in a variety of conditions:

- The generation operation completes normally.
- The generation operation pauses from an active Pause trigger.
- The generation operation terminates due to an underflow error.

Unlike the [niHSDIO_ConfigureIdleState](/csh?topicname=hsdiocref/cvinihsdio_configureidlestate.html) function which uses a string, this function uses a binary format to only represent high and low. If you require more choices for your Idle state, use the [niHSDIO_ConfigureIdleState](/csh?topicname=hsdiocref/cvinihsdio_configureidlestate.html) function.

#### Related topics:

- Initial and Idle States
- Configuring Initial and Idle States

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Idle State | ViInt32 | Specifies the bit mask representing the Idle state. High is specified with a 1, and low is specified with a 0. If you need to specify values other than high or low, use the niHSDIO_ConfigureIdleState function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_configureinitialstate.html language=enus -->
## TOPIC 00005: niHSDIO_ConfigureInitialState

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_configureinitialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_configureinitialstate.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_ConfigureInitialState

ViStatus = niHSDIO_ConfigureInitialState (
 ViSession vi, 
 ViConstString channelList, 
 ViConstString initialState);

#### Purpose

Sets the [Initial state](/csh?topicname=/) for a dynamic generation operation. The Initial state of each channel is driven after the session is initiated using the [niHSDIO_Initiate](/csh?topicname=hsdiocref/cvinihsdio_initiate.html) function. 
Channels remain unchanged until the Start trigger generates the first waveform sample.

**Valid Syntax:** 
 
Both of these examples are valid and do the same thing. The 
order of **channelList** determines the order of the pattern 
string.

- niHSDIO_ConfigureInitialState (vi, "19-0", "0000 0XXX XX11 111Z ZZZZ");
- niHSDIO_ConfigureInitialState (vi, "0-19", "ZZZZ Z111 11XX XXX0 0000");

#### Related topics:

- Initial and Idle States
- Configuring Initial and Idle States

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Channel List | ViConstString | Specifies which channels have their initial value set using the initialState string. The order of channels in channelList determines the order of the initialState string. |
| Initial State | ViConstString | Describes the Initial state of a dynamic generation operation. This expression is composed of characters: 'X' or 'x': keeps the previous value '1': sets the channel to logic high '0': sets the channel to logic low 'Z' or 'z': disables the channel or sets it to high-impedance Note NI 656x devices do not support the high-impedance (Z) Initial state. The first character in the expression corresponds to the first channel in channelList. The number of characters in pattern must equal the number of channels specified in channelList or an error is returned. The default state of a channel is to keep the previous value. |
|  | Note NI 656x devices do not support the high-impedance (Z) Initial state. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_configurepatternmatchadvancetriggeru32.html language=enus -->
## TOPIC 00006: niHSDIO_ConfigurePatternMatchAdvanceTriggerU32

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_configurepatternmatchadvancetriggeru32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_configurepatternmatchadvancetriggeru32.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_ConfigurePatternMatchAdvanceTriggerU32

ViStatus = niHSDIO_ConfigurePatternMatchAdvanceTriggerU32 (
 ViSession vi, 
 ViConstString channelList,
 ViUInt32 pattern,
 ViInt32 triggerWhen);

#### Purpose

Configures the [Advance trigger](/csh?topicname=/) for pattern-match triggering.

Unlike the [niHSDIO_ConfigurePatternMatchAdvanceTrigger](/csh?topicname=hsdiocref/cvinihsdio_configurepatternmatchadvancetrigger.html) function, which uses a string, this function uses a binary format to only represent high and low. If you require more choices for your pattern, use the [niHSDIO_ConfigurePatternMatchAdvanceTrigger](/csh?topicname=hsdiocref/cvinihsdio_configurepatternmatchadvancetrigger.html) function.

This function is valid only for acquisition operations.

#### Related topics:

- Triggers Summary
- Pattern-Match Trigger
- Making Multirecord Acquisitions

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Channel List | ViConstString | This string specifies which channels are configured for pattern matching using the pattern value. |
| Pattern | ViUInt32 | Specifies the binary pattern that activates the pattern match trigger under the conditions specified in triggerWhen. Bits on channels not specified in channelList are ignored. |
| Trigger When | ViInt32 | Specifies when the trigger asserts. Defined Values NIHSDIO_VAL_PATTERN_MATCHES (36)—The trigger asserts when the pattern matches. NIHSDIO_VAL_PATTERN_DOES_NOT_MATCH (37)—The trigger asserts when the pattern does not match. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_configurepatternmatchpausetrigger.html language=enus -->
## TOPIC 00007: niHSDIO_ConfigurePatternMatchPauseTrigger

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_configurepatternmatchpausetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_configurepatternmatchpausetrigger.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_ConfigurePatternMatchPauseTrigger

ViStatus = niHSDIO_ConfigurePatternMatchPauseTrigger (
 ViSession vi, 
 ViConstString channelList,
 ViConstString pattern,
 ViInt32 triggerWhen);

#### Purpose

Configures the [Pause trigger](/csh?topicname=/) for 
pattern-match triggering. This function is valid only for acquisition sessions.

**Valid Syntax:** 
 
Both of the following examples are valid and do the same thing. 
The order of **channelList** determines the order of the 
pattern string.

- niHSDIO_ConfigurePatternMatchPauseTrigger (vi, "19-0", "0000 0XXX XX11 1111 1111");
- niHSDIO_ConfigurePatternMatchPauseTrigger (vi, "0-19", "1111 1111 11XX XXX0 0000");

|  | Note The values seen by pattern matching are affected by data interpretation. |
| --- | --- |

#### Related topics:

- Triggers Summary
- Pattern-Match Trigger

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Channel List | ViConstString | This string specifies which channels are configured for pattern matching using the pattern string. The order of channels in the list determines the order of the pattern string. |
| Pattern | ViConstString | This string expression describes the pattern to be matched. This expression is composed of the following characters: X or x: Ignore the channel 1: Match on a logic 1 0: Match on a logic 0 R or r: Match on a rising edge F or f: Match on a falling edge E or e: Match on either edge The first character in the expression corresponds to the first channel in channelList. The number of characters in pattern must correspond to the number of channels specified in channelList. |
| Trigger When | ViInt32 | Specifies when the trigger asserts. Defined Values NIHSDIO_VAL_PATTERN_MATCHES (36)—The trigger asserts when the pattern matches. NIHSDIO_VAL_PATTERN_DOES_NOT_MATCH (37)—The trigger asserts when the pattern does not match. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_configurepatternmatchpausetriggeru32.html language=enus -->
## TOPIC 00008: niHSDIO_ConfigurePatternMatchPauseTriggerU32

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_configurepatternmatchpausetriggeru32.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_configurepatternmatchpausetriggeru32.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_ConfigurePatternMatchPauseTriggerU32

ViStatus = niHSDIO_ConfigurePatternMatchPauseTriggerU32 (
 ViSession vi, 
 ViConstString channelList,
 ViUInt32 pattern,
 ViInt32 triggerWhen);

#### Purpose

Configures the [Pause trigger](/csh?topicname=/) for 
pattern-match triggering.

Unlike the [niHSDIO_ConfigurePatternMatchPauseTrigger](/csh?topicname=hsdiocref/cvinihsdio_configurepatternmatchpausetrigger.html) function, which uses a string, this function uses a binary format to only represent high and low. If you require more choices for your pattern, use the [niHSDIO_ConfigurePatternMatchPauseTrigger](/csh?topicname=hsdiocref/cvinihsdio_configurepatternmatchpausetrigger.html) function.

This function is valid only for acquisition sessions.

|  | Note The values seen by pattern matching are affected by data interpretation. |
| --- | --- |

#### Related topics:

- Triggers Summary
- Pattern-Match Trigger

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Channel List | ViConstString | This string specifies which channels are configured for pattern matching using the pattern value. |
| Pattern | ViUInt32 | Specifies the binary pattern that activates the pattern match trigger under the conditions specified in triggerWhen. Bits on channels not specified in channelList are ignored. |
| Trigger When | ViInt32 | Specifies when the trigger asserts. Defined Values NIHSDIO_VAL_PATTERN_MATCHES (36)—The trigger asserts when the pattern matches. NIHSDIO_VAL_PATTERN_DOES_NOT_MATCH (37)—The trigger asserts when the pattern does not match. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_stpmu_disablepmu.html language=enus -->
## TOPIC 00009: niHSDIO_STPMU_DisablePMU

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_stpmu_disablepmu.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_stpmu_disablepmu.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_STPMU_DisablePMU

ViStatus = niHSDIO_STPMU_DisablePMU (
 ViSession vi,
 ViConstString channelList,
 ViInt32 returnState);

#### Purpose

Disables the PMU source operations on the channels specified in the **channelList** parameter. Use the **returnState** parameter to tristate or return each channel to its previous digital [state](/csh?topicname=hsdio/ppmu_state_diagram_6556.html).

|  | Note When you use the PMU functions to source a voltage or current on your system, the voltage or current continues to be sourced on the selected channels until you reset your device or call this function. The niHSDIO_Abort and niHSDIO_close functions do not stop sourcing the voltage or current. |
| --- | --- |

|  | Note After using this function to disable the PMU source operations, you can still utilize the PMU measure voltage operations. |
| --- | --- |

|  | Note Only NI 6555/6556 devices support this function. |
| --- | --- |

#### Related topics:

- DCL with PPMU and Deskew

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| channelList | ViConstString | Specifies the channels being configured. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). Use PFI1 or PFI2 to specify a valid PFI channel. Use DDC_CLKOUT or STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error. |
| returnState | ViInt32 | Selects, after disabling the PPMU functionality, whether to tristate the channel or to return it to its previous digital state. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_stpmu_sourcecurrent.html language=enus -->
## TOPIC 00010: niHSDIO_STPMU_SourceCurrent

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_stpmu_sourcecurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_stpmu_sourcecurrent.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_STPMU_SourceCurrent

ViStatus = niHSDIO_STPMU_SourceCurrent (
 ViSession vi,
 ViConstString channelList,
 ViReal64 currentLevel,
 ViReal64 currentLevelRange,
 ViReal64 lowerVoltageLimit,
 ViReal64 upperVoltageLimit);

#### Purpose

Enables the PMU capabilities on the channels specified in the **channelList** parameter and sources the current specified in the **currentLevel** parameter while maintaining the voltage within the specified limits.

|  | Note Only NI 6555/6556 devices support this function. |
| --- | --- |

#### Related topics:

- DCL with PPMU and Deskew
- Force Current
- Force Current Voltage Clamps

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| channelList | ViConstString | Specifies the channels being configured. Specify multiple channels by using a channel list or a channel range. A channel list is a comma (,) separated sequence of channel names (for example, 0,2 specifies channels 0 and 2). A channel range is a lower bound channel followed by a hyphen (-) or colon (:) followed by an upper bound channel (for example, 0-2 specifies channels 0, 1, and 2). Use PFI1 or PFI2 to specify a valid PFI channel. Use DDC_CLKOUT or STROBE to specify a valid clocking terminal. If you configure multiple channels with this parameter, all those channels have the same settings. Selecting no channels for this parameter returns an error. |
| currentLevel | ViReal64 | Specifies the current level, in amps (A), to source on the specified channel(s). |
| currentLevelRange | ViReal64 | Specifies the current range, in amps (A), that is used in the ensuing current measurement on the specified channel(s). Tightening your current range increases your accuracy. The NI 6555/6556 supports the following eight current range options: 32 mA, 8 mA, 2 mA, 512 μA, 128 μA, 32 μA, 8 μA, or 2 μA. If you choose a range other than one of these options, NI-HSDIO coerces the value up to the nearest range. The default value for this parameter is 0. NI-HSDIO returns an error if you choose a value for this paramter greater than 32 mA or less than or equal to 0. |
| lowerVoltageLimit | ViReal64 | Specifies the minimum voltage limit, in volts (V), on the specified channel(s). |
| upperVoltageLimit | ViReal64 | Specifies the maximum voltage limit, in volts (V), on the specified channel(s). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_unlocksession.html language=enus -->
## TOPIC 00011: niHSDIO_UnlockSession

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_unlocksession.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_unlocksession.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_UnlockSession

ViStatus = niHSDIO_UnlockSession (
 ViSession vi, 
 ViBoolean *callerHasLock);

#### Purpose

This function releases a lock that you acquired on an instrument session using the [niHSDIO_LockSession](/csh?topicname=hsdiocref/cvinihsdio_locksession.html) function.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Output |  |  |
| Name | Type | Description |
| Caller Has Lock | ViBoolean | This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL. You can use this parameter in complex functions to track lock status and the need to unlock the session. Pass the address of a local ViBoolean variable in the declaration of the local variable and initialize it to VI_FALSE. Also, pass the address of the same local variable to any other calls you make to niHSDIO_LockSession or niHSDIO_UnlockSession in the same function. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_waituntildone.html language=enus -->
## TOPIC 00012: niHSDIO_WaitUntilDone

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_waituntildone.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_waituntildone.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_WaitUntilDone

ViStatus = niHSDIO_WaitUntilDone (
 ViSession vi, 
 ViInt32 maxTime);

#### Purpose

Pauses execution of your program until the dynamic data operation is completed or the function returns a timeout error. This function periodically checks the operation status and returns control to the calling program if the operation completes successfully or an error occurs (including a timeout error).

This function is most useful for finite data operations that you expect to complete within a certain time.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Max Time Milliseconds | ViInt32 | Specifies the number of milliseconds to allow the function to complete before returning. If the specified time elapses before the data operation has completed, the function returns a timeout error.Setting a value of 0 causes the function to return immediately. This setting can be useful to manually poll for hardware errors after a data operation has been initiated. If no other error has occurred and the data operation is still not complete, the function returns a timeout error. Setting a value of -1 causes the function to never timeout. Be careful not to use this value during a continuous operation, as it does not return unless a hardware error occurs. Perform a manual device reset from Measurement & Automation Explorer if you get stuck in this state or call the niHSDIO_reset or niHSDIO_ResetDevice functions from the other session of the device. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_writenamedwaveformfromfilehws.html language=enus -->
## TOPIC 00013: niHSDIO_WriteNamedWaveformFromFileHWS

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_writenamedwaveformfromfilehws.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_writenamedwaveformfromfilehws.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_WriteNamedWaveformFromFileHWS

ViStatus = niHSDIO_WriteNamedWaveformFromFileHWS( 
 ViSession vi,
 ViConstString waveformName,
 ViConstString filePath,
 ViBoolean useRateFromWaveform,
 ViInt32* waveformSizeInSamples);

#### Purpose

Reads and transfers data from a digital .hws file to [onboard memory](/csh?topicname=/).

If you specify a **waveformName** not already [allocated](/csh?topicname=hsdiocref/cvinihsdio_allocatenamedwaveform.html) on the device, the appropriate amount of onboard memory is allocated (if available), and the data is stored in that new location.

Data is always written to memory starting at the current write position of the waveform. A new waveform's write position is the start of the allocated memory. Calling this function moves the next write position to the end of the data just written. Thus, subsequent calls to this function append data to the end of previously written data. You can manually change the write position by calling the [niHSDIO_SetNamedWaveformNextWritePosition](/csh?topicname=hsdiocref/cvinihsdio_setnamedwaveformnextwriteposition.html) function.
If you try to write past the end of the allocated space, NI-HSDIO returns an error.

Waveforms are stored contiguously in onboard memory. You cannot 
resize an existing named waveform. Instead, delete the existing waveform using the
[niHSDIO_DeleteNamedWaveform](/csh?topicname=hsdiocref/cvinihsdio_deletenamedwaveform.html) function and then re-create it with the new size using the same name.

This function calls the [niHSDIO_CommitDynamic](/csh?topicname=hsdiocref/cvinihsdio_commitdynamic.html) function. All pending attributes are committed to hardware.

#### Related topics:

- Writing Waveforms to Your Device
- File I/O and Digital Waveform Data
- Generation Onboard Memory
- Digital Waveform Data Representation in LabVIEW

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Waveform Name | ViConstString | Specifies a string representing the name to associate with the allocated waveform memory. |
| File Path | ViConstString | Specifies the path and file name of the digital .hws file to open. The .hws extension is typically used for .hws files, although using this extension is optional. |
| Use Rate From Waveform | ViBoolean | Controls how the sample rate is computed. Setting this value to TRUE computes the generation rate from the WDT value. If the sample rate has been configured using the niHSDIO_ConfigureSampleClock function, useRateFromWaveform overrides the sample rate. |
| Output |  |  |
| Name | Type | Description |
| Waveform Size | ViInt32 | Returns the number of samples contained in the waveform. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_writenamedwaveformu16.html language=enus -->
## TOPIC 00014: niHSDIO_WriteNamedWaveformU16

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_writenamedwaveformu16.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_writenamedwaveformu16.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_WriteNamedWaveformU16

ViStatus = niHSDIO_WriteNamedWaveformU16 (
 ViSession vi, 
 ViConstString waveformName, 
 ViInt32 samplesToWrite, 
 ViUInt16 data[]);

#### Purpose

Transfers waveform data from PC memory to onboard memory. Supported devices for this function depend on the [data width](/csh?topicname=hsdiocref/nihsdio_attr_data_width.html) for your device, not on the number of assigned dynamic channels. This function may be used when the data width is 2.

If you specify a **waveformName** not already allocated on the device, the appropriate amount of onboard memory is allocated (if available) and the data is stored in that new location.

Data is always written to memory starting at the current write position of the 
waveform. A new waveform's write position is the start of the allocated memory. 
Calling this function moves the next write position to the end of the data just written. Thus, subsequent calls to this function append data to the end of previously written data. You may also manually change the write position by calling the 
[niHSDIO_SetNamedWaveformNextWritePosition](/csh?topicname=hsdiocref/cvinihsdio_setnamedwaveformnextwriteposition.html) function. 
If you try to write past the end of the allocated space, an error is returned.

Waveforms are stored contiguously in onboard memory. You cannot resize an existing 
named waveform. Instead, delete the existing waveform using the
[niHSDIO_DeleteNamedWaveform](/csh?topicname=hsdiocref/cvinihsdio_deletenamedwaveform.html) function and then re-create it with the new size using the same name.

This function calls the [niHSDIO_CommitDynamic](/csh?topicname=hsdiocref/cvinihsdio_commitdynamic.html) function. All pending attributes are committed to hardware.

When you explicitly call the [niHSDIO_AllocateNamedWaveform](/csh?topicname=hsdiocref/cvinihsdio_allocatenamedwaveform.html) function and write waveforms using multiple niHSDIO_WriteNamedWaveformU16 calls, each waveform block written must be a multiple of 32 samples for the 
NI 6541/6542/6544/6545/655*x* devices (64 samples for the NI 6547/6548 in DDR mode) or a multiple of 64 samples 
for the NI 656*x* devices (128 samples if the NI 656*x* is in DDR mode).

#### Related topics:

- Writing Waveforms to Your Device
- Generating Multiple Waveforms/Linking & Looping
- Generation Onboard Memory

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Waveform Name | ViConstString | Specifies a string representing the name to associate with the allocated waveform memory. |
| Samples To Write | ViInt32 | Specifies the number of samples in data[] to be written to onboard memory. If samples to write is less than the size of data[], only the number of samples indicated in samplesToWrite are written. |
| Data | ViUInt16[] | Specifies the waveform data.If you want to use direct DMA to write your waveform from onboard memory, pass the memory address (pointer value) of the region so that you write within the direct DMA window. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_writenamedwaveformu8.html language=enus -->
## TOPIC 00015: niHSDIO_WriteNamedWaveformU8

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_writenamedwaveformu8.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_writenamedwaveformu8.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_WriteNamedWaveformU8

ViStatus = niHSDIO_WriteNamedWaveformU8 (
 ViSession vi, 
 ViConstString waveformName, 
 ViInt32 samplesToWrite, 
 ViUInt8 data[]);

#### Purpose

Transfers waveform data from PC memory to onboard memory. Supported devices for this function depend on the [data width](/csh?topicname=hsdiocref/nihsdio_attr_data_width.html) for your device, not on the number of assigned dynamic channels. This function may be used when the data width is 1.

If you specify a **waveformName** not already allocated on the device, the appropriate amount of onboard memory is allocated (if available) and the data is stored in that new location.

Data is always written to memory starting at the current write position of the 
waveform. A new waveform's write position is the start of the allocated memory. 
Calling this function moves the next write position to the end of the data just written. Thus, subsequent calls to this function append data to the end of 
previously written data. You may also manually change the write position by calling the 
[niHSDIO_SetNamedWaveformNextWritePosition](/csh?topicname=hsdiocref/cvinihsdio_setnamedwaveformnextwriteposition.html) function. 
If you try to write past the end of the allocated space, an error is returned.

Waveforms are stored contiguously in onboard memory. You cannot resize an existing 
named waveform. Instead, delete the existing waveform using the
[niHSDIO_DeleteNamedWaveform](/csh?topicname=hsdiocref/cvinihsdio_deletenamedwaveform.html) function and then recreate it with the new size using the same name.

This function calls the [niHSDIO_CommitDynamic](/csh?topicname=hsdiocref/cvinihsdio_commitdynamic.html) function. All pending attributes are committed to hardware. 
 

When you explicitly call the [niHSDIO_AllocateNamedWaveform](/csh?topicname=hsdiocref/cvinihsdio_allocatenamedwaveform.html) function and write waveforms using multiple niHSDIO_WriteNamedWaveformU8 
calls, each waveform block written must be a multiple of 32 samples for the 
NI 6541/6542/6544/6545/655*x* devices (64 samples for the NI 6547/6548 in DDR mode) or a multiple of 64 samples 
for the NI 656*x* devices (128 samples if the NI 656*x* is in 
DDR mode).

#### Related topics:

- Writing Waveforms to Your Device
- Generating Multiple Waveforms/Linking & Looping
- Generation Onboard Memory

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Waveform Name | ViConstString | Specifies a string representing the name to associate with the allocated waveform memory. |
| Samples To Write | ViInt32 | Specifies the number of samples in data[] to be written to onboard memory. If samples to write is less than the size of data[], only the number of samples indicated in samplesToWrite are written. |
| Data | ViUInt8[] | Specifies the waveform data.If you want to use direct DMA to write your waveform from onboard memory, pass the memory address (pointer value) of the region so that you write within the direct DMA window. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_writenamedwaveformwdt.html language=enus -->
## TOPIC 00016: niHSDIO_WriteNamedWaveformWDT

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_writenamedwaveformwdt.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_writenamedwaveformwdt.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_WriteNamedWaveformWDT

ViStatus = niHSDIO_WriteNamedWaveformWDT( 
 ViSession vi, 
 ViConstString waveformName, 
 ViInt32 samplesPerChannel,
 ViInt32 dataLayout,
 ViUInt8 data[]);

#### Purpose

Transfers multistate digital waveforms from PC memory to [onboard memory](/csh?topicname=/).
Each element of **data**[] uses one byte per channel per sample. The 
supported values are defined in niHSDIO.h.

If you specify a **waveformName** not already [allocated](/csh?topicname=hsdiocref/cvinihsdio_allocatenamedwaveform.html) 
on the device, the appropriate amount of onboard memory is allocated (if available), 
and the data is stored in that new location.

Data is always written to memory starting at the current write position of the waveform. A new waveform's write position is the start of the allocated memory. Calling this function moves the next write position to the end of the data just written. Thus, subsequent calls to this function append data to the end of previously written data. You can manually change the write position by calling the [niHSDIO_SetNamedWaveformNextWritePosition](/csh?topicname=hsdiocref/cvinihsdio_setnamedwaveformnextwriteposition.html) function.
If you try to write past the end of the allocated space, NI-HSDIO returns an error.

Waveforms are stored contiguously in onboard memory. You cannot 
resize an existing named waveform. Instead, delete the existing waveform using the [niHSDIO_DeleteNamedWaveform](/csh?topicname=hsdiocref/cvinihsdio_deletenamedwaveform.html) function and then recreate it with the new size using the same name.

This function calls the [niHSDIO_CommitDynamic](/csh?topicname=hsdiocref/cvinihsdio_commitdynamic.html) function. All pending attributes are committed to hardware.

#### Related topics:

- Writing Waveforms to Your Device
- File I/O and Digital Waveform Data
- Generation Onboard Memory
- Digital Waveform Data Representation in LabVIEW

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Waveform Name | ViConstString | Specifies a string representing the name to associate with the allocated waveform memory. |
| Samples To Write | ViInt32 | Specifies the number of samples in data[] to be written to onboard memory. If samples to write is less than the size of data[], only the number of samples indicated in samplesToWrite are written. |
| Data Layout | ViInt32 | Describes the layout of the waveform contained in data[]. Defined Values NIHSDIO_VAL_GROUP_BY_SAMPLE—Specifies that consecutive samples in data[] are such that the array contains the first sample from every signal in the operation, then the second sample from every signal, up to the last sample from every signal. NIHSDIO_VAL_GROUP_BY_CHANNEL—Specifies that consecutive samples in data[] are such that the array contains all the samples from the first signal in the operation, then all the samples from the second signal, up to all samples from the last signal. |
| Data | ViUInt8[] | Specifies the digital waveform data. Each value on this array defines the state of one channel of one sample. Supported states are defined in niHSDIO.h |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/cvinihsdio_writescript.html language=enus -->
## TOPIC 00017: niHSDIO_WriteScript

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/cvinihsdio_writescript.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/cvinihsdio_writescript.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### niHSDIO_WriteScript

ViStatus = niHSDIO_WriteScript (
 ViSession vi, 
 ViConstString script);

#### Purpose

Writes a string to the onboard memory containing scripts that govern the waveform generation. If this function is called repeatedly, previously written scripts with unique names remain loaded. Previously written scripts with identical names to those being written are replaced.

If multiple scripts load when the [niHSDIO_Initiate](/csh?topicname=hsdiocref/cvinihsdio_initiate.html) function is called, then one of the scripts must be designated as the script to generate by setting the [NIHSDIO_ATTR_SCRIPT_TO_GENERATE](/csh?topicname=hsdiocref/nihsdio_attr_script_to_generate.html) attribute to the desired script name. If only one script exists in memory, then you do not need to designate the script to generate. All waveforms referenced in the scripts must be written before the script is written.

An error is returned if the script uses incorrect syntax. This function calls the [niHSDIO_CommitDynamic](/csh?topicname=hsdiocref/cvinihsdio_commitdynamic.html) function. All pending attributes are committed to hardware.

#### Related topics:

- Generation Onboard Memory

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| vi | ViSession | Identifies your instrument session. vi was obtained from the niHSDIO_InitAcquisitionSession or niHSDIO_InitGenerationSession function. |
| Script | ViConstString | Specifies a string containing a syntactically correct script. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| Status | ViStatus | Reports the status of this operation. To obtain a text description of the status code, call the niHSDIO_error_message function. To obtain additional information concerning the error condition, use the niHSDIO_GetError and niHSDIO_ClearError functions. The general meaning of the status code is as follows: Value Meaning 0 Success Positive Values Warnings Negative Values Errors |
| Value | Meaning |  |
| 0 | Success |  |
| Positive Values | Warnings |  |
| Negative Values | Errors |  |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/defaults.html language=enus -->
## TOPIC 00018: Alphabetical Attribute List and Default Values

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/defaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/defaults.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### Alphabetical Attribute List and Default Values

The following table lists the default values for each attribute you can configure for your device. 
An "N/A" in a table cell indicates that the listed attribute is not supported for that device. A dash indicates that the attribute does not have a default value or that it is a read-only attribute. "" is used in the following ways:

- In output terminal attributes to indicate to the device not to export the relevant signal
- In trigger source attributes to indicate to the device that the relevant trigger is not used
- In dynamic and static channels to mean "all channels"

| C/C++ Attribute | NI 6541/6542Default Value | NI 6544/6545 and NI 6547/6548Default Value | NI 6551/6552Default Value | NI 6555/6556Default Value | NI 656xDefault Value |
| --- | --- | --- | --- | --- | --- |
| ADVANCE TRIGGER TYPE | NONE | NONE | NONE | NONE | NONE |
| NIHSDIO_ATTR_CLOCK_VOLTAGE_HIGH_LEVEL | N/A | N/A | N/A | Acquisition = 1.7 VGeneration = 3.3 V | N/A |
| NIHSDIO_ATTR_CLOCK_VOLTAGE_LOW_LEVEL | N/A | N/A | N/A | Acquisition = 1.6 VGeneration = 0 V | N/A |
| NIHSDIO_ATTR_CLOCK_VOLTAGE_RANGE | N/A | N/A | N/A | MINUS_2_TO_6_VOLTAGE_RANGE | N/A |
| DATA_ACTIVE_EVENT_LEVEL_ACTIVE_LEVEL | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH |
| DATA_ACTIVE_EVENT_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| DATA_ACTIVE_EVENT_POSITION | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE |
| DATA_ACTIVE_EVENT_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| DATA_ACTIVE_INTERNAL_ROUTE_DELAY | N/A | N/A | 0 | 0 | N/A |
| DATA_DESKEW | N/A | N/A | N/A | 0 | N/A |
| DATA_INTERPRETATION | HIGH_OR_LOW | HIGH_OR_LOW | HIGH_OR_LOW | HIGH_OR_LOW | HIGH_OR_LOW |
| DATA_POSITION | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE |
| DATA_POSITION_DELAY | 0 % | 0 % | 0 % | 0 % | 0 % |
| DATA_RATE_MULTIPLIER | SINGLE_DATA_RATE | SINGLE_DATA_RATE | SINGLE_DATA_RATE | SINGLE_DATA_RATE | SINGLE_DATA_RATE |
| DATA_TERMINATION_MODE | N/A | N/A | N/A | HIGH_IMPEDANCE | N/A |
| DATA_TERMINATION_VOLTAGE_LEVEL | N/A | N/A | N/A | 0 | N/A |
| DATA_TRANSFER_BLOCK_SIZE | 0 | 0 | 0 | 0 | 0 |
| DATA_TRISTATE_MODE | N/A | N/A | N/A | HIGH_IMPEDANCE | N/A |
| DATA_VOLTAGE_HIGH_LEVEL | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | N/A |
| DATA_VOLTAGE_LOW_LEVEL | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | N/A |
| DATA_VOLTAGE_RANGE | N/A | N/A | N/A | MINUS_2_TO_6_VOLTAGE_RANGE | N/A |
| DATA_WIDTH | 4 | 4 | 4 | 4 | 2 |
| DEVICE_PEAK_POWER_CONSUMED | — | — | — | — | — |
| DEVICE_POWER_CONSUMPTION | — | — | — | — | — |
| DIGITAL_EDGE_ADVANCE_TRIGGER_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE |
| DIGITAL_EDGE_ADVANCE_TRIGGER_IMPEDANCE | 50000 Ω | 50000 Ω | 50000 Ω | N/A | 100 Ω |
| DIGITAL_EDGE_ADVANCE_TRIGGER_POSITION | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE |  |
| DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE | "" | "" | "" | "" | "" |
| DIGITAL_EDGE_ADVANCE_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| DIGITAL_EDGE_REF_TRIGGER_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE |
| DIGITAL_EDGE_REF_TRIGGER_IMPEDANCE | 50000 Ω | 50000 Ω | 50000 Ω | N/A | 100 Ω |
| DIGITAL_EDGE_REF_TRIGGER_POSITION | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE |
| DIGITAL_EDGE_REF_TRIGGER_SOURCE | "" | "" | "" | "" | "" |
| DIGITAL_EDGE_REF_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE |
| DIGITAL_EDGE_SCRIPT_TRIGGER_IMPEDANCE | 50000 Ω | 50000 Ω | 50000 Ω | N/A | 100 Ω |
| DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE | "" | "" | "" | "" | "" |
| DIGITAL_EDGE_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| DIGITAL_EDGE_START_TRIGGER_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE | RISING_EDGE |
| DIGITAL_EDGE_START_TRIGGER_IMPEDANCE | 50000 Ω | 50000 Ω | 50000 Ω | N/A | 100 Ω |
| DIGITAL_EDGE_START_TRIGGER_POSITION | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE |
| START_TRIGGER_SOURCE | "" | "" | "" | "" | "" |
| DIGITAL_EDGE_START_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| DIGITAL_EDGE_STOP_TRIGGER_EDGE | N/A | RISING_EDGE | N/A | RISING_EDGE | N/A |
| DIGITAL_EDGE_STOP_TRIGGER_IMPEDANCE | N/A | 50000 Ω | N/A | N/A | N/A |
| DIGITAL_EDGE_STOP_TRIGGER_SOURCE | N/A | "" | N/A | "" | N/A |
| DIGITAL_EDGE_STOP_TRIGGER_TERMINAL_CONFIGURATION | N/A | SINGLE_ENDED | N/A | SINGLE_ENDED | N/A |
| DIGITAL_LEVEL_PAUSE_TRIGGER_IMPEDANCE | 50000 Ω | 50000 Ω | 50000 Ω | N/A | 100 Ω |
| DIGITAL_LEVEL_PAUSE_TRIGGER_POSITION | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE |
| DIGITAL_LEVEL_PAUSE_TRIGGER_SOURCE | "" | "" | "" | "" | "" |
| DIGITAL_LEVEL_PAUSE_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| DIGITAL_LEVEL_PAUSE_TRIGGER_WHEN | HIGH | HIGH | HIGH | HIGH | HIGH |
| DIGITAL_LEVEL_SCRIPT_TRIGGER_IMPEDANCE | 50000 Ω | 50000 Ω | 50000 Ω | N/A | 100 Ω |
| DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE | "" | "" | "" | "" | "" |
| DIGITAL_LEVEL_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| DIGITAL_LEVEL_SCRIPT_TRIGGER_WHEN | HIGH | HIGH | HIGH | HIGH | HIGH |
| DIRECT_DMA_ENABLED | VI_FALSE | VI_FALSE | VI_FALSE | VI_FALSE | VI_FALSE |
| DIRECT_DMA_WINDOW_ADDRESS | 0 | 0 | 0 | 0 | 0 |
| DIRECT_DMA_WINDOW_SIZE | 0 | 0 | 0 | 0 | 0 |
| DYNAMIC_CHANNELS | "" | "" | "" | "" | "" |
| END_OF_RECORD_EVENT_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| END_OF_RECORD_EVENT_PULSE_POLARITY | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH |
| END_OF_RECORD_EVENT_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| EVENT_DESKEW | N/A | N/A | N/A | 0 | N/A |
| EVENT_POSITION_DELAY | N/A | N/A | N/A | 0 | N/A |
| EVENT_VOLTAGE_HIGH_LEVEL | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | N/A |
| EVENT_VOLTAGE_LOW_LEVEL | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | N/A |
| EVENT_VOLTAGE_RANGE | N/A | N/A | N/A | MINUS_2_TO_6_VOLTAGE_RANGE | N/A |
| EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| EXPORTED_ADVANCE_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| EXPORTED_ONBOARD_REF_CLOCK_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| EXPORTED_PAUSE_TRIGGER_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| EXPORTED_PAUSE_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| EXPORTED_REF_CLOCK_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| EXPORTED_REF_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| EXPORTED_SAMPLE_CLOCK_DELAY | 0 % | 0 % | 0 % | 0 % | 0 % |
| EXPORTED_SAMPLE_CLOCK_MODE | NONINVERTED | NONINVERTED | NONINVERTED | NONINVERTED | NONINVERTED |
| EXPORTED_SAMPLE_CLOCK_OFFSET | 2.5 ns | 1.65 ns | 2.5 ns | 1.65 ns | 1.6 ns |
| EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| EXPORTED_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| EXPORTED_START_TRIGGER_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| EXPORTED_START_TRIGGER_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| EXPORTED_STOP_TRIGGER_OUTPUT_TERMINAL | N/A | "" | N/A | "" | N/A |
| EXPORTED_STOP_TRIGGER_TERMINAL_CONFIGURATION | N/A | SINGLE_ENDED | N/A | SINGLE_ENDED | N/A |
| FETCH_BACKLOG | — | — | — | — | — |
| FETCH_OFFSET | 0 S | 0 S | 0 S | 0 S | 0 S |
| FETCH_RELATIVE_TO | MOST_RECENT_SAMPLE when Reference trigger is not configured; REFERENCE_TRIGGER when Reference trigger is configured | MOST_RECENT_SAMPLE when Reference trigger is not configured; REFERENCE_TRIGGER when Reference trigger is configured | MOST_RECENT_SAMPLE when Reference trigger is not configured; REFERENCE_TRIGGER when Reference trigger is configured | MOST_RECENT_SAMPLE when Reference trigger is not configured; REFERENCE_TRIGGER when Reference trigger is configured | MOST_RECENT_SAMPLE when Reference trigger is not configured; REFERENCE_TRIGGER when Reference trigger is configured |
| HWC_FILTER_REPEATED_SAMPLE_ERRORS | N/A | VI_FALSE | VI_FALSE | VI_FALSE | N/A |
| GENERATION_MODE | WAVEFORM | WAVEFORM | WAVEFORM | WAVEFORM | WAVEFORM |
| IDLE_STATE | HOLD_LAST_VALUE | HOLD_LAST_VALUE | HOLD_LAST_VALUE | HOLD_LAST_VALUE | HOLD_LAST_VALUE |
| INITIAL_STATE | HOLD_LAST_VALUE | HOLD_LAST_VALUE | HOLD_LAST_VALUE | HOLD_LAST_VALUE | HOLD_LAST_VALUE |
| INPUT_IMPEDANCE | 50 Ω | 50 Ω | 50 Ω | N/A | 50 Ω |
| MARKER_EVENT_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| MARKER_EVENT_POSITION | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE | SAMPLE_CLOCK_RISING_EDGE |
| MARKER_EVENT_PULSE_POLARITY | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH |
| MARKER_EVENT_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| NUM_RECORDS | 1 | 1 | 1 | 1 | 1 |
| HWC_NUM_SAMPLE_ERRORS | — | — | — | — | — |
| OSCILLATOR_PHASE_DAC_VALUE | 0 | 0 | 0 | 0 | 0 |
| PATTERN_MATCH_ADVANCE_TRIGGER_PATTERN | "" | "" | "" | "" | "" |
| PATTERN_MATCH_ADVANCE_TRIGGER_WHEN | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES |
| PATTERN_MATCH_PAUSE_TRIGGER_PATTERN | "" | "" | "" | "" | "" |
| PATTERN_MATCH_PAUSE_TRIGGER_WHEN | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES |
| PATTERN_MATCHES_REF_TRIGGER_PATTERN | "" | "" | "" | "" | "" |
| PATTERN_MATCH_REF_TRIGGER_WHEN | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES |
| PATTERN_MATCH_START_TRIGGER_PATTERN | "" | "" | "" | "" | "" |
| PATTERN_MATCH_START_TRIGGER_WHEN | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES | PATTERN_MATCHES |
| PAUSE_TRIGGER_TYPE | NONE | NONE | NONE | NONE | NONE |
| READY_FOR_ADVANCE_EVENT_LEVEL_ACTIVE_LEVEL | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH |
| READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| READY_FOR_ADVANCE_EVENT_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH | ACTIVE_HIGH |
| READY_FOR_START_EVENT_OUTPUT_TERMINAL | "" | "" | "" | "" | "" |
| READY_FOR_START_EVENT_TERMINAL_CONFIGURATION | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | SINGLE_ENDED | LVDS |
| RECORDS_DONE | — | — | — | — | — |
| REF_CLOCK_IMPEDANCE | 50 Ω | 50 Ω | 50 Ω | 50 Ω | 100 Ω |
| REF_CLOCK_RATE | 10M | 10M | 10M | 10M | 10M |
| REF_CLOCK_SOURCE | "" | "" | "" | "" | "" |
| REF_TRIGGER_PRETRIGGER_SAMPLES | 0 | 0 | 0 | 0 | 0 |
| REF_TRIGGER_TYPE | NONE | NONE | NONE | NONE | NONE |
| REPEAT_COUNT | 1 | 1 | 1 | 1 | 1 |
| REPEAT_MODE | FINITE | FINITE | FINITE | FINITE | FINITE |
| SAMPLE_CLOCK_IMPEDANCE | 50 Ω | 50 Ω | 50 Ω | 50 Ω | 100 Ω |
| SAMPLE_CLOCK_RATE | 50 MHz | 50 MHz | 50 MHz | 50 MHz | 50 MHz |
| SAMPLE_CLOCK_SOURCE | ON_BOARD_CLOCK_STR | ON_BOARD_CLOCK_STR | ON_BOARD_CLOCK_STR | ON_BOARD_CLOCK_STR | ON_BOARD_CLOCK_STR |
| HWC_SAMPLE_ERROR_BACKLOG | N/A | N/A | — | — | N/A |
| HWC_SAMPLE_ERROR_BUFFER_OVERFLOWED | N/A | N/A | — | — | N/A |
| HWC_SAMPLE_ERROR_EVENT_OUTPUT_TERMINAL | N/A | N/A | "" | "" | N/A |
| HWC_SAMPLES_COMPARED | N/A | N/A | — | — | N/A |
| SAMPLES_PER_RECORD | 1000 | 1000 | 1000 | 1000 | 1000 |
| SAMPLES_PER_RECORD_IS_FINITE | VI_TRUE | VI_TRUE | VI_TRUE | VI_TRUE | VI_TRUE |
| SCRIPT_TO_GENERATE | "" | "" | "" | "" | "" |
| SCRIPT_TRIGGER_TYPE | NONE | NONE | NONE | NONE | NONE |
| SERIAL_NUMBER | — | — | — | — | — |
| SPACE_AVAILABLE_IN_STREAMING_WAVEFORM | 0 | 0 | 0 | 0 | 0 |
| START_TRIGGER_TYPE | NONE | NONE | NONE | NONE | NONE |
| STATIC_CHANNELS | "" | "" | "" | "" | "" |
| STOP_TRIGGER_TYPE | N/A | NONE | N/A | NONE | N/A |
| STREAMING_ENABLED | VI_FALSE | VI_FALSE | VI_FALSE | VI_FALSE | VI_FALSE |
| STREAMING_WAVEFORM_NAME | "" | "" | "" | "" | "" |
| SUPPORTED_DATA_STATES | N/A | NIHSDIO_VAL_0_1 (NI 6547/6548 only) | NIHSDIO_VAL_0_1 | NIHSDIO_VAL_0_1 | N/A |
| TOTAL_ACQUISITION_SIZE | — | — | — | — | — |
| TOTAL_GENERATION_SIZE | — | — | — | — | — |
| TRIGGER_DESKEW | N/A | N/A | N/A | 0 | N/A |
| TRIGGER_POSITION_DELAY | N/A | N/A | N/A | 0 | N/A |
| TRIGGER_VOLTAGE_HIGH_LEVEL | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | N/A |
| TRIGGER_VOLTAGE_LOW_LEVEL | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | 3.3 V logic family voltage levels. Refer to device specifications for more information. | N/A |
| TRIGGER_VOLTAGE_RANGE | N/A | N/A | N/A | MINUS_2_TO_6_VOLTAGE_RANGE | N/A |
| WAVEFORM_TO_GENERATE | "" | "" | "" | "" | "" |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_active_load_commutating_voltage_level.html language=enus -->
## TOPIC 00019: NIHSDIO_ATTR_ACTIVE_LOAD_COMMUTATING_VOLTAGE_LEVEL

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_active_load_commutating_voltage_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_active_load_commutating_voltage_level.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_ACTIVE_LOAD_COMMUTATING_VOLTAGE_LEVEL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | N/A |

#### Description

Specifies the voltage threshold that causes the driver to switch from sourcing to sinking current. 
If the incoming voltage is greater than or equal to the commutating voltage level, the device sinks current. 
Conversely, if the incoming voltage is less than the commutating voltage level, the device sources current.

Valid values range from –2 V to 7 V.

The default value is 0 V.

The units are volts (V).

You can select the PFI channels and clocks in the **channelName** input in the Set Attribute function 
 using the following strings: PFI1, PFI2, STROBE, and DDC_CLKOUT. These strings are not case sensitive and can be grouped with the standard input strings separated by commas. The following are examples of valid string syntax: 0, 4, 6, PFI1, 7 or 0-12, STROBE, DDC_CLKOUT.

|  | Note | Only NI 6556 devices support this attribute. |
| --- | --- | --- |

|  | Note When NIHSDIO_ATTR_ATTRIBUTE_COMMITTAL_STRATEGY is configured to NIHSDIO_VAL_IMMEDIATELY_UPON_SET_VOLTAGE, setting this attribute while the session is in the Committed or Running state causes the new value to take effect by the time the attribute returns. |
| --- | --- |

##### Related Topics

[Active Load (L)](/csh?topicname=hsdio/hactive_load_2_6556.html)

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_active_load_sourcing_current_value.html language=enus -->
## TOPIC 00020: NIHSDIO_ATTR_ACTIVE_LOAD_SOURCING_CURRENT_VALUE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_active_load_sourcing_current_value.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_active_load_sourcing_current_value.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_ACTIVE_LOAD_SOURCING_CURRENT_VALUE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | N/A |

#### Description

Specifies the amount of current for the driver to source if the input voltage is less than the commutating 
 voltage.

Valid values range from 1.5 mA to 24 mA.

The default value is 1.5 mA.

Units are amps (A).

|  | Note This attribute takes effect only if the NIHSDIO_ATTR_ACTIVE_LOAD_MODE attribute is set to NIHSDIO_VAL_ACTIVE_LOAD_ENABLED_WHEN_TRISTATE in the current session. |
| --- | --- |

You can select the PFI channels and clocks in the **channelName** input in the 
 Set Attribute function 
 using the following strings: PFI1, PFI2, 
 STROBE, and DDC_CLKOUT. These strings are not case 
 sensitive and can be grouped with the standard input strings separated by commas. 
 The following are examples of valid string syntax: 0, 4, 6, PFI1,
 7 or 0-12, STROBE, DDC_CLKOUT.

|  | Note | Only NI 6556 devices support this attribute. |
| --- | --- | --- |

|  | Note When NIHSDIO_ATTR_ATTRIBUTE_COMMITTAL_STRATEGY is configured to NIHSDIO_VAL_IMMEDIATELY_UPON_SET_VOLTAGE, setting this attribute while the session is in the Committed or Running state causes the new value to take effect by the time the attribute returns. |
| --- | --- |

##### Related Topics

[Active Load (L)](/csh?topicname=hsdio/hactive_load_2_6556.html)

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_active_event_output_terminal.html language=enus -->
## TOPIC 00021: NIHSDIO_ATTR_DATA_ACTIVE_EVENT_OUTPUT_TERMINAL

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_active_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_active_event_output_terminal.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_ACTIVE_EVENT_OUTPUT_TERMINAL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niHSDIO_ExportSignal |

#### Description

Specifies the destination terminal for the [Data Active](/csh?topicname=hsdio/fevents_hsdi.html) event. Event voltages 
and positions are only relevant if the destination of the event is a front panel connector.

This attribute is valid only for generation sessions.

#### Defined Values:

| NIHSDIO_VAL_DO_NOT_EXPORT_STR ("None") | The signal is not exported. |
| --- | --- |
| NIHSDIO_VAL_PFI0_STR ("PFI0") | PFI 0 front panel connector. |
| NIHSDIO_VAL_PFI1_STR ("PFI1") | PFI 1 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI2_STR ("PFI2") | PFI 2 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI3_STR ("PFI3") | PFI 3 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI24_STR ("PFI24") | PFI 24 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI25_STR ("PFI25") | PFI 25 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI26_STR ("PFI26") | PFI 26 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI27_STR ("PFI27") | PFI 27 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI28_STR ("PFI28") | PFI 28 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI29_STR ("PFI29") | PFI 29 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI30_STR ("PFI30") | PFI 30 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI31_STR ("PFI31") | PFI 31 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |

##### Related Topics

[Events Summary](/csh?topicname=hsdio/fevents_hsdi.html)

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_active_event_position.html language=enus -->
## TOPIC 00022: NIHSDIO_ATTR_DATA_ACTIVE_EVENT_POSITION

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_active_event_position.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_active_event_position.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_ACTIVE_EVENT_POSITION

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the position of the [Data Active](/csh?topicname=hsdio/fevents_hsdi.html) event relative to the 
Sample clock. Event voltages and positions are only relevant if the destination of the 
event is a front panel connector.

#### Defined Values:

| NIHSDIO_VAL_SAMPLE_CLOCK_RISING_EDGE (18) | The event is issued synchronously with the Sample clock rising edge. |
| --- | --- |
| NIHSDIO_VAL_SAMPLE_CLOCK_FALLING_EDGE (19) | The event is issued synchronously with the Sample clock falling edge. |
| NIHSDIO_VAL_DELAY_FROM_SAMPLE_CLOCK_RISING_EDGE (20) | The event is issued synchronously with delay from rising edge of the Sample clock. Specify the delay using NIHSDIO_ATTR_DATA_POSITION_DELAY. This choice has more jitter than the rising or falling edge values. Certain devices have Sample clock frequency limitations on when a custom delay can be used. Refer to the device documentation for details. |

##### Related Topics

[Events Summary](/csh?topicname=hsdio/fevents_hsdi.html)

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_active_event_terminal_configuration.html language=enus -->
## TOPIC 00023: NIHSDIO_ATTR_DATA_ACTIVE_EVENT_TERMINAL_CONFIGURATION

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_active_event_terminal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_active_event_terminal_configuration.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_ACTIVE_EVENT_TERMINAL_CONFIGURATION

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies whether the [Data Active](/csh?topicname=hsdio/fevents_hsdi.html) event terminal is 
configured for single-ended or LVDS operation. Valid values for this 
attribute vary by device. Refer to your device documentation to determine 
if your hardware supports LVDS operation.

#### Defined Values:

| NIHSDIO_VAL_LVDS (64) | The terminal is configured for LVDS voltage levels. |
| --- | --- |
| NIHSDIO_VAL_SINGLE_ENDED (65) | The terminal is configured for single-ended voltage levels. |

##### Related Topics

[Events Summary](/csh?topicname=hsdio/fevents_hsdi.html)

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_position.html language=enus -->
## TOPIC 00024: NIHSDIO_ATTR_DATA_POSITION

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_position.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_position.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_POSITION

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Channel | None | niHSDIO_ConfigureDataPosition |

#### Description

Specifies the [data position](/csh?topicname=hsdio/fdata_position.html) for the operation, 
which specifies which edge of the [Sample clock](/csh?topicname=hsdio/fsample_clock.html) 
is used to time the generation or acquisition. You can 
also configure the device to generate or acquire data at a configurable 
delay past each rising edge of the Sample clock. When this attribute is set to 
NIHSDIO_VAL_DELAY_FROM_SAMPLE_CLOCK_RISING_EDGE, 
use the [NIHSDIO_ATTR_DATA_POSITION_DELAY](nihsdio_attr_data_position_delay.html) attribute to specify the delay value.
This attribute is relevant only when the
[NIHSDIO_ATTR_DATA_POSITION](nihsdio_attr_data_position.html) attribute is set to 
NIHSDIO_VAL_DELAY_FROM_SAMPLE_CLOCK_RISING_EDGE.
Refer to the [Alphabetical Attributes List](defaults.html) topic for a list of default values per device.

This attribute applies to static and dynamic data operations.

|  | Note On NI 6555/6556 devices, this attribute is per channel selectable. |
| --- | --- |

|  | Note To configure a delay on NI 656x devices, you must delay all channels on the device. NI-HSDIO returns an error if you apply a delay to only a partial channel list. |
| --- | --- |

Refer to the [NIHSDIO_ATTR_DATA_POSITION_DELAY](nihsdio_attr_data_position_delay.html) attribute for more information about multibank data delay.

#### Defined Values:

| NIHSDIO_VAL_SAMPLE_CLOCK_RISING_EDGE (18) | Samples or generates data on the Sample clock rising edge. |
| --- | --- |
| NIHSDIO_VAL_SAMPLE_CLOCK_FALLING_EDGE (19) | Samples or generates data on the Sample clock falling edge. |
| NIHSDIO_VAL_DELAY_FROM_SAMPLE_CLOCK_RISING_EDGE (20) | Samples or generates data with a delay from the Sample clock rising edge. Specify the delay using the NIHSDIO_ATTR_DATA_POSITION_DELAY attribute. This value has more jitter than the rising or falling edge values. Certain devices have Sample clock frequency limitations on when a custom delay can be used. Refer to the device sections for details. |

##### Related Topics

[Data Position Delay Resolution](/csh?topicname=hsdio/fdata_resolution.html)

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_position_delay.html language=enus -->
## TOPIC 00025: NIHSDIO_ATTR_DATA_POSITION_DELAY

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_position_delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_position_delay.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_POSITION_DELAY

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | Channel | None | niHSDIO_ConfigureDataPositionDelay |

#### Description

Specifies the delay after the Sample clock rising edge 
when the device generates or acquires a new data sample. Data delay is 
expressed as a fraction of the clock period 
(for example, a fraction of 1/[NIHSDIO_ATTR_SAMPLE_CLOCK_RATE](nihsdio_attr_sample_clock_rate.html)). 
This attribute is relevant only when the
[NIHSDIO_ATTR_DATA_POSITION](nihsdio_attr_data_position.html) attribute is set to 
NIHSDIO_VAL_DELAY_FROM_SAMPLE_CLOCK_RISING_EDGE.

|  | Note On NI 6555/6556 devices, valid values range from –1 to 2 clock cycles in increments of 0.001 cycles. Delay on NI 6555/6556 devices is configured on a per channel basis. |
| --- | --- |

|  | Note To configure a delay on NI 656x devices, you must delay all channels on the device. NI-HSDIO returns an error if you apply a delay to only a partial channel list. |
| --- | --- |

The NI 6547/6548 supports [multibank data delay](/csh?topicname=hsdio/hmultibank_data_delay_6547.html). All channels configured to NIHSDIO_VAL_DELAY_FROM_SAMPLE_CLOCK_RISING_EDGE and assigned to the same data delay bank must share a data delay value, even if channels on that bank are configured to NIHSDIO_VAL_SAMPLE_CLOCK_RISING_EDGE or NIHSDIO_VAL_SAMPLE_CLOCK_FALLING_EDGE. NI-HSDIO returns an error if you set different delay values for two channels within the same bank.

The following table shows which channels belong to each bank.

| Channels | 0-3 | 4-7 | 8-11 | 12-15 | 16-19 | 20-23 | 24-27 | 28-31 | PFI 0-3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bank # | 0 | 1 | 2 | 2 | 0 | 1 | 2 | 0 | 0 |

|  | Note DDR and extended data states do not change the bank assignments. |
| --- | --- |

#### Related topics:

- Data Position Delay Resolution

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_rate_multiplier.html language=enus -->
## TOPIC 00026: NIHSDIO_ATTR_DATA_RATE_MULTIPLIER

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_rate_multiplier.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_rate_multiplier.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_RATE_MULTIPLIER

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies whether you want the device to acquire or generate in 
single data rate (SDR) mode or in double data rate (DDR) mode.

#### Defined Values:

| NIHSDIO_VAL_SINGLE_DATA_RATE (1) | The device samples or generates data in single data rate (SDR) mode. When in SDR mode, the NI digital waveform generator/analyzer generates or acquires data on a single edge of the Sample clock. Therefore, you can generate or acquire data on the rising or falling edge of every Sample clock pulse or on a delayed version of the rising edge of the Sample clock. |
| --- | --- |
| NIHSDIO_VAL_DOUBLE_DATA_RATE (2) | The device samples or generates data in double data rate (DDR) mode. When in DDR mode, the NI digital waveform generator/analyzer generates or acquires data on both edges of the Sample clock. Therefore, you can generate or acquire data on every rising and falling edge of the Sample clock. Acquisition and generation sessions can be configured in DDR mode to acquire or generate the first data sample on the rising or falling edge of the clock or on a delayed version of the rising edge of the clock. |

#### Related topics:

- Data Rate Multiplier
- Double Data Rate (DDR)
- Data Position with DDR

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_termination_mode.html language=enus -->
## TOPIC 00027: NIHSDIO_ATTR_DATA_TERMINATION_MODE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_termination_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_termination_mode.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_TERMINATION_MODE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Channel | None | None |

#### Description

Specifies the action taken by NI-HSDIO when a channel is tristated. A tristate condition can occur during [initial states](/csh?topicname=hsdio/falternatevectors.html), 
[idle states](/csh?topicname=hsdio/falternatevectors.html), [per cycle tristate](/csh?topicname=hsdio/fsample_tristate.html), and static tristate. 
Selecting NIHSDIO_VAL_HIGH_IMPEDANCE sets the channel to a high-impedance state when tristated. Selecting NIHSDIO_VAL_DRIVE_TERMINATION_VOLTAGE sets the channel to drive a termination voltage (V<sub>TT</sub>).

|  | Note This attribute is supported only on NI 6555/6556 devices. |
| --- | --- |

This attribute is valid only for acquisition sessions.

|  | Note If you set the NIHSDIO_ATTR_DATA_TERMINATION_MODE and NIHSDIO_ATTR_DATA_TRISTATE_MODE attributes to different values on the same channel, NI-HSDIO returns an error. |
| --- | --- |

#### Defined Values:

| NIHSDIO_VAL_HIGH_IMPEDANCE (84) | Digital driver is disabled when tristated. This value is the default. |
| --- | --- |
| NIHSDIO_VAL_DRIVE_TERMINATION_VOLTAGE (85) | The channel drives the specified termination voltage when tristated. |

#### Related topics:

- Input Impedance
- Per Cycle Tristate
- Comparator (C)

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_transfer_block_size.html language=enus -->
## TOPIC 00028: NIHSDIO_ATTR_DATA_TRANSFER_BLOCK_SIZE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_transfer_block_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_transfer_block_size.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_TRANSFER_BLOCK_SIZE

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the number of samples to download to onboard memory at one time.

#### Related topics:

- Direct DMA
- Generating Waveforms Using Streaming

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_transfer_maximum_bandwidth.html language=enus -->
## TOPIC 00029: NIHSDIO_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_transfer_maximum_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_transfer_maximum_bandwidth.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | N/A |

#### Description

Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The high-speed digital device limits data transfer speeds on the PCI Express bus to the value you specify for this attribute. Set this attribute to optimize bus bandwidth usage for multi-device streaming applications by preventing the high-speed digital device from consuming all of the available bandwidth on a PCI Express link when waveforms are being written to the onboard memory of the device.

#### Related topics:

- PXI Express Bandwidth Considerations

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_transfer_maximum_in_flight_reads.html language=enus -->
## TOPIC 00030: NIHSDIO_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_transfer_maximum_in_flight_reads.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_transfer_maximum_in_flight_reads.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | N/A |

#### Description

Specifies the maximum number of concurrent PCI Express read requests the high-speed digital device can issue.

When transferring data from computer memory to device onboard memory across the PCI Express bus, the high-speed digital device can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus. This efficiency is caused by the multiple read requests that keep data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this attribute is set to the highest value the high-speed digital device supports.

If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the high-speed digital device issues. This change helps to reduce the amount of data the high-speed digital device reads at one time.

#### Related topics:

- PXI Express Bandwidth Considerations

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_data_transfer_preferred_packet_size.html language=enus -->
## TOPIC 00031: NIHSDIO_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_data_transfer_preferred_packet_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_data_transfer_preferred_packet_size.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | N/A |

#### Description

Specifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI high-speed digital devices use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.

Recommended values for this attribute are powers of two between 64 and 512.

|  | Note In some cases, the high-speed digital device generates packets smaller than the preferred size you set with this attribute. |
| --- | --- |

#### Related topics:

- PXI Express Bandwidth Considerations

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_exported_stop_trigger_output_terminal.html language=enus -->
## TOPIC 00032: NIHSDIO_ATTR_EXPORTED_STOP_TRIGGER_OUTPUT_TERMINAL

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_exported_stop_trigger_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_exported_stop_trigger_output_terminal.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_EXPORTED_STOP_TRIGGER_OUTPUT_TERMINAL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niHSDIO_ExportSignal |

#### Description

Specifies the destination terminal for the exported [Stop trigger](/csh?topicname=hsdio/ftriggers_hsdi.html). 
Event voltages and positions are only relevant if the destination of the event is one of the 
front panel connectors.

This attribute is only valid for generation sessions.

#### Defined Values:

| NIHSDIO_VAL_DO_NOT_EXPORT_STR ("None") | The signal is not exported. |
| --- | --- |
| NIHSDIO_VAL_PFI0_STR ("PFI0") | PFI 0 front panel connector. |
| NIHSDIO_VAL_PFI1_STR ("PFI1") | PFI 1 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI2_STR ("PFI2") | PFI 2 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI3_STR ("PFI3") | PFI 3 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI24_STR ("PFI24") | PFI 24 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI25_STR ("PFI25") | PFI 25 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI26_STR ("PFI26") | PFI 26 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI27_STR ("PFI27") | PFI 27 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI28_STR ("PFI28") | PFI 28 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI29_STR ("PFI29") | PFI 29 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI30_STR ("PFI30") | PFI 30 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI31_STR ("PFI31") | PFI 31 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PXI_TRIG0_STR ("PXI_Trig0") | PXI trigger line 0. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG1_STR ("PXI_Trig1") | PXI trigger line 1. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG2_STR ("PXI_Trig2") | PXI trigger line 2. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG3_STR ("PXI_Trig3") | PXI trigger line 3. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG4_STR ("PXI_Trig4") | PXI trigger line 4. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG5_STR ("PXI_Trig5") | PXI trigger line 5. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG6_STR ("PXI_Trig6") | PXI trigger line 6. (PXI devices) |
| NIHSDIO_VAL_RTSI0_STR ("RTSI0") | RTSI trigger line 0. (PCI devices) |
| NIHSDIO_VAL_RTSI1_STR ("RTSI1") | RTSI trigger line 1. (PCI devices) |
| NIHSDIO_VAL_RTSI2_STR ("RTSI2") | RTSI trigger line 2. (PCI devices) |
| NIHSDIO_VAL_RTSI3_STR ("RTSI3") | RTSI trigger line 3. (PCI devices) |
| NIHSDIO_VAL_RTSI4_STR ("RTSI4") | RTSI trigger line 4. (PCI devices) |
| NIHSDIO_VAL_RTSI5_STR ("RTSI5") | RTSI trigger line 5. (PCI devices) |
| NIHSDIO_VAL_RTSI6_STR ("RTSI6") | RTSI trigger line 6. (PCI devices) |

#### Related topics:

- Triggers Summary

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_exported_stop_trigger_terminal_configuration.html language=enus -->
## TOPIC 00033: NIHSDIO_ATTR_EXPORTED_STOP_TRIGGER_TERMINAL_CONFIGURATION

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_exported_stop_trigger_terminal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_exported_stop_trigger_terminal_configuration.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_EXPORTED_STOP_TRIGGER_TERMINAL_CONFIGURATION

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies that the [Stop trigger](/csh?topicname=hsdio/ftriggers_hsdi.html) output terminal is configured for single-ended operations. Stop trigger does not support LVDS operations. This attribute is valid only for generation sessions.

#### Defined Values:

| NIHSDIO_VAL_SINGLE_ENDED (65) | The terminal is configured for single-ended voltage levels. |
| --- | --- |

#### Related topics:

- Triggers Summary

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_fetch_backlog.html language=enus -->
## TOPIC 00034: NIHSDIO_ATTR_FETCH_BACKLOG

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_fetch_backlog.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_fetch_backlog.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_FETCH_BACKLOG

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Use this attribute to query how many acquired samples remain in onboard 
memory. This attribute is used with 
[NIHSDIO_ATTR_FETCH_OFFSET](nihsdio_attr_fetch_offset.html) and 
[NIHSDIO_FETCH_RELATIVE_TO](nihsdio_attr_fetch_relative_to.html). 
This attribute returns the number of samples available from the specified
[NIHSDIO_ATTR_FETCH_OFFSET](nihsdio_attr_fetch_offset.html) and 
[NIHSDIO_FETCH_RELATIVE_TO](nihsdio_attr_fetch_relative_to.html) values.

This attribute is valid only for acquisition sessions.

#### Related topics:

- Records

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_fetch_offset.html language=enus -->
## TOPIC 00035: NIHSDIO_ATTR_FETCH_OFFSET

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_fetch_offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_fetch_offset.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_FETCH_OFFSET

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Offset in samples to start fetching acquired waveform data. The offset is 
applied relative to the [NIHSDIO_ATTR_FETCH_RELATIVE_TO](nihsdio_attr_fetch_relative_to.html) 
position. Offset can be a positive or negative value.

If the specified offset would cause the fetch to occur before the start of the waveform or exceed the end of the waveform, NI-HSDIO returns a data overwrite error.

This attribute is valid only for acquisition sessions.

#### Related topics:

- Records

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_fetch_relative_to.html language=enus -->
## TOPIC 00036: NIHSDIO_ATTR_FETCH_RELATIVE_TO

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_fetch_relative_to.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_fetch_relative_to.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_FETCH_RELATIVE_TO

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the absolute location within the [acquired record](/csh?topicname=hsdio/fmem_acq_operations.html) from which to 
begin fetching.

This attribute is supported only for acquisition sessions.

#### Defined Values:

| NIHSDIO_VAL_MOST_RECENT_SAMPLE (46) | Specifies that fetching occur relative to the most recently acquired data. The fetch offset (NIHSDIO_ATTR_FETCH_OFFSET) must be negative to use this value. |
| --- | --- |
| NIHSDIO_VAL_FIRST_SAMPLE (47) | Specifies that fetching occurs at the first sample acquired by the device. If the device wraps its buffer, then the first sample is no longer available. In this case, NI-HSDIO returns an error if the fetch offset is in the overwritten data. |
| NIHSDIO_VAL_REFERENCE_TRIGGER (48) | Specifies that fetching occur relative to the Reference trigger. This value behaves like NIHSDIO_VAL_FIRST_SAMPLE if no Reference trigger is configured. |
| NIHSDIO_VAL_FIRST_PRETRIGGER_SAMPLE (49) | Specifies that fetching occur relative to the first pretrigger sample acquired. This value behaves like NIHSDIO_VAL_FIRST_SAMPLE if no Reference trigger is configured. |
| NIHSDIO_VAL_CURRENT_READ_POSITION (50) | Specifies that fetching occur after the last fetched sample. The initial read position depends on whether the Reference trigger is enabled. If the Reference trigger is disabled, the initial read position is the first sample acquired. If a Reference trigger is enabled, the initial read position is the first pretrigger sample. |

#### Related topics:

- Records

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_generation_mode.html language=enus -->
## TOPIC 00037: NIHSDIO_ATTR_GENERATION_MODE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_generation_mode.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_generation_mode.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_GENERATION_MODE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niHSDIO_ConfigureGenerationMode |

#### Description

Use this attribute to specify whether to generate the waveform specified by 
[NIHSDIO_ATTR_WAVEFORM_TO_GENERATE](nihsdio_attr_waveform_to_generate.html) 
or the script specified by [NIHSDIO_ATTR_SCRIPT_TO_GENERATE](nihsdio_attr_script_to_generate.html) 
upon calling [niHSDIO_Initiate](cvinihsdio_initiate.html).

This attribute is valid 
only for generation sessions.

#### Defined Values:

| NIHSDIO_VAL_WAVEFORM (14) | Calling niHSDIO_Initiate generates the named waveform represented by NIHSDIO_ATTR_WAVEFORM_TO_GENERATE. |
| --- | --- |
| NIHSDIO_VAL_SCRIPTED (15) | Calling niHSDIO_Initiate generates the script represented by NIHSDIO_ATTR_SCRIPT_TO_GENERATE. |

#### Related topics:

- Generating Data in Single-Waveform Mode
- Generating Multiple Waveforms/Linking & Looping

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_hwc_cumulative_error_bits.html language=enus -->
## TOPIC 00038: NIHSDIO_ATTR_HWC_CUMULATIVE_ERROR_BITS

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_hwc_cumulative_error_bits.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_hwc_cumulative_error_bits.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_HWC_CUMULATIVE_ERROR_BITS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViUInt32 | RO | N/A | None |  |

#### Description

Returns an aggregate bit error mask. If a channel has a hardware compare sample error at any point in the execution, 
the bit corresponding to that channel is enabled. Use this attribute to determine which channel reported a sample error 
independently of the state of the hardware compare FIFO.

|  | Note This attribute is supported for NI 6555/6556 devices only. |
| --- | --- |

#### Related topics:

- Comparing Response Data in Hardware

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_hwc_filter_repeated_sample_errors.html language=enus -->
## TOPIC 00039: NIHSDIO_ATTR_HWC_FILTER_REPEATED_SAMPLE_ERRORS

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_hwc_filter_repeated_sample_errors.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_hwc_filter_repeated_sample_errors.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_HWC_FILTER_REPEATED_SAMPLE_ERRORS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | None | None | None |

#### Description

Specifies whether the device stores and counts errors when the same error appears in consecutive samples. If this attribute is set to VI_TRUE, the device only counts distinct errors. An error is defined as distinct if the expected response value and the actual sample error do not change over the same number of Sample clock cycles. The [niHSDIO_HWC_FetchSampleErrors](cvinihsdio_hwc_fetchsampleerrors.html) function returns the number of clock cycles for which the repeated error occurred.

This attribute is helpful if your NI device clock rate is significantly faster than your DUT clock rate. In this case, one error from the DUT could result in several identical errors on the device.

#### Related topics:

- Comparing Response Data in Hardware

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_hwc_num_sample_errors.html language=enus -->
## TOPIC 00040: NIHSDIO_ATTR_HWC_NUM_SAMPLE_ERRORS

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_hwc_num_sample_errors.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_hwc_num_sample_errors.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_HWC_NUM_SAMPLE_ERRORS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViIn32 | RO | None | None | None |

#### Description

Returns the total number of sample errors since the acquisition was initiated. Use this attribute, along with [NIHSDIO_ATTR_HWC_SAMPLES_COMPARED](nihsdio_attr_hwc_samples_compared.html), to calculate the sample error rate.

#### Related topics:

- Comparing Response Data in Hardware

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_hwc_sample_error_backlog.html language=enus -->
## TOPIC 00041: NIHSDIO_ATTR_HWC_SAMPLE_ERROR_BACKLOG

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_hwc_sample_error_backlog.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_hwc_sample_error_backlog.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_HWC_SAMPLE_ERROR_BACKLOG

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViIn32 | RO | None | None | None |

#### Description

Returns the number of sample errors available you can read using the [niHSDIO_HWC_FetchSampleErrors](cvinihsdio_hwc_fetchsampleerrors.html) function.

#### Related topics:

- Comparing Response Data in Hardware

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_marker_event_pulse_polarity.html language=enus -->
## TOPIC 00042: NIHSDIO_ATTR_MARKER_EVENT_PULSE_POLARITY

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_marker_event_pulse_polarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_marker_event_pulse_polarity.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_MARKER_EVENT_PULSE_POLARITY

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | Marker | None | None |

#### Description

Specifies the output polarity of the [Marker event](/csh?topicname=hsdio/fevents_hsdi.html).

This attribute is valid only for generation sessions.

#### Defined Values:

| NIHSDIO_VAL_ACTIVE_HIGH (10) | The exported signal is low level while the event is deasserted. A high pulse occurs when the event asserts. This attribute does not apply to other exported signals. |
| --- | --- |
| NIHSDIO_VAL_ACTIVE_LOW (11) | The exported signal is high level while the event is deasserted. A low pulse occurs when the event asserts. This attribute does not apply to other exported signals. |

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_marker_event_terminal_configuration.html language=enus -->
## TOPIC 00043: NIHSDIO_ATTR_MARKER_EVENT_TERMINAL_CONFIGURATION

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_marker_event_terminal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_marker_event_terminal_configuration.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_MARKER_EVENT_TERMINAL_CONFIGURATION

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies whether the [Marker](/csh?topicname=hsdio/fevents_hsdi.html) event terminal is 
configured for single-ended or LVDS operation. Valid values for this 
attribute vary by device. Refer to your device documentation to determine 
if your hardware supports LVDS operation.

#### Defined Values:

| NIHSDIO_VAL_LVDS (64) | The terminal is configured for LVDS voltage levels. |
| --- | --- |
| NIHSDIO_VAL_SINGLE_ENDED (65) | The terminal is configured for single-ended voltage levels. |

#### Related topics:

- Events Summary

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_num_records.html language=enus -->
## TOPIC 00044: NIHSDIO_ATTR_NUM_RECORDS

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_num_records.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_num_records.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_NUM_RECORDS

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the number of records you want to acquire.

#### Related topics:

- Acquisition Onboard Memory

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_pattern_match_ref_trigger_pattern.html language=enus -->
## TOPIC 00045: NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_PATTERN

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_pattern_match_ref_trigger_pattern.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_pattern_match_ref_trigger_pattern.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_PATTERN

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niHSDIO_ConfigurePatternMatchRefTrigger |

#### Description

Sets the pattern match mask for the [Reference trigger](/csh?topicname=hsdio/ftriggers_hsdi.html). This attribute is 
used when [NIHSDIO_ATTR_REF_TRIGGER_TYPE](nihsdio_attr_ref_trigger_type.html) is set to 
NIHSDIO_VAL_PATTERN_MATCH.

The pattern is a string of characters representing the entire pattern to be matched on. 
Each character corresponds to a particular channel.

- 'X': Match on any value
- '1': Match on a logic 1
- '0': Match on a logic 0
- R or r : Match on a rising edge
- F or f : Match on a falling edge
- E or e : Match on either edge

Spaces are ignored, and are useful for readability to segment long patterns. The 
rightmost character in the expression corresponds to the lowest numbered physical 
channel. For example, XXXX XXXX XXXX 1111 1100
specifies to match when channels 0 and 1 are '0' and channels 2-7 are '1'. 
The values seen by pattern matching are 
affected by [NIHSDIO_ATTR_DATA_INTERPRETATION](nihsdio_attr_data_interpretation.html).

This attribute is valid only for acquisition sessions.

#### Related topics:

- Triggers Summary
- Pattern-Match Trigger
- Dynamic Acquisition Triggers and Events

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_pattern_match_ref_trigger_when.html language=enus -->
## TOPIC 00046: NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_WHEN

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_pattern_match_ref_trigger_when.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_pattern_match_ref_trigger_when.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_WHEN

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niHSDIO_ConfigurePatternMatchRefTrigger |

#### Description

Specifies whether a [pattern match](/csh?topicname=hsdio/fpattern_match_trigger.html) 
[Reference trigger](/csh?topicname=hsdio/ftriggers_hsdi.html) asserts when a particular pattern 
is matched or not matched. This attribute is valid only for acquisition tasks.

#### Defined Values:

| NIHSDIO_VAL_PATTERN_MATCHES (36) | The trigger asserts when the pattern matches. |
| --- | --- |
| NIHSDIO_VAL_PATTERN_DOES_NOT_MATCH (37) | The trigger asserts when the pattern does not match. |

#### Related topics:

- Triggers Summary
- Pattern-Match Trigger
- Dynamic Acquisition Triggers and Events

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_pattern_match_start_trigger_pattern.html language=enus -->
## TOPIC 00047: NIHSDIO_ATTR_PATTERN_MATCH_START_TRIGGER_PATTERN

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_pattern_match_start_trigger_pattern.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_pattern_match_start_trigger_pattern.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_PATTERN_MATCH_START_TRIGGER_PATTERN

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niHSDIO_ConfigurePatternMatchStartTrigger |

#### Description

Sets the pattern match mask for the [Start trigger](/csh?topicname=hsdio/ftriggers_hsdi.html). This attribute is used 
when [NIHSDIO_ATTR_START_TRIGGER_TYPE](nihsdio_attr_start_trigger_type.html) 
is set to NIHSDIO_VAL_PATTERN_MATCH. 
The pattern is a string of characters representing the entire pattern to be matched on. 
Each character corresponds to a particular channel.

- 'X': Match on any value
- '1': Match on a logic 1
- '0': Match on a logic 0
- R or r : Match on a rising edge
- F or f : Match on a falling edge
- E or e : Match on either edge

Spaces are ignored, and are useful for readability to segment long patterns. The 
rightmost character in the expression corresponds to the lowest numbered physical 
channel. For example, XXXX XXXX XXXX 1111 1100
specifies to match when channels 0 and 1 are '0' and channels 2-7 are '1'. 
The values seen by pattern matching are 
affected by [NIHSDIO_ATTR_DATA_INTERPRETATION](nihsdio_attr_data_interpretation.html).

#### Related topics:

- Triggers Summary
- Pattern-Match Trigger
- Dynamic Acquisition Triggers and Events

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_ready_for_start_event_level_active_level.html language=enus -->
## TOPIC 00048: NIHSDIO_ATTR_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_ready_for_start_event_level_active_level.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_ready_for_start_event_level_active_level.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | None |

#### Description

Specifies the output polarity of the [Ready 
for Start](/csh?topicname=hsdio/fevents_hsdi.html) event.

#### Defined Values:

| NIHSDIO_VAL_ACTIVE_HIGH (10) | The exported signal is low level while the event is deasserted. A high pulse occurs when the event asserts. This attribute does not apply to other exported signals. |
| --- | --- |
| NIHSDIO_VAL_ACTIVE_LOW (11) | The exported signal is high level while the event is deasserted. A low pulse occurs when the event asserts. This attribute does not apply to other exported signals. |

#### Related topics:

- Events Summary

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_ready_for_start_event_output_terminal.html language=enus -->
## TOPIC 00049: NIHSDIO_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_ready_for_start_event_output_terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_ready_for_start_event_output_terminal.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niHSDIO_ExportSignal |

#### Description

Specifies the destination terminal for the [Ready for Start](/csh?topicname=hsdio/fevents_hsdi.html) event. Event voltages and positions are only relevant if the destination of the event is a front panel connector.

#### Defined Values:

| NIHSDIO_VAL_DO_NOT_EXPORT_STR ("None") | The signal is not exported. |
| --- | --- |
| NIHSDIO_VAL_PFI0_STR ("PFI0") | PFI 0 front panel connector. |
| NIHSDIO_VAL_PFI1_STR ("PFI1") | PFI 1 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI2_STR ("PFI2") | PFI 2 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI3_STR ("PFI3") | PFI 3 on the front panel DDC connector. |
| NIHSDIO_VAL_PFI24_STR ("PFI24") | PFI 24 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI25_STR ("PFI25") | PFI 25 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI26_STR ("PFI26") | PFI 26 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI27_STR ("PFI27") | PFI 27 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI28_STR ("PFI28") | PFI 28 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI29_STR ("PFI29") | PFI 29 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI30_STR ("PFI30") | PFI 30 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PFI31_STR ("PFI31") | PFI 31 on the front panel DDC connector. This selection is available only for NI 6555/6556 devices. |
| NIHSDIO_VAL_PXI_TRIG0_STR ("PXI_Trig0") | PXI trigger line 0. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG1_STR ("PXI_Trig1") | PXI trigger line 1. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG2_STR ("PXI_Trig2") | PXI trigger line 2. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG3_STR ("PXI_Trig3") | PXI trigger line 3. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG4_STR ("PXI_Trig4") | PXI trigger line 4. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG5_STR ("PXI_Trig5") | PXI trigger line 5. (PXI devices) |
| NIHSDIO_VAL_PXI_TRIG6_STR ("PXI_Trig6") | PXI trigger line 6. (PXI devices) |
| NIHSDIO_VAL_RTSI0_STR ("RTSI0") | RTSI trigger line 0. (PCI devices) |
| NIHSDIO_VAL_RTSI1_STR ("RTSI1") | RTSI trigger line 1. (PCI devices) |
| NIHSDIO_VAL_RTSI2_STR ("RTSI2") | RTSI trigger line 2. (PCI devices) |
| NIHSDIO_VAL_RTSI3_STR ("RTSI3") | RTSI trigger line 3. (PCI devices) |
| NIHSDIO_VAL_RTSI4_STR ("RTSI4") | RTSI trigger line 4. (PCI devices) |
| NIHSDIO_VAL_RTSI5_STR ("RTSI5") | RTSI trigger line 5. (PCI devices) |
| NIHSDIO_VAL_RTSI6_STR ("RTSI6") | RTSI trigger line 6. (PCI devices) |

#### Related topics:

- Events Summary

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_ref_clock_impedance.html language=enus -->
## TOPIC 00050: NIHSDIO_ATTR_REF_CLOCK_IMPEDANCE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_ref_clock_impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_ref_clock_impedance.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_REF_CLOCK_IMPEDANCE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Specifies the input impedance of the Reference clock when it is 
supplied through the CLK IN front panel connector. Valid values are 50 or 1000.

**Units:** ohms

#### Related topics:

- Reference Clock
- Input Impedance

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_ref_clock_rate.html language=enus -->
## TOPIC 00051: NIHSDIO_ATTR_REF_CLOCK_RATE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_ref_clock_rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_ref_clock_rate.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_REF_CLOCK_RATE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | niHSDIO_ConfigureRefClock |

#### Description

Use this attribute to specify the
[Reference clock](/csh?topicname=hsdio/fref_clock.html) rate. Rate is expresses in Hertz. This attribute is 
ignored when the [NIHSDIO_ATTR_REF_CLOCK_SOURCE](nihsdio_attr_ref_clock_source.html) attribute
is set to None.

|  | Note Valid values for NI 6544/6545/6547/6548/6555/6556 devices are from 5 MHz to 100 MHz in 1 MHz steps. All other high-speed digital devices support only 10 MHz as a valid value. |
| --- | --- |

**Units:** hertz

#### Related topics:

- Reference Clock

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_ref_clock_source.html language=enus -->
## TOPIC 00052: NIHSDIO_ATTR_REF_CLOCK_SOURCE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_ref_clock_source.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_ref_clock_source.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_REF_CLOCK_SOURCE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | R/W | N/A | None | niHSDIO_ConfigureRefClock |

#### Description

Use this attribute to specify the [Reference clock](/csh?topicname=hsdio/fref_clock.html) source.

#### Defined Values:

| NIHSDIO_VAL_NONE_STR ("None") | The device does not use a Reference clock. |
| --- | --- |
| NIHSDIO_VAL_CLK_IN_STR ("ClkIn") | The device uses the clock present at the front panel CLK IN SMB jack connector. |
| NIHSDIO_VAL_PXI_CLK_STR ("PXI_CLK") | The device chooses between the PXI_CLK10 and PXIe_CLK100 signals, which are present on the backplane. |
| NIHSDIO_VAL_RTSI7_STR ("RTSI7") | The device uses RTSI trigger line 7. This selection is valid only for PCI devices. |
| NIHSDIO_VAL_DSTARA_STR ("PXIe_DStarA") | The device uses the PXIe_DStarA signal present on the PXI Express backplane as the Sample clock source. This selection is valid only for NI 6555/6556 devices. |

#### Related topics:

- Reference Clock

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_ref_to_ref_trigger_holdoff.html language=enus -->
## TOPIC 00053: NIHSDIO_ATTR_REF_TO_REF_TRIGGER_HOLDOFF

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_ref_to_ref_trigger_holdoff.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_ref_to_ref_trigger_holdoff.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_REF_TO_REF_TRIGGER_HOLDOFF

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViReal64 | R/W | N/A | None | None |

#### Description

Use this attribute to specify the amount of time until the next record's 
Reference trigger can be recognized. If the posttrigger time of the current 
record plus the pretrigger time of the next record (posttrigger record *n* + 
pretrigger record *n+1* / frequency) is greater than this attribute, then 
the holdoff value is ignored.

This attribute is especially useful when you want each device in a 
multidevice situation to recognize the Reference trigger at the same time,
though the Reference trigger is shared among devices and each device 
has a different record size.

**Units:** seconds

#### Related topics:

- Triggers Summary
- Reference Clock

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_ref_trigger_pretrigger_samples.html language=enus -->
## TOPIC 00054: NIHSDIO_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLES

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_ref_trigger_pretrigger_samples.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_ref_trigger_pretrigger_samples.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLES

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niHSDIO_ConfigureDigitalEdgeRefTrigger niHSDIO_ConfigurePatternMatchRefTrigger niHSDIO_ConfigureSoftwareRefTrigger |

#### Description

Specifies the number of pretrigger samples to be acquired per record 
(for example, the samples acquired before the [Reference trigger](/csh?topicname=hsdio/ftriggers_hsdi.html) is received). The number of 
pretrigger samples cannot be greater than the value of [NIHSDIO_ATTR_SAMPLES_PER_RECORD](nihsdio_attr_samples_per_record.html).

This attribute is valid only for acquisition sessions.

#### Related topics:

- Triggers Summary
- Reference Clock

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_ref_trigger_type.html language=enus -->
## TOPIC 00055: NIHSDIO_ATTR_REF_TRIGGER_TYPE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_ref_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_ref_trigger_type.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_REF_TRIGGER_TYPE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niHSDIO_ConfigureDigitalEdgeRefTrigger niHSDIO_ConfigurePatternMatchRefTrigger niHSDIO_ConfigureSoftwareRefTrigger niHSDIO_DisableRefTrigger |

#### Description

Specifies the [Reference trigger](/csh?topicname=hsdio/ftriggers_hsdi.html) type. Depending on this attribute value, you may need to set more attributes to fully configure the trigger.

This attribute is valid only for acquisition sessions.

#### Defined Values:

| NIHSDIO_VAL_NONE (28) | The acquisition operation does not have a Reference trigger. The data operation starts immediately after you call niHSDIO_Initiate and after the Start trigger, if configured, asserts. |
| --- | --- |
| NIHSDIO_VAL_DIGITAL_EDGE (29) | The Reference trigger asserts when a digital edge is detected. The source of the digital edge is specified with NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE, and the active edge is specified with NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_EDGE. |
| NIHSDIO_VAL_SOFTWARE (32) | The Reference trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling niHSDIO_SendSoftwareEdgeTrigger with NIHSDIO_VAL_REF_TRIGGER as the trigger name. |
| NIHSDIO_VAL_PATTERN_MATCH (31) | The Reference trigger is asserted when a specific data pattern matching condition is met. Configure the condition by setting NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_PATTERN and NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_WHEN. This is valid only for acquisition sessions. |

#### Related topics:

- Triggers Summary
- Reference Clock

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_serial_number.html language=enus -->
## TOPIC 00056: NIHSDIO_ATTR_SERIAL_NUMBER

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_serial_number.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_serial_number.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_SERIAL_NUMBER

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViString | RO | None | None | None |

#### Description

Returns the device serial number.

#### Related topics:

- NI-ModInst Overview

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_space_available_in_streaming_waveform.html language=enus -->
## TOPIC 00057: NIHSDIO_ATTR_SPACE_AVAILABLE_IN_STREAMING_WAVEFORM

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_space_available_in_streaming_waveform.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_space_available_in_streaming_waveform.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_SPACE_AVAILABLE_IN_STREAMING_WAVEFORM

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Specifies the space available (in samples) in the streaming waveform for writing new data.

This attribute is valid only when streaming.

#### Related topics:

- Generating Waveforms Using Streaming

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_stop_trigger_type.html language=enus -->
## TOPIC 00058: NIHSDIO_ATTR_STOP_TRIGGER_TYPE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_stop_trigger_type.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_stop_trigger_type.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_STOP_TRIGGER_TYPE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | R/W | N/A | None | niHSDIO_ConfigureDigitalEdgeStopTrigger niHSDIO_ConfigureSoftwareStopTrigger niHSDIO_DisableStopTrigger |

#### Description

Use this attribute to specify whether you want the 
[Stop trigger](/csh?topicname=hsdio/ftriggers_hsdi.html) to be a [digital edge](/csh?topicname=hsdio/fedge_trigger.html) or [software trigger](/csh?topicname=hsdio/fsoftware_trigger.html). You can also choose NIHSDIO_VAL_NONE as the value for this attribute. This attribute is valid only for generation sessions.

#### Defined Values:

| NIHSDIO_VAL_NONE (28) | The data operation does not stop. |
| --- | --- |
| NIHSDIO_VAL_DIGITAL_EDGE (29) | The data operation does not stop until a digital edge is detected. The source of the digital edge is specified with NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_SOURCE, and the active edge is specified with NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_EDGE. |
| NIHSDIO_VAL_SOFTWARE (32) | The data operation does not stop until a software trigger occurs. You can assert the software trigger by calling niHSDIO_SendSoftwareEdgeTrigger with NIHSDIO_VAL_STOP_TRIGGER as the trigger name. |

#### Related topics:

- Triggers Summary

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_streaming_enabled.html language=enus -->
## TOPIC 00059: NIHSDIO_ATTR_STREAMING_ENABLED

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_streaming_enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_streaming_enabled.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_STREAMING_ENABLED

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViBoolean | R/W | N/A | None | None |

#### Description

Enables streaming of data from host memory to the device.

This attribute is valid only for dynamic generation sessions.

#### Related topics:

- Generating Waveforms Using Streaming

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attr_total_generation_memory_size.html language=enus -->
## TOPIC 00060: NIHSDIO_ATTR_TOTAL_GENERATION_MEMORY_SIZE

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attr_total_generation_memory_size.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attr_total_generation_memory_size.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NIHSDIO_ATTR_TOTAL_GENERATION_MEMORY_SIZE

#### Specific Attribute

| Datatype | Access | Applies to | Coercion | High-Level Functions |
| --- | --- | --- | --- | --- |
| ViInt32 | RO | N/A | None | None |

#### Description

Returns the total 
[onboard memory](/csh?topicname=hsdio/fonboard_memory.html) size, in samples, 
for generating data. The number of samples is based on the default 
device data width.

If you configure your device to use a different data width, the total 
memory size is actually the value returned by this attribute multiplied 
by the quotient of the default data width divided by the configured data 
width. For example, if you configure 1-byte data width for a 2-byte 
device, the total generation memory size is twice the number of samples 
that is returned by this attribute.

**Units:** samples

#### Related topics:

- Generating Waveforms Using Streaming

<!--NI_TOPIC bundle=ni-hsdio-c-api-ref path=hsdiocref/nihsdio_attributes.html language=enus -->
## TOPIC 00061: NI-HSDIO Attributes

- bundle_id: `ni-hsdio-c-api-ref`
- source_path: `hsdiocref/nihsdio_attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-hsdio-c-api-ref/raw/resource/enus/hsdiocref/nihsdio_attributes.html
- document_id: `ni-hsdio-c-api-ref`
- page_type: `leaf`
- content_type: ``

### NI-HSDIO Attributes

| Group/Attribute Name | Attribute Label |
| --- | --- |
| Dynamic Channels | NIHSDIO_ATTR_DYNAMIC_CHANNELS |
| Static Channels | NIHSDIO_ATTR_STATIC_CHANNELS |
| Voltage Levels |  |
| Data High | NIHSDIO_ATTR_DATA_VOLTAGE_HIGH_LEVEL |
| Data Low | NIHSDIO_ATTR_DATA_VOLTAGE_LOW_LEVEL |
| Trigger High | NIHSDIO_ATTR_TRIGGER_VOLTAGE_HIGH_LEVEL |
| Trigger Low | NIHSDIO_ATTR_TRIGGER_VOLTAGE_LOW_LEVEL |
| Event High | NIHSDIO_ATTR_EVENT_VOLTAGE_HIGH_LEVEL |
| Event Low | NIHSDIO_ATTR_EVENT_VOLTAGE_LOW_LEVEL |
| Clock High | NIHSDIO_ATTR_CLOCK_VOLTAGE_HIGH_LEVEL |
| Clock Low | NIHSDIO_ATTR_CLOCK_VOLTAGE_LOW_LEVEL |
| Voltage Range |  |
| Data Voltage Range | NIHSDIO_ATTR_DATA_VOLTAGE_RANGE |
| Trigger Voltage Range | NIHSDIO_ATTR_TRIGGER_VOLTAGE_RANGE |
| Event Voltage Range | NIHSDIO_ATTR_EVENT_VOLTAGE_RANGE |
| Clock Voltage Range | NIHSDIO_ATTR_CLOCK_VOLTAGE_RANGE |
| Dynamic Acquisition |  |
| Samples Per Record | NIHSDIO_ATTR_SAMPLES_PER_RECORD |
| Number Of Records To Acquire | NIHSDIO_ATTR_NUM_RECORDS |
| Input Impedance | NIHSDIO_ATTR_INPUT_IMPEDANCE |
| Data Interpretation | NIHSDIO_ATTR_DATA_INTERPRETATION |
| Termination Mode | NIHSDIO_ATTR_DATA_TERMINATION_MODE |
| Fetch |  |
| Fetch Relative To | NIHSDIO_ATTR_FETCH_RELATIVE_TO |
| Fetch Offset | NIHSDIO_ATTR_FETCH_OFFSET |
| Fetch Backlog | NIHSDIO_ATTR_FETCH_BACKLOG |
| Records Done | NIHSDIO_ATTR_RECORDS_DONE |
| Dynamic Generation |  |
| Initial State | NIHSDIO_ATTR_INITIAL_STATE |
| Idle State | NIHSDIO_ATTR_IDLE_STATE |
| Drive Type | NIHSDIO_ATTR_DRIVE_TYPE |
| Tristate Mode | NIHSDIO_ATTR_DATA_TRISTATE_MODE |
| Repeat Mode | NIHSDIO_ATTR_REPEAT_MODE |
| Repeat Count | NIHSDIO_ATTR_REPEAT_COUNT |
| Generation Mode | NIHSDIO_ATTR_GENERATION_MODE |
| Waveform To Generate | NIHSDIO_ATTR_WAVEFORM_TO_GENERATE |
| Script To Generate | NIHSDIO_ATTR_SCRIPT_TO_GENERATE |
| Timing |  |
| Sample Clock |  |
| Rate | NIHSDIO_ATTR_SAMPLE_CLOCK_RATE |
| Source | NIHSDIO_ATTR_SAMPLE_CLOCK_SOURCE |
| Impedance | NIHSDIO_ATTR_SAMPLE_CLOCK_IMPEDANCE |
| Exported Sample Clock Output Terminal | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL |
| Exported Sample Clock Mode | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_MODE |
| Exported Sample Clock Delay | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_DELAY |
| Ref Clock |  |
| Rate | NIHSDIO_ATTR_REF_CLOCK_RATE |
| Source | NIHSDIO_ATTR_REF_CLOCK_SOURCE |
| Impedance | NIHSDIO_ATTR_REF_CLOCK_IMPEDANCE |
| Export Output Terminal | NIHSDIO_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL |
| Onboard Ref Clock |  |
| Export Output Terminal | NIHSDIO_ATTR_EXPORTED_ONBOARD_REF_CLOCK_OUTPUT_TERMINAL |
| Data Position |  |
| Position | NIHSDIO_ATTR_DATA_POSITION |
| Delay | NIHSDIO_ATTR_DATA_POSITION_DELAY |
| Deskew | NIHSDIO_ATTR_DATA_DESKEW |
| Trigger Delay | NIHSDIO_ATTR_TRIGGER_POSITION_DELAY |
| Trigger Deskew | NIHSDIO_ATTR_TRIGGER_DESKEW |
| Event Delay | NIHSDIO_ATTR_EVENT_POSITION_DELAY |
| Event Deskew | NIHSDIO_ATTR_EVENT_DESKEW |
| Advanced |  |
| Oscillator Phase DAC Value | NIHSDIO_ATTR_OSCILLATOR_PHASE_DAC_VALUE |
| Exported Sample Clock Offset | NIHSDIO_ATTR_EXPORTED_SAMPLE_CLOCK_OFFSET |
| Triggers |  |
| Start Trigger |  |
| Type | NIHSDIO_ATTR_START_TRIGGER_TYPE |
| Digital Edge Source | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE |
| Digital Edge Edge | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE |
| Position | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_POSITION |
| Digital Edge Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_START_TRIGGER_IMPEDANCE |
| Pattern Match Pattern | NIHSDIO_ATTR_PATTERN_MATCH_START_TRIGGER_PATTERN |
| Pattern Match Trigger When | NIHSDIO_ATTR_PATTERN_MATCH_START_TRIGGER_WHEN |
| Export Output Terminal | NIHSDIO_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL |
| Export Terminal Configuration | NIHSDIO_ATTR_EXPORTED_START_TRIGGER_TERMINAL_CONFIGURATION |
| Ref Trigger |  |
| Ref Trigger Type | NIHSDIO_ATTR_REF_TRIGGER_TYPE |
| Pretrigger Samples Per Record | NIHSDIO_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLES |
| Digital Edge Source | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE |
| Digital Edge Edge | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_EDGE |
| Position | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_POSITION |
| Digital Edge Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_IMPEDANCE |
| Digital Edge Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_REF_TRIGGER_TERMINAL_CONFIGURATION |
| Pattern Match Pattern | NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_PATTERN |
| Pattern Match Trigger When | NIHSDIO_ATTR_PATTERN_MATCH_REF_TRIGGER_WHEN |
| Export Output Terminal | NIHSDIO_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL |
| Export Terminal Configuration | NIHSDIO_ATTR_EXPORTED_REF_TRIGGER_TERMINAL_CONFIGURATION |
| Start to Reference Trigger Holdoff | NIHSDIO_ATTR_START_TO_REF_TRIGGER_HOLDOFF |
| Reference to Reference Trigger Holdoff | NIHSDIO_ATTR_REF_TO_REF_TRIGGER_HOLDOFF |
| Advance Trigger |  |
| Type | NIHSDIO_ATTR_ADVANCE_TRIGGER_TYPE |
| Digital Edge Source | NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE |
| Digital Edge Edge | NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_EDGE |
| Digital Edge Position | NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_POSITION |
| Digital Edge Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_IMPEDANCE |
| Pattern Match Pattern | NIHSDIO_ATTR_PATTERN_MATCH_ADVANCE_TRIGGER_PATTERN |
| Pattern Match Trigger When | NIHSDIO_ATTR_PATTERN_MATCH_ADVANCE_TRIGGER_WHEN |
| Export Output Terminal | NIHSDIO_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL |
| Export Terminal Configuration | NIHSDIO_ATTR_EXPORTED_ADVANCE_TRIGGER_TERMINAL_CONFIGURATION |
| Script Trigger |  |
| Type | NIHSDIO_ATTR_SCRIPT_TRIGGER_TYPE |
| Digital Edge Source | NIHSDIO_ATTR_SCRIPT_TRIGGER_SOURCE |
| Digital Edge Edge | NIHSDIO_ATTR_SCRIPT_TRIGGER_EDGE |
| Digital Edge Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Edge Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_IMPEDANCE |
| Digital Level Source | NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE |
| Digital Level Level | NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_WHEN |
| Digital Level Terminal Configuration | NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Level Impedance | NIHSDIO_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_IMPEDANCE |
| Export Output Terminal | NIHSDIO_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL |
| Export Terminal Configuration | NIHSDIO_ATTR_EXPORTED_SCRIPT_TRIGGER_TERMINAL_CONFIGURATION |
| Pause Trigger |  |
| Type | NIHSDIO_ATTR_PAUSE_TRIGGER_TYPE |
| Digital Level Source | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_SOURCE |
| Digital Level Level | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_WHEN |
| Digital Level Position | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_POSITION |
| Digital Level Terminal Configuration | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_TERMINAL_CONFIGURATION |
| Digital Level Impedance | NIHSDIO_ATTR_DIGITAL_LEVEL_PAUSE_TRIGGER_IMPEDANCE |
| Pattern Match Pattern | NIHSDIO_ATTR_PATTERN_MATCH_PAUSE_TRIGGER_PATTERN |
| Pattern Match Trigger When | NIHSDIO_ATTR_PATTERN_MATCH_PAUSE_TRIGGER_WHEN |
| Export Output Terminal | NIHSDIO_ATTR_EXPORTED_PAUSE_TRIGGER_OUTPUT_TERMINAL |
| Export Terminal Configuration | NIHSDIO_ATTR_EXPORTED_PAUSE_TRIGGER_TERMINAL_CONFIGURATION |
| Stop Trigger |  |
| Type | NIHSDIO_ATTR_STOP_TRIGGER_TYPE |
| Digital Edge Edge | NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_EDGE |
| Digital Edge Impedance | NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_IMPEDANCE |
| Digital Edge Source | NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_SOURCE |
| Digital Edge Terminal Configuration | NIHSDIO_ATTR_DIGITAL_EDGE_STOP_TRIGGER_TERMINAL_CONFIGURATION |
| Export Output Terminal | NIHSDIO_ATTR_EXPORTED_STOP_TRIGGER_OUTPUT_TERMINAL |
| Export Terminal Configuration | NIHSDIO_ATTR_EXPORTED_STOP_TRIGGER_TERMINAL_CONFIGURATION |
| Events |  |
| Ready For Start Event |  |
| Output Terminal | NIHSDIO_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL |
| Active Level | NIHSDIO_ATTR_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL |
| Terminal Configuration | NIHSDIO_ATTR_READY_FOR_START_EVENT_TERMINAL_CONFIGURATION |
| Ready For Advance Event |  |
| Output Terminal | NIHSDIO_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL |
| Active Level | NIHSDIO_ATTR_READY_FOR_ADVANCE_EVENT_LEVEL_ACTIVE_LEVEL |
| Terminal Configuration | NIHSDIO_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_CONFIGURATION |
| End Of Record Event |  |
| Output Terminal | NIHSDIO_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL |
| Pulse Polarity | NIHSDIO_ATTR_END_OF_RECORD_EVENT_PULSE_POLARITY |
| Terminal Configuration | NIHSDIO_ATTR_END_OF_RECORD_EVENT_TERMINAL_CONFIGURATION |
| Data Active Event |  |
| Output Terminal | NIHSDIO_ATTR_DATA_ACTIVE_EVENT_OUTPUT_TERMINAL |
| Active Level | NIHSDIO_ATTR_DATA_ACTIVE_EVENT_LEVEL_ACTIVE_LEVEL |
| Position | NIHSDIO_ATTR_DATA_ACTIVE_EVENT_POSITION |
| Terminal Configuration | NIHSDIO_ATTR_DATA_ACTIVE_EVENT_TERMINAL_CONFIGURATION |
| Marker Event |  |
| Output Terminal | NIHSDIO_ATTR_MARKER_EVENT_OUTPUT_TERMINAL |
| Pulse Polarity | NIHSDIO_ATTR_MARKER_EVENT_PULSE_POLARITY |
| Position | NIHSDIO_ATTR_MARKER_EVENT_POSITION |
| Terminal Configuration | NIHSDIO_ATTR_MARKER_EVENT_TERMINAL_CONFIGURATION |
| Device Characteristics |  |
| Total Acquisition Memory Size | NIHSDIO_ATTR_TOTAL_ACQUISITION_MEMORY_SIZE |
| Total Generation Memory Size | NIHSDIO_ATTR_TOTAL_GENERATION_MEMORY_SIZE |
| Serial Number | NIHSDIO_ATTR_SERIAL_NUMBER |
| Advanced |  |
| Data Width | NIHSDIO_ATTR_DATA_WIDTH |
| Data Rate Multiplier | NIHSDIO_ATTR_DATA_RATE_MULTIPLIER |
| Data Active Internal Route Delay | NIHSDIO_ATTR_DATA_ACTIVE_INTERNAL_ROUTE_DELAY |
| Supported Data States | NIHSDIO_ATTR_SUPPORTED_DATA_STATES |
| Device |  |
| Power Consumption | NIHSDIO_ATTR_DEVICE_POWER_CONSUMPTION |
| Peak Power Consumed | NIHSDIO_ATTR_DEVICE_PEAK_POWER_CONSUMED |
| PPMU-Capable I/O Switch | NIHSDIO_ATTR_PPMU_CAPABLE_IO_SWITCH_CONTROL |
