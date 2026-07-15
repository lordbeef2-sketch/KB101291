# NI DOCUMENT BUNDLE: ni-digital-pattern-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-digital-pattern-c-api-ref start=1 end=112 -->
<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-Digital Pattern Driver C API Reference

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-Digital Pattern Driver C API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes.html language=enus -->
## TOPIC 00002: Attributes

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsClock GeneratorEventsFrequency MeasurementHistory RAMInherent IVI AttributesKeep AliveLevel ConfigurationPatternsPin ControlPPMUSynchronizationTDR Endpoint TerminationTiming OffsetTrigger ConfigurationGroup membersNoneAttachmentsNone

### Attributes

#### Groups

- Clock Generator
- Events
- Frequency Measurement
- History RAM
- Inherent IVI Attributes
- Keep Alive
- Level Configuration
- Patterns
- Pin Control
- PPMU
- Synchronization
- TDR Endpoint Termination
- Timing Offset
- Trigger Configuration

#### Group members

None

#### Attachments

None

Parent topic:

niDigital.h

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__clock__generator.html language=enus -->
## TOPIC 00003: Clock Generator

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__clock__generator.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__clock__generator.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCYSpecifies the frequency for the clock generator. NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNINGIndicates whether the clock generator is running. AttachmentsNone

### Clock Generator

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCY | Specifies the frequency for the clock generator. |
| NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNING | Indicates whether the clock generator is running. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__clock__generator_1ga6a076e8f864bbd7351f01d2b2b31c161.html language=enus -->
## TOPIC 00004: NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNING

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__clock__generator_1ga6a076e8f864bbd7351f01d2b2b31c161.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__clock__generator_1ga6a076e8f864bbd7351f01d2b2b31c161.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the clock generator is running. SyntaxNIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNINGNumeric ValueData TypeAccessApplies To1150074ViBooleanRead-OnlyChannels, Pins

### NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNING

Indicates whether the clock generator is running.

#### Syntax

NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150074 | ViBoolean | Read-Only | Channels, Pins |

Parent topic:

Clock Generator

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__clock__generator_1ga7a9c904498d818506b8ca089c391a066.html language=enus -->
## TOPIC 00005: NIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCY

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__clock__generator_1ga7a9c904498d818506b8ca089c391a066.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__clock__generator_1ga7a9c904498d818506b8ca089c391a066.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency for the clock generator. SyntaxNIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCYNumeric ValueData TypeAccessApplies To1150073ViReal64Read/WriteChannels, PinsRemarksHigh-Level Functions:niDigital_ClockGenerator_GenerateClock

### NIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCY

Specifies the frequency for the clock generator.

#### Syntax

NIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150073 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

**High-Level Functions**:

- [niDigital_ClockGenerator_GenerateClock](group____root__ni_digital__functions__clock__generator_1ga1c5e6c8d1abfec3fc65142fcd8510bce.html)

Parent topic:

Clock Generator

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__events.html language=enus -->
## TOPIC 00006: Events

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__events.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__events.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINALSpecifies the destination terminal for exporting the Pattern Opcode Event. NIDIGITAL_ATTR_EXPORTED_RIO_EVENT_OUTPUT_TERMINALSpecifies the destination terminal for exporting the RIO Event. NIDIGITAL_ATTR

### Events

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL | Specifies the destination terminal for exporting the Pattern Opcode Event. |
| NIDIGITAL_ATTR_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL | Specifies the destination terminal for exporting the RIO Event. |
| NIDIGITAL_ATTR_RIO_EVENT_TERMINAL_NAME | Specifies the terminal name for the output trigger signal of the specified instance of a RIO Event. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__events_1ga346d103e2ddb7805dbf8c567151b62c6.html language=enus -->
## TOPIC 00007: NIDIGITAL_ATTR_RIO_EVENT_TERMINAL_NAME

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__events_1ga346d103e2ddb7805dbf8c567151b62c6.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__events_1ga346d103e2ddb7805dbf8c567151b62c6.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal name for the output trigger signal of the specified instance of a RIO Event. SyntaxNIDIGITAL_ATTR_RIO_EVENT_TERMINAL_NAMENumeric ValueData TypeAccessApplies To1150091ViStringRead-OnlyRIO EventsRemarks You can use this terminal name as an input signal source for another trigger

### NIDIGITAL_ATTR_RIO_EVENT_TERMINAL_NAME

Specifies the terminal name for the output trigger signal of the specified instance of a RIO Event.

#### Syntax

NIDIGITAL_ATTR_RIO_EVENT_TERMINAL_NAME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150091 | ViString | Read-Only | RIO Events |

#### Remarks

You can use this terminal name as an input signal source for another trigger.

Parent topic:

Events

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__events_1ga8b74cb07c4a9881e6fba56ac0efe912a.html language=enus -->
## TOPIC 00008: NIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__events_1ga8b74cb07c4a9881e6fba56ac0efe912a.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__events_1ga8b74cb07c4a9881e6fba56ac0efe912a.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for exporting the Pattern Opcode Event. SyntaxNIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To1150041ViStringRead/WritePattern Opcode EventsRemarks Terminals can be specified in one of two ways. If the digital patte

### NIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL

Specifies the destination terminal for exporting the Pattern Opcode Event.

#### Syntax

NIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150041 | ViString | Read/Write | Pattern Opcode Events |

#### Remarks

Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

| Defined Values: |  |
| --- | --- |
| PXI_Trig0 | PXI trigger line 0 |
| PXI_Trig1 | PXI trigger line 1 |
| PXI_Trig2 | PXI trigger line 2 |
| PXI_Trig3 | PXI trigger line 3 |
| PXI_Trig4 | PXI trigger line 4 |
| PXI_Trig5 | PXI trigger line 5 |
| PXI_Trig6 | PXI trigger line 6 |
| PXI_Trig7 | PXI trigger line 7 |

Parent topic:

Events

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__events_1gaf3f3a08de0531376732b038f1320b8e0.html language=enus -->
## TOPIC 00009: NIDIGITAL_ATTR_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__events_1gaf3f3a08de0531376732b038f1320b8e0.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__events_1gaf3f3a08de0531376732b038f1320b8e0.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for exporting the RIO Event. SyntaxNIDIGITAL_ATTR_EXPORTED_RIO_EVENT_OUTPUT_TERMINALNumeric ValueData TypeAccessApplies To1150090ViStringRead/WriteRIO EventsRemarks Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and y

### NIDIGITAL_ATTR_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL

Specifies the destination terminal for exporting the RIO Event.

#### Syntax

NIDIGITAL_ATTR_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150090 | ViString | Read/Write | RIO Events |

#### Remarks

Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

| Defined Values: |  |
| --- | --- |
| PXI_Trig0 | PXI trigger line 0 |
| PXI_Trig1 | PXI trigger line 1 |
| PXI_Trig2 | PXI trigger line 2 |
| PXI_Trig3 | PXI trigger line 3 |
| PXI_Trig4 | PXI trigger line 4 |
| PXI_Trig5 | PXI trigger line 5 |
| PXI_Trig6 | PXI trigger line 6 |
| PXI_Trig7 | PXI trigger line 7 |

Parent topic:

Events

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__frequency__measurement.html language=enus -->
## TOPIC 00010: Frequency Measurement

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__frequency__measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__frequency__measurement.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLEDSpecifies whether hysteresis is enabled for the frequency counters of a digital pattern instrument. NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_MODEDetermines how the frequency counters of a digital pattern ins

### Frequency Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED | Specifies whether hysteresis is enabled for the frequency counters of a digital pattern instrument. |
| NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_MODE | Determines how the frequency counters of a digital pattern instrument make measurements. |
| NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_TIME | Specifies the measurement time for the frequency counter. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__frequency__measurement_1gaacba6c11223adea9bfc5cad1b289e141.html language=enus -->
## TOPIC 00011: NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__frequency__measurement_1gaacba6c11223adea9bfc5cad1b289e141.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__frequency__measurement_1gaacba6c11223adea9bfc5cad1b289e141.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether hysteresis is enabled for the frequency counters of a digital pattern instrument. SyntaxNIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLEDNumeric ValueData TypeAccessApplies To1150085ViBooleanRead/WriteN/ARemarks Frequency counter hysteresis filters out noise by requiring the corr

### NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED

Specifies whether hysteresis is enabled for the frequency counters of a digital pattern instrument.

#### Syntax

NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150085 | ViBoolean | Read/Write | N/A |

#### Remarks

Frequency counter hysteresis filters out noise by requiring the corresponding rising and falling edges of a signal to pass through both Vol and Voh in the correct order.

Note

Hysteresis is available only when the frequency counter measurement mode is set to **parallel**.

**Related Information**

- [niDigital_FrequencyCounter_ConfigureMeasurementMode](group____root__ni_digital__functions__frequency__measurement_1ga98d0aec5fe820e67cc77392e4f868062.html)
- [NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_MODE](group____root__ni_digital__attributes__frequency__measurement_1ga126b0395537d270dff1307c3f123ffca.html)

Parent topic:

Frequency Measurement

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__history__ram.html language=enus -->
## TOPIC 00012: History RAM

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__history__ram.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__history__ram.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBERSpecifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger. NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITESpecifies the size, in sam

### History RAM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER | Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger. |
| NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITE | Specifies the size, in samples, of the host memory buffer. |
| NIDIGITAL_ATTR_HISTORY_RAM_CYCLES_TO_ACQUIRE | Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0. |
| NIDIGITAL_ATTR_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE | Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full. |
| NIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE | Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously. |
| NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES | Specifies the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0. |
| NIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE | Specifies the type of trigger condition on which History RAM starts acquiring pattern information. |
| NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET | Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger. |
| NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL | Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger. |
| NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET | Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__history__ram_1gab79a6f4befb9fce2e1643ff4c6a1ff9c.html language=enus -->
## TOPIC 00013: NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITE

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__history__ram_1gab79a6f4befb9fce2e1643ff4c6a1ff9c.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__history__ram_1gab79a6f4befb9fce2e1643ff4c6a1ff9c.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the size, in samples, of the host memory buffer. SyntaxNIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITENumeric ValueData TypeAccessApplies To1150079ViInt64Read/WriteN/ARemarksValid Values:0-INT64_MAXDefault Value:32,000

### NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITE

Specifies the size, in samples, of the host memory buffer.

#### Syntax

NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150079 | ViInt64 | Read/Write | N/A |

#### Remarks

| Valid Values: |
| --- |
| 0-INT64_MAX |

| Default Value: |
| --- |
| 32,000 |

Parent topic:

History RAM

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__history__ram_1gac442a5455cf4f611cc16af9c0dfda4ab.html language=enus -->
## TOPIC 00014: NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__history__ram_1gac442a5455cf4f611cc16af9c0dfda4ab.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__history__ram_1gac442a5455cf4f611cc16af9c0dfda4ab.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger. SyntaxNIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSETNumeric ValueData TypeAccessApplies To1150052ViIn

### NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET

Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.

#### Syntax

NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150052 | ViInt64 | Read/Write | N/A |

#### Remarks

**High-Level Functions**:

- [niDigital_ConfigurePatternLabelHistoryRAMTrigger](group____root__ni_digital__functions__history__ram_1gabbc12535c3ee176e74172c501b645db4.html)

Parent topic:

History RAM

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__history__ram_1gad30eb4ae25a3e2996efe953bfad8d436.html language=enus -->
## TOPIC 00015: NIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__history__ram_1gad30eb4ae25a3e2996efe953bfad8d436.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__history__ram_1gad30eb4ae25a3e2996efe953bfad8d436.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously. SyntaxNIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITENumeric ValueData TypeAccessApplies To1150078ViBooleanRead/WriteN/ARemarks The maximum number of samples that will be acquired when t

### NIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE

Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously.

#### Syntax

NIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150078 | ViBoolean | Read/Write | N/A |

#### Remarks

The maximum number of samples that will be acquired when this property is set to VI_TRUE is determined by the instrument History RAM depth specification and the History RAM Max Samples to Acquire Per Site property.

| Valid Values: |  |
| --- | --- |
| VI_TRUE | Specifies that History RAM results will not stream into the host buffer until a History RAM fetch API is called. |
| VI_FALSE | Specifies that History RAM results will automatically start streaming into a host buffer after a pattern is burst and the History RAM has triggered. |

| Default Value: |
| --- |
| VI_TRUE |

Parent topic:

History RAM

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__history__ram_1gafcc6149a6ae0f63f051775f1956a843c.html language=enus -->
## TOPIC 00016: NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__history__ram_1gafcc6149a6ae0f63f051775f1956a843c.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__history__ram_1gafcc6149a6ae0f63f051775f1956a843c.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger. SyntaxNIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABELNumeric ValueData TypeAccessApplies To1150

### NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL

Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger.

#### Syntax

NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150046 | ViString | Read/Write | N/A |

#### Remarks

**High-Level Functions**:

- [niDigital_ConfigurePatternLabelHistoryRAMTrigger](group____root__ni_digital__functions__history__ram_1gabbc12535c3ee176e74172c501b645db4.html)

Parent topic:

History RAM

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes.html language=enus -->
## TOPIC 00017: Inherent IVI Attributes

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvanced Session InformationDriver CapabilitiesDriver IdentificationInstrument IdentificationUser OptionsGroup membersNoneAttachmentsNone

### Inherent IVI Attributes

#### Groups

- Advanced Session Information
- Driver Capabilities
- Driver Identification
- Instrument Identification
- User Options

#### Group members

None

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__advanced__session__information_1ga6366bf47973e76b76282b7546a5d98d3.html language=enus -->
## TOPIC 00018: NIDIGITAL_ATTR_DRIVER_SETUP

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__advanced__session__information_1ga6366bf47973e76b76282b7546a5d98d3.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__advanced__session__information_1ga6366bf47973e76b76282b7546a5d98d3.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This attribute returns initial values for NI-Digital Pattern Driver attributes as a string. SyntaxNIDIGITAL_ATTR_DRIVER_SETUPNumeric ValueData TypeAccessApplies To1050007ViStringRead-OnlyN/A

### NIDIGITAL_ATTR_DRIVER_SETUP

This attribute returns initial values for NI-Digital Pattern Driver attributes as a string.

#### Syntax

NIDIGITAL_ATTR_DRIVER_SETUP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050007 | ViString | Read-Only | N/A |

Parent topic:

Advanced Session Information

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities.html language=enus -->
## TOPIC 00019: Driver Capabilities

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDIGITAL_ATTR_CHANNEL_COUNTReturns the number of channels that the specific digital pattern instrument driver supports. NIDIGITAL_ATTR_GROUP_CAPABILITIESReturns a string that contains a comma-separated list of class-extension groups that the driver implements.

### Driver Capabilities

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDIGITAL_ATTR_CHANNEL_COUNT | Returns the number of channels that the specific digital pattern instrument driver supports. |
| NIDIGITAL_ATTR_GROUP_CAPABILITIES | Returns a string that contains a comma-separated list of class-extension groups that the driver implements. |
| NIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELS | Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver. |

#### Attachments

None

Parent topic:

Inherent IVI Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities_1ga5e47ece9386ac82850c73abc47f88666.html language=enus -->
## TOPIC 00020: NIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELS

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities_1ga5e47ece9386ac82850c73abc47f88666.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities_1ga5e47ece9386ac82850c73abc47f88666.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver. SyntaxNIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELSNumeric ValueData TypeAccessApplies To1050327ViStringRead-OnlyN/A

### NIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELS

Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver.

#### Syntax

NIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050327 | ViString | Read-Only | N/A |

Parent topic:

Driver Capabilities

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities_1gab6dda6ab7ba671cc60c4d420fbdc559b.html language=enus -->
## TOPIC 00021: NIDIGITAL_ATTR_CHANNEL_COUNT

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities_1gab6dda6ab7ba671cc60c4d420fbdc559b.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__driver__capabilities_1gab6dda6ab7ba671cc60c4d420fbdc559b.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of channels that the specific digital pattern instrument driver supports. SyntaxNIDIGITAL_ATTR_CHANNEL_COUNTNumeric ValueData TypeAccessApplies To1050203ViInt32Read-OnlyN/A

### NIDIGITAL_ATTR_CHANNEL_COUNT

Returns the number of channels that the specific digital pattern instrument driver supports.

#### Syntax

NIDIGITAL_ATTR_CHANNEL_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050203 | ViInt32 | Read-Only | N/A |

Parent topic:

Driver Capabilities

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__driver__identification_1gaaa1347146e4e7ecb6d83007ba79fc03b.html language=enus -->
## TOPIC 00022: NIDIGITAL_ATTR_SPECIFIC_DRIVER_PREFIX

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__driver__identification_1gaaa1347146e4e7ecb6d83007ba79fc03b.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__driver__identification_1gaaa1347146e4e7ecb6d83007ba79fc03b.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the prefix for the NI-Digital Pattern driver. SyntaxNIDIGITAL_ATTR_SPECIFIC_DRIVER_PREFIXNumeric ValueData TypeAccessApplies To1050302ViStringRead-OnlyN/A

### NIDIGITAL_ATTR_SPECIFIC_DRIVER_PREFIX

Returns a string that contains the prefix for the NI-Digital Pattern driver.

#### Syntax

NIDIGITAL_ATTR_SPECIFIC_DRIVER_PREFIX

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050302 | ViString | Read-Only | N/A |

Parent topic:

Driver Identification

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__instrument__identification_1ga129838745cf8e02d22d3379ea0315a9b.html language=enus -->
## TOPIC 00023: NIDIGITAL_ATTR_INSTRUMENT_MODEL

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__instrument__identification_1ga129838745cf8e02d22d3379ea0315a9b.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__instrument__identification_1ga129838745cf8e02d22d3379ea0315a9b.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the model number or name of the digital pattern instrument. SyntaxNIDIGITAL_ATTR_INSTRUMENT_MODELNumeric ValueData TypeAccessApplies To1050512ViStringRead-OnlyN/A

### NIDIGITAL_ATTR_INSTRUMENT_MODEL

Returns a string that contains the model number or name of the digital pattern instrument.

#### Syntax

NIDIGITAL_ATTR_INSTRUMENT_MODEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050512 | ViString | Read-Only | N/A |

Parent topic:

Instrument Identification

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__instrument__identification_1gac59151c9d1528f75d846d2dafff3d46f.html language=enus -->
## TOPIC 00024: NIDIGITAL_ATTR_INSTRUMENT_FIRMWARE_REVISION

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__instrument__identification_1gac59151c9d1528f75d846d2dafff3d46f.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__instrument__identification_1gac59151c9d1528f75d846d2dafff3d46f.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the firmware revision information for the digital pattern instrument. SyntaxNIDIGITAL_ATTR_INSTRUMENT_FIRMWARE_REVISIONNumeric ValueData TypeAccessApplies To1050510ViStringRead-OnlyInstruments

### NIDIGITAL_ATTR_INSTRUMENT_FIRMWARE_REVISION

Returns a string that contains the firmware revision information for the digital pattern instrument.

#### Syntax

NIDIGITAL_ATTR_INSTRUMENT_FIRMWARE_REVISION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050510 | ViString | Read-Only | Instruments |

Parent topic:

Instrument Identification

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__user__options_1ga93c7e39d8fdbbd1f5f0740a42ed168b9.html language=enus -->
## TOPIC 00025: NIDIGITAL_ATTR_QUERY_INSTRUMENT_STATUS

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__user__options_1ga93c7e39d8fdbbd1f5f0740a42ed168b9.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__user__options_1ga93c7e39d8fdbbd1f5f0740a42ed168b9.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation. SyntaxNIDIGITAL_ATTR_QUERY_INSTRUMENT_STATUSNumeric ValueData TypeAccessApplies To1050003ViBooleanRead/WriteN/ARemarks The instrument status is always queried, regardless of the attrib

### NIDIGITAL_ATTR_QUERY_INSTRUMENT_STATUS

Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation.

#### Syntax

NIDIGITAL_ATTR_QUERY_INSTRUMENT_STATUS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050003 | ViBoolean | Read/Write | N/A |

#### Remarks

The instrument status is always queried, regardless of the attribute setting.

Parent topic:

User Options

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__inherent__ivi__attributes__user__options_1gadf24eb273f839cba12b2f79e228ae8fd.html language=enus -->
## TOPIC 00026: NIDIGITAL_ATTR_CACHE

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__inherent__ivi__attributes__user__options_1gadf24eb273f839cba12b2f79e228ae8fd.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__inherent__ivi__attributes__user__options_1gadf24eb273f839cba12b2f79e228ae8fd.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to cache the value of attributes. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. This significantly increases execution speed. Caching is always enabled in the driver, regardless

### NIDIGITAL_ATTR_CACHE

Specifies whether to cache the value of attributes. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. This significantly increases execution speed. Caching is always enabled in the driver, regardless of the value of this attribute.

#### Syntax

NIDIGITAL_ATTR_CACHE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1050004 | ViBoolean | Read/Write | N/A |

#### Remarks

**Related reference**

[niDigital_BurstPatternSynchronized](group____root__ni_digital__functions__pattern__action_1gadec831e054a2c74721253a679c06e6ca.html)

Parent topic:

User Options

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__level__configuration_1ga5802564677a916ff7eb82de4e9ba9fcc.html language=enus -->
## TOPIC 00027: NIDIGITAL_ATTR_ACTIVE_LOAD_IOH

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__level__configuration_1ga5802564677a916ff7eb82de4e9ba9fcc.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__level__configuration_1ga5802564677a916ff7eb82de4e9ba9fcc.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current that the DUT sources to the active load while outputting a voltage above VCOM. SyntaxNIDIGITAL_ATTR_ACTIVE_LOAD_IOHNumeric ValueData TypeAccessApplies To1150013ViReal64Read/WriteChannels, PinsRemarksHigh-Level Functions:niDigital_ConfigureActiveLoadLevels

### NIDIGITAL_ATTR_ACTIVE_LOAD_IOH

Specifies the current that the DUT sources to the active load while outputting a voltage above VCOM.

#### Syntax

NIDIGITAL_ATTR_ACTIVE_LOAD_IOH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150013 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

**High-Level Functions**:

- [niDigital_ConfigureActiveLoadLevels](group____root__ni_digital__functions__levels__and__timing_1ga6a267e2b042a357835012950b678db9c.html)

Parent topic:

Level Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__level__configuration_1ga77b5f40b91d5041a7aa0ea9d6b8a5dc7.html language=enus -->
## TOPIC 00028: NIDIGITAL_ATTR_VIH

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__level__configuration_1ga77b5f40b91d5041a7aa0ea9d6b8a5dc7.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__level__configuration_1ga77b5f40b91d5041a7aa0ea9d6b8a5dc7.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1). SyntaxNIDIGITAL_ATTR_VIHNumeric ValueData TypeAccessApplies To1150008ViReal64Read/WriteChannels, PinsRemarksHigh-Level Functions:niDigital_ConfigureVoltageLe

### NIDIGITAL_ATTR_VIH

Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

#### Syntax

NIDIGITAL_ATTR_VIH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150008 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

**High-Level Functions**:

- [niDigital_ConfigureVoltageLevels](group____root__ni_digital__functions__levels__and__timing_1gafd9996bb5bd233842ffa22b8e30e32dc.html)

Parent topic:

Level Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu.html language=enus -->
## TOPIC 00029: PPMU

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDIGITAL_ATTR_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGEEnables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to VI_TRUE, this attribute enables extended voltage range operation. Review s

### PPMU

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDIGITAL_ATTR_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE | Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to VI_TRUE, this attribute enables extended voltage range operation. Review specification deviations for application suitability before using this attribute. NI recommends setting this attribute to VI_FALSE when not using the extended voltage range to avoid unintentional use of this range. |
| NIDIGITAL_ATTR_PPMU_APERTURE_TIME | Specifies the measurement aperture time for the PPMU. |
| NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS | Specifies the units of the measurement aperture time for the PPMU. |
| NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL | Specifies the current level, in amps, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current. |
| NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL_RANGE | Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current. |
| NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT | Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage. The PXIe-6570/6571 does not support the NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT attribute and only allows configuration of the NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE attribute. |
| NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR | Specifies how the output should behave when the current limit is reached. |
| NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE | Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage. |
| NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_SUPPORTED | Returns whether the device supports configuration of a current limit when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage. |
| NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION | Specifies whether the PPMU forces voltage or current to the DUT. |
| NIDIGITAL_ATTR_PPMU_VOLTAGE_LEVEL | Specifies the voltage level, in volts, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage. |
| NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGH | Specifies the maximum voltage limit, or high clamp voltage (VCH ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current. |
| NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOW | Specifies the minimum voltage limit, or low clamp voltage (VCL ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu_1ga00e28802461473468c649213329f52fd.html language=enus -->
## TOPIC 00030: NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu_1ga00e28802461473468c649213329f52fd.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu_1ga00e28802461473468c649213329f52fd.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of the measurement aperture time for the PPMU. SyntaxNIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITSNumeric ValueData TypeAccessApplies To1150038ViInt32Read/WriteChannels, PinsRemarksDefined Values:NameValueDescriptionNIDIGITAL_VAL_SECONDS2100 (0x834)Specifies the aperture time in second

### NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS

Specifies the units of the measurement aperture time for the PPMU.

#### Syntax

NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150038 | ViInt32 | Read/Write | Channels, Pins |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDIGITAL_VAL_SECONDS | 2100 (0x834) | Specifies the aperture time in seconds. |

**Related reference**

[NIDIGITAL_ATTR_PPMU_APERTURE_TIME](group____root__ni_digital__attributes__ppmu_1gab5332330016ff0c1ab59e1b0a5e6291c.html)

**High-Level Functions**:

- [niDigital_PPMU_ConfigureApertureTime](group____root__ni_digital__functions__ppmu__configuration_1gaa343f96f9dc83a4bae59d5ac1b07d393.html)

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu_1ga43e8c43d820cbd80ccef5e5c4c372467.html language=enus -->
## TOPIC 00031: NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu_1ga43e8c43d820cbd80ccef5e5c4c372467.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu_1ga43e8c43d820cbd80ccef5e5c4c372467.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the output should behave when the current limit is reached. SyntaxNIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIORNumeric ValueData TypeAccessApplies To1150064ViInt32Read/WriteChannels, PinsRemarksDefined Values:NameValueDescriptionNIDIGITAL_VAL_CURRENT_REGULATE3100 (0xc1c)Controls output cu

### NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR

Specifies how the output should behave when the current limit is reached.

#### Syntax

NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150064 | ViInt32 | Read/Write | Channels, Pins |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDIGITAL_VAL_CURRENT_REGULATE | 3100 (0xc1c) | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |

**High-Level Functions**:

- [niDigital_PPMU_ConfigureCurrentLimit](group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga007276bb58783032610844d6430769d0.html)

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu_1ga8415a88eacebb5faf5b5006ab217a93f.html language=enus -->
## TOPIC 00032: NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOW

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu_1ga8415a88eacebb5faf5b5006ab217a93f.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu_1ga8415a88eacebb5faf5b5006ab217a93f.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum voltage limit, or low clamp voltage (V[CL] ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current. SyntaxNIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOWNumeric ValueDa

### NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOW

Specifies the minimum voltage limit, or low clamp voltage (V<sub>CL</sub> ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the [NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION](group____root__ni_digital__attributes__ppmu_1gaa7ea1af7c7da59c44b50d446d30a94b1.html) attribute to DC Current.

#### Syntax

NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150021 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

**Related reference**

[NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL](group____root__ni_digital__attributes__ppmu_1ga3fbc583a241430ac454a958c3de349ad.html)

**High-Level Functions**:

- [niDigital_PPMU_ConfigureVoltageLimits](group____root__ni_digital__functions__ppmu__configuration__dc__current_1ga2d195368a0962a5da5e614a9a56ed1a3.html)

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu_1gaa7ea1af7c7da59c44b50d446d30a94b1.html language=enus -->
## TOPIC 00033: NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu_1gaa7ea1af7c7da59c44b50d446d30a94b1.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu_1gaa7ea1af7c7da59c44b50d446d30a94b1.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the PPMU forces voltage or current to the DUT. SyntaxNIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTIONNumeric ValueData TypeAccessApplies To1150015ViInt32Read/WriteChannels, PinsRemarksDefined Values:NameValueDescriptionNIDIGITAL_VAL_DC_VOLTAGE1300 (0x514)Specifies the output function to DC Volt

### NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION

Specifies whether the PPMU forces voltage or current to the DUT.

#### Syntax

NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150015 | ViInt32 | Read/Write | Channels, Pins |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDIGITAL_VAL_DC_VOLTAGE | 1300 (0x514) | Specifies the output function to DC Voltage. |
| NIDIGITAL_VAL_DC_CURRENT | 1301 (0x515) | Specifies the output function to DC Current. |

**High-Level Functions**:

- [niDigital_PPMU_ConfigureOutputFunction](group____root__ni_digital__functions__ppmu__configuration_1ga9bbbaabd50b857dc9aa21c90853711aa.html)

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu_1gab5332330016ff0c1ab59e1b0a5e6291c.html language=enus -->
## TOPIC 00034: NIDIGITAL_ATTR_PPMU_APERTURE_TIME

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu_1gab5332330016ff0c1ab59e1b0a5e6291c.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu_1gab5332330016ff0c1ab59e1b0a5e6291c.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement aperture time for the PPMU. SyntaxNIDIGITAL_ATTR_PPMU_APERTURE_TIMENumeric ValueData TypeAccessApplies To1150037ViReal64Read/WriteChannels, PinsRemarks The NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS attribute sets the units of the PPMU aperture time.Related referenceNIDIGITAL_

### NIDIGITAL_ATTR_PPMU_APERTURE_TIME

Specifies the measurement aperture time for the PPMU.

#### Syntax

NIDIGITAL_ATTR_PPMU_APERTURE_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150037 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

The [NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS](group____root__ni_digital__attributes__ppmu_1ga00e28802461473468c649213329f52fd.html) attribute sets the units of the PPMU aperture time.

**Related reference**

[NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS](group____root__ni_digital__attributes__ppmu_1ga00e28802461473468c649213329f52fd.html)

**High-Level Functions**:

- [niDigital_PPMU_ConfigureApertureTime](group____root__ni_digital__functions__ppmu__configuration_1gaa343f96f9dc83a4bae59d5ac1b07d393.html)

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu_1gad09000548a344464a16984f7b6dac7f6.html language=enus -->
## TOPIC 00035: NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu_1gad09000548a344464a16984f7b6dac7f6.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu_1gad09000548a344464a16984f7b6dac7f6.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage. The PXIe-6570/6571 does not support the NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT attr

### NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT

Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This attribute is applicable only when you set the [NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION](group____root__ni_digital__attributes__ppmu_1gaa7ea1af7c7da59c44b50d446d30a94b1.html) attribute to DC Voltage. The PXIe-6570/6571 does not support the [NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT](group____root__ni_digital__attributes__ppmu_1gad09000548a344464a16984f7b6dac7f6.html) attribute and only allows configuration of the [NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE](group____root__ni_digital__attributes__ppmu_1gae2a0d08b7fa0dc8be19c4ff8365ff8d5.html) attribute.

#### Syntax

NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150054 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

**High-Level Functions**:

- [niDigital_PPMU_ConfigureCurrentLimit](group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga007276bb58783032610844d6430769d0.html)

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu_1gae042182cdf44954334874698a5a70862.html language=enus -->
## TOPIC 00036: NIDIGITAL_ATTR_PPMU_VOLTAGE_LEVEL

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu_1gae042182cdf44954334874698a5a70862.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu_1gae042182cdf44954334874698a5a70862.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level, in volts, that the PPMU forces to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Voltage. SyntaxNIDIGITAL_ATTR_PPMU_VOLTAGE_LEVELNumeric ValueData TypeAccessApplies To1150016ViReal64Read/WriteChannels, Pins

### NIDIGITAL_ATTR_PPMU_VOLTAGE_LEVEL

Specifies the voltage level, in volts, that the PPMU forces to the DUT. This attribute is applicable only when you set the [NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION](group____root__ni_digital__attributes__ppmu_1gaa7ea1af7c7da59c44b50d446d30a94b1.html) attribute to DC Voltage.

#### Syntax

NIDIGITAL_ATTR_PPMU_VOLTAGE_LEVEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150016 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

**Related reference**

[niDigital_PPMU_ConfigureOutputFunction](group____root__ni_digital__functions__ppmu__configuration_1ga9bbbaabd50b857dc9aa21c90853711aa.html)

[niDigital_PPMU_ConfigureCurrentLimitRange](group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga86083163cb6d3329d5eb44f5f56baf1b.html)

**High-Level Functions**:

- [niDigital_PPMU_ConfigureVoltageLevel](group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga76e05e23c36013fdc42c8492633547a6.html)

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__ppmu_1gaf5bf9f9a8d65531b589a57eabbe81957.html language=enus -->
## TOPIC 00037: NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGH

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__ppmu_1gaf5bf9f9a8d65531b589a57eabbe81957.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__ppmu_1gaf5bf9f9a8d65531b589a57eabbe81957.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum voltage limit, or high clamp voltage (V[CH] ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION attribute to DC Current. SyntaxNIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGHNumeric Value

### NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGH

Specifies the maximum voltage limit, or high clamp voltage (V<sub>CH</sub> ), in volts, at the pin when the PPMU forces current to the DUT. This attribute is applicable only when you set the [NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION](group____root__ni_digital__attributes__ppmu_1gaa7ea1af7c7da59c44b50d446d30a94b1.html) attribute to DC Current.

#### Syntax

NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150022 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

**Related reference**

[NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL](group____root__ni_digital__attributes__ppmu_1ga3fbc583a241430ac454a958c3de349ad.html)

**High-Level Functions**:

- [niDigital_PPMU_ConfigureVoltageLimits](group____root__ni_digital__functions__ppmu__configuration__dc__current_1ga2d195368a0962a5da5e614a9a56ed1a3.html)

Parent topic:

PPMU

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__synchronization.html language=enus -->
## TOPIC 00038: Synchronization

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__synchronization.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__synchronization.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDIGITAL_ATTR_PATTERN_OPCODE_EVENT_TERMINAL_NAMESpecifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. NIDIGITAL_ATTR_SEQUENCER_FLAG_TERMINAL_NAMESpecifies the terminal name for the output trigger signal o

### Synchronization

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDIGITAL_ATTR_PATTERN_OPCODE_EVENT_TERMINAL_NAME | Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. |
| NIDIGITAL_ATTR_SEQUENCER_FLAG_TERMINAL_NAME | Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger. |
| NIDIGITAL_ATTR_START_TRIGGER_TERMINAL_NAME | Specifies the terminal name for the output trigger signal of the Start trigger. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__tdr__endpoint__termination_1gab781c0ac668a1752692e5b31ea5ea787.html language=enus -->
## TOPIC 00039: NIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATION

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__tdr__endpoint__termination_1gab781c0ac668a1752692e5b31ea5ea787.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__tdr__endpoint__termination_1gab781c0ac668a1752692e5b31ea5ea787.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether TDR Channels are connected to an open circuit or a short to ground. SyntaxNIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATIONNumeric ValueData TypeAccessApplies To1150081ViInt32Read/WriteN/ARemarksDefined Values:NameValueDescriptionNIDIGITAL_VAL_TDR_TO_OPEN3600 (0xe10)TDR channels are connecte

### NIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATION

Specifies whether TDR Channels are connected to an open circuit or a short to ground.

#### Syntax

NIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150081 | ViInt32 | Read/Write | N/A |

#### Remarks

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDIGITAL_VAL_TDR_TO_OPEN | 3600 (0xe10) | TDR channels are connected to an open circuit. |
| NIDIGITAL_VAL_TDR_TO_SHORT_TO_GROUND | 3601 (0xe11) | TDR channels are connected to a short to ground. |

**High-Level Functions**:

- [niDigital_ApplyTDROffsets](group____root__ni_digital__functions__tdr_1ga58e5f9120d9df3e3507f8b8ab19836f9.html)

Parent topic:

TDR Endpoint Termination

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__timing__offset.html language=enus -->
## TOPIC 00040: Timing Offset

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__timing__offset.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__timing__offset.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionNIDIGITAL_ATTR_TDR_OFFSETSpecifies the TDR Offset. NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAYSpecifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. NIDIGITAL_ATTR_TIMING_AB

### Timing Offset

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| NIDIGITAL_ATTR_TDR_OFFSET | Specifies the TDR Offset. |
| NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY | Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. |
| NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED | Specifies whether the TIMING_ABSOLUTE_DELAY attribute should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__timing__offset_1gac7b351f7b3579c53da84899f883ce162.html language=enus -->
## TOPIC 00041: NIDIGITAL_ATTR_TDR_OFFSET

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__timing__offset_1gac7b351f7b3579c53da84899f883ce162.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__timing__offset_1gac7b351f7b3579c53da84899f883ce162.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the TDR Offset. SyntaxNIDIGITAL_ATTR_TDR_OFFSETNumeric ValueData TypeAccessApplies To1150051ViReal64Read/WriteChannels, PinsRemarksHigh-Level Functions:niDigital_ApplyTDROffsets

### NIDIGITAL_ATTR_TDR_OFFSET

Specifies the TDR Offset.

#### Syntax

NIDIGITAL_ATTR_TDR_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150051 | ViReal64 | Read/Write | Channels, Pins |

#### Remarks

**High-Level Functions**:

- [niDigital_ApplyTDROffsets](group____root__ni_digital__functions__tdr_1ga58e5f9120d9df3e3507f8b8ab19836f9.html)

Parent topic:

Timing Offset

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__timing__offset_1gae466c33edf11807e377a0afa3bf5c3ef.html language=enus -->
## TOPIC 00042: NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__timing__offset_1gae466c33edf11807e377a0afa3bf5c3ef.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__timing__offset_1gae466c33edf11807e377a0afa3bf5c3ef.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the TIMING_ABSOLUTE_DELAY attribute should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. SyntaxNIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLEDNumeric ValueData TypeAccessApplies To1150071ViBooleanRead/WriteN/ARemarks

### NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED

Specifies whether the TIMING_ABSOLUTE_DELAY attribute should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system.

#### Syntax

NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150071 | ViBoolean | Read/Write | N/A |

#### Remarks

Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts with the adjustment performed during STS timing calibration.

When set to VI_TRUE, the digital pattern instrument automatically adjusts the timing absolute delay to correct the instrument timing reference relative to other instruments in the system for better timing alignment among synchronized instruments.

Parent topic:

Timing Offset

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__trigger__configuration_1ga5726f74a562e2c79f8fdb8ac17eb100e.html language=enus -->
## TOPIC 00043: NIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_SOURCE

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__trigger__configuration_1ga5726f74a562e2c79f8fdb8ac17eb100e.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__trigger__configuration_1ga5726f74a562e2c79f8fdb8ac17eb100e.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the digital trigger source terminal for a RIO trigger instance. SyntaxNIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_SOURCENumeric ValueData TypeAccessApplies To1150087ViStringRead/WriteRIO TriggersRemarks You can specify source terminals in one of two ways. If the digital pattern instrument is

### NIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_SOURCE

Configures the digital trigger source terminal for a RIO trigger instance.

#### Syntax

NIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_SOURCE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150087 | ViString | Read/Write | RIO Triggers |

#### Remarks

You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line).

| Valid Values: |
| --- |
| String identifier to any valid terminal name |

| Default Value: |  |
| --- | --- |
| VI_NULL ("") | Returns an empty string. |

**High-Level Functions**:

- [niDigital_ConfigureDigitalEdgeRIOTrigger](group____root__ni_digital__functions__triggers__and__events_1ga587804d11344bd7780372f2970ad098a.html)

Parent topic:

Trigger Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__trigger__configuration_1ga5c4635b1ef8ea436136202f15da2d8ed.html language=enus -->
## TOPIC 00044: NIDIGITAL_ATTR_START_TRIGGER_TYPE

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__trigger__configuration_1ga5c4635b1ef8ea436136202f15da2d8ed.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__trigger__configuration_1ga5c4635b1ef8ea436136202f15da2d8ed.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Start trigger type. SyntaxNIDIGITAL_ATTR_START_TRIGGER_TYPENumeric ValueData TypeAccessApplies To1150029ViInt32Read/WriteN/ARemarks The digital pattern instrument waits for this trigger after you call the niDigital_init function or the niDigital_BurstPattern function, and does not burs

### NIDIGITAL_ATTR_START_TRIGGER_TYPE

Specifies the Start trigger type.

#### Syntax

NIDIGITAL_ATTR_START_TRIGGER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150029 | ViInt32 | Read/Write | N/A |

#### Remarks

The digital pattern instrument waits for this trigger after you call the [niDigital_init](group____root__ni_digital__functions__init__and__close_1gaaf7538e74e33f67b44ba2d9eb917ae14.html) function or the [niDigital_BurstPattern](group____root__ni_digital__functions__pattern__action_1ga0e9a6597044b41afae031dcd59e32330.html) function, and does not burst a pattern until this trigger is received.

**Defined Values:**

| Name | Value | Description |
| --- | --- | --- |
| NIDIGITAL_VAL_NONE | 1700 (0x6a4) | Disables the Start trigger. Pattern bursting starts immediately after you call the niDigital_init function or the niDigital_BurstPattern function. |
| NIDIGITAL_VAL_DIGITAL_EDGE | 1701 (0x6a5) | Pattern bursting does not start until the digital pattern instrument detects a digital edge. |
| NIDIGITAL_VAL_SOFTWARE | 1702 (0x6a6) | Pattern bursting does not start until the digital pattern instrument receives a software Start trigger. Create a software Start trigger by calling the niDigital_SendSoftwareEdgeTrigger function and selecting start trigger in the trigger parameter.Related information: SendSoftwareEdgeTrigger function. |

**Related reference**

[niDigital_BurstPattern](group____root__ni_digital__functions__pattern__action_1ga0e9a6597044b41afae031dcd59e32330.html)

[niDigital_Initiate](group____root__ni_digital__functions__pattern__action__low__level__action_1ga992e80f747168211cd44d3ca09309f6f.html)

[niDigital_SendSoftwareEdgeTrigger](group____root__ni_digital__functions__triggers__and__events_1gabc755885dd1fdedc6389af5af9341b9f.html)

**High-Level Functions**:

- [niDigital_ConfigureDigitalEdgeStartTrigger](group____root__ni_digital__functions__triggers__and__events_1gadbd322b670febe92e050399487ccb274.html)
- [niDigital_ConfigureSoftwareEdgeStartTrigger](group____root__ni_digital__functions__triggers__and__events_1ga40f3defc50a0536eb6b3a856a36b36e8.html)
- [niDigital_DisableStartTrigger](group____root__ni_digital__functions__triggers__and__events_1ga144ef5d79c425f5f9635206551bf7720.html)

Parent topic:

Trigger Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__attributes__trigger__configuration_1ga61d7e67b3dcd7c0c65c23e00c3ba92fe.html language=enus -->
## TOPIC 00045: NIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_EDGE

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__attributes__trigger__configuration_1ga61d7e67b3dcd7c0c65c23e00c3ba92fe.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__attributes__trigger__configuration_1ga61d7e67b3dcd7c0c65c23e00c3ba92fe.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the active edge of the incoming trigger signal for the RIO trigger instance. SyntaxNIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_EDGENumeric ValueData TypeAccessApplies To1150088ViInt32Read/WriteRIO TriggersRemarksValid Values:NIDIGITAL_VAL_RISING_EDGE (1800)Specifies the signal transition from

### NIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_EDGE

Configures the active edge of the incoming trigger signal for the RIO trigger instance.

#### Syntax

NIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_EDGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1150088 | ViInt32 | Read/Write | RIO Triggers |

#### Remarks

| Valid Values: |  |
| --- | --- |
| NIDIGITAL_VAL_RISING_EDGE (1800) | Specifies the signal transition from low level to high level. |
| NIDIGITAL_VAL_FALLING_EDGE (1801) | Specifies the signal transition from high level to low level. |

| Default Value: |
| --- |
| NIDIGITAL_VAL_RISING_EDGE (1800) |

**High-Level Functions**:

- [niDigital_ConfigureDigitalEdgeRIOTrigger](group____root__ni_digital__functions__triggers__and__events_1ga587804d11344bd7780372f2970ad098a.html)

Parent topic:

Trigger Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__attributes_1ga68ce39023a29864f266c92f9d0aad07f.html language=enus -->
## TOPIC 00046: niDigital_SetAttributeViBoolean

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__attributes_1ga68ce39023a29864f266c92f9d0aad07f.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__attributes_1ga68ce39023a29864f266c92f9d0aad07f.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViBoolean attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes. SyntaxViStatus _VI_FUNC niDigital_SetAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attribute, ViBoolean value)ParametersNam

### niDigital_SetAttributeViBoolean

Sets the value of a ViBoolean attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.

#### Syntax

ViStatus _VI_FUNC niDigital_SetAttributeViBoolean(ViSession vi, ViConstString channelName, ViAttr attribute, ViBoolean value)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelName | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| attribute | [in] | ViAttr | The ID of an attribute. |
| value | [in] | ViBoolean | The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session. |

#### Returns

Reports the status of the operation.

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__attributes_1gac3532ba2197c8ab17239e90c6578bf11.html language=enus -->
## TOPIC 00047: niDigital_SetAttributeViInt64

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__attributes_1gac3532ba2197c8ab17239e90c6578bf11.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__attributes_1gac3532ba2197c8ab17239e90c6578bf11.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViInt64 attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes. SyntaxViStatus _VI_FUNC niDigital_SetAttributeViInt64(ViSession vi, ViConstString channelName, ViAttr attribute, ViInt64 value)ParametersNameDirec

### niDigital_SetAttributeViInt64

Sets the value of a ViInt64 attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.

#### Syntax

ViStatus _VI_FUNC niDigital_SetAttributeViInt64(ViSession vi, ViConstString channelName, ViAttr attribute, ViInt64 value)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelName | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| attribute | [in] | ViAttr | The ID of an attribute. |
| value | [in] | ViInt64 | The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session. |

#### Returns

Reports the status of the operation.

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__attributes_1gacb4a9fd9908c95b58e96a1bc903aca04.html language=enus -->
## TOPIC 00048: niDigital_SetAttributeViSession

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__attributes_1gacb4a9fd9908c95b58e96a1bc903aca04.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__attributes_1gacb4a9fd9908c95b58e96a1bc903aca04.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a ViSession attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes. SyntaxViStatus _VI_FUNC niDigital_SetAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attribute, ViSession value)ParametersNam

### niDigital_SetAttributeViSession

Sets the value of a ViSession attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.

#### Syntax

ViStatus _VI_FUNC niDigital_SetAttributeViSession(ViSession vi, ViConstString channelName, ViAttr attribute, ViSession value)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelName | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| attribute | [in] | ViAttr | The ID of an attribute. |
| value | [in] | ViSession | The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session. |

#### Returns

Reports the status of the operation.

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__attributes_1gaf9e5a601347a059e816aa0c111ab16bc.html language=enus -->
## TOPIC 00049: niDigital_GetAttributeViString

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__attributes_1gaf9e5a601347a059e816aa0c111ab16bc.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__attributes_1gaf9e5a601347a059e816aa0c111ab16bc.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of a ViString attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes. SyntaxViStatus _VI_FUNC niDigital_GetAttributeViString(ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 bufferSize, ViChar v

### niDigital_GetAttributeViString

Queries the value of a ViString attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.

#### Syntax

ViStatus _VI_FUNC niDigital_GetAttributeViString(ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 bufferSize, ViChar value[])

#### Remarks

You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **bufferSize**. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **bufferSize**, the function copies (**bufferSize** - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the **bufferSize** you must pass to get the entire value. For example, if the value is "123456" and the **bufferSize** is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for the **bufferSize** and VI_NULL for the value.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelName | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| attribute | [in] | ViAttr | The ID of an attribute. |
| bufferSize | [in] | ViInt32 | The number of elements in the ViChar array you specify for value. |
| value | [out] | ViChar[] | The buffer in which the function returns the current value of the attribute; the buffer must be of type ViChar and have at least as many bytes as indicated in the bufferSize. |

#### Returns

Reports the status of the operation.

Parent topic:

Attributes

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__calibration_1gaa59b60f83189e84ffca61d2e0554e22d.html language=enus -->
## TOPIC 00050: niDigital_SelfCalibrate

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__calibration_1gaa59b60f83189e84ffca61d2e0554e22d.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__calibration_1gaa59b60f83189e84ffca61d2e0554e22d.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs self-calibration on a digital pattern instrument. SyntaxViStatus _VI_FUNC niDigital_SelfCalibrate(ViSession vi)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigital_init or niDigital_InitWithOptions function returns. ReturnsReports the status of the opera

### niDigital_SelfCalibrate

Performs self-calibration on a digital pattern instrument.

#### Syntax

ViStatus _VI_FUNC niDigital_SelfCalibrate(ViSession vi)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Calibration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__capture__memory_1ga4efdf2a8c2fb030f242ec6a313807e75.html language=enus -->
## TOPIC 00051: niDigital_FetchCaptureWaveformU32

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__capture__memory_1ga4efdf2a8c2fb030f242ec6a313807e75.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__capture__memory_1ga4efdf2a8c2fb030f242ec6a313807e75.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches a defined number of samples for a specific list of sites. This function only returns data from sites that are enabled when fetch is called. SyntaxViStatus _VI_FUNC niDigital_FetchCaptureWaveformU32(ViSession vi, ViConstString siteList, ViConstString waveformName, ViInt32 samplesToRead, ViRea

### niDigital_FetchCaptureWaveformU32

Fetches a defined number of samples for a specific list of sites. This function only returns data from sites that are enabled when fetch is called.

#### Syntax

ViStatus _VI_FUNC niDigital_FetchCaptureWaveformU32(ViSession vi, ViConstString siteList, ViConstString waveformName, ViInt32 samplesToRead, ViReal64 timeout, ViInt32 dataBufferSize, ViUInt32 data[], ViInt32 *actualNumWaveforms, ViInt32 *actualSamplesPerWaveform)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| siteList | [in] | ViConstString | Site numbers listed as a comma-delimited list of strings of form siteN, where N is the site number. If you enter an empty string, the function fetches data from all sites. |
| waveformName | [in] | ViConstString | Waveform name you create with the create capture waveform function. Use the waveformName parameter with capture_start opcode in your pattern. |
| samplesToRead | [in] | ViInt32 | Number of samples to fetch. |
| timeout | [in] | ViReal64 | Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error. |
| dataBufferSize | [in] | ViInt32 | The number of elements in the ViUInt32 array you specify for data. To determine the size of the buffer to allocate for the data array, pass a value of 0 to the dataBufferSize parameter and a value of VI_NULL to the data parameter. In this case, the value returned by the actualNumWaveforms and actualSamplesPerWaveform parameters determine the size of the array necessary to hold the data. The data buffer size should be the number of samples per waveform multiplied by the number of waveforms. |
| data | [out] | ViUInt32[] | An array of digital states read from the sites in the siteList. Each row in the array corresponds to a site in the list. If a site is disabled, not enabled for burst, or the current instrument does not include any capture pins, the function does not return data for that site. Data for each site in the siteList are returned sequentially (non-interleaved). If you are using a list of pin names to read data from multiple instruments, use the niDigital_SortSiteResultsViUInt32Waveform function to order and combine the data to match the siteList. You can also use the niDigital_GetSiteResultsSiteNumbers function to obtain a list of returned sites. |
| actualNumWaveforms | [out] | ViInt32 * | Number of waveforms written to the data array. |
| actualSamplesPerWaveform | [out] | ViInt32 * | Number of samples per waveform written to the data array. |

#### Returns

Reports the status of the operation.

Parent topic:

Capture Memory

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__capture__memory_1ga911cef6fcaa5c84f084adcfd93892edb.html language=enus -->
## TOPIC 00052: niDigital_CreateCaptureWaveformParallel

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__capture__memory_1ga911cef6fcaa5c84f084adcfd93892edb.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__capture__memory_1ga911cef6fcaa5c84f084adcfd93892edb.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created. SyntaxViStatus _VI_FUNC niDigital_CreateCaptureWaveformParallel(ViSession vi, ViConstString pinLi

### niDigital_CreateCaptureWaveformParallel

Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

#### Syntax

ViStatus _VI_FUNC niDigital_CreateCaptureWaveformParallel(ViSession vi, ViConstString pinList, ViConstString waveformName)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| pinList | [in] | ViConstString | List of capture pins from the waveform. The pinList must match the capture pins in the pattern that references the waveform. The pin order in the pinList determines the bit positions of the data captured by the niDigital_FetchCaptureWaveformU32 function. |
| waveformName | [in] | ViConstString | Waveform name you want to use. Use the waveformName with the capture_start opcode in your pattern. |

#### Returns

Reports the status of the operation.

Parent topic:

Capture Memory

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__conditional__jump__trigger_1ga0cff037936d4d6ba01a468885033816f.html language=enus -->
## TOPIC 00053: niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__conditional__jump__trigger_1ga0cff037936d4d6ba01a468885033816f.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__conditional__jump__trigger_1ga0cff037936d4d6ba01a468885033816f.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the conditional jump trigger instance to trigger on a software function call. To assert the trigger, use the niDigital_SendSoftwareEdgeTrigger function. SyntaxViStatus _VI_FUNC niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger(ViSession vi, ViConstString triggerIdentifier)ParametersNa

### niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger

Configures the conditional jump trigger instance to trigger on a software function call. To assert the trigger, use the [niDigital_SendSoftwareEdgeTrigger](group____root__ni_digital__functions__triggers__and__events_1gabc755885dd1fdedc6389af5af9341b9f.html) function.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigureSoftwareEdgeConditionalJumpTrigger(ViSession vi, ViConstString triggerIdentifier)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| triggerIdentifier | [in] | ViConstString | Specifies which instance of the conditional jump trigger you want to override.Defined Values:NameValueDescriptionNIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER0"conditionalJumpTrigger0"conditionalJumpTrigger0NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER1"conditionalJumpTrigger1"conditionalJumpTrigger1NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2"conditionalJumpTrigger2"conditionalJumpTrigger2NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER3"conditionalJumpTrigger3"conditionalJumpTrigger3 |
| Name | Value | Description |  |
| NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER0 | "conditionalJumpTrigger0" | conditionalJumpTrigger0 |  |
| NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER1 | "conditionalJumpTrigger1" | conditionalJumpTrigger1 |  |
| NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2 | "conditionalJumpTrigger2" | conditionalJumpTrigger2 |  |
| NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER3 | "conditionalJumpTrigger3" | conditionalJumpTrigger3 |  |

#### Returns

Reports the status of the operation.

Parent topic:

Conditional Jump Trigger

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__error__handling_1ga4e55e6d0d92dbc631f1e906a8873fa73.html language=enus -->
## TOPIC 00054: niDigital_GetError

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__error__handling_1ga4e55e6d0d92dbc631f1e906a8873fa73.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__error__handling_1ga4e55e6d0d92dbc631f1e906a8873fa73.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the error information associated with the digital pattern instrument handle. This function retrieves and then clears the error information for the session. If vi is VI_NULL, this function retrieves and then clears the error information for the current thread. SyntaxViStatus _VI_FUNC niDigita

### niDigital_GetError

Returns the error information associated with the digital pattern instrument handle. This function retrieves and then clears the error information for the session. If **vi** is VI_NULL, this function retrieves and then clears the error information for the current thread.

#### Syntax

ViStatus _VI_FUNC niDigital_GetError(ViSession vi, ViStatus *errorCode, ViInt32 errorDescriptionBufferSize, ViChar errorDescription[])

#### Remarks

You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the buffer size. If the current value of the error description, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the function copies (buffer size -1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for the buffer size and VI_NULL for **errorDescription**.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| errorCode | [out] | ViStatus * | The returned error code for the session or execution thread. |
| errorDescriptionBufferSize | [in] | ViInt32 | The number of elements in the ViChar array you specify for errorDescription. |
| errorDescription | [out] | ViChar[] | The returned error description for the IVI session or execution thread. If there is no description, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the buffer size parameter. If you pass 0 for errorDescriptionBufferSize, you can pass VI_NULL for this parameter. |

#### Returns

Reports the status of the operation. If the buffer size is 0 or too small for the error description, the buffer size needed for the full description is returned.

Parent topic:

Error Handling

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__error__handling_1ga54feafefeff7d21ec7831a77c0dfc4f1.html language=enus -->
## TOPIC 00055: niDigital_ClearError

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__error__handling_1ga54feafefeff7d21ec7831a77c0dfc4f1.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__error__handling_1ga54feafefeff7d21ec7831a77c0dfc4f1.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the error information for the current execution thread and the IVI session you specify. If you pass VI_NULL for the vi parameter, this function clears the error information only for the current execution thread. SyntaxViStatus _VI_FUNC niDigital_ClearError(ViSession vi)ParametersNameDirection

### niDigital_ClearError

Clears the error information for the current execution thread and the IVI session you specify. If you pass VI_NULL for the **vi** parameter, this function clears the error information only for the current execution thread.

#### Syntax

ViStatus _VI_FUNC niDigital_ClearError(ViSession vi)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Error Handling

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__frequency__measurement_1ga98d0aec5fe820e67cc77392e4f868062.html language=enus -->
## TOPIC 00056: niDigital_FrequencyCounter_ConfigureMeasurementMode

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__frequency__measurement_1ga98d0aec5fe820e67cc77392e4f868062.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__frequency__measurement_1ga98d0aec5fe820e67cc77392e4f868062.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines how the frequency counters of a digital pattern instrument make measurements. SyntaxViStatus _VI_FUNC niDigital_FrequencyCounter_ConfigureMeasurementMode(ViSession vi, ViInt32 measurementMode)RemarksThe NI-Digital Pattern Driver includes the following frequency counter measurement modes:B

### niDigital_FrequencyCounter_ConfigureMeasurementMode

Determines how the frequency counters of a digital pattern instrument make measurements.

#### Syntax

ViStatus _VI_FUNC niDigital_FrequencyCounter_ConfigureMeasurementMode(ViSession vi, ViInt32 measurementMode)

#### Remarks

The NI-Digital Pattern Driver includes the following frequency counter measurement modes:

- **Banked** mode: each discrete frequency counter is mapped to specific channels and makes frequency measurements from only those channels. Use banked mode when you need access to the full measure frequency range of the instrument.
- **Parallel** mode: all discrete frequency counters make frequency measurements from all channels in parallel with one another. Use parallel mode to increase the speed of frequency measurements if you do not need access to the full measure frequency range of the instrument; in parallel mode, you can also add hysteresis to reduce measurement noise.

Note

For banked mode, if you request frequency measurements from multiple channels within the same bank, the measurements are made in series for the channels in that bank.

**Related Information**

- [NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED](group____root__ni_digital__attributes__frequency__measurement_1gaacba6c11223adea9bfc5cad1b289e141.html)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| measurementMode | [in] | ViInt32 | Measurement mode specifies how the frequency counters make measurements.Defined Values:NameValueDescriptionNIDIGITAL_VAL_BANKED3700 (0xe74)Frequency measurements are made serially for groups of channels associated with a single frequency counter for each group. Maximum frequency measured: 200 MHz.NIDIGITAL_VAL_PARALLEL3701 (0xe75)Frequency measurements are made by multiple frequency counters in parallel. Maximum frequency measured: 100 MHz. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_BANKED | 3700 (0xe74) | Frequency measurements are made serially for groups of channels associated with a single frequency counter for each group. Maximum frequency measured: 200 MHz. |  |
| NIDIGITAL_VAL_PARALLEL | 3701 (0xe75) | Frequency measurements are made by multiple frequency counters in parallel. Maximum frequency measured: 100 MHz. |  |

#### Returns

Reports the status of the operation.

Parent topic:

Frequency Measurement

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__history__ram_1ga477596ee419feb6da986e292fda04976.html language=enus -->
## TOPIC 00057: niDigital_ConfigureFirstFailureHistoryRAMTrigger

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__history__ram_1ga477596ee419feb6da986e292fda04976.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__history__ram_1ga477596ee419feb6da986e292fda04976.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures History RAM to acquire pattern information starting from the first failed cycle encountered. Depending on the cycles History RAM is configured to acquire, samples may include passing and failing cycles. SyntaxViStatus _VI_FUNC niDigital_ConfigureFirstFailureHistoryRAMTrigger(ViSession vi,

### niDigital_ConfigureFirstFailureHistoryRAMTrigger

Configures History RAM to acquire pattern information starting from the first failed cycle encountered. Depending on the cycles History RAM is configured to acquire, samples may include passing and failing cycles.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigureFirstFailureHistoryRAMTrigger(ViSession vi, ViInt32 pretriggerSamples)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| pretriggerSamples | [in] | ViInt32 | The number of samples to acquire before the trigger conditions are met. The digital pattern instrument may capture up to 15 pretrigger samples. |

#### Returns

Reports the status of the operation.

Parent topic:

History RAM

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__history__ram_1ga6bf7d50027ee90ed03518e242411607c.html language=enus -->
## TOPIC 00058: niDigital_ConfigureHistoryRAMCyclesToAcquire

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__history__ram_1ga6bf7d50027ee90ed03518e242411607c.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__history__ram_1ga6bf7d50027ee90ed03518e242411607c.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures History RAM to acquire either all cycles or only failed cycles after triggering conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretriggerSamples for History RAM to 0. SyntaxViStatus _VI_FUNC niDigital_ConfigureHistoryRAMCyclesToAcquire(ViS

### niDigital_ConfigureHistoryRAMCyclesToAcquire

Configures History RAM to acquire either all cycles or only failed cycles after triggering conditions are met. If you configure History RAM to only acquire failed cycles, you must set the **pretriggerSamples** for History RAM to 0.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigureHistoryRAMCyclesToAcquire(ViSession vi, ViInt32 cyclesToAcquire)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| cyclesToAcquire | [in] | ViInt32 | Cycles History RAM will acquire after triggering conditions are met.Defined Values:NameValueDescriptionNIDIGITAL_VAL_FAILED_CYCLES2303 (0x8ff)Only acquires cycles that fail a compare after the triggering conditions are met.NIDIGITAL_VAL_ALL_CYCLES2304 (0x900)Acquires all cycles after the triggering conditions are met. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_FAILED_CYCLES | 2303 (0x8ff) | Only acquires cycles that fail a compare after the triggering conditions are met. |  |
| NIDIGITAL_VAL_ALL_CYCLES | 2304 (0x900) | Acquires all cycles after the triggering conditions are met. |  |

#### Returns

Reports the status of the operation.

Parent topic:

History RAM

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__init__and__close.html language=enus -->
## TOPIC 00059: Init and Close

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__init__and__close.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__init__and__close.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_InitWithOptionsCreates and returns a new session to the specified digital pattern instrument to use in all subsequent function calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to VI_TRUE, whic

### Init and Close

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_InitWithOptions | Creates and returns a new session to the specified digital pattern instrument to use in all subsequent function calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to VI_TRUE, which is equivalent to calling the niDigital_reset function immediately after initializing the session. |
| niDigital_close | Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state. |
| niDigital_init | Creates and returns a new session to the specified digital pattern instrument to use in all subsequent function calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to VI_TRUE, which is equivalent to calling the niDigital_reset function immediately after initializing the session. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__levels__and__timing_1ga5d805c67256c552cb0898002a43b274b.html language=enus -->
## TOPIC 00060: niDigital_ConfigureTimeSetDriveEdges2x

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__levels__and__timing_1ga5d805c67256c552cb0898002a43b274b.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__levels__and__timing_1ga5d805c67256c552cb0898002a43b274b.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive edges of the pins in the time set, including 2x edges. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not mod

### niDigital_ConfigureTimeSetDriveEdges2x

Configures the drive edges of the pins in the time set, including 2x edges. Use this function to modify time set values after applying a timing sheet with the [niDigital_ApplyLevelsAndTiming](group____root__ni_digital__functions__levels__and__timing_1ga2d08e97007c4f46ad280d74b2b246e6d.html) function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to [niDigital_ApplyLevelsAndTiming](group____root__ni_digital__functions__levels__and__timing_1ga2d08e97007c4f46ad280d74b2b246e6d.html); it only affects the values of the current timing context.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigureTimeSetDriveEdges2x(ViSession vi, ViConstString pinList, ViConstString timeSet, ViInt32 format, ViReal64 driveOnEdge, ViReal64 driveDataEdge, ViReal64 driveReturnEdge, ViReal64 driveOffEdge, ViReal64 driveData2Edge, ViReal64 driveReturn2Edge)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| pinList | [in] | ViConstString | List of pin and pin group names for which to configure the time set edges. |
| timeSet | [in] | ViConstString | The specified time set name. |
| format | [in] | ViInt32 | Drive format of the time set.Defined Values:NameValueDescriptionNIDIGITAL_VAL_NR1500 (0x5dc)Non-return: Drive format remains at logic level after each bit.NIDIGITAL_VAL_RL1501 (0x5dd)Return to low: Drive format returns to a logic level low after each bit.NIDIGITAL_VAL_RH1502 (0x5de)Return to high: Drive format returns to a logic level high after each bit.NIDIGITAL_VAL_SBC1503 (0x5df)Surround by complement: Drive format returns to the complement logic level of the bit after each bit. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_NR | 1500 (0x5dc) | Non-return: Drive format remains at logic level after each bit. |  |
| NIDIGITAL_VAL_RL | 1501 (0x5dd) | Return to low: Drive format returns to a logic level low after each bit. |  |
| NIDIGITAL_VAL_RH | 1502 (0x5de) | Return to high: Drive format returns to a logic level high after each bit. |  |
| NIDIGITAL_VAL_SBC | 1503 (0x5df) | Surround by complement: Drive format returns to the complement logic level of the bit after each bit. |  |
| driveOnEdge | [in] | ViReal64 | Delay, in seconds, from the beginning of the vector period for turning on the pin driver. This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven. |
| driveDataEdge | [in] | ViReal64 | Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value. The ending state from the previous vector persists until this point. |
| driveReturnEdge | [in] | ViReal64 | Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format. |
| driveOffEdge | [in] | ViReal64 | Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E). |
| driveData2Edge | [in] | ViReal64 | Delay, in seconds, from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value. |
| driveReturn2Edge | [in] | ViReal64 | Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format. |

#### Returns

Reports the status of the operation.

Parent topic:

Levels and Timing

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__levels__and__timing_1ga63ece04823f2837b5101e9218a581b94.html language=enus -->
## TOPIC 00061: niDigital_DeleteAllTimeSets

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__levels__and__timing_1ga63ece04823f2837b5101e9218a581b94.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__levels__and__timing_1ga63ece04823f2837b5101e9218a581b94.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all time sets from instrument memory. SyntaxViStatus _VI_FUNC niDigital_DeleteAllTimeSets(ViSession vi)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigital_init or niDigital_InitWithOptions function returns. ReturnsReports the status of the operation.

### niDigital_DeleteAllTimeSets

Deletes all time sets from instrument memory.

#### Syntax

ViStatus _VI_FUNC niDigital_DeleteAllTimeSets(ViSession vi)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Levels and Timing

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__levels__and__timing__low__level.html language=enus -->
## TOPIC 00062: Low Level

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__levels__and__timing__low__level.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__levels__and__timing__low__level.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_ConfigureTimeSetDriveFormatConfigures the drive format for the pins not specified in the pinList. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets program

### Low Level

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_ConfigureTimeSetDriveFormat | Configures the drive format for the pins not specified in the pinList. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context. |
| niDigital_ConfigureTimeSetEdge | Configures the edge placement for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context. |
| niDigital_GetTimeSetDriveFormat | Returns the drive format of a pin in the specified time set. |
| niDigital_GetTimeSetEdge | Returns the edge time of a pin in the specified time set. |
| niDigital_GetTimeSetEdgeMultiplier | Returns the edge multiplier of the specified time set. |
| niDigital_GetTimeSetPeriod | Returns the period of the specified time set. |

#### Attachments

None

Parent topic:

Levels and Timing

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__levels__and__timing__low__level_1ga2bf2eb0eec6fc284f0a2db8b22a795b6.html language=enus -->
## TOPIC 00063: niDigital_GetTimeSetPeriod

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__levels__and__timing__low__level_1ga2bf2eb0eec6fc284f0a2db8b22a795b6.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__levels__and__timing__low__level_1ga2bf2eb0eec6fc284f0a2db8b22a795b6.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the period of the specified time set. SyntaxViStatus _VI_FUNC niDigital_GetTimeSetPeriod(ViSession vi, ViConstString timeSet, ViReal64 *period)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe specified digital pattern instrument handle timeSet[in]ViConstStringThe specified time set n

### niDigital_GetTimeSetPeriod

Returns the period of the specified time set.

#### Syntax

ViStatus _VI_FUNC niDigital_GetTimeSetPeriod(ViSession vi, ViConstString timeSet, ViReal64 *period)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The specified digital pattern instrument handle |
| timeSet | [in] | ViConstString | The specified time set name. |
| period | [out] | ViReal64 * | Returned period, in seconds, that the edge is configured to. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__levels__and__timing__low__level_1ga4b7ae8cd446f5fd0518239a594ec33d0.html language=enus -->
## TOPIC 00064: niDigital_ConfigureTimeSetEdge

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__levels__and__timing__low__level_1ga4b7ae8cd446f5fd0518239a594ec33d0.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__levels__and__timing__low__level_1ga4b7ae8cd446f5fd0518239a594ec33d0.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the edge placement for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify th

### niDigital_ConfigureTimeSetEdge

Configures the edge placement for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the [niDigital_ApplyLevelsAndTiming](group____root__ni_digital__functions__levels__and__timing_1ga2d08e97007c4f46ad280d74b2b246e6d.html) function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to [niDigital_ApplyLevelsAndTiming](group____root__ni_digital__functions__levels__and__timing_1ga2d08e97007c4f46ad280d74b2b246e6d.html); it only affects the values of the current timing context.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigureTimeSetEdge(ViSession vi, ViConstString pinList, ViConstString timeSet, ViInt32 edge, ViReal64 time)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The specified digital pattern instrument handle |
| pinList | [in] | ViConstString | List of pin and pin group names for which to configure the time set edges. |
| timeSet | [in] | ViConstString | The specified time set name. |
| edge | [in] | ViInt32 | Name of the edge.Defined Values:NameValueDescriptionNIDIGITAL_VAL_DRIVE_ON2800 (0xaf0)Specifies the drive on edge of the time set.NIDIGITAL_VAL_DRIVE_DATA2801 (0xaf1)Specifies the drive data edge of the time set.NIDIGITAL_VAL_DRIVE_RETURN2802 (0xaf2)Specifies the drive return edge of the time set.NIDIGITAL_VAL_DRIVE_OFF2803 (0xaf3)Specifies the drive off edge of the time set.NIDIGITAL_VAL_COMPARE_STROBE2804 (0xaf4)Specifies the compare strobe of the time set.NIDIGITAL_VAL_DRIVE_DATA22805 (0xaf5)Specifies the drive data 2 edge of the time set.NIDIGITAL_VAL_DRIVE_RETURN22806 (0xaf6)Specifies the drive return 2 edge of the time set.NIDIGITAL_VAL_COMPARE_STROBE22807 (0xaf7)Specifies the compare strobe 2 of the time set. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_DRIVE_ON | 2800 (0xaf0) | Specifies the drive on edge of the time set. |  |
| NIDIGITAL_VAL_DRIVE_DATA | 2801 (0xaf1) | Specifies the drive data edge of the time set. |  |
| NIDIGITAL_VAL_DRIVE_RETURN | 2802 (0xaf2) | Specifies the drive return edge of the time set. |  |
| NIDIGITAL_VAL_DRIVE_OFF | 2803 (0xaf3) | Specifies the drive off edge of the time set. |  |
| NIDIGITAL_VAL_COMPARE_STROBE | 2804 (0xaf4) | Specifies the compare strobe of the time set. |  |
| NIDIGITAL_VAL_DRIVE_DATA2 | 2805 (0xaf5) | Specifies the drive data 2 edge of the time set. |  |
| NIDIGITAL_VAL_DRIVE_RETURN2 | 2806 (0xaf6) | Specifies the drive return 2 edge of the time set. |  |
| NIDIGITAL_VAL_COMPARE_STROBE2 | 2807 (0xaf7) | Specifies the compare strobe 2 of the time set. |  |
| time | [in] | ViReal64 | The time from the beginning of the vector period in which to place the edge. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__levels__and__timing__low__level_1gaa014a211b3708d2d30e7bfed80c43be3.html language=enus -->
## TOPIC 00065: niDigital_GetTimeSetDriveFormat

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__levels__and__timing__low__level_1gaa014a211b3708d2d30e7bfed80c43be3.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__levels__and__timing__low__level_1gaa014a211b3708d2d30e7bfed80c43be3.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the drive format of a pin in the specified time set. SyntaxViStatus _VI_FUNC niDigital_GetTimeSetDriveFormat(ViSession vi, ViConstString pin, ViConstString timeSet, ViInt32 *format)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe specified digital pattern instrument handle pin[in]ViC

### niDigital_GetTimeSetDriveFormat

Returns the drive format of a pin in the specified time set.

#### Syntax

ViStatus _VI_FUNC niDigital_GetTimeSetDriveFormat(ViSession vi, ViConstString pin, ViConstString timeSet, ViInt32 *format)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The specified digital pattern instrument handle |
| pin | [in] | ViConstString | Name of the specified pin. |
| timeSet | [in] | ViConstString | The specified time set name. |
| format | [out] | ViInt32 * | Returned drive format of the time set for the specified pin. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__levels__and__timing__low__level_1gaeb4693b6d9be928395e5297ab4024833.html language=enus -->
## TOPIC 00066: niDigital_ConfigureTimeSetDriveFormat

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__levels__and__timing__low__level_1gaeb4693b6d9be928395e5297ab4024833.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__levels__and__timing__low__level_1gaeb4693b6d9be928395e5297ab4024833.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive format for the pins not specified in the pinList. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify t

### niDigital_ConfigureTimeSetDriveFormat

Configures the drive format for the pins not specified in the **pinList**. Use this function to modify time set values after applying a timing sheet with the [niDigital_ApplyLevelsAndTiming](group____root__ni_digital__functions__levels__and__timing_1ga2d08e97007c4f46ad280d74b2b246e6d.html) function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to [niDigital_ApplyLevelsAndTiming](group____root__ni_digital__functions__levels__and__timing_1ga2d08e97007c4f46ad280d74b2b246e6d.html); it only affects the values of the current timing context.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigureTimeSetDriveFormat(ViSession vi, ViConstString pinList, ViConstString timeSet, ViInt32 driveFormat)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| pinList | [in] | ViConstString | List of pin and pin group names for which to configure the time set edges. |
| timeSet | [in] | ViConstString | The specified time set name. |
| driveFormat | [in] | ViInt32 | Drive format of the time set.Defined Values:NameValueDescriptionNIDIGITAL_VAL_NR1500 (0x5dc)Non-return: Drive format remains at logic level after each bit.NIDIGITAL_VAL_RL1501 (0x5dd)Return to low: Drive format returns to a logic level low after each bit.NIDIGITAL_VAL_RH1502 (0x5de)Return to high: Drive format returns to a logic level high after each bit.NIDIGITAL_VAL_SBC1503 (0x5df)Surround by complement: Drive format returns to the complement logic level of the bit after each bit. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_NR | 1500 (0x5dc) | Non-return: Drive format remains at logic level after each bit. |  |
| NIDIGITAL_VAL_RL | 1501 (0x5dd) | Return to low: Drive format returns to a logic level low after each bit. |  |
| NIDIGITAL_VAL_RH | 1502 (0x5de) | Return to high: Drive format returns to a logic level high after each bit. |  |
| NIDIGITAL_VAL_SBC | 1503 (0x5df) | Surround by complement: Drive format returns to the complement logic level of the bit after each bit. |  |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__match__fail__combination.html language=enus -->
## TOPIC 00067: Match Fail Combination

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__match__fail__combination.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__match__fail__combination.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_EnableMatchFailCombinationConfigures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those r

### Match Fail Combination

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_EnableMatchFailCombination | Configures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__match__fail__combination_1ga83d37f47d53452984f270f105a8b728e.html language=enus -->
## TOPIC 00068: niDigital_EnableMatchFailCombination

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__match__fail__combination_1ga83d37f47d53452984f270f105a8b728e.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__match__fail__combination_1ga83d37f47d53452984f270f105a8b728e.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results. SyntaxViStatus _VI_FUNC niDigital_EnableMatchFailCombination(ViUIn

### niDigital_EnableMatchFailCombination

Configures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results.

#### Syntax

ViStatus _VI_FUNC niDigital_EnableMatchFailCombination(ViUInt32 sessionCount, ViSession sessions[], ViSession syncSession)

#### Remarks

You must initialize the PXIe-6674T using NI-Sync and use the niTClk Synchronize function to synchronize instruments before calling the [niDigital_EnableMatchFailCombination](group____root__ni_digital__functions__match__fail__combination_1ga83d37f47d53452984f270f105a8b728e.html) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| sessionCount | [in] | ViUInt32 | Number of sessions. |
| sessions | [in] | ViSession[] | The specified array of sessions synchronized using NI-TClk. |
| syncSession | [in] | ViSession | The specified NI-Sync session. |

#### Returns

Reports the status of the operation.

Parent topic:

Match Fail Combination

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__action_1gadec831e054a2c74721253a679c06e6ca.html language=enus -->
## TOPIC 00069: niDigital_BurstPatternSynchronized

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__action_1gadec831e054a2c74721253a679c06e6ca.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__action_1gadec831e054a2c74721253a679c06e6ca.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Uses the startLabel you specify to burst a pattern on the sites you specify. Use this function to burst a pattern on digital pattern instruments that you have previously synchronized using NI-TClk. SyntaxViStatus _VI_FUNC niDigital_BurstPatternSynchronized(ViUInt32 sessionCount, ViSession sessions[]

### niDigital_BurstPatternSynchronized

Uses the **startLabel** you specify to burst a pattern on the sites you specify. Use this function to burst a pattern on digital pattern instruments that you have previously synchronized using NI-TClk.

#### Syntax

ViStatus _VI_FUNC niDigital_BurstPatternSynchronized(ViUInt32 sessionCount, ViSession sessions[], ViConstString siteList, ViConstString startLabel, ViBoolean selectDigitalFunction, ViBoolean waitUntilDone, ViReal64 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| sessionCount | [in] | ViUInt32 | Number of niDigital sessions. |
| sessions | [in] | ViSession[] | An array of niDigital sessions. |
| siteList | [in] | ViConstString | The sites on which to burst the pattern as a comma-delimited list of strings in the form siteN, where N is the site number. If you specify an empty string, the pattern is burst on all sites. |
| startLabel | [in] | ViConstString | Pattern name or exported pattern label from which to start bursting the pattern. |
| selectDigitalFunction | [in] | ViBoolean | A Boolean that specifies whether to select the digital function for the pins in the pattern prior to bursting. |
| waitUntilDone | [in] | ViBoolean | A Boolean that indicates whether to wait until the bursting is complete. |
| timeout | [in] | ViReal64 | The maximum time allowed for this function to complete, in seconds. If this function does not complete within this time interval, the function returns an error if waitUntilDone is True. |

#### Returns

Reports the status of the operation.

Parent topic:

Pattern Action

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__action__low__level__action.html language=enus -->
## TOPIC 00070: Low Level Action

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__action__low__level__action.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__action__low__level__action.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_AbortStops bursting the pattern. niDigital_AbortKeepAliveStops the keep alive pattern if it is currently running. niDigital_CommitApplies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern

### Low Level Action

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_Abort | Stops bursting the pattern. |
| niDigital_AbortKeepAlive | Stops the keep alive pattern if it is currently running. |
| niDigital_Commit | Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the niDigital_Commit function, then the niDigital_Initiate function or the niDigital_BurstPattern function will implicitly call this function for you. Calling this function moves the session from the Uncommitted state to the Committed state. |
| niDigital_Initiate | Starts bursting the pattern. If you do not call the niDigital_Commit function, this function implicitly calls the niDigital_Commit function for you. |
| niDigital_IsDone | Checks the hardware to determine if the pattern burst has completed or if any errors have occurred. |
| niDigital_WaitUntilDone | Waits until the pattern burst has completed or the timeout has expired. |

#### Attachments

None

Parent topic:

Pattern Action

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__action__low__level__action_1ga3f502a5b2a666ce35f25f119a081d57c.html language=enus -->
## TOPIC 00071: niDigital_Abort

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__action__low__level__action_1ga3f502a5b2a666ce35f25f119a081d57c.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__action__low__level__action_1ga3f502a5b2a666ce35f25f119a081d57c.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops bursting the pattern. SyntaxViStatus _VI_FUNC niDigital_Abort(ViSession vi)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigital_init or niDigital_InitWithOptions function returns. ReturnsReports the status of the operation.

### niDigital_Abort

Stops bursting the pattern.

#### Syntax

ViStatus _VI_FUNC niDigital_Abort(ViSession vi)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level Action

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__action__low__level__action_1ga4f9e50272e8fed85b2c4b0db6ca38884.html language=enus -->
## TOPIC 00072: niDigital_Commit

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__action__low__level__action_1ga4f9e50272e8fed85b2c4b0db6ca38884.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__action__low__level__action_1ga4f9e50272e8fed85b2c4b0db6ca38884.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the niDigital_Commit function, then the niDigital_Initiate function or the niDigital_BurstPattern function will implicitly call this function for

### niDigital_Commit

Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the [niDigital_Commit](group____root__ni_digital__functions__pattern__action__low__level__action_1ga4f9e50272e8fed85b2c4b0db6ca38884.html) function, then the [niDigital_Initiate](group____root__ni_digital__functions__pattern__action__low__level__action_1ga992e80f747168211cd44d3ca09309f6f.html) function or the [niDigital_BurstPattern](group____root__ni_digital__functions__pattern__action_1ga0e9a6597044b41afae031dcd59e32330.html) function will implicitly call this function for you. Calling this function moves the session from the Uncommitted state to the Committed state.

#### Syntax

ViStatus _VI_FUNC niDigital_Commit(ViSession vi)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level Action

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__action__low__level__action_1ga8b46cfedd663e9ce87041a73fe75f157.html language=enus -->
## TOPIC 00073: niDigital_WaitUntilDone

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__action__low__level__action_1ga8b46cfedd663e9ce87041a73fe75f157.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__action__low__level__action_1ga8b46cfedd663e9ce87041a73fe75f157.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the pattern burst has completed or the timeout has expired. SyntaxViStatus _VI_FUNC niDigital_WaitUntilDone(ViSession vi, ViReal64 timeout)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigital_init or niDigital_InitWithOptions function returns. timeout

### niDigital_WaitUntilDone

Waits until the pattern burst has completed or the timeout has expired.

#### Syntax

ViStatus _VI_FUNC niDigital_WaitUntilDone(ViSession vi, ViReal64 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| timeout | [in] | ViReal64 | Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level Action

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__action__low__level__action_1ga992e80f747168211cd44d3ca09309f6f.html language=enus -->
## TOPIC 00074: niDigital_Initiate

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__action__low__level__action_1ga992e80f747168211cd44d3ca09309f6f.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__action__low__level__action_1ga992e80f747168211cd44d3ca09309f6f.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts bursting the pattern. If you do not call the niDigital_Commit function, this function implicitly calls the niDigital_Commit function for you. SyntaxViStatus _VI_FUNC niDigital_Initiate(ViSession vi)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigital_init

### niDigital_Initiate

Starts bursting the pattern. If you do not call the [niDigital_Commit](group____root__ni_digital__functions__pattern__action__low__level__action_1ga4f9e50272e8fed85b2c4b0db6ca38884.html) function, this function implicitly calls the [niDigital_Commit](group____root__ni_digital__functions__pattern__action__low__level__action_1ga4f9e50272e8fed85b2c4b0db6ca38884.html) function for you.

#### Syntax

ViStatus _VI_FUNC niDigital_Initiate(ViSession vi)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level Action

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__action__low__level__action_1ga9941885d9d609773ffd6723057a30f46.html language=enus -->
## TOPIC 00075: niDigital_AbortKeepAlive

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__action__low__level__action_1ga9941885d9d609773ffd6723057a30f46.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__action__low__level__action_1ga9941885d9d609773ffd6723057a30f46.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the keep alive pattern if it is currently running. SyntaxViStatus _VI_FUNC niDigital_AbortKeepAlive(ViSession vi)RemarksIf a pattern burst is in progress, the function aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs

### niDigital_AbortKeepAlive

Stops the keep alive pattern if it is currently running.

#### Syntax

ViStatus _VI_FUNC niDigital_AbortKeepAlive(ViSession vi)

#### Remarks

If a pattern burst is in progress, the function aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level Action

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__action__low__level__action_1gafcafdc8a785766c1082abf537ae57da3.html language=enus -->
## TOPIC 00076: niDigital_IsDone

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__action__low__level__action_1gafcafdc8a785766c1082abf537ae57da3.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__action__low__level__action_1gafcafdc8a785766c1082abf537ae57da3.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the hardware to determine if the pattern burst has completed or if any errors have occurred. SyntaxViStatus _VI_FUNC niDigital_IsDone(ViSession vi, ViBoolean *done)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigital_init or niDigital_InitWithOptions funct

### niDigital_IsDone

Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.

#### Syntax

ViStatus _VI_FUNC niDigital_IsDone(ViSession vi, ViBoolean *done)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| done | [out] | ViBoolean * | A Boolean that indicates whether the pattern burst completed. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level Action

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__configuration.html language=enus -->
## TOPIC 00077: Pattern Configuration

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__configuration.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__configuration.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_ConfigurePatternBurstSitesConfigures which sites burst the pattern on the next call to the niDigital_Initiate function. The pattern burst sites can also be modified through the siteList parameter in the niDigital_BurstPattern function. If a site has be

### Pattern Configuration

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_ConfigurePatternBurstSites | Configures which sites burst the pattern on the next call to the niDigital_Initiate function. The pattern burst sites can also be modified through the siteList parameter in the niDigital_BurstPattern function. If a site has been disabled through the niDigital_DisableSites function, the site does not burst a pattern even if included in the pattern burst sites. |
| niDigital_ConfigureStartLabel | Configures the pattern name or exported label in the loaded patterns from which to start bursting the pattern. If you want to start bursting the pattern from the first vector, specify the pattern name. |
| niDigital_GetPatternName | Gets the name of a pattern from the pattern index. |
| niDigital_GetPatternPinIndexes | Returns the indexes of the pins included in the pattern you specify. |
| niDigital_GetPatternPinList | Returns the pattern pin list. |
| niDigital_LoadPattern | Loads the specified pattern file. |
| niDigital_UnloadAllPatterns | Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__configuration_1ga3fe7061b8701331ea078282b044d26df.html language=enus -->
## TOPIC 00078: niDigital_ConfigurePatternBurstSites

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__configuration_1ga3fe7061b8701331ea078282b044d26df.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__configuration_1ga3fe7061b8701331ea078282b044d26df.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures which sites burst the pattern on the next call to the niDigital_Initiate function. The pattern burst sites can also be modified through the siteList parameter in the niDigital_BurstPattern function. If a site has been disabled through the niDigital_DisableSites function, the site does not

### niDigital_ConfigurePatternBurstSites

Configures which sites burst the pattern on the next call to the [niDigital_Initiate](group____root__ni_digital__functions__pattern__action__low__level__action_1ga992e80f747168211cd44d3ca09309f6f.html) function. The pattern burst sites can also be modified through the **siteList** parameter in the [niDigital_BurstPattern](group____root__ni_digital__functions__pattern__action_1ga0e9a6597044b41afae031dcd59e32330.html) function. If a site has been disabled through the [niDigital_DisableSites](group____root__ni_digital__functions__pin__map_1gaaef0da31adbbfa8ea1431946ffcc57a3.html) function, the site does not burst a pattern even if included in the pattern burst sites.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigurePatternBurstSites(ViSession vi, ViConstString siteList)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| siteList | [in] | ViConstString | A comma-delimited list of strings in the form of siteN, where N is the site number. If you specify an empty string, the function returns pass or fail results for all sites. If the string is empty, all sites are configured for pattern bursting. |

#### Returns

Reports the status of the operation.

Parent topic:

Pattern Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__configuration_1ga55cf45e1052dbc15c0c80c0fbd7fe1bf.html language=enus -->
## TOPIC 00079: niDigital_UnloadAllPatterns

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__configuration_1ga55cf45e1052dbc15c0c80c0fbd7fe1bf.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__configuration_1ga55cf45e1052dbc15c0c80c0fbd7fe1bf.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument. SyntaxViStatus _VI_FUNC niDigital_UnloadAllPatterns(ViSession vi, ViBoolean unloadKeepAlivePattern)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigital_init or niDigi

### niDigital_UnloadAllPatterns

Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

#### Syntax

ViStatus _VI_FUNC niDigital_UnloadAllPatterns(ViSession vi, ViBoolean unloadKeepAlivePattern)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| unloadKeepAlivePattern | [in] | ViBoolean | A Boolean that specifies whether to keep or unload the keep alive pattern. |

#### Returns

Reports the status of the operation.

Parent topic:

Pattern Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pattern__configuration_1gaa00caf3633e6b5cfd0f1d4975a425712.html language=enus -->
## TOPIC 00080: niDigital_GetPatternPinIndexes

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pattern__configuration_1gaa00caf3633e6b5cfd0f1d4975a425712.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pattern__configuration_1gaa00caf3633e6b5cfd0f1d4975a425712.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the indexes of the pins included in the pattern you specify. SyntaxViStatus _VI_FUNC niDigital_GetPatternPinIndexes(ViSession vi, ViConstString startLabel, ViInt32 pinIndexesBufferSize, ViInt32 pinIndexes[], ViInt32 *actualNumPins)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe inst

### niDigital_GetPatternPinIndexes

Returns the indexes of the pins included in the pattern you specify.

#### Syntax

ViStatus _VI_FUNC niDigital_GetPatternPinIndexes(ViSession vi, ViConstString startLabel, ViInt32 pinIndexesBufferSize, ViInt32 pinIndexes[], ViInt32 *actualNumPins)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| startLabel | [in] | ViConstString | The specified pattern name or exported pattern label from which to get the pin names referenced by the pattern. |
| pinIndexesBufferSize | [in] | ViInt32 | The number of elements in the ViInt32 array you specify for pinIndexes. To determine the size of the buffer to allocate for the pinIndexes array, pass a value of 0 to the pinIndexesBufferSize parameter and a value of VI_NULL to the pinIndexes parameter. In this case, the value returned by the actualNumPins parameter is the size of the array necessary to hold the pin indexes. |
| pinIndexes | [out] | ViInt32[] | The returned pin indexes referenced by the pattern with the start label. Call niDigital_GetPinName to get the pin name associated with each pin index. |
| actualNumPins | [out] | ViInt32 * | Number of pin indexes written to the pinIndexes array. |

#### Returns

Reports the status of the operation.

Parent topic:

Pattern Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pin__control.html language=enus -->
## TOPIC 00081: Pin Control

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pin__control.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pin__control.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_SelectFunctionSpecifies whether digital pattern instrument channels are controlled by the PPMU, Digital, disconnected, or off. Changes take effect immediately. AttachmentsNone

### Pin Control

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_SelectFunction | Specifies whether digital pattern instrument channels are controlled by the PPMU, Digital, disconnected, or off. Changes take effect immediately. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pin__control_1ga062a77889dfe3b634fcd7ba3188b9589.html language=enus -->
## TOPIC 00082: niDigital_SelectFunction

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pin__control_1ga062a77889dfe3b634fcd7ba3188b9589.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pin__control_1ga062a77889dfe3b634fcd7ba3188b9589.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether digital pattern instrument channels are controlled by the PPMU, Digital, disconnected, or off. Changes take effect immediately. SyntaxViStatus _VI_FUNC niDigital_SelectFunction(ViSession vi, ViConstString channelList, ViInt32 function)RemarksChannels disconnect when a new instrumen

### niDigital_SelectFunction

Specifies whether digital pattern instrument channels are controlled by the PPMU, Digital, disconnected, or off. Changes take effect immediately.

#### Syntax

ViStatus _VI_FUNC niDigital_SelectFunction(ViSession vi, ViConstString channelList, ViInt32 function)

#### Remarks

Channels disconnect when a new instrument session is created if the reset input parameter is VI_TRUE. The [niDigital_BurstPattern](group____root__ni_digital__functions__pattern__action_1ga0e9a6597044b41afae031dcd59e32330.html) function automatically changes the function to Digital for the pins in the pattern if the **selectDigitalFunction** parameter is set to VI_TRUE. The [niDigital_PPMU_Source](group____root__ni_digital__functions__ppmu__action_1gabdf567482e391df8f38a4a5fb96dba69.html) function always changes the function to PPMU for the pins in the **channelList** automatically.

Note

You can make PPMU voltage measurements using the [niDigital_PPMU_Measure](group____root__ni_digital__functions__ppmu__action_1ga76923e247e169fc5960454f8935aa2b6.html) function from within any selected function.

**Caution:** In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelList | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| function | [in] | ViInt32 | Parameter that specifies whether to disconnect the pins, or use the PPMU or pin driver to control the pins.Defined Values:NameValueDescriptionNIDIGITAL_VAL_DIGITAL1100 (0x44c)The pin is connected to the driver, comparator, and active load functions. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the selected function to Digital is determined by the most recent call to the niDigital_WriteStatic function or the last vector of the most recently executed pattern burst, whichever happened last. Use the niDigital_WriteStatic function to control the state of the digital pin driver through software. Use the niDigital_BurstPattern function to control the state of the digital pin driver through a pattern. Set the selectDigitalFunction parameter of the niDigital_BurstPattern function to VI_TRUE to automatically switch the selected function of the pins in the pattern burst to NIDIGITAL_VAL_DIGITAL.NIDIGITAL_VAL_PPMU1101 (0x44d)The pin is connected to the PPMU. The driver, comparator, and active load are off while this function is selected. Call the niDigital_PPMU_Source function to source a voltage or current. The niDigital_PPMU_Source function automatically switches the selected function to the PPMU state and starts sourcing from the PPMU. Changing the selected function to NIDIGITAL_VAL_DISCONNECT, NIDIGITAL_VAL_OFF, or NIDIGITAL_VAL_DIGITAL causes the PPMU to stop sourcing. If you change the selected function to PPMU using the niDigital_SelectFunction function, the PPMU is initially not sourcing.NIDIGITAL_VAL_OFF1102 (0x44e)The pin is electrically connected, and the PPMU and digital pin driver are off while this function is selected.NIDIGITAL_VAL_DISCONNECT1103 (0x44f)The pin is electrically disconnected from instrument functions. Selecting this function causes the PPMU to stop sourcing prior to disconnecting the pin.NIDIGITAL_VAL_RIO1104 (0x450)Yields control of the specified pin(s) to LabVIEW FPGA. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_DIGITAL | 1100 (0x44c) | The pin is connected to the driver, comparator, and active load functions. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the selected function to Digital is determined by the most recent call to the niDigital_WriteStatic function or the last vector of the most recently executed pattern burst, whichever happened last. Use the niDigital_WriteStatic function to control the state of the digital pin driver through software. Use the niDigital_BurstPattern function to control the state of the digital pin driver through a pattern. Set the selectDigitalFunction parameter of the niDigital_BurstPattern function to VI_TRUE to automatically switch the selected function of the pins in the pattern burst to NIDIGITAL_VAL_DIGITAL. |  |
| NIDIGITAL_VAL_PPMU | 1101 (0x44d) | The pin is connected to the PPMU. The driver, comparator, and active load are off while this function is selected. Call the niDigital_PPMU_Source function to source a voltage or current. The niDigital_PPMU_Source function automatically switches the selected function to the PPMU state and starts sourcing from the PPMU. Changing the selected function to NIDIGITAL_VAL_DISCONNECT, NIDIGITAL_VAL_OFF, or NIDIGITAL_VAL_DIGITAL causes the PPMU to stop sourcing. If you change the selected function to PPMU using the niDigital_SelectFunction function, the PPMU is initially not sourcing. |  |
| NIDIGITAL_VAL_OFF | 1102 (0x44e) | The pin is electrically connected, and the PPMU and digital pin driver are off while this function is selected. |  |
| NIDIGITAL_VAL_DISCONNECT | 1103 (0x44f) | The pin is electrically disconnected from instrument functions. Selecting this function causes the PPMU to stop sourcing prior to disconnecting the pin. |  |
| NIDIGITAL_VAL_RIO | 1104 (0x450) | Yields control of the specified pin(s) to LabVIEW FPGA. |  |

#### Returns

Reports the status of the operation.

Parent topic:

Pin Control

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pin__map_1ga1f009d26e02dfde4788e4f4d49ca12ab.html language=enus -->
## TOPIC 00083: niDigital_LoadPinMap

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pin__map_1ga1f009d26e02dfde4788e4f4d49ca12ab.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pin__map_1ga1f009d26e02dfde4788e4f4d49ca12ab.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the niDigital_reset function. SyntaxViStatus _VI_FUNC niDigital_LoadPinMap(ViSession vi, ViConstString pinMapFilePath)ParametersName

### niDigital_LoadPinMap

Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the [niDigital_reset](group____root__ni_digital__functions__utility_1ga3b85968802e1434b912ed112f8614f7d.html) function.

#### Syntax

ViStatus _VI_FUNC niDigital_LoadPinMap(ViSession vi, ViConstString pinMapFilePath)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| pinMapFilePath | [in] | ViConstString | Absolute file path to a pin map file created with the Digital Pattern Editor or the NI TestStand Semiconductor Module. |

#### Returns

Reports the status of the operation.

Parent topic:

Pin Map

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pin__map_1gaaef0da31adbbfa8ea1431946ffcc57a3.html language=enus -->
## TOPIC 00084: niDigital_DisableSites

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pin__map_1gaaef0da31adbbfa8ea1431946ffcc57a3.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pin__map_1gaaef0da31adbbfa8ea1431946ffcc57a3.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables specified sites. Disabled sites are not included in pattern bursts initiated by the niDigital_Initiate function or the niDigital_BurstPattern function, even if the site is specified in the list of pattern burst sites in niDigital_ConfigurePatternBurstSites function or in the siteList input

### niDigital_DisableSites

Disables specified sites. Disabled sites are not included in pattern bursts initiated by the [niDigital_Initiate](group____root__ni_digital__functions__pattern__action__low__level__action_1ga992e80f747168211cd44d3ca09309f6f.html) function or the [niDigital_BurstPattern](group____root__ni_digital__functions__pattern__action_1ga0e9a6597044b41afae031dcd59e32330.html) function, even if the site is specified in the list of pattern burst sites in [niDigital_ConfigurePatternBurstSites](group____root__ni_digital__functions__pattern__configuration_1ga3fe7061b8701331ea078282b044d26df.html) function or in the **siteList** input of the [niDigital_BurstPattern](group____root__ni_digital__functions__pattern__action_1ga0e9a6597044b41afae031dcd59e32330.html) function.

#### Syntax

ViStatus _VI_FUNC niDigital_DisableSites(ViSession vi, ViConstString siteList)

#### Remarks

Additionally, if you specify a list of pin or pin group names in a **channelList** parameter in any NI-Digital function, digital pattern instrument channels mapped to disabled sites are not affected by the function. The functions that return per-pin data, such as the [niDigital_PPMU_Measure](group____root__ni_digital__functions__ppmu__action_1ga76923e247e169fc5960454f8935aa2b6.html) function, do not return data for channels mapped to disabled sites.

The digital pattern instrument channels mapped to the sites specified are left in their current state.

NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this function with the Semiconductor Module.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| siteList | [in] | ViConstString | Comma-delimited list of strings in the form of siteN, where N is the site number. If you enter an empty string, the function disables all sites. |

#### Returns

Reports the status of the operation.

Parent topic:

Pin Map

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pin__map__low__level_1ga6b84b495d77ea95d9155353ec8b3e006.html language=enus -->
## TOPIC 00085: niDigital_GetPinName

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pin__map__low__level_1ga6b84b495d77ea95d9155353ec8b3e006.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pin__map__low__level_1ga6b84b495d77ea95d9155353ec8b3e006.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of the pin at the index you specify. SyntaxViStatus _VI_FUNC niDigital_GetPinName(ViSession vi, ViInt32 pinIndex, ViInt32 nameBufferSize, ViChar name[])RemarksYou must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the nameBu

### niDigital_GetPinName

Returns the name of the pin at the index you specify.

#### Syntax

ViStatus _VI_FUNC niDigital_GetPinName(ViSession vi, ViInt32 pinIndex, ViInt32 nameBufferSize, ViChar name[])

#### Remarks

You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **nameBufferSize**. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the function copies (buffer size - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for **nameBufferSize** and VI_NULL for the name.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| pinIndex | [in] | ViInt32 | Index of pin to query. Pin indexes begin at 0. |
| nameBufferSize | [in] | ViInt32 | The number of elements in the ViChar array you specify for name. |
| name | [out] | ViChar[] | Returns the pin name at the specified pinIndex. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pin__map__low__level_1gae9d68883b801478399ddb1e99e12c321.html language=enus -->
## TOPIC 00086: niDigital_CreatePinMap

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pin__map__low__level_1gae9d68883b801478399ddb1e99e12c321.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pin__map__low__level_1gae9d68883b801478399ddb1e99e12c321.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates and loads a pin map. Use this function if you are not loading a pin map file using the niDigital_LoadPinMap function. SyntaxViStatus _VI_FUNC niDigital_CreatePinMap(ViSession vi, ViConstString dutPinList, ViConstString systemPinList)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe in

### niDigital_CreatePinMap

Creates and loads a pin map. Use this function if you are not loading a pin map file using the [niDigital_LoadPinMap](group____root__ni_digital__functions__pin__map_1ga1f009d26e02dfde4788e4f4d49ca12ab.html) function.

#### Syntax

ViStatus _VI_FUNC niDigital_CreatePinMap(ViSession vi, ViConstString dutPinList, ViConstString systemPinList)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| dutPinList | [in] | ViConstString | A list of device under test (DUT) pin names to include in the pin map. DUT pins are duplicated for all sites and are used in patterns. |
| systemPinList | [in] | ViConstString | A list of system pins to include in the pin map. System pins do not scale with the number of sites and are not used with pattern functions. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__pin__map__low__level_1gaeff7e326939d2cba4a29c8d53be2f1c0.html language=enus -->
## TOPIC 00087: niDigital_MapPinToChannel

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__pin__map__low__level_1gaeff7e326939d2cba4a29c8d53be2f1c0.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__pin__map__low__level_1gaeff7e326939d2cba4a29c8d53be2f1c0.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps a pin to a digital pattern instrument channel. You must call the niDigital_CreateChannelMap function before you call this function and call the niDigital_EndChannelMap function after creating all connections. For DUT pins, you must call this function multiple times for each pin and once for eac

### niDigital_MapPinToChannel

Maps a pin to a digital pattern instrument channel. You must call the [niDigital_CreateChannelMap](group____root__ni_digital__functions__pin__map__low__level_1ga97227f2540babc13fa7c10398a8ee3c6.html) function before you call this function and call the [niDigital_EndChannelMap](group____root__ni_digital__functions__pin__map__low__level_1ga53ee9dadf6501ebea3efd66118633db9.html) function after creating all connections. For DUT pins, you must call this function multiple times for each pin and once for each site. For system pins, call this function only once per pin because the function ignores the **site** input for system pins.

#### Syntax

ViStatus _VI_FUNC niDigital_MapPinToChannel(ViSession vi, ViConstString pin, ViInt32 site, ViConstString channel)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| pin | [in] | ViConstString | Name of the pin to map to the specified channel. |
| site | [in] | ViInt32 | Site number for the pin mapped to the specified channel. If the pin is a system pin, the function ignores this parameter. |
| channel | [in] | ViConstString | Channel to map to the specified pin and site. Specify channel names using the channel number, for example, "0" or "31." To specify channels used in multi-instrument sessions, use the form PXI1Slot2/0 or PXI1Spot2/31. |

#### Returns

Reports the status of the operation.

Parent topic:

Low Level

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__ppmu__action.html language=enus -->
## TOPIC 00088: PPMU Action

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__ppmu__action.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__ppmu__action.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_PPMU_MeasureInstructs the PPMU to measure voltage or current. This function can be called to take a voltage measurement even if the pin function is not set to PPMU. niDigital_PPMU_SourceStarts sourcing voltage or current from the PPMU. This function au

### PPMU Action

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_PPMU_Measure | Instructs the PPMU to measure voltage or current. This function can be called to take a voltage measurement even if the pin function is not set to PPMU. |
| niDigital_PPMU_Source | Starts sourcing voltage or current from the PPMU. This function automatically selects the PPMU function. Changes to PPMU source settings do not take effect until you call this function. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__ppmu__configuration_1ga9bbbaabd50b857dc9aa21c90853711aa.html language=enus -->
## TOPIC 00089: niDigital_PPMU_ConfigureOutputFunction

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__ppmu__configuration_1ga9bbbaabd50b857dc9aa21c90853711aa.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__ppmu__configuration_1ga9bbbaabd50b857dc9aa21c90853711aa.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures to source DC voltage or DC current from the PPMU. SyntaxViStatus _VI_FUNC niDigital_PPMU_ConfigureOutputFunction(ViSession vi, ViConstString channelList, ViInt32 outputFunction)RemarksYou must call the niDigital_PPMU_Source function for changes to the PPMU configuration to take effect, ev

### niDigital_PPMU_ConfigureOutputFunction

Configures to source DC voltage or DC current from the PPMU.

#### Syntax

ViStatus _VI_FUNC niDigital_PPMU_ConfigureOutputFunction(ViSession vi, ViConstString channelList, ViInt32 outputFunction)

#### Remarks

You must call the [niDigital_PPMU_Source](group____root__ni_digital__functions__ppmu__action_1gabdf567482e391df8f38a4a5fb96dba69.html) function for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelList | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| outputFunction | [in] | ViInt32 | Parameter that configures the operation to use for the channels or pins you specify.Defined Values:NameValueDescriptionNIDIGITAL_VAL_DC_VOLTAGE1300 (0x514)Specifies the output function to DC Voltage.NIDIGITAL_VAL_DC_CURRENT1301 (0x515)Specifies the output function to DC Current. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_DC_VOLTAGE | 1300 (0x514) | Specifies the output function to DC Voltage. |  |
| NIDIGITAL_VAL_DC_CURRENT | 1301 (0x515) | Specifies the output function to DC Current. |  |

#### Returns

Reports the status of the operation.

Parent topic:

PPMU Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__ppmu__configuration_1gaa343f96f9dc83a4bae59d5ac1b07d393.html language=enus -->
## TOPIC 00090: niDigital_PPMU_ConfigureApertureTime

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__ppmu__configuration_1gaa343f96f9dc83a4bae59d5ac1b07d393.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__ppmu__configuration_1gaa343f96f9dc83a4bae59d5ac1b07d393.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the aperture time for a PPMU measurement on the specified channel(s). SyntaxViStatus _VI_FUNC niDigital_PPMU_ConfigureApertureTime(ViSession vi, ViConstString channelList, ViReal64 apertureTime, ViInt32 units)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the

### niDigital_PPMU_ConfigureApertureTime

Configures the aperture time for a PPMU measurement on the specified channel(s).

#### Syntax

ViStatus _VI_FUNC niDigital_PPMU_ConfigureApertureTime(ViSession vi, ViConstString channelList, ViReal64 apertureTime, ViInt32 units)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelList | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| apertureTime | [in] | ViReal64 | The measurement aperture time for the PPMU. |
| units | [in] | ViInt32 | Units of the measurement aperture time.Defined Values:NameValueDescriptionNIDIGITAL_VAL_SECONDS2100 (0x834)Specifies the aperture time in seconds. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_SECONDS | 2100 (0x834) | Specifies the aperture time in seconds. |  |

#### Returns

Reports the status of the operation.

Parent topic:

PPMU Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__ppmu__configuration__dc__current.html language=enus -->
## TOPIC 00091: DC Current

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__ppmu__configuration__dc__current.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__ppmu__configuration__dc__current.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_PPMU_ConfigureCurrentLevelSpecifies the current level that the PPMU forces to the DUT. niDigital_PPMU_ConfigureCurrentLevelRangeConfigures the current level range and defines the valid values that the current level can be set to using the niDigital_PPM

### DC Current

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_PPMU_ConfigureCurrentLevel | Specifies the current level that the PPMU forces to the DUT. |
| niDigital_PPMU_ConfigureCurrentLevelRange | Configures the current level range and defines the valid values that the current level can be set to using the niDigital_PPMU_ConfigureCurrentLevel function. The current level range setting is applicable only if the channel is set to the DC Current output function using the niDigital_PPMU_ConfigureOutputFunction function. |
| niDigital_PPMU_ConfigureVoltageLimits | Specifies the voltage limit high, or high clamp voltage (VCH), and voltage limit low, or low clamp voltage (VCL), for the specified pins when forcing current. |

#### Attachments

None

Parent topic:

PPMU Configuration

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__ppmu__configuration__dc__current_1ga2d195368a0962a5da5e614a9a56ed1a3.html language=enus -->
## TOPIC 00092: niDigital_PPMU_ConfigureVoltageLimits

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__ppmu__configuration__dc__current_1ga2d195368a0962a5da5e614a9a56ed1a3.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__ppmu__configuration__dc__current_1ga2d195368a0962a5da5e614a9a56ed1a3.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage limit high, or high clamp voltage (V[CH]), and voltage limit low, or low clamp voltage (V[CL]), for the specified pins when forcing current. SyntaxViStatus _VI_FUNC niDigital_PPMU_ConfigureVoltageLimits(ViSession vi, ViConstString channelList, ViReal64 lowerVoltageLimit, ViReal

### niDigital_PPMU_ConfigureVoltageLimits

Specifies the voltage limit high, or high clamp voltage (V<sub>CH</sub>), and voltage limit low, or low clamp voltage (V<sub>CL</sub>), for the specified pins when forcing current.

#### Syntax

ViStatus _VI_FUNC niDigital_PPMU_ConfigureVoltageLimits(ViSession vi, ViConstString channelList, ViReal64 lowerVoltageLimit, ViReal64 upperVoltageLimit)

#### Remarks

You must call the [niDigital_PPMU_Source](group____root__ni_digital__functions__ppmu__action_1gabdf567482e391df8f38a4a5fb96dba69.html) function for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

When forcing current by setting the [niDigital_PPMU_ConfigureOutputFunction](group____root__ni_digital__functions__ppmu__configuration_1ga9bbbaabd50b857dc9aa21c90853711aa.html) function to **DC Current**, the voltage is clamped to the specified voltage limits. Select the smallest voltage limits appropriate for the DUT.

If the voltage required by the DUT exceeds the specified voltage limits, the current output may not meet the specified current level. Choose larger voltage limits as needed and appropriate for the DUT.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelList | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| lowerVoltageLimit | [in] | ViReal64 | The nominal voltage at the pin at which the low side voltage clamp activates when the PPMU forces current to the DUT. |
| upperVoltageLimit | [in] | ViReal64 | The nominal voltage at the pin at which the high side voltage clamp activates when the PPMU forces current to the DUT. |

#### Returns

Reports the status of the operation.

Parent topic:

DC Current

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga007276bb58783032610844d6430769d0.html language=enus -->
## TOPIC 00093: niDigital_PPMU_ConfigureCurrentLimit

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga007276bb58783032610844d6430769d0.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga007276bb58783032610844d6430769d0.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit for the specified pins when forcing voltage. SyntaxViStatus _VI_FUNC niDigital_PPMU_ConfigureCurrentLimit(ViSession vi, ViConstString channelList, ViInt32 behavior, ViReal64 limit)RemarksYou must call the niDigital_PPMU_Source function for changes to the PPMU configuratio

### niDigital_PPMU_ConfigureCurrentLimit

Specifies the current limit for the specified pins when forcing voltage.

#### Syntax

ViStatus _VI_FUNC niDigital_PPMU_ConfigureCurrentLimit(ViSession vi, ViConstString channelList, ViInt32 behavior, ViReal64 limit)

#### Remarks

You must call the [niDigital_PPMU_Source](group____root__ni_digital__functions__ppmu__action_1gabdf567482e391df8f38a4a5fb96dba69.html) function for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

When forcing voltage by setting the [niDigital_PPMU_ConfigureOutputFunction](group____root__ni_digital__functions__ppmu__configuration_1ga9bbbaabd50b857dc9aa21c90853711aa.html) function to **NIDIGITAL_VAL_DC_VOLTAGE**, the current sourced or sunk is clamped to the specified current limit. Select the smallest current limit that meets the expected current requirements of the DUT. If the current required by the DUT exceeds the selected current limit range, the voltage output may not meet the specified voltage level. Choose a larger current limit range if needed.

Not all instruments support this capability. Refer to the Current Limit Supported attribute to programmatically determine whether an instrument supports this capability. If high-accuracy current clamping functionality is required, consider using a Source Measure Unit (SMU) instrument.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelList | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| behavior | [in] | ViInt32 | Behavior of the output current when the current limit is reached.Defined Values:NameValueDescriptionNIDIGITAL_VAL_CURRENT_REGULATE3100 (0xc1c)Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_CURRENT_REGULATE | 3100 (0xc1c) | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |  |
| limit | [in] | ViReal64 | Current limit, in amps, on the pins in the channelList parameter.The valid values for this parameter are defined by the current limit range. |

#### Returns

Reports the status of the operation.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga86083163cb6d3329d5eb44f5f56baf1b.html language=enus -->
## TOPIC 00094: niDigital_PPMU_ConfigureCurrentLimitRange

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga86083163cb6d3329d5eb44f5f56baf1b.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__ppmu__configuration__dc__voltage_1ga86083163cb6d3329d5eb44f5f56baf1b.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current limit range for the specified pins when forcing voltage. SyntaxViStatus _VI_FUNC niDigital_PPMU_ConfigureCurrentLimitRange(ViSession vi, ViConstString channelList, ViReal64 range)RemarksYou must call the niDigital_PPMU_Source function for changes to the PPMU configuration to ta

### niDigital_PPMU_ConfigureCurrentLimitRange

Specifies the current limit range for the specified pins when forcing voltage.

#### Syntax

ViStatus _VI_FUNC niDigital_PPMU_ConfigureCurrentLimitRange(ViSession vi, ViConstString channelList, ViReal64 range)

#### Remarks

You must call the [niDigital_PPMU_Source](group____root__ni_digital__functions__ppmu__action_1gabdf567482e391df8f38a4a5fb96dba69.html) function for changes to the PPMU configuration to take effect, even if the PPMU is already sourcing.

When forcing voltage by setting the [niDigital_PPMU_ConfigureOutputFunction](group____root__ni_digital__functions__ppmu__configuration_1ga9bbbaabd50b857dc9aa21c90853711aa.html) function to **NIDIGITAL_VAL_DC_VOLTAGE**, the current sourced or sunk is moderated by the specified current limit range. Select the smallest current range that meets the expected current requirements of the DUT.

If the current required by the DUT exceeds the selected current limit range, the voltage output may not meet the specified voltage level. Choose a larger current limit range if needed.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelList | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| range | [in] | ViReal64 | Current range, in amps, to use when forcing a voltage from the PPMU to a DUT. |

#### Returns

Reports the status of the operation.

Parent topic:

DC Voltage

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__sequencer__flag.html language=enus -->
## TOPIC 00095: Sequencer Flag

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__sequencer__flag.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__sequencer__flag.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_ReadSequencerFlagReads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program. niDigital_WriteSequencerFlagWrites the state of a pattern sequencer flag. Use pa

### Sequencer Flag

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_ReadSequencerFlag | Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program. |
| niDigital_WriteSequencerFlag | Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program. |
| niDigital_WriteSequencerFlagSynchronized | Writes a Boolean value to the pattern sequencer flag for synchronized digital pattern instruments. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime program. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__sequencer__register.html language=enus -->
## TOPIC 00096: Sequencer Register

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__sequencer__register.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__sequencer__register.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_ReadSequencerRegisterReads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this function to read a register modified by

### Sequencer Register

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_ReadSequencerRegister | Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this function to read a register modified by the write_reg opcode during a pattern burst. |
| niDigital_WriteSequencerRegister | Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__sort__results.html language=enus -->
## TOPIC 00097: Sort Results

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__sort__results.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__sort__results.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_GetPinResultsPinInformationReturns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. niDigital_GetSiteResultsSiteNumbersReturns the site numbers that correspond to per-site data rea

### Sort Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_GetPinResultsPinInformation | Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. |
| niDigital_GetSiteResultsSiteNumbers | Returns the site numbers that correspond to per-site data read from the digital pattern instrument. |
| niDigital_SortPinResultsBySiteViInt64 | Organizes data read from multiple digital pattern instruments by grouping the data by site number. |
| niDigital_SortPinResultsBySiteViReal64 | Organizes data read from multiple digital pattern instruments by grouping the data by site number. |
| niDigital_SortPinResultsBySiteViUInt8 | Organizes data read from multiple digital pattern instruments by grouping the data by site number. |
| niDigital_SortSiteResultsViBoolean | Orders site data read from multiple instruments to match the siteList you specify and combines data from instruments mapped to the same site. |
| niDigital_SortSiteResultsViUInt32Waveform | Orders site data read from multiple instruments to match the siteList you specify and combines data from instruments mapped to the same site. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__sort__results_1ga062f65a14dae37e5d05e80436cb9bdde.html language=enus -->
## TOPIC 00098: niDigital_GetPinResultsPinInformation

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__sort__results_1ga062f65a14dae37e5d05e80436cb9bdde.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__sort__results_1ga062f65a14dae37e5d05e80436cb9bdde.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. SyntaxViStatus _VI_FUNC niDigital_GetPinResultsPinInformation(ViSession vi, ViConstString channelList, ViInt32 bufferSize, ViInt32 pinIndexes[], ViInt32 siteNumbers[], ViI

### niDigital_GetPinResultsPinInformation

Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument.

#### Syntax

ViStatus _VI_FUNC niDigital_GetPinResultsPinInformation(ViSession vi, ViConstString channelList, ViInt32 bufferSize, ViInt32 pinIndexes[], ViInt32 siteNumbers[], ViInt32 channelIndexes[], ViInt32 *actualNumValues)

#### Remarks

The function returns pin information in the same order as values read using the [niDigital_ReadStatic](group____root__ni_digital__functions__static__io_1ga63b89932df489394341c0cbe99c074e9.html) function, [niDigital_PPMU_Measure](group____root__ni_digital__functions__ppmu__action_1ga76923e247e169fc5960454f8935aa2b6.html) function, and [niDigital_GetFailCount](group____root__ni_digital__functions__pattern__results_1ga63ab6243788d36aeb03fd02dd76b96a1.html) function. Use this function to match values the previously listed functions return with pins, sites, and instrument channels.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| channelList | [in] | ViConstString | List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.Pin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form siteN/pinName, where N is the site number. This function ignores pins that are not mapped to the digital pattern instrument.Specify channel names using the form PXI1Slot3/0,2-3 or PXI1Slot3/0,PXI1Slot3/2-3, where PXI1Slot3 is the instrument resource name and 0, 2, 3 are channel names. To specify channels from multiple instruments, use the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3. The instruments must be in the same chassis. |
| bufferSize | [in] | ViInt32 | The number of elements in the arrays you specify for pinIndexes, siteNumbers, and channelIndexes, if they are not NULL. To determine the size of the buffer to allocate for the arrays, pass a value of 0 to the bufferSize parameter and a value of VI_NULL to the array parameters. In this case, the value returned by the actualNumValues parameter is the size of the arrays necessary to hold the output values. |
| pinIndexes | [out] | ViInt32[] | The returned index of the pins corresponding to data read from the digital pattern instrument using the specified channelList. If you do not want to use this parameter, pass VI_NULL.Call niDigital_GetPinName to get the name of the pin associated with an index. |
| siteNumbers | [out] | ViInt32[] | The returned site numbers that correspond to data read from the digital pattern instrument using the specified channelList. If you do not want to use this parameter, pass VI_NULL. |
| channelIndexes | [out] | ViInt32[] | The returned index of channels corresponding to data read from the digital pattern instrument using the specified channelList. If you do not want to use this parameter, pass VI_NULL.Call niDigital_GetChannelName to get the name of the channel associated with an index. Channel indexes are one-based. |
| actualNumValues | [out] | ViInt32 * | The number of values written to the output arrays. This function always writes the same number of values to all output arrays, if they are not set to VI_NULL. |

#### Returns

Reports the status of the operation.

Parent topic:

Sort Results

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__sort__results_1ga1d4267f11bea58c943e5ebd5d91e15cc.html language=enus -->
## TOPIC 00099: niDigital_SortPinResultsBySiteViUInt8

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__sort__results_1ga1d4267f11bea58c943e5ebd5d91e15cc.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__sort__results_1ga1d4267f11bea58c943e5ebd5d91e15cc.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organizes data read from multiple digital pattern instruments by grouping the data by site number. SyntaxViStatus _VI_FUNC niDigital_SortPinResultsBySiteViUInt8(ViInt32 sessionCount, ViSession sessions[], ViConstString channelList, ViInt32 numResults, ViUInt8 results[], ViInt32 pinIndexes[], ViInt32

### niDigital_SortPinResultsBySiteViUInt8

Organizes data read from multiple digital pattern instruments by grouping the data by site number.

#### Syntax

ViStatus _VI_FUNC niDigital_SortPinResultsBySiteViUInt8(ViInt32 sessionCount, ViSession sessions[], ViConstString channelList, ViInt32 numResults, ViUInt8 results[], ViInt32 pinIndexes[], ViInt32 siteNumbers[])

#### Remarks

To use this function, allocate an array large enough to hold the data to read from all instruments. Read data from each instrument using the same list of pins and pin groups for the **channelList** parameter, appending each instrument's data in the allocated array. Each instrument returns data only for the pins that are mapped to its channels. Pass the data array and the same channel list as parameters to this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| sessionCount | [in] | ViInt32 | Number of sessions in the sessions array. |
| sessions | [in] | ViSession[] | Instrument sessions obtained from the niDigital_InitWithOptions function. |
| channelList | [in] | ViConstString | The specified channelList you use to read data in the results array. This function requires that the channelList contain only pin and pin group names. |
| numResults | [in] | ViInt32 | Number of values in the results array. |
| results | [in] | ViUInt8[] | The specified data read from the digital pattern instruments, appended into an array. This function sorts the results in-place in the results array so that they are ordered according to the specified channelList and in increasing site order. |
| pinIndexes | [out] | ViInt32[] | The returned pin indexes corresponding to the data returned in the results array. If non-NULL, this array must be of the same size as the results array. |
| siteNumbers | [out] | ViInt32[] | The returned site numbers corresponding to the data returned in the results array. If non-NULL, this array must be of the same size as the results array. |

#### Returns

Reports the status of the operation.

Parent topic:

Sort Results

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__sort__results_1gaeed9edb31bb2fe5886c922e60c3da28f.html language=enus -->
## TOPIC 00100: niDigital_GetSiteResultsSiteNumbers

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__sort__results_1gaeed9edb31bb2fe5886c922e60c3da28f.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__sort__results_1gaeed9edb31bb2fe5886c922e60c3da28f.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the site numbers that correspond to per-site data read from the digital pattern instrument. SyntaxViStatus _VI_FUNC niDigital_GetSiteResultsSiteNumbers(ViSession vi, ViConstString siteList, ViInt32 siteResultType, ViInt32 siteNumbersBufferSize, ViInt32 siteNumbers[], ViInt32 *actualNumSiteNu

### niDigital_GetSiteResultsSiteNumbers

Returns the site numbers that correspond to per-site data read from the digital pattern instrument.

#### Syntax

ViStatus _VI_FUNC niDigital_GetSiteResultsSiteNumbers(ViSession vi, ViConstString siteList, ViInt32 siteResultType, ViInt32 siteNumbersBufferSize, ViInt32 siteNumbers[], ViInt32 *actualNumSiteNumbers)

#### Remarks

The function returns site numbers in the same order as values read using the [niDigital_GetSitePassFail](group____root__ni_digital__functions__pattern__results_1ga40ffa595ce28c71e9220ed89904225e1.html) and [niDigital_FetchCaptureWaveformU32](group____root__ni_digital__functions__capture__memory_1ga4efdf2a8c2fb030f242ec6a313807e75.html) functions. Use this function to match values the previously listed functions return with site numbers.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| siteList | [in] | ViConstString | Site numbers listed as a comma-delimited list of strings of form siteN, where N is the site number. |
| siteResultType | [in] | ViInt32 | The type of data specified in the results array.Defined Values:NameValueDescriptionNIDIGITAL_VAL_PASS_FAIL3300 (0xce4)Pass/fail site result.NIDIGITAL_VAL_CAPTURE_WAVEFORM3301 (0xce5)Capture waveform site result. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_PASS_FAIL | 3300 (0xce4) | Pass/fail site result. |  |
| NIDIGITAL_VAL_CAPTURE_WAVEFORM | 3301 (0xce5) | Capture waveform site result. |  |
| siteNumbersBufferSize | [in] | ViInt32 | The number of elements in the ViInt32 array you specify for siteNumbers. To determine the size of the buffer to allocate for the siteNumbers array, pass a value of 0 to the siteNumbersBufferSize parameter and a value of VI_NULL to the siteNumbers parameter. In this case, the value returned by the actualNumSiteNumbers parameter is the size of the array necessary to hold the site numbers. |
| siteNumbers | [out] | ViInt32[] | The returned array of site numbers that correspond to the values specified by siteResultType. |
| actualNumSiteNumbers | [out] | ViInt32 * | Number of sites written in the siteNumbers array. |

#### Returns

Reports the status of the operation.

Parent topic:

Sort Results

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__source__memory_1ga18b80da3ea71e9f7e8c8125312a56e86.html language=enus -->
## TOPIC 00101: niDigital_CreateSourceWaveformFromFileTDMS

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__source__memory_1ga18b80da3ea71e9f7e8c8125312a56e86.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__source__memory_1ga18b80da3ea71e9f7e8c8125312a56e86.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file. SyntaxViStatus _VI_FUNC niDigital_CreateSourceWaveformFromFileTDMS(ViSession vi, ViConstString waveformName, ViConstString wavefor

### niDigital_CreateSourceWaveformFromFileTDMS

Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.

#### Syntax

ViStatus _VI_FUNC niDigital_CreateSourceWaveformFromFileTDMS(ViSession vi, ViConstString waveformName, ViConstString waveformFilePath, ViBoolean writeWaveformData)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| waveformName | [in] | ViConstString | The waveform name you want to use from the file. You must specify waveformName if the file contains multiple waveforms. Use the waveformName with the source_start opcode in your pattern. |
| waveformFilePath | [in] | ViConstString | Absolute file path to the load source waveform file (.tdms). |
| writeWaveformData | [in] | ViBoolean | A Boolean that writes waveform data to source memory if True and the waveform data is in the file. |

#### Returns

Reports the status of the operation.

Parent topic:

Source Memory

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__source__memory_1gad03c1739a5ed68bbd23911f6bcbc1cee.html language=enus -->
## TOPIC 00102: niDigital_WriteSourceWaveformSiteUniqueU32

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__source__memory_1gad03c1739a5ed68bbd23911f6bcbc1cee.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__source__memory_1gad03c1739a5ed68bbd23911f6bcbc1cee.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one waveform per site. Use this write function if you set the parameter of the create source waveform function to Site Unique. SyntaxViStatus _VI_FUNC niDigital_WriteSourceWaveformSiteUniqueU32(ViSession vi, ViConstString siteList, ViConstString waveformName, ViInt32 numWaveforms, ViInt32 sam

### niDigital_WriteSourceWaveformSiteUniqueU32

Writes one waveform per site. Use this write function if you set the parameter of the create source waveform function to Site Unique.

#### Syntax

ViStatus _VI_FUNC niDigital_WriteSourceWaveformSiteUniqueU32(ViSession vi, ViConstString siteList, ViConstString waveformName, ViInt32 numWaveforms, ViInt32 samplesPerWaveform, ViUInt32 waveformData[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| siteList | [in] | ViConstString | Site numbers listed as a comma-delimited list of strings of form siteN, where N is the site number. |
| waveformName | [in] | ViConstString | The name to assign to the waveform. Use the waveformName with source_start opcode in your pattern. |
| numWaveforms | [in] | ViInt32 | Number of waveforms. |
| samplesPerWaveform | [in] | ViInt32 | Number of samples per waveform. |
| waveformData | [in] | ViUInt32[] | An array of samples to use as source data. Data for each site must be appended sequentially in the array (non-interleaved). |

#### Returns

Reports the status of the operation.

Parent topic:

Source Memory

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__static__io.html language=enus -->
## TOPIC 00103: Static I/O

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__static__io.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__static__io.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_ReadStaticReads the current state of comparators for pins you specify in the channelList parameter. If there are uncommitted changes to levels or the termination mode, this function commits the changes to the pins. niDigital_WriteStaticWrites a static

### Static I/O

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_ReadStatic | Reads the current state of comparators for pins you specify in the channelList parameter. If there are uncommitted changes to levels or the termination mode, this function commits the changes to the pins. |
| niDigital_WriteStatic | Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this function. If there are uncommitted changes to levels or the termination mode, this function commits the changes to the pins. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__triggers__and__events_1ga587804d11344bd7780372f2970ad098a.html language=enus -->
## TOPIC 00104: niDigital_ConfigureDigitalEdgeRIOTrigger

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__triggers__and__events_1ga587804d11344bd7780372f2970ad098a.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__triggers__and__events_1ga587804d11344bd7780372f2970ad098a.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a RIO trigger instance to trigger on an incoming digital edge and routes the specified signal source to the instrument. SyntaxViStatus _VI_FUNC niDigital_ConfigureDigitalEdgeRIOTrigger(ViSession vi, ViConstString triggerIdentifier, ViConstString source, ViInt32 edge)ParametersNameDirectio

### niDigital_ConfigureDigitalEdgeRIOTrigger

Configures a RIO trigger instance to trigger on an incoming digital edge and routes the specified signal source to the instrument.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigureDigitalEdgeRIOTrigger(ViSession vi, ViConstString triggerIdentifier, ViConstString source, ViInt32 edge)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| triggerIdentifier | [in] | ViConstString | Specifies which instance of the RIO trigger you want to override.Defined Values:NameValueDescriptionNIDIGITAL_VAL_RIO_TRIGGER0"RIOTrigger0"RIOTrigger0NIDIGITAL_VAL_RIO_TRIGGER1"RIOTrigger1"RIOTrigger1NIDIGITAL_VAL_RIO_TRIGGER2"RIOTrigger2"RIOTrigger2NIDIGITAL_VAL_RIO_TRIGGER3"RIOTrigger3"RIOTrigger3NIDIGITAL_VAL_RIO_TRIGGER4"RIOTrigger4"RIOTrigger4NIDIGITAL_VAL_RIO_TRIGGER5"RIOTrigger5"RIOTrigger5NIDIGITAL_VAL_RIO_TRIGGER6"RIOTrigger6"RIOTrigger6NIDIGITAL_VAL_RIO_TRIGGER7"RIOTrigger7"RIOTrigger7 |
| Name | Value | Description |  |
| NIDIGITAL_VAL_RIO_TRIGGER0 | "RIOTrigger0" | RIOTrigger0 |  |
| NIDIGITAL_VAL_RIO_TRIGGER1 | "RIOTrigger1" | RIOTrigger1 |  |
| NIDIGITAL_VAL_RIO_TRIGGER2 | "RIOTrigger2" | RIOTrigger2 |  |
| NIDIGITAL_VAL_RIO_TRIGGER3 | "RIOTrigger3" | RIOTrigger3 |  |
| NIDIGITAL_VAL_RIO_TRIGGER4 | "RIOTrigger4" | RIOTrigger4 |  |
| NIDIGITAL_VAL_RIO_TRIGGER5 | "RIOTrigger5" | RIOTrigger5 |  |
| NIDIGITAL_VAL_RIO_TRIGGER6 | "RIOTrigger6" | RIOTrigger6 |  |
| NIDIGITAL_VAL_RIO_TRIGGER7 | "RIOTrigger7" | RIOTrigger7 |  |
| source | [in] | ViConstString | The string identifier for a supported trigger source terminal to route into the instrument for the RIO trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. |
| edge | [in] | ViInt32 | Specifies the polarity of the incoming trigger signal that will assert this RIO trigger instance.Defined Values:NameValueDescriptionNIDIGITAL_VAL_RISING_EDGE1800 (0x708)Asserts the trigger when the signal transitions from low level to high level.NIDIGITAL_VAL_FALLING_EDGE1801 (0x709)Asserts the trigger when the signal transitions from high level to low level. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_RISING_EDGE | 1800 (0x708) | Asserts the trigger when the signal transitions from low level to high level. |  |
| NIDIGITAL_VAL_FALLING_EDGE | 1801 (0x709) | Asserts the trigger when the signal transitions from high level to low level. |  |

#### Returns

Reports the status of the operation.

Parent topic:

Triggers and Events

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__triggers__and__events_1ga9b98374f1e68357c0c4d6134b3656e65.html language=enus -->
## TOPIC 00105: niDigital_ExportSignal

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__triggers__and__events_1ga9b98374f1e68357c0c4d6134b3656e65.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__triggers__and__events_1ga9b98374f1e68357c0c4d6134b3656e65.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes trigger and event signals to the outputTerminal you specify. SyntaxViStatus _VI_FUNC niDigital_ExportSignal(ViSession vi, ViInt32 signal, ViConstString signalIdentifier, ViConstString outputTerminal)ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigital_init

### niDigital_ExportSignal

Routes trigger and event signals to the **outputTerminal** you specify.

#### Syntax

ViStatus _VI_FUNC niDigital_ExportSignal(ViSession vi, ViInt32 signal, ViConstString signalIdentifier, ViConstString outputTerminal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| signal | [in] | ViInt32 | The type of signal to export from a digital pattern instrument.Defined Values:NameValueDescriptionNIDIGITAL_VAL_START_TRIGGER2000 (0x7d0)NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2001 (0x7d1)NIDIGITAL_VAL_PATTERN_OPCODE_EVENT2002 (0x7d2)NIDIGITAL_VAL_REF_CLOCK2003 (0x7d3)NIDIGITAL_VAL_RIO_EVENT2004 (0x7d4) |
| Name | Value | Description |  |
| NIDIGITAL_VAL_START_TRIGGER | 2000 (0x7d0) |  |  |
| NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER | 2001 (0x7d1) |  |  |
| NIDIGITAL_VAL_PATTERN_OPCODE_EVENT | 2002 (0x7d2) |  |  |
| NIDIGITAL_VAL_REF_CLOCK | 2003 (0x7d3) |  |  |
| NIDIGITAL_VAL_RIO_EVENT | 2004 (0x7d4) |  |  |
| signalIdentifier | [in] | ViConstString | Instance of the selected signals to export.VI_NULL ("")NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER0 ("conditionalJumpTrigger0")NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER1 ("conditionalJumpTrigger1")NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2 ("conditionalJumpTrigger2")NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER3 ("conditionalJumpTrigger3")NIDIGITAL_VAL_PATTERN_OPCODE_EVENT0 ("patternOpcodeEvent0")NIDIGITAL_VAL_PATTERN_OPCODE_EVENT1 ("patternOpcodeEvent1")NIDIGITAL_VAL_PATTERN_OPCODE_EVENT2 ("patternOpcodeEvent2")NIDIGITAL_VAL_PATTERN_OPCODE_EVENT3 ("patternOpcodeEvent3")NIDIGITAL_VAL_RIO_EVENT0 ("RIOEvent0")NIDIGITAL_VAL_RIO_EVENT1 ("RIOEvent1")NIDIGITAL_VAL_RIO_EVENT2 ("RIOEvent2")NIDIGITAL_VAL_RIO_EVENT3 ("RIOEvent3")NIDIGITAL_VAL_RIO_EVENT4 ("RIOEvent4")NIDIGITAL_VAL_RIO_EVENT5 ("RIOEvent5")NIDIGITAL_VAL_RIO_EVENT6 ("RIOEvent6")NIDIGITAL_VAL_RIO_EVENT7 ("RIOEvent7") |
| outputTerminal | [in] | ViConstString | Parameter that configures properties depending on the type of signal you select in the signalIdentifier parameter.Defined Values:NameValueDescriptionNIDIGITAL_VAL_DO_NOT_EXPORT_STR""Signal will not be exported.NIDIGITAL_VAL_PXI_TRIG0_STR"PXI_Trig0"Specifies PXI trigger line 0.NIDIGITAL_VAL_PXI_TRIG1_STR"PXI_Trig1"Specifies PXI trigger line 1.NIDIGITAL_VAL_PXI_TRIG2_STR"PXI_Trig2"Specifies PXI trigger line 2.NIDIGITAL_VAL_PXI_TRIG3_STR"PXI_Trig3"Specifies PXI trigger line 3.NIDIGITAL_VAL_PXI_TRIG4_STR"PXI_Trig4"Specifies PXI trigger line 4.NIDIGITAL_VAL_PXI_TRIG5_STR"PXI_Trig5"Specifies PXI trigger line 5.NIDIGITAL_VAL_PXI_TRIG6_STR"PXI_Trig6"Specifies PXI trigger line 6.NIDIGITAL_VAL_PXI_TRIG7_STR"PXI_Trig7"Specifies PXI trigger line 7. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_DO_NOT_EXPORT_STR | "" | Signal will not be exported. |  |
| NIDIGITAL_VAL_PXI_TRIG0_STR | "PXI_Trig0" | Specifies PXI trigger line 0. |  |
| NIDIGITAL_VAL_PXI_TRIG1_STR | "PXI_Trig1" | Specifies PXI trigger line 1. |  |
| NIDIGITAL_VAL_PXI_TRIG2_STR | "PXI_Trig2" | Specifies PXI trigger line 2. |  |
| NIDIGITAL_VAL_PXI_TRIG3_STR | "PXI_Trig3" | Specifies PXI trigger line 3. |  |
| NIDIGITAL_VAL_PXI_TRIG4_STR | "PXI_Trig4" | Specifies PXI trigger line 4. |  |
| NIDIGITAL_VAL_PXI_TRIG5_STR | "PXI_Trig5" | Specifies PXI trigger line 5. |  |
| NIDIGITAL_VAL_PXI_TRIG6_STR | "PXI_Trig6" | Specifies PXI trigger line 6. |  |
| NIDIGITAL_VAL_PXI_TRIG7_STR | "PXI_Trig7" | Specifies PXI trigger line 7. |  |

#### Returns

Reports the status of the operation.

Parent topic:

Triggers and Events

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__triggers__and__events_1gabc755885dd1fdedc6389af5af9341b9f.html language=enus -->
## TOPIC 00106: niDigital_SendSoftwareEdgeTrigger

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__triggers__and__events_1gabc755885dd1fdedc6389af5af9341b9f.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__triggers__and__events_1gabc755885dd1fdedc6389af5af9341b9f.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this function as a software override. SyntaxViStatus _VI_FUNC niDigital_SendSoftwareEdgeTrigger(ViSession vi, ViInt32 trigger, ViConstString triggerIdentifier)ParametersNameDirectionTyp

### niDigital_SendSoftwareEdgeTrigger

Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this function as a software override.

#### Syntax

ViStatus _VI_FUNC niDigital_SendSoftwareEdgeTrigger(ViSession vi, ViInt32 trigger, ViConstString triggerIdentifier)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| trigger | [in] | ViInt32 | The trigger you want to override.Defined Values:NameValueDescriptionNIDIGITAL_VAL_START_TRIGGER2000 (0x7d0)Overrides the start trigger.NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2001 (0x7d1)Specifies to route a conditional jump trigger.Note: You must specify an empty string in the triggerIdentifier parameter, to override the start trigger. You must specify a conditional jump trigger instance in the triggerIdentifier parameter, to route a conditional jump trigger. |
| Name | Value | Description |  |
| NIDIGITAL_VAL_START_TRIGGER | 2000 (0x7d0) | Overrides the start trigger. |  |
| NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER | 2001 (0x7d1) | Specifies to route a conditional jump trigger. |  |
| triggerIdentifier | [in] | ViConstString | Specifies which instance of the conditional jump trigger you want to override.VI_NULL ("")NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER0 ("conditionalJumpTrigger0")NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER1 ("conditionalJumpTrigger1")NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER2 ("conditionalJumpTrigger2")NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER3 ("conditionalJumpTrigger3") |

#### Returns

Reports the status of the operation.

Parent topic:

Triggers and Events

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__triggers__and__events_1gadbd322b670febe92e050399487ccb274.html language=enus -->
## TOPIC 00107: niDigital_ConfigureDigitalEdgeStartTrigger

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__triggers__and__events_1gadbd322b670febe92e050399487ccb274.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__triggers__and__events_1gadbd322b670febe92e050399487ccb274.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Start trigger for digital edge triggering. The digital pattern instrument responds to the trigger on a physical PXI chassis backplane trigger line and waits for this trigger after you call the niDigital_Initiate function or the niDigital_BurstPattern function. The pattern does not bur

### niDigital_ConfigureDigitalEdgeStartTrigger

Configures the Start trigger for digital edge triggering. The digital pattern instrument responds to the trigger on a physical PXI chassis backplane trigger line and waits for this trigger after you call the [niDigital_Initiate](group____root__ni_digital__functions__pattern__action__low__level__action_1ga992e80f747168211cd44d3ca09309f6f.html) function or the [niDigital_BurstPattern](group____root__ni_digital__functions__pattern__action_1ga0e9a6597044b41afae031dcd59e32330.html) function. The pattern does not burst until it receives this trigger.

#### Syntax

ViStatus _VI_FUNC niDigital_ConfigureDigitalEdgeStartTrigger(ViSession vi, ViConstString source, ViInt32 edge)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| source | [in] | ViConstString | The string identifier for a supported trigger source terminal to route into the instrument for the conditional jump trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. |
| edge | [in] | ViInt32 | Specifies the polarity of the incoming trigger signal that will assert the Start trigger. |

#### Returns

Reports the status of the operation.

Parent topic:

Triggers and Events

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__utility.html language=enus -->
## TOPIC 00108: Utility

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__utility.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniDigital_ResetDeviceReturns a digital pattern instrument to a known state. niDigital_resetResets a digital pattern instrument to a known state. niDigital_self_testReturns self test results from a digital pattern instrument. This test requires several minutes to

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niDigital_ResetDevice | Returns a digital pattern instrument to a known state. |
| niDigital_reset | Resets a digital pattern instrument to a known state. |
| niDigital_self_test | Returns self test results from a digital pattern instrument. This test requires several minutes to execute. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__utility_1ga278956f2629dcbc7f7b2125170feef46.html language=enus -->
## TOPIC 00109: niDigital_self_test

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__utility_1ga278956f2629dcbc7f7b2125170feef46.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__utility_1ga278956f2629dcbc7f7b2125170feef46.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns self test results from a digital pattern instrument. This test requires several minutes to execute. SyntaxViStatus _VI_FUNC niDigital_self_test(ViSession vi, ViInt16 *testResult, ViChar testMessage[2048])ParametersNameDirectionTypeDescriptionvi[in]ViSessionThe instrument session the niDigita

### niDigital_self_test

Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

#### Syntax

ViStatus _VI_FUNC niDigital_self_test(ViSession vi, ViInt16 *testResult, ViChar testMessage[2048])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |
| testResult | [out] | ViInt16 * | A parameter that indicates if the self test passed (0) or failed (!=0). |
| testMessage | [out] | ViChar[2048] | The returned self test status message. The array must contain at least 256 characters. |

#### Returns

Reports the status of the operation.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__utility_1ga3b85968802e1434b912ed112f8614f7d.html language=enus -->
## TOPIC 00110: niDigital_reset

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__utility_1ga3b85968802e1434b912ed112f8614f7d.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__utility_1ga3b85968802e1434b912ed112f8614f7d.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a digital pattern instrument to a known state. SyntaxViStatus _VI_FUNC niDigital_reset(ViSession vi)RemarksThis function performs the following actions:Aborts pattern execution.Clears pin maps, time sets, source and capture waveforms, and patterns.Resets all properties to default values, incl

### niDigital_reset

Resets a digital pattern instrument to a known state.

#### Syntax

ViStatus _VI_FUNC niDigital_reset(ViSession vi)

#### Remarks

This function performs the following actions:

- Aborts pattern execution.
- Clears pin maps, time sets, source and capture waveforms, and patterns.
- Resets all properties to default values, including the niDigital Selected Function property that is set to Disconnect, causing the I/O switches to open.
- Stops exporting all external signals and events.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group____root__ni_digital__functions__utility_1ga7c5219942a20018e1d90d63d8ab151d5.html language=enus -->
## TOPIC 00111: niDigital_ResetDevice

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group____root__ni_digital__functions__utility_1ga7c5219942a20018e1d90d63d8ab151d5.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group____root__ni_digital__functions__utility_1ga7c5219942a20018e1d90d63d8ab151d5.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a digital pattern instrument to a known state. SyntaxViStatus _VI_FUNC niDigital_ResetDevice(ViSession vi)RemarksThis function performs the following actions:Aborts pattern execution.Clears pin maps, time sets, source and capture waveforms, and patterns.Resets all properties to default value

### niDigital_ResetDevice

Returns a digital pattern instrument to a known state.

#### Syntax

ViStatus _VI_FUNC niDigital_ResetDevice(ViSession vi)

#### Remarks

This function performs the following actions:

- Aborts pattern execution.
- Clears pin maps, time sets, source and capture waveforms, and patterns.
- Resets all properties to default values, including the niDigital Selected Function property that is set to Disconnect, causing the I/O switches to open.
- Stops export of all external signals and events.
- Clears over-temperature and over-power conditions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| vi | [in] | ViSession | The instrument session the niDigital_init or niDigital_InitWithOptions function returns. |

#### Returns

Reports the status of the operation.

Parent topic:

Utility

<!--NI_TOPIC bundle=ni-digital-pattern-c-api-ref path=group__root__ni_digital.html language=enus -->
## TOPIC 00112: niDigital.h

- bundle_id: `ni-digital-pattern-c-api-ref`
- source_path: `group__root__ni_digital.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-c-api-ref/raw/resource/enus/group__root__ni_digital.html
- document_id: `ni-digital-pattern-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niDigital.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
