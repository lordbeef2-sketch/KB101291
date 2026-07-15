# NI DOCUMENT BUNDLE: diadem

<!--NI_BUNDLE_CHUNK bundle=diadem start=1501 end=1610 -->
<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkrmode.htm language=enus -->
## TOPIC 01501: Variable: PkMode

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkrmode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkrmode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkMode

Variable: PkMode

Specifies in packet processing how DIAdem extracts data from incoming data packets.

| Definition | PkMode, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Transmit quantity A, ignore quantity B 2 Ignore quantity A, transmit quantity B 3 Transmit when control input HIGH 4 Cut when control input HIGH |
| Index | Meaning |
| 1 | Transmit quantity A, ignore quantity B |
| 2 | Ignore quantity A, transmit quantity B |
| 3 | Transmit when control input HIGH |
| 4 | Cut when control input HIGH |

|  | Note Do not assign values 3 or 4 to the PkMode variable if you have started a measurement. These settings block the packet processing, because DIAdem cannot create a control input during a measurement. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkMode = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Ignore Block](../../dlgdacpp/dac_packet_dlg_handling/hb_xa_abschnitt.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkscaledimvs.htm language=enus -->
## TOPIC 01502: Variable: PkScaleDimV

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkscaledimvs.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkscaledimvs.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkScaleDimV

Variable: PkScaleDimV

Specifies in packet processing the unit of the physical output value of a linear scale.

| Definition | PkScaleDimV, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Without change 2 Seconds 3 Milliseconds 4 Hours 5 Minutes 6 Hertz 7 Kilohertz 8 Volt 9 Millivolt 10 Kilovolt |
| Index | Meaning |
| 1 | Without change |
| 2 | Seconds |
| 3 | Milliseconds |
| 4 | Hours |
| 5 | Minutes |
| 6 | Hertz |
| 7 | Kilohertz |
| 8 | Volt |
| 9 | Millivolt |
| 10 | Kilovolt |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkScaleDimV = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[2-Point Scaling](../../dlgdacpp/dac_packet_dlg_handling/hb_2_punkt_skalierung.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkskipval.htm language=enus -->
## TOPIC 01503: Variable: PkSkipVal

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkskipval.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkskipval.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkSkipVal

Variable: PkSkipVal

Specifies in packet processing the number of values that DIAdem rejects at the start of a measurement, when creating sections.

| Definition | PkSkipVal, Word variable |
| --- | --- |
|  | 0 <= PkSkipVal <= 65535 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkSkipVal = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Ignore Block](../../dlgdacpp/dac_packet_dlg_handling/hb_xa_abschnitt.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkslopetype.htm language=enus -->
## TOPIC 01504: Variable: PkSlopeType

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkslopetype.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkslopetype.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkSlopeType

Variable: PkSlopeType

Specifies in packet processing the type of slope condition to be activated.

| Definition | PkSlopeType, LongInteger variable |
| --- | --- |
|  | Selection term from the following list: Index Meaning 0 Increasing 1 Decreasing 2 Increasing or decreasing |
| Index | Meaning |
| 0 | Increasing |
| 1 | Decreasing |
| 2 | Increasing or decreasing |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkSlopeType = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Trigger Finder](../../dlgdacpp/dac_packet_dlg/hb_trigsuch.htm) | [Trigger](../../dlgdacpp/dac_packet_dlg_handling/hb_trigger.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkslopetyper.htm language=enus -->
## TOPIC 01505: Variable: PkSlopeTypeR

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkslopetyper.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkslopetyper.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkSlopeTypeR

Variable: PkSlopeTypeR

Specifies in packet processing the type of retrigger slope condition to be activated.

| Definition | PkSlopeTypeR, Enumeration variable |
| --- | --- |
|  | Selection term from the following list: Index Meaning 0 Increasing 1 Decreasing 2 Increasing or decreasing |
| Index | Meaning |
| 0 | Increasing |
| 1 | Decreasing |
| 2 | Increasing or decreasing |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkSlopeTypeR = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Trigger Finder](../../dlgdacpp/dac_packet_dlg/hb_trigsuch.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pksoutmode.htm language=enus -->
## TOPIC 01506: Variable: PkOutMode

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pksoutmode.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pksoutmode.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkOutMode

Variable: PkOutMode

Specifies in packet processing whether DIAdem outputs all statistical characteristic values in one multi-channel data packet to one data output or in several one-channel data packets to various data outputs in the block diagram.

| Definition | PkOutMode, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 All statistical values to one output 2 One output for each statistical value |
| Index | Meaning |
| 1 | All statistical values to one output |
| 2 | One output for each statistical value |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkOutMode = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Statistics/Characteristic Statistical Values](../../dlgdacpp/dac_packet_dlg_math/hb_statistikm.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkstdabw.htm language=enus -->
## TOPIC 01507: Variable: PkStdAbw

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkstdabw.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkstdabw.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkStdAbw

Variable: PkStdAbw

Specifies in packet processing whether DIAdem calculates the standard deviation as the statistical characteristic value.

| Definition | PkStdAbw, Integer variable |
| --- | --- |
|  | 0 or 1 |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkStdAbw = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Statistics/Characteristic Statistical Values](../../dlgdacpp/dac_packet_dlg_math/hb_statistikm.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkstop.htm language=enus -->
## TOPIC 01508: Variable: PkStop

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkstop.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkstop.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkStop

Variable: PkStop

Specifies in packet processing the stop string to deinitialize an external device over the serial interface.

| Definition | PkStop, String variable |
| --- | --- |
|  | Maximum 80 characters |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkStop = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pksumall.htm language=enus -->
## TOPIC 01509: Variable: PkSumAll

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pksumall.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pksumall.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkSumAll

Variable: PkSumAll

Specifies in packet processing whether DIAdem calculates the sum of all values that have arrived since the start of the measurement.

| Definition | PkSumAll, Integer variable |
| --- | --- |
|  | 0 or 1 |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkSumAll = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Statistics/Characteristic Statistical Values](../../dlgdacpp/dac_packet_dlg_math/hb_statistikm.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pksumblock.htm language=enus -->
## TOPIC 01510: Variable: PkSumBlock

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pksumblock.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pksumblock.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkSumBlock

Variable: PkSumBlock

Specifies in packet processing whether DIAdem calculates the sum of the measured values in one data packet.

| Definition | PkSumBlock, Integer variable |
| --- | --- |
|  | 0 or 1 |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkSumBlock = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Statistics/Characteristic Statistical Values](../../dlgdacpp/dac_packet_dlg_math/hb_statistikm.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkswitch.htm language=enus -->
## TOPIC 01511: Variable: PkSwitch

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkswitch.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkswitch.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkSwitch

Variable: PkSwitch

Specifies in packet processing how the relay switch works.

| Definition | PkSwitch, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Switch on/off 2 Toggle switch |
| Index | Meaning |
| 1 | Switch on/off |
| 2 | Toggle switch |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkSwitch = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pktarget.htm language=enus -->
## TOPIC 01512: Variable: PkTarget

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pktarget.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pktarget.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkTarget

Variable: PkTarget

Specifies in packet processing that DIAdem prints out the protocol lists.

| Definition | PkTarget, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 Off 2 At LPT1 3 At LPT2 4 At COM1 5 At COM2 6 At COM3 7 At COM4 |
| Index | Meaning |
| 1 | Off |
| 2 | At LPT1 |
| 3 | At LPT2 |
| 4 | At COM1 |
| 5 | At COM2 |
| 6 | At COM3 |
| 7 | At COM4 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkTarget = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkthreshold.htm language=enus -->
## TOPIC 01513: Variable: PkThreshold

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkthreshold.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkthreshold.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkThreshold

Variable: PkThreshold

Specifies in packet processing the threshold value of a slope condition.

| Definition | PkThreshold, Integer variable |
| --- | --- |
|  | 0 < PkThreshold < ∞ |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkThreshold = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Trigger Finder](../../dlgdacpp/dac_packet_dlg/hb_trigsuch.htm) | [Trigger](../../dlgdacpp/dac_packet_dlg_handling/hb_trigger.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkthresholdr.htm language=enus -->
## TOPIC 01514: Variable: PkThresholdR

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkthresholdr.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkthresholdr.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkThresholdR

Variable: PkThresholdR

Specifies in packet processing the threshold value of the retrigger slope.

| Definition | PkThresholdR, Integer variable |
| --- | --- |
|  | 0 < PkThresholdR < ∞ |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkThresholdR = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Trigger Finder](../../dlgdacpp/dac_packet_dlg/hb_trigsuch.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pktimehold.htm language=enus -->
## TOPIC 01515: Variable: PkTimeHold

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pktimehold.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pktimehold.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkTimeHold

Variable: PkTimeHold

Specifies in packet processing the time in seconds that DIAdem deletes from the level calculation before a pause.

| Definition | PkTimeHold, Integer variable |
| --- | --- |
|  | 0 <= PkTimeHold < ∞ |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkTimeHold(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Level Calculation](../../dlgdacpp/dac_packet_dlg/hb_pegelber.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pktimetc.htm language=enus -->
## TOPIC 01516: Variable: PkTimeTc

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pktimetc.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pktimetc.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkTimeTc

Variable: PkTimeTc

Specifies in packet processing the time constant for calculating the root mean square of a level calculation.

| Definition | PkTimeTc, Integer variable |
| --- | --- |
|  | Index Meaning 0 Slow[1000ms] 1 Fast[125ms] 2 Impulse[35ms] |
| Index | Meaning |
| 0 | Slow[1000ms] |
| 1 | Fast[125ms] |
| 2 | Impulse[35ms] |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkTimeTc = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Level Calculation](../../dlgdacpp/dac_packet_dlg/hb_pegelber.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pktimetx.htm language=enus -->
## TOPIC 01517: Variable: PkTimeTx

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pktimetx.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pktimetx.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkTimeTx

Variable: PkTimeTx

Specifies in packet processing a fixed time span in seconds in which DIAdem acquires the maximum level of the clock during a level calculation.

| Definition | PkTimeTx, Integer variable |
| --- | --- |
|  | Value Meaning 0 1s 1 3s 2 5s |
| Value | Meaning |
| 0 | 1s |
| 1 | 3s |
| 2 | 5s |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkTimeTx = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Level Calculation](../../dlgdacpp/dac_packet_dlg/hb_pegelber.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pktype.htm language=enus -->
## TOPIC 01518: Variable: PKType

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pktype.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pktype.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PKType

Variable: PKType

Specifies in packet processing the filter type of digital filters.

| Definition | PKType(i), String variablei = 1 ... 255 |
| --- | --- |
|  | Maximum 20 characters |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkType = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

The PkType variable can contain the following values:

| Index | Meaning |
| --- | --- |
| 1 | Lowpass |
| 2 | Highpass |
| 3 | Bandpass |
| 4 | Bandstop |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkupperlimr.htm language=enus -->
## TOPIC 01519: Variable: PkUpperLimR

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkupperlimr.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkupperlimr.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkUpperLimR

Variable: PkUpperLimR

Specifies in packet processing the top window limit of a retrigger.

| Definition | PkUpperLimR, Integer variable |
| --- | --- |
|  | PkUpperLimR » PkLowerLimR |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkUpperLimR = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Trigger Finder](../../dlgdacpp/dac_packet_dlg/hb_trigsuch.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkupwarnon.htm language=enus -->
## TOPIC 01520: Variable: PkUpWarnOn

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkupwarnon.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkupwarnon.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkUpWarnOn

Variable: PkUpWarnOn

Specifies in packet processing whether DIAdem displays the exceeding of the top warning limit in the voltmeter.

| Definition | PkUpWarnOn(i), Boolean variablei=1...Number of channels |
| --- | --- |
|  | 0 or 1 |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkUpWarnOn(i) = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Limit Values in the Voltmeter](../../dlgdacpp/dac_packet_voltmeter/pk_voltmeter_limits.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkxch1.htm language=enus -->
## TOPIC 01521: Variable: PkXCh

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkxch1.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkxch1.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkXCh

Variable: PkXCh

Specifies in packet processing whether DIAdem creates an x-data channel to every y-data channel when DIAdem writes data.

| Definition | PkXCh, Enumeration variable |
| --- | --- |
|  | Enumeration variable with the following selection terms: Index Meaning 1 1 x-channel 2 No x-channel 3 Always new channels |
| Index | Meaning |
| 1 | 1 x-channel |
| 2 | No x-channel |
| 3 | Always new channels |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkXCh = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[DATA Writer](../../dlgdacpp/dac_packet_dlg_disp_io/hb_write_matrix.htm) | [Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm)

<!--NI_TOPIC bundle=diadem path=pkvaronl/pkvaronl/pkxonymax.htm language=enus -->
## TOPIC 01522: Variable: PkXonYMax

- bundle_id: `diadem`
- source_path: `pkvaronl/pkvaronl/pkxonymax.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/pkvaronl/pkvaronl/pkxonymax.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Packet Processing Variables](../pkvaronl/dac_packetvariables_overview.htm) > Variable: PkXonYMax

Variable: PkXonYMax

Specifies in packet processing whether DIAdem calculates the time value of the maximum measurement value as the statistical characteristic value.

| Definition | PkXonYMax, Integer variable |
| --- | --- |
|  | 0 or 1 |

|  | Note Do not change the value of a measurement after the measurement has started. |
| --- | --- |

|  | Note You must use the following object hierarchy to access the variable: DACObjOpen(BlockName) PkXonYMax = Value DACObjClose(BlockName) You need the DAC block name to open the DAC block, to access the variable, and to close the DAC block.Refer to Accessing Objects in DIAdem DAC for more information. |
| --- | --- |

#### Used by

[Program Variables in Commands](../../genas/genauto/genauto_programmvariables.htm) | [Statistics/Characteristic Statistical Values](../../dlgdacpp/dac_packet_dlg_math/hb_statistikm.htm)

<!--NI_TOPIC bundle=diadem path=portal/events/portal_events_oncontextmenupointselected.htm language=enus -->
## TOPIC 01523: Event: OnContextMenuPointSelected

- bundle_id: `diadem`
- source_path: `portal/events/portal_events_oncontextmenupointselected.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/events/portal_events_oncontextmenupointselected.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Events](../events/portal_events_overview.htm) > Event: OnContextMenuPointSelected

Event: OnContextMenuPointSelected

Is triggered when an item in a context menu is selected in the Data Portal.

The event starts the [user command](../../procauto/procauto/procauto_usercommand.htm) that you assigned to the [OnContextMenuPointSelected](../properties/diacmpnt_property_oncontextmenupointselected_portalevents.htm) property. If the script of the user command contains an error, DIAdem aborts the script without an error message. The DIAdem logfile contains information on the error.

The user command receives two parameters: The first parameter corresponds to an [Area](../../scriptview/objects/view_objects_itoareaobjectint.htm) object and contains the current area when the user command opens. The second parameter corresponds with a [Menupoint](../../contextmenu/objects/contextmenu_objects_imenupoint.htm) object and contains the entry of the context menu.

If you open a context menu in DIAdem VIEW, DIAdem configures this context menu and then triggers the event [OnShowingContextMenu](../events/portal_events_onshowingcontextmenu.htm) before the context menu displays. If you select a context menu item, DIAdem triggers the event OnContextMenuPointSelected. Then DIAdem closes the context menu.

Refer to [Working with Events in DIAdem](../../genshell/genshell/genshell_generalevents.htm) for further information on events in DIAdem.

```text
OnContextMenuPointSelected(ParentObj, MenuPoint)
```

| ParentObj | The first parameter is the same as the object corresponding to the context in the Data Portal, in which you opened the context menu. Use the IsKindof method with the following selection terms to specify the object types. ePortalList List view. ePortalStructure Structure view. |
| --- | --- |
| ePortalList List view. ePortalStructure Structure view. |  |
| ePortalList | List view. |
| ePortalStructure | Structure view. |
| MenuPoint | Specifies an entry in the context menu. |

|  | Note To test the example script, you must first save the script and register it as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example executes the user command MyOnShowingContextMenu as soon as you open the context menu in the Data Portal. This user command adds two new entries. When you select a context menu item, the example executes the MyOnContextMenuPointSelected user command, which displays the selected item and the type of portal view in a message:

[Copy script](javascript:void(0);)

```text
Call AddUserCommandToEvent("Portal.Events.OnShowingContextMenu", "MyOnShowingContextMenu")
Call AddUserCommandToEvent("Portal.Events.OnContextMenuPointSelected","MyOnContextMenuPointSelected")

Sub MyOnShowingContextMenu(oPortalView, oMenuPoints)
  Call oMenuPoints.Add("MyMenuPoint1", 1)
  Call oMenuPoints.Add("MyMenuPoint2", 2)
End Sub

Sub MyOnContextMenuPointSelected(oPortalView, oMenuPoint)
  Dim sPortal
  If oPortalView.IsKindof(ePortalStructure) Then
    sPortal = "Structure"
  Else
    sPortal = "List"
  End If
  Select Case oMenuPoint.ID
    Case 1    Call MsgBoxDisp(sPortal & ": MyMenuPoint1 selected")
    Case 2    Call MsgBoxDisp(sPortal & ": MyMenuPoint2 selected")
  End Select
End Sub
```

|  | Note Use the AddUserCommandToEvent command to assign several user commands to one event. Use the RemoveUserCommandFromEvent command to delete a single user command from a list of user commands which you assigned to an event. Assign an empty string to an event so that the event is no longer assigned to a user command. |
| --- | --- |

#### See Also

[OnContextMenuPointSelected](../properties/diacmpnt_property_oncontextmenupointselected_portalevents.htm) | [Objects Overview](../../scriptview/objects/view_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=portal/events/portal_events_onshowingcontextmenu.htm language=enus -->
## TOPIC 01524: Event: OnShowingContextMenu

- bundle_id: `diadem`
- source_path: `portal/events/portal_events_onshowingcontextmenu.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/events/portal_events_onshowingcontextmenu.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Events](../events/portal_events_overview.htm) > Event: OnShowingContextMenu

Event: OnShowingContextMenu

Is triggered in the Data Portal when a context menu displays.

The event starts the [user command](../../procauto/procauto/procauto_usercommand.htm) you assigned to the [OnShowingContextMenu](../properties/diacmpnt_property_onshowingcontextmenu_portalevents.htm) property. If the script of the user command contains an error, DIAdem aborts the script without an error message. The DIAdem logfile contains information on the error.

The user command receives two parameters: The first parameter corresponds to a [List](../objects/diacmpnt_objects_list.htm) or a [Structure](../objects/diacmpnt_objects_structure.htm) object. The second parameter corresponds with a [Menupoint](../../contextmenu/objects/contextmenu_objects_imenupoint.htm) object and contains the entry of the context menu. If the script of the user command contains an error, DIAdem aborts the script without an error message. The DIAdem logfile contains information on the error.

If you open a context menu in the Data Portal, DIAdem configures this context menu and then triggers the event OnShowingContextMenu before the context menu displays. If you select a context menu item, DIAdem triggers the event [OnContextMenuPointSelected](../events/portal_events_oncontextmenupointselected.htm). Then DIAdem closes the context menu.

Refer to [Working with Events in DIAdem](../../genshell/genshell/genshell_generalevents.htm) for further information on events in DIAdem.

```text
OnShowingContextMenu(ParentObj, MenuPoint)
```

| ParentObj | The first parameter is the same as the object corresponding to the context in the Data Portal, in which you opened the context menu. Use the IsKindof method with the following selection terms to specify the object types. ePortalList List view. ePortalStructure Structure view. |
| --- | --- |
| ePortalList List view. ePortalStructure Structure view. |  |
| ePortalList | List view. |
| ePortalStructure | Structure view. |
| MenuPoint | Specifies an entry in the context menu. |

|  | Note To test the example script, you must first save the script and register it as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example executes the user command MyOnShowingContextMenu as soon as you open the context menu in the Data Portal. This user command adds two new entries. When you select a context menu item, the example executes the MyOnContextMenuPointSelected user command, which displays the selected item and the type of portal view in a message:

[Copy script](javascript:void(0);)

```text
Call AddUserCommandToEvent("Portal.Events.OnShowingContextMenu", "MyOnShowingContextMenu")
Call AddUserCommandToEvent("Portal.Events.OnContextMenuPointSelected","MyOnContextMenuPointSelected")

Sub MyOnShowingContextMenu(oPortalView, oMenuPoints)
  Call oMenuPoints.Add("MyMenuPoint1", 1)
  Call oMenuPoints.Add("MyMenuPoint2", 2)
End Sub

Sub MyOnContextMenuPointSelected(oPortalView, oMenuPoint)
  Dim sPortal
  If oPortalView.IsKindof(ePortalStructure) Then
    sPortal = "Structure"
  Else
    sPortal = "List"
  End If
  Select Case oMenuPoint.ID
    Case 1    Call MsgBoxDisp(sPortal & ": MyMenuPoint1 selected")
    Case 2    Call MsgBoxDisp(sPortal & ": MyMenuPoint2 selected")
  End Select
End Sub
```

|  | Note Use the AddUserCommandToEvent command to assign several user commands to one event. Use the RemoveUserCommandFromEvent command to delete a single user command from a list of user commands which you assigned to an event. Assign an empty string to an event so that the event is no longer assigned to a user command. |
| --- | --- |

#### See Also

[OnShowingContextMenu](../properties/diacmpnt_property_onshowingcontextmenu_portalevents.htm) | [Objects Overview](../../scriptview/objects/view_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_collapse_structure.htm language=enus -->
## TOPIC 01525: Method: Collapse for Structure

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_collapse_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_collapse_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: Collapse for Structure

Method: Collapse for Structure

Hides the channels from a channel group in the structure view of the Data Portal.

```text
Set oElement = Object.Collapse(Element)
```

| Object | StructureObject with this method |
| --- | --- |
| Element | Element <Data>Contains a ChannelGroup object or a Channel object. |
| oElement | Element <Data>Contains a ChannelGroup object or a Channel object. |

|  | Note If you use commands in your script that change data in the Data Portal, DIAdem refreshes the Data Portal at the end of the script. Use the UIAutoRefreshSet command to refresh the Data Portal while the script is running. Then execute the commands that select elements of the Data Portal or change the drop-down status. |
| --- | --- |

The following example hides the channels of the first channel group, in the structure view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If Portal.Structure.IsExpanded (Data.Root.ChannelGroups(1)) Then
  Call Portal.Structure.Collapse(Data.Root.ChannelGroups(1))
End If
```

[Copy script](javascript:void(0);)

```text
if dd.Portal.Structure.IsExpanded (dd.Data.Root.ChannelGroups(1)) : 
    +nbsp; Call dd.Portal.Structure.Collapse(dd.Data.Root.ChannelGroups(1)) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_display_structure.htm language=enus -->
## TOPIC 01526: Method: Display for Structure

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_display_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_display_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: Display for Structure

Method: Display for Structure

Changes the display of the Data Portal contents. You can display all the elements in the Data Portal or display only the [pinned elements](../../genportal/genportal/portal_filter.htm).

```text
Object.Display(PortalStructureDisplayType)
```

| Object | StructureObject with this method |  |
| --- | --- | --- |
| PortalStructureDisplayType | TcPortalStructureDisplayType value with read/write access.Enumeration with the following selection terms: 1 ePortalStructureDisplayNormal The Data Portal displays all elements. 2 ePortalStructureDisplayPinnedElements The Data Portal displays only the pinned elements. |  |
| 1 | ePortalStructureDisplayNormal | The Data Portal displays all elements. |
| 2 | ePortalStructureDisplayPinnedElements | The Data Portal displays only the pinned elements. |

The following example displays only the pinned channel groups and channels in the Data Portal if the first channel group is pinned:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If Portal.Structure.IsElementPinned(Data.Root.ChannelGroups(1)) Then
  Call Portal.Structure.Display(ePortalStructureDisplayPinnedElements)
End If
```

[Copy script](javascript:void(0);)

```text
if dd.Portal.Structure.IsElementPinned(dd.Data.Root.ChannelGroups(1)) : 
    dd.Portal.Structure.Display(dd.ePortalStructureDisplayPinnedElements) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_expand_channelpreview.htm language=enus -->
## TOPIC 01527: Method: Expand for ChannelPreview

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_expand_channelpreview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_expand_channelpreview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: Expand for ChannelPreview

Method: Expand for ChannelPreview

Opens or closes the [channel preview](../../genportal/genportal/portal_general_prop.htm) of the Data Portal.

```text
Object.Expand(ExpandChannelPreview)
```

| Object | ChannelPreviewObject with this method |
| --- | --- |
| ExpandChannelPreview | BooleanSpecifies whether the channel preview is open (TRUE) or closed (FALSE). |

The following example opens the channel preview if the area is not already open:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If NOT Portal.ChannelPreview.IsExpanded Then
  Call Portal.ChannelPreview.Expand(TRUE)
End If
```

[Copy script](javascript:void(0);)

```text
if not dd.Portal.ChannelPreview.IsExpanded() : 
    dd.Portal.ChannelPreview.Expand(True) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_expand_filterform.htm language=enus -->
## TOPIC 01528: Method: Expand for FilterForm

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_expand_filterform.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_expand_filterform.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: Expand for FilterForm

Method: Expand for FilterForm

Opens or closes the [filter area](../../genportal/genportal/portal_filter.htm) of the Data Portal.

```text
Object.Expand(ExpandFilter)
```

| Object | FilterFormObject with this method |
| --- | --- |
| ExpandFilter | BooleanSpecifies whether the filter area is open (TRUE) or closed (FALSE). |

The following example opens the filter area if the area is not already open:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If Not Portal.Structure.FilterForm.IsExpanded Then
  Call Portal.Structure.FilterForm.Expand(TRUE)
End If
```

[Copy script](javascript:void(0);)

```text
if not dd.Portal.Structure.FilterForm.IsExpanded() : 
    dd.Portal.Structure.FilterForm.Expand(True) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_expand_structure.htm language=enus -->
## TOPIC 01529: Method: Expand for Structure

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_expand_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_expand_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: Expand for Structure

Method: Expand for Structure

Displays the channels from a channel group in the structure view of the Data Portal.

```text
Set oElement = Object.Expand(Element)
```

| Object | StructureObject with this method |
| --- | --- |
| Element | Element <Data>Contains a ChannelGroup object or a Channel object. |
| oElement | Element <Data>Contains a ChannelGroup object or a Channel object. |

|  | Note If you use commands in your script that change data in the Data Portal, DIAdem refreshes the Data Portal at the end of the script. Use the UIAutoRefreshSet command to refresh the Data Portal while the script is running. Then execute the commands that select elements of the Data Portal or change the drop-down status. |
| --- | --- |

The following example displays the channels of the first channel group, in the structure view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If Not Portal.Structure.IsExpanded(Data.Root.ChannelGroups(1)) Then
  Call Portal.Structure.Expand(Data.Root.ChannelGroups(1))
End If
```

[Copy script](javascript:void(0);)

```text
if not dd.Portal.Structure.IsExpanded(dd.Data.Root.ChannelGroups(1)) : 
    +nbsp; Call dd.Portal.Structure.Expand(dd.Data.Root.ChannelGroups(1)) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_getfloatingpos_portal.htm language=enus -->
## TOPIC 01530: Method: GetFloatingPos for Portal

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_getfloatingpos_portal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_getfloatingpos_portal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: GetFloatingPos for Portal

Method: GetFloatingPos for Portal

Returns the position of the top left corner of the floating Data Portal in relation to the screen origin in pixels. The screen origin is the top-left corner of the screen.

```text
Object.GetFloatingPos(Top, Left)
```

| Object | PortalObject with this method |
| --- | --- |
| Top | VariantSpecifies the distance to the top screen edge in pixels. |
| Left | VariantSpecifies the distance to the left screen edge in pixels. |

The following example determines and displays the current position of the floating Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dTop, dLeft
Portal.Floating = TRUE
Portal.Visible = TRUE
Call Portal.GetFloatingPos(dTop, dLeft)
Call MsgBoxDisp("Top : " & dTop & ", left: " & dLeft)
```

[Copy script](javascript:void(0);)

```text
Portal.Floating = True 
Portal.Visible = True 
dd.Portal.GetFloatingPos(dTop, dLeft) 
dd.MsgBoxDisp("Top : " + dTop + ", left: " + dLeft) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_getfloatingsize_portal.htm language=enus -->
## TOPIC 01531: Method: GetFloatingSize for Portal

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_getfloatingsize_portal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_getfloatingsize_portal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: GetFloatingSize for Portal

Method: GetFloatingSize for Portal

Returns the size of the floating Data Portal in pixels.

```text
Object.GetFloatingSize(Width, Height)
```

| Object | PortalObject with this method |
| --- | --- |
| Width | VariantSpecifies the width of the Data Portal in pixels. |
| Height | VariantSpecifies the height of the Data Portal in pixels. |

The following example determines and displays the size of the floating Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim dWidth, dHeight
Portal.Floating = TRUE
Portal.Visible = TRUE
Call Portal.GetFloatingSize(dWidth, dHeight)
Call MsgBoxDisp("Width : " & dWidth & ", Height: " & dHeight)
```

[Copy script](javascript:void(0);)

```text
Portal.Floating = True 
Portal.Visible = True 
dd.Portal.GetFloatingSize(dWidth, dHeight) 
dd.MsgBoxDisp("Width : " + dWidth + ", Height: " + dHeight) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_iselementdisplayed_structure.htm language=enus -->
## TOPIC 01532: Method: IsElementDisplayed for Structure

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_iselementdisplayed_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_iselementdisplayed_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: IsElementDisplayed for Structure

Method: IsElementDisplayed for Structure

Determines whether the Data Portal displays a specific channel group or channel and does not hide it by collapsing a channel group or using a filter condition. If you show or hide channels in scripts using filters or pins, you must first call the [Refresh for Portal](../methods/diacmpnt_method_refresh_portal.htm) method so that DIAdem recognizes the display state.

```text
bIsElementDisplayed = Object.IsElementDisplayed(Element)
```

| Object | StructureObject with this method |
| --- | --- |
| Element | Element <Data>Specifies the element to be checked. Elements can be channel groups or channels. |
| bIsElementDisplayed | BooleanReceives the results of the check. When the Data Portal displays the specified element, bIsElementDisplayed receives the value TRUE, otherwise FALSE. |

The following example displays whether the Data Portal displays the time channel in the first channel group:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp (Portal.Structure.IsElementDisplayed(Data.Root.ChannelGroups(1).Channels("time")))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp (dd.Portal.Structure.IsElementDisplayed(dd.Data.Root.ChannelGroups(1).Channels("time"))) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_iselementpinned_structure.htm language=enus -->
## TOPIC 01533: Method: IsElementPinned for Structure

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_iselementpinned_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_iselementpinned_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: IsElementPinned for Structure

Method: IsElementPinned for Structure

Determines whether a specific element is [pinned](../../genportal/genportal/portal_pinnen.htm) in the Data Portal.

```text
bIsElementPinned = Object.IsElementPinned(Element)
```

| Object | StructureObject with this method |
| --- | --- |
| Element | Element <Data>Specifies an element. Pinned elements can only be channels. When you pin a group, DIAdem pins all channels of this group. |
| bIsElementPinned | BooleanReceives the results of the check. If the specified element is pinned, bIsElementPinned receives the value TRUE. Otherwise it receives the value FALSE. |

The following example checks whether the time channel in the first channel group is pinned. If the channel is pinned, the example removes all the pins in the Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyElement
Set oMyElement = Data.Root.ChannelGroups(1).Channels("time")
If Portal.Structure.IsElementPinned(oMyElement) Then
  Call Portal.Structure.ResetPinnedElements
End If
```

[Copy script](javascript:void(0);)

```text
oMyElement = dd.Data.Root.ChannelGroups(1).Channels("time") 
if dd.Portal.Structure.IsElementPinned(oMyElement) : 
    dd.Portal.Structure.Reset()PinnedElements 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_isexpanded_channelpreview.htm language=enus -->
## TOPIC 01534: Method: IsExpanded for ChannelPreview

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_isexpanded_channelpreview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_isexpanded_channelpreview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: IsExpanded for ChannelPreview

Method: IsExpanded for ChannelPreview

Checks whether the Data Portal displays the [channel preview](../../genportal/genportal/portal_general_prop.htm).

```text
bIsExpanded = Object.IsExpanded
```

| Object | ChannelPreviewObject with this method |
| --- | --- |
| bIsExpanded | BooleanReceives the results of the check. |

The following example opens the channel preview if the area is not already open:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If NOT Portal.ChannelPreview.IsExpanded Then
  Call Portal.ChannelPreview.Expand(TRUE)
End If
```

[Copy script](javascript:void(0);)

```text
if not dd.Portal.ChannelPreview.IsExpanded() : 
    dd.Portal.ChannelPreview.Expand(True) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/methods/diacmpnt_method_removeall_selection.htm language=enus -->
## TOPIC 01535: Method: RemoveAll for Selection

- bundle_id: `diadem`
- source_path: `portal/methods/diacmpnt_method_removeall_selection.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/methods/diacmpnt_method_removeall_selection.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Methods](../methods/portal_method_overview.htm) > Method: RemoveAll for Selection

Method: RemoveAll for Selection

Deletes all elements from the Selection collection in the Data Portal script interface.

```text
Object.RemoveAll
```

| Object | SelectionObject with this method |
| --- | --- |

|  | Note If you use commands in your script that change data in the Data Portal, DIAdem refreshes the Data Portal at the end of the script. Use the UIAutoRefreshSet command to refresh the Data Portal while the script is running. Then execute the commands that select elements of the Data Portal or change the drop-down status. |
| --- | --- |

The following example deletes the selection in the structure view of the Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Portal.Structure.Selection.RemoveAll
```

[Copy script](javascript:void(0);)

```text
dd.Portal.Structure.Selection.RemoveAll() 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/objects/diacmpnt_objects_column.htm language=enus -->
## TOPIC 01536: Object: Column

- bundle_id: `diadem`
- source_path: `portal/objects/diacmpnt_objects_column.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/objects/diacmpnt_objects_column.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/portal_objects_collections.htm) | [List](../objects/diacmpnt_objects_list.htm)) > [Columns](../objects/diacmpnt_objects_columns.htm) > Object: Column

Object: Column

The Column object corresponds to a column in the list view of the Data Portal. Use the Column object to specify information about this column that displays a channel property.

The following example changes the width of all columns of the list view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Portal.List.Activate
Dim oMyCol
For each oMyCol in Portal.List.Columns
  oMyCol.Width = 100
Next
```

[Copy script](javascript:void(0);)

```text
dd.Portal.List.Activate() 
for oMyCol in dd.Portal.List.Columns: 
    oMyCol.Width = 100 
```

#### Properties

[Format](../properties/diacmpnt_property_format_column.htm) | [Property](../properties/diacmpnt_property_property_column.htm) | [Title](../properties/diacmpnt_property_title_column.htm) | [Width](../properties/diacmpnt_property_width_column.htm)

#### Returned From

[Columns](../objects/diacmpnt_objects_columns.htm).[Add](../methods/diacmpnt_method_add_columns.htm) | [Columns](../objects/diacmpnt_objects_columns.htm).[Item](../methods/diacmpnt_method_item_columns.htm)

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/objects/diacmpnt_objects_columns.htm language=enus -->
## TOPIC 01537: Collection: Columns

- bundle_id: `diadem`
- source_path: `portal/objects/diacmpnt_objects_columns.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/objects/diacmpnt_objects_columns.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

([Collections](../objects/portal_objects_collections.htm) | [List](../objects/diacmpnt_objects_list.htm)) > Collection: Columns

Collection: Columns

Collection of all [Columns](../objects/diacmpnt_objects_column.htm) in the list view of the Data Portal. You can use the Columns collection to delete the columns of the list view or to add columns.

The following example changes the width of all columns of the list view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Portal.List.Activate
Dim oMyCol
For each oMyCol in Portal.List.Columns
  oMyCol.Width = 100
Next
```

[Copy script](javascript:void(0);)

```text
dd.Portal.List.Activate() 
for oMyCol in dd.Portal.List.Columns: 
    oMyCol.Width = 100 
```

#### Properties

[Count](../properties/diacmpnt_property_count_columns.htm)

#### Methods

[Add](../methods/diacmpnt_method_add_columns.htm) | [Item](../methods/diacmpnt_method_item_columns.htm) | [Remove](../methods/diacmpnt_method_remove_columns.htm) | [RemoveAll](../methods/diacmpnt_method_removeall_columns.htm)

#### Returned From

[List](../objects/diacmpnt_objects_list.htm).[Columns](../properties/diacmpnt_property_columns_list.htm)

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/objects/diacmpnt_objects_structureorlist.htm language=enus -->
## TOPIC 01538: Object: StructureOrList

- bundle_id: `diadem`
- source_path: `portal/objects/diacmpnt_objects_structureorlist.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/objects/diacmpnt_objects_structureorlist.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Objects](../objects/portal_objects_overview.htm) > [Portal](../objects/diacmpnt_objects_portal.htm) > Object: StructureOrList

Object: StructureOrList

The StructureOrList object corresponds to the current view of the Data Portal and can correspond to the [Structure view](../../genportal/genportal/portal_general.htm) or [List view](../../genportal/genportal/portal_general_list.htm) of the Data Portal.

The StructureOrList object corresponds to one of the following objects:

| Structure (Structure) | Structure view |
| --- | --- |
| List (List) | List view |

The following example enables the structure view of the Data Portal if this view is not already enabled:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyObj
Set oMyObj = Portal.ActiveView
If oMyObj.IsKindOf(ePortalList) Then
  Call Portal.Structure.Activate
End If
```

[Copy script](javascript:void(0);)

```text
oMyObj = dd.Portal.ActiveView 
if oMyObj.IsKindOf(ePortalList) : 
    dd.Portal.Structure.Activate() 
```

#### Returned From

[Portal](../objects/diacmpnt_objects_portal.htm).[ActiveView](../properties/diacmpnt_property_activeview_portal.htm)

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/objects/portal_objects_collections.htm language=enus -->
## TOPIC 01539: Collections

- bundle_id: `diadem`
- source_path: `portal/objects/portal_objects_collections.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/objects/portal_objects_collections.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > Collections

Collections

A collection is an object that contains a group of associated objects. The following topics describe all the collections of the script interface of the Data Portal.

<!--NI_TOPIC bundle=diadem path=portal/objects/portal_objects_overview.htm language=enus -->
## TOPIC 01540: Objects

- bundle_id: `diadem`
- source_path: `portal/objects/portal_objects_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/objects/portal_objects_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > Objects

[[IMAGE alt='image' src='ms-its:diadem.chm::/plus.png']Display all](#nowhere)  [[IMAGE alt='image' src='ms-its:diadem.chm::/minus2.png']Hide all](#nowhere)

Objects

The Data Portal consists of objects and subobjects that you can create, delete, and modify with a script.

The global object is the Portal object. Use the Portal object to design the view of the Data Portal and to access the subobjects of the Data Portal. Because the Data Portal comprises the structure view and the list view, the Portal object has the respective subobjects Structure and List.

Some subobjects have a collection of single objects. You can access the single objects and the collection. Use the [Set](../../vbs/general/vbs_set.htm) statement to assign objects to a variable and to make it easier to access these objects. You use the Add methods to create new objects. You use the Remove methods to delete existing objects. You use properties to change objects.

The following structure of the objects of the Data Portal shows you how to click to the objects:

- Portal
  - ChannelPreview
  - List
    - Channel <Data>
    - Columns
      - Column
    - Selection
  - Structure
    - FilterForm
    - Selection
  - StructureOrList

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_activeview_portal.htm language=enus -->
## TOPIC 01541: Property: ActiveView for Portal

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_activeview_portal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_activeview_portal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: ActiveView for Portal

Property: ActiveView for Portal

Returns the [List](../objects/diacmpnt_objects_list.htm) object or the [Structure](../objects/diacmpnt_objects_structure.htm) object. The List object corresponds to the list view of the Data Portal. The list view lists all channels in a table and if specified, sorts the channels according to the selected property. The Structure object corresponds to the structure view of the Data Portal. The structure view organizes channels hierarchically into channel groups.

```text
Set oStructureOrList = Object.ActiveView
```

| Object | PortalObject with this property |
| --- | --- |
| oStructureOrList | StructureOrListReturned object |

The following example enables the structure view of the Data Portal if this view is not already enabled:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyObj
Set oMyObj = Portal.ActiveView
If oMyObj.IsKindOf(ePortalList) Then
  Call Portal.Structure.Activate
End If
```

[Copy script](javascript:void(0);)

```text
oMyObj = dd.Portal.ActiveView 
if oMyObj.IsKindOf(ePortalList) : 
    dd.Portal.Structure.Activate() 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_channelfiltertext_filterform.htm language=enus -->
## TOPIC 01542: Property: ChannelFilterText for FilterForm

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_channelfiltertext_filterform.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_channelfiltertext_filterform.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: ChannelFilterText for FilterForm

Property: ChannelFilterText for FilterForm

Specifies the filter condition for channels in the Data Portal filter area.

```text
Object.ChannelFilterText
```

| Object | FilterFormObject with this property |
| --- | --- |
| Object.ChannelFilterText | String with read and write accessSpecifies the filter condition for the channels. |

The following example displays the filter conditions for channel groups and channels if the filter area is open and a filter is enabled:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If Portal.Structure.FilterForm.IsFiltered Then
  Call MsgBoxDisp (Portal.Structure.FilterForm.GroupFilterText)
  Call MsgBoxDisp (Portal.Structure.FilterForm.ChannelFilterText)
End If
```

[Copy script](javascript:void(0);)

```text
if dd.Portal.Structure.FilterForm.IsFiltered() : 
    dd.MsgBoxDisp (dd.Portal.Structure.FilterForm.GroupFilterText) 
    dd.MsgBoxDisp (dd.Portal.Structure.FilterForm.ChannelFilterText) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_filterform_structure.htm language=enus -->
## TOPIC 01543: Property: FilterForm for Structure

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_filterform_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_filterform_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: FilterForm for Structure

Property: FilterForm for Structure

Returns the [filter settings](../../genportal/genportal/portal_filter.htm) in the Data Portal.

```text
Set oFilterForm = Object.FilterForm
```

| Object | StructureObject with this property |
| --- | --- |
| oFilterForm | FilterFormReturned object |

The following example opens the filter area if the area is not already open:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If Not Portal.Structure.FilterForm.IsExpanded Then
  Call Portal.Structure.FilterForm.Expand(TRUE)
End If
```

[Copy script](javascript:void(0);)

```text
if not dd.Portal.Structure.FilterForm.IsExpanded() : 
    dd.Portal.Structure.FilterForm.Expand(True) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_firstvisiblecolumn_list.htm language=enus -->
## TOPIC 01544: Property: FirstVisibleColumn for List

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_firstvisiblecolumn_list.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_firstvisiblecolumn_list.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: FirstVisibleColumn for List

Property: FirstVisibleColumn for List

Specifies in the Data Portal list view the first visible object.

```text
Object.FirstVisibleColumn
```

| Object | ListObject with this property |
| --- | --- |
| Object.FirstVisibleColumn | LongInteger with read and write access |

|  | Note Depending on the size of the list view, DIAdem does not display the specified column as the first visible column. DIAdem only moves this column into the visible area. |
| --- | --- |

The following example displays four channel properties columnwise in the list view of the Data Portal. The second column, which contains the channel names, is the first visible column.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Portal.Visible = TRUE
Call Portal.List.Activate
Portal.Width = 200

Call Portal.List.Columns.RemoveAll()
Call Portal.List.Columns.Add("number")
Call Portal.List.Columns.Add("name")
Call Portal.List.Columns.Add("length")
Call Portal.List.Columns.Add("description")

Portal.List.FirstVisibleColumn = 2
```

[Copy script](javascript:void(0);)

```text
Portal.Visible = True 
dd.Portal.List.Activate() 
Portal.Width = 200 
dd.Portal.List.Columns.RemoveAll() 
dd.Portal.List.Columns.Add("number") 
dd.Portal.List.Columns.Add("name") 
dd.Portal.List.Columns.Add("length") 
dd.Portal.List.Columns.Add("description") 
Portal.List.FirstVisibleColumn = 2 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_firstvisibleelement_list.htm language=enus -->
## TOPIC 01545: Property: FirstVisibleElement for List

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_firstvisibleelement_list.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_firstvisibleelement_list.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: FirstVisibleElement for List

Property: FirstVisibleElement for List

Specifies in the Data Portal list view the first visible channel.

```text
Set oChannel = Object.FirstVisibleElement
```

| Object | ListObject with this property |
| --- | --- |
| oChannel | Channel <Data>Returned object |

The following example displays four channel properties columnwise in the list view of the Data Portal. The first channel of the third channel group is the first visible channel.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Portal.Visible = TRUE
Call Portal.List.Activate
Portal.Ratio = 20

Call Portal.List.Columns.RemoveAll()
Call Portal.List.Columns.Add("number")
Call Portal.List.Columns.Add("name")
Call Portal.List.Columns.Add("length")
Call Portal.List.Columns.Add("description")

Set Portal.List.FirstVisibleElement = Data.Root.ChannelGroups(3).Channels(1)
```

[Copy script](javascript:void(0);)

```text
Portal.Visible = True 
dd.Portal.List.Activate() 
Portal.Ratio = 20 
dd.Portal.List.Columns.RemoveAll() 
dd.Portal.List.Columns.Add("number") 
dd.Portal.List.Columns.Add("name") 
dd.Portal.List.Columns.Add("length") 
dd.Portal.List.Columns.Add("description") 
dd.Portal.List.FirstVisibleElement = dd.Data.Root.ChannelGroups(3).Channels(1) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_onshowingcontextmenu_portalevents.htm language=enus -->
## TOPIC 01546: Property: OnShowingContextMenu for Events <Portal>

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_onshowingcontextmenu_portalevents.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_onshowingcontextmenu_portalevents.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: OnShowingContextMenu for Events <Portal>

Property: OnShowingContextMenu for Events <Portal>

Specifies the name of the user command that DIAdem executes when you open a context menu in the Data Portal.

The user command receives two parameters: The first parameter is the same as the object corresponding to the context in the Data Portal, in which you opened the context menu. The object can be a [List object](../objects/diacmpnt_objects_list.htm) or a [Structure objekt](../objects/diacmpnt_objects_structure.htm). The second parameter corresponds with a [Menupoint](../../contextmenu/objects/contextmenu_objects_imenupoint.htm) object and contains the entry of the context menu. If the script of the user command contains an error, DIAdem aborts the script without an error message. The DIAdem logfile contains information on the error.

```text
Object.OnShowingContextMenu
```

| Object | Events <Portal>Object with this property |
| --- | --- |
| Object.OnShowingContextMenu | String with read and write access |

|  | Note To test the example script, you must first save the script and register it as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example executes the user command MyOnShowingContextMenu as soon as you open the context menu in the Data Portal. This user command adds two new entries. When you select a context menu item, the example executes the MyOnContextMenuPointSelected user command, which displays the selected item and the type of portal view in a message:

[Copy script](javascript:void(0);)

```text
Call AddUserCommandToEvent("Portal.Events.OnShowingContextMenu", "MyOnShowingContextMenu")
Call AddUserCommandToEvent("Portal.Events.OnContextMenuPointSelected","MyOnContextMenuPointSelected")

Sub MyOnShowingContextMenu(oPortalView, oMenuPoints)
  Call oMenuPoints.Add("MyMenuPoint1", 1)
  Call oMenuPoints.Add("MyMenuPoint2", 2)
End Sub

Sub MyOnContextMenuPointSelected(oPortalView, oMenuPoint)
  Dim sPortal
  If oPortalView.IsKindof(ePortalStructure) Then
    sPortal = "Structure"
  Else
    sPortal = "List"
  End If
  Select Case oMenuPoint.ID
    Case 1    Call MsgBoxDisp(sPortal & ": MyMenuPoint1 selected")
    Case 2    Call MsgBoxDisp(sPortal & ": MyMenuPoint2 selected")
  End Select
End Sub
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_property_column.htm language=enus -->
## TOPIC 01547: Property: Property for Column

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_property_column.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_property_column.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Property for Column

Property: Property for Column

Specifies the name of the property that DIAdem displays in a column of the Data Portal list view.

```text
Object.Property
```

| Object | ColumnObject with this property |
| --- | --- |
| Object.Property | String with read access |

The following example displays the names of all channel properties that DIAdem displays columnwise in the list view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oCol
For Each oCol in Portal.List.Columns
  Call MsgBoxDisp("Property: " & oCol.Property)
Next
```

[Copy script](javascript:void(0);)

```text
for oCol in dd.Portal.List.Columns: 
    dd.MsgBoxDisp("Property: " + oCol.Property) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_ratio_portal.htm language=enus -->
## TOPIC 01548: Property: Ratio for Portal

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_ratio_portal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_ratio_portal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Ratio for Portal

Property: Ratio for Portal

Specifies the ratio of the area of the structure view or list view to the joint area of the properties display and the channel preview. If you assign 0 to this property, the structure view or the list view of the Data Portal is not visible. If you assign the value 100 to the property, the properties display and the channel preview of the Data Portal are not visible.

|  | Note You cannot assign a value to the Portal.Ratio property that is greater than or equal to the Portal.ChannelPreview.Ratio property. The channel preview remains the same size and DIAdem automatically assigns a value that is a little lower than the value of Portal.ChannelPreview.Ratio to the Portal.Ratio property. |
| --- | --- |

```text
Object.Ratio
```

| Object | PortalObject with this property |
| --- | --- |
| Object.Ratio | Double with read and write access |

The following example shows the Data Portal and specifies that DIAdem displays the structure or list view the same size as the channel preview and the properties display together:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Portal.Visible = TRUE
Portal.Ratio = 50
```

[Copy script](javascript:void(0);)

```text
Portal.Visible = True 
Portal.Ratio = 50 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_selection_list.htm language=enus -->
## TOPIC 01549: Property: Selection for List

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_selection_list.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_selection_list.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Selection for List

Property: Selection for List

Returns a collection of all [Selections](../objects/diacmpnt_objects_selection.htm) in the the list view of the Data Portal. A selection is a number of selected channels. Use the [Item](../methods/diacmpnt_method_item_selection.htm) method or enter the index in parentheses to access individual selections in scripts.

```text
Set oSelection = Object.Selection
```

| Object | ListObject with this property |
| --- | --- |
| oSelection | SelectionReturned collection |

The following example displays the number of channels selected in the list view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Portal.List.Selection.Count)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Portal.List.Select()ion.Count) 
```

The following example displays the name of the first selected element:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Portal.List.Selection.Item(1).Name)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Portal.List.Selection.Item(1).Name) 
```

The following example displays the name of the second selected element:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Portal.List.Selection(2).Name)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Portal.List.Selection(2).Name) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_selection_structure.htm language=enus -->
## TOPIC 01550: Property: Selection for Structure

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_selection_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_selection_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Selection for Structure

Property: Selection for Structure

Returns a collection of all [Selections](../objects/diacmpnt_objects_selection.htm) in the the structure view of the Data Portal. A selection can comprise several selected channel groups or channels, or the selected data set. Use the [Item](../methods/diacmpnt_method_item_selection.htm) method or enter the index in parentheses to access individual selections in scripts.

```text
Set oSelection = Object.Selection
```

| Object | StructureObject with this property |
| --- | --- |
| oSelection | SelectionReturned collection |

The following example displays the number of elements selected in the structure view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Portal.Structure.Selection.Count)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Portal.Structure.Select()ion.Count) 
```

The following example displays the name of the first selected element:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Portal.Structure.Selection.Item(1).Name)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Portal.Structure.Selection.Item(1).Name) 
```

The following example displays the name of the second selected element:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Portal.Structure.Selection(2).Name)
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Portal.Structure.Selection(2).Name) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_soundstate_channelpreview.htm language=enus -->
## TOPIC 01551: Property: SoundState for ChannelPreview

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_soundstate_channelpreview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_soundstate_channelpreview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: SoundState for ChannelPreview

Property: SoundState for ChannelPreview

Specifies whether to enable waveform channel [Sound](../../genportal/genportal/portal_general_prop.htm) in the Data Portal.

```text
Object.SoundState
```

| Object | ChannelPreviewObject with this property |
| --- | --- |
| Object.SoundState | Boolean with read and write access |

The following example enables the sound of waveform channels in the Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Portal.ChannelPreview.SoundState(TRUE)
```

[Copy script](javascript:void(0);)

```text
Portal.ChannelPreview.SoundState(True) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_structure_portal.htm language=enus -->
## TOPIC 01552: Property: Structure for Portal

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_structure_portal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_structure_portal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Structure for Portal

Property: Structure for Portal

Returns the [Structure](../objects/diacmpnt_objects_structure.htm) object. The Structure object corresponds to the structure view of the Data Portal. The structure view organizes channels hierarchically into channel groups.

```text
Set oStructure = Object.Structure
```

| Object | PortalObject with this property |
| --- | --- |
| oStructure | StructureReturned object |

The following example enables the structure view of the Data Portal if this view is not already enabled:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyObj
Set oMyObj = Portal.ActiveView
If oMyObj.IsKindOf(ePortalList) Then
  Call Portal.Structure.Activate
End If
```

[Copy script](javascript:void(0);)

```text
oMyObj = dd.Portal.ActiveView 
if oMyObj.IsKindOf(ePortalList) : 
    dd.Portal.Structure.Activate() 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_title_column.htm language=enus -->
## TOPIC 01553: Property: Title for Column

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_title_column.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_title_column.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Title for Column

Property: Title for Column

Specifies a column label in the list view of the Data Portal.

```text
Object.Title
```

| Object | ColumnObject with this property |
| --- | --- |
| Object.Title | String with read access |

The following example displays the column labels which DIAdem displays in the list view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oCol
For Each oCol in Portal.List.Columns
  Call MsgBoxDisp("Title: " & oCol.Title)
Next
```

[Copy script](javascript:void(0);)

```text
for oCol in dd.Portal.List.Columns: 
    dd.MsgBoxDisp("Title: " + oCol.Title) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_useautopins_structure.htm language=enus -->
## TOPIC 01554: Property: UseAutoPins for Structure

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_useautopins_structure.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_useautopins_structure.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: UseAutoPins for Structure

Property: UseAutoPins for Structure

Specifies whether DIAdem automatically pins new channels in the Data Portal when the Data Portal displays only pinned channels. New channels, for example, can be created by loading additional channels or through calculation results.

```text
Object.UseAutoPins
```

| Object | StructureObject with this property |
| --- | --- |
| Object.UseAutoPins | Boolean with read and write accessSpecifies whether DIAdem automatically pins new channels (TRUE) or not (FALSE). |

The following example automatically pins new channels:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Portal.Structure.UseAutoPins = True
```

[Copy script](javascript:void(0);)

```text
Portal.Structure.UseAutoPins = True 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_visible_portal.htm language=enus -->
## TOPIC 01555: Property: Visible for Portal

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_visible_portal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_visible_portal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Visible for Portal

Property: Visible for Portal

Specifies whether the Data Portal is visible.

```text
Object.Visible
```

| Object | PortalObject with this property |
| --- | --- |
| Object.Visible | Boolean with read and write access |

The following example displays the Data Portal in floating mode:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Portal.Visible = TRUE
Portal.Floating = TRUE
```

[Copy script](javascript:void(0);)

```text
Portal.Visible = True 
Portal.Floating = True 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_width_column.htm language=enus -->
## TOPIC 01556: Property: Width for Column

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_width_column.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_width_column.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Width for Column

Property: Width for Column

Specifies in the list view of the Data Portal the column width in pixels.

```text
Object.Width
```

| Object | ColumnObject with this property |
| --- | --- |
| Object.Width | LongInteger with read and write access |

|  | Note The value -1 refers to the default column width. |
| --- | --- |

The following example returns the column widths which DIAdem displays in the list view:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oCol
For Each oCol in Portal.List.Columns
  Call MsgBoxDisp("Width: " & oCol.Width)
Next
```

[Copy script](javascript:void(0);)

```text
for oCol in dd.Portal.List.Columns: 
    dd.MsgBoxDisp("Width: " + oCol.Width) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=portal/properties/diacmpnt_property_width_portal.htm language=enus -->
## TOPIC 01557: Property: Width for Portal

- bundle_id: `diadem`
- source_path: `portal/properties/diacmpnt_property_width_portal.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/portal/properties/diacmpnt_property_width_portal.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Data Portal](../scriptportal_overview.htm) > [Properties](../properties/portal_property_overview.htm) > Property: Width for Portal

Property: Width for Portal

Specifies the width of the docked Data Portal in pixels. The minimum width of the Data Portal is 10 pixels.

```text
Object.Width
```

| Object | PortalObject with this property |
| --- | --- |
| Object.Width | LongInteger with read and write access |

The following example displays the width of the docked Data Portal:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Portal.Floating = FALSE
Call MsgBoxDisp(Portal.Width)
```

[Copy script](javascript:void(0);)

```text
Portal.Floating = False 
dd.MsgBoxDisp(dd.Portal.Width) 
```

#### See Also

[Objects Overview](../objects/portal_objects_overview.htm)

#### Procedures

[Creating a Template for Custom Properties](../../procportal/procportal/procportal_custompropertytemplate.htm) | [Deleting Channels from the Data Portal](../../procportal/procportal/procportal_channel_delete.htm) | [Expanding Registered Channels](../../procportal/procportal/procportal_expanding_channels.htm) | [Generating Data Set, Group, and Channel Custom Properties in the Data Portal](../../procportal/procportal/procportal_additional_properties.htm) | [Generating New Channels in the Data Portal](../../procportal/procportal/procportal_new_channels.htm) | [Generating New Groups in the Data Portal](../../procportal/procportal/procportal_new_groups.htm) | [Saving a Data Store](../../procportal/procportal/procportal_save_channels.htm) | [Specifying the Default Group in the Data Portal](../../procportal/procportal/procportal_default_group.htm)

#### Examples

[Concatenate Channels](../../exploff/examples/channelconcate.htm)

<!--NI_TOPIC bundle=diadem path=procauto/procauto/procauto_group_channel_generate.htm language=enus -->
## TOPIC 01558: Generating Channels and Groups with a Script

- bundle_id: `diadem`
- source_path: `procauto/procauto/procauto_group_channel_generate.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procauto/procauto/procauto_group_channel_generate.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating Scripts](../procauto/procauto_overview.htm) > [Working with Files](../procauto/procauto_overview_filesworking.htm) > Generating Channels and Groups with a Script

Generating Channels and Groups with a Script

Use the [Add for ChannelGroups](../../inavidata/methods/diacmpnt_method_add_idiademchannelgroups.htm) method to generate a new group in the Data Portal with a script. Use the [Add for Channels](../../inavidata/methods/diacmpnt_method_add_idiademchannels.htm) method to generate new channels in the Data Portal with a script. For example, to generate a new group, to generate a new channel in this group, and to fill this channel with numeric values with a script, complete the following steps:

1. Select the **DIAdem SCRIPT** panel.
2. Select **File»New»VBS Script** to create a new script.
3. Enter or copy the following text into the script editor: 
 VBScriptPython 
 [Copy script](javascript:void(0);) 
 Dim intLoop, oMyRoot, oMyGroup, oMyChannel
Set oMyRoot = Data.Root
Call oMyRoot.Clear() 'Delete all data
Set oMyGroup = oMyRoot.ChannelGroups.Add("MyGroup") 'Create new group
Set oMyChannel = oMyGroup.Channels.Add("MyChannel", DataTypeChnFloat64) 'Create new channel
For intLoop = 1 to 10
 oMyChannel.Values(intLoop) = intLoop 'Fill channel with data
Next [Copy script](javascript:void(0);) oMyRoot = dd.Data.Root 
oMyRoot.Clear() #Delete all data
oMyGroup = oMyRoot.ChannelGroups.Add("MyGroup") #Create new group
oMyChannel = oMyGroup.Channels.Add("MyChannel", dd.DataTypeChnFloat64) #Create new channel
for intLoop in range( 1, 10 + 1): 
 oMyChannel.Values(intLoop) = intLoop #Fill channel with data
4. Select **Script»Run VBS Script** to start the script.

The script uses the method [Clear for Root](../../inavidata/methods/diacmpnt_method_clear_idiademroot.htm) to delete the existing data store from the Data Portal. The script uses the [Add for ChannelGroups](../../inavidata/methods/diacmpnt_method_add_idiademchannelgroups.htm) method to generate a new group named MyGroup. The script uses the [Add for Channels](../../inavidata/methods/diacmpnt_method_add_idiademchannels.htm) method to generate a data channel named MyChannel. In the For loop the script fills the channel that has the [Values for Channel](../../inavidata/properties/diacmpnt_property_values_idiademchannel.htm) property with integer numbers from 1 to 10.

<!--NI_TOPIC bundle=diadem path=procauto/procauto/procauto_interaction.htm language=enus -->
## TOPIC 01559: Interrupting Scripts to Use DIAdem Interactively

- bundle_id: `diadem`
- source_path: `procauto/procauto/procauto_interaction.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procauto/procauto/procauto_interaction.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating Scripts](../procauto/procauto_overview.htm) > [More Procedures](../procauto/procauto_overview_furtherprocedures.htm) > Interrupting Scripts to Use DIAdem Interactively

Interrupting Scripts to Use DIAdem Interactively

Use the DIAdem interaction mode to interrupt the execution of a script. Afterwards you can use DIAdem as usual. When you stop the interaction mode, DIAdem continues to execute the script from the point of interruption onwards. To create and execute a script in the interaction mode, complete the following steps:

1. Select the **DIAdem SCRIPT** panel.
2. Select **File»New»VBS Script** to create a new script.
3. Enter or copy the following text into the script editor: 
 VBScriptPython 
 [Copy script](javascript:void(0);) 
 Dim oMyChannel
Set oMyChannel = Data.Root.ChannelGroups(1).Channels(1)
Call MsgBoxDisp("First value in channel Input before loading data: " & oMyChannel.Values(1))
Call MsgBoxDisp("Please load new data")
Call InteractionOn
Call MsgBoxDisp("First value in channel Input after loading data: " & oMyChannel.Values(1)) [Copy script](javascript:void(0);) oMyChannel = dd.Data.Root.ChannelGroups(1).Channels(1) 
dd.MsgBoxDisp("First value in channel Input before loading data: " + oMyChannel.Values(1)) 
dd.MsgBoxDisp("Please load new data") 
dd.InteractionOn 
dd.MsgBoxDisp("First value in channel Input after loading data: " + oMyChannel.Values(1))
4. Select **Script»Run VBS Script** to start the script. DIAdem displays the first value in the first data channel. DIAdem then prompts you to load new data.
5. Load a new data set.
6. To end interaction, select **File»End Interaction**. DIAdem continues to execute the script.

The [InteractionOn](../../comoff/interactionon.htm) command switches the script into the interaction mode so you can use DIAdem. When you stop the interaction mode, DIAdem continues to execute the script and returns the first value of the new data channel.

|  | Note Refer to the DIAdem Help under Programming Reference for more information. If the cursor in the script editor is in a keyword, press <F1> to open the Help file for this keyword. |
| --- | --- |

<!--NI_TOPIC bundle=diadem path=procpresent/axis_systems/procpres_2daxis_defining.htm language=enus -->
## TOPIC 01560: Displaying Curves in 2D Axis Systems

- bundle_id: `diadem`
- source_path: `procpresent/axis_systems/procpres_2daxis_defining.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procpresent/axis_systems/procpres_2daxis_defining.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating a Report](../procreport_overview.htm) > [Axis Systems](../axis_systems/procpres_axis_overview.htm) > Displaying Curves in 2D Axis Systems

Displaying Curves in 2D Axis Systems

Use 2D axis systems to display data channels as curves. To display a curve in a 2D axis system, complete the following steps:

|  | Note For this example, delete all the data in the Data Portal and load the data file example.tdm from the user folder. Refer to Loading Data into the Data Portal for further details. |
| --- | --- |

1. Select the **DIAdem REPORT** panel.
2. Select **File»New**.
3. Select **Insert»2D Axis System with Line** and click and drag to open the axis system in the worksheet.
4. Double-click the axis system.
5. Select **[1]/Time** as the x-channel.
6. Select **[1]/Speed** as the y-channel.
7. Select the **Line** display mode.
8. Click **OK** to close the dialog boxes. DIAdem displays the speed over time as a curve.

|  | Note You can modify the display mode for each curve definition, for example, you can change line display to bar display. Specify curve parameters such as line width in the Curve Parameters subdialog box. |
| --- | --- |

#### Examples

[2D Axis Synchronization](../../exploff/examples/2d_axissynchronization.htm) | [2D Axis System with a Legend](../../exploff/examples/expl_report_av7.htm) | [2D Axis System with Coordinate Displays](../../exploff/examples/expl_report_coordinates_1.htm) | [2D Axis System with Curve Coordinates](../../exploff/examples/expl_report_coordinate.htm) | [2D Axis System with Curve Display and Curve Coordinates](../../exploff/examples/expl_report_av12.htm) | [2D Axis System with Filled Curve Area and Color Shading in Background](../../exploff/examples/report_filled.htm) | [2D Axis System with Line and Symbol and with Constants](../../exploff/examples/expl_report_av10.htm) | [2D Axis System with Linear Axis Scaling](../../exploff/examples/expl_report_av8.htm) | [2D Axis System with Lines and Markers](../../exploff/examples/expl_report_marker.htm) | [2D Axis System with Logarithmic Axis Scaling](../../exploff/examples/expl_report_av9.htm) | [2D Axis System with Multiple Y-Axes](../../exploff/examples/expl_report_av3.htm) | [2D Axis System with Text from a Text Channel](../../exploff/examples/expl_report_av11.htm) | [2D Axis Systems and 3D Axis Systems with Legends](../../exploff/examples/expl_report_av34.htm) | [2D Axis Systems with Bar Display and Differential Display](../../exploff/examples/expl_report_av6.htm) | [2D Axis Systems with Bar Displays](../../exploff/examples/expl_report_av31.htm) | [2D Axis Systems with Channel-Related Coloring](../../exploff/examples/expl_report_2daxis_2.htm) | [2D Axis Systems with Different Axis Arrangements](../../exploff/examples/expl_report_av30.htm) | [2D Axis Systems with Different Curve Labels](../../exploff/examples/expl_report_av33.htm) | [2D Axis Systems with Different Line Displays](../../exploff/examples/expl_report_av35.htm) | [2D Axis Systems with Grid Displays](../../exploff/examples/expl_report_av32.htm) | [2D Axis Systems with Grouped Bars](../../exploff/examples/expl_report_2dbars_3.htm) | [2D Axis Systems with Logarithmic Axes](../../exploff/examples/expl_report_av36.htm) | [2D Axis Systems with Spike Displays and Constants](../../exploff/examples/expl_report_av38.htm) | [2D Axis Systems with Stacked Bars](../../exploff/examples/expl_report_2dbars_2.htm) | [2D Tables as Legend and Legend for Axis System Labeling](../../exploff/examples/report_2dlegendsnippet.htm) | [2D-Axis System with Scalable Background Graphic](../../exploff/examples/expl_report_photosynthetic_scalablebackground.htm) | [2D-Axis System with Scalable Background Map](../../exploff/examples/expl_report_map_scalablebackgroundimage.htm) | [Aachen Weather](../../exploff/examples/expl_report_ab1.htm) | [AC/DC Coupling](../../exploff/examples/expl_ac-dccoupling.htm) | [Adapted DIAdem Functions](../../exploff/examples/expl_script_av15.htm) | [Area Calculation between Curves](../../exploff/examples/expl_enclosedarea.htm) | [Background Segments in DIAdem REPORT](../../exploff/examples/expl_reportsegment.htm) | [Calculating and Displaying the Biorhythm](../../exploff/examples/expl_script_ab2.htm) | [Channel-Dependent Marker Color and Marker Size](../../exploff/examples/expl_marker_coloring2.htm) | [Color Marker Depending on Channel](../../exploff/examples/expl_marker_coloring.htm) | [Comparing Speed](../../exploff/examples/expl_script_av17.htm) | [Converting Units](../../exploff/examples/unitcalcandreport.htm) | [Copying Signals into Channel Groups](../../exploff/examples/expl_script_av23.htm) | [Detrending an Oscillation Signal](../../exploff/examples/expl_detrend.htm) | [Diesel Diagram](../../exploff/examples/expl_report_ab3.htm) | [Different Display Modes in DIAdem REPORT](../../exploff/examples/expl_report_av46.htm) | [Event Search](../../exploff/examples/expl_eventdetection.htm) | [Extracting Bits Using Curve Transformation](../../exploff/examples/report_curventransform.htm) | [Frequency Weighting (A-, B-, C-Filtering)](../../exploff/examples/expl_abcfiltering.htm) | [Grid Display in 2D Axis Systems](../../exploff/examples/grid_example.htm) | [Legend Template in DIAdem REPORT](../../exploff/examples/expl_reportcurvelegendcreate.htm) | [Merging Channels from Different Measurements](../../exploff/examples/merge_measurements.htm) | [Multi-Column Legend in One 2D Axis System](../../exploff/examples/report_2dlegend.htm) | [Multiple Sorting of Channel Data](../../exploff/examples/expl_channelsort.htm) | [Pareto Diagram](../../exploff/examples/expl_pareto.htm) | [Part Average Analysis](../../exploff/examples/paa_example.htm) | [Pump Diagram](../../exploff/examples/expl_report_ab5.htm) | [Resampling](../../exploff/examples/expl_resampling.htm) | [Searching for and Interpolating Invalid Values](../../exploff/examples/expl_script_av26.htm) | [Seismic Phase Picker](../../exploff/examples/expl_seismicphasepicking.htm) | [Specifying Intersection Points](../../exploff/examples/expl_script_av18.htm) | [Swivel Analysis at the Engine](../../exploff/examples/expl_swiveltest_report.htm) | [Test Rig Analysis](../../exploff/examples/expl_valve_analysis.htm) | [Wind Energy Plant](../../exploff/examples/expl_report_ab2.htm)

<!--NI_TOPIC bundle=diadem path=procsud/procsud/procsud_variables.htm language=enus -->
## TOPIC 01561: Transferring User Dialog Box Entries to DIAdem

- bundle_id: `diadem`
- source_path: `procsud/procsud/procsud_variables.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procsud/procsud/procsud_variables.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating User Dialog Boxes](../procsud/procsud_overview.htm) > Transferring User Dialog Box Entries to DIAdem

Transferring User Dialog Box Entries to DIAdem

Use this variable to transfer the settings in user dialog boxes to DIAdem. Complete the following steps to transfer a selection in a selection field to DIAdem:

1. Select the **DIAdem SCRIPT** panel.

1. Select **Edit»Create Dialog Box**.
2. Select **View»Catalog**.
3. Click the **OK and Cancel** control group in the **Catalog** window and click and drag the group into the dialog box.
4. Click the **ComboBox** control on the **Controls** bar.
5. Drag open the control in the dialog box.
6. Click the column to the right of **ListItems** in the **Properties** tab. The ComboBox must be selected.
7. The dialog editor opens the **ListItems** dialog box.
8. Click **Add** twice and enter Value0 and Value1 as the names.
9. Click **OK**.
10. Click the column to the right of the **Variable** field on the **Properties** tab.
11. Enter **L1**.

|  | Note If you enter a variable here which is unknown to DIAdem, DIAdem prompts you to add information on the type, storage mode, dimension, and the reset behavior of this variable. During the dialog box runtime, the variable you select here must conform to the variable definition in DIAdem. Select Edit»Variables and open the DIAdem Variables dialog box to display the properties of the registered variable, to enter new variables, and to delete existing variables.Refer to the page on Variable Types for Controls for a list of the variable types that you can assign to the controls. |
| --- | --- |

1. Select **File»Save As** and save the file as Test.sud.
2. Close the dialog editor and switch to DIAdem.
3. Select **File»New** to create a new script.
4. Enter or copy the following text into the script editor: 
 [Copy script](javascript:void(0);) 
 L1 = 1 'Set the default value for the variable L1
Call SUDDlgShow("Dlg1","Test.sud") 'Shows the dialog
Call MsgBoxDisp("Selected value is " & L1) 'Shows the selected value of L1
5. Select **Script»Run VBS Script** to start the script.
6. Select an entry from the selection field.
7. Close the user dialog box with **OK** or **Cancel.**

If you close the user dialog box by clicking **OK**, the user dialog box returns the value L1, which you selected in the selection box, to the calling script. If you close the user dialog box by clicking **Cancel**, the user dialog box resets the L1 value to the original value.

#### Examples

[Analyzing and Displaying Channels Section by Section](../../exploff/examples/expl_viewdisplaychnparts.htm) | [Checking Dialog Box Entries](../../exploff/examples/expl_script_av16.htm) | [Dynamic User Dialog Box](../../exploff/examples/expl_script_av11.htm) | [Translating User Dialog Boxes](../../exploff/examples/example_sud_translate.htm) | [User Dialog Box for Entering Text and Numbers](../../exploff/examples/expl_script_av2.htm) | [User Dialog Box for Sequence Control](../../exploff/examples/expl_script_av13.htm) | [User Dialog Box in DIAdem VIEW](../../exploff/examples/expl_viewcreatecurve.htm) | [User Dialog Box in VIEW for the Calculation of the FFT and Harmonic Frequencies](../../exploff/examples/view_fft_analysis.htm) | [User Dialog Box with Changing Background Color](../../exploff/examples/expl_script_av9.htm) | [User Dialog Box with Curve Preview and Slider Control](../../exploff/examples/expl_curve2dpreview.htm) | [User Dialog Box with Extended Table](../../exploff/examples/expl_weather_info.htm) | [User Dialog Box with Internet Explorer](../../exploff/examples/expl_script_av22.htm) | [User Dialog Box with Scalable Table](../../exploff/examples/expl_zoom_xtable_example.htm) | [User Dialog Box with Selection Lists](../../exploff/examples/expl_script_av7.htm) | [User Dialog Box with Selection Lists](../../exploff/examples/expl_script_av8.htm) | [User Dialog Box with Subdialog Boxes](../../exploff/examples/expl_script_av12.htm) | [User Dialog Box with Tables](../../exploff/examples/expl_script_av10.htm) | [User Dialog Box with Tree](../../exploff/examples/expl_treecontrol.htm) | [Wizard for Tolerance Evaluation](../../exploff/examples/expl_tolerance.htm)

<!--NI_TOPIC bundle=diadem path=procsud/procsud/procsud_withoutvar.htm language=enus -->
## TOPIC 01562: Creating a User Dialog Box without Linking Variables

- bundle_id: `diadem`
- source_path: `procsud/procsud/procsud_withoutvar.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procsud/procsud/procsud_withoutvar.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating User Dialog Boxes](../procsud/procsud_overview.htm) > Creating a User Dialog Box without Linking Variables

Creating a User Dialog Box without Linking Variables

Use the Text property to access the settings made in user dialog boxes.

Complete the following steps to generate a user dialog box that reads in two numbers, calculates the sum, and displays the results in a text.

1. Select the **DIAdem SCRIPT** panel.

1. Select **Edit»Create Dialog Box**.
2. Click the **Text** control on the **Controls** bar.
3. Drag open the control in the dialog box.
4. Click the column to the right of the **Text** field on the **Properties** tab. Text1 must be selected. EnterFirst Value:as the text.
5. Click the **EditBox** control on the **Controls** bar.
6. Drag open the control in the dialog box. Position EditBox1 next to the text.
7. Click the column to the right of the **ObjectCode** field on the **Properties** tab. EditBox1 must be selected. Enter ebFirstVal as the name.
8. Click the **Text** control on the **Controls** bar.
9. Drag open the control in the dialog box.
10. Click the column to the right of the **Text** field on the **Properties** tab. Text2 must be selected. EnterSecond Value:as the text.
11. Click the **EditBox** control on the **Controls** bar.
12. Drag open the control in the dialog box. Position EditBox2 next to the text.
13. Click the column to the right of the **ObjectCode** field on the **Properties** tab. EditBox2 must be selected. Enter ebSecondVal as the name.
14. Click the **Text** control on the **Controls** bar.
15. Drag open the control in the dialog box. Position the text below the textboxes.
16. Click the column to the right of the **Text** field on the **Properties** tab. Text3 must be selected. EnterResult:as the text.
17. Click the **Button** control on the **Controls** bar.
18. Drag open the control in the dialog box. Position the button below the input text.
19. Click the column to the right of the **Text** field in the **Properties** tab and enter Calculate. Button1 must be selected.
20. Click the column to the right of the **EventClick** field on the **Events** tab. Button1 must be selected.
21. Enter or copy the following text into the script editor: 
 [Copy script](javascript:void(0);) 
 Sub Button1_EventClick(ByRef This)
 Dim dVal : dVal = val(ebFirstVal.Text) + val(ebSecondVal.Text)
 Text3.Text = "Result : " & str(dVal)
End Sub 
 [IMAGE alt='image' src='../image/note.gif']**Note**Add the above text to the lines generated automatically by the script editor.
22. Select **File»Save As** and save the file as Test.sud.
23. Select **View»Test in DIAdem**.
24. Enable the first input field and enter a number. Enable the second input field and also enter a number. Click Calculate. 
 The user dialog box calculates the sum of the two numbers and displays the result in a text.
25. Close the user dialog box in DIAdem.
26. Close the dialog editor.

#### Examples

[Analyzing and Displaying Channels Section by Section](../../exploff/examples/expl_viewdisplaychnparts.htm) | [Checking Dialog Box Entries](../../exploff/examples/expl_script_av16.htm) | [Dynamic User Dialog Box](../../exploff/examples/expl_script_av11.htm) | [Translating User Dialog Boxes](../../exploff/examples/example_sud_translate.htm) | [User Dialog Box for Entering Text and Numbers](../../exploff/examples/expl_script_av2.htm) | [User Dialog Box for Sequence Control](../../exploff/examples/expl_script_av13.htm) | [User Dialog Box in DIAdem VIEW](../../exploff/examples/expl_viewcreatecurve.htm) | [User Dialog Box in VIEW for the Calculation of the FFT and Harmonic Frequencies](../../exploff/examples/view_fft_analysis.htm) | [User Dialog Box with Changing Background Color](../../exploff/examples/expl_script_av9.htm) | [User Dialog Box with Curve Preview and Slider Control](../../exploff/examples/expl_curve2dpreview.htm) | [User Dialog Box with Extended Table](../../exploff/examples/expl_weather_info.htm) | [User Dialog Box with Internet Explorer](../../exploff/examples/expl_script_av22.htm) | [User Dialog Box with Scalable Table](../../exploff/examples/expl_zoom_xtable_example.htm) | [User Dialog Box with Selection Lists](../../exploff/examples/expl_script_av7.htm) | [User Dialog Box with Selection Lists](../../exploff/examples/expl_script_av8.htm) | [User Dialog Box with Subdialog Boxes](../../exploff/examples/expl_script_av12.htm) | [User Dialog Box with Tables](../../exploff/examples/expl_script_av10.htm) | [User Dialog Box with Tree](../../exploff/examples/expl_treecontrol.htm) | [Wizard for Tolerance Evaluation](../../exploff/examples/expl_tolerance.htm)

<!--NI_TOPIC bundle=diadem path=procsud/procsud/procsud_xtable.htm language=enus -->
## TOPIC 01563: Creating an Extended Table

- bundle_id: `diadem`
- source_path: `procsud/procsud/procsud_xtable.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procsud/procsud/procsud_xtable.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Creating User Dialog Boxes](../procsud/procsud_overview.htm) > Creating an Extended Table

Creating an Extended Table

Use the [XTable](../../sudref/objects/sud_objects_tovirtgridctrl.htm) control to create an extended table in a user dialog box. Use the events EventValSet and EventValGet to control the contents of the extended table. The user dialog box triggers the [EventValSet](../../sudref/events/sud_event_eventvalset.htm) event to save the value of a cell from the extended table. The user dialog box uses the [EventValGet](../../sudref/events/sud_event_eventvalget.htm) event to display a value in a cell of the extended table.

Complete the following steps to create a user dialog box with an extended table that contains the values of four data channels. Design the extended table so that the table cells are yellow and the edited table cell is red.

|  | Note For this example, delete all the data in the Data Portal and load the data file Example.tdm from the library folder. |
| --- | --- |

1. Select the **DIAdem SCRIPT** panel.

1. Select **Edit»Create Dialog Box**.
2. Click the **XTable** control on the **Controls** bar.
3. Drag open the control in the dialog box.
4. Click the column on the right of the **Columns** field in the **Properties** tab. XTable1 must be selected.
5. Click **Add** in the **Configure Columns** dialog box to add a <Default> type column to the extended table. The <Default> column type corresponds to the EditBox control.
6. Click the **...** button to the right of the **Cell type** in the **<Default>** area.
7. Configure the **Display control**. Click the right column next to the **BackColor** field and select the color yellow.
8. Click **Entry control** to configure the input control. Click the right column next to the **BackColor** field and select the color red. Click the right column next to the **ForeColor** field and select the color white.
9. Click **OK** to close the dialog boxes.
10. Click**...** in the **EventInitialize** field on the **Events** tab. XTable1 must be selected.
11. Enter or copy the following text into the script editor: 
 [Copy script](javascript:void(0);) 
 Sub XTable1_EventInitialize(ByRef This)
 This.RowCount = Data.GetChannel("[1]/[1]").Size ' same number of table rows as number of values in first channel
End Sub 
 [IMAGE alt='image' src='../image/note.gif']**Note** Add the above text to the lines generated automatically by the script editor.

1. Select **View»Script View**.
2. Click **...** in the **EventValGet** field on the **Events** tab. XTable1 must be selected.
3. Enter or copy the following text into the script editor: 
 [Copy script](javascript:void(0);) 
 Sub XTable1_EventValGet(ByRef This, Row, Col, ByRef Cell, IsInputCell)
 If Row = 0 Then ' set title of table
 Select Case Col
 Case 0
 Cell.Text = "" ' row with line numbers doesn't contain title
 Case Else
 Cell.Text = Data.GetChannel(Col).Name ' display channel name
 End Select 
 Else
 Select Case Col
 Case 0
 Cell.Text = Row ' display line number
 Case Else
 Cell.Text = Str(Data.GetChannel(Col).Values(Row)) ' display channel value
 End Select 
 End If
End Sub 
 [IMAGE alt='image' src='../image/note.gif']**Note** Add the above text to the lines generated automatically by the script editor.
4. Select **View»Script View**.
5. Click **...** in the **EventValSet** field on the **Events** tab. XTable1 must be selected.
6. Enter or copy the following text into the script editor: 
 [Copy script](javascript:void(0);) 
 Sub XTable1_EventValSet(ByRef This, Row, Col, ByRef Cell)
 If Row > 0 And Col > 0 Then
 Data.GetChannel(Col).Values(Row) = Val(Eval(Cell.Text)) ' entered value included in channel
 End If
End Sub 
 [IMAGE alt='image' src='../image/note.gif']**Note**Add the above text to the lines generated automatically by the script editor.
7. Select **View»Script View**.
8. Select **File»Save As** and save the file as Test.sud.
9. Select View»Test in DIAdem . The extended table displays the table cells in yellow. As soon as you edit a table cell, the cell appears in red.
10. Close the user dialog box in DIAdem.
11. Close the dialog editor.

#### Examples

[Analyzing and Displaying Channels Section by Section](../../exploff/examples/expl_viewdisplaychnparts.htm) | [Checking Dialog Box Entries](../../exploff/examples/expl_script_av16.htm) | [Dynamic User Dialog Box](../../exploff/examples/expl_script_av11.htm) | [Translating User Dialog Boxes](../../exploff/examples/example_sud_translate.htm) | [User Dialog Box for Entering Text and Numbers](../../exploff/examples/expl_script_av2.htm) | [User Dialog Box for Sequence Control](../../exploff/examples/expl_script_av13.htm) | [User Dialog Box in DIAdem VIEW](../../exploff/examples/expl_viewcreatecurve.htm) | [User Dialog Box in VIEW for the Calculation of the FFT and Harmonic Frequencies](../../exploff/examples/view_fft_analysis.htm) | [User Dialog Box with Changing Background Color](../../exploff/examples/expl_script_av9.htm) | [User Dialog Box with Curve Preview and Slider Control](../../exploff/examples/expl_curve2dpreview.htm) | [User Dialog Box with Extended Table](../../exploff/examples/expl_weather_info.htm) | [User Dialog Box with Internet Explorer](../../exploff/examples/expl_script_av22.htm) | [User Dialog Box with Scalable Table](../../exploff/examples/expl_zoom_xtable_example.htm) | [User Dialog Box with Selection Lists](../../exploff/examples/expl_script_av7.htm) | [User Dialog Box with Selection Lists](../../exploff/examples/expl_script_av8.htm) | [User Dialog Box with Subdialog Boxes](../../exploff/examples/expl_script_av12.htm) | [User Dialog Box with Tables](../../exploff/examples/expl_script_av10.htm) | [User Dialog Box with Tree](../../exploff/examples/expl_treecontrol.htm) | [Wizard for Tolerance Evaluation](../../exploff/examples/expl_tolerance.htm)

<!--NI_TOPIC bundle=diadem path=procunitcatalog/procunitcatalog/procunitcatalog_calculate_units.htm language=enus -->
## TOPIC 01564: Converting Channel Units in DIAdem ANALYSIS

- bundle_id: `diadem`
- source_path: `procunitcatalog/procunitcatalog/procunitcatalog_calculate_units.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procunitcatalog/procunitcatalog/procunitcatalog_calculate_units.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Working with Units](../procunitcatalog/procunitcatalog_overview.htm) > Converting Channel Units in DIAdem ANALYSIS

Converting Channel Units in DIAdem ANALYSIS

Use the [Convert channel unit](../../dlgmaths/calc_basis_dlg/dlgunitcatalog_calculate_unit_dialog.htm) function to convert the values of a channel into a new unit. To convert channel values into a new unit, complete the following steps:

1. Select the **DIAdem ANALYSIS** panel.
2. Open the function group **Channel Functions**.
3. Select **Convert Channel Unit**. DIAdem opens the dialog box.
4. Select the channel with the values that you want to convert to a new unit.

|  | Note If you select a channel that has a unit that is not included in the units catalog, DIAdem disables the other settings in the dialog box. Alternatively, you can assign a different unit to the channel. |
| --- | --- |

1. Select the unit to which you want DIAdem to convert the channel values. DIAdem automatically displays the units of the physical quantity, to which the unit of the selected channel is assigned.

1. If required, select a different unit set. DIAdem displays only the unit sets that contain the physical quantity of the selected channel.
2. Click **Calculate**. DIAdem assigns a new unit to the selected channel and converts the values of the channel to the new unit.

|  | Note If you select the Store result in original channel checkbox, DIAdem overwrites the values of the input channels. Do not select this setting if you want to use the input channels again. |
| --- | --- |

1. Click **Close** to close the dialog box.

#### Examples

[Converting Units](../../exploff/examples/unitcalcandreport.htm)

<!--NI_TOPIC bundle=diadem path=procunitcatalog/procunitcatalog/procunitcatalog_convert_units.htm language=enus -->
## TOPIC 01565: Replacing and Converting Channel Units in the Input Help

- bundle_id: `diadem`
- source_path: `procunitcatalog/procunitcatalog/procunitcatalog_convert_units.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procunitcatalog/procunitcatalog/procunitcatalog_convert_units.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Working with Units](../procunitcatalog/procunitcatalog_overview.htm) > Replacing and Converting Channel Units in the Input Help

Replacing and Converting Channel Units in the Input Help

Use the **Channel Unit: Symbol Input Help** dialog box to replace the unit of a channel with a different unit, without modifying the values of the channel. To replace the unit of the channel that is selected in the Data Portal with a different unit, complete the following steps:

1. Open the **Data Portal**.
2. Select the channel of which you want to replace the unit.
3. Click the input space of the **Unit** cell in the properties display of the Data Portal.
4. Click the **...** button of the cell. DIAdem opens the [Channel Unit: Symbol Input Help](../../dlgunitcatalog/dlgunitcatalog/dlgunitcatalog_channelunit_symbolassistant_dialog.htm) dialog box.

|  | Note If you select a waveform channel in the Data Portal, and you select Waveform x-unit in the properties display, you open the Waveform X-Unit: Symbol Input Help dialog box. In this dialog box, you assign a new unit and a new unit symbol to the x-part of a waveform channel. |
| --- | --- |

1. Select a unit set.
2. Select a physical quantity.
3. Select the unit.
4. Click **Replace**. DIAdem replaces the unit without converting the channel values to the new unit.

|  | Note If you click Convert, DIAdem also converts the channel values into the new unit. |
| --- | --- |

1. Click OK to close the dialog box.

|  | Note If the unit of the selected channel does not exist in the units catalog, click the Add button in the Channel Unit: Symbol Input Help dialog box. |
| --- | --- |

#### Examples

[Converting Units](../../exploff/examples/unitcalcandreport.htm)

<!--NI_TOPIC bundle=diadem path=procunitcatalog/procunitcatalog/procunitcatalog_convert_unitset.htm language=enus -->
## TOPIC 01566: Converting Channels According to a Unit Set

- bundle_id: `diadem`
- source_path: `procunitcatalog/procunitcatalog/procunitcatalog_convert_unitset.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procunitcatalog/procunitcatalog/procunitcatalog_convert_unitset.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[Working with Units](../procunitcatalog/procunitcatalog_overview.htm) > Converting Channels According to a Unit Set

Converting Channels According to a Unit Set

Use the **Convert to unit set** function to convert several channels to a new unit according to a predefined unit set. Which unit DIAdem converts the units of the selected channels to, depends on the [default units](../../dlgunitcatalog/dlgunitcatalog/dlgunitcatalog_edit_units_dialog.htm) of the [physical quantities](../../genshell/genshell/genunitcatalog_basics.htm). For example, you can use this function to convert several channels from the international unit system into a local unit system in one step.

To convert several channel values according to a unit set, complete the following steps:

1. Select the **DIAdem ANALYSIS** panel.
2. Open the function group **Channel Functions**.
3. Select [Convert to Unit Set](../../dlgmaths/calc_basis_dlg/dlgunitcatalog_calculate_toset_dialog.htm). DIAdem opens the dialog box.
4. Drag and drop the channel of which you want to convert the unit, from the Data Portal into the dialog box.
5. Select the checkbox **Ignore unknown units**. DIAdem only executes the calculation if it recognizes all the units of the selected channels.
6. Select the unit set that has the default units that you want DIAdem to assign to the selected channels.
7. Click **Calculate**. DIAdem replaces the units of the selected channels and converts the channel values according to the new units.
8. Click Close to close the dialog box.

#### Examples

[Converting Units](../../exploff/examples/unitcalcandreport.htm)

<!--NI_TOPIC bundle=diadem path=procunitcatalog/procunitcatalog/procunitcatalog_overview.htm language=enus -->
## TOPIC 01567: Working with Units in DIAdem

- bundle_id: `diadem`
- source_path: `procunitcatalog/procunitcatalog/procunitcatalog_overview.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/procunitcatalog/procunitcatalog/procunitcatalog_overview.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

Working with Units in DIAdem

Working with Units in DIAdem

The subordinate topics contained in the tree on the contents tab of the Help describe how to edit the DIAdem units catalog and to customize the DIAdem units catalog to your requirements. You also learn how to assign new units to channels and to convert channel values to new units.

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_add_irepcurvelegendcontentcolumnslistint.htm language=enus -->
## TOPIC 01568: Method: Add for CurveLegendColumns

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_add_irepcurvelegendcontentcolumnslistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_add_irepcurvelegendcontentcolumnslistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Add for CurveLegendColumns

Method: Add for CurveLegendColumns

Adds a column to the curve legend of a 2D axis system in DIAdem REPORT.

```text
Set oCurveLegendColumnBase = Object.Add()
```

| Object | CurveLegendColumnsObject with this method |
| --- | --- |
| oCurveLegendColumnBase | CurveLegendColumnBaseReturned object |

The following example generates a 2D axis system with a curve, displays the associated legend, and adds a column which contains the channel comment to this legend:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMy2DaxisSystem, oMy2DCurve, oMyLegendColumn
Call Report.NewLayout()
Set oMy2DaxisSystem = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem,"My2DAxisSystem")
Set oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(e2DShapeLine, "MyNewCurve")
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]"
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]"
oMy2DaxisSystem.CurveLegend.Visible = True
Set oMyLegendColumn = oMy2DaxisSystem.CurveLegend.Columns.Add()
oMyLegendColumn.Type = eLegendTextComment
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Report.NewLayout() 
oMy2DaxisSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem,"My2DAxisSystem") 
oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(dd.e2DShapeLine, "MyNewCurve") 
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]" 
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]" 
oMy2DaxisSystem.CurveLegend.Visible = True 
oMyLegendColumn = oMy2DaxisSystem.CurveLegend.Columns.Add() 
oMyLegendColumn.Type = dd.eLegendTextComment 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_add_irepcustomscalingaxissystem2dlistint.htm language=enus -->
## TOPIC 01569: Method: Add for AxisSystem2DCustomScalings

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_add_irepcustomscalingaxissystem2dlistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_add_irepcustomscalingaxissystem2dlistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Add for AxisSystem2DCustomScalings

Method: Add for AxisSystem2DCustomScalings

Adds a user-defined axis scaling to a 2D axis system in DIAdem REPORT.

```text
Set oAxisSystem2DCustomScaling = Object.Add(ID)
```

| Object | AxisSystem2DCustomScalingsObject with this method |
| --- | --- |
| ID | StringSpecifies the ID of the user-defined scaling. |
| oAxisSystem2DCustomScaling | AxisSystem2DCustomScalingReturned object |

|  | Note To test the following example scripts, first save the bottom script and select Settings»Extensions»User Commands to register it as a user command. |
| --- | --- |

The following example creates a 2D axis system with a curve and assigns the user-defined axis scaling with the ID MotorWarmScaling to the y-axis.

[Copy script](javascript:void(0);)

```text
Dim oMy2DAxisSystem, oMyPos, oMyYScaling, oMy2DCurve, oMyCustomScalings, oMyCustomScalingObj
Call Report.NewLayout()
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Example.tdm","TDM","")
'Creating Axis System and Curve
Set oMy2DAxisSystem = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem, "My2DAxisSystem")
Set oMyPos = oMy2DAxisSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80
Set oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(e2DShapeLine, "My2DDCurve")
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]"
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]"
'Creating Custom Scaling
Set oMyCustomScalings = Report.Settings.CustomScaling.AxisSystem2DList
Call oMyCustomScalings.RemoveAll
Set oMyCustomScalingObj = oMyCustomScalings.Add("MotorWarmScaling")
oMyCustomScalingObj.BaseScalingType = eAxisAutoScalingCompleteAutomatic
oMyCustomScalingObj.EventName = "MyCustomScalingEvent2D"
oMyCustomScalingObj.Label = "LabelForMotorWarmScaling"
'Assigning Custom Scaling to Axis
Set oMyYScaling = oMy2DAxisSystem.YAxis.Scaling
oMyYScaling.AutoScalingType = eAxisAutoScalingCustom
oMyYScaling.CustomScalingID = "MotorWarmScaling"
Call Report.Refresh()
```

The user command calculates the values for the axis scaling. The user command receives a parameter. This parameter is a [CustomScalingAxisSystem2DContext object](../objects/report_objects_irepcustomscalingaxissystem2dcontextint.htm) and provides information about the axis system and about the ID of the user-defined axis scaling.

[Copy script](javascript:void(0);)

```text
Sub MyCustomScalingEvent2D(Context)
  Dim oMyAxisSystem, oMyAxis, MinMax
  Set oMyAxisSystem = Context.AxisSystem
  If Context.AxisType = e2DAxisTypeY Then
    Set oMyAxis = oMyAxisSystem.YAxisList(Context.AxisNumber)
    MinMax = ValMax(Abs(oMyAxis.Scaling.End),Abs(oMyAxis.Scaling.Begin))
    oMyAxis.Scaling.Origin = oMyAxis.Scaling.Begin
    oMyAxis.Scaling.Begin = -MinMax
    oMyAxis.Scaling.End = +MinMax
  End If
End Sub
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_add_irepcustomscalingaxissystem2dscaledlistint.htm language=enus -->
## TOPIC 01570: Method: Add for AxisSystem2DScaledCustomScalings

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_add_irepcustomscalingaxissystem2dscaledlistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_add_irepcustomscalingaxissystem2dscaledlistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Add for AxisSystem2DScaledCustomScalings

Method: Add for AxisSystem2DScaledCustomScalings

Adds a user-defined axis scaling to a 2D axis system in DIAdem REPORT in scaled display.

```text
Set oAxisSystem2DScaledCustomScaling = Object.Add(ID)
```

| Object | AxisSystem2DScaledCustomScalingsObject with this method |
| --- | --- |
| ID | StringSpecifies the ID of the user-defined axis scaling. |
| oAxisSystem2DScaledCustomScaling | AxisSystem2DScaledCustomScalingReturned object |

The following example creates the scaled display of a 2D axis system with a curve and assigns the user-defined axis scaling with the ID MotorWarmScaling to the y-axis:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oDisplayDimensions, oMy2DAxisSystem, oMyPos, oMyYScaling, oMy2DCurve, oMyCustomScalings, oMyCustomScalingObj
Call Report.NewLayout()
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Example.tdm","TDM","")
'Activating Scaled Mode
Set oDisplayDimensions = Report.Settings.Page.Dimensions
oDisplayDimensions.ScaledHeight = 20
oDisplayDimensions.ScaledWidth = 30
oDisplayDimensions.UseScaledOutput = True
'Creating Axis System and Curve
Set oMy2DAxisSystem = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem, "My2DAxisSystem")
Set oMyPos = oMy2DAxisSystem.Position.ByCoordinate
oMyPos.X1 = 5
oMyPos.X2 = 25
oMyPos.Y1 = 5
oMyPos.Y2 = 15
Set oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(e2DShapeLine, "My2DDCurve")
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]"
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]"
'Creating Custom Scaling
Set oMyCustomScalings = Report.Settings.CustomScaling.AxisSystem2DScaledList
Call oMyCustomScalings.RemoveAll
Set oMyCustomScalingObj = oMyCustomScalings.Add("MotorWarmScaling")
oMyCustomScalingObj.BaseScalingType = eAxisAutoScalingCompleteAutomatic
oMyCustomScalingObj.EventName = "MyCustomScalingEvent2D"
oMyCustomScalingObj.Label = "LabelForMotorWarmScaling"
'Assigning Custom Scaling to Axis
Set oMyYScaling = oMy2DAxisSystem.YAxis.Scaling
oMyYScaling.AutoScalingType = eAxisAutoScalingCustom
oMyYScaling.CustomScalingID = "MotorWarmScaling"
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Report.NewLayout() 
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Example.tdm","TDM","") 
#Activating Scaled Mode
oDisplayDimensions = dd.Report.Settings.Page.Dimensions 
oDisplayDimensions.ScaledHeight = 20 
oDisplayDimensions.ScaledWidth = 30 
oDisplayDimensions.UseScaledOutput = True 
#Creating Axis System and Curve
oMy2DAxisSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem, "My2DAxisSystem") 
oMyPos = oMy2DAxisSystem.Position.ByCoordinate 
oMyPos.X1 = 5 
oMyPos.X2 = 25 
oMyPos.Y1 = 5 
oMyPos.Y2 = 15 
oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(dd.e2DShapeLine, "My2DDCurve") 
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]" 
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]" 
#Creating Custom Scaling
oMyCustomScalings = dd.Report.Settings.CustomScaling.AxisSystem2DScaledList 
oMyCustomScalings.RemoveAll() 
oMyCustomScalingObj = oMyCustomScalings.Add("MotorWarmScaling") 
oMyCustomScalingObj.BaseScalingType = dd.eAxisAutoScalingCompleteAutomatic 
oMyCustomScalingObj.EventName = "MyCustomScalingEvent2D" 
oMyCustomScalingObj.Label = "LabelForMotorWarmScaling" 
#Assigning Custom Scaling to Axis
oMyYScaling = oMy2DAxisSystem.YAxis.Scaling 
oMyYScaling.AutoScalingType = dd.eAxisAutoScalingCustom 
oMyYScaling.CustomScalingID = "MotorWarmScaling" 
dd.Report.Refresh() 
```

The user command calculates the values for the axis scaling. The user command receives a parameter. This parameter is a [CustomScalingAxisSystem2DScaledContext object](../objects/report_objects_irepcustomscalingaxissystem2dscaledcontextint.htm) and provides information about the axis system and about the ID of the user-defined axis scaling:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub MyCustomScalingEvent2D(Context)
  Dim oMyAxisSystem, oMyAxis, MinMax
  Set oMyAxisSystem = Context.AxisSystem
  If Context.AxisType = e2DAxisTypeY Then
    Set oMyAxis = oMyAxisSystem.YAxisList(Context.AxisNumber)
    MinMax = ValMax(Abs(oMyAxis.Scaling.End),Abs(oMyAxis.Scaling.Begin))
    oMyAxis.Scaling.Origin = oMyAxis.Scaling.Begin
    oMyAxis.Scaling.Begin = -MinMax
    oMyAxis.Scaling.End = +MinMax
  End If
End Sub
```

[Copy script](javascript:void(0);)

```text
def MyCustomScalingEvent2D(Context): 
    oMyAxisSystem = Context.AxisSystem 
    if Context.AxisType == dd.e2DAxisTypeY : 
        oMyAxis = oMyAxisSystem.YAxisList(Context.AxisNumber) 
        MinMax = dd.ValMax(Abs(oMyAxis.Scaling.End),Abs(oMyAxis.Scaling.Begin)) 
        oMyAxis.Scaling.Origin = oMyAxis.Scaling.Begin 
        oMyAxis.Scaling.Begin = -MinMax 
        oMyAxis.Scaling.End = +MinMax 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_convertpagexypositiontoangle_ireppolarint.htm language=enus -->
## TOPIC 01571: Method: ConvertPageXYPositionToAngle for PolarSystem

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_convertpagexypositiontoangle_ireppolarint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_convertpagexypositiontoangle_ireppolarint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ConvertPageXYPositionToAngle for PolarSystem

Method: ConvertPageXYPositionToAngle for PolarSystem

Converts in a polar axis system in DIAdem REPORT a page coordinate into an angle.

```text
iConvertPageXYPositionToAngle = Object.ConvertPageXYPositionToAngle(X, Y)
```

| Object | PolarSystemObject with this method |
| --- | --- |
| X | DoubleContains the x-page coordinate. |
| Y | DoubleContains the y-page coordinate. |
| iConvertPageXYPositionToAngle | DoubleReceives the converted angle. |

|  | Note To test the example script, you must first save the second script and register it as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example creates an polar axis system and assigns the user command MyClickEvent to the [OnAxisSystemPolar for ClickedWithKeyEvents](../properties/report_property_onaxissystempolar_irepreportonclickedwithkeyint.htm) property:

[Copy script](javascript:void(0);)

```text
Dim oMyPolarSystem, oMyPos, oMyPolarCurve
Call Report.NewLayout()
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Report_Data.tdm","TDM","")

Set oMyPolarSystem = Report.ActiveSheet.Objects.Add(eReportObjectPolarSystem, "MyPolarSystem")
Set oMyPos = oMyPolarSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80

Set oMyPolarCurve = oMyPolarSystem.CurvesPolar.Add(ePolarShapeLine, "MyPolarCurve")
oMyPolarCurve.Shape.XChannel.Reference = "[5]/[1]"
oMyPolarCurve.Shape.YChannel.Reference = "[5]/[4]"

'This event will be raised if you click a 2D axis system while you press a keyboard key
Report.Events.ClickedWithKey.OnAxisSystemPolar = "MyClickEvent"
Call Report.Refresh()
```

If you press the <C> key and click the axis system, the user command specifies the mouse position. The example calculates the radius and the angle from the mouse position and displays them in a message. The user command receives a parameter. The first parameter corresponds to a [PolarAxisSystemClickedWithKeyContext](../objects/report_objects_ireppolaraxissystemclickedwithkeycontextint.htm) object and provides information about the polar axis system in DIAdem REPORT.

[Copy script](javascript:void(0);)

```text
Sub MyClickEvent(Context)
  Dim oSystem, oCurve, Lenght, Angle, oXAxis, oYAxis, oPoint, sgMessage, oChannel, oSubObject
  Context.DoProceed = False'True
  'Check the key
  If Chr(Context.KeyValue) = "C" or Chr(Context.KeyValue) = "c" Then
    Context.DoProceed = True
    Set oSystem = Context.AxisSystemPolar

    'Map cursor point to length and angle
    Lenght = oSystem.ConvertPageXYPositionToLength(Context.Position.X, Context.Position.Y)
    Angle  = oSystem.ConvertPageXYPositionToAngle(Context.Position.X, Context.Position.Y)

    'Build message text
    sgMessage =  "Lenght: " & VBTab & Lenght & VBCrLf & "Angle: " & VBTab & Angle
    Call MsgBoxDisp(sgMessage,,,,5,True)
  End If
End Sub
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_convertpagexypositiontolength_ireppolarint.htm language=enus -->
## TOPIC 01572: Method: ConvertPageXYPositionToLength for PolarSystem

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_convertpagexypositiontolength_ireppolarint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_convertpagexypositiontolength_ireppolarint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ConvertPageXYPositionToLength for PolarSystem

Method: ConvertPageXYPositionToLength for PolarSystem

Converts in a polar axis system in DIAdem REPORT a page coordinate into a radius.

```text
iConvertPageXYPositionToLength = Object.ConvertPageXYPositionToLength(X, Y)
```

| Object | PolarSystemObject with this method |
| --- | --- |
| X | DoubleContains the x-page coordinate. |
| Y | DoubleContains the y-page coordinate. |
| iConvertPageXYPositionToLength | DoubleReceives the converted radius. |

|  | Note To test the example script, you must first save the second script and register it as a user command in the dialog box that opens when you select Settings»Extensions»User Commands. |
| --- | --- |

The following example creates an polar axis system and assigns the user command MyClickEvent to the [OnAxisSystemPolar for ClickedWithKeyEvents](../properties/report_property_onaxissystempolar_irepreportonclickedwithkeyint.htm) property:

[Copy script](javascript:void(0);)

```text
Dim oMyPolarSystem, oMyPos, oMyPolarCurve
Call Report.NewLayout()
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Report_Data.tdm","TDM","")

Set oMyPolarSystem = Report.ActiveSheet.Objects.Add(eReportObjectPolarSystem, "MyPolarSystem")
Set oMyPos = oMyPolarSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80

Set oMyPolarCurve = oMyPolarSystem.CurvesPolar.Add(ePolarShapeLine, "MyPolarCurve")
oMyPolarCurve.Shape.XChannel.Reference = "[5]/[1]"
oMyPolarCurve.Shape.YChannel.Reference = "[5]/[4]"

'This event will be raised if you click a 2D axis system while you press a keyboard key
Report.Events.ClickedWithKey.OnAxisSystemPolar = "MyClickEvent"
Call Report.Refresh()
```

If you press the <C> key and click the axis system, the user command specifies the mouse position. The example calculates the radius and the angle from the mouse position and displays them in a message. The user command receives a parameter. The first parameter corresponds to a [PolarAxisSystemClickedWithKeyContext](../objects/report_objects_ireppolaraxissystemclickedwithkeycontextint.htm) object and provides information about the polar axis system in DIAdem REPORT.

[Copy script](javascript:void(0);)

```text
Sub MyClickEvent(Context)
  Dim oSystem, oCurve, Lenght, Angle, oXAxis, oYAxis, oPoint, sgMessage, oChannel, oSubObject
  Context.DoProceed = False'True
  'Check the key
  If Chr(Context.KeyValue) = "C" or Chr(Context.KeyValue) = "c" Then
    Context.DoProceed = True
    Set oSystem = Context.AxisSystemPolar

    'Map cursor point to length and angle
    Lenght = oSystem.ConvertPageXYPositionToLength(Context.Position.X, Context.Position.Y)
    Angle  = oSystem.ConvertPageXYPositionToAngle(Context.Position.X, Context.Position.Y)

    'Build message text
    sgMessage =  "Lenght: " & VBTab & Lenght & VBCrLf & "Angle: " & VBTab & Angle
    Call MsgBoxDisp(sgMessage,,,,5,True)
  End If
End Sub
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_convertpageypositiontoyaxisvalue_irepd2axisyint.htm language=enus -->
## TOPIC 01573: Method: ConvertPageYPositionToYAxisValue for 2DAxisY

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_convertpageypositiontoyaxisvalue_irepd2axisyint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_convertpageypositiontoyaxisvalue_irepd2axisyint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ConvertPageYPositionToYAxisValue for 2DAxisY

Method: ConvertPageYPositionToYAxisValue for 2DAxisY

Converts a y-page coordinate into a y-axis coordinate in a 2D axis system in DIAdem REPORT.

```text
iConvertPageYPositionToYAxisValue = Object.ConvertPageYPositionToYAxisValue(Value)
```

| Object | 2DAxisYObject with this method |
| --- | --- |
| Value | DoubleContains the page coordinate to be converted. |
| iConvertPageYPositionToYAxisValue | DoubleReceives the converted y-coordinate. |

The following example creates a 2D axis system and assigns the user command MyToolTipEvent to the [OnAxisSystem2D for ToolTipEvents](../properties/report_property_onaxissystem2d_irepreportontooltipint.htm) property:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMy2DAxisSystem, oMyPos, oMy2DCurve
Call Report.NewLayout()
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Report_Data.tdm","TDM","")

Set oMy2DAxisSystem = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem, "My2DAxisSystem")
Set oMyPos = oMy2DAxisSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80

Set oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(e2DShapeLine, "My2DCurve")
oMy2DCurve.Shape.XChannel.Reference = "[6]/[1]"
oMy2DCurve.Shape.YChannel.Reference = "[6]/[4]"

'This event will be raised if the mouse is moved AND the shift key pressed 
Report.Events.ToolTip.OnAxisSystem2D = "MyToolTipEvent"
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Report.NewLayout() 
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Report_Data.tdm","TDM","") 
oMy2DAxisSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem, "My2DAxisSystem") 
oMyPos = oMy2DAxisSystem.Position.ByCoordinate 
oMyPos.X1 = 20 
oMyPos.X2 = 80 
oMyPos.Y1 = 20 
oMyPos.Y2 = 80 
oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(dd.e2DShapeLine, "My2DCurve") 
oMy2DCurve.Shape.XChannel.Reference = "[6]/[1]" 
oMy2DCurve.Shape.YChannel.Reference = "[6]/[4]" 
#This event will be raised if the mouse is moved AND the shift key pressed 
Report.Events.ToolTip.OnAxisSystem2D = "MyToolTipEvent" 
dd.Report.Refresh() 
```

If you press shift and move the mouse over the axis system, the user command determines the position of the mouse. The example calculates the coordinate of the nearest curve point from the mouse position and adds this to the default tooltip. If the mouse is not on a curve, the example displays the name and the type of the subobject over which you idle the mouse. The user command receives two parameters. The first parameter corresponds with the [ToolTip2DAxisContext](../objects/report_objects_ireptooltip2daxiscontextint.htm) object and provides the information about the 2D axis system in DIAdem REPORT when you press the shift key and move the mouse over the 2D axis system. The second parameter is a text and corresponds with the tooltip for display:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Sub MyToolTipEvent(Context,ToolTipText)
  Dim oSystem, oCurve, x, y, oXAxis, oYAxis, oPoint, oChannel, oSubObject
  If Context.SubObject.Type = e2DElementCurve then
    Set oSystem = Context.AxisSystem2D
    
    'Find curve, x and y-axis to convert the coordinate to value
    Set oXAxis = oSystem.XAxis
    Set oCurve = oSystem.Curves2D.Item(Context.SubObject.Name)
    set oYAxis = oSystem.YAxisList.Item(oCurve.YAxisReference)
    
    'Convert cursor position to axis coordinates
    x = oXAxis.ConvertPageXPositionToXAxisValue(Context.Position.X)
    y = oYAxis.ConvertPageYPositionToYAxisValue(Context.Position.Y)
    
    'Find nearest point on curve
    Set oPoint = oCurve.FindNearestValue(x,y)
    
    'Build tooltip text
    ToolTipText =  ToolTipText & VBCrLf & "Point (" & oPoint.Index & ")" & VBCrLf & "X = " & RTT(oPoint.X) & VBCrLf & "Y = " & Str(oPoint.Y)
    'Add assignment value which categorizes the value as a string value based on value limits
    Set oChannel = Data.GetChannel(oCurve.Shape.YChannel.Reference)
    ToolTipText =  ToolTipText & VBCrLf & "Assignment value: " & oChannel.Values(oPoint.Index)
  Else 
    Set oSubObject = Context.SubObject
    ToolTipText = "Sheet: " & Context.Sheet.Name & VBCrLf & "Sub object" & VBCrLf & "Name: " &  oSubObject.Name & VBCrLf & "Type: " & GetConstNameForREPORTSubObj(oSubObject, oSubObject.Type)
  End If
End Sub
```

[Copy script](javascript:void(0);)

```text
def MyToolTipEvent(Context,ToolTipText): 
    if Context.SubObject.Type == e2DElementCurve : 
        oSystem = Context.AxisSystem2D 
#Find curve, x and y-axis to convert the coordinate to value
        oXAxis = oSystem.XAxis 
        oCurve = oSystem.Curves2D.Item(Context.SubObject.Name) 
        oYAxis = oSystem.YAxisList.Item(oCurve.YAxisReference) 
#Convert cursor position to axis coordinates
        x = oXAxis.ConvertPageXPositionToXAxisValue(Context.Position.X) 
        y = oYAxis.ConvertPageYPositionToYAxisValue(Context.Position.Y) 
#Find nearest point on curve
        oPoint = oCurve.FindNearestValue(x,y) 
#Build tooltip text
        ToolTipText =  ToolTipText + "\r\n" + "Point (" + oPoint.Index + ")" + "\r\n" + "X = " + dd.RTT(oPoint.X) + "\r\n" + "Y = " + dd.Str(oPoint.Y) 
#Add assignment value which categorizes the value as a string value based on value limits
        oChannel = dd.Data.GetChannel(oCurve.Shape.YChannel.Reference) 
        ToolTipText =  ToolTipText + "\r\n" + "Assignment value: " + oChannel.Values(oPoint.Index) 
    else: 
        oSubObject = Context.SubObject 
        ToolTipText = "Sheet: " + Context.Sheet.Name + "\r\n" + "Sub object" + "\r\n" + "Name: " +  oSubObject.Name + "\r\n" + "Type: " + GetConstNameForREPORTSubObj(oSubObject, oSubObject.Type) 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_convertpolarcoordinatetopagexposition_ireppolarint.htm language=enus -->
## TOPIC 01574: Method: ConvertPolarCoordinateToPageXPosition for PolarSystem

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_convertpolarcoordinatetopagexposition_ireppolarint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_convertpolarcoordinatetopagexposition_ireppolarint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ConvertPolarCoordinateToPageXPosition for PolarSystem

Method: ConvertPolarCoordinateToPageXPosition for PolarSystem

Converts in a polar axis system in DIAdem REPORT an angle and a radius into an x-page coordinate.

```text
iConvertPolarCoordinateToPageXPosition = Object.ConvertPolarCoordinateToPageXPosition(Angle, Length)
```

| Object | PolarSystemObject with this method |
| --- | --- |
| Angle | DoubleContains the angle. |
| Length | DoubleContains the radius. |
| iConvertPolarCoordinateToPageXPosition | DoubleReceives the converted x-page coordinate. |

The following example generates a polar axis system with a curve and adds an arrow, which points to the curve maximum, to the current worksheet.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyPolarSystem, oMyPos, oMyPolarCurve, oMyArrow, oMyChnGroupChannels, oMyArrowPosition, MaxValLength, MaxValAngle
Call Report.NewLayout()
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Report_Data.tdm","TDM","")

Set oMyPolarSystem = Report.ActiveSheet.Objects.Add(eReportObjectPolarSystem, "MyPolarSystem")
Set oMyPos = oMyPolarSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80

Set oMyPolarCurve = oMyPolarSystem.CurvesPolar.Add(ePolarShapeLine, "MyPolarCurve")
oMyPolarCurve.Shape.XChannel.Reference = "[5]/[1]"
oMyPolarCurve.Shape.YChannel.Reference = "[5]/[4]"

Call Report.Refresh
Set oMyArrow = Report.ActiveSheet.Objects.Add(eReportObjectArrow, "MyArrow")
Set oMyArrowPosition = oMyArrow.Position.ByCoordinate
Set oMyChnGroupChannels = Data.Root.ChannelGroups(5).Channels
MaxValLength = oMyChnGroupChannels(4).Properties("maximum").Value
MaxValAngle  = oMyChnGroupChannels(1).Values(PNo("[5]/[4]", MaxValLength))
oMyArrowPosition.X1 = oMyPolarSystem.ConvertPolarCoordinateToPageXPosition (MaxValAngle, MaxValLength) + 10
oMyArrowPosition.Y1 = oMyPolarSystem.ConvertPolarCoordinateToPageYPosition (MaxValAngle, MaxValLength) + 10
oMyArrowPosition.X2 = oMyPolarSystem.ConvertPolarCoordinateToPageXPosition (MaxValAngle, MaxValLength)
oMyArrowPosition.Y2 = oMyPolarSystem.ConvertPolarCoordinateToPageYPosition (MaxValAngle, MaxValLength)
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Report.NewLayout() 
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Report_Data.tdm","TDM","") 
oMyPolarSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObjectPolarSystem, "MyPolarSystem") 
oMyPos = oMyPolarSystem.Position.ByCoordinate 
oMyPos.X1 = 20 
oMyPos.X2 = 80 
oMyPos.Y1 = 20 
oMyPos.Y2 = 80 
oMyPolarCurve = oMyPolarSystem.CurvesPolar.Add(dd.ePolarShapeLine, "MyPolarCurve") 
oMyPolarCurve.Shape.XChannel.Reference = "[5]/[1]" 
oMyPolarCurve.Shape.YChannel.Reference = "[5]/[4]" 
dd.Report.Refresh() 
oMyArrow = dd.Report.ActiveSheet.Objects.Add(dd.eReportObjectArrow, "MyArrow") 
oMyArrowPosition = oMyArrow.Position.ByCoordinate 
oMyChnGroupChannels = dd.Data.Root.ChannelGroups(5).Channels 
MaxValLength = oMyChnGroupChannels(4).Properties("maximum").Value 
MaxValAngle  = oMyChnGroupChannels(1).Values(dd.PNo("[5]/[4]", MaxValLength)) 
oMyArrowPosition.X1 = oMyPolarSystem.ConvertPolarCoordinateToPageXPosition (MaxValAngle, MaxValLength) + 10 
oMyArrowPosition.Y1 = oMyPolarSystem.ConvertPolarCoordinateToPageYPosition (MaxValAngle, MaxValLength) + 10 
oMyArrowPosition.X2 = oMyPolarSystem.ConvertPolarCoordinateToPageXPosition (MaxValAngle, MaxValLength) 
oMyArrowPosition.Y2 = oMyPolarSystem.ConvertPolarCoordinateToPageYPosition (MaxValAngle, MaxValLength) 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_convertpolarcoordinatetopageyposition_ireppolarint.htm language=enus -->
## TOPIC 01575: Method: ConvertPolarCoordinateToPageYPosition for PolarSystem

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_convertpolarcoordinatetopageyposition_ireppolarint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_convertpolarcoordinatetopageyposition_ireppolarint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ConvertPolarCoordinateToPageYPosition for PolarSystem

Method: ConvertPolarCoordinateToPageYPosition for PolarSystem

Converts in a polar axis system in DIAdem REPORT an angle and a radius into a y-page coordinate.

```text
iConvertPolarCoordinateToPageYPosition = Object.ConvertPolarCoordinateToPageYPosition(Angle, Length)
```

| Object | PolarSystemObject with this method |
| --- | --- |
| Angle | DoubleContains the angle. |
| Length | DoubleContains the radius. |
| iConvertPolarCoordinateToPageYPosition | DoubleReceives the converted y-page coordinate. |

The following example generates a polar axis system with a curve and adds an arrow, which points to the curve maximum, to the current worksheet.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyPolarSystem, oMyPos, oMyPolarCurve, oMyArrow, oMyChnGroupChannels, oMyArrowPosition, MaxValLength, MaxValAngle
Call Report.NewLayout()
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Report_Data.tdm","TDM","")

Set oMyPolarSystem = Report.ActiveSheet.Objects.Add(eReportObjectPolarSystem, "MyPolarSystem")
Set oMyPos = oMyPolarSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80

Set oMyPolarCurve = oMyPolarSystem.CurvesPolar.Add(ePolarShapeLine, "MyPolarCurve")
oMyPolarCurve.Shape.XChannel.Reference = "[5]/[1]"
oMyPolarCurve.Shape.YChannel.Reference = "[5]/[4]"

Call Report.Refresh
Set oMyArrow = Report.ActiveSheet.Objects.Add(eReportObjectArrow, "MyArrow")
Set oMyArrowPosition = oMyArrow.Position.ByCoordinate
Set oMyChnGroupChannels = Data.Root.ChannelGroups(5).Channels
MaxValLength = oMyChnGroupChannels(4).Properties("maximum").Value
MaxValAngle  = oMyChnGroupChannels(1).Values(PNo("[5]/[4]", MaxValLength))
oMyArrowPosition.X1 = oMyPolarSystem.ConvertPolarCoordinateToPageXPosition (MaxValAngle, MaxValLength) + 10
oMyArrowPosition.Y1 = oMyPolarSystem.ConvertPolarCoordinateToPageYPosition (MaxValAngle, MaxValLength) + 10
oMyArrowPosition.X2 = oMyPolarSystem.ConvertPolarCoordinateToPageXPosition (MaxValAngle, MaxValLength)
oMyArrowPosition.Y2 = oMyPolarSystem.ConvertPolarCoordinateToPageYPosition (MaxValAngle, MaxValLength)
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Report.NewLayout() 
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Report_Data.tdm","TDM","") 
oMyPolarSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObjectPolarSystem, "MyPolarSystem") 
oMyPos = oMyPolarSystem.Position.ByCoordinate 
oMyPos.X1 = 20 
oMyPos.X2 = 80 
oMyPos.Y1 = 20 
oMyPos.Y2 = 80 
oMyPolarCurve = oMyPolarSystem.CurvesPolar.Add(dd.ePolarShapeLine, "MyPolarCurve") 
oMyPolarCurve.Shape.XChannel.Reference = "[5]/[1]" 
oMyPolarCurve.Shape.YChannel.Reference = "[5]/[4]" 
dd.Report.Refresh() 
oMyArrow = dd.Report.ActiveSheet.Objects.Add(dd.eReportObjectArrow, "MyArrow") 
oMyArrowPosition = oMyArrow.Position.ByCoordinate 
oMyChnGroupChannels = dd.Data.Root.ChannelGroups(5).Channels 
MaxValLength = oMyChnGroupChannels(4).Properties("maximum").Value 
MaxValAngle  = oMyChnGroupChannels(1).Values(dd.PNo("[5]/[4]", MaxValLength)) 
oMyArrowPosition.X1 = oMyPolarSystem.ConvertPolarCoordinateToPageXPosition (MaxValAngle, MaxValLength) + 10 
oMyArrowPosition.Y1 = oMyPolarSystem.ConvertPolarCoordinateToPageYPosition (MaxValAngle, MaxValLength) + 10 
oMyArrowPosition.X2 = oMyPolarSystem.ConvertPolarCoordinateToPageXPosition (MaxValAngle, MaxValLength) 
oMyArrowPosition.Y2 = oMyPolarSystem.ConvertPolarCoordinateToPageYPosition (MaxValAngle, MaxValLength) 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_converttoscaledoutput_irepdisplaydimensionsint.htm language=enus -->
## TOPIC 01576: Method: ConvertToScaledOutput for DisplayDimensions

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_converttoscaledoutput_irepdisplaydimensionsint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_converttoscaledoutput_irepdisplaydimensionsint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ConvertToScaledOutput for DisplayDimensions

Method: ConvertToScaledOutput for DisplayDimensions

Enables scaled display in DIAdem REPORT and converts the position and the distance of the objects according to the measurement unit.

```text
Object.ConvertToScaledOutput()
```

| Object | DisplayDimensionsObject with this method |
| --- | --- |

The following example enables the scaled display:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Report.Settings.Page.Dimensions.ConvertToScaledOutput()
```

[Copy script](javascript:void(0);)

```text
dd.Report.Settings.Page.Dimensions.ConvertToScaledOutput() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_convertxaxisvaluetopagexposition_irepd2axisxint.htm language=enus -->
## TOPIC 01577: Method: ConvertXAxisValueToPageXPosition for 2DAxisX

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_convertxaxisvaluetopagexposition_irepd2axisxint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_convertxaxisvaluetopagexposition_irepd2axisxint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ConvertXAxisValueToPageXPosition for 2DAxisX

Method: ConvertXAxisValueToPageXPosition for 2DAxisX

Converts the x-coordinates of a 2D axis system in DIAdem REPORT into page coordinates.

```text
iConvertXAxisValueToPageXPosition = Object.ConvertXAxisValueToPageXPosition(Value)
```

| Object | 2DAxisXObject with this method |
| --- | --- |
| Value | DoubleSpecifies which x-coordinate of the axis system to convert. |
| iConvertXAxisValueToPageXPosition | DoubleContains the converted page coordinate. |

The following example generates a 2D axis system with a curve and adds an arrow, which points to the curve maximum, to the current worksheet.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMy2DAxisSystem, oMyPos, oMy2DCurve, oMyArrow, oMyArrowPosition, oMyChnGroupChannels, MaxValX, MaxValY
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Example.tdm","TDM","")
Call Report.NewLayout()
Set oMy2DAxisSystem = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem, "My2DAxisSystem")
Set oMyPos = oMy2DAxisSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80
Set oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(e2DShapeLine, "MyNew2DCurve")
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]"
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]"
Call Report.Refresh()
Set oMyArrow = Report.ActiveSheet.Objects.Add(eReportObjectArrow, "MyArrow")
Set oMyArrowPosition = oMyArrow.Position.ByCoordinate
Set oMyChnGroupChannels = Data.Root.ChannelGroups(1).Channels
MaxValY = oMyChnGroupChannels(2).Properties("maximum").Value
MaxValX = oMyChnGroupChannels(1).Values(PNo("[1]/[2]", MaxValY))
oMyArrowPosition.X1 = oMy2DaxisSystem.XAxis.ConvertXAxisValueToPageXPosition(MaxValX) + 10
oMyArrowPosition.Y1 = oMy2DaxisSystem.YAxis.ConvertYAxisValueToPageYPosition(MaxValY) + 10
oMyArrowPosition.X2 = oMy2DaxisSystem.XAxis.ConvertXAxisValueToPageXPosition(MaxValX)
oMyArrowPosition.Y2 = oMy2DaxisSystem.YAxis.ConvertYAxisValueToPageYPosition(MaxValY)
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Example.tdm","TDM","") 
dd.Report.NewLayout() 
oMy2DAxisSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem, "My2DAxisSystem") 
oMyPos = oMy2DAxisSystem.Position.ByCoordinate 
oMyPos.X1 = 20 
oMyPos.X2 = 80 
oMyPos.Y1 = 20 
oMyPos.Y2 = 80 
oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(dd.e2DShapeLine, "MyNew2DCurve") 
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]" 
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]" 
dd.Report.Refresh() 
oMyArrow = dd.Report.ActiveSheet.Objects.Add(dd.eReportObjectArrow, "MyArrow") 
oMyArrowPosition = oMyArrow.Position.ByCoordinate 
oMyChnGroupChannels = dd.Data.Root.ChannelGroups(1).Channels 
MaxValY = oMyChnGroupChannels(2).Properties("maximum").Value 
MaxValX = oMyChnGroupChannels(1).Values(dd.PNo("[1]/[2]", MaxValY)) 
oMyArrowPosition.X1 = oMy2DaxisSystem.XAxis.ConvertXAxisValueToPageXPosition(MaxValX) + 10 
oMyArrowPosition.Y1 = oMy2DaxisSystem.YAxis.ConvertYAxisValueToPageYPosition(MaxValY) + 10 
oMyArrowPosition.X2 = oMy2DaxisSystem.XAxis.ConvertXAxisValueToPageXPosition(MaxValX) 
oMyArrowPosition.Y2 = oMy2DaxisSystem.YAxis.ConvertYAxisValueToPageYPosition(MaxValY) 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_convertyaxisvaluetopageyposition_irepd2axisyint.htm language=enus -->
## TOPIC 01578: Method: ConvertYAxisValueToPageYPosition for 2DAxisY

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_convertyaxisvaluetopageyposition_irepd2axisyint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_convertyaxisvaluetopageyposition_irepd2axisyint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ConvertYAxisValueToPageYPosition for 2DAxisY

Method: ConvertYAxisValueToPageYPosition for 2DAxisY

Converts the y-coordinates of a 2D axis system in DIAdem REPORT into page coordinates.

```text
iConvertYAxisValueToPageYPosition = Object.ConvertYAxisValueToPageYPosition(Value)
```

| Object | 2DAxisYObject with this method |
| --- | --- |
| Value | DoubleSpecifies which x-coordinate of the axis system to convert. |
| iConvertYAxisValueToPageYPosition | DoubleContains the converted page coordinate. |

The following example generates a 2D axis system with a curve and adds an arrow, which points to the curve maximum, to the current worksheet.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMy2DAxisSystem, oMyPos, oMy2DCurve, oMyArrow, oMyArrowPosition, oMyChnGroupChannels, MaxValX, MaxValY
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Example.tdm","TDM","")
Call Report.NewLayout()
Set oMy2DAxisSystem = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem, "My2DAxisSystem")
Set oMyPos = oMy2DAxisSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80
Set oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(e2DShapeLine, "MyNew2DCurve")
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]"
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]"
Call Report.Refresh()
Set oMyArrow = Report.ActiveSheet.Objects.Add(eReportObjectArrow, "MyArrow")
Set oMyArrowPosition = oMyArrow.Position.ByCoordinate
Set oMyChnGroupChannels = Data.Root.ChannelGroups(1).Channels
MaxValY = oMyChnGroupChannels(2).Properties("maximum").Value
MaxValX = oMyChnGroupChannels(1).Values(PNo("[1]/[2]", MaxValY))
oMyArrowPosition.X1 = oMy2DaxisSystem.XAxis.ConvertXAxisValueToPageXPosition(MaxValX) + 10
oMyArrowPosition.Y1 = oMy2DaxisSystem.YAxis.ConvertYAxisValueToPageYPosition(MaxValY) + 10
oMyArrowPosition.X2 = oMy2DaxisSystem.XAxis.ConvertXAxisValueToPageXPosition(MaxValX)
oMyArrowPosition.Y2 = oMy2DaxisSystem.YAxis.ConvertYAxisValueToPageYPosition(MaxValY)
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Example.tdm","TDM","") 
dd.Report.NewLayout() 
oMy2DAxisSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem, "My2DAxisSystem") 
oMyPos = oMy2DAxisSystem.Position.ByCoordinate 
oMyPos.X1 = 20 
oMyPos.X2 = 80 
oMyPos.Y1 = 20 
oMyPos.Y2 = 80 
oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(dd.e2DShapeLine, "MyNew2DCurve") 
oMy2DCurve.Shape.XChannel.Reference = "[1]/[1]" 
oMy2DCurve.Shape.YChannel.Reference = "[1]/[2]" 
dd.Report.Refresh() 
oMyArrow = dd.Report.ActiveSheet.Objects.Add(dd.eReportObjectArrow, "MyArrow") 
oMyArrowPosition = oMyArrow.Position.ByCoordinate 
oMyChnGroupChannels = dd.Data.Root.ChannelGroups(1).Channels 
MaxValY = oMyChnGroupChannels(2).Properties("maximum").Value 
MaxValX = oMyChnGroupChannels(1).Values(dd.PNo("[1]/[2]", MaxValY)) 
oMyArrowPosition.X1 = oMy2DaxisSystem.XAxis.ConvertXAxisValueToPageXPosition(MaxValX) + 10 
oMyArrowPosition.Y1 = oMy2DaxisSystem.YAxis.ConvertYAxisValueToPageYPosition(MaxValY) + 10 
oMyArrowPosition.X2 = oMy2DaxisSystem.XAxis.ConvertXAxisValueToPageXPosition(MaxValX) 
oMyArrowPosition.Y2 = oMy2DaxisSystem.YAxis.ConvertYAxisValueToPageYPosition(MaxValY) 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_copy_irepchannelreferencelistint.htm language=enus -->
## TOPIC 01579: Method: Copy for Channels

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_copy_irepchannelreferencelistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_copy_irepchannelreferencelistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Copy for Channels

Method: Copy for Channels

Copies in DIAdem REPORT the existing y-channel of a 2D axis system in the display mode **Stacked bars** or **Grouped bars** and adds this channel to the axis system.

```text
Set oChannelReferenceListItem = Object.Copy(Index, IndexTo)
```

| Object | ChannelsObject with this method |
| --- | --- |
| Index | LongIntegerSpecifies the index of the channel to be copied. |
| IndexTo | LongIntegerSpecifies the index of the y-channel at whose position DIAdem copies the y-channel. |
| oChannelReferenceListItem | ChannelReferenceListItemReturned object |

The following example creates a 2D axis system with grouped bars and copies the first y-channel to the position of the second y-channel:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMy2DAxisSystem, oMyPos, oMy2DCurve
Call Report.NewLayout()
Call Data.Root.Clear()
Call DataFileLoad("Example.tdm","TDM","")

Set oMy2DAxisSystem = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem, "My2DAxisSystem")
Set oMyPos = oMy2DAxisSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20
oMyPos.Y2 = 80

Set oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(e2DShapeGroupedBars, "MyNew2DCurve1")
oMy2DCurve.Shape.XChannel.Reference = ""
oMy2DCurve.Shape.YChannels.Add("[4]/[1]")
oMy2DCurve.Shape.YChannels.Add("[4]/[2]") 
Call oMy2DCurve.Shape.YChannels.Copy(1,2) 

Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Report.NewLayout() 
dd.Data.Root.Clear() 
dd.DataFileLoad("Example.tdm","TDM","") 
oMy2DAxisSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem, "My2DAxisSystem") 
oMyPos = oMy2DAxisSystem.Position.ByCoordinate 
oMyPos.X1 = 20 
oMyPos.X2 = 80 
oMyPos.Y1 = 20 
oMyPos.Y2 = 80 
oMy2DCurve = oMy2DaxisSystem.Curves2D.Add(dd.e2DShapeGroupedBars, "MyNew2DCurve1") 
oMy2DCurve.Shape.XChannel.Reference = "" 
oMy2DCurve.Shape.YChannels.Add("[4]/[1]") 
oMy2DCurve.Shape.YChannels.Add("[4]/[2]") 
oMy2DCurve.Shape.YChannels.Copy(1,2) 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_copy_irepctrllistint.htm language=enus -->
## TOPIC 01580: Method: Copy for ReportObjects

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_copy_irepctrllistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_copy_irepctrllistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Copy for ReportObjects

Method: Copy for ReportObjects

Copies an object in DIAdem REPORT.

```text
Set oReportObject = Object.Copy(NameOrIndex, NewName, InsertOnSheet)
```

| Object | ReportObjectsObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the object. |
| NewName | StringSpecifies the name of the new object. |
| InsertOnSheet | VariantSpecifies the name or index of the target worksheet. |
| oReportObject | ReportObjectReturned object |

The following example copies a frame:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyObjects, oMyPosition, oMyFrame, oMyCopyFrame
Call Report.NewLayout()
Set oMyObjects = Report.ActiveSheet.Objects
Set oMyFrame = oMyObjects.Add(eReportObjectFrame,"MyFrame")
Set oMyCopyFrame = oMyObjects.Copy("MyFrame","MyFrame2",1)
Set oMyPosition = oMyCopyFrame.Position.ByBorder
oMyPosition.Left = 30
oMyPosition.Bottom = 30
oMyPosition.Height = 40
oMyPosition.Width = 40
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Report.NewLayout() 
oMyObjects = dd.Report.ActiveSheet.Objects 
oMyFrame = oMyObjects.Add(dd.eReportObjectFrame,"MyFrame") 
oMyCopyFrame = oMyObjects.Copy("MyFrame","MyFrame2",1) 
oMyPosition = oMyCopyFrame.Position.ByBorder 
oMyPosition.Left = 30 
oMyPosition.Bottom = 30 
oMyPosition.Height = 40 
oMyPosition.Width = 40 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_copy_irepd2curvelistint.htm language=enus -->
## TOPIC 01581: Method: Copy for 2DCurves

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_copy_irepd2curvelistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_copy_irepd2curvelistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Copy for 2DCurves

Method: Copy for 2DCurves

Copies a curve in a 2D axis system in DIAdem REPORT and adds this curve to the axis system.

```text
Set o2DCurve = Object.Copy(NameOrIndex, NewName, InsertBeforeNameOrIndex)
```

| Object | 2DCurvesObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the curve that is to be copied. |
| NewName | StringSpecifies the name of the copied curve. |
| InsertBeforeNameOrIndex | VariantSpecifies the name or the index of the curve before which DIAdem inserts the curve. If you specify the index 0 or "", DIAdem copies the curve and inserts it behind the last curve. |
| o2DCurve | 2DCurveReturned object |

The following example generates a 2D axis system with a curve, copies this curve, and inserts the curve before the first curve:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMy2DAxisSys, oMyPosition, oMyCurve1, oMyCurve2, oMy2DCurves
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Report_Data.tdm","TDM","")
Call Report.NewLayout()
Set oMy2DAxisSys = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem,"My2DAxisSystem")
Set oMyPosition = oMy2DAxisSys.Position.ByBorder
oMyPosition.Top = 30
oMyPosition.Bottom = 20
oMyPosition.Left = 20
oMyPosition.Right = 30
Set oMyCurve1 = oMy2DAxisSys.Curves2D.Add(e2DShapeLine, "MyNewCurve1")
oMyCurve1.Shape.XChannel.Reference= "[1]/[1]"
oMyCurve1.Shape.YChannel.Reference = "[1]/[2]"
Set oMy2DCurves = oMy2DAxisSys.Curves2D
Set oMyCurve2 = oMy2DCurves.Copy("MyNewCurve1","NewCurve2",1)
Call MsgBox("Number of curves: " & oMy2DCurves.Count)
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Report_Data.tdm","TDM","") 
dd.Report.NewLayout() 
oMy2DAxisSys = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem,"My2DAxisSystem") 
oMyPosition = oMy2DAxisSys.Position.ByBorder 
oMyPosition.Top = 30 
oMyPosition.Bottom = 20 
oMyPosition.Left = 20 
oMyPosition.Right = 30 
oMyCurve1 = oMy2DAxisSys.Curves2D.Add(dd.e2DShapeLine, "MyNewCurve1") 
oMyCurve1.Shape.XChannel.Reference= "[1]/[1]" 
oMyCurve1.Shape.YChannel.Reference = "[1]/[2]" 
oMy2DCurves = oMy2DAxisSys.Curves2D 
oMyCurve2 = oMy2DCurves.Copy("MyNewCurve1","NewCurve2",1) 
print("Number of curves: " + oMy2DCurves.Count) 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_copy_irepd3curvelistint.htm language=enus -->
## TOPIC 01582: Method: Copy for 3DCurves

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_copy_irepd3curvelistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_copy_irepd3curvelistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Copy for 3DCurves

Method: Copy for 3DCurves

Copies a curve in a 3D axis system in DIAdem REPORT and adds this curve to the axis system.

```text
Set o3DCurve = Object.Copy(NameOrIndex, NewName, InsertBeforeNameOrIndex)
```

| Object | 3DCurvesObject with this method |
| --- | --- |
| NameOrIndex | VariantSpecifies the name or the index of the curve that is to be copied. |
| NewName | StringSpecifies the new name of the curve. |
| InsertBeforeNameOrIndex | VariantSpecifies the name or the index of the curve before which DIAdem inserts the curve. If you specify the index 0 or "", DIAdem copies the curve and inserts it behind the last curve. |
| o3DCurve | 3DCurveReturned object |

The following example creates a 3D axis system with two curves, copies the first curve and inserts this curve into the axis system before the first curve:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMy3DAxisSys, oMyPosition, oMyCurve1, oMyCurve2, oMy3DCurves
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Report_Data.tdm","TDM","")
Call Report.NewLayout()
Set oMy3DAxisSys = Report.ActiveSheet.Objects.Add(eReportObject3DAxisSystem,"My3DAxisSystem")
Set oMyPosition = oMy3DAxisSys.Position.ByBorder
oMyPosition.Top = 30
oMyPosition.Bottom = 20
oMyPosition.Left = 20
oMyPosition.Right = 30
Set oMyCurve1 = oMy3DAxisSys.Curves3D.Add(e3DShapeLine, "MyNewCurve1")
oMyCurve1.Shape.XChannel.Reference= "[3]/[1]"
oMyCurve1.Shape.YChannel.Reference = "[3]/[2]"
oMyCurve1.Shape.ZChannel.Reference = "[3]/[3]"
Set oMy3DCurves = oMy3DAxisSys.Curves3D
Set oMyCurve2 = oMy3DCurves.Copy("MyNewCurve1","NewCurve2",1)
Call MsgBox("Number of curves: " & oMy3DCurves.Count)
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Report_Data.tdm","TDM","") 
dd.Report.NewLayout() 
oMy3DAxisSys = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject3DAxisSystem,"My3DAxisSystem") 
oMyPosition = oMy3DAxisSys.Position.ByBorder 
oMyPosition.Top = 30 
oMyPosition.Bottom = 20 
oMyPosition.Left = 20 
oMyPosition.Right = 30 
oMyCurve1 = oMy3DAxisSys.Curves3D.Add(dd.e3DShapeLine, "MyNewCurve1") 
oMyCurve1.Shape.XChannel.Reference= "[3]/[1]" 
oMyCurve1.Shape.YChannel.Reference = "[3]/[2]" 
oMyCurve1.Shape.ZChannel.Reference = "[3]/[3]" 
oMy3DCurves = oMy3DAxisSys.Curves3D 
oMyCurve2 = oMy3DCurves.Copy("MyNewCurve1","NewCurve2",1) 
print("Number of curves: " + oMy3DCurves.Count) 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exists_ireppolarcurvelistint.htm language=enus -->
## TOPIC 01583: Method: Exists for PolarCurves

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exists_ireppolarcurvelistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exists_ireppolarcurvelistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Exists for PolarCurves

Method: Exists for PolarCurves

Checks whether a polar curve with a specific name already exists in a polar axis system in DIAdem REPORT.

```text
bExists = Object.Exists(Name)
```

| Object | PolarCurvesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the polar curve. |
| bExists | BooleanSpecifies whether the polar curve with the specified name already exists (TRUE) or not (FALSE). |

The following example displays whether a polar curve called 2DPolar1_Curve1 already exists:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Report.ActiveSheet.Objects(1).Curves.Exists("2DPolar1_Curve1"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Report.ActiveSheet.Objects(1).Curves.Exists("2DPolar1_Curve1")) 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exists_irepselectedobjectslistint.htm language=enus -->
## TOPIC 01584: Method: Exists for SelectedObjects

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exists_irepselectedobjectslistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exists_irepselectedobjectslistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Exists for SelectedObjects

Method: Exists for SelectedObjects

Checks whether an object with a specific name already exists in the objects selected in the current worksheet of DIAdem REPORT.

```text
bExists = Object.Exists(Name)
```

| Object | SelectedObjectsObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the selected object. |
| bExists | BooleanSpecifies whether the object with the specified name exists (TRUE) or not (FALSE) within the selected objects. |

The following example displays whether an object with the name 2DTable1 exists within the selected objects:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Report.SelectedObjects.Exists("2DTable1"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Report.SelectedObjects.Exists("2DTable1")) 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exists_irepsettingsexportpropertiesint.htm language=enus -->
## TOPIC 01585: Method: Exists for Properties

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exists_irepsettingsexportpropertiesint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exists_irepsettingsexportpropertiesint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Exists for Properties

Method: Exists for Properties

Checks in DIAdem REPORT whether a custom property for the export of the layout already exists. If you export the layout as an Office file in XML format, or as a PDF-, JPEG-, PNG- or TIFF-file, DIAdem saves these properties as meta properties in the document. Use [Document <Data>](../../filetagging/objects/diacmpnt_objects_idiademdocument.htm) to access the meta properties in exported documents.

```text
bExists = Object.Exists(Name)
```

| Object | PropertiesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the custom property. |
| bExists | BooleanSpecifies whether the custom property with the specified name already exists (TRUE) or not (FALSE). |

The following example sets the custom properties of the layout and exports all worksheets into the PDF file MyFile:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyExport, oMyProperties, oMyProperty
Set oMyExport = Report.Settings.Export
Set oMyProperties = oMyExport.Properties
If Not(oMyProperties.Exists("Company")) Then
  Set oMyProperty = oMyProperties.Add("Company")
  oMyProperty.DataType = ePropertyDataTypeString
  oMyProperty.Value = "NI"
End If
Call Report.Sheets.ExportToPDF(ScriptWritePath & "MyFile.pdf",False)
```

[Copy script](javascript:void(0);)

```text
oMyExport = dd.Report.Settings.Export 
oMyProperties = oMyExport.Properties 
if not(oMyProperties.Exists("Company")) : 
    oMyProperty = oMyProperties.Add("Company") 
    oMyProperty.DataType = dd.ePropertyDataTypeString 
    oMyProperty.Value = "NI" 
dd.Report.Sheets.ExportToPDF(dd.ScriptWritePath + "MyFile.pdf",False) 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exists_irepsheetlistint.htm language=enus -->
## TOPIC 01586: Method: Exists for Sheets

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exists_irepsheetlistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exists_irepsheetlistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Exists for Sheets

Method: Exists for Sheets

Checks whether a worksheet with a specific name already exists in DIAdem REPORT.

```text
bExists = Object.Exists(Name)
```

| Object | SheetsObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the worksheet. |
| bExists | BooleanSpecifies whether the worksheet with the specified name already exists (TRUE) or not (FALSE). |

The following example adds the new worksheet MySheet if this worksheet does not already exist:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
If Not Report.Sheets.Exists("MySheet") Then
  Call Report.Sheets.Add("MySheet")
End If
```

[Copy script](javascript:void(0);)

```text
if not dd.Report.Sheets.Exists("MySheet") : 
    dd.Report.Sheets.Add("MySheet") 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exists_irepspidercurvelistint.htm language=enus -->
## TOPIC 01587: Method: Exists for SpiderCurves

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exists_irepspidercurvelistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exists_irepspidercurvelistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Exists for SpiderCurves

Method: Exists for SpiderCurves

Checks whether a curve with a specific name already exists in a spider axis system in DIAdem REPORT.

```text
bExists = Object.Exists(Name)
```

| Object | SpiderCurvesObject with this method |
| --- | --- |
| Name | StringSpecifies the name of the curve. |
| bExists | BooleanSpecifies whether the curve with the specified name already exists (TRUE) or not (FALSE). |

The following example displays whether a curve named Spider_Curve1 already exists.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call MsgBoxDisp(Report.ActiveSheet.Objects(1).CurvesSpider.Exists("Spider_Curve1"))
```

[Copy script](javascript:void(0);)

```text
dd.MsgBoxDisp(dd.Report.ActiveSheet.Objects(1).CurvesSpider.Exists("Spider_Curve1")) 
```

#### See also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exists_irepsynchronizationgroupsint.htm language=enus -->
## TOPIC 01588: Method: Exists for SynchronizationGroups

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exists_irepsynchronizationgroupsint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exists_irepsynchronizationgroupsint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Exists for SynchronizationGroups

Method: Exists for SynchronizationGroups

Checks whether a synchronization group exists in the list of synchronization groups in DIAdem REPORT.

```text
bExists = Object.Exists(ID)
```

| Object | SynchronizationGroupsObject with this method |
| --- | --- |
| ID | StringSpecifies the name of the synchronization group. |
| bExists | BooleanSpecifies whether the synchronization group already exists (TRUE) or not (FALSE). |

The following example creates a synchronization group for x-axes if the synchronization group does not yet exist, and assigns this synchronization group to the x-axes of all 2D axis systems in the current worksheet. If you then modify the x-axis scaling, DIAdem automatically modifies the scaling of all x-axes of the same synchronization group.

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyXSync, oMyReportObjs, oMyReportObj
Set oMyXSync = Report.Settings.Synchronization.AxisSystem2D.XAxis
If Not oMyXSync.Exists("XAxis Group1") Then
  Call oMyXSync.Add("XAxis Group1")
End If
Set oMyReportObjs = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjs
  If oMyReportObj.ObjectType = eReportObject2DAxisSystem Then
    oMyReportObj.XAxis.Scaling.SynchronizationID = "XAxis Group1"
  End If
Next
```

[Copy script](javascript:void(0);)

```text
oMyXSync = dd.Report.Settings.Synchronization.AxisSystem2D.XAxis 
if not oMyXSync.Exists("XAxis Group1") : 
    oMyXSync.Add("XAxis Group1") 
oMyReportObjs = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjs: 
    if oMyReportObj.ObjectType == dd.eReportObject2DAxisSystem : 
        oMyReportObj.XAxis.Scaling.SynchronizationID = "XAxis Group1" 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_expand_irepexpansionsettingsint.htm language=enus -->
## TOPIC 01589: Method: Expand for CurveExpansionSettings

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_expand_irepexpansionsettingsint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_expand_irepexpansionsettingsint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Expand for CurveExpansionSettings

Method: Expand for CurveExpansionSettings

Expands the curves in a REPORT layout. To create a layout with curve expansion, you must assign the value [True](../properties/report_property_enable_irepexpansionsettingsint.htm) to the property Enable for CurveExpansionSettings.

```text
Object.Expand()
```

| Object | CurveExpansionSettingsObject with this method |
| --- | --- |

The following example enables the [name-oriented mode](../../genpresent/genpresent/genreport_nameoriented_mode.htm) with curve expansion and generates a 2D axis system with a curve definition. Then the example expands curves and adds curve markers to the expanded curves. DIAdem displays two curves because the specified channel name occurs in two channel groups:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportSettings, oMy2DAxisSystem, oMyCurve, oMyPos, oMyShape, oMyExpandedCurve
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "TR_M17_QT_32-1.tdm","TDM","")
Call Report.NewLayout()
Set oMyReportSettings = Report.Settings
oMyReportSettings.CurveExpansion.Enable = True
oMyReportSettings.CurveExpansion.AttributeList.Enable = True

Set oMy2DAxisSystem = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem, "My2DAxisSystem")
Set oMyPos = oMy2DAxisSystem.Position.ByCoordinate
oMyPos.X1 = 20
oMyPos.X2 = 80
oMyPos.Y1 = 20 
oMyPos.Y2 = 80
Set oMyCurve = oMy2DAxisSystem.Curves2D.Add(e2DShapeLine, "MyCurve")
Set oMyShape = oMyCurve.Shape
oMyShape.Settings.UseCurveExpansion = True
oMyShape.XChannel.Reference = "" 
oMyShape.YChannel.Reference = "Temp_A"

Call Report.Settings.CurveExpansion.Expand()
Call MsgBox ("Number of expanded curves: " & oMy2DAxisSystem.Curves2D.Count)
For Each oMyExpandedCurve in oMy2DAxisSystem.Curves2D
  oMyExpandedCurve.Shape.Extensions.Marker.Type = eMarkerCircle
Next
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "TR_M17_QT_32-1.tdm","TDM","") 
dd.Report.NewLayout() 
oMyReportSettings = dd.Report.Settings 
oMyReportSettings.CurveExpansion.Enable = True 
oMyReportSettings.CurveExpansion.AttributeList.Enable = True 
oMy2DAxisSystem = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem, "My2DAxisSystem") 
oMyPos = oMy2DAxisSystem.Position.ByCoordinate 
oMyPos.X1 = 20 
oMyPos.X2 = 80 
oMyPos.Y1 = 20 
oMyPos.Y2 = 80 
oMyCurve = oMy2DAxisSystem.Curves2D.Add(dd.e2DShapeLine, "MyCurve") 
oMyShape = oMyCurve.Shape 
oMyShape.Settings.UseCurveExpansion = True 
oMyShape.XChannel.Reference = "" 
oMyShape.YChannel.Reference = "Temp_A" 
dd.Report.Settings.CurveExpansion.Expand() 
print ("Number of expanded curves: " + oMy2DAxisSystem.Curves2D.Count) 
for oMyExpandedCurve in oMy2DAxisSystem.Curves2D: 
    oMyExpandedCurve.Shape.Extensions.Marker.Type = dd.eMarkerCircle 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoclipboard_irepsheetint.htm language=enus -->
## TOPIC 01590: Method: ExportToClipboard for Sheet

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoclipboard_irepsheetint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoclipboard_irepsheetint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToClipboard for Sheet

Method: ExportToClipboard for Sheet

Exports a DIAdem REPORT worksheet as a graphic to the Windows clipboard.

```text
Object.ExportToClipboard()
```

| Object | SheetObject with this method |
| --- | --- |

The following example generates a worksheet with a circle and exports this worksheet as a graphic to the Windows clipboard:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMySheet, oMyCircle
Call Report.NewLayout()
Set oMySheet = Report.Sheets.Add("NewSheet")
Set oMyCircle = oMySheet.Objects.Add(eReportObjectCircle,"MyCircle")
Call oMyCircle.BackgroundColor.SetPredefinedColor(eColorIndexGreen)
oMyCircle.BorderLine.Width = eLineWidth0200
oMyCircle.BorderLine.LineType = eLineTypeSolid
Call oMyCircle.BorderLine.Color.SetPredefinedColor(eColorIndexRed)
Call oMySheet.ExportToClipboard()
```

[Copy script](javascript:void(0);)

```text
dd.Report.NewLayout() 
oMySheet = dd.Report.Sheets.Add("NewSheet") 
oMyCircle = oMySheet.Objects.Add(dd.eReportObjectCircle,"MyCircle") 
oMyCircle.BackgroundColor.SetPredefinedColor(dd.eColorIndexGreen) 
oMyCircle.BorderLine.Width = dd.eLineWidth0200 
oMyCircle.BorderLine.LineType = dd.eLineTypeSolid 
oMyCircle.BorderLine.Color.SetPredefinedColor(dd.eColorIndexRed) 
oMySheet.ExportToClipboard() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttohtml_irepsheetlistint.htm language=enus -->
## TOPIC 01591: Method: ExportToHTML for Sheets

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttohtml_irepsheetlistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttohtml_irepsheetlistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToHTML for Sheets

Method: ExportToHTML for Sheets

Exports all worksheets from DIAdem REPORT to an HTML file.

```text
Object.ExportToHTML(FileName)
```

| Object | SheetsObject with this method |
| --- | --- |
| FileName | StringSpecifies the path and the filename of the HTML file. |

The following example exports all worksheets to the HTML file MySheets:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Call Report.Sheets.ExportToHTML("d:\MySheets")
```

[Copy script](javascript:void(0);)

```text
dd.Report.Sheets.ExportToHTML("d:\\MySheets") 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_ireparrowint.htm language=enus -->
## TOPIC 01592: Method: ExportToImage for Arrow

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_ireparrowint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_ireparrowint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for Arrow

Method: ExportToImage for Arrow

Exports an arrow from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | ArrowObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example adds an arrow to the current worksheet, changes the arrow display, and then exports the arrow to the graphics file MyNewArrow.png:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyArrow, oMyArrowLine, oMyArrowLineColor, oMyArrowPosition
Set oMyArrow = Report.ActiveSheet.Objects.Add(eReportObjectArrow,"MyArrow")

oMyArrow.ArrowHeadAtBegin = eArrowHeadPoint
oMyArrow.ArrowHeadAtEnd = eArrowHeadStandardArrow

Set oMyArrowPosition = oMyArrow.Position.ByCoordinate
oMyArrowPosition.X1 = 10
oMyArrowPosition.X2 = 40
oMyArrowPosition.Y1 = 30
oMyArrowPosition.Y2 = 90

Set oMyArrowLine = oMyArrow.Line
oMyArrowLine.LineType = eLineTypeDotted
oMyArrowLine.Width = eLineWidth0200

Set oMyArrowLineColor = oMyArrowLine.Color
Call oMyArrowLineColor.SetPredefinedColor(eColorIndexGreen)

Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
Call oMyArrow.ExportToImage(LayoutWritePath & "MyNewArrow", eImageExportTypePNG)
```

[Copy script](javascript:void(0);)

```text
oMyArrow = dd.Report.ActiveSheet.Objects.Add(dd.eReportObjectArrow,"MyArrow") 
oMyArrow.ArrowHeadAtBegin = dd.eArrowHeadPoint 
oMyArrow.ArrowHeadAtEnd = dd.eArrowHeadStandardArrow 
oMyArrowPosition = oMyArrow.Position.ByCoordinate 
oMyArrowPosition.X1 = 10 
oMyArrowPosition.X2 = 40 
oMyArrowPosition.Y1 = 30 
oMyArrowPosition.Y2 = 90 
oMyArrowLine = oMyArrow.Line 
oMyArrowLine.LineType = dd.eLineTypeDotted 
oMyArrowLine.Width = dd.eLineWidth0200 
oMyArrowLineColor = oMyArrowLine.Color 
oMyArrowLineColor.SetPredefinedColor(dd.eColorIndexGreen) 
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
oMyArrow.ExportToImage(dd.LayoutWritePath + "MyNewArrow", dd.eImageExportTypePNG) 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepbasectrlint.htm language=enus -->
## TOPIC 01593: Method: ExportToImage for ReportObject

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepbasectrlint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepbasectrlint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for ReportObject

Method: ExportToImage for ReportObject

Exports an object from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | ReportObjectObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports all selected objects to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Width = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.IsSelected Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Width = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.IsSelected : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepcircleint.htm language=enus -->
## TOPIC 01594: Method: ExportToImage for Circle

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepcircleint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepcircleint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for Circle

Method: ExportToImage for Circle

Exports a circle from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | CircleObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example adds a circle to the current worksheet, changes the display of the circle, and then exports the circle into the graphics file MyCircle.png:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyCircle, oMyBackgroundColor, oMyBorderLineColor
Set oMyCircle = Report.ActiveSheet.Objects.Add(eReportObjectCircle,"MyCircle")

oMyCircle.ForceCircle = True

Set oMyBackgroundColor = oMyCircle.BackgroundColor
Call oMyBackgroundColor.SetPredefinedColor(eColorIndexRed )
oMyBackgroundColor.Transparency = 50

oMyCircle.Position.ByCoordinate.X1 = 10
oMyCircle.Position.ByCoordinate.X2 = 40
oMyCircle.Position.ByCoordinate.Y1 = 50
oMyCircle.Position.ByCoordinate.Y2 = 80

Set oMyBorderLineColor = oMyCircle.BorderLine.Color
Call oMyBorderLineColor.SetPredefinedColor(eColorIndexGreen)
oMyCircle.BorderLine.LineType = eLineTypeDotted
oMyCircle.BorderLine.Width = eLineWidth0140

Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
Call oMyCircle.ExportToImage(LayoutWritePath & "MyCircle", eImageExportTypePNG)
```

[Copy script](javascript:void(0);)

```text
oMyCircle = dd.Report.ActiveSheet.Objects.Add(dd.eReportObjectCircle,"MyCircle") 
oMyCircle.ForceCircle = True 
oMyBackgroundColor = oMyCircle.BackgroundColor 
oMyBackgroundColor.SetPredefinedColor(dd.eColorIndexRed ) 
oMyBackgroundColor.Transparency = 50 
oMyCircle.Position.ByCoordinate.X1 = 10 
oMyCircle.Position.ByCoordinate.X2 = 40 
oMyCircle.Position.ByCoordinate.Y1 = 50 
oMyCircle.Position.ByCoordinate.Y2 = 80 
oMyBorderLineColor = oMyCircle.BorderLine.Color 
oMyBorderLineColor.SetPredefinedColor(dd.eColorIndexGreen) 
oMyCircle.BorderLine.LineType = dd.eLineTypeDotted 
oMyCircle.BorderLine.Width = dd.eLineWidth0140 
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
oMyCircle.ExportToImage(dd.LayoutWritePath + "MyCircle", dd.eImageExportTypePNG) 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepcommentint.htm language=enus -->
## TOPIC 01595: Method: ExportToImage for Comment

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepcommentint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepcommentint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for Comment

Method: ExportToImage for Comment

Exports a comment from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | CommentObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each comment to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectComment Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectComment : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepd2axisint.htm language=enus -->
## TOPIC 01596: Method: ExportToImage for 2DAxisSystem

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepd2axisint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepd2axisint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for 2DAxisSystem

Method: ExportToImage for 2DAxisSystem

Exports a 2D axis system from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | 2DAxisSystemObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each 2D axis system to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObject2DAxisSystem Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObject2DAxisSystem : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepd3axisint.htm language=enus -->
## TOPIC 01597: Method: ExportToImage for 3DAxisSystem

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepd3axisint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepd3axisint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for 3DAxisSystem

Method: ExportToImage for 3DAxisSystem

Exports a 3D axis system from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | 3DAxisSystemObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each 3D axis system to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObject3DAxisSystem Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObject3DAxisSystem : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepformuladisplayint.htm language=enus -->
## TOPIC 01598: Method: ExportToImage for FormulaDisplay

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepformuladisplayint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepformuladisplayint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for FormulaDisplay

Method: ExportToImage for FormulaDisplay

Exports a formula graphic from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | FormulaDisplayObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each formula graphic to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectFormulaDisplay Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectFormulaDisplay : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepfreeframeint.htm language=enus -->
## TOPIC 01599: Method: ExportToImage for Frame

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepfreeframeint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepfreeframeint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for Frame

Method: ExportToImage for Frame

Exports a rectangle from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | FrameObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each rectangle to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectFrame Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectFrame : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepimageint.htm language=enus -->
## TOPIC 01600: Method: ExportToImage for Image

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepimageint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepimageint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for Image

Method: ExportToImage for Image

Exports a formula graphic from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | ImageObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each graphic to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectImage Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectImage : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_ireppiechartint.htm language=enus -->
## TOPIC 01601: Method: ExportToImage for PieChart

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_ireppiechartint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_ireppiechartint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for PieChart

Method: ExportToImage for PieChart

Exports a pie chart from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | PieChartObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports all pie charts to graphic files:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectPieChart Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectPieChart : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_ireppolarint.htm language=enus -->
## TOPIC 01602: Method: ExportToImage for PolarSystem

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_ireppolarint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_ireppolarint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for PolarSystem

Method: ExportToImage for PolarSystem

Exports a polar axis system from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | PolarSystemObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each polar axis system to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectPolarSystem Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectPolarSystem : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepsheetint.htm language=enus -->
## TOPIC 01603: Method: ExportToImage for Sheet

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepsheetint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepsheetint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for Sheet

Method: ExportToImage for Sheet

Exports a worksheet from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | SheetObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports all worksheets to individual graphics files:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB08
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.Sheets
For Each oMyReportObj in oMyReportObjects
  Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
  i = i+1
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB08 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.Sheets 
for oMyReportObj in oMyReportObjects: 
    oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
    i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_irepspiderint.htm language=enus -->
## TOPIC 01604: Method: ExportToImage for Spider

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_irepspiderint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_irepspiderint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for Spider

Method: ExportToImage for Spider

Exports a spider axis system from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | SpiderObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | 1eImageExportTypeEMF EMF file 2eImageExportTypePNG PNG file 3eImageExportTypeJPG JPG file 4eImageExportTypeGIF GIF file 5eImageExportTypeTIF TIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports all spider axis systems to graphic files:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectSpider Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectSpider : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_ireptable2dint.htm language=enus -->
## TOPIC 01605: Method: ExportToImage for 2DTable

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_ireptable2dint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_ireptable2dint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for 2DTable

Method: ExportToImage for 2DTable

Exports a 2D table from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | 2DTableObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each table to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObject2DTable Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObject2DTable : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_ireptable3dint.htm language=enus -->
## TOPIC 01606: Method: ExportToImage for 3DTable

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_ireptable3dint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_ireptable3dint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for 3DTable

Method: ExportToImage for 3DTable

Exports a 3D table from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | 3DTableObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each 3D table to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObject3DTable Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObject3DTable : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_ireptextobjectint.htm language=enus -->
## TOPIC 01607: Method: ExportToImage for RTFText

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_ireptextobjectint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_ireptextobjectint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for RTFText

Method: ExportToImage for RTFText

Exports a [Text object](../../gfsgraph/txtobj/txtobj_general_dialog.htm) from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | RTFTextObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each text object to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectRTFText Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectRTFText : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_exporttoimage_ireptextsimpleint.htm language=enus -->
## TOPIC 01608: Method: ExportToImage for Text

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_exporttoimage_ireptextsimpleint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_exporttoimage_ireptextsimpleint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: ExportToImage for Text

Method: ExportToImage for Text

Exports a text from DIAdem REPORT to a graphics file.

```text
Object.ExportToImage(FileName, ImageType)
```

| Object | TextObject with this method |  |
| --- | --- | --- |
| FileName | StringSpecifies the path and the filename of the graphics file. |  |
| ImageType | Specifies the graphics file type.Enumeration with the following selection terms: 1 eImageExportTypeEMFEMF file 2 eImageExportTypePNGPNG file 3 eImageExportTypeJPGJPG file 4 eImageExportTypeGIFGIF file 5 eImageExportTypeTIFTIF file |  |
| 1 | eImageExportTypeEMF | EMF file |
| 2 | eImageExportTypePNG | PNG file |
| 3 | eImageExportTypeJPG | JPG file |
| 4 | eImageExportTypeGIF | GIF file |
| 5 | eImageExportTypeTIF | TIF file |

The following example exports each text to a graphics file:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, i
Report.Settings.ImageExport.PNG.BitsPerPixel = ePNGBitsPerPixelRGB24
Report.Settings.ImageExport.PNG.Height = 300
Report.Settings.ImageExport.PNG.UseRatio = True
i = 0
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObjectText Then
    Call oMyReportObj.ExportToImage(LayoutWritePath & "MyExportFile" & i, eImageExportTypePNG)
    i = i+1
  End If
Next
```

[Copy script](javascript:void(0);)

```text
Report.Settings.ImageExport.PNG.BitsPerPixel = dd.ePNGBitsPerPixelRGB24 
Report.Settings.ImageExport.PNG.Height = 300 
Report.Settings.ImageExport.PNG.UseRatio = True 
i = 0 
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObjectText : 
        oMyReportObj.ExportToImage(dd.LayoutWritePath + "MyExportFile" + i, dd.eImageExportTypePNG) 
        i = i+1 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

#### Related Topics

[Command: ExecuteExclusiveBegin](../../comoff/executeexclusivebegin.htm) | [Command: ExecuteExclusiveEnd](../../comoff/executeexclusiveend.htm) | [Command: ExecuteExclusiveEndAll](../../comoff/executeexclusiveendall.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_item_irepd3selectedsubobjectslistint.htm language=enus -->
## TOPIC 01609: Method: Item for 3DSelectedElements

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_item_irepd3selectedsubobjectslistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_item_irepd3selectedsubobjectslistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Item for 3DSelectedElements

Method: Item for 3DSelectedElements

Returns the selected element associated with a specific index in a 3D axis system in DIAdem REPORT.

```text
Set o3DSelectedElement = Object.Item(Index)
```

| Object | 3DSelectedElementsObject with this method |
| --- | --- |
| Index | LongIntegerSpecifies the index of the selected element. |
| o3DSelectedElement | 3DSelectedElementReturned object |

|  | Note You can always omit the Item method because it is the standard element of the collection. |
| --- | --- |

The following example checks whether elements of a 3D axis system are selected in the current worksheet and displays the name of the axis system, the number of selected elements, and their type:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMyReportObj, oMyReportObjects, oMySelection, sOutput, i
Set oMyReportObjects = Report.ActiveSheet.Objects
For Each oMyReportObj in oMyReportObjects
  If oMyReportObj.ObjectType = eReportObject3DAxisSystem Then
    Set oMySelection = oMyReportObj.SelectedElements
    sOutput = "Object name: " & oMyReportObj.Name & vbCrLf &_
              "Number of selected elements: " & oMySelection.Count & vbCrLf
    For i = 1 to oMySelection.Count
      sOutput = sOutput & "Element type: " & oMySelection.Item(i).Type & vbCrLf
    Next
    Call MsgBoxDisp(sOutput)
  End If
Next
```

[Copy script](javascript:void(0);)

```text
oMyReportObjects = dd.Report.ActiveSheet.Objects 
for oMyReportObj in oMyReportObjects: 
    if oMyReportObj.ObjectType == dd.eReportObject3DAxisSystem : 
        oMySelection = oMyReportObj.Select()edElements 
        sOutput = "Object name: " + oMyReportObj.Name + "\r\n" +"Number of selected elements: " + oMySelection.Count + "\r\n" 
        for i in range( 1, oMySelection.Count + 1): 
            sOutput = sOutput + "Element type: " + oMySelection.Item(i).Type + "\r\n" 
        dd.MsgBoxDisp(sOutput) 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)

<!--NI_TOPIC bundle=diadem path=reportapi/methods/report_method_move_irepd2curvelistint.htm language=enus -->
## TOPIC 01610: Method: Move for 2DCurves

- bundle_id: `diadem`
- source_path: `reportapi/methods/report_method_move_irepd2curvelistint.htm`
- source_url: https://docs-be.ni.com/bundle/diadem/raw/resource/enus/reportapi/methods/report_method_move_irepd2curvelistint.htm
- source_language: `enus`
- document_id: `diadem`
- page_type: `leaf`
- content_type: ``

[DIAdem REPORT](../reportapi_overview.htm) > [Methods](../methods/report_method_overview.htm) > Method: Move for 2DCurves

Method: Move for 2DCurves

Moves in a 2D axis system in DIAdem REPORT a curve to a different position.

```text
Object.Move(NameOrIndexFrom, NameOrIndexTo)
```

| Object | 2DCurvesObject with this method |
| --- | --- |
| NameOrIndexFrom | VariantSpecifies the name or the index of the curve that is to be moved. |
| NameOrIndexTo | VariantSpecifies the name or the index of the curve to where DIAdem shifts the curve to be moved. |

The following example creates a 2D axis system with two curves and shifts the second curve to the position of the first curve:

| VBScript | Python |
| --- | --- |

[Copy script](javascript:void(0);)

```text
Dim oMy2DAxisSys, oMyPosition, oMyCurve1, oMyCurve2, oMy2DCurves
Call Data.Root.Clear()
Call DataFileLoad(DataReadPath & "Report_Data.tdm","TDM","")
Call Report.NewLayout()
Set oMy2DAxisSys = Report.ActiveSheet.Objects.Add(eReportObject2DAxisSystem,"My2DAxisSystem")
Set oMyPosition = oMy2DAxisSys.Position.ByCoordinate
oMyPosition.X1 = 10
oMyPosition.X2 = 40
oMyPosition.Y1 = 10
oMyPosition.Y2 = 40
Set oMyCurve1 = oMy2DAxisSys.Curves2D.Add(e2DShapeLine, "MyNewCurve1")
oMyCurve1.Shape.XChannel.Reference= "[5]/[1]"
oMyCurve1.Shape.YChannel.Reference = "[5]/[2]"
Set oMyCurve2 = oMy2DAxisSys.Curves2D.Add(e2DShapeLine, "MyNewCurve2")
oMyCurve2.Shape.XChannel.Reference= "[5]/[3]"
oMyCurve2.Shape.YChannel.Reference = "[5]/[4]"
Set oMy2DCurves = oMy2DAxisSys.Curves2D
Call oMy2DCurves.Move(1,2)
Call Report.Refresh()
```

[Copy script](javascript:void(0);)

```text
dd.Data.Root.Clear() 
dd.DataFileLoad(dd.DataReadPath + "Report_Data.tdm","TDM","") 
dd.Report.NewLayout() 
oMy2DAxisSys = dd.Report.ActiveSheet.Objects.Add(dd.eReportObject2DAxisSystem,"My2DAxisSystem") 
oMyPosition = oMy2DAxisSys.Position.ByCoordinate 
oMyPosition.X1 = 10 
oMyPosition.X2 = 40 
oMyPosition.Y1 = 10 
oMyPosition.Y2 = 40 
oMyCurve1 = oMy2DAxisSys.Curves2D.Add(dd.e2DShapeLine, "MyNewCurve1") 
oMyCurve1.Shape.XChannel.Reference= "[5]/[1]" 
oMyCurve1.Shape.YChannel.Reference = "[5]/[2]" 
oMyCurve2 = oMy2DAxisSys.Curves2D.Add(dd.e2DShapeLine, "MyNewCurve2") 
oMyCurve2.Shape.XChannel.Reference= "[5]/[3]" 
oMyCurve2.Shape.YChannel.Reference = "[5]/[4]" 
oMy2DCurves = oMy2DAxisSys.Curves2D 
oMy2DCurves.Move(1,2) 
dd.Report.Refresh() 
```

#### See Also

[Objects Overview](../objects/irepreportint_objects_overview.htm)
