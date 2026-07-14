# NI DOCUMENT BUNDLE: ni-daqmx-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-c-api-ref start=2001 end=2250 -->
<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__input__timing_1gab508f152f1cc0a6a9069c3e15c409502.html language=enus -->
## TOPIC 02001: DAQmx_Dev_CI_SampModes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__input__timing_1gab508f152f1cc0a6a9069c3e15c409502.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__input__timing_1gab508f152f1cc0a6a9069c3e15c409502.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CI_SampModesRemarksData TypeDescriptionRestrictionsint32*Indicates sample modes supported by devices that support sample clocked counter input.Not SettableValid valuesDAQmx_Val_FiniteSamps10178Acquire or generate a finite number of samples.DAQmx_Val_ContSamps10123Acquire or generate

### DAQmx_Dev_CI_SampModes

#### Syntax

DAQmx_Dev_CI_SampModes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32* | Indicates sample modes supported by devices that support sample clocked counter input. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_FiniteSamps | 10178 | Acquire or generate a finite number of samples. |
| DAQmx_Val_ContSamps | 10123 | Acquire or generate samples until you stop the task. |
| DAQmx_Val_HWTimedSinglePoint | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

You can get this property using:

- [DAQmxGetDevCISampModes](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf206070b316047570503be02ad8b47fb.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__input__timing_1gaf6822b6bde3713a3920b58899ba03f7c.html language=enus -->
## TOPIC 02002: DAQmx_Dev_CI_MaxSize

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__input__timing_1gaf6822b6bde3713a3920b58899ba03f7c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__input__timing_1gaf6822b6bde3713a3920b58899ba03f7c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CI_MaxSizeRemarksData TypeDescriptionRestrictionsuInt32Indicates in bits the size of the counters on the device.Not SettableYou can get this property using:DAQmxGetDevCIMaxSize

### DAQmx_Dev_CI_MaxSize

#### Syntax

DAQmx_Dev_CI_MaxSize

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates in bits the size of the counters on the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevCIMaxSize](group__ni-daqmx__c__functions__property__manipulation__getter_1ga3d025153b99611bb109db1aed2172b0f.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__input__trigger.html language=enus -->
## TOPIC 02003: Trigger

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__input__trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__input__trigger.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_CI_TrigUsageAttachmentsNone

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_CI_TrigUsage |  |

#### Attachments

None

Parent topic:

Counter Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__input__trigger_1ga3f6d57438da45ee2b41a4d4918c7c860.html language=enus -->
## TOPIC 02004: DAQmx_Dev_CI_TrigUsage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__input__trigger_1ga3f6d57438da45ee2b41a4d4918c7c860.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__input__trigger_1ga3f6d57438da45ee2b41a4d4918c7c860.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CI_TrigUsageRemarksData TypeDescriptionRestrictionsint32Indicates the triggers supported by this device for counter input tasks.Not SettableValid valuesDAQmx_Val_Bit_TriggerUsageTypes_Advance1Device supports advance triggersDAQmx_Val_Bit_TriggerUsageTypes_Pause2Device supports pause

### DAQmx_Dev_CI_TrigUsage

#### Syntax

DAQmx_Dev_CI_TrigUsage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the triggers supported by this device for counter input tasks. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Bit_TriggerUsageTypes_Advance | 1 | Device supports advance triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_Pause | 2 | Device supports pause triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_Reference | 4 | Device supports reference triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_Start | 8 | Device supports start triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_Handshake | 16 | Device supports handshake triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_ArmStart | 32 | Device supports arm start triggers |

You can get this property using:

- [DAQmxGetDevCITrigUsage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga729f6538135b744c71a7345122ba7c6d.html)

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__output.html language=enus -->
## TOPIC 02005: Counter Output

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__output.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__output.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimingTriggerGroup membersNameDescriptionDAQmx_Dev_CO_PhysicalChansDAQmx_Dev_CO_SupportedOutputTypesAttachmentsNone

### Counter Output

#### Groups

- Timing
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_CO_PhysicalChans |  |
| DAQmx_Dev_CO_SupportedOutputTypes |  |

#### Attachments

None

Parent topic:

I/O Type

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__output__timing.html language=enus -->
## TOPIC 02006: Timing

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__output__timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__output__timing.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_CO_SampClkSupportedDAQmx_Dev_CO_SampModesAttachmentsNone

### Timing

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_CO_SampClkSupported |  |
| DAQmx_Dev_CO_SampModes |  |

#### Attachments

None

Parent topic:

Counter Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__output__timing_1gab7d9879f23ac13dcc34e9a9a812ecbc7.html language=enus -->
## TOPIC 02007: DAQmx_Dev_CO_SampModes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__output__timing_1gab7d9879f23ac13dcc34e9a9a812ecbc7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__output__timing_1gab7d9879f23ac13dcc34e9a9a812ecbc7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CO_SampModesRemarksData TypeDescriptionRestrictionsint32*Indicates sample modes supported by devices that support sample clocked counter output.Not SettableValid valuesDAQmx_Val_FiniteSamps10178Acquire or generate a finite number of samples.DAQmx_Val_ContSamps10123Acquire or generate

### DAQmx_Dev_CO_SampModes

#### Syntax

DAQmx_Dev_CO_SampModes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32* | Indicates sample modes supported by devices that support sample clocked counter output. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_FiniteSamps | 10178 | Acquire or generate a finite number of samples. |
| DAQmx_Val_ContSamps | 10123 | Acquire or generate samples until you stop the task. |
| DAQmx_Val_HWTimedSinglePoint | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

You can get this property using:

- [DAQmxGetDevCOSampModes](group__ni-daqmx__c__functions__property__manipulation__getter_1ga885f4c0f60f524b161efa4e54178d0bf.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger.html language=enus -->
## TOPIC 02008: Trigger

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_CO_MaxSizeDAQmx_Dev_CO_MaxTimebaseDAQmx_Dev_CO_TrigUsageAttachmentsNone

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_CO_MaxSize |  |
| DAQmx_Dev_CO_MaxTimebase |  |
| DAQmx_Dev_CO_TrigUsage |  |

#### Attachments

None

Parent topic:

Counter Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger_1ga9d42e78aa3941487549ccaedf6332503.html language=enus -->
## TOPIC 02009: DAQmx_Dev_CO_MaxTimebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger_1ga9d42e78aa3941487549ccaedf6332503.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger_1ga9d42e78aa3941487549ccaedf6332503.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CO_MaxTimebaseRemarksData TypeDescriptionRestrictionsfloat64Indicates in hertz the maximum counter timebase frequency.Not SettableYou can get this property using:DAQmxGetDevCOMaxTimebase

### DAQmx_Dev_CO_MaxTimebase

#### Syntax

DAQmx_Dev_CO_MaxTimebase

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Indicates in hertz the maximum counter timebase frequency. | Not Settable |

You can get this property using:

- [DAQmxGetDevCOMaxTimebase](group__ni-daqmx__c__functions__property__manipulation__getter_1ga339b63dfe4b766a9f4c735647233f332.html)

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger_1gab3b3080a68c3f13eb13f19e472659b4b.html language=enus -->
## TOPIC 02010: DAQmx_Dev_CO_MaxSize

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger_1gab3b3080a68c3f13eb13f19e472659b4b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__counter__output__trigger_1gab3b3080a68c3f13eb13f19e472659b4b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CO_MaxSizeRemarksData TypeDescriptionRestrictionsuInt32Indicates in bits the size of the counters on the device.Not SettableYou can get this property using:DAQmxGetDevCOMaxSize

### DAQmx_Dev_CO_MaxSize

#### Syntax

DAQmx_Dev_CO_MaxSize

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates in bits the size of the counters on the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevCOMaxSize](group__ni-daqmx__c__functions__property__manipulation__getter_1ga273b163c0beed6f1e94a59bea03c874d.html)

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__input.html language=enus -->
## TOPIC 02011: Digital Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimingTriggerGroup membersNameDescriptionDAQmx_Dev_DI_LinesDAQmx_Dev_DI_PortsAttachmentsNone

### Digital Input

#### Groups

- Timing
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_DI_Lines |  |
| DAQmx_Dev_DI_Ports |  |

#### Attachments

None

Parent topic:

I/O Type

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__input_1gae816e0be5f39dd57ff659b56747fb28a.html language=enus -->
## TOPIC 02012: DAQmx_Dev_DI_Lines

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__input_1gae816e0be5f39dd57ff659b56747fb28a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__input_1gae816e0be5f39dd57ff659b56747fb28a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_DI_LinesRemarksData TypeDescriptionRestrictionschar*Indicates an array containing the names of the digital input lines available on the device.Not SettableYou can get this property using:DAQmxGetDevDILines

### DAQmx_Dev_DI_Lines

#### Syntax

DAQmx_Dev_DI_Lines

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates an array containing the names of the digital input lines available on the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevDILines](group__ni-daqmx__c__functions__property__manipulation__getter_1ga29aae10cd709b30acb917d712ecb019d.html)

Parent topic:

Digital Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__input__timing_1ga01652eb74eda7a3787f606721c5afd9c.html language=enus -->
## TOPIC 02013: DAQmx_Dev_DI_NumSampTimingEngines

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__input__timing_1ga01652eb74eda7a3787f606721c5afd9c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__input__timing_1ga01652eb74eda7a3787f606721c5afd9c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_DI_NumSampTimingEnginesRemarksData TypeDescriptionRestrictionsuInt32Indicates the number of Digital Input sample timing engines supported by the device.Not SettableYou can get this property using:DAQmxGetDevDINumSampTimingEngines

### DAQmx_Dev_DI_NumSampTimingEngines

#### Syntax

DAQmx_Dev_DI_NumSampTimingEngines

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the number of Digital Input sample timing engines supported by the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevDINumSampTimingEngines](group__ni-daqmx__c__functions__property__manipulation__getter_1gacc1ca40f9f2cdf2b0b98d2c0c8f7fe5c.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__input__timing_1ga630a45273053aa2d6bbf4eed716bca4c.html language=enus -->
## TOPIC 02014: DAQmx_Dev_DI_MaxRate

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__input__timing_1ga630a45273053aa2d6bbf4eed716bca4c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__input__timing_1ga630a45273053aa2d6bbf4eed716bca4c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_DI_MaxRateRemarksData TypeDescriptionRestrictionsfloat64Indicates the maximum digital input rate of the device.Not SettableYou can get this property using:DAQmxGetDevDIMaxRate

### DAQmx_Dev_DI_MaxRate

#### Syntax

DAQmx_Dev_DI_MaxRate

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Indicates the maximum digital input rate of the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevDIMaxRate](group__ni-daqmx__c__functions__property__manipulation__getter_1ga681d6d191fbc2625cc40d0505aee95bb.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__input__trigger.html language=enus -->
## TOPIC 02015: Trigger

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__input__trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__input__trigger.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_DI_TrigUsageAttachmentsNone

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_DI_TrigUsage |  |

#### Attachments

None

Parent topic:

Digital Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__output.html language=enus -->
## TOPIC 02016: Digital Output

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__output.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__output.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimingTriggerGroup membersNameDescriptionDAQmx_Dev_DO_LinesDAQmx_Dev_DO_PortsAttachmentsNone

### Digital Output

#### Groups

- Timing
- Trigger

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_DO_Lines |  |
| DAQmx_Dev_DO_Ports |  |

#### Attachments

None

Parent topic:

I/O Type

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__output_1ga007032104fc62f18ce0a377f006868e5.html language=enus -->
## TOPIC 02017: DAQmx_Dev_DO_Lines

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__output_1ga007032104fc62f18ce0a377f006868e5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__output_1ga007032104fc62f18ce0a377f006868e5.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_DO_LinesRemarksData TypeDescriptionRestrictionschar*Indicates an array containing the names of the digital output lines available on the device.Not SettableYou can get this property using:DAQmxGetDevDOLines

### DAQmx_Dev_DO_Lines

#### Syntax

DAQmx_Dev_DO_Lines

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates an array containing the names of the digital output lines available on the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevDOLines](group__ni-daqmx__c__functions__property__manipulation__getter_1gadad7e44930cf85bd0f1f5d33de7f3026.html)

Parent topic:

Digital Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__output__timing.html language=enus -->
## TOPIC 02018: Timing

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__output__timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__output__timing.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_DO_MaxRateDAQmx_Dev_DO_NumSampTimingEnginesAttachmentsNone

### Timing

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_DO_MaxRate |  |
| DAQmx_Dev_DO_NumSampTimingEngines |  |

#### Attachments

None

Parent topic:

Digital Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__output__timing_1gad58b6a4eb96bc88cbffae0e77a522695.html language=enus -->
## TOPIC 02019: DAQmx_Dev_DO_NumSampTimingEngines

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__output__timing_1gad58b6a4eb96bc88cbffae0e77a522695.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__output__timing_1gad58b6a4eb96bc88cbffae0e77a522695.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_DO_NumSampTimingEnginesRemarksData TypeDescriptionRestrictionsuInt32Indicates the number of Digital Output synchronization pulse sources supported by the device.Not SettableYou can get this property using:DAQmxGetDevDONumSampTimingEngines

### DAQmx_Dev_DO_NumSampTimingEngines

#### Syntax

DAQmx_Dev_DO_NumSampTimingEngines

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the number of Digital Output synchronization pulse sources supported by the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevDONumSampTimingEngines](group__ni-daqmx__c__functions__property__manipulation__getter_1gae12d96a19ec520e63475a82ed84caa1a.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__i__o__type__digital__output__trigger_1ga8ed6748ecc677ccf7e70bb5e20c17900.html language=enus -->
## TOPIC 02020: DAQmx_Dev_DO_TrigUsage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__i__o__type__digital__output__trigger_1ga8ed6748ecc677ccf7e70bb5e20c17900.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__i__o__type__digital__output__trigger_1ga8ed6748ecc677ccf7e70bb5e20c17900.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_DO_TrigUsageRemarksData TypeDescriptionRestrictionsint32Indicates the triggers supported by this device for digital output tasks.Not SettableValid valuesDAQmx_Val_Bit_TriggerUsageTypes_Advance1Device supports advance triggersDAQmx_Val_Bit_TriggerUsageTypes_Pause2Device supports pause

### DAQmx_Dev_DO_TrigUsage

#### Syntax

DAQmx_Dev_DO_TrigUsage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the triggers supported by this device for digital output tasks. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Bit_TriggerUsageTypes_Advance | 1 | Device supports advance triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_Pause | 2 | Device supports pause triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_Reference | 4 | Device supports reference triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_Start | 8 | Device supports start triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_Handshake | 16 | Device supports handshake triggers |
| DAQmx_Val_Bit_TriggerUsageTypes_ArmStart | 32 | Device supports arm start triggers |

You can get this property using:

- [DAQmxGetDevDOTrigUsage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga6cb16dba33e40bddd231994e6ccac29c.html)

Parent topic:

Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification.html language=enus -->
## TOPIC 02021: Identification

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAccessoryFieldDAQID PinGroup membersNameDescriptionDAQmx_Dev_ProductCategoryDAQmx_Dev_ProductNumDAQmx_Dev_ProductTypeDAQmx_Dev_SerialNumAttachmentsNone

### Identification

#### Groups

- Accessory
- FieldDAQ
- ID Pin

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_ProductCategory |  |
| DAQmx_Dev_ProductNum |  |
| DAQmx_Dev_ProductType |  |
| DAQmx_Dev_SerialNum |  |

#### Attachments

None

Parent topic:

Device

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification_1gadd0412d63cf12682ca7b51ae9ede94fa.html language=enus -->
## TOPIC 02022: DAQmx_Dev_ProductType

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification_1gadd0412d63cf12682ca7b51ae9ede94fa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification_1gadd0412d63cf12682ca7b51ae9ede94fa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_ProductTypeRemarksData TypeDescriptionRestrictionschar*Indicates the product name of the device.Not SettableYou can get this property using:DAQmxGetDevProductType

### DAQmx_Dev_ProductType

#### Syntax

DAQmx_Dev_ProductType

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the product name of the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevProductType](group__ni-daqmx__c__functions__property__manipulation__getter_1ga707f7097fa840dcbde5d06f3084f4827.html)

Parent topic:

Identification

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification_1gaea415fab5428b1aea9b7488dc09e8f58.html language=enus -->
## TOPIC 02023: DAQmx_Dev_SerialNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification_1gaea415fab5428b1aea9b7488dc09e8f58.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification_1gaea415fab5428b1aea9b7488dc09e8f58.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_SerialNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the serial number of the device. This value is zero if the device does not have a serial number.Not SettableYou can get this property using:DAQmxGetDevSerialNum

### DAQmx_Dev_SerialNum

#### Syntax

DAQmx_Dev_SerialNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the serial number of the device. This value is zero if the device does not have a serial number. | Not Settable |

You can get this property using:

- [DAQmxGetDevSerialNum](group__ni-daqmx__c__functions__property__manipulation__getter_1ga07435a6f23049b6add6caa2fad21a324.html)

Parent topic:

Identification

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__accessory_1ga57681375e52e94f796be7aecb5eff6c6.html language=enus -->
## TOPIC 02024: DAQmx_Dev_Accessory_ProductNums

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__accessory_1ga57681375e52e94f796be7aecb5eff6c6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__accessory_1ga57681375e52e94f796be7aecb5eff6c6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_Accessory_ProductNumsRemarksData TypeDescriptionRestrictionsuInt32*Indicates the unique hardware identification number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for eac

### DAQmx_Dev_Accessory_ProductNums

#### Syntax

DAQmx_Dev_Accessory_ProductNums

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32* | Indicates the unique hardware identification number for accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains 0 for each connector with no accessory connected. | Not Settable |

You can get this property using:

- [DAQmxGetDevAccessoryProductNums](group__ni-daqmx__c__functions__property__manipulation__getter_1gacefd4b6a4f2f90a14c7d485347d2f0c7.html)

Parent topic:

Accessory

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__accessory_1gafa88fd14709efa240f33091368aa7db2.html language=enus -->
## TOPIC 02025: DAQmx_Dev_Accessory_ProductTypes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__accessory_1gafa88fd14709efa240f33091368aa7db2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__accessory_1gafa88fd14709efa240f33091368aa7db2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_Accessory_ProductTypesRemarksData TypeDescriptionRestrictionschar*Indicates the model names of accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains an empty string for each connector wi

### DAQmx_Dev_Accessory_ProductTypes

#### Syntax

DAQmx_Dev_Accessory_ProductTypes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the model names of accessories connected to the device. Each array element corresponds to a connector. For example, index 0 corresponds to connector 0. The array contains an empty string for each connector with no accessory connected. | Not Settable |

You can get this property using:

- [DAQmxGetDevAccessoryProductTypes](group__ni-daqmx__c__functions__property__manipulation__getter_1gac889de9e3d93e6d263ebeccc746c4ec9.html)

Parent topic:

Accessory

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__fielddaq.html language=enus -->
## TOPIC 02026: FieldDAQ

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__fielddaq.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__fielddaq.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_FieldDAQ_BankDevNamesDAQmx_FieldDAQ_DevNameAttachmentsNone

### FieldDAQ

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_FieldDAQ_BankDevNames |  |
| DAQmx_FieldDAQ_DevName |  |

#### Attachments

None

Parent topic:

Identification

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__fielddaq_1ga34118e4302d1b06248a6adac6cf0ede5.html language=enus -->
## TOPIC 02027: DAQmx_FieldDAQ_DevName

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__fielddaq_1ga34118e4302d1b06248a6adac6cf0ede5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__fielddaq_1ga34118e4302d1b06248a6adac6cf0ede5.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_FieldDAQ_DevNameRemarksData TypeDescriptionRestrictionschar*Indicates the parent device which this bank is located in.Not SettableYou can get this property using:DAQmxGetFieldDAQDevName

### DAQmx_FieldDAQ_DevName

#### Syntax

DAQmx_FieldDAQ_DevName

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the parent device which this bank is located in. | Not Settable |

You can get this property using:

- [DAQmxGetFieldDAQDevName](group__ni-daqmx__c__functions__property__manipulation__getter_1gac6fefe0d6b27bc4a5e4cbbde7b64bf9b.html)

Parent topic:

FieldDAQ

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__id__pin.html language=enus -->
## TOPIC 02028: ID Pin

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__id__pin.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__id__pin.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_IDPin_MemFamilyCodesDAQmx_Dev_IDPin_MemSerialNumsDAQmx_Dev_IDPin_MemSizesDAQmx_Dev_IDPin_PinNamesDAQmx_Dev_IDPin_PinStatusesAttachmentsNone

### ID Pin

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_IDPin_MemFamilyCodes |  |
| DAQmx_Dev_IDPin_MemSerialNums |  |
| DAQmx_Dev_IDPin_MemSizes |  |
| DAQmx_Dev_IDPin_PinNames |  |
| DAQmx_Dev_IDPin_PinStatuses |  |

#### Attachments

None

Parent topic:

Identification

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__id__pin_1ga024cbbe544f738bc23725e597fbc35a4.html language=enus -->
## TOPIC 02029: DAQmx_Dev_IDPin_MemSerialNums

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__id__pin_1ga024cbbe544f738bc23725e597fbc35a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__id__pin_1ga024cbbe544f738bc23725e597fbc35a4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_IDPin_MemSerialNumsRemarksData TypeDescriptionRestrictionschar*Indicates the serial number of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains an empty string for each ID Pin with no memory connected.Not SettableYou can get this pro

### DAQmx_Dev_IDPin_MemSerialNums

#### Syntax

DAQmx_Dev_IDPin_MemSerialNums

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the serial number of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains an empty string for each ID Pin with no memory connected. | Not Settable |

You can get this property using:

- [DAQmxGetDevIDPinMemSerialNums](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7047ad580d4c22a243597b855ed625d2.html)

Parent topic:

ID Pin

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__id__pin_1ga3119fbfb630a3191583bb16814ee8830.html language=enus -->
## TOPIC 02030: DAQmx_Dev_IDPin_PinNames

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__id__pin_1ga3119fbfb630a3191583bb16814ee8830.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__id__pin_1ga3119fbfb630a3191583bb16814ee8830.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_IDPin_PinNamesRemarksData TypeDescriptionRestrictionschar*Indicates the names of all the ID Pins on this device.Not SettableYou can get this property using:DAQmxGetDevIDPinPinNames

### DAQmx_Dev_IDPin_PinNames

#### Syntax

DAQmx_Dev_IDPin_PinNames

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the names of all the ID Pins on this device. | Not Settable |

You can get this property using:

- [DAQmxGetDevIDPinPinNames](group__ni-daqmx__c__functions__property__manipulation__getter_1gad69afbc76901020d8ff743ac3137948e.html)

Parent topic:

ID Pin

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__id__pin_1ga40ad9a283a86850b35443cf3ec542f1d.html language=enus -->
## TOPIC 02031: DAQmx_Dev_IDPin_MemSizes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__id__pin_1ga40ad9a283a86850b35443cf3ec542f1d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__id__pin_1ga40ad9a283a86850b35443cf3ec542f1d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_IDPin_MemSizesRemarksData TypeDescriptionRestrictionsuInt32*Indicates the size in bytes of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains 0 for each ID Pin with no memory connected.Not SettableYou can get this property using:DAQmx

### DAQmx_Dev_IDPin_MemSizes

#### Syntax

DAQmx_Dev_IDPin_MemSizes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32* | Indicates the size in bytes of the memory connected to each ID Pin. Each array element corresponds to an ID Pin. The array contains 0 for each ID Pin with no memory connected. | Not Settable |

- [DAQmxGetDevIDPinMemSizes](group__ni-daqmx__c__functions__property__manipulation__getter_1ga35cec8735ad4b3a51868c6c0d2bcb040.html)

Parent topic:

ID Pin

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__identification__id__pin_1gacce39aba8cb78e735e2ebccc3c26c363.html language=enus -->
## TOPIC 02032: DAQmx_Dev_IDPin_PinStatuses

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__identification__id__pin_1gacce39aba8cb78e735e2ebccc3c26c363.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__identification__id__pin_1gacce39aba8cb78e735e2ebccc3c26c363.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_IDPin_PinStatusesRemarksData TypeDescriptionRestrictionsint32*Indicates status of each ID Pin.Not SettableValid valuesDAQmx_Val_MemoryNotPresent16205No memory is connected to ID Pin.DAQmx_Val_MemoryPresent16206The memory is connected to ID Pin.You can get this property using:DAQmxGet

### DAQmx_Dev_IDPin_PinStatuses

#### Syntax

DAQmx_Dev_IDPin_PinStatuses

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32* | Indicates status of each ID Pin. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_MemoryNotPresent | 16205 | No memory is connected to ID Pin. |
| DAQmx_Val_MemoryPresent | 16206 | The memory is connected to ID Pin. |

You can get this property using:

- [DAQmxGetDevIDPinPinStatuses](group__ni-daqmx__c__functions__property__manipulation__getter_1gada78ed453a6d3036da8cce4f9f7d82cd.html)

Parent topic:

ID Pin

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location_1gad8eda133c484d7eb03224710b513d79d.html language=enus -->
## TOPIC 02033: DAQmx_Dev_BusType

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location_1gad8eda133c484d7eb03224710b513d79d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location_1gad8eda133c484d7eb03224710b513d79d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_BusTypeRemarksData TypeDescriptionRestrictionsint32Indicates the bus type of the device.Not SettableValid valuesDAQmx_Val_PCI12582PCI.DAQmx_Val_PCIe13612PCI Express.DAQmx_Val_PXI12583PXI.DAQmx_Val_PXIe14706PXI Express.DAQmx_Val_SCXI12584SCXI.DAQmx_Val_SCC14707SCC.DAQmx_Val_PCCard1258

### DAQmx_Dev_BusType

#### Syntax

DAQmx_Dev_BusType

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the bus type of the device. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_PCI | 12582 | PCI. |
| DAQmx_Val_PCIe | 13612 | PCI Express. |
| DAQmx_Val_PXI | 12583 | PXI. |
| DAQmx_Val_PXIe | 14706 | PXI Express. |
| DAQmx_Val_SCXI | 12584 | SCXI. |
| DAQmx_Val_SCC | 14707 | SCC. |
| DAQmx_Val_PCCard | 12585 | PC Card/PCMCIA. |
| DAQmx_Val_USB | 12586 | USB. |
| DAQmx_Val_CompactDAQ | 14637 | CompactDAQ. |
| DAQmx_Val_CompactRIO | 16143 | CompactRIO. |
| DAQmx_Val_TCPIP | 14828 | TCP/IP. |
| DAQmx_Val_Unknown | 12588 | Unknown bus type. |
| DAQmx_Val_SwitchBlock | 15870 | SwitchBlock. |

You can get this property using:

- [DAQmxGetDevBusType](group__ni-daqmx__c__functions__property__manipulation__getter_1gad0b1ae4e2f4d48eca746ded545d07c88.html)

Parent topic:

Location

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__compactdaq.html language=enus -->
## TOPIC 02034: CompactDAQ

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__compactdaq.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__compactdaq.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_CompactDAQ_ChassisDevNameDAQmx_Dev_CompactDAQ_SlotNumAttachmentsNone

### CompactDAQ

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_CompactDAQ_ChassisDevName |  |
| DAQmx_Dev_CompactDAQ_SlotNum |  |

#### Attachments

None

Parent topic:

Location

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__compactdaq_1ga9677b3145f4bebad1487ae61d21e10de.html language=enus -->
## TOPIC 02035: DAQmx_Dev_CompactDAQ_SlotNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__compactdaq_1ga9677b3145f4bebad1487ae61d21e10de.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__compactdaq_1ga9677b3145f4bebad1487ae61d21e10de.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CompactDAQ_SlotNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the slot number in which this module is located in the CompactDAQ chassis.Not SettableYou can get this property using:DAQmxGetDevCompactDAQSlotNum

### DAQmx_Dev_CompactDAQ_SlotNum

#### Syntax

DAQmx_Dev_CompactDAQ_SlotNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the slot number in which this module is located in the CompactDAQ chassis. | Not Settable |

You can get this property using:

- [DAQmxGetDevCompactDAQSlotNum](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf566afe36377aa290131057e01907710.html)

Parent topic:

CompactDAQ

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__compactdaq_1gad80f75b252264e512fea966b78693915.html language=enus -->
## TOPIC 02036: DAQmx_Dev_CompactDAQ_ChassisDevName

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__compactdaq_1gad80f75b252264e512fea966b78693915.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__compactdaq_1gad80f75b252264e512fea966b78693915.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CompactDAQ_ChassisDevNameRemarksData TypeDescriptionRestrictionschar*Indicates the name of the CompactDAQ chassis that contains this module.Not SettableYou can get this property using:DAQmxGetDevCompactDAQChassisDevName

### DAQmx_Dev_CompactDAQ_ChassisDevName

#### Syntax

DAQmx_Dev_CompactDAQ_ChassisDevName

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the name of the CompactDAQ chassis that contains this module. | Not Settable |

You can get this property using:

- [DAQmxGetDevCompactDAQChassisDevName](group__ni-daqmx__c__functions__property__manipulation__getter_1gad94b6032acf7533872acb652d59260ef.html)

Parent topic:

CompactDAQ

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__compactrio.html language=enus -->
## TOPIC 02037: CompactRIO

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__compactrio.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__compactrio.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_CompactRIO_ChassisDevNameDAQmx_Dev_CompactRIO_SlotNumAttachmentsNone

### CompactRIO

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_CompactRIO_ChassisDevName |  |
| DAQmx_Dev_CompactRIO_SlotNum |  |

#### Attachments

None

Parent topic:

Location

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__compactrio_1ga2ea51c7e6672dc30f73ffb3030b8a48a.html language=enus -->
## TOPIC 02038: DAQmx_Dev_CompactRIO_SlotNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__compactrio_1ga2ea51c7e6672dc30f73ffb3030b8a48a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__compactrio_1ga2ea51c7e6672dc30f73ffb3030b8a48a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CompactRIO_SlotNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the slot number of the CompactRIO chassis where this module is located.Not SettableYou can get this property using:DAQmxGetDevCompactRIOSlotNum

### DAQmx_Dev_CompactRIO_SlotNum

#### Syntax

DAQmx_Dev_CompactRIO_SlotNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the slot number of the CompactRIO chassis where this module is located. | Not Settable |

You can get this property using:

- [DAQmxGetDevCompactRIOSlotNum](group__ni-daqmx__c__functions__property__manipulation__getter_1ga73c8f58a7057b0bfd892f213898a515b.html)

Parent topic:

CompactRIO

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__compactrio_1gaef962c9aa77e48b1280fcddff1bb5478.html language=enus -->
## TOPIC 02039: DAQmx_Dev_CompactRIO_ChassisDevName

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__compactrio_1gaef962c9aa77e48b1280fcddff1bb5478.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__compactrio_1gaef962c9aa77e48b1280fcddff1bb5478.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_CompactRIO_ChassisDevNameRemarksData TypeDescriptionRestrictionschar*Indicates the name of the CompactRIO chassis that contains this module.Not SettableYou can get this property using:DAQmxGetDevCompactRIOChassisDevName

### DAQmx_Dev_CompactRIO_ChassisDevName

#### Syntax

DAQmx_Dev_CompactRIO_ChassisDevName

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the name of the CompactRIO chassis that contains this module. | Not Settable |

You can get this property using:

- [DAQmxGetDevCompactRIOChassisDevName](group__ni-daqmx__c__functions__property__manipulation__getter_1gad6ae64d03b57826da5680739ec9b7f01.html)

Parent topic:

CompactRIO

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__pci_1ga95b4d8a56e3613a3e4ac274f12e601a6.html language=enus -->
## TOPIC 02040: DAQmx_Dev_PCI_DevNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__pci_1ga95b4d8a56e3613a3e4ac274f12e601a6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__pci_1ga95b4d8a56e3613a3e4ac274f12e601a6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_PCI_DevNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the PCI slot number of the device.Not SettableYou can get this property using:DAQmxGetDevPCIDevNum

### DAQmx_Dev_PCI_DevNum

#### Syntax

DAQmx_Dev_PCI_DevNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the PCI slot number of the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevPCIDevNum](group__ni-daqmx__c__functions__property__manipulation__getter_1ga35db1e754412a502588d96862801426a.html)

Parent topic:

PCI

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__pci_1ga9ed9e4dcb3b885e3c11e3b2bea351c0e.html language=enus -->
## TOPIC 02041: DAQmx_Dev_PCI_BusNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__pci_1ga9ed9e4dcb3b885e3c11e3b2bea351c0e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__pci_1ga9ed9e4dcb3b885e3c11e3b2bea351c0e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_PCI_BusNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the PCI bus number of the device.Not SettableYou can get this property using:DAQmxGetDevPCIBusNum

### DAQmx_Dev_PCI_BusNum

#### Syntax

DAQmx_Dev_PCI_BusNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the PCI bus number of the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevPCIBusNum](group__ni-daqmx__c__functions__property__manipulation__getter_1ga25d20feaec1f40d8319c734421a74394.html)

Parent topic:

PCI

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__pxi.html language=enus -->
## TOPIC 02042: PXI

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__pxi.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__pxi.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_PXI_ChassisNumDAQmx_Dev_PXI_SlotNumAttachmentsNone

### PXI

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_PXI_ChassisNum |  |
| DAQmx_Dev_PXI_SlotNum |  |

#### Attachments

None

Parent topic:

Location

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__pxi_1ga2756a103400e64331e472f2ed54cb196.html language=enus -->
## TOPIC 02043: DAQmx_Dev_PXI_SlotNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__pxi_1ga2756a103400e64331e472f2ed54cb196.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__pxi_1ga2756a103400e64331e472f2ed54cb196.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_PXI_SlotNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the PXI slot number of the device.Not SettableYou can get this property using:DAQmxGetDevPXISlotNum

### DAQmx_Dev_PXI_SlotNum

#### Syntax

DAQmx_Dev_PXI_SlotNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the PXI slot number of the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevPXISlotNum](group__ni-daqmx__c__functions__property__manipulation__getter_1gaacf6a7a2b88c304aa33d205081f6443b.html)

Parent topic:

PXI

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__pxi_1gab19906446ee4a6edf6da6c60a65b4981.html language=enus -->
## TOPIC 02044: DAQmx_Dev_PXI_ChassisNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__pxi_1gab19906446ee4a6edf6da6c60a65b4981.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__pxi_1gab19906446ee4a6edf6da6c60a65b4981.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_PXI_ChassisNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the PXI chassis number of the device, as identified in MAX.Not SettableYou can get this property using:DAQmxGetDevPXIChassisNum

### DAQmx_Dev_PXI_ChassisNum

#### Syntax

DAQmx_Dev_PXI_ChassisNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the PXI chassis number of the device, as identified in MAX. | Not Settable |

You can get this property using:

- [DAQmxGetDevPXIChassisNum](group__ni-daqmx__c__functions__property__manipulation__getter_1gabcb319a2c28a8b44116dab08eef059c8.html)

Parent topic:

PXI

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__tcp__ip.html language=enus -->
## TOPIC 02045: TCP/IP

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__tcp__ip.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__tcp__ip.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Dev_TCPIP_EthernetIPDAQmx_Dev_TCPIP_HostnameDAQmx_Dev_TCPIP_WirelessIPDAQmx_Dev_TerminalsAttachmentsNone

### TCP/IP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Dev_TCPIP_EthernetIP |  |
| DAQmx_Dev_TCPIP_Hostname |  |
| DAQmx_Dev_TCPIP_WirelessIP |  |
| DAQmx_Dev_Terminals |  |

#### Attachments

None

Parent topic:

Location

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__tcp__ip_1ga70464cc230f0a5dac4db8e7a8fae5620.html language=enus -->
## TOPIC 02046: DAQmx_Dev_TCPIP_Hostname

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__tcp__ip_1ga70464cc230f0a5dac4db8e7a8fae5620.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__tcp__ip_1ga70464cc230f0a5dac4db8e7a8fae5620.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_TCPIP_HostnameRemarksData TypeDescriptionRestrictionschar*Indicates the IPv4 hostname of the device.Not SettableYou can get this property using:DAQmxGetDevTCPIPHostname

### DAQmx_Dev_TCPIP_Hostname

#### Syntax

DAQmx_Dev_TCPIP_Hostname

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the IPv4 hostname of the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevTCPIPHostname](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7a2c854f555bc7673f871dc2fafd863f.html)

Parent topic:

TCP/IP

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__location__tcp__ip_1gaf7459769afc73fd388c24cf9e57a3af9.html language=enus -->
## TOPIC 02047: DAQmx_Dev_Terminals

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__location__tcp__ip_1gaf7459769afc73fd388c24cf9e57a3af9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__location__tcp__ip_1gaf7459769afc73fd388c24cf9e57a3af9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_TerminalsRemarksData TypeDescriptionRestrictionschar*Indicates a list of all terminals on the device.Not SettableYou can get this property using:DAQmxGetDevTerminals

### DAQmx_Dev_Terminals

#### Syntax

DAQmx_Dev_Terminals

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of all terminals on the device. | Not Settable |

You can get this property using:

- [DAQmxGetDevTerminals](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1541df92a26f0c0a31e4eead27891b2c.html)

Parent topic:

TCP/IP

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__teds_1ga21417855d4423a6c5e236be0d057ce9a.html language=enus -->
## TOPIC 02048: DAQmx_Dev_TEDS_HWTEDSSupported

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__teds_1ga21417855d4423a6c5e236be0d057ce9a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__teds_1ga21417855d4423a6c5e236be0d057ce9a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_TEDS_HWTEDSSupportedRemarksData TypeDescriptionRestrictionsbool32Indicates whether the device supports hardware TEDS.Not SettableYou can get this property using:DAQmxGetDevTEDSHWTEDSSupported

### DAQmx_Dev_TEDS_HWTEDSSupported

#### Syntax

DAQmx_Dev_TEDS_HWTEDSSupported

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates whether the device supports hardware TEDS. | Not Settable |

You can get this property using:

- [DAQmxGetDevTEDSHWTEDSSupported](group__ni-daqmx__c__functions__property__manipulation__getter_1gacbdbb7c2f2005207502db7db82e7d276.html)

Parent topic:

TEDS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__device__triggering_1ga8b7aefb15dc830c630729d7f088ec0af.html language=enus -->
## TOPIC 02049: DAQmx_Dev_AnlgTrigSupported

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__device__triggering_1ga8b7aefb15dc830c630729d7f088ec0af.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__device__triggering_1ga8b7aefb15dc830c630729d7f088ec0af.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Dev_AnlgTrigSupportedRemarksData TypeDescriptionRestrictionsbool32Indicates if the device supports analog triggering.Not SettableYou can get this property using:DAQmxGetDevAnlgTrigSupported

### DAQmx_Dev_AnlgTrigSupported

#### Syntax

DAQmx_Dev_AnlgTrigSupported

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device supports analog triggering. | Not Settable |

You can get this property using:

- [DAQmxGetDevAnlgTrigSupported](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa9ff78ee4690862c843aad445550abc8.html)

Parent topic:

Triggering

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__clocks__ai__convert__clock__pulse.html language=enus -->
## TOPIC 02050: Pulse

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__clocks__ai__convert__clock__pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__clocks__ai__convert__clock__pulse.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_AIConvClk_Pulse_PolarityAttachmentsNone

### Pulse

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_AIConvClk_Pulse_Polarity |  |

#### Attachments

None

Parent topic:

AI Convert Clock

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__pulse.html language=enus -->
## TOPIC 02051: Pulse

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__pulse.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_SampClk_Pulse_PolarityAttachmentsNone

### Pulse

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_SampClk_Pulse_Polarity |  |

#### Attachments

None

Parent topic:

Sample Clock

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__pulse_1gabc27cfb38465368ace892916bceb7abf.html language=enus -->
## TOPIC 02052: DAQmx_Exported_SampClk_Pulse_Polarity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__pulse_1gabc27cfb38465368ace892916bceb7abf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__pulse_1gabc27cfb38465368ace892916bceb7abf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_SampClk_Pulse_PolarityRemarksData TypeDescriptionRestrictionsint32Specifies the polarity of the exported Sample Clock if Output Behavior is DAQmx_Val_Pulse.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.Y

### DAQmx_Exported_SampClk_Pulse_Polarity

#### Syntax

DAQmx_Exported_SampClk_Pulse_Polarity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the polarity of the exported Sample Clock if Output Behavior is DAQmx_Val_Pulse. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedSampClkPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__getter_1gae0048f5e61a7aa7ee46295d928b19ebe.html)
- [DAQmxSetExportedSampClkPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3421da24263754c0304a12ff676fea89.html)
- [DAQmxResetExportedSampClkPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafb199e0a04fbb858c5db94fc22d26b3f.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__timebase.html language=enus -->
## TOPIC 02053: Sample Clock Timebase

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__timebase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__clocks__sample__clock__timebase.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_SampClkTimebase_OutputTermAttachmentsNone

### Sample Clock Timebase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_SampClkTimebase_OutputTerm |  |

#### Attachments

None

Parent topic:

Clocks

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event.html language=enus -->
## TOPIC 02054: Advance Complete Event

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPulseGroup membersNameDescriptionDAQmx_Exported_AdvCmpltEvent_DelayDAQmx_Exported_AdvCmpltEvent_OutputTermAttachmentsNone

### Advance Complete Event

#### Groups

- Pulse

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_AdvCmpltEvent_Delay |  |
| DAQmx_Exported_AdvCmpltEvent_OutputTerm |  |

#### Attachments

None

Parent topic:

Events

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event_1ga1ac3cd57468564acc4eb3622d3cc1c47.html language=enus -->
## TOPIC 02055: DAQmx_Exported_AdvCmpltEvent_Delay

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event_1ga1ac3cd57468564acc4eb3622d3cc1c47.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event_1ga1ac3cd57468564acc4eb3622d3cc1c47.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_AdvCmpltEvent_DelayRemarksData TypeDescriptionRestrictionsfloat64Specifies the output signal delay in periods of the sample clock.You can get/set/reset this property using:DAQmxGetExportedAdvCmpltEventDelayDAQmxSetExportedAdvCmpltEventDelayDAQmxResetExportedAdvCmpltEventDelay

### DAQmx_Exported_AdvCmpltEvent_Delay

#### Syntax

DAQmx_Exported_AdvCmpltEvent_Delay

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the output signal delay in periods of the sample clock. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedAdvCmpltEventDelay](group__ni-daqmx__c__functions__property__manipulation__getter_1gab0e2b1b0944cfaf1d0537b6f854fcd1e.html)
- [DAQmxSetExportedAdvCmpltEventDelay](group__ni-daqmx__c__functions__property__manipulation__setter_1ga53cb9e1182afefc1da844bebdbb70432.html)
- [DAQmxResetExportedAdvCmpltEventDelay](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga635de09e01fedc3855d89cae1859f3c5.html)

Parent topic:

Advance Complete Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event__pulse.html language=enus -->
## TOPIC 02056: Pulse

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event__pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event__pulse.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_AdvCmpltEvent_Pulse_PolarityDAQmx_Exported_AdvCmpltEvent_Pulse_WidthAttachmentsNone

### Pulse

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_AdvCmpltEvent_Pulse_Polarity |  |
| DAQmx_Exported_AdvCmpltEvent_Pulse_Width |  |

#### Attachments

None

Parent topic:

Advance Complete Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event__pulse_1ga7aa507066f7becc3c9d90c4459be67d8.html language=enus -->
## TOPIC 02057: DAQmx_Exported_AdvCmpltEvent_Pulse_Polarity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event__pulse_1ga7aa507066f7becc3c9d90c4459be67d8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__advance__complete__event__pulse_1ga7aa507066f7becc3c9d90c4459be67d8.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_AdvCmpltEvent_Pulse_PolarityRemarksData TypeDescriptionRestrictionsint32Specifies the polarity of the exported Advance Complete Event.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get/set/reset t

### DAQmx_Exported_AdvCmpltEvent_Pulse_Polarity

#### Syntax

DAQmx_Exported_AdvCmpltEvent_Pulse_Polarity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the polarity of the exported Advance Complete Event. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedAdvCmpltEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__getter_1gada6233ca4efc7d76b2670d0a6788edfa.html)
- [DAQmxSetExportedAdvCmpltEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__setter_1gabe64c7e1140e039ef6b1af494f9bd104.html)
- [DAQmxResetExportedAdvCmpltEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4f71400109e2fe54c8624f39831022c5.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event.html language=enus -->
## TOPIC 02058: AI Hold Complete Event

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPulseGroup membersNameDescriptionDAQmx_Exported_AIHoldCmpltEvent_OutputTermAttachmentsNone

### AI Hold Complete Event

#### Groups

- Pulse

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_AIHoldCmpltEvent_OutputTerm |  |

#### Attachments

None

Parent topic:

Events

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event__pulse.html language=enus -->
## TOPIC 02059: Pulse

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event__pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event__pulse.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_AIHoldCmpltEvent_PulsePolarityAttachmentsNone

### Pulse

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_AIHoldCmpltEvent_PulsePolarity |  |

#### Attachments

None

Parent topic:

AI Hold Complete Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event__pulse_1ga9c22836da856aeea0e6c215f38b52159.html language=enus -->
## TOPIC 02060: DAQmx_Exported_AIHoldCmpltEvent_PulsePolarity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event__pulse_1ga9c22836da856aeea0e6c215f38b52159.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__ai__hold__complete__event__pulse_1ga9c22836da856aeea0e6c215f38b52159.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_AIHoldCmpltEvent_PulsePolarityRemarksData TypeDescriptionRestrictionsint32Specifies the polarity of an exported AI Hold Complete Event pulse.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get/set/

### DAQmx_Exported_AIHoldCmpltEvent_PulsePolarity

#### Syntax

DAQmx_Exported_AIHoldCmpltEvent_PulsePolarity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the polarity of an exported AI Hold Complete Event pulse. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedAIHoldCmpltEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__getter_1gae3346dc3d075f1def36d7ac8b7408346.html)
- [DAQmxSetExportedAIHoldCmpltEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__setter_1ga59af24a1cca40ebe90cc05bf6b083677.html)
- [DAQmxResetExportedAIHoldCmpltEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga57007d1229be2833b3778038bb148b7f.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__change__detection__event.html language=enus -->
## TOPIC 02061: Change Detection Event

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__change__detection__event.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__change__detection__event.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPulseGroup membersNameDescriptionDAQmx_Exported_ChangeDetectEvent_OutputTermAttachmentsNone

### Change Detection Event

#### Groups

- Pulse

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_ChangeDetectEvent_OutputTerm |  |

#### Attachments

None

Parent topic:

Events

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__change__detection__event__pulse.html language=enus -->
## TOPIC 02062: Pulse

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__change__detection__event__pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__change__detection__event__pulse.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_ChangeDetectEvent_Pulse_PolarityAttachmentsNone

### Pulse

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_ChangeDetectEvent_Pulse_Polarity |  |

#### Attachments

None

Parent topic:

Change Detection Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__change__detection__event__pulse_1gaef4843944681a49a3559e8b9b83645d9.html language=enus -->
## TOPIC 02063: DAQmx_Exported_ChangeDetectEvent_Pulse_Polarity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__change__detection__event__pulse_1gaef4843944681a49a3559e8b9b83645d9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__change__detection__event__pulse_1gaef4843944681a49a3559e8b9b83645d9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_ChangeDetectEvent_Pulse_PolarityRemarksData TypeDescriptionRestrictionsint32Specifies the polarity of an exported Change Detection Event pulse.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get/se

### DAQmx_Exported_ChangeDetectEvent_Pulse_Polarity

#### Syntax

DAQmx_Exported_ChangeDetectEvent_Pulse_Polarity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the polarity of an exported Change Detection Event pulse. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedChangeDetectEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa3309de936517897384a331f9a88896a.html)
- [DAQmxSetExportedChangeDetectEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa4047b6c179efe7e597a13c9e8e189e5.html)
- [DAQmxResetExportedChangeDetectEventPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga312d94d3de13be063babf1f3ea18ecd0.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__counter__output__event.html language=enus -->
## TOPIC 02064: Counter Output Event

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__counter__output__event.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__counter__output__event.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPulseToggleGroup membersNameDescriptionDAQmx_Exported_CtrOutEvent_OutputBehaviorDAQmx_Exported_CtrOutEvent_OutputTermAttachmentsNone

### Counter Output Event

#### Groups

- Pulse
- Toggle

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_CtrOutEvent_OutputBehavior |  |
| DAQmx_Exported_CtrOutEvent_OutputTerm |  |

#### Attachments

None

Parent topic:

Events

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__counter__output__event_1ga67041824a29cff05b737d09e24d3d03b.html language=enus -->
## TOPIC 02065: DAQmx_Exported_CtrOutEvent_OutputBehavior

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__counter__output__event_1ga67041824a29cff05b737d09e24d3d03b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__counter__output__event_1ga67041824a29cff05b737d09e24d3d03b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_CtrOutEvent_OutputBehaviorRemarksData TypeDescriptionRestrictionsint32Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count.Valid valuesDAQmx_Val_Pulse10265Send a pulse to the terminal.DAQmx_Val_

### DAQmx_Exported_CtrOutEvent_OutputBehavior

#### Syntax

DAQmx_Exported_CtrOutEvent_OutputBehavior

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Pulse | 10265 | Send a pulse to the terminal. |
| DAQmx_Val_Toggle | 10307 | Toggle the state of the terminal from low to high or from high to low. |

You can get/set/reset this property using:

- [DAQmxGetExportedCtrOutEventOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__getter_1gad22e66aed4cb244ab4aa76d31c59d9ab.html)
- [DAQmxSetExportedCtrOutEventOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__setter_1ga0a1d39f7c4a7894d0bc800a19d340230.html)
- [DAQmxResetExportedCtrOutEventOutputBehavior](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae11fa61992a82ec68177ba9957c4a989.html)

Parent topic:

Counter Output Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__pulse.html language=enus -->
## TOPIC 02066: Pulse

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__pulse.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_CtrOutEvent_Pulse_PolarityAttachmentsNone

### Pulse

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_CtrOutEvent_Pulse_Polarity |  |

#### Attachments

None

Parent topic:

Counter Output Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__toggle.html language=enus -->
## TOPIC 02067: Toggle

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__toggle.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__toggle.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_CtrOutEvent_Toggle_IdleStateAttachmentsNone

### Toggle

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_CtrOutEvent_Toggle_IdleState |  |

#### Attachments

None

Parent topic:

Counter Output Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__toggle_1gabe72d0811b235c5bdb6b0d41e87d2679.html language=enus -->
## TOPIC 02068: DAQmx_Exported_CtrOutEvent_Toggle_IdleState

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__toggle_1gabe72d0811b235c5bdb6b0d41e87d2679.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__counter__output__event__toggle_1gabe72d0811b235c5bdb6b0d41e87d2679.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_CtrOutEvent_Toggle_IdleStateRemarksData TypeDescriptionRestrictionsint32Specifies the initial state of the output terminal of the counter when Output Behavior is DAQmx_Val_Toggle. The terminal enters this state when NI-DAQmx commits the task.Valid valuesDAQmx_Val_High10192High s

### DAQmx_Exported_CtrOutEvent_Toggle_IdleState

#### Syntax

DAQmx_Exported_CtrOutEvent_Toggle_IdleState

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the initial state of the output terminal of the counter when Output Behavior is DAQmx_Val_Toggle. The terminal enters this state when NI-DAQmx commits the task. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_High | 10192 | High state. |
| DAQmx_Val_Low | 10214 | Low state. |

You can get/set/reset this property using:

- [DAQmxGetExportedCtrOutEventToggleIdleState](group__ni-daqmx__c__functions__property__manipulation__getter_1gac63a8edf78faa0dbcbfadfcd375b1e3e.html)
- [DAQmxSetExportedCtrOutEventToggleIdleState](group__ni-daqmx__c__functions__property__manipulation__setter_1ga9f227cb6e5f666eebcfc41cddf6d6bb6.html)
- [DAQmxResetExportedCtrOutEventToggleIdleState](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab1598d26f3e714cd5cc0a4a932546f74.html)

Parent topic:

Toggle

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__data__active__event_1gae1a275fe7396689990791600053ec1e5.html language=enus -->
## TOPIC 02069: DAQmx_Exported_DataActiveEvent_OutputTerm

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__data__active__event_1gae1a275fe7396689990791600053ec1e5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__data__active__event_1gae1a275fe7396689990791600053ec1e5.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_DataActiveEvent_OutputTermRemarksData TypeDescriptionRestrictionschar*Specifies the terminal to which to export the Data Active Event.You can get/set/reset this property using:DAQmxGetExportedDataActiveEventOutputTermDAQmxSetExportedDataActiveEventOutputTermDAQmxResetExportedDat

### DAQmx_Exported_DataActiveEvent_OutputTerm

#### Syntax

DAQmx_Exported_DataActiveEvent_OutputTerm

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the terminal to which to export the Data Active Event. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedDataActiveEventOutputTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1gac8cb1f3b6285def4d78843ecf299687b.html)
- [DAQmxSetExportedDataActiveEventOutputTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1ga8754c4d409bd0e726c134c5cff736500.html)
- [DAQmxResetExportedDataActiveEventOutputTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga72f35b0f31e37fa43bc2d845474f21e9.html)

Parent topic:

Data Active Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__data__active__event__level.html language=enus -->
## TOPIC 02070: Level

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__data__active__event__level.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__data__active__event__level.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_DataActiveEvent_Lvl_ActiveLvlAttachmentsNone

### Level

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_DataActiveEvent_Lvl_ActiveLvl |  |

#### Attachments

None

Parent topic:

Data Active Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__data__active__event__level_1ga06e80d0e70fa66198b1717e774dd90fb.html language=enus -->
## TOPIC 02071: DAQmx_Exported_DataActiveEvent_Lvl_ActiveLvl

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__data__active__event__level_1ga06e80d0e70fa66198b1717e774dd90fb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__data__active__event__level_1ga06e80d0e70fa66198b1717e774dd90fb.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_DataActiveEvent_Lvl_ActiveLvlRemarksData TypeDescriptionRestrictionsint32Specifies the polarity of the exported Data Active Event.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get/set/reset this

### DAQmx_Exported_DataActiveEvent_Lvl_ActiveLvl

#### Syntax

DAQmx_Exported_DataActiveEvent_Lvl_ActiveLvl

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the polarity of the exported Data Active Event. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedDataActiveEventLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__getter_1ga9a99c88a99284229a3ec023487480191.html)
- [DAQmxSetExportedDataActiveEventLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__setter_1ga46aad6d0f5ba6d0fe651365630d5e25a.html)
- [DAQmxResetExportedDataActiveEventLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga12791302c4f1a7bb05364a66f4882040.html)

Parent topic:

Level

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__handshake__event_1ga7e55e2cd64c467b167a75cd0c79270e7.html language=enus -->
## TOPIC 02072: DAQmx_Exported_HshkEvent_Delay

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__handshake__event_1ga7e55e2cd64c467b167a75cd0c79270e7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__handshake__event_1ga7e55e2cd64c467b167a75cd0c79270e7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_HshkEvent_DelayRemarksData TypeDescriptionRestrictionsfloat64Specifies the number of seconds to delay after the Handshake Trigger deasserts before asserting the Handshake Event.You can get/set/reset this property using:DAQmxGetExportedHshkEventDelayDAQmxSetExportedHshkEventDelay

### DAQmx_Exported_HshkEvent_Delay

#### Syntax

DAQmx_Exported_HshkEvent_Delay

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the number of seconds to delay after the Handshake Trigger deasserts before asserting the Handshake Event. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedHshkEventDelay](group__ni-daqmx__c__functions__property__manipulation__getter_1ga592287e54984c6680a048cfd34a685d4.html)
- [DAQmxSetExportedHshkEventDelay](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3902f5d609f93c4d9fc31c3e3eacfbdc.html)
- [DAQmxResetExportedHshkEventDelay](group__ni-daqmx__c__functions__property__manipulation__resetter_1gae0b67ce1f741e92e1ef8005dd081c695.html)

Parent topic:

Handshake Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked.html language=enus -->
## TOPIC 02073: Interlocked

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_HshkEvent_Interlocked_AssertOnStartDAQmx_Exported_HshkEvent_Interlocked_AssertedLvlDAQmx_Exported_HshkEvent_Interlocked_DeassertDelayAttachmentsNone

### Interlocked

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_HshkEvent_Interlocked_AssertOnStart |  |
| DAQmx_Exported_HshkEvent_Interlocked_AssertedLvl |  |
| DAQmx_Exported_HshkEvent_Interlocked_DeassertDelay |  |

#### Attachments

None

Parent topic:

Handshake Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked_1ga18f09df7c245ccf591ef4d2273ff4b7d.html language=enus -->
## TOPIC 02074: DAQmx_Exported_HshkEvent_Interlocked_AssertedLvl

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked_1ga18f09df7c245ccf591ef4d2273ff4b7d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked_1ga18f09df7c245ccf591ef4d2273ff4b7d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_HshkEvent_Interlocked_AssertedLvlRemarksData TypeDescriptionRestrictionsint32Specifies the asserted level of the exported Handshake Event if Output Behavior is DAQmx_Val_Interlocked.Valid valuesDAQmx_Val_High10192High state.DAQmx_Val_Low10214Low state.You can get/set/reset this

### DAQmx_Exported_HshkEvent_Interlocked_AssertedLvl

#### Syntax

DAQmx_Exported_HshkEvent_Interlocked_AssertedLvl

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the asserted level of the exported Handshake Event if Output Behavior is DAQmx_Val_Interlocked. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_High | 10192 | High state. |
| DAQmx_Val_Low | 10214 | Low state. |

You can get/set/reset this property using:

- [DAQmxGetExportedHshkEventInterlockedAssertedLvl](group__ni-daqmx__c__functions__property__manipulation__getter_1ga73dfd37d6b321fcb4d9d0d4fc3683cb1.html)
- [DAQmxSetExportedHshkEventInterlockedAssertedLvl](group__ni-daqmx__c__functions__property__manipulation__setter_1ga60845033b5986db7ad8e0756ca36c7d7.html)
- [DAQmxResetExportedHshkEventInterlockedAssertedLvl](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaca4a1c1d1296d38df25ffff804c7ef27.html)

Parent topic:

Interlocked

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked_1ga2cd441c076a50493227e1fad5afa29e6.html language=enus -->
## TOPIC 02075: DAQmx_Exported_HshkEvent_Interlocked_DeassertDelay

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked_1ga2cd441c076a50493227e1fad5afa29e6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__handshake__event__interlocked_1ga2cd441c076a50493227e1fad5afa29e6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_HshkEvent_Interlocked_DeassertDelayRemarksData TypeDescriptionRestrictionsfloat64Specifies in seconds the amount of time to wait after the Handshake Trigger asserts before deasserting the Handshake Event if Output Behavior is DAQmx_Val_Interlocked.You can get/set/reset this prop

### DAQmx_Exported_HshkEvent_Interlocked_DeassertDelay

#### Syntax

DAQmx_Exported_HshkEvent_Interlocked_DeassertDelay

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in seconds the amount of time to wait after the Handshake Trigger asserts before deasserting the Handshake Event if Output Behavior is DAQmx_Val_Interlocked. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedHshkEventInterlockedDeassertDelay](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf49f1b64c36bb3358c63c9b41bcf88ac.html)
- [DAQmxSetExportedHshkEventInterlockedDeassertDelay](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa0d6b6c70d29209d83762fcf73db3e21.html)
- [DAQmxResetExportedHshkEventInterlockedDeassertDelay](group__ni-daqmx__c__functions__property__manipulation__resetter_1gac5ec731ee8b232044cd8ed954af7af48.html)

Parent topic:

Interlocked

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__handshake__event__pulse_1ga8316c8f647c9e86fedaec3029fa08fd9.html language=enus -->
## TOPIC 02076: DAQmx_Exported_HshkEvent_Pulse_Width

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__handshake__event__pulse_1ga8316c8f647c9e86fedaec3029fa08fd9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__handshake__event__pulse_1ga8316c8f647c9e86fedaec3029fa08fd9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_HshkEvent_Pulse_WidthRemarksData TypeDescriptionRestrictionsfloat64Specifies in seconds the pulse width of the exported Handshake Event if Output Behavior is DAQmx_Val_Pulse.You can get/set/reset this property using:DAQmxGetExportedHshkEventPulseWidthDAQmxSetExportedHshkEventPul

### DAQmx_Exported_HshkEvent_Pulse_Width

#### Syntax

DAQmx_Exported_HshkEvent_Pulse_Width

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies in seconds the pulse width of the exported Handshake Event if Output Behavior is DAQmx_Val_Pulse. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedHshkEventPulseWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1ga9dba900d9a88ee31dcb4037210c782f2.html)
- [DAQmxSetExportedHshkEventPulseWidth](group__ni-daqmx__c__functions__property__manipulation__setter_1ga6f59949476bde6f3eddaa0784e6ba500.html)
- [DAQmxResetExportedHshkEventPulseWidth](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab50bacc3f0cf22e6d73e4ead9573c373.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event.html language=enus -->
## TOPIC 02077: Ready For Transfer Event

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsLevelGroup membersNameDescriptionDAQmx_Exported_RdyForXferEvent_OutputTermAttachmentsNone

### Ready For Transfer Event

#### Groups

- Level

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_RdyForXferEvent_OutputTerm |  |

#### Attachments

None

Parent topic:

Events

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event_1gadf806c33202cf9daf11a94a2449d2a38.html language=enus -->
## TOPIC 02078: DAQmx_Exported_RdyForXferEvent_OutputTerm

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event_1gadf806c33202cf9daf11a94a2449d2a38.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event_1gadf806c33202cf9daf11a94a2449d2a38.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_RdyForXferEvent_OutputTermRemarksData TypeDescriptionRestrictionschar*Specifies the terminal to which to route the Ready for Transfer Event.You can get/set/reset this property using:DAQmxGetExportedRdyForXferEventOutputTermDAQmxSetExportedRdyForXferEventOutputTermDAQmxResetExpor

### DAQmx_Exported_RdyForXferEvent_OutputTerm

#### Syntax

DAQmx_Exported_RdyForXferEvent_OutputTerm

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the terminal to which to route the Ready for Transfer Event. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedRdyForXferEventOutputTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1gaecd7615915979a82128a6cb916f5a2d9.html)
- [DAQmxSetExportedRdyForXferEventOutputTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1ga9c842b20b1af0c3a45985037a0d160e2.html)
- [DAQmxResetExportedRdyForXferEventOutputTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8c6e7977c4f8940491fd89a48da5bcb2.html)

Parent topic:

Ready For Transfer Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level.html language=enus -->
## TOPIC 02079: Level

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_RdyForXferEvent_DeassertCondDAQmx_Exported_RdyForXferEvent_DeassertCondCustomThresholdDAQmx_Exported_RdyForXferEvent_Lvl_ActiveLvlAttachmentsNone

### Level

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_RdyForXferEvent_DeassertCond |  |
| DAQmx_Exported_RdyForXferEvent_DeassertCondCustomThreshold |  |
| DAQmx_Exported_RdyForXferEvent_Lvl_ActiveLvl |  |

#### Attachments

None

Parent topic:

Ready For Transfer Event

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level_1ga98306a617a5d5b80423e11ca4496ec7b.html language=enus -->
## TOPIC 02080: DAQmx_Exported_RdyForXferEvent_Lvl_ActiveLvl

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level_1ga98306a617a5d5b80423e11ca4496ec7b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level_1ga98306a617a5d5b80423e11ca4496ec7b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_RdyForXferEvent_Lvl_ActiveLvlRemarksData TypeDescriptionRestrictionsint32Specifies the active level of the exported Ready for Transfer Event.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get/set/

### DAQmx_Exported_RdyForXferEvent_Lvl_ActiveLvl

#### Syntax

DAQmx_Exported_RdyForXferEvent_Lvl_ActiveLvl

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the active level of the exported Ready for Transfer Event. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedRdyForXferEventLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7478526dfc42757647f5552c4a88548f.html)
- [DAQmxSetExportedRdyForXferEventLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__setter_1ga0a9fbdbf227d74d4bd3cdec0528ca0c9.html)
- [DAQmxResetExportedRdyForXferEventLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga9893091c6d5e306aa27d8af88ca3bfe3.html)

Parent topic:

Level

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level_1gacd3facfea1ec7f063427ee025001aae4.html language=enus -->
## TOPIC 02081: DAQmx_Exported_RdyForXferEvent_DeassertCondCustomThreshold

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level_1gacd3facfea1ec7f063427ee025001aae4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__ready__for__transfer__event__level_1gacd3facfea1ec7f063427ee025001aae4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_RdyForXferEvent_DeassertCondCustomThresholdRemarksData TypeDescriptionRestrictionsuInt32Specifies in samples the threshold below which the Ready for Transfer Event deasserts. This threshold is an amount of space available in the onboard memory of the device. Deassert Condition m

### DAQmx_Exported_RdyForXferEvent_DeassertCondCustomThreshold

#### Syntax

DAQmx_Exported_RdyForXferEvent_DeassertCondCustomThreshold

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Specifies in samples the threshold below which the Ready for Transfer Event deasserts. This threshold is an amount of space available in the onboard memory of the device. Deassert Condition must be DAQmx_Val_OnbrdMemCustomThreshold to use a custom threshold. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedRdyForXferEventDeassertCondCustomThreshold](group__ni-daqmx__c__functions__property__manipulation__getter_1gac0270e9108d04fd209096fc1e7dfaaa4.html)
- [DAQmxSetExportedRdyForXferEventDeassertCondCustomThreshold](group__ni-daqmx__c__functions__property__manipulation__setter_1ga2b4f74229c39602d5a38aac7be26988c.html)
- [DAQmxResetExportedRdyForXferEventDeassertCondCustomThreshold](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga9bfe62988d45c9e32b327e56aedbcebf.html)

Parent topic:

Level

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__events__watchdog__timer__expired__event.html language=enus -->
## TOPIC 02082: Watchdog Timer Expired Event

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__events__watchdog__timer__expired__event.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__events__watchdog__timer__expired__event.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_WatchdogExpiredEvent_OutputTermAttachmentsNone

### Watchdog Timer Expired Event

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_WatchdogExpiredEvent_OutputTerm |  |

#### Attachments

None

Parent topic:

Events

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers.html language=enus -->
## TOPIC 02083: Triggers

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvance TriggerPause TriggerReference TriggerStart TriggerGroup membersNoneAttachmentsNone

### Triggers

#### Groups

- Advance Trigger
- Pause Trigger
- Reference Trigger
- Start Trigger

#### Group members

None

#### Attachments

None

Parent topic:

ExportSignal

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger_1ga43967137c359e06ec0412438816a3e9c.html language=enus -->
## TOPIC 02084: DAQmx_Exported_AdvTrig_OutputTerm

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger_1ga43967137c359e06ec0412438816a3e9c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger_1ga43967137c359e06ec0412438816a3e9c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_AdvTrig_OutputTermRemarksData TypeDescriptionRestrictionschar*Specifies the terminal to which to route the Advance Trigger.You can get/set/reset this property using:DAQmxGetExportedAdvTrigOutputTermDAQmxSetExportedAdvTrigOutputTermDAQmxResetExportedAdvTrigOutputTerm

### DAQmx_Exported_AdvTrig_OutputTerm

#### Syntax

DAQmx_Exported_AdvTrig_OutputTerm

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the terminal to which to route the Advance Trigger. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedAdvTrigOutputTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf888ed9464562e50a42c70239a8b8553.html)
- [DAQmxSetExportedAdvTrigOutputTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1gacffed9d25da5825b8c2562f238996176.html)
- [DAQmxResetExportedAdvTrigOutputTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8e9861770b5c22e5b392f965786b8289.html)

Parent topic:

Advance Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse.html language=enus -->
## TOPIC 02085: Pulse

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_AdvTrig_Pulse_PolarityDAQmx_Exported_AdvTrig_Pulse_WidthDAQmx_Exported_AdvTrig_Pulse_WidthUnitsAttachmentsNone

### Pulse

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_AdvTrig_Pulse_Polarity |  |
| DAQmx_Exported_AdvTrig_Pulse_Width |  |
| DAQmx_Exported_AdvTrig_Pulse_WidthUnits |  |

#### Attachments

None

Parent topic:

Advance Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga1648e5231fd13efbcc6923fda5c0333b.html language=enus -->
## TOPIC 02086: DAQmx_Exported_AdvTrig_Pulse_Width

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga1648e5231fd13efbcc6923fda5c0333b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga1648e5231fd13efbcc6923fda5c0333b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_AdvTrig_Pulse_WidthRemarksData TypeDescriptionRestrictionsfloat64Specifies the width of an exported Advance Trigger pulse. Specify this value in the units you specify with Width Units.You can get/set/reset this property using:DAQmxGetExportedAdvTrigPulseWidthDAQmxSetExportedAdvT

### DAQmx_Exported_AdvTrig_Pulse_Width

#### Syntax

DAQmx_Exported_AdvTrig_Pulse_Width

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the width of an exported Advance Trigger pulse. Specify this value in the units you specify with Width Units. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedAdvTrigPulseWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa73022ff4bc88fe38da05834ba007d55.html)
- [DAQmxSetExportedAdvTrigPulseWidth](group__ni-daqmx__c__functions__property__manipulation__setter_1gae97428612aa076efcb3d5cca7da121f4.html)
- [DAQmxResetExportedAdvTrigPulseWidth](group__ni-daqmx__c__functions__property__manipulation__resetter_1gacfcd25509449e7e4872053f991aab045.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga65f9323becf6b89e560bec2d27644509.html language=enus -->
## TOPIC 02087: DAQmx_Exported_AdvTrig_Pulse_WidthUnits

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga65f9323becf6b89e560bec2d27644509.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga65f9323becf6b89e560bec2d27644509.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_AdvTrig_Pulse_WidthUnitsRemarksData TypeDescriptionRestrictionsint32Specifies the units of Width Value.Valid valuesDAQmx_Val_Seconds10364Seconds.You can get/set/reset this property using:DAQmxGetExportedAdvTrigPulseWidthUnitsDAQmxSetExportedAdvTrigPulseWidthUnitsDAQmxResetExport

### DAQmx_Exported_AdvTrig_Pulse_WidthUnits

#### Syntax

DAQmx_Exported_AdvTrig_Pulse_WidthUnits

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the units of Width Value. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Seconds | 10364 | Seconds. |

You can get/set/reset this property using:

- [DAQmxGetExportedAdvTrigPulseWidthUnits](group__ni-daqmx__c__functions__property__manipulation__getter_1ga96f03eb93c1dd8edcde88544caffefc0.html)
- [DAQmxSetExportedAdvTrigPulseWidthUnits](group__ni-daqmx__c__functions__property__manipulation__setter_1gada59d515db5b7b5c8e3e34219522d21a.html)
- [DAQmxResetExportedAdvTrigPulseWidthUnits](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaf6f45c053b3e97ee4e5cf9cae2dbebf0.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga685479cf09c1a717bb504cef78202d59.html language=enus -->
## TOPIC 02088: DAQmx_Exported_AdvTrig_Pulse_Polarity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga685479cf09c1a717bb504cef78202d59.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__advance__trigger__pulse_1ga685479cf09c1a717bb504cef78202d59.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_AdvTrig_Pulse_PolarityRemarksData TypeDescriptionRestrictionsint32Indicates the polarity of the exported Advance Trigger.Not SettableValid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get this propert

### DAQmx_Exported_AdvTrig_Pulse_Polarity

#### Syntax

DAQmx_Exported_AdvTrig_Pulse_Polarity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the polarity of the exported Advance Trigger. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get this property using:

- [DAQmxGetExportedAdvTrigPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__getter_1gad859d99a20096f514c8e985237a61791.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__pause__trigger__level.html language=enus -->
## TOPIC 02089: Level

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__pause__trigger__level.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__pause__trigger__level.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_PauseTrig_Lvl_ActiveLvlAttachmentsNone

### Level

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_PauseTrig_Lvl_ActiveLvl |  |

#### Attachments

None

Parent topic:

Pause Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__pause__trigger__level_1ga34c7a18aa7e69de1ddf9dcc064c36cd0.html language=enus -->
## TOPIC 02090: DAQmx_Exported_PauseTrig_Lvl_ActiveLvl

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__pause__trigger__level_1ga34c7a18aa7e69de1ddf9dcc064c36cd0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__pause__trigger__level_1ga34c7a18aa7e69de1ddf9dcc064c36cd0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_PauseTrig_Lvl_ActiveLvlRemarksData TypeDescriptionRestrictionsint32Specifies the active level of the exported Pause Trigger.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get/set/reset this proper

### DAQmx_Exported_PauseTrig_Lvl_ActiveLvl

#### Syntax

DAQmx_Exported_PauseTrig_Lvl_ActiveLvl

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the active level of the exported Pause Trigger. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedPauseTrigLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__getter_1ga73c7b4709324747bf64ec21dac9b950a.html)
- [DAQmxSetExportedPauseTrigLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__setter_1gac523e8681142a50e23bdeeadc46efee6.html)
- [DAQmxResetExportedPauseTrigLvlActiveLvl](group__ni-daqmx__c__functions__property__manipulation__resetter_1gac611c9f6b31e010c16735ca9d0beb310.html)

Parent topic:

Level

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__reference__trigger.html language=enus -->
## TOPIC 02091: Reference Trigger

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__reference__trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__reference__trigger.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPulseGroup membersNameDescriptionDAQmx_Exported_RefTrig_OutputTermAttachmentsNone

### Reference Trigger

#### Groups

- Pulse

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_RefTrig_OutputTerm |  |

#### Attachments

None

Parent topic:

Triggers

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__reference__trigger__pulse_1ga68a68e5475a9821ae6550a939617f757.html language=enus -->
## TOPIC 02092: DAQmx_Exported_RefTrig_Pulse_Polarity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__reference__trigger__pulse_1ga68a68e5475a9821ae6550a939617f757.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__reference__trigger__pulse_1ga68a68e5475a9821ae6550a939617f757.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_RefTrig_Pulse_PolarityRemarksData TypeDescriptionRestrictionsint32Specifies the polarity of the exported Reference Trigger.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get/set/reset this propert

### DAQmx_Exported_RefTrig_Pulse_Polarity

#### Syntax

DAQmx_Exported_RefTrig_Pulse_Polarity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the polarity of the exported Reference Trigger. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedRefTrigPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__getter_1gaafa72f479bae8e93ad7dbbbfd88f74a2.html)
- [DAQmxSetExportedRefTrigPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__setter_1ga1a1418554f8375397897d32867a5e728.html)
- [DAQmxResetExportedRefTrigPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga95269a01a37852213aacdd4c2df67e30.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger.html language=enus -->
## TOPIC 02093: Start Trigger

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPulseGroup membersNameDescriptionDAQmx_Exported_StartTrig_OutputTermAttachmentsNone

### Start Trigger

#### Groups

- Pulse

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_StartTrig_OutputTerm |  |

#### Attachments

None

Parent topic:

Triggers

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger_1gad7157fa283704ac107ee07cc9f9f6cdd.html language=enus -->
## TOPIC 02094: DAQmx_Exported_StartTrig_OutputTerm

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger_1gad7157fa283704ac107ee07cc9f9f6cdd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger_1gad7157fa283704ac107ee07cc9f9f6cdd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_StartTrig_OutputTermRemarksData TypeDescriptionRestrictionschar*Specifies the terminal to which to route the Start Trigger.You can get/set/reset this property using:DAQmxGetExportedStartTrigOutputTermDAQmxSetExportedStartTrigOutputTermDAQmxResetExportedStartTrigOutputTerm

### DAQmx_Exported_StartTrig_OutputTerm

#### Syntax

DAQmx_Exported_StartTrig_OutputTerm

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the terminal to which to route the Start Trigger. |  |

You can get/set/reset this property using:

- [DAQmxGetExportedStartTrigOutputTerm](group__ni-daqmx__c__functions__property__manipulation__getter_1gab23ccd3b47797850198ec447e0a50442.html)
- [DAQmxSetExportedStartTrigOutputTerm](group__ni-daqmx__c__functions__property__manipulation__setter_1gafad0bef831ff2da3762681c428e3ef65.html)
- [DAQmxResetExportedStartTrigOutputTerm](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga020f91174bd5990e9850e7cc6e9dee2e.html)

Parent topic:

Start Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger__pulse.html language=enus -->
## TOPIC 02095: Pulse

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger__pulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger__pulse.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Exported_StartTrig_Pulse_PolarityAttachmentsNone

### Pulse

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Exported_StartTrig_Pulse_Polarity |  |

#### Attachments

None

Parent topic:

Start Trigger

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger__pulse_1gacf3f80429420058e9c6b4cbeb9768089.html language=enus -->
## TOPIC 02096: DAQmx_Exported_StartTrig_Pulse_Polarity

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger__pulse_1gacf3f80429420058e9c6b4cbeb9768089.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__exportsignal__triggers__start__trigger__pulse_1gacf3f80429420058e9c6b4cbeb9768089.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Exported_StartTrig_Pulse_PolarityRemarksData TypeDescriptionRestrictionsint32Specifies the polarity of the exported Start Trigger.Valid valuesDAQmx_Val_ActiveHigh10095High state is the active state.DAQmx_Val_ActiveLow10096Low state is the active state.You can get/set/reset this property

### DAQmx_Exported_StartTrig_Pulse_Polarity

#### Syntax

DAQmx_Exported_StartTrig_Pulse_Polarity

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the polarity of the exported Start Trigger. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_ActiveHigh | 10095 | High state is the active state. |
| DAQmx_Val_ActiveLow | 10096 | Low state is the active state. |

You can get/set/reset this property using:

- [DAQmxGetExportedStartTrigPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__getter_1gab21179bac3230bf043ebe62a60f15578.html)
- [DAQmxSetExportedStartTrigPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__setter_1ga6548795c587f0b8486d9732f537f09a2.html)
- [DAQmxResetExportedStartTrigPulsePolarity](group__ni-daqmx__c__functions__property__manipulation__resetter_1gacc44543312706d096c91e20aeb370c2b.html)

Parent topic:

Pulse

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__persistedchannel_1ga26b20d3e66253093e8b7942f58323f4d.html language=enus -->
## TOPIC 02097: DAQmx_PersistedChan_AllowInteractiveDeletion

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__persistedchannel_1ga26b20d3e66253093e8b7942f58323f4d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__persistedchannel_1ga26b20d3e66253093e8b7942f58323f4d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PersistedChan_AllowInteractiveDeletionRemarksData TypeDescriptionRestrictionsbool32Indicates whether the global channel can be deleted through MAX.Not SettableYou can get this property using:DAQmxGetPersistedChanAllowInteractiveDeletion

### DAQmx_PersistedChan_AllowInteractiveDeletion

#### Syntax

DAQmx_PersistedChan_AllowInteractiveDeletion

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates whether the global channel can be deleted through MAX. | Not Settable |

You can get this property using:

- [DAQmxGetPersistedChanAllowInteractiveDeletion](group__ni-daqmx__c__functions__property__manipulation__getter_1ga51a24d9cc48b70a5af8b95c476a90600.html)

Parent topic:

PersistedChannel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__persistedchannel_1ga6c93f7494bd95f37d4b37b1ce5b09c77.html language=enus -->
## TOPIC 02098: DAQmx_PersistedChan_Author

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__persistedchannel_1ga6c93f7494bd95f37d4b37b1ce5b09c77.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__persistedchannel_1ga6c93f7494bd95f37d4b37b1ce5b09c77.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PersistedChan_AuthorRemarksData TypeDescriptionRestrictionschar*Indicates the author of the global channel.Not SettableYou can get this property using:DAQmxGetPersistedChanAuthor

### DAQmx_PersistedChan_Author

#### Syntax

DAQmx_PersistedChan_Author

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the author of the global channel. | Not Settable |

You can get this property using:

- [DAQmxGetPersistedChanAuthor](group__ni-daqmx__c__functions__property__manipulation__getter_1gac24683df6ce633f406952633ea961d30.html)

Parent topic:

PersistedChannel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__persistedchannel_1gabc01d630aa61bec6e72cdc1aa57669be.html language=enus -->
## TOPIC 02099: DAQmx_PersistedChan_AllowInteractiveEditing

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__persistedchannel_1gabc01d630aa61bec6e72cdc1aa57669be.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__persistedchannel_1gabc01d630aa61bec6e72cdc1aa57669be.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PersistedChan_AllowInteractiveEditingRemarksData TypeDescriptionRestrictionsbool32Indicates whether the global channel can be edited in the DAQ Assistant.Not SettableYou can get this property using:DAQmxGetPersistedChanAllowInteractiveEditing

### DAQmx_PersistedChan_AllowInteractiveEditing

#### Syntax

DAQmx_PersistedChan_AllowInteractiveEditing

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates whether the global channel can be edited in the DAQ Assistant. | Not Settable |

You can get this property using:

- [DAQmxGetPersistedChanAllowInteractiveEditing](group__ni-daqmx__c__functions__property__manipulation__getter_1gad689e2c481373427d42c6486cca1a332.html)

Parent topic:

PersistedChannel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__persistedscale.html language=enus -->
## TOPIC 02100: PersistedScale

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__persistedscale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__persistedscale.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_PersistedScale_AllowInteractiveDeletionDAQmx_PersistedScale_AllowInteractiveEditingDAQmx_PersistedScale_AuthorAttachmentsNone

### PersistedScale

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PersistedScale_AllowInteractiveDeletion |  |
| DAQmx_PersistedScale_AllowInteractiveEditing |  |
| DAQmx_PersistedScale_Author |  |

#### Attachments

None

Parent topic:

NI-DAQmx C Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__persistedscale_1ga7fbb6873c2b797ff2f03595557a94cb2.html language=enus -->
## TOPIC 02101: DAQmx_PersistedScale_AllowInteractiveEditing

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__persistedscale_1ga7fbb6873c2b797ff2f03595557a94cb2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__persistedscale_1ga7fbb6873c2b797ff2f03595557a94cb2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PersistedScale_AllowInteractiveEditingRemarksData TypeDescriptionRestrictionsbool32Indicates whether the custom scale can be edited in the DAQ Assistant.Not SettableYou can get this property using:DAQmxGetPersistedScaleAllowInteractiveEditing

### DAQmx_PersistedScale_AllowInteractiveEditing

#### Syntax

DAQmx_PersistedScale_AllowInteractiveEditing

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates whether the custom scale can be edited in the DAQ Assistant. | Not Settable |

You can get this property using:

- [DAQmxGetPersistedScaleAllowInteractiveEditing](group__ni-daqmx__c__functions__property__manipulation__getter_1gac730022674a4c84e0b3671aecfddc550.html)

Parent topic:

PersistedScale

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__persistedscale_1gadaff97b0b14ba76d96f1799d02c213d5.html language=enus -->
## TOPIC 02102: DAQmx_PersistedScale_Author

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__persistedscale_1gadaff97b0b14ba76d96f1799d02c213d5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__persistedscale_1gadaff97b0b14ba76d96f1799d02c213d5.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PersistedScale_AuthorRemarksData TypeDescriptionRestrictionschar*Indicates the author of the custom scale.Not SettableYou can get this property using:DAQmxGetPersistedScaleAuthor

### DAQmx_PersistedScale_Author

#### Syntax

DAQmx_PersistedScale_Author

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the author of the custom scale. | Not Settable |

You can get this property using:

- [DAQmxGetPersistedScaleAuthor](group__ni-daqmx__c__functions__property__manipulation__getter_1ga5b16dcffda9ba0f494ee50b688b04fc4.html)

Parent topic:

PersistedScale

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__input_1gaba36fd2fc0f8c6cc3ed5d4b9da9655e5.html language=enus -->
## TOPIC 02103: DAQmx_PhysicalChan_AI_SupportedMeasTypes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__input_1gaba36fd2fc0f8c6cc3ed5d4b9da9655e5.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__input_1gaba36fd2fc0f8c6cc3ed5d4b9da9655e5.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_AI_SupportedMeasTypesRemarksData TypeDescriptionRestrictionsint32*Indicates the measurement types supported by the channel.Not SettableValid valuesDAQmx_Val_Voltage10322Voltage measurement.DAQmx_Val_VoltageRMS10350Voltage RMS measurement.DAQmx_Val_Current10134Current measure

### DAQmx_PhysicalChan_AI_SupportedMeasTypes

#### Syntax

DAQmx_PhysicalChan_AI_SupportedMeasTypes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32* | Indicates the measurement types supported by the channel. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Voltage | 10322 | Voltage measurement. |
| DAQmx_Val_VoltageRMS | 10350 | Voltage RMS measurement. |
| DAQmx_Val_Current | 10134 | Current measurement. |
| DAQmx_Val_CurrentRMS | 10351 | Current RMS measurement. |
| DAQmx_Val_Voltage_CustomWithExcitation | 10323 | Voltage measurement with an excitation source. You can use this measurement type for custom sensors that require excitation, but you must use a custom scale to scale the measured voltage. |
| DAQmx_Val_Bridge | 15908 | Measure voltage ratios from a Wheatstone bridge. |
| DAQmx_Val_Freq_Voltage | 10181 | Frequency measurement using a frequency to voltage converter. |
| DAQmx_Val_Resistance | 10278 | Resistance measurement. |
| DAQmx_Val_Temp_TC | 10303 | Temperature measurement using a thermocouple. |
| DAQmx_Val_Temp_Thrmstr | 10302 | Temperature measurement using a thermistor. |
| DAQmx_Val_Temp_RTD | 10301 | Temperature measurement using an RTD. |
| DAQmx_Val_Temp_BuiltInSensor | 10311 | Temperature measurement using a built-in sensor on a terminal block or device. On SCXI modules, for example, this could be the CJC sensor. |
| DAQmx_Val_Strain_Gage | 10300 | Strain measurement. |
| DAQmx_Val_Rosette_Strain_Gage | 15980 | Strain measurement using a rosette strain gage. |
| DAQmx_Val_Position_LVDT | 10352 | Position measurement using an LVDT. |
| DAQmx_Val_Position_RVDT | 10353 | Position measurement using an RVDT. |
| DAQmx_Val_Position_EddyCurrentProximityProbe | 14835 | Position measurement using an eddy current proximity probe. |
| DAQmx_Val_Accelerometer | 10356 | Acceleration measurement using an accelerometer. |
| DAQmx_Val_Acceleration_Charge | 16104 | Acceleration measurement using a charge-based sensor. |
| DAQmx_Val_Acceleration_4WireDCVoltage | 16106 | Acceleration measurement using a 4 wire DC voltage based sensor. |
| DAQmx_Val_Velocity_IEPESensor | 15966 | Velocity measurement using an IEPE Sensor. |
| DAQmx_Val_Force_Bridge | 15899 | Force measurement using a bridge-based sensor. |
| DAQmx_Val_Force_IEPESensor | 15895 | Force measurement using an IEPE Sensor. |
| DAQmx_Val_Pressure_Bridge | 15902 | Pressure measurement using a bridge-based sensor. |
| DAQmx_Val_SoundPressure_Microphone | 10354 | Sound pressure measurement using a microphone. |
| DAQmx_Val_Torque_Bridge | 15905 | Torque measurement using a bridge-based sensor. |
| DAQmx_Val_TEDS_Sensor | 12531 | Measurement type defined by TEDS. |
| DAQmx_Val_Charge | 16105 | Charge measurement. |
| DAQmx_Val_Power | 16201 | Power source and measurement. |
| DAQmx_Val_Calculated_Power | 16204 | Calculated power measurement. |

You can get this property using:

- [DAQmxGetPhysicalChanAISupportedMeasTypes](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa19fc9abd2d88c0769082a3904935db4.html)

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__input__input__configuration_1ga3409748602b907a4c97859554f94acf0.html language=enus -->
## TOPIC 02104: DAQmx_PhysicalChan_AI_TermCfgs

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__input__input__configuration_1ga3409748602b907a4c97859554f94acf0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__input__input__configuration_1ga3409748602b907a4c97859554f94acf0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_AI_TermCfgsRemarksData TypeDescriptionRestrictionsint32Indicates the list of terminal configurations supported by the channel.Not SettableValid valuesDAQmx_Val_Bit_TermCfg_RSE1RSE terminal configurationDAQmx_Val_Bit_TermCfg_NRSE2NRSE terminal configurationDAQmx_Val_Bit_TermC

### DAQmx_PhysicalChan_AI_TermCfgs

#### Syntax

DAQmx_PhysicalChan_AI_TermCfgs

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the list of terminal configurations supported by the channel. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Bit_TermCfg_RSE | 1 | RSE terminal configuration |
| DAQmx_Val_Bit_TermCfg_NRSE | 2 | NRSE terminal configuration |
| DAQmx_Val_Bit_TermCfg_Diff | 4 | Differential terminal configuration |
| DAQmx_Val_Bit_TermCfg_PseudoDIFF | 8 | Pseudodifferential terminal configuration |

You can get this property using:

- [DAQmxGetPhysicalChanAITermCfgs](group__ni-daqmx__c__functions__property__manipulation__getter_1ga0d0efa13df757098745f609fd7bbed39.html)

Parent topic:

Input Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning.html language=enus -->
## TOPIC 02105: Signal Conditioning

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsSensor PowerGroup membersNoneAttachmentsNone

### Signal Conditioning

#### Groups

- Sensor Power

#### Group members

None

#### Attachments

None

Parent topic:

Analog Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power.html language=enus -->
## TOPIC 02106: Sensor Power

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPower ControlStatusGroup membersNameDescriptionDAQmx_PhysicalChan_AI_SensorPower_TypesDAQmx_PhysicalChan_AI_SensorPower_VoltageRangeValsAttachmentsNone

### Sensor Power

#### Groups

- Power Control
- Status

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_AI_SensorPower_Types |  |
| DAQmx_PhysicalChan_AI_SensorPower_VoltageRangeVals |  |

#### Attachments

None

Parent topic:

Signal Conditioning

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power_1ga6f11b051bb119e5c7a10b6dd495dd069.html language=enus -->
## TOPIC 02107: DAQmx_PhysicalChan_AI_SensorPower_VoltageRangeVals

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power_1ga6f11b051bb119e5c7a10b6dd495dd069.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power_1ga6f11b051bb119e5c7a10b6dd495dd069.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_AI_SensorPower_VoltageRangeValsRemarksData TypeDescriptionRestrictionsfloat64*Indicates pairs of sensor power voltage ranges supported by this channel. Each pair consists of the low value followed by the high value.Not SettableYou can get this property using:DAQmxGetPhysical

### DAQmx_PhysicalChan_AI_SensorPower_VoltageRangeVals

#### Syntax

DAQmx_PhysicalChan_AI_SensorPower_VoltageRangeVals

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64* | Indicates pairs of sensor power voltage ranges supported by this channel. Each pair consists of the low value followed by the high value. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanAISensorPowerVoltageRangeVals](group__ni-daqmx__c__functions__property__manipulation__getter_1gae7e5c7041c7a3f5e79e6a7d4ea1f5765.html)

Parent topic:

Sensor Power

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power__power__control.html language=enus -->
## TOPIC 02108: Power Control

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power__power__control.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power__power__control.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_PhysicalChan_AI_PowerControl_EnableDAQmx_PhysicalChan_AI_PowerControl_TypeDAQmx_PhysicalChan_AI_PowerControl_VoltageAttachmentsNone

### Power Control

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_AI_PowerControl_Enable |  |
| DAQmx_PhysicalChan_AI_PowerControl_Type |  |
| DAQmx_PhysicalChan_AI_PowerControl_Voltage |  |

#### Attachments

None

Parent topic:

Sensor Power

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power__power__control_1gaf643d876e9651054e654a341f8aa6a0f.html language=enus -->
## TOPIC 02109: DAQmx_PhysicalChan_AI_PowerControl_Type

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power__power__control_1gaf643d876e9651054e654a341f8aa6a0f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__input__signal__conditioning__sensor__power__power__control_1gaf643d876e9651054e654a341f8aa6a0f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_AI_PowerControl_TypeRemarksData TypeDescriptionRestrictionsint32Specifies the type of power supplied to the sensor.Valid valuesDAQmx_Val_DC10050Sensor power supply generates a single DC voltage level.DAQmx_Val_AC10045Sensor power supply generates an AC voltage.DAQmx_Val_Bipo

### DAQmx_PhysicalChan_AI_PowerControl_Type

#### Syntax

DAQmx_PhysicalChan_AI_PowerControl_Type

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the type of power supplied to the sensor. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_DC | 10050 | Sensor power supply generates a single DC voltage level. |
| DAQmx_Val_AC | 10045 | Sensor power supply generates an AC voltage. |
| DAQmx_Val_BipolarDC | 16147 | Sensor power supply generates a pair of DC voltage levels. |

You can get/set/reset this property using:

- [DAQmxGetPhysicalChanAIPowerControlType](group__ni-daqmx__c__functions__property__manipulation__getter_1ga03584c9cb506f08593ee98e494250ac2.html)
- [DAQmxSetPhysicalChanAIPowerControlType](group__ni-daqmx__c__functions__property__manipulation__setter_1ga030700ef086c3ea7207e18d0e78acf81.html)
- [DAQmxResetPhysicalChanAIPowerControlType](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga9ed925ee6374fcf6343e58ed29f2a1df.html)

Parent topic:

Power Control

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output.html language=enus -->
## TOPIC 02110: Analog Output

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedOutput ConfigurationGroup membersNameDescriptionDAQmx_PhysicalChan_AO_SupportedOutputTypesDAQmx_PhysicalChan_AO_SupportedPowerUpOutputTypesAttachmentsNone

### Analog Output

#### Groups

- Advanced
- Output Configuration

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_AO_SupportedOutputTypes |  |
| DAQmx_PhysicalChan_AO_SupportedPowerUpOutputTypes |  |

#### Attachments

None

Parent topic:

PhysicalChannel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output_1gabb2d09cae751a50f16e3a4496c468fd7.html language=enus -->
## TOPIC 02111: DAQmx_PhysicalChan_AO_SupportedOutputTypes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output_1gabb2d09cae751a50f16e3a4496c468fd7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output_1gabb2d09cae751a50f16e3a4496c468fd7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_AO_SupportedOutputTypesRemarksData TypeDescriptionRestrictionsint32*Indicates the output types supported by the channel.Not SettableValid valuesDAQmx_Val_Voltage10322Voltage generation.DAQmx_Val_Current10134Current generation.DAQmx_Val_FuncGen14750Function generation.You can

### DAQmx_PhysicalChan_AO_SupportedOutputTypes

#### Syntax

DAQmx_PhysicalChan_AO_SupportedOutputTypes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32* | Indicates the output types supported by the channel. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Voltage | 10322 | Voltage generation. |
| DAQmx_Val_Current | 10134 | Current generation. |
| DAQmx_Val_FuncGen | 14750 | Function generation. |

You can get this property using:

- [DAQmxGetPhysicalChanAOSupportedOutputTypes](group__ni-daqmx__c__functions__property__manipulation__getter_1ga49c0acbbe7b4569ff159c8c64a227acb.html)

Parent topic:

Analog Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced.html language=enus -->
## TOPIC 02112: Advanced

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsManual ControlPower AmplifierGroup membersNoneAttachmentsNone

### Advanced

#### Groups

- Manual Control
- Power Amplifier

#### Group members

None

#### Attachments

None

Parent topic:

Analog Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control.html language=enus -->
## TOPIC 02113: Manual Control

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_PhysicalChan_AO_ManualControlAmplitudeDAQmx_PhysicalChan_AO_ManualControlEnableDAQmx_PhysicalChan_AO_ManualControlFreqDAQmx_PhysicalChan_AO_ManualControl_ShortDetectedAttachmentsNone

### Manual Control

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_AO_ManualControlAmplitude |  |
| DAQmx_PhysicalChan_AO_ManualControlEnable |  |
| DAQmx_PhysicalChan_AO_ManualControlFreq |  |
| DAQmx_PhysicalChan_AO_ManualControl_ShortDetected |  |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control_1ga162afd651ea10c6950fe5bcab2f6d656.html language=enus -->
## TOPIC 02114: DAQmx_PhysicalChan_AO_ManualControl_ShortDetected

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control_1ga162afd651ea10c6950fe5bcab2f6d656.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control_1ga162afd651ea10c6950fe5bcab2f6d656.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_AO_ManualControl_ShortDetectedRemarksData TypeDescriptionRestrictionsbool32Indicates whether the physical channel is currently disabled due to a short detected on the channel.Not SettableYou can get this property using:DAQmxGetPhysicalChanAOManualControlShortDetected

### DAQmx_PhysicalChan_AO_ManualControl_ShortDetected

#### Syntax

DAQmx_PhysicalChan_AO_ManualControl_ShortDetected

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates whether the physical channel is currently disabled due to a short detected on the channel. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanAOManualControlShortDetected](group__ni-daqmx__c__functions__property__manipulation__getter_1ga3ce5def8b58cb8647d7a5859816aad83.html)

Parent topic:

Manual Control

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control_1ga48e74bdbdb1ca36c8b1512088729338f.html language=enus -->
## TOPIC 02115: DAQmx_PhysicalChan_AO_ManualControlEnable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control_1ga48e74bdbdb1ca36c8b1512088729338f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__manual__control_1ga48e74bdbdb1ca36c8b1512088729338f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_AO_ManualControlEnableRemarksData TypeDescriptionRestrictionsbool32Specifies if you can control the physical channel externally via a manual control located on the device. You cannot simultaneously control a channel manually and with NI-DAQmx.You can get/set/reset this prope

### DAQmx_PhysicalChan_AO_ManualControlEnable

#### Syntax

DAQmx_PhysicalChan_AO_ManualControlEnable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies if you can control the physical channel externally via a manual control located on the device. You cannot simultaneously control a channel manually and with NI-DAQmx. |  |

You can get/set/reset this property using:

- [DAQmxGetPhysicalChanAOManualControlEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga02611ee353519f5003d2634da369b091.html)
- [DAQmxSetPhysicalChanAOManualControlEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1ga2969e9561842cf5ddc73feb2c28237c7.html)
- [DAQmxResetPhysicalChanAOManualControlEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafb2f111beb9a2c68e22f590bb55766c5.html)

Parent topic:

Manual Control

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier.html language=enus -->
## TOPIC 02116: Power Amplifier

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCalibrationGroup membersNameDescriptionDAQmx_AO_PowerAmp_ChannelEnableDAQmx_AO_PowerAmp_OvercurrentDAQmx_AO_PowerAmp_ScalingCoeffAttachmentsNone

### Power Amplifier

#### Groups

- Calibration

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_PowerAmp_ChannelEnable |  |
| DAQmx_AO_PowerAmp_Overcurrent |  |
| DAQmx_AO_PowerAmp_ScalingCoeff |  |

#### Attachments

None

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier_1gad9cadf6aa075ac668b8fb0e713487041.html language=enus -->
## TOPIC 02117: DAQmx_AO_PowerAmp_ScalingCoeff

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier_1gad9cadf6aa075ac668b8fb0e713487041.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier_1gad9cadf6aa075ac668b8fb0e713487041.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_PowerAmp_ScalingCoeffRemarksData TypeDescriptionRestrictionsfloat64*Indicates the coefficients of a polynomial equation used to scale from pre-amplified values.Not SettableYou can get this property using:DAQmxGetAOPowerAmpScalingCoeff

### DAQmx_AO_PowerAmp_ScalingCoeff

#### Syntax

DAQmx_AO_PowerAmp_ScalingCoeff

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64* | Indicates the coefficients of a polynomial equation used to scale from pre-amplified values. | Not Settable |

You can get this property using:

- [DAQmxGetAOPowerAmpScalingCoeff](group__ni-daqmx__c__functions__property__manipulation__getter_1ga42f4091c943064e8a38f6ff428cfab32.html)

Parent topic:

Power Amplifier

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier_1gae75fd1bc50e181dc769adea9c3deb7c1.html language=enus -->
## TOPIC 02118: DAQmx_AO_PowerAmp_ChannelEnable

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier_1gae75fd1bc50e181dc769adea9c3deb7c1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier_1gae75fd1bc50e181dc769adea9c3deb7c1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_PowerAmp_ChannelEnableRemarksData TypeDescriptionRestrictionsbool32Specifies whether to enable or disable a channel for amplification. This property can also be used to check if a channel is enabled.You can get/set/reset this property using:DAQmxGetAOPowerAmpChannelEnableDAQmxSetAOPow

### DAQmx_AO_PowerAmp_ChannelEnable

#### Syntax

DAQmx_AO_PowerAmp_ChannelEnable

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether to enable or disable a channel for amplification. This property can also be used to check if a channel is enabled. |  |

You can get/set/reset this property using:

- [DAQmxGetAOPowerAmpChannelEnable](group__ni-daqmx__c__functions__property__manipulation__getter_1ga91ece2c5d836a8be1480c61dabc1d615.html)
- [DAQmxSetAOPowerAmpChannelEnable](group__ni-daqmx__c__functions__property__manipulation__setter_1gaf1b7a0ea0badb35cf48391a93f0bd1fa.html)
- [DAQmxResetAOPowerAmpChannelEnable](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaee1fa4b3bf4e0aa18fdeeec322700abc.html)

Parent topic:

Power Amplifier

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration.html language=enus -->
## TOPIC 02119: Calibration

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AO_PowerAmp_GainDAQmx_AO_PowerAmp_OffsetAttachmentsNone

### Calibration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AO_PowerAmp_Gain |  |
| DAQmx_AO_PowerAmp_Offset |  |

#### Attachments

None

Parent topic:

Power Amplifier

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration_1gab77f1e5b4a6c431287dce1d1d2af4b64.html language=enus -->
## TOPIC 02120: DAQmx_AO_PowerAmp_Gain

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration_1gab77f1e5b4a6c431287dce1d1d2af4b64.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration_1gab77f1e5b4a6c431287dce1d1d2af4b64.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_PowerAmp_GainRemarksData TypeDescriptionRestrictionsfloat64Indicates the calibrated gain of the channel.Not SettableYou can get this property using:DAQmxGetAOPowerAmpGain

### DAQmx_AO_PowerAmp_Gain

#### Syntax

DAQmx_AO_PowerAmp_Gain

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Indicates the calibrated gain of the channel. | Not Settable |

You can get this property using:

- [DAQmxGetAOPowerAmpGain](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf96ccb53d10f7012441585449cca418f.html)

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration_1gaf34747beb328a22926747fb18107ae4d.html language=enus -->
## TOPIC 02121: DAQmx_AO_PowerAmp_Offset

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration_1gaf34747beb328a22926747fb18107ae4d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__advanced__power__amplifier__calibration_1gaf34747beb328a22926747fb18107ae4d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AO_PowerAmp_OffsetRemarksData TypeDescriptionRestrictionsfloat64Indicates the calibrated offset of the channel in volts.Not SettableYou can get this property using:DAQmxGetAOPowerAmpOffset

### DAQmx_AO_PowerAmp_Offset

#### Syntax

DAQmx_AO_PowerAmp_Offset

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Indicates the calibrated offset of the channel in volts. | Not Settable |

You can get this property using:

- [DAQmxGetAOPowerAmpOffset](group__ni-daqmx__c__functions__property__manipulation__getter_1ga13a6a1ca8cbf29e368b4e9c6d9804ad5.html)

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__analog__output__output__configuration_1gaec7eedc8f89d04d484a370c58d88a4be.html language=enus -->
## TOPIC 02122: DAQmx_PhysicalChan_AO_TermCfgs

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__analog__output__output__configuration_1gaec7eedc8f89d04d484a370c58d88a4be.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__analog__output__output__configuration_1gaec7eedc8f89d04d484a370c58d88a4be.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_AO_TermCfgsRemarksData TypeDescriptionRestrictionsint32Indicates the list of terminal configurations supported by the channel.Not SettableValid valuesDAQmx_Val_Bit_TermCfg_RSE1RSE terminal configurationDAQmx_Val_Bit_TermCfg_NRSE2NRSE terminal configurationDAQmx_Val_Bit_TermC

### DAQmx_PhysicalChan_AO_TermCfgs

#### Syntax

DAQmx_PhysicalChan_AO_TermCfgs

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Indicates the list of terminal configurations supported by the channel. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Bit_TermCfg_RSE | 1 | RSE terminal configuration |
| DAQmx_Val_Bit_TermCfg_NRSE | 2 | NRSE terminal configuration |
| DAQmx_Val_Bit_TermCfg_Diff | 4 | Differential terminal configuration |
| DAQmx_Val_Bit_TermCfg_PseudoDIFF | 8 | Pseudodifferential terminal configuration |

You can get this property using:

- [DAQmxGetPhysicalChanAOTermCfgs](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1798e95b27dd9623ae509016164d6c44.html)

Parent topic:

Output Configuration

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__counter__output.html language=enus -->
## TOPIC 02123: Counter Output

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__counter__output.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__counter__output.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_PhysicalChan_CO_SupportedOutputTypesAttachmentsNone

### Counter Output

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_CO_SupportedOutputTypes |  |

#### Attachments

None

Parent topic:

PhysicalChannel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__counter__output_1ga0cb58fb6dc1ff12b240e87037e7be460.html language=enus -->
## TOPIC 02124: DAQmx_PhysicalChan_CO_SupportedOutputTypes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__counter__output_1ga0cb58fb6dc1ff12b240e87037e7be460.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__counter__output_1ga0cb58fb6dc1ff12b240e87037e7be460.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_CO_SupportedOutputTypesRemarksData TypeDescriptionRestrictionsint32*Indicates the output types supported by the channel.Not SettableValid valuesDAQmx_Val_Pulse_Time10269Generate pulses defined by the time the pulse is at a low state and the time the pulse is at a high state.

### DAQmx_PhysicalChan_CO_SupportedOutputTypes

#### Syntax

DAQmx_PhysicalChan_CO_SupportedOutputTypes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32* | Indicates the output types supported by the channel. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Pulse_Time | 10269 | Generate pulses defined by the time the pulse is at a low state and the time the pulse is at a high state. |
| DAQmx_Val_Pulse_Freq | 10119 | Generate digital pulses defined by frequency and duty cycle. |
| DAQmx_Val_Pulse_Ticks | 10268 | Generate digital pulses defined by the number of timebase ticks that the pulse is at a low state and the number of timebase ticks that the pulse is at a high state. |

You can get this property using:

- [DAQmxGetPhysicalChanCOSupportedOutputTypes](group__ni-daqmx__c__functions__property__manipulation__getter_1ga4d155fe43982fb8a7864f6ce434ab196.html)

Parent topic:

Counter Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital_1gabfbf75f6d2ffda1e4b91b878bb680483.html language=enus -->
## TOPIC 02125: DAQmx_PhysicalChan_Dig_PortLogicFamily

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital_1gabfbf75f6d2ffda1e4b91b878bb680483.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital_1gabfbf75f6d2ffda1e4b91b878bb680483.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_Dig_PortLogicFamilyRemarks| Data Type | Description | Restrictions | | -----— | -----— | -----— | -----— | | int32 | Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a gro

### DAQmx_PhysicalChan_Dig_PortLogicFamily

#### Syntax

DAQmx_PhysicalChan_Dig_PortLogicFamily

#### Remarks

| Data Type | Description | Restrictions | | -----— | -----— | -----— | -----— | | int32 | Specifies the digital port logic family to use for acquisition and generation. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. | |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_1point8V | 16184 | Compatible with 1.8 V CMOS signals. |
| DAQmx_Val_2point5V | 14620 | Compatible with 2.5 V CMOS signals. |
| DAQmx_Val_3point3V | 14621 | Compatible with LVTTL signals. |
| DAQmx_Val_5V | 14619 | Compatible with TTL and 5 V CMOS signals. |

You can get/set/reset this property using:

- [DAQmxGetPhysicalChanDigPortLogicFamily](group__ni-daqmx__c__functions__property__manipulation__getter_1ga4527946f80de1ab51dc95f6712a66882.html)
- [DAQmxSetPhysicalChanDigPortLogicFamily](group__ni-daqmx__c__functions__property__manipulation__setter_1ga9b08c8a3ebab3c1252c7897bcb14621d.html)
- [DAQmxResetPhysicalChanDigPortLogicFamily](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga2b09432656d5588f9e01534dbfaf2ce0.html)

Parent topic:

Digital

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__input.html language=enus -->
## TOPIC 02126: Digital Input

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__input.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__input.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTimingGroup membersNameDescriptionDAQmx_PhysicalChan_DI_PortWidthAttachmentsNone

### Digital Input

#### Groups

- Timing

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_DI_PortWidth |  |

#### Attachments

None

Parent topic:

PhysicalChannel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__input_1gafa2f302474f9626bc8830ac05871e2f1.html language=enus -->
## TOPIC 02127: DAQmx_PhysicalChan_DI_PortWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__input_1gafa2f302474f9626bc8830ac05871e2f1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__input_1gafa2f302474f9626bc8830ac05871e2f1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_DI_PortWidthRemarksData TypeDescriptionRestrictionsuInt32Indicates in bits the width of digital input port.Not SettableYou can get this property using:DAQmxGetPhysicalChanDIPortWidth

### DAQmx_PhysicalChan_DI_PortWidth

#### Syntax

DAQmx_PhysicalChan_DI_PortWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates in bits the width of digital input port. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanDIPortWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1gae91dfb53e6ee68b0c465fceca80b53c1.html)

Parent topic:

Digital Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__input__timing.html language=enus -->
## TOPIC 02128: Timing

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__input__timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__input__timing.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_PhysicalChan_DI_ChangeDetectSupportedDAQmx_PhysicalChan_DI_SampClkSupportedDAQmx_PhysicalChan_DI_SampModesAttachmentsNone

### Timing

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_DI_ChangeDetectSupported |  |
| DAQmx_PhysicalChan_DI_SampClkSupported |  |
| DAQmx_PhysicalChan_DI_SampModes |  |

#### Attachments

None

Parent topic:

Digital Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1ga1fc1f029a6acb1ec67b9d36eb3b24c26.html language=enus -->
## TOPIC 02129: DAQmx_PhysicalChan_DI_ChangeDetectSupported

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1ga1fc1f029a6acb1ec67b9d36eb3b24c26.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1ga1fc1f029a6acb1ec67b9d36eb3b24c26.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_DI_ChangeDetectSupportedRemarksData TypeDescriptionRestrictionsbool32Indicates if the change detection timing type is supported for the digital input physical channel.Not SettableYou can get this property using:DAQmxGetPhysicalChanDIChangeDetectSupported

### DAQmx_PhysicalChan_DI_ChangeDetectSupported

#### Syntax

DAQmx_PhysicalChan_DI_ChangeDetectSupported

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the change detection timing type is supported for the digital input physical channel. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanDIChangeDetectSupported](group__ni-daqmx__c__functions__property__manipulation__getter_1ga15410659d2bb3a35109ef17916520c1f.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1gaa9ea4ea63d17b82340492453172b9c23.html language=enus -->
## TOPIC 02130: DAQmx_PhysicalChan_DI_SampModes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1gaa9ea4ea63d17b82340492453172b9c23.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1gaa9ea4ea63d17b82340492453172b9c23.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_DI_SampModesRemarksData TypeDescriptionRestrictionsint32*Indicates the sample modes supported by devices that support sample clocked digital input.Not SettableValid valuesDAQmx_Val_FiniteSamps10178Acquire or generate a finite number of samples.DAQmx_Val_ContSamps10123Acquire

### DAQmx_PhysicalChan_DI_SampModes

#### Syntax

DAQmx_PhysicalChan_DI_SampModes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32* | Indicates the sample modes supported by devices that support sample clocked digital input. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_FiniteSamps | 10178 | Acquire or generate a finite number of samples. |
| DAQmx_Val_ContSamps | 10123 | Acquire or generate samples until you stop the task. |
| DAQmx_Val_HWTimedSinglePoint | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

You can get this property using:

- [DAQmxGetPhysicalChanDISampModes](group__ni-daqmx__c__functions__property__manipulation__getter_1gabc8c50a6461d610b462d83798dbe9947.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1gad4678d0bd40d9e62368811ab826ad629.html language=enus -->
## TOPIC 02131: DAQmx_PhysicalChan_DI_SampClkSupported

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1gad4678d0bd40d9e62368811ab826ad629.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__input__timing_1gad4678d0bd40d9e62368811ab826ad629.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_DI_SampClkSupportedRemarksData TypeDescriptionRestrictionsbool32Indicates if the sample clock timing type is supported for the digital input physical channel.Not SettableYou can get this property using:DAQmxGetPhysicalChanDISampClkSupported

### DAQmx_PhysicalChan_DI_SampClkSupported

#### Syntax

DAQmx_PhysicalChan_DI_SampClkSupported

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the sample clock timing type is supported for the digital input physical channel. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanDISampClkSupported](group__ni-daqmx__c__functions__property__manipulation__getter_1gaceb9980627abf712837854e00c37bdf5.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__output_1ga8f3663ee967b0d8be35f3b4a8f2cc5bf.html language=enus -->
## TOPIC 02132: DAQmx_PhysicalChan_DO_PortWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__output_1ga8f3663ee967b0d8be35f3b4a8f2cc5bf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__output_1ga8f3663ee967b0d8be35f3b4a8f2cc5bf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_DO_PortWidthRemarksData TypeDescriptionRestrictionsuInt32Indicates in bits the width of digital output port.Not SettableYou can get this property using:DAQmxGetPhysicalChanDOPortWidth

### DAQmx_PhysicalChan_DO_PortWidth

#### Syntax

DAQmx_PhysicalChan_DO_PortWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates in bits the width of digital output port. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanDOPortWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1ga6a126a0b53bf305ae49234f3ce168fac.html)

Parent topic:

Digital Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__output__timing.html language=enus -->
## TOPIC 02133: Timing

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__output__timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__output__timing.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_PhysicalChan_DO_SampClkSupportedDAQmx_PhysicalChan_DO_SampModesAttachmentsNone

### Timing

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_DO_SampClkSupported |  |
| DAQmx_PhysicalChan_DO_SampModes |  |

#### Attachments

None

Parent topic:

Digital Output

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__output__timing_1ga2acc842bf6a5fc6c50eff063901d15aa.html language=enus -->
## TOPIC 02134: DAQmx_PhysicalChan_DO_SampModes

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__output__timing_1ga2acc842bf6a5fc6c50eff063901d15aa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__output__timing_1ga2acc842bf6a5fc6c50eff063901d15aa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_DO_SampModesRemarksData TypeDescriptionRestrictionsint32*Indicates the sample modes supported by devices that support sample clocked digital output.Not SettableValid valuesDAQmx_Val_FiniteSamps10178Acquire or generate a finite number of samples.DAQmx_Val_ContSamps10123Acquir

### DAQmx_PhysicalChan_DO_SampModes

#### Syntax

DAQmx_PhysicalChan_DO_SampModes

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32* | Indicates the sample modes supported by devices that support sample clocked digital output. | Not Settable |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_FiniteSamps | 10178 | Acquire or generate a finite number of samples. |
| DAQmx_Val_ContSamps | 10123 | Acquire or generate samples until you stop the task. |
| DAQmx_Val_HWTimedSinglePoint | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

You can get this property using:

- [DAQmxGetPhysicalChanDOSampModes](group__ni-daqmx__c__functions__property__manipulation__getter_1ga94db2c5e5f246f7935bf6699617c3962.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__digital__output__timing_1ga6878dc64de0eea8fdc74c03d942d481d.html language=enus -->
## TOPIC 02135: DAQmx_PhysicalChan_DO_SampClkSupported

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__digital__output__timing_1ga6878dc64de0eea8fdc74c03d942d481d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__digital__output__timing_1ga6878dc64de0eea8fdc74c03d942d481d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_DO_SampClkSupportedRemarksData TypeDescriptionRestrictionsbool32Indicates if the sample clock timing type is supported for the digital output physical channel.Not SettableYou can get this property using:DAQmxGetPhysicalChanDOSampClkSupported

### DAQmx_PhysicalChan_DO_SampClkSupported

#### Syntax

DAQmx_PhysicalChan_DO_SampClkSupported

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the sample clock timing type is supported for the digital output physical channel. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanDOSampClkSupported](group__ni-daqmx__c__functions__property__manipulation__getter_1gac3dc67db4b0352d65c2e6ce1a82d0a38.html)

Parent topic:

Timing

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__teds.html language=enus -->
## TOPIC 02136: TEDS

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__teds.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__teds.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_PhysicalChan_TEDS_BitStreamDAQmx_PhysicalChan_TEDS_MfgIDDAQmx_PhysicalChan_TEDS_ModelNumDAQmx_PhysicalChan_TEDS_SerialNumDAQmx_PhysicalChan_TEDS_TemplateIDsDAQmx_PhysicalChan_TEDS_VersionLetterDAQmx_PhysicalChan_TEDS_VersionNumAttachmentsNone

### TEDS

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_PhysicalChan_TEDS_BitStream |  |
| DAQmx_PhysicalChan_TEDS_MfgID |  |
| DAQmx_PhysicalChan_TEDS_ModelNum |  |
| DAQmx_PhysicalChan_TEDS_SerialNum |  |
| DAQmx_PhysicalChan_TEDS_TemplateIDs |  |
| DAQmx_PhysicalChan_TEDS_VersionLetter |  |
| DAQmx_PhysicalChan_TEDS_VersionNum |  |

#### Attachments

None

Parent topic:

PhysicalChannel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__teds_1ga4e3f0592784cfda6862d1ca25334c418.html language=enus -->
## TOPIC 02137: DAQmx_PhysicalChan_TEDS_ModelNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__teds_1ga4e3f0592784cfda6862d1ca25334c418.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__teds_1ga4e3f0592784cfda6862d1ca25334c418.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_TEDS_ModelNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the model number of the sensor.Not SettableYou can get this property using:DAQmxGetPhysicalChanTEDSModelNum

### DAQmx_PhysicalChan_TEDS_ModelNum

#### Syntax

DAQmx_PhysicalChan_TEDS_ModelNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the model number of the sensor. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanTEDSModelNum](group__ni-daqmx__c__functions__property__manipulation__getter_1gae0e396e66fa30bd7a64f5afc535514b9.html)

Parent topic:

TEDS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__teds_1ga9c3ef23bed50cbd7dd8bade4f438ac3e.html language=enus -->
## TOPIC 02138: DAQmx_PhysicalChan_TEDS_MfgID

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__teds_1ga9c3ef23bed50cbd7dd8bade4f438ac3e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__teds_1ga9c3ef23bed50cbd7dd8bade4f438ac3e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_TEDS_MfgIDRemarksData TypeDescriptionRestrictionsuInt32Indicates the manufacturer ID of the sensor.Not SettableYou can get this property using:DAQmxGetPhysicalChanTEDSMfgID

### DAQmx_PhysicalChan_TEDS_MfgID

#### Syntax

DAQmx_PhysicalChan_TEDS_MfgID

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the manufacturer ID of the sensor. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanTEDSMfgID](group__ni-daqmx__c__functions__property__manipulation__getter_1gacdd4e74238e11814c3dad92700e9581d.html)

Parent topic:

TEDS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__teds_1gaaba5c304222f261173b88fdb13eb3a7e.html language=enus -->
## TOPIC 02139: DAQmx_PhysicalChan_TEDS_VersionLetter

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__teds_1gaaba5c304222f261173b88fdb13eb3a7e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__teds_1gaaba5c304222f261173b88fdb13eb3a7e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_TEDS_VersionLetterRemarksData TypeDescriptionRestrictionschar*Indicates the version letter of the sensor.Not SettableYou can get this property using:DAQmxGetPhysicalChanTEDSVersionLetter

### DAQmx_PhysicalChan_TEDS_VersionLetter

#### Syntax

DAQmx_PhysicalChan_TEDS_VersionLetter

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the version letter of the sensor. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanTEDSVersionLetter](group__ni-daqmx__c__functions__property__manipulation__getter_1ga91be75faced2de8f65328b05b35c368f.html)

Parent topic:

TEDS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__physicalchannel__teds_1gaec980359203be25a597ac117b25ebc6d.html language=enus -->
## TOPIC 02140: DAQmx_PhysicalChan_TEDS_SerialNum

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__physicalchannel__teds_1gaec980359203be25a597ac117b25ebc6d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__physicalchannel__teds_1gaec980359203be25a597ac117b25ebc6d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_PhysicalChan_TEDS_SerialNumRemarksData TypeDescriptionRestrictionsuInt32Indicates the serial number of the sensor.Not SettableYou can get this property using:DAQmxGetPhysicalChanTEDSSerialNum

### DAQmx_PhysicalChan_TEDS_SerialNum

#### Syntax

DAQmx_PhysicalChan_TEDS_SerialNum

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the serial number of the sensor. | Not Settable |

You can get this property using:

- [DAQmxGetPhysicalChanTEDSSerialNum](group__ni-daqmx__c__functions__property__manipulation__getter_1gae4e003de0af29ca99cd7c97aff516b4c.html)

Parent topic:

TEDS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read_1gab0c240f5e4f2d7b493d178cbff139c13.html language=enus -->
## TOPIC 02141: DAQmx_Read_OverWrite

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read_1gab0c240f5e4f2d7b493d178cbff139c13.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read_1gab0c240f5e4f2d7b493d178cbff139c13.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OverWriteRemarksData TypeDescriptionRestrictionsint32Specifies whether to overwrite samples in the buffer that you have not yet read.Valid valuesDAQmx_Val_OverwriteUnreadSamps10252When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the

### DAQmx_Read_OverWrite

#### Syntax

DAQmx_Read_OverWrite

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies whether to overwrite samples in the buffer that you have not yet read. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_OverwriteUnreadSamps | 10252 | When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the unread samples with new ones. You can read the new samples by setting RelativeTo to DAQmx_Val_MostRecentSamp and setting Offset to the appropriate number of samples. |
| DAQmx_Val_DoNotOverwriteUnreadSamps | 10159 | The acquisition stops when it encounters a sample in the buffer that you have not read. |

You can get/set/reset this property using:

- [DAQmxGetReadOverWrite](group__ni-daqmx__c__functions__property__manipulation__getter_1ga3238089a7e207c1370f0590a2f6684ea.html)
- [DAQmxSetReadOverWrite](group__ni-daqmx__c__functions__property__manipulation__setter_1ga37dcaea7e80bfde1952e926dde1899a9.html)
- [DAQmxResetReadOverWrite](group__ni-daqmx__c__functions__property__manipulation__resetter_1gab33c93aea4da66dbd8b6c359bd391946.html)

Parent topic:

Read

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read_1gac024f58278dc668323e3d9036ad74cae.html language=enus -->
## TOPIC 02142: DAQmx_Read_Offset

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read_1gac024f58278dc668323e3d9036ad74cae.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read_1gac024f58278dc668323e3d9036ad74cae.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OffsetRemarksData TypeDescriptionRestrictionsint32Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with RelativeTo.You can get/set/reset this property using:DAQmxGetReadOffsetDAQmxSetReadOffsetDAQmxRes

### DAQmx_Read_Offset

#### Syntax

DAQmx_Read_Offset

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with RelativeTo. |  |

You can get/set/reset this property using:

- [DAQmxGetReadOffset](group__ni-daqmx__c__functions__property__manipulation__getter_1ga8ce613597ba1f47a206816b44c26c9d7.html)
- [DAQmxSetReadOffset](group__ni-daqmx__c__functions__property__manipulation__setter_1ga49131c7a2d3024cce641f61cdfbf6042.html)
- [DAQmxResetReadOffset](group__ni-daqmx__c__functions__property__manipulation__resetter_1gabfa3a5615363c9dc9b6d589a920e63ac.html)

Parent topic:

Read

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read_1gadcd24cbe547e4af966f562d9e5fe537c.html language=enus -->
## TOPIC 02143: DAQmx_Read_AutoStart

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read_1gadcd24cbe547e4af966f562d9e5fe537c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read_1gadcd24cbe547e4af966f562d9e5fe537c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_AutoStartRemarksData TypeDescriptionRestrictionsbool32Specifies if an NI-DAQmx Read function automatically starts the task if you did not start the task explicitly by using DAQmxStartTask(). The default value is TRUE. When an NI-DAQmx Read function starts a finite acquisition task,

### DAQmx_Read_AutoStart

#### Syntax

DAQmx_Read_AutoStart

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies if an NI-DAQmx Read function automatically starts the task if you did not start the task explicitly by using DAQmxStartTask(). The default value is TRUE. When an NI-DAQmx Read function starts a finite acquisition task, it also stops the task after reading the last sample. |  |

You can get/set/reset this property using:

- [DAQmxGetReadAutoStart](group__ni-daqmx__c__functions__property__manipulation__getter_1gae39722b67942e36b4d7b9b05fa534d9d.html)
- [DAQmxSetReadAutoStart](group__ni-daqmx__c__functions__property__manipulation__setter_1ga7ff42a9fc29b09a542a1fe789119e4cc.html)
- [DAQmxResetReadAutoStart](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafdc48c1f1c72aaa0867c43667073a3ec.html)

Parent topic:

Read

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read_1gaf6d15fd93876a25701a1a1df337aae22.html language=enus -->
## TOPIC 02144: DAQmx_Read_RelativeTo

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read_1gaf6d15fd93876a25701a1a1df337aae22.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read_1gaf6d15fd93876a25701a1a1df337aae22.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_RelativeToRemarksData TypeDescriptionRestrictionsint32Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with Offset, the read operation begins at that offset relative to the point you select with this property. The default value is D

### DAQmx_Read_RelativeTo

#### Syntax

DAQmx_Read_RelativeTo

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with Offset, the read operation begins at that offset relative to the point you select with this property. The default value is DAQmx_Val_CurrReadPos unless you configure a Reference Trigger for the task. If you configure a Reference Trigger, the default value is DAQmx_Val_FirstPretrigSamp. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_FirstSample | 10424 | Start reading samples relative to the first sample acquired. |
| DAQmx_Val_CurrReadPos | 10425 | Start reading samples relative to the last sample returned by the previous read. For the first read operation, this position is the first sample acquired or the first pretrigger sample if you configured a reference trigger for the task. |
| DAQmx_Val_RefTrig | 10426 | Start reading samples relative to the first sample after the reference trigger occurred. |
| DAQmx_Val_FirstPretrigSamp | 10427 | Start reading samples relative to the first pretrigger sample. You specify the number of pretrigger samples to acquire when you configure a reference trigger. |
| DAQmx_Val_MostRecentSamp | 10428 | Start reading samples relative to the next sample acquired. For example, use this value and set Offset to -1 to read the last sample acquired. |

You can get/set/reset this property using:

- [DAQmxGetReadRelativeTo](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7957dffef7b9f95ec51527b87c60312f.html)
- [DAQmxSetReadRelativeTo](group__ni-daqmx__c__functions__property__manipulation__setter_1ga40f7824693cc8317a2de5d409747a46a.html)
- [DAQmxResetReadRelativeTo](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga1714346ea11cd580f4bb83e17ae8bc7a.html)

Parent topic:

Read

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__advanced.html language=enus -->
## TOPIC 02145: Advanced

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__advanced.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDigital InputGroup membersNameDescriptionDAQmx_Read_NumChansDAQmx_Read_RawDataWidthAttachmentsNone

### Advanced

#### Groups

- Digital Input

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_NumChans |  |
| DAQmx_Read_RawDataWidth |  |

#### Attachments

None

Parent topic:

Read

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__advanced_1ga26765a6d551d8e1fa60c1823f4cb6ba3.html language=enus -->
## TOPIC 02146: DAQmx_Read_NumChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__advanced_1ga26765a6d551d8e1fa60c1823f4cb6ba3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__advanced_1ga26765a6d551d8e1fa60c1823f4cb6ba3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_NumChansRemarksData TypeDescriptionRestrictionsuInt32Indicates the number of channels that an NI-DAQmx Read function reads from the task. This value is the number of channels in the task or the number of channels you specify with Channels to Read.Not SettableYou can get this propert

### DAQmx_Read_NumChans

#### Syntax

DAQmx_Read_NumChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the number of channels that an NI-DAQmx Read function reads from the task. This value is the number of channels in the task or the number of channels you specify with Channels to Read. | Not Settable |

You can get this property using:

- [DAQmxGetReadNumChans](group__ni-daqmx__c__functions__property__manipulation__getter_1gadf635166a83f82e677953b696821a188.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__advanced_1ga457eb53c5e5b174fa8abd1b567a52083.html language=enus -->
## TOPIC 02147: DAQmx_Read_RawDataWidth

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__advanced_1ga457eb53c5e5b174fa8abd1b567a52083.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__advanced_1ga457eb53c5e5b174fa8abd1b567a52083.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_RawDataWidthRemarksData TypeDescriptionRestrictionsuInt32Indicates in bytes the size of a raw sample from the task.Not SettableYou can get this property using:DAQmxGetReadRawDataWidth

### DAQmx_Read_RawDataWidth

#### Syntax

DAQmx_Read_RawDataWidth

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates in bytes the size of a raw sample from the task. | Not Settable |

You can get this property using:

- [DAQmxGetReadRawDataWidth](group__ni-daqmx__c__functions__property__manipulation__getter_1ga297affc77bd4fc90d3b69f2f9d06dc81.html)

Parent topic:

Advanced

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__advanced__digital__input_1ga45d6fc546db4ffe3f018d1586d8f0dc2.html language=enus -->
## TOPIC 02148: DAQmx_Read_DigitalLines_BytesPerChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__advanced__digital__input_1ga45d6fc546db4ffe3f018d1586d8f0dc2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__advanced__digital__input_1ga45d6fc546db4ffe3f018d1586d8f0dc2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_DigitalLines_BytesPerChanRemarksData TypeDescriptionRestrictionsuInt32Indicates the number of bytes per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra bytes are FALSE.Not SettableYou can get this property usin

### DAQmx_Read_DigitalLines_BytesPerChan

#### Syntax

DAQmx_Read_DigitalLines_BytesPerChan

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the number of bytes per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra bytes are FALSE. | Not Settable |

You can get this property using:

- [DAQmxGetReadDigitalLinesBytesPerChan](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa630abd5e2e89cb3c7b018c455f1b62a.html)

Parent topic:

Digital Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__advanced__digital__input_1gad88ef9ef7ea512c145932d052762ebbe.html language=enus -->
## TOPIC 02149: DAQmx_Read_WaitMode

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__advanced__digital__input_1gad88ef9ef7ea512c145932d052762ebbe.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__advanced__digital__input_1gad88ef9ef7ea512c145932d052762ebbe.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_WaitModeRemarksData TypeDescriptionRestrictionsint32Specifies how an NI-DAQmx Read function waits for samples to become available.Valid valuesDAQmx_Val_WaitForInterrupt12523Check for available samples when the system receives an interrupt service request. This mode is the most CPU e

### DAQmx_Read_WaitMode

#### Syntax

DAQmx_Read_WaitMode

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies how an NI-DAQmx Read function waits for samples to become available. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_WaitForInterrupt | 12523 | Check for available samples when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates. |
| DAQmx_Val_Poll | 12524 | Repeatedly check for available samples as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |
| DAQmx_Val_Yield | 12525 | Repeatedly check for available samples, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency. |
| DAQmx_Val_Sleep | 12547 | Check for available samples once per the amount of time specified in Sleep Time. |

You can get/set/reset this property using:

- [DAQmxGetReadWaitMode](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf53525408b669b52cdfe013c938c245b.html)
- [DAQmxSetReadWaitMode](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3ee9fe161f08e46fa49397ed2e0f66f5.html)
- [DAQmxResetReadWaitMode](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga646c79b9ccc22c24350a48e53e206217.html)

Parent topic:

Digital Input

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__logging.html language=enus -->
## TOPIC 02150: Logging

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__logging.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__logging.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsTDMSGroup membersNameDescriptionDAQmx_Logging_FilePathDAQmx_Logging_ModeAttachmentsNone

### Logging

#### Groups

- TDMS

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Logging_FilePath |  |
| DAQmx_Logging_Mode |  |

#### Attachments

None

Parent topic:

Read

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__logging__tdms.html language=enus -->
## TOPIC 02151: TDMS

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__logging__tdms.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__logging__tdms.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Logging_FilePreallocationSizeDAQmx_Logging_FileWriteSizeDAQmx_Logging_PauseDAQmx_Logging_SampsPerFileDAQmx_Logging_TDMS_GroupNameDAQmx_Logging_TDMS_OperationAttachmentsNone

### TDMS

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Logging_FilePreallocationSize |  |
| DAQmx_Logging_FileWriteSize |  |
| DAQmx_Logging_Pause |  |
| DAQmx_Logging_SampsPerFile |  |
| DAQmx_Logging_TDMS_GroupName |  |
| DAQmx_Logging_TDMS_Operation |  |

#### Attachments

None

Parent topic:

Logging

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__logging__tdms_1ga213159a398460f4897c37bf4459b640c.html language=enus -->
## TOPIC 02152: DAQmx_Logging_TDMS_GroupName

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__logging__tdms_1ga213159a398460f4897c37bf4459b640c.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__logging__tdms_1ga213159a398460f4897c37bf4459b640c.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Logging_TDMS_GroupNameRemarksData TypeDescriptionRestrictionschar*Specifies the name of the group to create within the TDMS file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the gr

### DAQmx_Logging_TDMS_GroupName

#### Syntax

DAQmx_Logging_TDMS_GroupName

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies the name of the group to create within the TDMS file for data from this task. If you append data to an existing file and the specified group already exists, NI-DAQmx appends a number symbol and a number to the group name, incrementing that number until finding a group name that does not exist. For example, if you specify a group name of Voltage Task, and that group already exists, NI-DAQmx assigns the group name Voltage Task #1, then Voltage Task #2. |  |

You can get/set/reset this property using:

- [DAQmxGetLoggingTDMSGroupName](group__ni-daqmx__c__functions__property__manipulation__getter_1ga382f8c48d62cc533f3d8f5842a735985.html)
- [DAQmxSetLoggingTDMSGroupName](group__ni-daqmx__c__functions__property__manipulation__setter_1ga49cd5282161931549c9b75e208131780.html)
- [DAQmxResetLoggingTDMSGroupName](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga596512fff14915a8cd58cd3c010a4341.html)

Parent topic:

TDMS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__logging__tdms_1gab68231b8d8629646d9dfe9bddc93a2f6.html language=enus -->
## TOPIC 02153: DAQmx_Logging_TDMS_Operation

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__logging__tdms_1gab68231b8d8629646d9dfe9bddc93a2f6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__logging__tdms_1gab68231b8d8629646d9dfe9bddc93a2f6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Logging_TDMS_OperationRemarksData TypeDescriptionRestrictionsint32Specifies how to open the TDMS file.Valid valuesDAQmx_Val_Open10437Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx returns an error.DAQmx_Val_OpenOrCreate15846Open an existing

### DAQmx_Logging_TDMS_Operation

#### Syntax

DAQmx_Logging_TDMS_Operation

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies how to open the TDMS file. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Open | 10437 | Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx returns an error. |
| DAQmx_Val_OpenOrCreate | 15846 | Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx creates a new TDMS file. |
| DAQmx_Val_CreateOrReplace | 15847 | Create a new TDMS file, or replace an existing TDMS file. |
| DAQmx_Val_Create | 15848 | Create a new TDMS file. If the file already exists, NI-DAQmx returns an error. |

You can get/set/reset this property using:

- [DAQmxGetLoggingTDMSOperation](group__ni-daqmx__c__functions__property__manipulation__getter_1ga9ac58bf7c4dacf6589eb003f9a6d0860.html)
- [DAQmxSetLoggingTDMSOperation](group__ni-daqmx__c__functions__property__manipulation__setter_1ga701ec81365cfc1778ac08e248b38a8c9.html)
- [DAQmxResetLoggingTDMSOperation](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga0c253c6608990110743217d79e89c97d.html)

Parent topic:

TDMS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__logging__tdms_1gad0a7e104c9052bec51d42c363aeca229.html language=enus -->
## TOPIC 02154: DAQmx_Logging_FileWriteSize

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__logging__tdms_1gad0a7e104c9052bec51d42c363aeca229.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__logging__tdms_1gad0a7e104c9052bec51d42c363aeca229.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Logging_FileWriteSizeRemarksData TypeDescriptionRestrictionsuInt32Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes.You can get/set/reset this property using:DAQmxGetLoggingFileWriteSizeDAQmxSetLog

### DAQmx_Logging_FileWriteSize

#### Syntax

DAQmx_Logging_FileWriteSize

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes. |  |

You can get/set/reset this property using:

- [DAQmxGetLoggingFileWriteSize](group__ni-daqmx__c__functions__property__manipulation__getter_1gade46b04756b40ffacd592c1f4a4136be.html)
- [DAQmxSetLoggingFileWriteSize](group__ni-daqmx__c__functions__property__manipulation__setter_1ga1c9cf73a965b9804be9f17aa022615c6.html)
- [DAQmxResetLoggingFileWriteSize](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga33b58083e3e20ce5d1fa9242edd01d1d.html)

Parent topic:

TDMS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__logging__tdms_1gad719d7184032f56f3763823fecda24af.html language=enus -->
## TOPIC 02155: DAQmx_Logging_Pause

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__logging__tdms_1gad719d7184032f56f3763823fecda24af.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__logging__tdms_1gad719d7184032f56f3763823fecda24af.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Logging_PauseRemarksData TypeDescriptionRestrictionsbool32Specifies whether logging is paused while a task is executing. If Mode is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If Mode is set to Log Only m

### DAQmx_Logging_Pause

#### Syntax

DAQmx_Logging_Pause

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether logging is paused while a task is executing. If Mode is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If Mode is set to Log Only mode, this value is taken into consideration the next time that data is written to disk. A new TDMS group is written when logging is resumed from a paused state. |  |

You can get/set/reset this property using:

- [DAQmxGetLoggingPause](group__ni-daqmx__c__functions__property__manipulation__getter_1ga815d96f968fb905a25fb046b76d55f45.html)
- [DAQmxSetLoggingPause](group__ni-daqmx__c__functions__property__manipulation__setter_1gabcc5dcb289ecccf28a57caed0f883b74.html)
- [DAQmxResetLoggingPause](group__ni-daqmx__c__functions__property__manipulation__resetter_1gafc01f88236ce0ed1825261a32d8f6ae0.html)

Parent topic:

TDMS

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status.html language=enus -->
## TOPIC 02156: Status

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAccessoryAdvancedAux Power ErrorCommon Mode Range ErrorExcitation FaultInput Limits FaultOpen ChannelsOpen Current LoopOpen ThermocoupleOvercurrentOverloadOvertemperaturePhase-Locked LoopPower Supply FaultRemote Sense ErrorReverse Voltage ErrorSynchronizationGroup membersNameDescriptionDAQmx_R

### Status

#### Groups

- Accessory
- Advanced
- Aux Power Error
- Common Mode Range Error
- Excitation Fault
- Input Limits Fault
- Open Channels
- Open Current Loop
- Open Thermocouple
- Overcurrent
- Overload
- Overtemperature
- Phase-Locked Loop
- Power Supply Fault
- Remote Sense Error
- Reverse Voltage Error
- Synchronization

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_AvailSampPerChan |  |
| DAQmx_Read_CurrReadPos |  |
| DAQmx_Read_TotalSampPerChanAcquired |  |

#### Attachments

None

Parent topic:

Read

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status_1ga24c20c24a819d06daa59f23adeea5394.html language=enus -->
## TOPIC 02157: DAQmx_Read_CurrReadPos

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status_1ga24c20c24a819d06daa59f23adeea5394.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status_1ga24c20c24a819d06daa59f23adeea5394.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_CurrReadPosRemarksData TypeDescriptionRestrictionsuInt64Indicates in samples per channel the current position in the buffer.Not SettableYou can get this property using:DAQmxGetReadCurrReadPos

### DAQmx_Read_CurrReadPos

#### Syntax

DAQmx_Read_CurrReadPos

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt64 | Indicates in samples per channel the current position in the buffer. | Not Settable |

You can get this property using:

- [DAQmxGetReadCurrReadPos](group__ni-daqmx__c__functions__property__manipulation__getter_1ga270fa12e91b0df94ec767b75f7142e2e.html)

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status_1ga46d639a1bf85e3bac9d6ca6059da4cd3.html language=enus -->
## TOPIC 02158: DAQmx_Read_AvailSampPerChan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status_1ga46d639a1bf85e3bac9d6ca6059da4cd3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status_1ga46d639a1bf85e3bac9d6ca6059da4cd3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_AvailSampPerChanRemarksData TypeDescriptionRestrictionsuInt32Indicates the number of samples available to read per channel. This value is the same for all channels in the task.Not SettableYou can get this property using:DAQmxGetReadAvailSampPerChan

### DAQmx_Read_AvailSampPerChan

#### Syntax

DAQmx_Read_AvailSampPerChan

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the number of samples available to read per channel. This value is the same for all channels in the task. | Not Settable |

You can get this property using:

- [DAQmxGetReadAvailSampPerChan](group__ni-daqmx__c__functions__property__manipulation__getter_1ga21ea5e1d4a892ee1104bb7e0d11623e9.html)

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__accessory.html language=enus -->
## TOPIC 02159: Accessory

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__accessory.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__accessory.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_AccessoryInsertionOrRemovalDetectedDAQmx_Read_DevsWithInsertedOrRemovedAccessoriesAttachmentsNone

### Accessory

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_AccessoryInsertionOrRemovalDetected |  |
| DAQmx_Read_DevsWithInsertedOrRemovedAccessories |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__accessory_1ga782df08766fc2d46888b78d582b0d175.html language=enus -->
## TOPIC 02160: DAQmx_Read_DevsWithInsertedOrRemovedAccessories

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__accessory_1ga782df08766fc2d46888b78d582b0d175.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__accessory_1ga782df08766fc2d46888b78d582b0d175.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_DevsWithInsertedOrRemovedAccessoriesRemarksData TypeDescriptionRestrictionschar*Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read Accessory Insertion or Removal Detected before you read this property. Othe

### DAQmx_Read_DevsWithInsertedOrRemovedAccessories

#### Syntax

DAQmx_Read_DevsWithInsertedOrRemovedAccessories

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read Accessory Insertion or Removal Detected before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadDevsWithInsertedOrRemovedAccessories](group__ni-daqmx__c__functions__property__manipulation__getter_1ga190a7033067f94ca6d7f32024f0e3511.html)

Parent topic:

Accessory

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__aux__power__error.html language=enus -->
## TOPIC 02161: Aux Power Error

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__aux__power__error.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__aux__power__error.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_AuxPowerErrorChansDAQmx_AuxPowerErrorChansExistAttachmentsNone

### Aux Power Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_AuxPowerErrorChans |  |
| DAQmx_AuxPowerErrorChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__aux__power__error_1ga4642d3d1a06c2d5882ac5748b39ebdfe.html language=enus -->
## TOPIC 02162: DAQmx_AuxPowerErrorChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__aux__power__error_1ga4642d3d1a06c2d5882ac5748b39ebdfe.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__aux__power__error_1ga4642d3d1a06c2d5882ac5748b39ebdfe.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AuxPowerErrorChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device(s) detected an auxiliary power supply error condition for any channel in the task. Reading this property clears the error condition status for all channels in the task. You must read this property

### DAQmx_AuxPowerErrorChansExist

#### Syntax

DAQmx_AuxPowerErrorChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device(s) detected an auxiliary power supply error condition for any channel in the task. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Aux Power Error Channels property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetAuxPowerErrorChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1gab3fa5e69ebeb34ff8c582e107f24579a.html)

Parent topic:

Aux Power Error

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__aux__power__error_1ga7428a4ac71ea42c6ca5cf804eae2f737.html language=enus -->
## TOPIC 02163: DAQmx_AuxPowerErrorChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__aux__power__error_1ga7428a4ac71ea42c6ca5cf804eae2f737.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__aux__power__error_1ga7428a4ac71ea42c6ca5cf804eae2f737.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_AuxPowerErrorChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of any virtual channels in the task for which an auxiliary power supply error condition has been detected. You must read the Aux Power Error Channels Exist property before you read this property. Othe

### DAQmx_AuxPowerErrorChans

#### Syntax

DAQmx_AuxPowerErrorChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of any virtual channels in the task for which an auxiliary power supply error condition has been detected. You must read the Aux Power Error Channels Exist property before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetAuxPowerErrorChans](group__ni-daqmx__c__functions__property__manipulation__getter_1gad9e942b914febe950cab5b6fdc2213b0.html)

Parent topic:

Aux Power Error

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__common__mode__range__error_1gaeef9af89da0f1fcd3de08afe1056af14.html language=enus -->
## TOPIC 02164: DAQmx_Read_CommonModeRangeErrorChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__common__mode__range__error_1gaeef9af89da0f1fcd3de08afe1056af14.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__common__mode__range__error_1gaeef9af89da0f1fcd3de08afe1056af14.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_CommonModeRangeErrorChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read Common Mode Range Error Channels Exist before you read this property. Othe

### DAQmx_Read_CommonModeRangeErrorChans

#### Syntax

DAQmx_Read_CommonModeRangeErrorChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read Common Mode Range Error Channels Exist before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadCommonModeRangeErrorChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga44287b2edd291c0fc9200e603e6d074b.html)

Parent topic:

Common Mode Range Error

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__excitation__fault.html language=enus -->
## TOPIC 02165: Excitation Fault

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__excitation__fault.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__excitation__fault.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_ExcitFaultChansDAQmx_Read_ExcitFaultChansExistAttachmentsNone

### Excitation Fault

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_ExcitFaultChans |  |
| DAQmx_Read_ExcitFaultChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__excitation__fault_1ga5acf31981d156d5658a0a8735fdca820.html language=enus -->
## TOPIC 02166: DAQmx_Read_ExcitFaultChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__excitation__fault_1ga5acf31981d156d5658a0a8735fdca820.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__excitation__fault_1ga5acf31981d156d5658a0a8735fdca820.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_ExcitFaultChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of any virtual channels in the task for which the device(s) detected an excitation fault condition. You must read Excitation Fault Channels Exist before you read this property. Otherwise, you will r

### DAQmx_Read_ExcitFaultChans

#### Syntax

DAQmx_Read_ExcitFaultChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of any virtual channels in the task for which the device(s) detected an excitation fault condition. You must read Excitation Fault Channels Exist before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadExcitFaultChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga43c134a528439c90c096832c43da4fa6.html)

Parent topic:

Excitation Fault

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__input__limits__fault.html language=enus -->
## TOPIC 02167: Input Limits Fault

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__input__limits__fault.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__input__limits__fault.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_InputLimitsFaultChansDAQmx_Read_InputLimitsFaultChansExistAttachmentsNone

### Input Limits Fault

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_InputLimitsFaultChans |  |
| DAQmx_Read_InputLimitsFaultChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__input__limits__fault_1ga80ef1c08a4ea602f62ddca4107852258.html language=enus -->
## TOPIC 02168: DAQmx_Read_InputLimitsFaultChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__input__limits__fault_1ga80ef1c08a4ea602f62ddca4107852258.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__input__limits__fault_1ga80ef1c08a4ea602f62ddca4107852258.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_InputLimitsFaultChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all

### DAQmx_Read_InputLimitsFaultChansExist

#### Syntax

DAQmx_Read_InputLimitsFaultChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read Input Limits Fault Channels. Otherwise, you will receive an error. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA. | Not Settable |

You can get this property using:

- [DAQmxGetReadInputLimitsFaultChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1gaad1660787887633dcea08d279b08857f.html)

Parent topic:

Input Limits Fault

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__input__limits__fault_1ga89dbbda2aa1dcc93881f9a572cb98342.html language=enus -->
## TOPIC 02169: DAQmx_Read_InputLimitsFaultChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__input__limits__fault_1ga89dbbda2aa1dcc93881f9a572cb98342.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__input__limits__fault_1ga89dbbda2aa1dcc93881f9a572cb98342.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_InputLimitsFaultChansRemarksData TypeDescriptionRestrictionschar*Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read Input Limits Fault Channels Exist before you read this property. Otherw

### DAQmx_Read_InputLimitsFaultChans

#### Syntax

DAQmx_Read_InputLimitsFaultChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read Input Limits Fault Channels Exist before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadInputLimitsFaultChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga5a79a5b7aa703dd46f7fe5f1b18b92a4.html)

Parent topic:

Input Limits Fault

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__open__channels.html language=enus -->
## TOPIC 02170: Open Channels

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__open__channels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__open__channels.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_OpenChansDAQmx_Read_OpenChansDetailsDAQmx_Read_OpenChansExistAttachmentsNone

### Open Channels

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_OpenChans |  |
| DAQmx_Read_OpenChansDetails |  |
| DAQmx_Read_OpenChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__open__channels_1ga0acc815e7363bae2e53e547af1ed7f0a.html language=enus -->
## TOPIC 02171: DAQmx_Read_OpenChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__open__channels_1ga0acc815e7363bae2e53e547af1ed7f0a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__open__channels_1ga0acc815e7363bae2e53e547af1ed7f0a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OpenChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device or devices detected an open channel condition in any virtual channel in the task. Reading this property clears the open channel status for all channels in this task. You must read this property before

### DAQmx_Read_OpenChansExist

#### Syntax

DAQmx_Read_OpenChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device or devices detected an open channel condition in any virtual channel in the task. Reading this property clears the open channel status for all channels in this task. You must read this property before you read Open Channels. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOpenChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1gac70a51e4aa48220391f3da896bc9a0bd.html)

Parent topic:

Open Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__open__channels_1ga685378765dc6af786dad5cdd7cea407f.html language=enus -->
## TOPIC 02172: DAQmx_Read_OpenChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__open__channels_1ga685378765dc6af786dad5cdd7cea407f.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__open__channels_1ga685378765dc6af786dad5cdd7cea407f.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OpenChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of any open virtual channels. You must read Open Channels Exist before you read this property. Otherwise you will receive an error.Not SettableYou can get this property using:DAQmxGetReadOpenChans

### DAQmx_Read_OpenChans

#### Syntax

DAQmx_Read_OpenChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of any open virtual channels. You must read Open Channels Exist before you read this property. Otherwise you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOpenChans](group__ni-daqmx__c__functions__property__manipulation__getter_1gac2c5caf7998ea30f6912a1f2ec208f4e.html)

Parent topic:

Open Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__open__channels_1gaa4cfac972682f1059e2ddc4be83363e1.html language=enus -->
## TOPIC 02173: DAQmx_Read_OpenChansDetails

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__open__channels_1gaa4cfac972682f1059e2ddc4be83363e1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__open__channels_1gaa4cfac972682f1059e2ddc4be83363e1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OpenChansDetailsRemarksData TypeDescriptionRestrictionschar*Indicates a list of details of any open virtual channels. You must read Open Channels Exist before you read this property. Otherwise you will receive an error.Not SettableYou can get this property using:DAQmxGetReadOpenChan

### DAQmx_Read_OpenChansDetails

#### Syntax

DAQmx_Read_OpenChansDetails

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of details of any open virtual channels. You must read Open Channels Exist before you read this property. Otherwise you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOpenChansDetails](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1195619a210c292641c9254f2810d37d.html)

Parent topic:

Open Channels

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__open__current__loop.html language=enus -->
## TOPIC 02174: Open Current Loop

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__open__current__loop.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__open__current__loop.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_OpenCurrentLoopChansDAQmx_Read_OpenCurrentLoopChansExistAttachmentsNone

### Open Current Loop

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_OpenCurrentLoopChans |  |
| DAQmx_Read_OpenCurrentLoopChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__open__current__loop_1ga337d04268ddaa452c30814ab7c307dab.html language=enus -->
## TOPIC 02175: DAQmx_Read_OpenCurrentLoopChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__open__current__loop_1ga337d04268ddaa452c30814ab7c307dab.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__open__current__loop_1ga337d04268ddaa452c30814ab7c307dab.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OpenCurrentLoopChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read Open Current Loop Channels Exist before you read this property. Otherwise, you will rece

### DAQmx_Read_OpenCurrentLoopChans

#### Syntax

DAQmx_Read_OpenCurrentLoopChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read Open Current Loop Channels Exist before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOpenCurrentLoopChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1d630947bcd0f2afe2cedd3fc28e3e97.html)

Parent topic:

Open Current Loop

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__open__thermocouple.html language=enus -->
## TOPIC 02176: Open Thermocouple

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__open__thermocouple.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__open__thermocouple.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_OpenThrmcplChansDAQmx_Read_OpenThrmcplChansExistAttachmentsNone

### Open Thermocouple

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_OpenThrmcplChans |  |
| DAQmx_Read_OpenThrmcplChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__open__thermocouple_1gad96b6b19e4ce63dc413ff4c92996457b.html language=enus -->
## TOPIC 02177: DAQmx_Read_OpenThrmcplChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__open__thermocouple_1gad96b6b19e4ce63dc413ff4c92996457b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__open__thermocouple_1gad96b6b19e4ce63dc413ff4c92996457b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OpenThrmcplChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this propert

### DAQmx_Read_OpenThrmcplChansExist

#### Syntax

DAQmx_Read_OpenThrmcplChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read Open Thermocouple Channels. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOpenThrmcplChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1gab1018ae70ccecbca0c2bdceda1e523b8.html)

Parent topic:

Open Thermocouple

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__overcurrent_1ga752b3cfb604e0eb94a7e824aca76d5ee.html language=enus -->
## TOPIC 02178: DAQmx_Read_OvercurrentChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__overcurrent_1ga752b3cfb604e0eb94a7e824aca76d5ee.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__overcurrent_1ga752b3cfb604e0eb94a7e824aca76d5ee.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OvercurrentChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of any virtual channels in the task for which the device(s) detected an overcurrent condition. You must read Overcurrent Channels Exist before you read this property. Otherwise, you will receive an

### DAQmx_Read_OvercurrentChans

#### Syntax

DAQmx_Read_OvercurrentChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of any virtual channels in the task for which the device(s) detected an overcurrent condition. You must read Overcurrent Channels Exist before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent channels to recover. | Not Settable |

You can get this property using:

- [DAQmxGetReadOvercurrentChans](group__ni-daqmx__c__functions__property__manipulation__getter_1gad5c6d0a846178c9897ed4a56c614f8fe.html)

Parent topic:

Overcurrent

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__overcurrent_1gadc7774322a2e20a562e50f540fd72c7a.html language=enus -->
## TOPIC 02179: DAQmx_Read_OvercurrentChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__overcurrent_1gadc7774322a2e20a562e50f540fd72c7a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__overcurrent_1gadc7774322a2e20a562e50f540fd72c7a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OvercurrentChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device(s) detected an overcurrent condition for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before yo

### DAQmx_Read_OvercurrentChansExist

#### Syntax

DAQmx_Read_OvercurrentChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device(s) detected an overcurrent condition for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read Overcurrent Channels. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOvercurrentChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1ffe57c9405a578872f83d1aea9e4244.html)

Parent topic:

Overcurrent

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__overload_1ga269aeb11a25e696f29050f9eb9d49588.html language=enus -->
## TOPIC 02180: DAQmx_Read_OverloadedChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__overload_1ga269aeb11a25e696f29050f9eb9d49588.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__overload_1ga269aeb11a25e696f29050f9eb9d49588.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OverloadedChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of any overloaded virtual channels in the task. You must read Overloaded Channels Exist before you read this property. Otherwise, you will receive an error.Not SettableYou can get this property usin

### DAQmx_Read_OverloadedChans

#### Syntax

DAQmx_Read_OverloadedChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of any overloaded virtual channels in the task. You must read Overloaded Channels Exist before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOverloadedChans](group__ni-daqmx__c__functions__property__manipulation__getter_1gac81ae8c2927950ea12f6da2f6d2bddf5.html)

Parent topic:

Overload

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__overload_1ga619b4a020aa7c726fff1712f3679670d.html language=enus -->
## TOPIC 02181: DAQmx_Read_OverloadedChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__overload_1ga619b4a020aa7c726fff1712f3679670d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__overload_1ga619b4a020aa7c726fff1712f3679670d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OverloadedChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read Overloaded

### DAQmx_Read_OverloadedChansExist

#### Syntax

DAQmx_Read_OverloadedChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read Overloaded Channels. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOverloadedChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1ga8667a3477f637acb16d92e08d5d37e02.html)

Parent topic:

Overload

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__overtemperature.html language=enus -->
## TOPIC 02182: Overtemperature

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__overtemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__overtemperature.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_OvertemperatureChansDAQmx_Read_OvertemperatureChansExistAttachmentsNone

### Overtemperature

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_OvertemperatureChans |  |
| DAQmx_Read_OvertemperatureChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__overtemperature_1ga49645a33b2b58088ea1cec04127a5158.html language=enus -->
## TOPIC 02183: DAQmx_Read_OvertemperatureChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__overtemperature_1ga49645a33b2b58088ea1cec04127a5158.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__overtemperature_1ga49645a33b2b58088ea1cec04127a5158.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_OvertemperatureChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this propert

### DAQmx_Read_OvertemperatureChansExist

#### Syntax

DAQmx_Read_OvertemperatureChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read Overtemperature Channels. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadOvertemperatureChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1gad4648e7cd94b888b2884bd9a93c70cff.html)

Parent topic:

Overtemperature

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__phase__locked__loop.html language=enus -->
## TOPIC 02184: Phase-Locked Loop

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__phase__locked__loop.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__phase__locked__loop.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_PLL_UnlockedChansDAQmx_Read_PLL_UnlockedChansExistAttachmentsNone

### Phase-Locked Loop

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_PLL_UnlockedChans |  |
| DAQmx_Read_PLL_UnlockedChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__phase__locked__loop_1gae46079f321085af6654ad42b3a9ca9c2.html language=enus -->
## TOPIC 02185: DAQmx_Read_PLL_UnlockedChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__phase__locked__loop_1gae46079f321085af6654ad42b3a9ca9c2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__phase__locked__loop_1gae46079f321085af6654ad42b3a9ca9c2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_PLL_UnlockedChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition.Not SettableYou can get this

### DAQmx_Read_PLL_UnlockedChansExist

#### Syntax

DAQmx_Read_PLL_UnlockedChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition. | Not Settable |

You can get this property using:

- [DAQmxGetReadPLLUnlockedChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1ga5dee68cd3051460ce5f76e300a47ce48.html)

Parent topic:

Phase-Locked Loop

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__power__supply__fault.html language=enus -->
## TOPIC 02186: Power Supply Fault

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__power__supply__fault.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__power__supply__fault.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_PowerSupplyFaultChansDAQmx_Read_PowerSupplyFaultChansExistAttachmentsNone

### Power Supply Fault

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_PowerSupplyFaultChans |  |
| DAQmx_Read_PowerSupplyFaultChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__power__supply__fault_1gaa32d029cd7b5f00a07f77e7ac5156690.html language=enus -->
## TOPIC 02187: DAQmx_Read_PowerSupplyFaultChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__power__supply__fault_1gaa32d029cd7b5f00a07f77e7ac5156690.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__power__supply__fault_1gaa32d029cd7b5f00a07f77e7ac5156690.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_PowerSupplyFaultChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must re

### DAQmx_Read_PowerSupplyFaultChansExist

#### Syntax

DAQmx_Read_PowerSupplyFaultChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read Power Supply Fault Channels. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReadPowerSupplyFaultChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1ga811f4ff9e8744a1ccf787a297ab37b6b.html)

Parent topic:

Power Supply Fault

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__remote__sense__error.html language=enus -->
## TOPIC 02188: Remote Sense Error

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__remote__sense__error.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__remote__sense__error.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_RemoteSenseErrorChansDAQmx_RemoteSenseErrorChansExistAttachmentsNone

### Remote Sense Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_RemoteSenseErrorChans |  |
| DAQmx_RemoteSenseErrorChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__remote__sense__error_1ga45aa83cbbaa7207d757487bc47d608e4.html language=enus -->
## TOPIC 02189: DAQmx_RemoteSenseErrorChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__remote__sense__error_1ga45aa83cbbaa7207d757487bc47d608e4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__remote__sense__error_1ga45aa83cbbaa7207d757487bc47d608e4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_RemoteSenseErrorChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device(s) detected an error condition of the remote sense connection for any channel in the task. You must disable the output and resolve the hardware connection issue to clear the error condition. Yo

### DAQmx_RemoteSenseErrorChansExist

#### Syntax

DAQmx_RemoteSenseErrorChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device(s) detected an error condition of the remote sense connection for any channel in the task. You must disable the output and resolve the hardware connection issue to clear the error condition. You must read this property before you read the Remote Sense Error Channels property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetRemoteSenseErrorChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1d6ed2267d5c127dadc3f408343b05d0.html)

Parent topic:

Remote Sense Error

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__remote__sense__error_1ga472caa52d9aad67150e136df07ef8441.html language=enus -->
## TOPIC 02190: DAQmx_RemoteSenseErrorChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__remote__sense__error_1ga472caa52d9aad67150e136df07ef8441.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__remote__sense__error_1ga472caa52d9aad67150e136df07ef8441.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_RemoteSenseErrorChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of any virtual channels in the task for which a remote sense connection error condition has been detected. You must read Remote Sense Error Channels Exist before you read this property. Otherwise,

### DAQmx_RemoteSenseErrorChans

#### Syntax

DAQmx_RemoteSenseErrorChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of any virtual channels in the task for which a remote sense connection error condition has been detected. You must read Remote Sense Error Channels Exist before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetRemoteSenseErrorChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga28e942f9a8bfa86b3f550d986218b385.html)

Parent topic:

Remote Sense Error

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__reverse__voltage__error.html language=enus -->
## TOPIC 02191: Reverse Voltage Error

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__reverse__voltage__error.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__reverse__voltage__error.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_ReverseVoltageErrorChansDAQmx_ReverseVoltageErrorChansExistAttachmentsNone

### Reverse Voltage Error

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_ReverseVoltageErrorChans |  |
| DAQmx_ReverseVoltageErrorChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__reverse__voltage__error_1ga010e2f8f7f045da580e2219670c59dbd.html language=enus -->
## TOPIC 02192: DAQmx_ReverseVoltageErrorChansExist

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__reverse__voltage__error_1ga010e2f8f7f045da580e2219670c59dbd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__reverse__voltage__error_1ga010e2f8f7f045da580e2219670c59dbd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_ReverseVoltageErrorChansExistRemarksData TypeDescriptionRestrictionsbool32Indicates if the device(s) detected reverse voltage error for any of the channels in the task. Reverse voltage error occurs if the local voltage is equal to the negative saturated voltage. Reading this property cle

### DAQmx_ReverseVoltageErrorChansExist

#### Syntax

DAQmx_ReverseVoltageErrorChansExist

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates if the device(s) detected reverse voltage error for any of the channels in the task. Reverse voltage error occurs if the local voltage is equal to the negative saturated voltage. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Reverse Voltage Error Channels property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReverseVoltageErrorChansExist](group__ni-daqmx__c__functions__property__manipulation__getter_1ga7c4ed9b9a744efe08657ebd850dfad5d.html)

Parent topic:

Reverse Voltage Error

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__reverse__voltage__error_1ga89bd360d6ba92fe00085c8ec87e600ed.html language=enus -->
## TOPIC 02193: DAQmx_ReverseVoltageErrorChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__reverse__voltage__error_1ga89bd360d6ba92fe00085c8ec87e600ed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__reverse__voltage__error_1ga89bd360d6ba92fe00085c8ec87e600ed.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_ReverseVoltageErrorChansRemarksData TypeDescriptionRestrictionschar*Indicates a list of names of all virtual channels in the task for which reverse voltage error condition has been detected. You must read the Reverse Voltage Error Channels Exist property before you read this property. Ot

### DAQmx_ReverseVoltageErrorChans

#### Syntax

DAQmx_ReverseVoltageErrorChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates a list of names of all virtual channels in the task for which reverse voltage error condition has been detected. You must read the Reverse Voltage Error Channels Exist property before you read this property. Otherwise, you will receive an error. | Not Settable |

You can get this property using:

- [DAQmxGetReverseVoltageErrorChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga20029ae4391be829c610aba4b0a58d0e.html)

Parent topic:

Reverse Voltage Error

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__synchronization.html language=enus -->
## TOPIC 02194: Synchronization

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__synchronization.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Read_Sync_UnlockedChansDAQmx_Read_Sync_UnlockedChansExistAttachmentsNone

### Synchronization

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Read_Sync_UnlockedChans |  |
| DAQmx_Read_Sync_UnlockedChansExist |  |

#### Attachments

None

Parent topic:

Status

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__read__status__synchronization_1ga8aab5e8450899cc28efe247989271e32.html language=enus -->
## TOPIC 02195: DAQmx_Read_Sync_UnlockedChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__read__status__synchronization_1ga8aab5e8450899cc28efe247989271e32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__read__status__synchronization_1ga8aab5e8450899cc28efe247989271e32.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Read_Sync_UnlockedChansRemarksData TypeDescriptionRestrictionschar*Indicates the channels from devices in an unlocked target.Not SettableYou can get this property using:DAQmxGetReadSyncUnlockedChans

### DAQmx_Read_Sync_UnlockedChans

#### Syntax

DAQmx_Read_Sync_UnlockedChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the channels from devices in an unlocked target. | Not Settable |

You can get this property using:

- [DAQmxGetReadSyncUnlockedChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga373c2b04080922de2148478a5cd33730.html)

Parent topic:

Synchronization

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__real-time_1ga0a75fc1c744aa7522f6eeb28b21b18b3.html language=enus -->
## TOPIC 02196: DAQmx_RealTime_NumOfWarmupIters

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__real-time_1ga0a75fc1c744aa7522f6eeb28b21b18b3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__real-time_1ga0a75fc1c744aa7522f6eeb28b21b18b3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_RealTime_NumOfWarmupItersRemarksData TypeDescriptionRestrictionsuInt32Specifies the number of loop iterations that must occur before DAQmxWaitForNextSampleClock() and an NI-DAQmx Read function return any late warnings or errors. The system needs a number of iterations to stabilize. Durin

### DAQmx_RealTime_NumOfWarmupIters

#### Syntax

DAQmx_RealTime_NumOfWarmupIters

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Specifies the number of loop iterations that must occur before DAQmxWaitForNextSampleClock() and an NI-DAQmx Read function return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be late. The default number of warmup iterations is 100. Specify a larger number if needed to stabilize the system. |  |

You can get/set/reset this property using:

- [DAQmxGetRealTimeNumOfWarmupIters](group__ni-daqmx__c__functions__property__manipulation__getter_1ga28c6b231337fda57e8dff065b60db4a9.html)
- [DAQmxSetRealTimeNumOfWarmupIters](group__ni-daqmx__c__functions__property__manipulation__setter_1ga12f12b7951af575971c30362cc88de7c.html)
- [DAQmxResetRealTimeNumOfWarmupIters](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga92f32c4c22f6e890bb9744b3f88bb199.html)

Parent topic:

Real-Time

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__real-time_1ga1d1ccd3c18199ac54466f64deed5b9fa.html language=enus -->
## TOPIC 02197: DAQmx_RealTime_WriteRecoveryMode

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__real-time_1ga1d1ccd3c18199ac54466f64deed5b9fa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__real-time_1ga1d1ccd3c18199ac54466f64deed5b9fa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_RealTime_WriteRecoveryModeRemarksData TypeDescriptionRestrictionsint32Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes.Valid valuesDAQmx_Val_WaitForInterrupt12523Attempt to recover when the system receives an interrupt service r

### DAQmx_RealTime_WriteRecoveryMode

#### Syntax

DAQmx_RealTime_WriteRecoveryMode

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_WaitForInterrupt | 12523 | Attempt to recover when the system receives an interrupt service request. This mode is the most CPU efficient and best suited for recovery at lower pulse train frequencies. |
| DAQmx_Val_Poll | 12524 | Repeatedly attempt to recover as fast as possible. This mode has the highest probability of recovery success at the expense of CPU efficiency. |

You can get/set/reset this property using:

- [DAQmxGetRealTimeWriteRecoveryMode](group__ni-daqmx__c__functions__property__manipulation__getter_1ga1f513dde4250f465c4f85f0539b6333d.html)
- [DAQmxSetRealTimeWriteRecoveryMode](group__ni-daqmx__c__functions__property__manipulation__setter_1gafbeb99b299d1d91cbdb79c5df63a9887.html)
- [DAQmxResetRealTimeWriteRecoveryMode](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga8e55d2dc33b88a734a76c754e057e472.html)

Parent topic:

Real-Time

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__real-time_1ga498a46ee447d0f6116cb34a692d51aa9.html language=enus -->
## TOPIC 02198: DAQmx_RealTime_ReportMissedSamp

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__real-time_1ga498a46ee447d0f6116cb34a692d51aa9.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__real-time_1ga498a46ee447d0f6116cb34a692d51aa9.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_RealTime_ReportMissedSampRemarksData TypeDescriptionRestrictionsbool32Specifies whether an NI-DAQmx Read function returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect DAQmxWaitForNextSampleClock(). Set this property to TRUE for appl

### DAQmx_RealTime_ReportMissedSamp

#### Syntax

DAQmx_RealTime_ReportMissedSamp

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Specifies whether an NI-DAQmx Read function returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect DAQmxWaitForNextSampleClock(). Set this property to TRUE for applications that need to detect lateness without using DAQmxWaitForNextSampleClock(). |  |

You can get/set/reset this property using:

- [DAQmxGetRealTimeReportMissedSamp](group__ni-daqmx__c__functions__property__manipulation__getter_1ga39d9ee8141483f0cf03507d2900edc81.html)
- [DAQmxSetRealTimeReportMissedSamp](group__ni-daqmx__c__functions__property__manipulation__setter_1ga089b450d42fe3d9cf222146b041288cb.html)
- [DAQmxResetRealTimeReportMissedSamp](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga4b662c62083609410c51679a4060ac82.html)

Parent topic:

Real-Time

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale_1ga6aeae201708554e970c2943b87f83e75.html language=enus -->
## TOPIC 02199: DAQmx_Scale_Descr

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale_1ga6aeae201708554e970c2943b87f83e75.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale_1ga6aeae201708554e970c2943b87f83e75.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_DescrRemarksData TypeDescriptionRestrictionschar*Specifies a description for the scale.You can get/set this property using:DAQmxGetScaleDescrDAQmxSetScaleDescr

### DAQmx_Scale_Descr

#### Syntax

DAQmx_Scale_Descr

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Specifies a description for the scale. |  |

You can get/set this property using:

- [DAQmxGetScaleDescr](group__ni-daqmx__c__functions__property__manipulation__getter_1ga606b75fc273704de311a3723ccc8c2ea.html)
- [DAQmxSetScaleDescr](group__ni-daqmx__c__functions__property__manipulation__setter_1gaef08bea76e938ea50984682e5129f9e4.html)

Parent topic:

Scale

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__linear_1gadb6b8b0df80e94074a39200d645eb1b7.html language=enus -->
## TOPIC 02200: DAQmx_Scale_Lin_YIntercept

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__linear_1gadb6b8b0df80e94074a39200d645eb1b7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__linear_1gadb6b8b0df80e94074a39200d645eb1b7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Lin_YInterceptRemarksData TypeDescriptionRestrictionsfloat64Specifies the y-intercept, b, in the equation y=mx+b.You can get/set this property using:DAQmxGetScaleLinYInterceptDAQmxSetScaleLinYIntercept

### DAQmx_Scale_Lin_YIntercept

#### Syntax

DAQmx_Scale_Lin_YIntercept

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the y-intercept, b, in the equation y=mx+b. |  |

You can get/set this property using:

- [DAQmxGetScaleLinYIntercept](group__ni-daqmx__c__functions__property__manipulation__getter_1ga238005c7ac81c1dc0dbf3d8409fa3a45.html)
- [DAQmxSetScaleLinYIntercept](group__ni-daqmx__c__functions__property__manipulation__setter_1gaf4530260e16aa13fb2ecc1820ccf04c0.html)

Parent topic:

Linear

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__map.html language=enus -->
## TOPIC 02201: Map

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__map.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__map.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Scale_Map_PreScaledMaxDAQmx_Scale_Map_PreScaledMinDAQmx_Scale_Map_ScaledMaxDAQmx_Scale_Map_ScaledMinAttachmentsNone

### Map

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Scale_Map_PreScaledMax |  |
| DAQmx_Scale_Map_PreScaledMin |  |
| DAQmx_Scale_Map_ScaledMax |  |
| DAQmx_Scale_Map_ScaledMin |  |

#### Attachments

None

Parent topic:

Scale

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__map_1ga24fcc687e8741f6d073798d7c05e14cf.html language=enus -->
## TOPIC 02202: DAQmx_Scale_Map_PreScaledMax

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__map_1ga24fcc687e8741f6d073798d7c05e14cf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__map_1ga24fcc687e8741f6d073798d7c05e14cf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Map_PreScaledMaxRemarksData TypeDescriptionRestrictionsfloat64Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to Scaled Maximum Value.You can get/set this property using:DAQmxGetScaleMapPreScaledMaxDAQmxSetScaleMapPreScaledMax

### DAQmx_Scale_Map_PreScaledMax

#### Syntax

DAQmx_Scale_Map_PreScaledMax

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to Scaled Maximum Value. |  |

You can get/set this property using:

- [DAQmxGetScaleMapPreScaledMax](group__ni-daqmx__c__functions__property__manipulation__getter_1gacd10cc6f6f654ec3b3e941564c3bf5bb.html)
- [DAQmxSetScaleMapPreScaledMax](group__ni-daqmx__c__functions__property__manipulation__setter_1gadd2319fbb457955d3a390dfacc2f9998.html)

Parent topic:

Map

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__map_1ga76abdbefa5911eba097b660e5dbc5ed3.html language=enus -->
## TOPIC 02203: DAQmx_Scale_Map_PreScaledMin

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__map_1ga76abdbefa5911eba097b660e5dbc5ed3.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__map_1ga76abdbefa5911eba097b660e5dbc5ed3.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Map_PreScaledMinRemarksData TypeDescriptionRestrictionsfloat64Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to Scaled Minimum Value.You can get/set this property using:DAQmxGetScaleMapPreScaledMinDAQmxSetScaleMapPreScaledMin

### DAQmx_Scale_Map_PreScaledMin

#### Syntax

DAQmx_Scale_Map_PreScaledMin

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to Scaled Minimum Value. |  |

You can get/set this property using:

- [DAQmxGetScaleMapPreScaledMin](group__ni-daqmx__c__functions__property__manipulation__getter_1ga0f1cfd80c6bd527480dcd9524ab78afa.html)
- [DAQmxSetScaleMapPreScaledMin](group__ni-daqmx__c__functions__property__manipulation__setter_1ga04e03facaacd61837ba99688d01ace3a.html)

Parent topic:

Map

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__map_1ga83e7cb95504a8853c7a960bf6ef66393.html language=enus -->
## TOPIC 02204: DAQmx_Scale_Map_ScaledMax

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__map_1ga83e7cb95504a8853c7a960bf6ef66393.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__map_1ga83e7cb95504a8853c7a960bf6ef66393.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Map_ScaledMaxRemarksData TypeDescriptionRestrictionsfloat64Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to Pre-Scaled Maximum Value. Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples t

### DAQmx_Scale_Map_ScaledMax

#### Syntax

DAQmx_Scale_Map_ScaledMax

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to Pre-Scaled Maximum Value. Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples that are larger than this value. |  |

You can get/set this property using:

- [DAQmxGetScaleMapScaledMax](group__ni-daqmx__c__functions__property__manipulation__getter_1ga67f5432aae76e075eca80424da50e0f0.html)
- [DAQmxSetScaleMapScaledMax](group__ni-daqmx__c__functions__property__manipulation__setter_1ga7d8107a21a03c0f50f47a7312029a96a.html)

Parent topic:

Map

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__map_1gaf3c90e5ea1a26d2cf74b487b39326371.html language=enus -->
## TOPIC 02205: DAQmx_Scale_Map_ScaledMin

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__map_1gaf3c90e5ea1a26d2cf74b487b39326371.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__map_1gaf3c90e5ea1a26d2cf74b487b39326371.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Map_ScaledMinRemarksData TypeDescriptionRestrictionsfloat64Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to Pre-Scaled Minimum Value. Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples

### DAQmx_Scale_Map_ScaledMin

#### Syntax

DAQmx_Scale_Map_ScaledMin

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to Pre-Scaled Minimum Value. Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples that are smaller than this value. |  |

You can get/set this property using:

- [DAQmxGetScaleMapScaledMin](group__ni-daqmx__c__functions__property__manipulation__getter_1gab70ef30239b11563542dac6e523f569d.html)
- [DAQmxSetScaleMapScaledMin](group__ni-daqmx__c__functions__property__manipulation__setter_1ga13f9fd99faa0920953e7c888ff5b3de2.html)

Parent topic:

Map

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__polynomial.html language=enus -->
## TOPIC 02206: Polynomial

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__polynomial.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__polynomial.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Scale_Poly_ForwardCoeffDAQmx_Scale_Poly_ReverseCoeffAttachmentsNone

### Polynomial

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Scale_Poly_ForwardCoeff |  |
| DAQmx_Scale_Poly_ReverseCoeff |  |

#### Attachments

None

Parent topic:

Scale

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__polynomial_1ga56e61c4d37ecaf29f4ef60d84e2748f7.html language=enus -->
## TOPIC 02207: DAQmx_Scale_Poly_ReverseCoeff

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__polynomial_1ga56e61c4d37ecaf29f4ef60d84e2748f7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__polynomial_1ga56e61c4d37ecaf29f4ef60d84e2748f7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Poly_ReverseCoeffRemarksData TypeDescriptionRestrictionsfloat64*Specifies an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, th

### DAQmx_Scale_Poly_ReverseCoeff

#### Syntax

DAQmx_Scale_Poly_ReverseCoeff

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64* | Specifies an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y^3. |  |

You can get/set this property using:

- [DAQmxGetScalePolyReverseCoeff](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2277b58ab44cd9bee1bf6a09031dffee.html)
- [DAQmxSetScalePolyReverseCoeff](group__ni-daqmx__c__functions__property__manipulation__setter_1gafcacca4407af3de32c5e282a43d78094.html)

Parent topic:

Polynomial

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__polynomial_1gaf469e4309fa8eb2eb067454666b3d9d1.html language=enus -->
## TOPIC 02208: DAQmx_Scale_Poly_ForwardCoeff

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__polynomial_1gaf469e4309fa8eb2eb067454666b3d9d1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__polynomial_1gaf469e4309fa8eb2eb067454666b3d9d1.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Poly_ForwardCoeffRemarksData TypeDescriptionRestrictionsfloat64*Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, th

### DAQmx_Scale_Poly_ForwardCoeff

#### Syntax

DAQmx_Scale_Poly_ForwardCoeff

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64* | Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. |  |

You can get/set this property using:

- [DAQmxGetScalePolyForwardCoeff](group__ni-daqmx__c__functions__property__manipulation__getter_1ga2e6a4af46432f09c5646241751fff7a1.html)
- [DAQmxSetScalePolyForwardCoeff](group__ni-daqmx__c__functions__property__manipulation__setter_1gab912995042111440f579436990192ac4.html)

Parent topic:

Polynomial

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__table.html language=enus -->
## TOPIC 02209: Table

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__table.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__table.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Scale_Table_PreScaledValsDAQmx_Scale_Table_ScaledValsAttachmentsNone

### Table

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Scale_Table_PreScaledVals |  |
| DAQmx_Scale_Table_ScaledVals |  |

#### Attachments

None

Parent topic:

Scale

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__table_1ga0c062a3617ed7952aa01cb4a4379bb28.html language=enus -->
## TOPIC 02210: DAQmx_Scale_Table_ScaledVals

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__table_1ga0c062a3617ed7952aa01cb4a4379bb28.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__table_1ga0c062a3617ed7952aa01cb4a4379bb28.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Table_ScaledValsRemarksData TypeDescriptionRestrictionsfloat64*Specifies an array of scaled values. These values map directly to the values in Pre-Scaled Values.You can get/set this property using:DAQmxGetScaleTableScaledValsDAQmxSetScaleTableScaledVals

### DAQmx_Scale_Table_ScaledVals

#### Syntax

DAQmx_Scale_Table_ScaledVals

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64* | Specifies an array of scaled values. These values map directly to the values in Pre-Scaled Values. |  |

You can get/set this property using:

- [DAQmxGetScaleTableScaledVals](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa40148ad5e1b6946202258658706c38e.html)
- [DAQmxSetScaleTableScaledVals](group__ni-daqmx__c__functions__property__manipulation__setter_1gaa9f2153b17f298c1265da6f19b6871d0.html)

Parent topic:

Table

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__scale__table_1ga7d0fc930eee18c73b54925e1f069aa53.html language=enus -->
## TOPIC 02211: DAQmx_Scale_Table_PreScaledVals

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__scale__table_1ga7d0fc930eee18c73b54925e1f069aa53.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__scale__table_1ga7d0fc930eee18c73b54925e1f069aa53.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Scale_Table_PreScaledValsRemarksData TypeDescriptionRestrictionsfloat64*Specifies an array of pre-scaled values. These values map directly to the values in Scaled Values.You can get/set this property using:DAQmxGetScaleTablePreScaledValsDAQmxSetScaleTablePreScaledVals

### DAQmx_Scale_Table_PreScaledVals

#### Syntax

DAQmx_Scale_Table_PreScaledVals

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64* | Specifies an array of pre-scaled values. These values map directly to the values in Scaled Values. |  |

You can get/set this property using:

- [DAQmxGetScaleTablePreScaledVals](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa0bf2745cf99deaeff42ef01870483eb.html)
- [DAQmxSetScaleTablePreScaledVals](group__ni-daqmx__c__functions__property__manipulation__setter_1ga59f7c6f969b92f6778826820a13adc1b.html)

Parent topic:

Table

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel.html language=enus -->
## TOPIC 02212: SwitchChannel

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDeprecatedGroup membersNoneAttachmentsNone

### SwitchChannel

#### Groups

- Deprecated

#### Group members

None

#### Attachments

None

Parent topic:

NI-DAQmx C Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated.html language=enus -->
## TOPIC 02213: Deprecated

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCapabilityGroup membersNameDescriptionDAQmx_SwitchChan_AnlgBusSharingEnableDAQmx_SwitchChan_UsageAttachmentsNone

### Deprecated

#### Groups

- Capability

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_SwitchChan_AnlgBusSharingEnable |  |
| DAQmx_SwitchChan_Usage |  |

#### Attachments

None

Parent topic:

SwitchChannel

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated_1ga5e18df3357db822040bb4f77f7a73d42.html language=enus -->
## TOPIC 02214: DAQmx_SwitchChan_Usage

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated_1ga5e18df3357db822040bb4f77f7a73d42.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated_1ga5e18df3357db822040bb4f77f7a73d42.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchChan_UsageRemarksData TypeDescriptionRestrictionsint32(Deprecated) Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example.Valid valuesDAQmx_Val_Source10439You can use the channel only as

### DAQmx_SwitchChan_Usage

#### Syntax

DAQmx_SwitchChan_Usage

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | (Deprecated) Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Source | 10439 | You can use the channel only as an input for a signal. |
| DAQmx_Val_Load | 10440 | You can use the channel only as the output for a signal passing through the switch. |
| DAQmx_Val_ReservedForRouting | 10441 | You can use the channel only to complete routes within a switch. |

You can get/set this property using:

- [DAQmxGetSwitchChanUsage](group__ni-daqmx__c__functions__property__manipulation__getter_1ga6cb4cd23519b3e4af576895500c6a1c0.html)
- [DAQmxSetSwitchChanUsage](group__ni-daqmx__c__functions__property__manipulation__setter_1ga64734c3e8e3137fcc1afbfd60bafb3de.html)

Parent topic:

Deprecated

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga02ff28c23e8a34cc09e10f1fcc523f72.html language=enus -->
## TOPIC 02215: DAQmx_SwitchChan_MaxDCCarryCurrent

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga02ff28c23e8a34cc09e10f1fcc523f72.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga02ff28c23e8a34cc09e10f1fcc523f72.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchChan_MaxDCCarryCurrentRemarksData TypeDescriptionRestrictionsfloat64(Deprecated) Indicates in amperes the maximum DC current that the device can carry.Not SettableYou can get this property using:DAQmxGetSwitchChanMaxDCCarryCurrent

### DAQmx_SwitchChan_MaxDCCarryCurrent

#### Syntax

DAQmx_SwitchChan_MaxDCCarryCurrent

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | (Deprecated) Indicates in amperes the maximum DC current that the device can carry. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchChanMaxDCCarryCurrent](group__ni-daqmx__c__functions__property__manipulation__getter_1ga3cea57cdca2502b7b72a30104998b29d.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga0dc7cea55e5b60f291b6f285bd411cc8.html language=enus -->
## TOPIC 02216: DAQmx_SwitchChan_MaxACSwitchPwr

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga0dc7cea55e5b60f291b6f285bd411cc8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga0dc7cea55e5b60f291b6f285bd411cc8.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchChan_MaxACSwitchPwrRemarksData TypeDescriptionRestrictionsfloat64(Deprecated) Indicates in watts the maximum AC power that the device can switch.Not SettableYou can get this property using:DAQmxGetSwitchChanMaxACSwitchPwr

### DAQmx_SwitchChan_MaxACSwitchPwr

#### Syntax

DAQmx_SwitchChan_MaxACSwitchPwr

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | (Deprecated) Indicates in watts the maximum AC power that the device can switch. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchChanMaxACSwitchPwr](group__ni-daqmx__c__functions__property__manipulation__getter_1ga23f82c8415c44156b33873f9e712a175.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga10c3dc8777c6b0b2539b8f12e753ddc0.html language=enus -->
## TOPIC 02217: DAQmx_SwitchChan_MaxDCCarryPwr

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga10c3dc8777c6b0b2539b8f12e753ddc0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga10c3dc8777c6b0b2539b8f12e753ddc0.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchChan_MaxDCCarryPwrRemarksData TypeDescriptionRestrictionsfloat64(Deprecated) Indicates in watts the maximum DC power that the device can carry.Not SettableYou can get this property using:DAQmxGetSwitchChanMaxDCCarryPwr

### DAQmx_SwitchChan_MaxDCCarryPwr

#### Syntax

DAQmx_SwitchChan_MaxDCCarryPwr

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | (Deprecated) Indicates in watts the maximum DC power that the device can carry. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchChanMaxDCCarryPwr](group__ni-daqmx__c__functions__property__manipulation__getter_1gacc1d1f5b99cd0dcd1136047ec42a894b.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga4d143444e78185b22377905d0b57ab15.html language=enus -->
## TOPIC 02218: DAQmx_SwitchChan_WireMode

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga4d143444e78185b22377905d0b57ab15.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1ga4d143444e78185b22377905d0b57ab15.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchChan_WireModeRemarksData TypeDescriptionRestrictionsuInt32(Deprecated) Indicates the number of wires that the channel switches.Not SettableYou can get this property using:DAQmxGetSwitchChanWireMode

### DAQmx_SwitchChan_WireMode

#### Syntax

DAQmx_SwitchChan_WireMode

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | (Deprecated) Indicates the number of wires that the channel switches. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchChanWireMode](group__ni-daqmx__c__functions__property__manipulation__getter_1ga9f53eba57f476b080f3b2bc90d49b7bb.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gaafd8adf7bbb87dd2757ed973b2773183.html language=enus -->
## TOPIC 02219: DAQmx_SwitchChan_MaxDCSwitchPwr

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gaafd8adf7bbb87dd2757ed973b2773183.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gaafd8adf7bbb87dd2757ed973b2773183.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchChan_MaxDCSwitchPwrRemarksData TypeDescriptionRestrictionsfloat64(Deprecated) Indicates in watts the maximum DC power that the device can switch.Not SettableYou can get this property using:DAQmxGetSwitchChanMaxDCSwitchPwr

### DAQmx_SwitchChan_MaxDCSwitchPwr

#### Syntax

DAQmx_SwitchChan_MaxDCSwitchPwr

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | (Deprecated) Indicates in watts the maximum DC power that the device can switch. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchChanMaxDCSwitchPwr](group__ni-daqmx__c__functions__property__manipulation__getter_1ga74ae0bcbf89f57286b5b3d4caeb21eb6.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gac8e543c356defb715ce449b5add1647d.html language=enus -->
## TOPIC 02220: DAQmx_SwitchChan_MaxACSwitchCurrent

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gac8e543c356defb715ce449b5add1647d.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gac8e543c356defb715ce449b5add1647d.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchChan_MaxACSwitchCurrentRemarksData TypeDescriptionRestrictionsfloat64(Deprecated) Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level.Not SettableYou can get this property using:DAQmxGetSwitchChanMaxACSwitchCur

### DAQmx_SwitchChan_MaxACSwitchCurrent

#### Syntax

DAQmx_SwitchChan_MaxACSwitchCurrent

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | (Deprecated) Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchChanMaxACSwitchCurrent](group__ni-daqmx__c__functions__property__manipulation__getter_1ga9c67cd98d631eb5b5d7d05e90a34a377.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gaeb508608755855592fafdb4f7a5ddc81.html language=enus -->
## TOPIC 02221: DAQmx_SwitchChan_MaxACCarryCurrent

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gaeb508608755855592fafdb4f7a5ddc81.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchchannel__deprecated__capability_1gaeb508608755855592fafdb4f7a5ddc81.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchChan_MaxACCarryCurrentRemarksData TypeDescriptionRestrictionsfloat64(Deprecated) Indicates in amperes the maximum AC current that the device can carry.Not SettableYou can get this property using:DAQmxGetSwitchChanMaxACCarryCurrent

### DAQmx_SwitchChan_MaxACCarryCurrent

#### Syntax

DAQmx_SwitchChan_MaxACCarryCurrent

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | (Deprecated) Indicates in amperes the maximum AC current that the device can carry. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchChanMaxACCarryCurrent](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf8d9dfb9ea12d2810b0ceaf5fe60da1b.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated.html language=enus -->
## TOPIC 02222: Deprecated

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCapabilityGroup membersNameDescriptionDAQmx_SwitchDev_AutoConnAnlgBusDAQmx_SwitchDev_PwrDownLatchRelaysAfterSettlingDAQmx_SwitchDev_SettledDAQmx_SwitchDev_SettlingTimeAttachmentsNone

### Deprecated

#### Groups

- Capability

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_SwitchDev_AutoConnAnlgBus |  |
| DAQmx_SwitchDev_PwrDownLatchRelaysAfterSettling |  |
| DAQmx_SwitchDev_Settled |  |
| DAQmx_SwitchDev_SettlingTime |  |

#### Attachments

None

Parent topic:

SwitchDevice

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated_1ga39c071a691e8d8fe66f9b861c77a9cd7.html language=enus -->
## TOPIC 02223: DAQmx_SwitchDev_Settled

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated_1ga39c071a691e8d8fe66f9b861c77a9cd7.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated_1ga39c071a691e8d8fe66f9b861c77a9cd7.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_SettledRemarksData TypeDescriptionRestrictionsbool32(Deprecated) Indicates when Settling Time expires.Not SettableYou can get this property using:DAQmxGetSwitchDevSettled

### DAQmx_SwitchDev_Settled

#### Syntax

DAQmx_SwitchDev_Settled

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | (Deprecated) Indicates when Settling Time expires. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevSettled](group__ni-daqmx__c__functions__property__manipulation__getter_1ga042a51c53b964b73f92203f7698a6c20.html)

Parent topic:

Deprecated

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated_1gaafb8b64bfd5108b947df9b6ebdc42c51.html language=enus -->
## TOPIC 02224: DAQmx_SwitchDev_SettlingTime

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated_1gaafb8b64bfd5108b947df9b6ebdc42c51.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated_1gaafb8b64bfd5108b947df9b6ebdc42c51.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_SettlingTimeRemarksData TypeDescriptionRestrictionsfloat64(Deprecated) Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settl

### DAQmx_SwitchDev_SettlingTime

#### Syntax

DAQmx_SwitchDev_SettlingTime

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | (Deprecated) Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported settling times. |  |

You can get/set this property using:

- [DAQmxGetSwitchDevSettlingTime](group__ni-daqmx__c__functions__property__manipulation__getter_1ga3a4f50870246bcd40f2fe44a20d87237.html)
- [DAQmxSetSwitchDevSettlingTime](group__ni-daqmx__c__functions__property__manipulation__setter_1ga3f924e07a6f59dc5b68047d2c4747909.html)

Parent topic:

Deprecated

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated_1gad903fdf5035a3c872730356d8d083b93.html language=enus -->
## TOPIC 02225: DAQmx_SwitchDev_AutoConnAnlgBus

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated_1gad903fdf5035a3c872730356d8d083b93.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated_1gad903fdf5035a3c872730356d8d083b93.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_AutoConnAnlgBusRemarksData TypeDescriptionRestrictionsbool32(Deprecated) Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property.You can get/set this property using:DAQmxGetSwitchDevAutoConnAnlgBusDAQ

### DAQmx_SwitchDev_AutoConnAnlgBus

#### Syntax

DAQmx_SwitchDev_AutoConnAnlgBus

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | (Deprecated) Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property. |  |

You can get/set this property using:

- [DAQmxGetSwitchDevAutoConnAnlgBus](group__ni-daqmx__c__functions__property__manipulation__getter_1ga814c1223c065eaa2cce5d87ea4edae32.html)
- [DAQmxSetSwitchDevAutoConnAnlgBus](group__ni-daqmx__c__functions__property__manipulation__setter_1gaf87c59d98c5519e244e336346989d5ba.html)

Parent topic:

Deprecated

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability.html language=enus -->
## TOPIC 02226: Capability

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_SwitchDev_NumColumnsDAQmx_SwitchDev_NumRelaysDAQmx_SwitchDev_NumRowsDAQmx_SwitchDev_NumSwitchChansDAQmx_SwitchDev_RelayListDAQmx_SwitchDev_SwitchChanListDAQmx_SwitchDev_TemperatureDAQmx_SwitchDev_TopologyAttachmentsNone

### Capability

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_SwitchDev_NumColumns |  |
| DAQmx_SwitchDev_NumRelays |  |
| DAQmx_SwitchDev_NumRows |  |
| DAQmx_SwitchDev_NumSwitchChans |  |
| DAQmx_SwitchDev_RelayList |  |
| DAQmx_SwitchDev_SwitchChanList |  |
| DAQmx_SwitchDev_Temperature |  |
| DAQmx_SwitchDev_Topology |  |

#### Attachments

None

Parent topic:

Deprecated

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga1469d564884972ce2bebdc0d468ec2a4.html language=enus -->
## TOPIC 02227: DAQmx_SwitchDev_RelayList

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga1469d564884972ce2bebdc0d468ec2a4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga1469d564884972ce2bebdc0d468ec2a4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_RelayListRemarksData TypeDescriptionRestrictionschar*(Deprecated) Indicates a comma-delimited list of relay names.Not SettableYou can get this property using:DAQmxGetSwitchDevRelayList

### DAQmx_SwitchDev_RelayList

#### Syntax

DAQmx_SwitchDev_RelayList

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | (Deprecated) Indicates a comma-delimited list of relay names. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevRelayList](group__ni-daqmx__c__functions__property__manipulation__getter_1gab33d1d24938b254786bc3b0a2e08d457.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga24deb911f8083858dd636f8c9f0e730e.html language=enus -->
## TOPIC 02228: DAQmx_SwitchDev_Temperature

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga24deb911f8083858dd636f8c9f0e730e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga24deb911f8083858dd636f8c9f0e730e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_TemperatureRemarksData TypeDescriptionRestrictionsfloat64(Deprecated) Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information.Not SettableYou can get this property using:DAQmxGetSwitchDevTemperat

### DAQmx_SwitchDev_Temperature

#### Syntax

DAQmx_SwitchDev_Temperature

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| float64 | (Deprecated) Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevTemperature](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa17b8ba245512cb1f9c12c7bfb208710.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga2e18653cccba612675a68c45f28c78a8.html language=enus -->
## TOPIC 02229: DAQmx_SwitchDev_SwitchChanList

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga2e18653cccba612675a68c45f28c78a8.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga2e18653cccba612675a68c45f28c78a8.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_SwitchChanListRemarksData TypeDescriptionRestrictionschar*(Deprecated) Indicates a comma-delimited list of channel names for the current topology of the device.Not SettableYou can get this property using:DAQmxGetSwitchDevSwitchChanList

### DAQmx_SwitchDev_SwitchChanList

#### Syntax

DAQmx_SwitchDev_SwitchChanList

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | (Deprecated) Indicates a comma-delimited list of channel names for the current topology of the device. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevSwitchChanList](group__ni-daqmx__c__functions__property__manipulation__getter_1gafa9077165569eae2e86335005befbf03.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga4799b0ea55a28cc769e0ff4245a819e6.html language=enus -->
## TOPIC 02230: DAQmx_SwitchDev_Topology

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga4799b0ea55a28cc769e0ff4245a819e6.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga4799b0ea55a28cc769e0ff4245a819e6.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_TopologyRemarksData TypeDescriptionRestrictionschar*(Deprecated) Indicates the current topology of the device. This value is one of the topology options in DAQmxSwitchSetTopologyAndReset().Not SettableYou can get this property using:DAQmxGetSwitchDevTopology

### DAQmx_SwitchDev_Topology

#### Syntax

DAQmx_SwitchDev_Topology

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | (Deprecated) Indicates the current topology of the device. This value is one of the topology options in DAQmxSwitchSetTopologyAndReset(). | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevTopology](group__ni-daqmx__c__functions__property__manipulation__getter_1ga0dad9fe23fcd5185856d59616153641c.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga6a45f0cf4193eca2b6cf34233fdf9adf.html language=enus -->
## TOPIC 02231: DAQmx_SwitchDev_NumRows

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga6a45f0cf4193eca2b6cf34233fdf9adf.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1ga6a45f0cf4193eca2b6cf34233fdf9adf.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_NumRowsRemarksData TypeDescriptionRestrictionsuInt32(Deprecated) Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology.Not SettableYou can get this property using:DAQmxGetSwitchDevNumRows

### DAQmx_SwitchDev_NumRows

#### Syntax

DAQmx_SwitchDev_NumRows

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | (Deprecated) Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevNumRows](group__ni-daqmx__c__functions__property__manipulation__getter_1gabf27adcf9cff758731c8dbb56b98ccaf.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gaa161cffd423d4237501cd3442a3435ce.html language=enus -->
## TOPIC 02232: DAQmx_SwitchDev_NumRelays

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gaa161cffd423d4237501cd3442a3435ce.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gaa161cffd423d4237501cd3442a3435ce.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_NumRelaysRemarksData TypeDescriptionRestrictionsuInt32(Deprecated) Indicates the number of relays on the device. This value matches the number of relay names in Relay List.Not SettableYou can get this property using:DAQmxGetSwitchDevNumRelays

### DAQmx_SwitchDev_NumRelays

#### Syntax

DAQmx_SwitchDev_NumRelays

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | (Deprecated) Indicates the number of relays on the device. This value matches the number of relay names in Relay List. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevNumRelays](group__ni-daqmx__c__functions__property__manipulation__getter_1ga635ec7065eb256422daf2b7b37efb8d0.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gacda60a6670154371ea3d46438e3ce5fa.html language=enus -->
## TOPIC 02233: DAQmx_SwitchDev_NumSwitchChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gacda60a6670154371ea3d46438e3ce5fa.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gacda60a6670154371ea3d46438e3ce5fa.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_NumSwitchChansRemarksData TypeDescriptionRestrictionsuInt32(Deprecated) Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in Switch Channel List.Not SettableYou can get this property using:DAQmxGetSwit

### DAQmx_SwitchDev_NumSwitchChans

#### Syntax

DAQmx_SwitchDev_NumSwitchChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | (Deprecated) Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in Switch Channel List. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevNumSwitchChans](group__ni-daqmx__c__functions__property__manipulation__getter_1ga47878f579fc198a623bbf356f32da6a8.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gaf2bb6dc2db07be2153c27f26c7f08429.html language=enus -->
## TOPIC 02234: DAQmx_SwitchDev_NumColumns

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gaf2bb6dc2db07be2153c27f26c7f08429.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchdevice__deprecated__capability_1gaf2bb6dc2db07be2153c27f26c7f08429.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchDev_NumColumnsRemarksData TypeDescriptionRestrictionsuInt32(Deprecated) Indicates the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology.Not SettableYou can get this property using:DAQmxGetSwitchDevNumColumns

### DAQmx_SwitchDev_NumColumns

#### Syntax

DAQmx_SwitchDev_NumColumns

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | (Deprecated) Indicates the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchDevNumColumns](group__ni-daqmx__c__functions__property__manipulation__getter_1ga078240b99ade4388b7aaa036e21a9ede.html)

Parent topic:

Capability

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchscan.html language=enus -->
## TOPIC 02235: SwitchScan

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchscan.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchscan.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsDeprecatedGroup membersNoneAttachmentsNone

### SwitchScan

#### Groups

- Deprecated

#### Group members

None

#### Attachments

None

Parent topic:

NI-DAQmx C Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchscan__deprecated.html language=enus -->
## TOPIC 02236: Deprecated

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchscan__deprecated.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchscan__deprecated.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_SwitchScan_BreakModeDAQmx_SwitchScan_RepeatModeDAQmx_SwitchScan_WaitingForAdvAttachmentsNone

### Deprecated

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_SwitchScan_BreakMode |  |
| DAQmx_SwitchScan_RepeatMode |  |
| DAQmx_SwitchScan_WaitingForAdv |  |

#### Attachments

None

Parent topic:

SwitchScan

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchscan__deprecated_1ga59152e1156769e16bb01b5fae239805a.html language=enus -->
## TOPIC 02237: DAQmx_SwitchScan_BreakMode

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchscan__deprecated_1ga59152e1156769e16bb01b5fae239805a.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchscan__deprecated_1ga59152e1156769e16bb01b5fae239805a.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchScan_BreakModeRemarksData TypeDescriptionRestrictionsint32(Deprecated) Specifies the action to take between each entry in a scan list.Valid valuesDAQmx_Val_NoAction10227When advancing to the next entry in the scan list, leave all previous connections intact.DAQmx_Val_BreakBeforeMak

### DAQmx_SwitchScan_BreakMode

#### Syntax

DAQmx_SwitchScan_BreakMode

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | (Deprecated) Specifies the action to take between each entry in a scan list. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_NoAction | 10227 | When advancing to the next entry in the scan list, leave all previous connections intact. |
| DAQmx_Val_BreakBeforeMake | 10110 | When advancing to the next entry in the scan list, disconnect all previous connections before making any new connections. |

You can get/set/reset this property using:

- [DAQmxGetSwitchScanBreakMode](group__ni-daqmx__c__functions__property__manipulation__getter_1ga5d440a77a80a09f2939394a03c540c50.html)
- [DAQmxSetSwitchScanBreakMode](group__ni-daqmx__c__functions__property__manipulation__setter_1gafb1153a142c588576cd9f2613229b232.html)
- [DAQmxResetSwitchScanBreakMode](group__ni-daqmx__c__functions__property__manipulation__resetter_1ga6a5c47b5ccdfa6d83453d8239b92989e.html)

Parent topic:

Deprecated

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchscan__deprecated_1ga79b391fb6673c66b645790c39f680ad4.html language=enus -->
## TOPIC 02238: DAQmx_SwitchScan_RepeatMode

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchscan__deprecated_1ga79b391fb6673c66b645790c39f680ad4.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchscan__deprecated_1ga79b391fb6673c66b645790c39f680ad4.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchScan_RepeatModeRemarksData TypeDescriptionRestrictionsint32(Deprecated) Specifies if the task advances through the scan list multiple times.Valid valuesDAQmx_Val_Finite10172The task advances through the scan list one time only. NI-DAQmx ignores any Advance Triggers after completing

### DAQmx_SwitchScan_RepeatMode

#### Syntax

DAQmx_SwitchScan_RepeatMode

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| int32 | (Deprecated) Specifies if the task advances through the scan list multiple times. |  |

| Valid values |  |  |
| --- | --- | --- |
| DAQmx_Val_Finite | 10172 | The task advances through the scan list one time only. NI-DAQmx ignores any Advance Triggers after completing the scan list. |
| DAQmx_Val_Cont | 10117 | The task returns to the beginning of the scan list when it reaches the end of the scan list. |

You can get/set/reset this property using:

- [DAQmxGetSwitchScanRepeatMode](group__ni-daqmx__c__functions__property__manipulation__getter_1ga85c7520714d5aab236591a5e58925de5.html)
- [DAQmxSetSwitchScanRepeatMode](group__ni-daqmx__c__functions__property__manipulation__setter_1ga25b5488b1e25671047be6ab18cb9615b.html)
- [DAQmxResetSwitchScanRepeatMode](group__ni-daqmx__c__functions__property__manipulation__resetter_1gaa7273d45780743fd7464e7a955ca518f.html)

Parent topic:

Deprecated

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__switchscan__deprecated_1ga84ba900f69968ecdff9959cdc583de00.html language=enus -->
## TOPIC 02239: DAQmx_SwitchScan_WaitingForAdv

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__switchscan__deprecated_1ga84ba900f69968ecdff9959cdc583de00.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__switchscan__deprecated_1ga84ba900f69968ecdff9959cdc583de00.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_SwitchScan_WaitingForAdvRemarksData TypeDescriptionRestrictionsbool32(Deprecated) Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list.Not SettableYou can get this property using:DAQmxGetSwitchSca

### DAQmx_SwitchScan_WaitingForAdv

#### Syntax

DAQmx_SwitchScan_WaitingForAdv

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | (Deprecated) Indicates if the switch hardware is waiting for an Advance Trigger. If the hardware is waiting, it completed the previous entry in the scan list. | Not Settable |

You can get this property using:

- [DAQmxGetSwitchScanWaitingForAdv](group__ni-daqmx__c__functions__property__manipulation__getter_1ga639f5966503d4dbc71bab8624f2732d9.html)

Parent topic:

Deprecated

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__system.html language=enus -->
## TOPIC 02240: System

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__system.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__system.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsSystemGroup membersNameDescriptionDAQmx_Sys_DevNamesDAQmx_Sys_GlobalChansDAQmx_Sys_ScalesDAQmx_Sys_TasksAttachmentsNone

### System

#### Groups

- System

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Sys_DevNames |  |
| DAQmx_Sys_GlobalChans |  |
| DAQmx_Sys_Scales |  |
| DAQmx_Sys_Tasks |  |

#### Attachments

None

Parent topic:

NI-DAQmx C Properties

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__system_1gab40f2695c26c785dd458c3a1aa3b5a3e.html language=enus -->
## TOPIC 02241: DAQmx_Sys_GlobalChans

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__system_1gab40f2695c26c785dd458c3a1aa3b5a3e.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__system_1gab40f2695c26c785dd458c3a1aa3b5a3e.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Sys_GlobalChansRemarksData TypeDescriptionRestrictionschar*Indicates an array that contains the names of all global channels saved on the system.Not SettableYou can get this property using:DAQmxGetSysGlobalChans

### DAQmx_Sys_GlobalChans

#### Syntax

DAQmx_Sys_GlobalChans

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates an array that contains the names of all global channels saved on the system. | Not Settable |

You can get this property using:

- [DAQmxGetSysGlobalChans](group__ni-daqmx__c__functions__property__manipulation__getter_1gaa1b486669a78f094677c87ec66a0a7d1.html)

Parent topic:

System

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__system_1gae81a9254faa099e98d837580d0d1d3bd.html language=enus -->
## TOPIC 02242: DAQmx_Sys_Tasks

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__system_1gae81a9254faa099e98d837580d0d1d3bd.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__system_1gae81a9254faa099e98d837580d0d1d3bd.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Sys_TasksRemarksData TypeDescriptionRestrictionschar*Indicates an array that contains the names of all tasks saved on the system.Not SettableYou can get this property using:DAQmxGetSysTasks

### DAQmx_Sys_Tasks

#### Syntax

DAQmx_Sys_Tasks

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates an array that contains the names of all tasks saved on the system. | Not Settable |

You can get this property using:

- [DAQmxGetSysTasks](group__ni-daqmx__c__functions__property__manipulation__getter_1gaec83b3d3a68b62e15f10d1587c2c77fe.html)

Parent topic:

System

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__system_1gaf43290d26a281b9a9033fe1e349797a2.html language=enus -->
## TOPIC 02243: DAQmx_Sys_DevNames

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__system_1gaf43290d26a281b9a9033fe1e349797a2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__system_1gaf43290d26a281b9a9033fe1e349797a2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Sys_DevNamesRemarksData TypeDescriptionRestrictionschar*Indicates the names of all devices installed in the system.Not SettableYou can get this property using:DAQmxGetSysDevNames

### DAQmx_Sys_DevNames

#### Syntax

DAQmx_Sys_DevNames

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the names of all devices installed in the system. | Not Settable |

You can get this property using:

- [DAQmxGetSysDevNames](group__ni-daqmx__c__functions__property__manipulation__getter_1ga4d127cd32bf378b973d7c882c1e78754.html)

Parent topic:

System

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__system__system.html language=enus -->
## TOPIC 02244: System

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__system__system.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__system__system.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNI-DAQ VersionGroup membersNoneAttachmentsNone

### System

#### Groups

- NI-DAQ Version

#### Group members

None

#### Attachments

None

Parent topic:

System

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__system__system__ni__daq__version.html language=enus -->
## TOPIC 02245: NI-DAQ Version

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__system__system__ni__daq__version.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__system__system__ni__daq__version.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionDAQmx_Sys_NIDAQMajorVersionDAQmx_Sys_NIDAQMinorVersionDAQmx_Sys_NIDAQUpdateVersionAttachmentsNone

### NI-DAQ Version

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| DAQmx_Sys_NIDAQMajorVersion |  |
| DAQmx_Sys_NIDAQMinorVersion |  |
| DAQmx_Sys_NIDAQUpdateVersion |  |

#### Attachments

None

Parent topic:

System

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__system__system__ni__daq__version_1ga69f97336b63c2c6aae8745048829e281.html language=enus -->
## TOPIC 02246: DAQmx_Sys_NIDAQMajorVersion

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__system__system__ni__daq__version_1ga69f97336b63c2c6aae8745048829e281.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__system__system__ni__daq__version_1ga69f97336b63c2c6aae8745048829e281.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Sys_NIDAQMajorVersionRemarksData TypeDescriptionRestrictionsuInt32Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0.Not SettableYou can get this property using:DAQmxGetSysNIDAQMajorVersion

### DAQmx_Sys_NIDAQMajorVersion

#### Syntax

DAQmx_Sys_NIDAQMajorVersion

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| uInt32 | Indicates the major portion of the installed version of NI-DAQmx, such as 7 for version 7.0. | Not Settable |

You can get this property using:

- [DAQmxGetSysNIDAQMajorVersion](group__ni-daqmx__c__functions__property__manipulation__getter_1ga8252089e116607ce33cabc55b686d9a4.html)

Parent topic:

NI-DAQ Version

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__task_1ga3afc9be463d568b69d03c2e9d7d89e61.html language=enus -->
## TOPIC 02247: DAQmx_Task_Devices

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__task_1ga3afc9be463d568b69d03c2e9d7d89e61.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__task_1ga3afc9be463d568b69d03c2e9d7d89e61.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Task_DevicesRemarksData TypeDescriptionRestrictionschar*Indicates an array containing the names of all devices in the task.Not SettableYou can get this property using:DAQmxGetTaskDevices

### DAQmx_Task_Devices

#### Syntax

DAQmx_Task_Devices

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates an array containing the names of all devices in the task. | Not Settable |

You can get this property using:

- [DAQmxGetTaskDevices](group__ni-daqmx__c__functions__property__manipulation__getter_1ga44f56fe42ea49717d4d1cc20fad4d8cb.html)

Parent topic:

Task

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__task_1ga4a6ec22766f6f5f361228c6f021c69db.html language=enus -->
## TOPIC 02248: DAQmx_Task_Channels

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__task_1ga4a6ec22766f6f5f361228c6f021c69db.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__task_1ga4a6ec22766f6f5f361228c6f021c69db.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Task_ChannelsRemarksData TypeDescriptionRestrictionschar*Indicates the names of all virtual channels in the task.Not SettableYou can get this property using:DAQmxGetTaskChannels

### DAQmx_Task_Channels

#### Syntax

DAQmx_Task_Channels

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the names of all virtual channels in the task. | Not Settable |

You can get this property using:

- [DAQmxGetTaskChannels](group__ni-daqmx__c__functions__property__manipulation__getter_1ga30a0aa5891cf52bf52a52e6a810602d3.html)

Parent topic:

Task

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__task_1gaa0c4fbd0c7cb02bb8a1754c549aac08b.html language=enus -->
## TOPIC 02249: DAQmx_Task_Complete

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__task_1gaa0c4fbd0c7cb02bb8a1754c549aac08b.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__task_1gaa0c4fbd0c7cb02bb8a1754c549aac08b.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Task_CompleteRemarksData TypeDescriptionRestrictionsbool32Indicates whether the task completed execution.Not SettableYou can get this property using:DAQmxGetTaskComplete

### DAQmx_Task_Complete

#### Syntax

DAQmx_Task_Complete

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| bool32 | Indicates whether the task completed execution. | Not Settable |

You can get this property using:

- [DAQmxGetTaskComplete](group__ni-daqmx__c__functions__property__manipulation__getter_1gad846386f30699095be53c26b953f1c99.html)

Parent topic:

Task

<!--NI_TOPIC bundle=ni-daqmx-c-api-ref path=group__ni-daqmx__c__properties__task_1gabf11c20fbb03c2842dc1916aa36081c2.html language=enus -->
## TOPIC 02250: DAQmx_Task_Name

- bundle_id: `ni-daqmx-c-api-ref`
- source_path: `group__ni-daqmx__c__properties__task_1gabf11c20fbb03c2842dc1916aa36081c2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-c-api-ref/raw/resource/enus/group__ni-daqmx__c__properties__task_1gabf11c20fbb03c2842dc1916aa36081c2.html
- document_id: `ni-daqmx-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxDAQmx_Task_NameRemarksData TypeDescriptionRestrictionschar*Indicates the name of the task.Not SettableYou can get this property using:DAQmxGetTaskName

### DAQmx_Task_Name

#### Syntax

DAQmx_Task_Name

#### Remarks

| Data Type | Description | Restrictions |
| --- | --- | --- |
| char* | Indicates the name of the task. | Not Settable |

You can get this property using:

- [DAQmxGetTaskName](group__ni-daqmx__c__functions__property__manipulation__getter_1gaf483bdccf74f647eebe3ebac9b5583b4.html)

Parent topic:

Task
