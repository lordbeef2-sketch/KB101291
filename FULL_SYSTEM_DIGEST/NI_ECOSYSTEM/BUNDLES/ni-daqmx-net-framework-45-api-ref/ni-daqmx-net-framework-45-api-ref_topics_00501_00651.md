# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-45-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-45-api-ref start=501 end=651 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_basictedsdataoption.htm language=enus -->
## TOPIC 00501: BasicTedsDataOption Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_basictedsdataoption.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_basictedsdataoption.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

BasicTedsDataOption Enumeration

### BasicTedsDataOption Enumeration

basic TEDS data

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum BasicTedsDataOption
```

```text
Public Enumeration BasicTedsDataOption
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | WriteToEeprom | 12538 | Basic TEDS data is written to the EEPROM, even if the sensor includes a PROM. You cannot write basic TEDS data if the PROM contains data. |
|  | WriteToProm | 12539 | Basic TEDS data is written to the PROM. Any subsequent attempts to write basic TEDS data results in an error. |
|  | DoNotWrite | 12540 | Basic TEDS data is ignored. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_bridgeshuntcalibrationsource.htm language=enus -->
## TOPIC 00502: BridgeShuntCalibrationSource Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_bridgeshuntcalibrationsource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_bridgeshuntcalibrationsource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

BridgeShuntCalibrationSource Enumeration

### BridgeShuntCalibrationSource Enumeration

Specifies whether to use internal or external shunt when Shunt Cal A is selected.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum BridgeShuntCalibrationSource
```

```text
Public Enumeration BridgeShuntCalibrationSource
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | BuiltIn | 10200 | Use the internal shunt. |
|  | UserProvided | 10167 | Use an external shunt. |

##### Remarks

BridgeShuntCalibrationASource

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration4463.htm language=enus -->
## TOPIC 00503: CalibrationInputTerminalConfiguration4463 Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration4463.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_calibrationinputterminalconfiguration4463.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CalibrationInputTerminalConfiguration4463 Enumeration

### CalibrationInputTerminalConfiguration4463 Enumeration

Specifies the input terminal configuration for the channel to calibrate on an NI PXIe 4463 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CalibrationInputTerminalConfiguration4463
```

```text
Public Enumeration CalibrationInputTerminalConfiguration4463
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | A differential input terminal configuration. |
|  | Pseudodifferential | 12529 | A pseudodifferential input terminal configuration. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_calibrationmode4480.htm language=enus -->
## TOPIC 00504: CalibrationMode4480 Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_calibrationmode4480.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_calibrationmode4480.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CalibrationMode4480 Enumeration

### CalibrationMode4480 Enumeration

Specifies which measurements to use to calibrate an NI 4480 device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CalibrationMode4480
```

```text
Public Enumeration CalibrationMode4480
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Voltage | 10322 | Voltage mode. |
|  | Charge | 16105 | Charge mode. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_changedetectioneventpulsepolarity.htm language=enus -->
## TOPIC 00505: ChangeDetectionEventPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_changedetectioneventpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_changedetectioneventpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ChangeDetectionEventPulsePolarity Enumeration

### ChangeDetectionEventPulsePolarity Enumeration

Specifies the polarity of an exported Change Detection Event pulse.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ChangeDetectionEventPulsePolarity
```

```text
Public Enumeration ChangeDetectionEventPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

ChangeDetectionEventPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirection.htm language=enus -->
## TOPIC 00506: CICountEdgesCountDirection Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesCountDirection Enumeration

### CICountEdgesCountDirection Enumeration

Specifies whether to increment or decrement the counter on each edge.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesCountDirection
```

```text
Public Enumeration CICountEdgesCountDirection
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Up | 10128 | Increment counter. |
|  | Down | 10124 | Decrement counter. |
|  | ExternallyControlled | 10326 | The state of a digital line controls the count direction. Each counter has a default count direction terminal. |

##### Remarks

CountEdgesCountDirection

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionlogiclevelbehavior.htm language=enus -->
## TOPIC 00507: CICountEdgesCountDirectionLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesCountDirectionLogicLevelBehavior Enumeration

### CICountEdgesCountDirectionLogicLevelBehavior Enumeration

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesCountDirectionLogicLevelBehavior
```

```text
Public Enumeration CICountEdgesCountDirectionLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

CountEdgesCountDirectionLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionterminalconfiguration.htm language=enus -->
## TOPIC 00508: CICountEdgesCountDirectionTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cicountedgescountdirectionterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CICountEdgesCountDirectionTerminalConfiguration Enumeration

### CICountEdgesCountDirectionTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CICountEdgesCountDirectionTerminalConfiguration
```

```text
Public Enumeration CICountEdgesCountDirectionTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

CountEdgesCountDirectionTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cidutycyclelogiclevelbehavior.htm language=enus -->
## TOPIC 00509: CIDutyCycleLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cidutycyclelogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cidutycyclelogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDutyCycleLogicLevelBehavior Enumeration

### CIDutyCycleLogicLevelBehavior Enumeration

Specifies the logic level behavior on the input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIDutyCycleLogicLevelBehavior
```

```text
Public Enumeration CIDutyCycleLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

DutyCycleLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cidutycyclestartingedge.htm language=enus -->
## TOPIC 00510: CIDutyCycleStartingEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cidutycyclestartingedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cidutycyclestartingedge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIDutyCycleStartingEdge Enumeration

### CIDutyCycleStartingEdge Enumeration

Specifies which edge of the input signal to begin the duty cycle measurement.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIDutyCycleStartingEdge
```

```text
Public Enumeration CIDutyCycleStartingEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

DutyCycleStartingEdge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderainputlogiclevelbehavior.htm language=enus -->
## TOPIC 00511: CIEncoderAInputLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderainputlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderainputlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIEncoderAInputLogicLevelBehavior Enumeration

### CIEncoderAInputLogicLevelBehavior Enumeration

Specifies the logic level behavior on the input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIEncoderAInputLogicLevelBehavior
```

```text
Public Enumeration CIEncoderAInputLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

EncoderAInputLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderzinputlogiclevelbehavior.htm language=enus -->
## TOPIC 00512: CIEncoderZInputLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderzinputlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderzinputlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIEncoderZInputLogicLevelBehavior Enumeration

### CIEncoderZInputLogicLevelBehavior Enumeration

Specifies the logic level behavior on the input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIEncoderZInputLogicLevelBehavior
```

```text
Public Enumeration CIEncoderZInputLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

EncoderZInputLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderzinputterminalconfiguration.htm language=enus -->
## TOPIC 00513: CIEncoderZInputTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderzinputterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ciencoderzinputterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIEncoderZInputTerminalConfiguration Enumeration

### CIEncoderZInputTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIEncoderZInputTerminalConfiguration
```

```text
Public Enumeration CIEncoderZInputTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

EncoderZInputTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifilterdelayunits.htm language=enus -->
## TOPIC 00514: CIFilterDelayUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifilterdelayunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifilterdelayunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIFilterDelayUnits Enumeration

### CIFilterDelayUnits Enumeration

FilterDelay

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIFilterDelayUnits
```

```text
Public Enumeration CIFilterDelayUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Seconds | 10364 | Seconds. |
|  | SampleClockPeriods | 10286 | Sample Clock Periods. |

##### Remarks

FilterDelay

FilterDelayUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifilterresponse.htm language=enus -->
## TOPIC 00515: CIFilterResponse Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifilterresponse.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifilterresponse.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIFilterResponse Enumeration

### CIFilterResponse Enumeration

Specifies the corresponding filter response and defines the shape of the filter response.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIFilterResponse
```

```text
Public Enumeration CIFilterResponse
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Comb | 16152 | Comb filter response. |
|  | Bessel | 16153 | Bessel filter response. |
|  | Brickwall | 16155 | Brickwall filter response. |
|  | Butterworth | 16076 | Butterworth filter response. |

##### Remarks

FilterResponse

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifrequencylogiclevelbehavior.htm language=enus -->
## TOPIC 00516: CIFrequencyLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifrequencylogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cifrequencylogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIFrequencyLogicLevelBehavior Enumeration

### CIFrequencyLogicLevelBehavior Enumeration

Specifies the logic level behavior on the input line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIFrequencyLogicLevelBehavior
```

```text
Public Enumeration CIFrequencyLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

FrequencyLogicalLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondlogiclevelbehavior.htm language=enus -->
## TOPIC 00517: CITwoEdgeSeparationSecondLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_citwoedgeseparationsecondlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CITwoEdgeSeparationSecondLogicLevelBehavior Enumeration

### CITwoEdgeSeparationSecondLogicLevelBehavior Enumeration

Specifies the logic level behavior on the count reset line.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CITwoEdgeSeparationSecondLogicLevelBehavior
```

```text
Public Enumeration CITwoEdgeSeparationSecondLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

TwoEdgeSeparationSecondLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_citwoedgeseparationunits.htm language=enus -->
## TOPIC 00518: CITwoEdgeSeparationUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_citwoedgeseparationunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_citwoedgeseparationunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CITwoEdgeSeparationUnits Enumeration

### CITwoEdgeSeparationUnits Enumeration

Specifies the units to use to return two-edge separation measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CITwoEdgeSeparationUnits
```

```text
Public Enumeration CITwoEdgeSeparationUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Seconds | 10364 | Seconds. |
|  | Ticks | 10304 | Timebase ticks. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

TwoEdgeSeparationUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityainputlogiclevelbehavior.htm language=enus -->
## TOPIC 00519: CIVelocityAInputLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityainputlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityainputlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityAInputLogicLevelBehavior Enumeration

### CIVelocityAInputLogicLevelBehavior Enumeration

Specifies the logic level behavior of the input terminal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityAInputLogicLevelBehavior
```

```text
Public Enumeration CIVelocityAInputLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

VelocityAInputLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityainputterminalconfiguration.htm language=enus -->
## TOPIC 00520: CIVelocityAInputTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityainputterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityainputterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityAInputTerminalConfiguration Enumeration

### CIVelocityAInputTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityAInputTerminalConfiguration
```

```text
Public Enumeration CIVelocityAInputTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

VelocityAInputTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityangularencoderunits.htm language=enus -->
## TOPIC 00521: CIVelocityAngularEncoderUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityangularencoderunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityangularencoderunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityAngularEncoderUnits Enumeration

### CIVelocityAngularEncoderUnits Enumeration

Specifies the units to use to return angular velocity counter measurements.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityAngularEncoderUnits
```

```text
Public Enumeration CIVelocityAngularEncoderUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | RPM | 16080 | Revolutions per minute. |
|  | RadiansPerSecond | 16081 | Radians per second. |
|  | DegreesPerSecond | 16082 | Degrees per second. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

VelocityAngularEncoderUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitybinputlogiclevelbehavior.htm language=enus -->
## TOPIC 00522: CIVelocityBInputLogicLevelBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitybinputlogiclevelbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitybinputlogiclevelbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityBInputLogicLevelBehavior Enumeration

### CIVelocityBInputLogicLevelBehavior Enumeration

Specifies the logic level behavior of the input terminal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityBInputLogicLevelBehavior
```

```text
Public Enumeration CIVelocityBInputLogicLevelBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | LogicLevelPullUp | 16064 | High logic. |
|  | None | 10230 | Supply no excitation to the channel. |

##### Remarks

VelocityBInputLogicLevelBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitybinputterminalconfiguration.htm language=enus -->
## TOPIC 00523: CIVelocityBInputTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitybinputterminalconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitybinputterminalconfiguration.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityBInputTerminalConfiguration Enumeration

### CIVelocityBInputTerminalConfiguration Enumeration

Specifies the input terminal configuration.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityBInputTerminalConfiguration
```

```text
Public Enumeration CIVelocityBInputTerminalConfiguration
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Differential | 10106 | Differential. |
|  | Rse | 10083 | Referenced Single-Ended. |

##### Remarks

VelocityBInputTerminalConfiguration

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityencodertype.htm language=enus -->
## TOPIC 00524: CIVelocityEncoderType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityencodertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocityencodertype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityEncoderType Enumeration

### CIVelocityEncoderType Enumeration

Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. Two Pulse Counting is valid for two-pulse encoders only.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityEncoderType
```

```text
Public Enumeration CIVelocityEncoderType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | X1 | 10090 | If signal A leads signal B, count the rising edges of signal A. If signal B leads signal A, count the falling edges of signal A. |
|  | X2 | 10091 | Count the rising and falling edges of signal A. |
|  | X4 | 10092 | Count the rising and falling edges of signal A and signal B. |
|  | TwoPulseCounting | 10313 | Increment the count on rising edges of signal A. Decrement the count on rising edges of signal B. |

##### Remarks

VelocityDecodingType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitylinearencoderunits.htm language=enus -->
## TOPIC 00525: CIVelocityLinearEncoderUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitylinearencoderunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_civelocitylinearencoderunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CIVelocityLinearEncoderUnits Enumeration

### CIVelocityLinearEncoderUnits Enumeration

Specifies the units to use to return linear encoder velocity measurements from the channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CIVelocityLinearEncoderUnits
```

```text
Public Enumeration CIVelocityLinearEncoderUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MetersPerSecond | 15959 | Meters per second. |
|  | InchesPerSecond | 15960 | Inches per second. |
|  | FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

##### Remarks

VelocityLinearEncoderUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cochannel.htm language=enus -->
## TOPIC 00526: COChannel Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cochannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cochannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COChannel Class

### COChannel Class

Encapsulates one or more counter/timer output channels and the properties for a counter/timer output channel.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class COChannel : Channel, IFilteredTypeDescriptor
```

```text
Public Class COChannel
	Inherits Channel
	Implements IFilteredTypeDescriptor
```

The COChannel type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AutoIncrementCount | Specifies a number of timebase ticks by which to increase the time spent in the idle state for each successive pulse. |
|  | ConstrainedGenerationMode | Specifies constraints to apply when the counter generates pulses. Constraining the counter reduces the device resources required for counter operation. Constraining the counter can also allow additional analog or counter tasks on the device to run concurrently. For continuous counter tasks, NI-DAQmx consumes no device resources when the counter is constrained. For finite counter tasks, resource use increases with the frequency regardless of the constraint mode. However, fixed frequency constraints significantly reduce resource usage, and fixed duty cycle constraint marginally reduces it. |
|  | Count | Indicates the current value of the count register. |
|  | CounterTimebaseActiveEdge | Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. |
|  | CounterTimebaseDigitalFilterEnable | Specifies whether to apply the pulse width filter to the signal. |
|  | CounterTimebaseDigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | CounterTimebaseDigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | CounterTimebaseDigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | CounterTimebaseDigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | CounterTimebaseMasterTimebaseDivisor | Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to generate slower signals without causing the count register to roll over. |
|  | CounterTimebaseRate | Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to define output pulses in seconds rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can define output pulses only in ticks of the timebase. |
|  | CounterTimebaseSource | Specifies the terminal of the timebase to use for the counter. Typically, NI-DAQmx uses one of the internal counter timebases when generating pulses. Use this property to specify an external timebase and produce custom pulse widths that are not possible using the internal timebases. |
|  | DataTransferMechanism | Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled. |
|  | DataTransferRequestCondition | Specifies under what condition to transfer data from the buffer to the onboard memory of the device. |
|  | Description | Specifies a user-defined description for the channel. (Inherited from Channel.) |
|  | EnableInitialDelayOnRetrigger | Specifies whether to apply the initial delay to retriggered pulse trains. |
|  | IsGlobal | Indicates whether the channel is a global channel. (Inherited from Channel.) |
|  | MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
|  | OutputState | Indicates the current state of the output terminal of the counter. |
|  | OutputType | Indicates how to define pulses generated on the channel. |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. (Inherited from Channel.) |
|  | Prescaler | Specifies the divisor to apply to the signal you connect to the counter source terminal. Pulse generations defined by frequency or time take this setting into account, but pulse generations defined by ticks do not. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase. |
|  | PulseDone | Indicates if the task completed pulse generation. Use this value for retriggerable pulse generation when you need to determine if the device generated the current pulse. For retriggerable tasks, when you query this property, NI-DAQmx resets it to . |
|  | PulseDutyCycle | Specifies the duty cycle of the pulses. The duty cycle of a signal is the width of the pulse divided by period. NI-DAQmx uses this ratio and the pulse frequency to determine the width of the pulses and the delay between pulses. |
|  | PulseFrequency | Specifies the frequency of the pulses to generate. This value is in the units you specify with PulseFrequencyUnits or when you create the channel. |
|  | PulseFrequencyInitialDelay | Specifies in seconds the amount of time to wait before generating the first pulse. |
|  | PulseFrequencyUnits | Specifies the units in which to define pulse frequency. |
|  | PulseHighTicks | Specifies the number of ticks the pulse is high. |
|  | PulseHighTime | Specifies the amount of time that the pulse is at a high voltage. This value is in the units you specify with PulseTimeUnits or when you create the channel. |
|  | PulseIdleState | Specifies the resting state of the output terminal. |
|  | PulseLowTicks | Specifies the number of ticks the pulse is low. |
|  | PulseLowTime | Specifies the amount of time that the pulse is at a low voltage. This value is in the units you specify with PulseTimeUnits or when you create the channel. |
|  | PulseTerminal | Specifies on which terminal to generate pulses. |
|  | PulseTicksInitialDelay | Specifies the number of ticks to wait before generating the first pulse. |
|  | PulseTimeInitialDelay | Specifies in seconds the amount of time to wait before generating the first pulse. |
|  | PulseTimeUnits | Specifies the units in which to define high and low pulse time. |
|  | ReadyForNewValue | Indicates whether the counter is ready for new continuous pulse train values. |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. (Inherited from Channel.) |
|  | Type | Indicates the type of the virtual channel. (Inherited from Channel.) |
|  | UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
|  | UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
|  | UseOnlyOnBoardMemory | Specifies whether to write samples directly to the onboard memory of the device, bypassing the memory buffer. Generally, you cannot update onboard memory directly after you start the task. Onboard memory includes data FIFOs. |
|  | VirtualName | Gets the name of the virtual channel. (Inherited from Channel.) |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Channel. (Inherited from Channel.) |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Channel or optionally releases only the unmanaged resources. (Inherited from Channel.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Inherited from Channel.) |

Top

##### Remarks

COChannels

COChannel

COChannel

COChannels

COChannelCollection

COChannel

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cochannelcollection.htm language=enus -->
## TOPIC 00527: COChannelCollection Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cochannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_cochannelcollection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COChannelCollection Class

### COChannelCollection Class

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class COChannelCollection : MarshalByRefObject, 
	ICollection
```

```text
Public Class COChannelCollection
	Inherits MarshalByRefObject
	Implements ICollection
```

The COChannelCollection type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets a COChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the COChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the COChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | CreatePulseChannelFrequency | Creates a COChannel to generate digital pulses defined by frequency and duty cycle. This method adds one or more channels to the COChannelCollection. |
|  | CreatePulseChannelTicks | Creates a COChannel to generate digital pulses defined by the number of timebase ticks that the pulse is at the high and low states. This method adds one or more channels to the COChannelCollection. |
|  | CreatePulseChannelTime | Creates a COChannel to generate digital pulses defined by the amount of time that the pulse is at the high and low states. This method adds one or more channels to the COChannelCollection. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetEnumerator | Returns an enumerator that you can use to iterate through the collection. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_coconstrainedgenerationmode.htm language=enus -->
## TOPIC 00528: COConstrainedGenerationMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_coconstrainedgenerationmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_coconstrainedgenerationmode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COConstrainedGenerationMode Enumeration

### COConstrainedGenerationMode Enumeration

Specifies constraints to apply when the counter generates pulses. Constraining the counter reduces the device resources required for counter operation. Constraining the counter can also allow additional analog or counter tasks on the device to run concurrently. For continuous counter tasks, NI-DAQmx consumes no device resources when the counter is constrained. For finite counter tasks, resource use increases with the frequency regardless of the constraint mode. However, fixed frequency constraints significantly reduce resource usage, and fixed duty cycle constraint marginally reduces it.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum COConstrainedGenerationMode
```

```text
Public Enumeration COConstrainedGenerationMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Unconstrained | 14708 | Counter has no restrictions on pulse generation. |
|  | FixedHighFrequency | 14709 | Pulse frequency must be above 7.63 Hz and cannot change while the task runs. In this mode, the duty cycle has 8 bits of resolution. |
|  | FixedLowFrequency | 14710 | Pulse frequency must be below 366.21 Hz and cannot change while the task runs. In this mode, the duty cycle has 16 bits of resolution. |
|  | Fixed50PercentDutyCycle | 14711 | Pulse duty cycle must be 50 percent. The frequency can change while the task runs. |

##### Remarks

ConstrainedGenerationMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_codatafrequency.htm language=enus -->
## TOPIC 00529: CODataFrequency Structure

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_codatafrequency.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_codatafrequency.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataFrequency Structure

### CODataFrequency Structure

Encapsulates a counter output specified in terms of frequency and duty cycle.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public struct CODataFrequency : ISerializable
```

```text
<SerializableAttribute>
Public Structure CODataFrequency
	Implements ISerializable
```

The CODataFrequency type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DutyCycle | Gets or sets the duty cycle of the pulse. |
|  | Frequency | Gets or sets the frequency of the pulse. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CODataFrequency) | Returns a value indicating if this instance is equal to the specified CODataFrequency object. |
|  | Equals(CODataFrequency, CODataFrequency) | Returns a value indicating if two specified instances of CODataFrequency are equal. |
|  | GetHashCode | Returns a hash code for the CODataFrequency object. (Overrides ValueTypeGetHashCode.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns true if two CODataFrequency objects are equal. |
|  | Inequality | Returns true if two CODataFrequency objects are not equal. |

Top

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_codataticks.htm language=enus -->
## TOPIC 00530: CODataTicks Structure

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_codataticks.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_codataticks.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CODataTicks Structure

### CODataTicks Structure

Encapsulates a counter output specified in terms of timebase ticks.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public struct CODataTicks : ISerializable
```

```text
<SerializableAttribute>
Public Structure CODataTicks
	Implements ISerializable
```

The CODataTicks type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | HighTicksInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | HighTicksUInt32 | Gets or sets the number of timebase ticks the pulse is high. |
|  | LowTicksInt32 | Gets or sets the number of timebase ticks the pulse is low. |
|  | LowTicksUInt32 | Gets or sets the number of timebase ticks the pulse is low. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals(Object) | Returns a value indicating if this instance is equal to the specified object. (Overrides ValueTypeEquals(Object).) |
|  | Equals(CODataTicks) | Returns a value indicating if this instance is equal to the specified CODataTicks object. |
|  | Equals(CODataTicks, CODataTicks) | Returns a value indicating if two specified instances of CODataTicks are equal. |
|  | GetHashCode | Returns a hash code for the CODataTicks object. (Overrides ValueTypeGetHashCode.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | ToString | Returns the fully qualified type name of this instance. (Inherited from ValueType.) |

Top

##### Operators

|  | Name | Description |
| --- | --- | --- |
|  | Equality | Returns true if two CODataTicks objects are equal. |
|  | Inequality | Returns true if two CODataTicks objects are not equal. |

Top

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_copulseidlestate.htm language=enus -->
## TOPIC 00531: COPulseIdleState Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_copulseidlestate.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_copulseidlestate.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COPulseIdleState Enumeration

### COPulseIdleState Enumeration

Specifies the resting state of the output terminal.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum COPulseIdleState
```

```text
Public Enumeration COPulseIdleState
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | High | 10192 | High state. |
|  | Low | 10214 | Low state. |

##### Remarks

PulseIdleState

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_copulsetimeunits.htm language=enus -->
## TOPIC 00532: COPulseTimeUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_copulsetimeunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_copulsetimeunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

COPulseTimeUnits Enumeration

### COPulseTimeUnits Enumeration

Specifies the units in which to define high and low pulse time.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum COPulseTimeUnits
```

```text
Public Enumeration COPulseTimeUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Seconds | 10364 | Seconds. |

##### Remarks

PulseTimeUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countermultichannelreader.htm language=enus -->
## TOPIC 00533: CounterMultiChannelReader Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countermultichannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countermultichannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelReader Class

### CounterMultiChannelReader Class

Contains methods for reading samples from one or more counter input channels in a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class CounterMultiChannelReader : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class CounterMultiChannelReader
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The CounterMultiChannelReader type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CounterMultiChannelReader | Creates a new instance of the CounterMultiChannelReader class to read from the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double, ReallocationPolicy) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleDouble | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleInt32 | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
|  | BeginReadMultiSampleUInt32 | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleDouble | Begins an asynchronous read of a single Double sample from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleInt32 | Begins an asynchronous read of a single Int32 sample from one or more CIChannel objects in a task. |
|  | BeginReadSingleSampleUInt32 | Begins an asynchronous read of a single UInt32 sample from one or more CIChannel objects in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) and retrieves the read samples. |
|  | EndReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleDouble | Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, Object) and retrieves the read sample. |
|  | EndReadSingleSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, Object) and retrieves the read sample. |
|  | EndReadSingleSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, Object) and retrieves the read sample. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, Int32) | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, ReallocationPolicy, Int32) | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, Int32) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, ReallocationPolicy, Int32) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, Int32) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleDouble | Reads one or more Double samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleInt32 | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
|  | ReadMultiSampleUInt32 | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
|  | ReadSingleSampleDouble | Reads a single Double sample from one or more CIChannel objects in a task. |
|  | ReadSingleSampleInt32 | Reads a single Int32 sample from one or more CIChannel objects in a task. |
|  | ReadSingleSampleUInt32 | Reads a single UInt32 sample from one or more CIChannel objects in a task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countermultichannelwriter.htm language=enus -->
## TOPIC 00534: CounterMultiChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countermultichannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countermultichannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterMultiChannelWriter Class

### CounterMultiChannelWriter Class

Contains methods for writing samples to one or more counter output channels in a counter output task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class CounterMultiChannelWriter : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class CounterMultiChannelWriter
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The CounterMultiChannelWriter type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CounterMultiChannelWriter | Initializes a new instance of the CounterMultiChannelWriter class to write to the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object) | Begins an asynchronous write of a single frequency sample to one or more COChannel objects in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTicks, AsyncCallback, Object) | Begins an asynchronous write of a single ticks sample to one or more COChannel objects in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTime, AsyncCallback, Object) | Begins an asynchronous write of a single time sample to one or more COChannel objects in a counter output task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndWrite | Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object). |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteSingleSample(Boolean, CODataFrequency) | Writes a single frequency sample to one or more COChannel objects in a counter output task. |
|  | WriteSingleSample(Boolean, CODataTicks) | Writes a single ticks sample to one or more COChannel objects in a counter output task. |
|  | WriteSingleSample(Boolean, CODataTime) | Writes a single time sample to one or more COChannel objects in a counter output task. |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_counteroutputeventargs.htm language=enus -->
## TOPIC 00535: CounterOutputEventArgs Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_counteroutputeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_counteroutputeventargs.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterOutputEventArgs Class

### CounterOutputEventArgs Class

CounterOutput

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class CounterOutputEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class CounterOutputEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The CounterOutputEventArgs type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_counteroutputeventoutputbehavior.htm language=enus -->
## TOPIC 00536: CounterOutputEventOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_counteroutputeventoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_counteroutputeventoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterOutputEventOutputBehavior Enumeration

### CounterOutputEventOutputBehavior Enumeration

Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum CounterOutputEventOutputBehavior
```

```text
Public Enumeration CounterOutputEventOutputBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Pulse | 10265 | Send a pulse to the terminal. |
|  | Toggle | 10307 | Toggle the state of the terminal from low to high or from high to low. |

##### Remarks

CounterOutputEventOutputBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countersinglechannelreader.htm language=enus -->
## TOPIC 00537: CounterSingleChannelReader Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countersinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countersinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelReader Class

### CounterSingleChannelReader Class

Contains methods for reading samples from the counter input channel in a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class CounterSingleChannelReader : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class CounterSingleChannelReader
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The CounterSingleChannelReader type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CounterSingleChannelReader | Creates a new instance of the CounterSingleChannelReader class to read from the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) | Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency) | Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks) | Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime) | Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. |
|  | BeginReadMultiSampleDouble | Begins an asynchronous read of one or more Double samples from a counter task. |
|  | BeginReadMultiSampleInt32 | Begins an asynchronous read of one or more Int32 samples from a counter task. |
|  | BeginReadMultiSamplePulseFrequency | Begins an asynchronous read of one or more pulse samples in terms of frequency from a counter task. |
|  | BeginReadMultiSamplePulseTicks | Begins an asynchronous read of one or more pulse samples in terms of ticks from a counter task. |
|  | BeginReadMultiSamplePulseTime | Begins an asynchronous read of one or more pulse samples in terms of time from a counter task. |
|  | BeginReadMultiSampleUInt32 | Begins an asynchronous read of one or more UInt32 samples from a counter task. |
|  | BeginReadSingleSampleDouble | Begins an asynchronous read of a Double sample from a counter task. |
|  | BeginReadSingleSampleInt32 | Begins an asynchronous read of a 32-bit integer sample from a counter task. |
|  | BeginReadSingleSamplePulseFrequency | Begins an asynchronous read of a single pulse sample in terms of frequency from a counter task. |
|  | BeginReadSingleSamplePulseTicks | Begins an asynchronous read of a single pulse sample in terms of ticks from a counter task. |
|  | BeginReadSingleSamplePulseTime | Begins an asynchronous read of a single pulse sample in terms of time from a counter task. |
|  | BeginReadSingleSampleUInt32 | Begins an asynchronous read of a UInt32 sample from a counter task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(Int32, AsyncCallback, Object, Double) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(Int32, AsyncCallback, Object, Int32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object, CIDataFrequency) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTicks(Int32, AsyncCallback, Object, CIDataTicks) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePulseTime | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTime(Int32, AsyncCallback, Object, CIDataTime) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(Int32, AsyncCallback, Object, UInt32) and retrieves the read samples. |
|  | EndReadMultiSampleDouble | Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseFrequency(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTicks(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePulseTime | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTime(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleDouble | Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseFrequency | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseFrequency(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseTicks | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTicks(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePulseTime | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTime(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleUInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, Int32) | Reads one or more Double samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleDouble(Int32, Double, ReallocationPolicy, Int32) | Reads one or more Double samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, Int32) | Reads one or more Int32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleInt32(Int32, Int32, ReallocationPolicy, Int32) | Reads one or more Int32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseFrequency(Int32, CIDataFrequency, Int32) | Reads one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseFrequency(Int32, CIDataFrequency, ReallocationPolicy, Int32) | Reads one or more CIDataFrequency samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTicks(Int32, CIDataTicks, Int32) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTicks(Int32, CIDataTicks, ReallocationPolicy, Int32) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTime(Int32, CIDataTime, Int32) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePulseTime(Int32, CIDataTime, ReallocationPolicy, Int32) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, Int32) | Reads one or more UInt32 samples from a single CIChannel in a task. |
|  | MemoryOptimizedReadMultiSampleUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more UInt32 samples from a single CIChannel in a task. |
|  | ReadMultiSampleDouble | Reads one or more Double samples from a counter task. |
|  | ReadMultiSampleInt32 | Reads one or more Int32 samples from a counter task. |
|  | ReadMultiSamplePulseFrequency | Reads one or more pulse samples in terms of frequency from a counter task. |
|  | ReadMultiSamplePulseTicks | Reads one or more pulse samples in terms of ticks from a counter task. |
|  | ReadMultiSamplePulseTime | Reads one or more pulse samples in terms of time from a counter task. |
|  | ReadMultiSampleUInt32 | Reads one or more UInt32 samples from a counter task. |
|  | ReadSingleSampleDouble | Reads a single Double sample from a counter task. |
|  | ReadSingleSampleInt32 | Reads a Int32 sample from a counter task. |
|  | ReadSingleSamplePulseFrequency | Reads a pulse sample in terms of frequency from a counter task. |
|  | ReadSingleSamplePulseTicks | Reads a pulse sample in terms of ticks from a counter task. |
|  | ReadSingleSamplePulseTime | Reads a pulse sample in terms of time from a counter task. |
|  | ReadSingleSampleUInt32 | Reads an UInt32 sample from a counter task. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countersinglechannelwriter.htm language=enus -->
## TOPIC 00538: CounterSingleChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countersinglechannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_countersinglechannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CounterSingleChannelWriter Class

### CounterSingleChannelWriter Class

Contains methods for writing samples to a single counter output channel in a counter output task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class CounterSingleChannelWriter : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class CounterSingleChannelWriter
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The CounterSingleChannelWriter type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | CounterSingleChannelWriter | Initializes a new instance of the CounterSingleChannelWriter class to write to the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteMultiSample(Boolean, CODataFrequency, AsyncCallback, Object) | Begins an asynchronous write of one or more frequency samples to a single COChannel in a counter output task. |
|  | BeginWriteMultiSample(Boolean, CODataTicks, AsyncCallback, Object) | Begins an asynchronous write of one or more ticks samples to a single COChannel in a counter output task. |
|  | BeginWriteMultiSample(Boolean, CODataTime, AsyncCallback, Object) | Begins an asynchronous write of one or more time samples to a single COChannel in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object) | Begins an asynchronous write of a frequency sample to a single COChannel in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTicks, AsyncCallback, Object) | Begins an asynchronous write of a ticks sample to a single COChannel in a counter output task. |
|  | BeginWriteSingleSample(Boolean, CODataTime, AsyncCallback, Object) | Begins an asynchronous write of a time sample to a single COChannel in a counter output task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndWrite | Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as BeginWriteSingleSample(Boolean, CODataFrequency, AsyncCallback, Object). |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteMultiSample(Boolean, CODataFrequency) | Writes one or more frequency samples to a single COChannel in a counter output task. |
|  | WriteMultiSample(Boolean, CODataTicks) | Writes one or more ticks samples to a single COChannel in a counter output task. |
|  | WriteMultiSample(Boolean, CODataTime) | Writes one or more time samples to a single COChannel in a counter output task. |
|  | WriteSingleSample(Boolean, CODataFrequency) | Writes a frequency sample to a single COChannel in a counter output task. |
|  | WriteSingleSample(Boolean, CODataTicks) | Writes a ticks sample to a single COChannel in a counter output task. |
|  | WriteSingleSample(Boolean, CODataTime) | Writes a time sample to a single COChannel in a counter output task. |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_couplingtypes.htm language=enus -->
## TOPIC 00539: CouplingTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_couplingtypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_couplingtypes.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

CouplingTypes Enumeration

### CouplingTypes Enumeration

Specifies a set of coupling types a device may support.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum CouplingTypes
```

```text
<FlagsAttribute>
Public Enumeration CouplingTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | No coupling types supported by the device. |
|  | AC | 1 | Remove the DC offset from the signal. |
|  | DC | 2 | Allow NI-DAQmx to measure all of the signal. |
|  | Ground | 4 | Remove the signal from the measurement and measure only ground. |

##### Remarks

Specifies a set of coupling types a device may support.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_daqbuffer.htm language=enus -->
## TOPIC 00540: DaqBuffer Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_daqbuffer.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_daqbuffer.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DaqBuffer Class

### DaqBuffer Class

buffer

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DaqBuffer : MarshalByRefObject, IFilteredTypeDescriptor
```

```text
Public Class DaqBuffer
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The DaqBuffer type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | InputBufferSize | Specifies the number of samples the input buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic input buffer allocation that NI-DAQmx performs. |
|  | InputOnBoardBufferSize | Indicates in samples per channel the size of the onboard input buffer of the device. |
|  | OutputBufferSize | Specifies the number of samples the output buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic output buffer allocation that NI-DAQmx performs. |
|  | OutputOnBoardBufferSize | Specifies in samples per channel the size of the onboard output buffer of the device. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dichannel.htm language=enus -->
## TOPIC 00541: DIChannel Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dichannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dichannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIChannel Class

### DIChannel Class

Encapsulates one or more digital input channels and the properties for a digital input channel.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DIChannel : Channel, IFilteredTypeDescriptor
```

```text
Public Class DIChannel
	Inherits Channel
	Implements IFilteredTypeDescriptor
```

The DIChannel type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AcquireOn | Specifies on which edge of the sample clock to acquire samples. |
|  | DataTransferMechanism | Specifies the data transfer mode for the device. |
|  | DataTransferRequestCondition | Specifies under what condition to transfer data from the onboard memory of the device to the buffer. |
|  | Description | Specifies a user-defined description for the channel. (Inherited from Channel.) |
|  | DigitalFilterEnable | Specifies whether to enable the digital filter for the line(s) or port(s). You can enable the filter on a line-by-line basis. You do not have to enable the filter for all lines in a channel. |
|  | DigitalFilterEnableBusMode | Specifies whether to enable bus mode for digital filtering. If you set this property to , NI-DAQmx treats all lines that use common filtering settings as a bus. If any line in the bus has jitter, all lines in the bus hold state until the entire bus stabilizes, or until 2 times the minimum pulse width elapses. If you set this property to , NI-DAQmx filters all lines individually. Jitter in one line does not affect other lines. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes as a valid high or low state transition. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the terminal of the signal to use as the timebase of the digital filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. |
|  | InvertLines | Specifies whether to invert the lines in the channel. If you set this property to , the lines are at high logic when off and at low logic when on. |
|  | IsGlobal | Indicates whether the channel is a global channel. (Inherited from Channel.) |
|  | LogicFamily | Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families. |
|  | MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
|  | NumberOfLines | Indicates the number of digital lines in the channel. |
|  | PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. (Inherited from Channel.) |
|  | SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. (Inherited from Channel.) |
|  | Tristate | Specifies whether to tristate the lines in the channel. If you set this property to , NI-DAQmx tristates the lines in the channel. If you set this property to , NI-DAQmx does not modify the configuration of the lines even if the lines were previously tristated. Set this property to to read lines in other tasks or to read output-only lines. |
|  | Type | Indicates the type of the virtual channel. (Inherited from Channel.) |
|  | UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
|  | UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
|  | VirtualName | Gets the name of the virtual channel. (Inherited from Channel.) |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Channel. (Inherited from Channel.) |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Channel or optionally releases only the unmanaged resources. (Inherited from Channel.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Inherited from Channel.) |

Top

##### Remarks

DIChannels

DIChannel

DIChannel

DIChannels

DIChannelCollection

DIChannel

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_didatatransfermechanism.htm language=enus -->
## TOPIC 00542: DIDataTransferMechanism Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_didatatransfermechanism.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_didatatransfermechanism.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIDataTransferMechanism Enumeration

### DIDataTransferMechanism Enumeration

Specifies the data transfer mode for the device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DIDataTransferMechanism
```

```text
Public Enumeration DIDataTransferMechanism
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Dma | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
|  | Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
|  | ProgrammedIO | 10264 | Data transfers take place when you call reading from the task or writing to the task. |
|  | UsbBulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

##### Remarks

DataTransferMechanism

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_didatatransferrequestcondition.htm language=enus -->
## TOPIC 00543: DIDataTransferRequestCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_didatatransferrequestcondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_didatatransferrequestcondition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DIDataTransferRequestCondition Enumeration

### DIDataTransferRequestCondition Enumeration

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DIDataTransferRequestCondition
```

```text
Public Enumeration DIDataTransferRequestCondition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | OnBoardMemoryMoreThanHalfFull | 10237 | Transfer data from the device when more than half of the onboard memory of the device fills. |
|  | OnBoardMemoryNotEmpty | 10241 | Transfer data from the device when there is data in the onboard memory. |
|  | OnBoardMemoryCustomThreshold | 12577 | Transfer data from the device when the number of samples specified with DataTransferCustomThreshold are in the device FIFO. |
|  | WhenAcquisitionComplete | 12546 | Transfer data when the acquisition is complete. |

##### Remarks

DataTransferRequestCondition

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventargs.htm language=enus -->
## TOPIC 00544: DigitalChangeDetectionEventArgs Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventargs.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalChangeDetectionEventArgs Class

### DigitalChangeDetectionEventArgs Class

DigitalChangeDetection

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class DigitalChangeDetectionEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class DigitalChangeDetectionEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The DigitalChangeDetectionEventArgs type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventhandler.htm language=enus -->
## TOPIC 00545: DigitalChangeDetectionEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalchangedetectioneventhandler.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalChangeDetectionEventHandler Delegate

### DigitalChangeDetectionEventHandler Delegate

DigitalChangeDetection

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void DigitalChangeDetectionEventHandler(
	Object sender,
	DigitalChangeDetectionEventArgs e
)
```

```text
Public Delegate Sub DigitalChangeDetectionEventHandler ( 
	sender As Object,
	e As DigitalChangeDetectionEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxDigitalChangeDetectionEventArgs A DigitalChangeDetectionEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetrigger.htm language=enus -->
## TOPIC 00546: DigitalEdgeAdvanceTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeAdvanceTrigger Class

### DigitalEdgeAdvanceTrigger Class

digital edge

advance triggers

AdvanceTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DigitalEdgeAdvanceTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class DigitalEdgeAdvanceTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The DigitalEdgeAdvanceTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalFilterEnable | Obsolete. (Deprecated) Specifies whether to apply the pulse width filter to the signal. |
|  | Edge | Obsolete. (Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list. |
|  | Source | Obsolete. (Deprecated) Specifies the name of a terminal where there is a digital signal to use as the source of the Advance Trigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetriggeredge.htm language=enus -->
## TOPIC 00547: DigitalEdgeAdvanceTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetriggeredge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgeadvancetriggeredge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeAdvanceTriggerEdge Enumeration

### DigitalEdgeAdvanceTriggerEdge Enumeration

**Note: This API is now obsolete.**

(Deprecated) Specifies on which edge of a digital signal to advance to the next entry in a scan list.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum DigitalEdgeAdvanceTriggerEdge
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration DigitalEdgeAdvanceTriggerEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

Edge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgearmstarttriggeredge.htm language=enus -->
## TOPIC 00548: DigitalEdgeArmStartTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgearmstarttriggeredge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgearmstarttriggeredge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeArmStartTriggerEdge Enumeration

### DigitalEdgeArmStartTriggerEdge Enumeration

Specifies on which edge of a digital signal to arm the task for a Start Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DigitalEdgeArmStartTriggerEdge
```

```text
Public Enumeration DigitalEdgeArmStartTriggerEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

Edge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgereferencetriggeredge.htm language=enus -->
## TOPIC 00549: DigitalEdgeReferenceTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgereferencetriggeredge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgereferencetriggeredge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeReferenceTriggerEdge Enumeration

### DigitalEdgeReferenceTriggerEdge Enumeration

Reference Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DigitalEdgeReferenceTriggerEdge
```

```text
Public Enumeration DigitalEdgeReferenceTriggerEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

Reference Trigger

Edge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgestarttrigger.htm language=enus -->
## TOPIC 00550: DigitalEdgeStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgestarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgestarttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeStartTrigger Class

### DigitalEdgeStartTrigger Class

digital edge

start triggers

StartTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DigitalEdgeStartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class DigitalEdgeStartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The DigitalEdgeStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | DigitalFilterEnable | Specifies whether to apply a digital filter to the trigger signal. |
|  | DigitalFilterMinimumPulseWidth | Specifies in seconds the minimum pulse width the filter recognizes. |
|  | DigitalFilterTimebaseRate | Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. |
|  | DigitalFilterTimebaseSource | Specifies the input terminal of the signal to use as the timebase of the pulse width filter. |
|  | DigitalSynchronizationEnable | Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. If you set this property to , the device does not recognize and act upon the trigger until the next pulse of the internal timebase. |
|  | Edge | Specifies on which edge of a digital pulse to start acquiring or generating samples. |
|  | Source | Specifies the name of a terminal where there is a digital signal to use as the source of the Start Trigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtriggeredge.htm language=enus -->
## TOPIC 00551: DigitalEdgeWatchdogExpirationTriggerEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtriggeredge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitaledgewatchdogexpirationtriggeredge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalEdgeWatchdogExpirationTriggerEdge Enumeration

### DigitalEdgeWatchdogExpirationTriggerEdge Enumeration

Specifies on which edge of a digital signal to expire the watchdog task.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DigitalEdgeWatchdogExpirationTriggerEdge
```

```text
Public Enumeration DigitalEdgeWatchdogExpirationTriggerEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

Edge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalpatternpausetriggercondition.htm language=enus -->
## TOPIC 00552: DigitalPatternPauseTriggerCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalpatternpausetriggercondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalpatternpausetriggercondition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalPatternPauseTriggerCondition Enumeration

### DigitalPatternPauseTriggerCondition Enumeration

Source

Pattern

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DigitalPatternPauseTriggerCondition
```

```text
Public Enumeration DigitalPatternPauseTriggerCondition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PatternMatches | 10254 | Trigger when the physical channels match the specified pattern. |
|  | PatternDoesNotMatch | 10253 | Trigger when the physical channels do not match the specified pattern. |

##### Remarks

Source

Pattern

Condition

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalsinglechannelreader.htm language=enus -->
## TOPIC 00553: DigitalSingleChannelReader Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalsinglechannelreader.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalsinglechannelreader.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelReader Class

### DigitalSingleChannelReader Class

Contains methods for reading samples from the digital input or output channel in a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DigitalSingleChannelReader : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class DigitalSingleChannelReader
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The DigitalSingleChannelReader type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | DigitalSingleChannelReader | Creates a new instance of the DigitalSingleChannelReader class to read from the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte, ReallocationPolicy) | Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32) | Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32, ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16, ReallocationPolicy) | Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32, ReallocationPolicy) | Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginMemoryOptimizedReadSingleSampleMultiLine | Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. |
|  | BeginReadMultiSamplePortByte | Begins an asynchronous read of one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginReadMultiSamplePortInt16 | Begins an asynchronous read of one or more 16-bit integer samples from a single DIChannel in a task. |
|  | BeginReadMultiSamplePortInt32 | Begins an asynchronous read of one or more 32-bit integer samples from a single DIChannel in a task. |
|  | BeginReadMultiSamplePortUInt16 | Begins an asynchronous read of one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginReadMultiSamplePortUInt32 | Begins an asynchronous read of one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
|  | BeginReadSingleSampleMultiLine | Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. |
|  | BeginReadSingleSamplePortByte | Begins an asynchronous read of a single 8-bit unsigned integer sample from a single DIChannel in a task. |
|  | BeginReadSingleSamplePortInt16 | Begins an asynchronous read of a single 16-bit integer sample from a single DIChannel in a task. |
|  | BeginReadSingleSamplePortInt32 | Begins an asynchronous read of a single 32-bit integer sample from a single DIChannel in a task. |
|  | BeginReadSingleSamplePortUInt16 | Begins an asynchronous read of a single 16-bit unsigned integer sample from a single DIChannel in a task. |
|  | BeginReadSingleSamplePortUInt32 | Begins an asynchronous read of a single 32-bit unsigned integer sample from a single DIChannel in a task. |
|  | BeginReadSingleSampleSingleLine | Begins an asynchronous read of a single Boolean sample from a single DIChannel in a task. The task can contain only a single digital line. |
|  | BeginReadWaveform(Int32, AsyncCallback, Object) | Begins an asynchronous read of one or more digital waveform samples from a single DIChannel in a task. |
|  | BeginReadWaveform(TimeSpan, AsyncCallback, Object) | Begins an asynchronous read of one or more digital waveform samples from a single DIChannel in a task for a specified duration. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndMemoryOptimizedReadMultiSamplePortByte | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortByte(Int32, AsyncCallback, Object, Byte) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePortInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortInt32(Int32, AsyncCallback, Object, Int32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePortUInt16 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt16(Int32, AsyncCallback, Object, UInt16) and retrieves the read samples. |
|  | EndMemoryOptimizedReadMultiSamplePortUInt32 | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePortUInt32(Int32, AsyncCallback, Object, UInt32) and retrieves the read samples. |
|  | EndMemoryOptimizedReadSingleSampleMultiLine | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadSingleSampleMultiLine(AsyncCallback, Object, Boolean) and retrieves the read samples. |
|  | EndReadMultiSamplePortByte | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortByte(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePortInt16 | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt16(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePortInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePortUInt16 | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt16(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadMultiSamplePortUInt32 | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePortUInt32(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleMultiLine | Handles the end of an asynchronous read initiated with BeginReadSingleSampleMultiLine(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortByte | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortByte(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortInt16 | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt16(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortUInt16 | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt16(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSamplePortUInt32 | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePortUInt32(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadSingleSampleSingleLine | Handles the end of an asynchronous read initiated with BeginReadSingleSampleSingleLine(AsyncCallback, Object) and retrieves the read samples. |
|  | EndReadWaveform | Handles the end of an asynchronous read initiated with BeginReadWaveform(Int32, AsyncCallback, Object) and retrieves the read samples. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | MemoryOptimizedReadMultiSamplePortByte(Int32, Byte, Int32) | Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePortByte(Int32, Byte, ReallocationPolicy, Int32) | Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePortInt32(Int32, Int32, Int32) | Reads one or more 32-bit integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePortInt32(Int32, Int32, ReallocationPolicy, Int32) | Reads one or more 32-bit integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt16(Int32, UInt16, Int32) | Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt16(Int32, UInt16, ReallocationPolicy, Int32) | Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt32(Int32, UInt32, Int32) | Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadMultiSamplePortUInt32(Int32, UInt32, ReallocationPolicy, Int32) | Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
|  | MemoryOptimizedReadSingleSampleMultiLine | Reads a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. |
|  | ReadMultiSamplePortByte | Reads one or more 8-bit unsigned integer samples from a single DIChannel in a task. |
|  | ReadMultiSamplePortInt16 | Reads one or more 16-bit integer samples from a single DIChannel in a task. |
|  | ReadMultiSamplePortInt32 | Reads one or more 32-bit integer samples from a single DIChannel in a task. |
|  | ReadMultiSamplePortUInt16 | Reads one or more 16-bit unsigned integer samples from a single DIChannel in a task. |
|  | ReadMultiSamplePortUInt32 | Reads one or more 32-bit unsigned integer samples from a single DIChannel in a task. |
|  | ReadSingleSampleMultiLine | Reads a single Boolean sample from a single DIChannel in a task. The channel can contain multiple digital lines. |
|  | ReadSingleSamplePortByte | Reads a single 8-bit unsigned integer sample from a single DIChannel in a task. |
|  | ReadSingleSamplePortInt16 | Reads a single 16-bit integer sample from a single DIChannel in a task. |
|  | ReadSingleSamplePortInt32 | Reads a single 32-bit integer sample from a single DIChannel in a task. |
|  | ReadSingleSamplePortUInt16 | Reads a single 16-bit unsigned integer sample from a single DIChannel in a task. |
|  | ReadSingleSamplePortUInt32 | Reads a single 32-bit unsigned integer sample from a single DIChannel in a task. |
|  | ReadSingleSampleSingleLine | Reads a single Boolean sample from a single DIChannel in a task. The task can contain only a single digital line. |
|  | ReadWaveform(Int32) | Reads one or more digital waveform samples from a single DIChannel in a task. |
|  | ReadWaveform(TimeSpan) | Reads one or more digital waveform samples from a single DIChannel in a task for a specified duration. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalsinglechannelwriter.htm language=enus -->
## TOPIC 00554: DigitalSingleChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalsinglechannelwriter.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_digitalsinglechannelwriter.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DigitalSingleChannelWriter Class

### DigitalSingleChannelWriter Class

Contains methods for writing samples to the digital output channel in a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DigitalSingleChannelWriter : MarshalByRefObject, 
	ISynchronizeCallbacks, ISupportSynchronizationContext
```

```text
Public Class DigitalSingleChannelWriter
	Inherits MarshalByRefObject
	Implements ISynchronizeCallbacks, ISupportSynchronizationContext
```

The DigitalSingleChannelWriter type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | DigitalSingleChannelWriter | Creates a new instance of the DigitalSingleChannelWriter class to write to the specified DaqStream. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | BeginWriteMultiSamplePort(Boolean, Byte, AsyncCallback, Object) | Begins an asynchronous write of one or more 8-bit unsigned integer samples to a single DOChannel in a task. |
|  | BeginWriteMultiSamplePort(Boolean, Int16, AsyncCallback, Object) | Begins an asynchronous write of one or more 32-bit integer samples to a single DOChannel in a task. |
|  | BeginWriteMultiSamplePort(Boolean, Int32, AsyncCallback, Object) | Begins an asynchronous write of one or more 32-bit integer samples to a single DOChannel in a task. |
|  | BeginWriteMultiSamplePort(Boolean, UInt16, AsyncCallback, Object) | Begins an asynchronous write of one or more 16-bit unsigned integer samples to a single DOChannel in a task. |
|  | BeginWriteMultiSamplePort(Boolean, UInt32, AsyncCallback, Object) | Begins an asynchronous write of one or more 32-bit unsigned integer samples to a single DOChannel in a task. |
|  | BeginWriteSingleSampleMultiLine | Begins an asynchronous write of a single Boolean sample to a single DOChannel in a task. The channel can contain multiple digital lines. |
|  | BeginWriteSingleSamplePort(Boolean, Byte, AsyncCallback, Object) | Begins an asynchronous write of a single 8-bit unsigned integer sample to a single DOChannel in a task. |
|  | BeginWriteSingleSamplePort(Boolean, Int16, AsyncCallback, Object) | Begins an asynchronous write of a single 16-bit integer sample to a single DOChannel in a task. |
|  | BeginWriteSingleSamplePort(Boolean, Int32, AsyncCallback, Object) | Begins an asynchronous write of a single 32-bit integer sample to a single DOChannel in a task. |
|  | BeginWriteSingleSamplePort(Boolean, UInt16, AsyncCallback, Object) | Begins an asynchronous write of a single 16-bit unsigned integer sample to a single DOChannel in a task. |
|  | BeginWriteSingleSamplePort(Boolean, UInt32, AsyncCallback, Object) | Begins an asynchronous write of a single 32-bit unsigned integer sample to a single DOChannel in a task. |
|  | BeginWriteSingleSampleSingleLine | Begins an asynchronous write of a single Boolean sample to a single digital line in a task. The task can contain only a single digital line. |
|  | BeginWriteWaveform | Begins an asynchronous write of one or more digital waveform samples to a single DOChannel in a task. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | EndWrite | Handles the end of an asynchronous write initiated with BeginWriteMultiSamplePort(Boolean, UInt32, AsyncCallback, Object), BeginWriteSingleSamplePort(Boolean, UInt32, AsyncCallback, Object), BeginWriteSingleSampleMultiLine(Boolean, Boolean, AsyncCallback, Object), BeginWriteSingleSampleSingleLine(Boolean, Boolean, AsyncCallback, Object), or BeginWriteWaveform(Boolean, DigitalWaveform, AsyncCallback, Object). |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteMultiSamplePort(Boolean, Byte) | Writes one or more 8-bit unsigned integer samples to a single DOChannel in a task. |
|  | WriteMultiSamplePort(Boolean, Int16) | Writes one or more 16-bit integer samples to a single DOChannel in a task. |
|  | WriteMultiSamplePort(Boolean, Int32) | Writes one or more 32-bit integer samples to a single DOChannel in a task. |
|  | WriteMultiSamplePort(Boolean, UInt16) | Writes one or more 16-bit unsigned integer samples to a single DOChannel in a task. |
|  | WriteMultiSamplePort(Boolean, UInt32) | Writes one or more 32-bit unsigned integer samples to a single DOChannel in a task. |
|  | WriteSingleSampleMultiLine | Writes a single Boolean sample to a single DOChannel in a task. The channel can contain multiple digital lines. |
|  | WriteSingleSamplePort(Boolean, Byte) | Writes a single 8-bit unsigned integer sample to a single DOChannel in a task. |
|  | WriteSingleSamplePort(Boolean, Int16) | Writes a single 16-bit integer sample to a single DOChannel in a task. |
|  | WriteSingleSamplePort(Boolean, Int32) | Writes a single 32-bit integer sample to a single DOChannel in a task. |
|  | WriteSingleSamplePort(Boolean, UInt16) | Writes a single 16-bit unsigned integer sample to a single DOChannel in a task. |
|  | WriteSingleSamplePort(Boolean, UInt32) | Writes a single 32-bit unsigned integer sample to a single DOChannel in a task. |
|  | WriteSingleSampleSingleLine | Writes a single Boolean sample to a single digital line in a task. The task can contain only a single digital line. |
|  | WriteWaveform | Writes one or more digital waveform samples to a single DOChannel in a task. |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dilogicfamily.htm language=enus -->
## TOPIC 00555: DILogicFamily Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dilogicfamily.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dilogicfamily.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DILogicFamily Enumeration

### DILogicFamily Enumeration

Specifies the logic family to use for acquisition. A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to the device documentation for information on the logic high and logic low voltages for these logic families.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum DILogicFamily
```

```text
Public Enumeration DILogicFamily
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TwoPointFiveVolts | 14620 | Compatible with 2.5 V CMOS signals. |
|  | ThreePointThreeVolts | 14621 | Compatible with LVTTL signals. |
|  | FiveVolts | 14619 | Compatible with TTL and 5 V CMOS signals. |

##### Remarks

LogicFamily

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dochannelcollection.htm language=enus -->
## TOPIC 00556: DOChannelCollection Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dochannelcollection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_dochannelcollection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

DOChannelCollection Class

### DOChannelCollection Class

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class DOChannelCollection : MarshalByRefObject, 
	ICollection
```

```text
Public Class DOChannelCollection
	Inherits MarshalByRefObject
	Implements ICollection
```

The DOChannelCollection type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | All | Gets a DOChannel that operates on all of the channels in the task. |
|  | Count | Gets the number of elements in the collection. |
|  | ItemInt64 | Gets the DOChannel at the specified index. In Visual C#, this property is the indexer. |
|  | ItemString | Gets the DOChannel with the specified virtual channel name. In Visual C#, this property is the indexer. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateChannel | Creates a DOChannel to generate digital signals. This method adds one or more channels to the DOChannelCollection. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetEnumerator | Returns an enumerator that you can use to iterate through the collection. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventhandler.htm language=enus -->
## TOPIC 00557: EveryNSamplesReadEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_everynsamplesreadeventhandler.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

EveryNSamplesReadEventHandler Delegate

### EveryNSamplesReadEventHandler Delegate

EveryNSamplesRead

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void EveryNSamplesReadEventHandler(
	Object sender,
	EveryNSamplesReadEventArgs e
)
```

```text
Public Delegate Sub EveryNSamplesReadEventHandler ( 
	sender As Object,
	e As EveryNSamplesReadEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxEveryNSamplesReadEventArgs An EveryNSamplesReadEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_everynsampleswritteneventargs.htm language=enus -->
## TOPIC 00558: EveryNSamplesWrittenEventArgs Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_everynsampleswritteneventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_everynsampleswritteneventargs.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

EveryNSamplesWrittenEventArgs Class

### EveryNSamplesWrittenEventArgs Class

EveryNSamplesWritten

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class EveryNSamplesWrittenEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class EveryNSamplesWrittenEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The EveryNSamplesWrittenEventArgs type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Error | Gets the Exception that occurred, if any. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CheckForException | Throws the Exception that occurred, if any exists. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_excitationidleoutputbehavior.htm language=enus -->
## TOPIC 00559: ExcitationIdleOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_excitationidleoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_excitationidleoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExcitationIdleOutputBehavior Enumeration

### ExcitationIdleOutputBehavior Enumeration

Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ExcitationIdleOutputBehavior
```

```text
Public Enumeration ExcitationIdleOutputBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ZeroVoltsOrAmps | 12526 | Drive excitation output to zero. |
|  | MaintainExistingValue | 12528 | Continue generating the current value. |

##### Remarks

ExcitationIdleOutputBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_exportsignal.htm language=enus -->
## TOPIC 00560: ExportSignal Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_exportsignal.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_exportsignal.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExportSignal Enumeration

### ExportSignal Enumeration

Specifies the name of the trigger, clock, or event to export.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ExportSignal
```

```text
Public Enumeration ExportSignal
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AIConvertClock | 12484 | Clock that causes an analog-to-digital conversion on an E Series device. One conversion corresponds to a single sample from one channel. |
|  | Timebase20MHz | 12486 | Output of an oscillator that is the onboard source of the Master Timebase. Other timebases are derived from this clock. |
|  | SampleClock | 12487 | Clock the device uses to time each sample. |
|  | AdvanceTrigger | 12488 | Trigger that moves a switch to the next entry in a scan list. |
|  | ReferenceTrigger | 12490 | Trigger that establishes the reference point between pretrigger and posttrigger samples. |
|  | StartTrigger | 12491 | Trigger that begins a measurement or generation. |
|  | AdvanceCompleteEvent | 12492 | Signal a switch product generates after it both executes the command(s) in a scan list entry and waits for the settling time to elapse. |
|  | AIHoldCompleteEvent | 12493 | Signal an E Series device generates when the device latches analog input data (the ADC enters "hold" mode) and it is safe for any external switching hardware to remove the signal and replace it with the next signal. This event does not indicate the completion of the actual analog-to-digital conversion. |
|  | CounterOutputEvent | 12494 | Signal a counter generates. Each time the counter reaches terminal count, this signal toggles or pulses. |
|  | ChangeDetectionEvent | 12511 | The signal that a static DIO device generates when the device detects a rising or falling edge on any of the lines or ports you selected when you configured change detection timing. |
|  | WatchdogExpiredEvent | 12512 | The signal that a static DIO device generates when the watchdog timer expires. |
|  | ReferenceClock10MHz | 12536 | Output of an oscillator that you can use to synchronize multiple devices. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_externalcalibrationsession.htm language=enus -->
## TOPIC 00561: ExternalCalibrationSession Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_externalcalibrationsession.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_externalcalibrationsession.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ExternalCalibrationSession Class

### ExternalCalibrationSession Class

external calibration

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class ExternalCalibrationSession : MarshalByRefObject, 
	IDisposable
```

```text
Public Class ExternalCalibrationSession
	Inherits MarshalByRefObject
	Implements IDisposable
```

The ExternalCalibrationSession type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Adjust1102 | Adjusts the external calibration constants for an SCXI-1102 module. |
|  | Adjust1104 | Adjusts the external calibration constants for an SCXI-1104 module. |
|  | Adjust1112 | Adjusts the external calibration constants for an SCXI-1112 module. |
|  | Adjust1122 | Adjusts the external calibration constants for an SCXI-1122 module. |
|  | Adjust1124 | Adjusts the external calibration constants for an SCXI-1124 module. |
|  | Adjust1125 | Adjusts the external calibration constants for an SCXI-1125 module. |
|  | Adjust1126 | Adjusts the external calibration constants for an SCXI-1126 module. |
|  | Adjust1141 | Adjusts the external calibration constants for an SCXI-1141 module. |
|  | Adjust1142 | Adjusts the external calibration constants for an SCXI-1142 module. |
|  | Adjust1143 | Adjusts the external calibration constants for an SCXI-1143 module. |
|  | Adjust11601 | Adjusts theexternal calibrationconstants for an NI FD-11601 device bank. |
|  | Adjust11603 | Adjusts theexternal calibrationconstants for an NI FD-11603 device bank. |
|  | Adjust11605 | Adjusts theexternal calibrationconstants for an NI FD-11605 device bank. |
|  | Adjust11613 | Adjusts theexternal calibrationconstants for an NI FD-11613 device bank. |
|  | Adjust11614 | Adjusts theexternal calibrationconstants for an NI FD-11614 device bank. |
|  | Adjust11634 | Adjusts theexternal calibrationconstants for an NI FD-11634 device bank. |
|  | Adjust11637 | Adjusts theexternal calibrationconstants for an NI FD-11637 device bank. |
|  | Adjust1502 | Adjusts the external calibration constants for an SCXI-1502 module. |
|  | Adjust1503 | Adjusts the external calibration constants for an SCXI-1503 module. |
|  | Adjust1503Current | Adjusts the external calibration constants for an SCXI-1503 module. |
|  | Adjust1520 | Adjusts the external calibration constants for an SCXI-1520 module. |
|  | Adjust1521 | Adjusts the external calibration constants for an SCXI-1521 module. |
|  | Adjust153x | Adjusts the external calibration constants for an SCXI-1530 or SCXI-1531 module. |
|  | Adjust1540 | Adjusts the external calibration constants for an SCXI-1540 module. |
|  | Adjust4204 | Adjusts the external calibration constants for an NI 4204 device. |
|  | Adjust4220 | Adjusts the external calibration constants for an NI 4220 device. |
|  | Adjust4224 | Adjusts the external calibration constants for an NI 4224 device. |
|  | Adjust4225 | Obsolete. The Adjust4225(String, Double, Double) method has been deprecated. Adjusts the external calibration constants for an NI 4225 device. |
|  | Adjust4300 | Adjusts the external calibration constants on an NI 4300 device. |
|  | Adjust4302 | Adjusts the external calibration constants for an NI 4302. Connect a known voltage to the device and specify that voltage with referenceVoltage. |
|  | Adjust4303 | Adjusts the external calibration constants for an NI 4303. Connect a known voltage to the device and specify that voltage with referenceVoltage. |
|  | Adjust4304 | Adjusts the external calibration constants for an NI 4304. Connect a known voltage to the device and specify that voltage with referenceVoltage. |
|  | Adjust4305 | Adjusts the external calibration constants for an NI 4305. Connect a known voltage to the device and specify that voltage with referenceVoltage. |
|  | Adjust4309 | Adjusts the calibration constants for a PXIe-4309 device. |
|  | Adjust4310 | Adjusts the calibration constants for a PXIe-4310 device. |
|  | Adjust4322 | Adjusts the external calibration constants on an NI 4322 device. |
|  | Adjust4339 | Adjusts the external calibration constants for an NI PXIe 4339 device. |
|  | Adjust433x | Adjusts the external calibration constants on an NI PXIe-433x device. |
|  | Adjust4353 | Adjusts the external calibration constants on an NI 4353 device. |
|  | Adjust4357 | Adjusts the external calibration constants for an NI 4357 device. |
|  | Adjust9201 | Adjusts the external calibration constants for an NI 9201 device. |
|  | Adjust9202 | Adjusts the external calibration constants for an NI 9202 device. |
|  | Adjust9203Gain | Adjusts the external calibration gain constants for an NI 9203 device. |
|  | Adjust9203Offset | Adjusts the external calibration offset constants for an NI 9203 device. |
|  | Adjust9205 | Adjusts the external calibration constants for an NI 9205 device. |
|  | Adjust9206 | Adjusts the external calibration constants for an NI 9206 device. |
|  | Adjust9207Gain | Adjusts the external calibration gain constants for an NI 9207 device. |
|  | Adjust9207Offset | Adjusts the external calibration offset constants for an NI 9207 device. |
|  | Adjust9208Gain | Adjusts the external calibration gain constants for an NI 9208 device. |
|  | Adjust9208Offset | Adjusts the external calibration offset constants for an NI 9208 device. |
|  | Adjust9209Gain | Adjusts the external calibration gain constants for an NI 9209 device. |
|  | Adjust9209Offset | Adjusts the external calibration offset constants for an NI 9209 device. |
|  | Adjust9210 | Adjusts the external calibration constants for an NI 9210 device. |
|  | Adjust9211 | Adjusts the external calibration constants for an NI 9211 device. |
|  | Adjust9212 | Adjusts the external calibration constants for an NI 9212 device. |
|  | Adjust9213 | Adjusts the external calibration constants for an NI 9213 device. |
|  | Adjust9214 | Adjusts the external calibration constants for an NI 9214 device. |
|  | Adjust9215 | Adjusts the external calibration constants for an NI 9215 device. |
|  | Adjust9216 | Adjusts the external calibration constants for an NI 9216 device. |
|  | Adjust9217 | Adjusts the external calibration constants for an NI 9217 device. |
|  | Adjust9218 | Adjusts the external calibration constants for an NI 9218 device. |
|  | Adjust9219 | Adjusts the external calibration constants for an NI 9219 device. |
|  | Adjust9220 | Adjusts the external calibration constants for an NI 9220 device. |
|  | Adjust9221 | Adjusts the external calibration constants for an NI 9221 device. |
|  | Adjust9222 | Adjusts the external calibration constants for an NI 9222 device. |
|  | Adjust9223 | Adjusts the external calibration constants for an NI 9223 device. |
|  | Adjust9224 | Adjusts the external calibration constants for an NI 9224 device. |
|  | Adjust9225 | Adjusts the external calibration constants for an NI 9225 device. |
|  | Adjust9226 | Adjusts the external calibration constants for an NI 9226 device. |
|  | Adjust9227 | Adjusts the external calibration constants for an NI 9227 device. |
|  | Adjust9228 | Adjusts the external calibration constants for an NI 9228 device. |
|  | Adjust9229 | Adjusts the external calibration constants for an NI 9229 device. |
|  | Adjust9230 | Adjusts the external calibration constants for an NI 9230 device. |
|  | Adjust9231 | Adjusts the external calibration constants for an NI 9231 device. |
|  | Adjust9232 | Adjusts the external calibration constants for an NI 9232 device. |
|  | Adjust9234Gain | Adjusts the external calibration gain constants for an NI 9234 device. |
|  | Adjust9234Offset | Adjusts the external calibration offset constants for an NI 9234 device. |
|  | Adjust9238 | Adjusts the external calibration constants for an NI 9238 device. |
|  | Adjust9239 | Adjusts the external calibration constants for an NI 9239 device. |
|  | Adjust9242 | Adjusts the external calibration constants for an NI 9242 device. |
|  | Adjust9244 | Adjusts the external calibration constants for an NI 9244 device. |
|  | Adjust9246 | Adjusts the external calibration constants for an NI 9246 device. |
|  | Adjust9247 | Adjusts the external calibration constants for an NI 9247 device. |
|  | Adjust9250 | Adjusts the external calibration constants for an NI 9250 device. |
|  | Adjust9251 | Adjusts the external calibration constants for an NI 9251 device. |
|  | Adjust9252 | Adjusts the external calibration constants for an NI 9252 device. |
|  | Adjust9253 | Adjusts the external calibration constants for an NI 9253 device. |
|  | Adjust9260 | Adjusts the external calibration constants for an NI 9260 device. |
|  | Adjust9262 | Adjusts the external calibration constants for an NI 9262 device. |
|  | Adjust9263 | Adjusts the external calibration constants for an NI 9263 device. |
|  | Adjust9264 | Adjusts the external calibration constants for an NI 9264 device. |
|  | Adjust9265 | Adjusts the external calibration constants for an NI 9265 device. |
|  | Adjust9266 | Adjusts the external calibration constants for an NI 9266 device. |
|  | Adjust9269 | Adjusts the external calibration constants for an NI 9269 device. |
|  | Adjust9775 | Adjusts the external calibration constants for an NI 9775 device. |
|  | AdjustAOSeries | Adjusts the external calibration constants on an AO Series device. |
|  | AdjustDsa4463 | Adjusts the external calibration constants for the analog output section of a NI 4463 device. |
|  | AdjustDsa4610 | Adjusts the external calibration gain constants for an NI 4610. |
|  | AdjustDsaAI(Double) | Adjusts the external calibration constants for the analog input section of a DSA device without shorting the input terminals. |
|  | AdjustDsaAI(Double, Boolean) | Adjusts the external calibration constants for the analog input section of a DSA device. You can specify whether you want to short the input terminals or not. |
|  | AdjustDsaAI(AICoupling, Double, Double) | Performs external calibration adjustment on a DSA device with the specified gain and coupling configuration. |
|  | AdjustDsaAO | Adjusts the external calibration constants for the analog output section of a DSA device. |
|  | AdjustDsaAOTimebase | Adjusts the external calibration constants for the timebase of a DSA device with an adjustible oscillator. |
|  | AdjustDsaTimebase | Adjusts the external calibration constants for the timebase of a DSA device with an adjustible oscillator. |
|  | AdjustESeries | Adjusts the external calibration constants on an E Series device. |
|  | AdjustMSeries | Adjusts the external calibration constants for an M Series device. |
|  | AdjustSCBaseboard | Adjusts the external calibration constants for the baseboard of an SC Series device. |
|  | AdjustSSeries | Adjusts the external calibration constants for an S Series device. |
|  | AdjustTioTimebase | Adjusts the external calibration constants for the timebase of a TIO device. |
|  | AdjustXSeries | Adjusts the external calibration constants for an X Series device. |
|  | ConnectSCExpressCalibrationAccessoryChannels | Configures a connection on the SC Express accessory for the specified physical channel(s). |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | CSeriesSetCalibrationTemperature | Specifies the temperature of a C Series device for the current external calibration session. |
|  | DisconnectSCExpressCalibrationAccessoryChannels | Disconnects the configured connection on an SC Express accessory and connects the accessory in the default configuration. |
|  | Dispose | Releases all resources used by ExternalCalibrationSession. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by ExternalCalibrationSession or optionally releases only the unmanaged resources. |
|  | DsaSetCalibrationTemperature | Specifies the temperature of a DSA device for the current external calibration session. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | FieldDAQSetCalibrationTemperature | Specifies the temperature of a FieldDAQ device for the current external calibration session. |
|  | Get11601AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11603AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11605AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11613AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11614AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get11634AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4302AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4303AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4304AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4305AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get4322AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get4339AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9201AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9202AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9203AdjustmentPoints | Returns the reference current values to be used by a reference device to create a reference signal. |
|  | Get9207AdjustmentPoints | Returns the reference voltage or current values to be used by a reference device to create a reference signal. |
|  | Get9208AdjustmentPoints | Returns the reference current values to be used by a reference device to create a reference signal. |
|  | Get9209AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9212AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9213AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9214AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9215AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9216AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9217AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9218AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9219AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9220AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9221AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9222AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9223AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9224AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9225AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9226AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9227AdjustmentPoints | Returns the reference current values to be used by a reference device to create a reference signal. |
|  | Get9228AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9229AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9230AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9231AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9232AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9234AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9238AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9239AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9242AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9244AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9246AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9247AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9250AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9251AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9252AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9253AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | Get9260AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | Get9262AdjustmentPoints | Returns the reference voltage values to be measured by a reference device. |
|  | Get9263AdjustmentPoints | Returns the reference voltage values to be measured by a reference device. |
|  | Get9264AdjustmentPoints | Returns the reference voltage values to be measured by a reference device. |
|  | Get9265AdjustmentPoints | Returns the reference current values to be measured by a reference device. |
|  | Get9266AdjustmentPoints | Returns the reference current values to be measured by a reference device. |
|  | Get9269AdjustmentPoints | Returns the reference voltage values to be measured by a reference device. |
|  | Get9775AdjustmentPoints | Returns the reference values to be used by a reference device to create a reference signal. |
|  | GetDsa4463AdjustmentPoints | Returns the reference voltage values to be used by a reference device to create a reference signal. |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | SaveChangesAndDispose | Closes an open external calibration session and saves the calibration changes made in the session. |
|  | SetSCExpressCalibrationAccessoryBridgeOutput | Configures an SC Express accessory to produce the bridge output specified in volts-per-volt. |
|  | Setup1102 | Configures the calibration task for an SCXI-1102 module. |
|  | Setup1104 | Configures the calibration task for an SCXI-1104 module. |
|  | Setup1112 | Configures the calibration task for an SCXI-1112 module. |
|  | Setup1122 | Configures the calibration task for an SCXI-1122 module. |
|  | Setup1124(String, Scxi1124Range, Int64) | Configures the calibration task for an SCXI-1124 module. |
|  | Setup1124(String, Scxi1124Range, UInt32) | Configures the calibration task for an SCXI-1124 module. |
|  | Setup1125 | Configures the calibration task for an SCXI-1125 module. |
|  | Setup1126 | Configures the channel and range for an SCXI-1126 module calibration task. |
|  | Setup1141 | Configures the gain value for an SCXI-1141 module calibration task. |
|  | Setup1142 | Configures the gain value for an SCXI-1142 module calibration task. |
|  | Setup1143 | Configures the gain value for an SCXI-1143 module calibration task. |
|  | Setup11605 | Sets up external calibration for an FD 11605 device. |
|  | Setup11634 | Sets up external calibration for an FD 11634 device. |
|  | Setup11637 | Sets up external calibration for an FD 11637 device. |
|  | Setup1502 | Configures the calibration task for an SCXI-1502 module. |
|  | Setup1503 | Configures the calibration task for an SCXI-1503 module. |
|  | Setup1520 | Configures the calibration task for an SCXI-1520 module. |
|  | Setup1521 | Configures the calibration task for an SCXI-1521 module. |
|  | Setup153x | Configures the gain value for an SCXI-1530 or SCXI-1531 module calibration task. |
|  | Setup1540 | Configures the gain value for an SCXI-1540 module calibration task. |
|  | Setup4302 | Initializes an NI PXIe-4302 device with the specified range for calibration. |
|  | Setup4303 | Initializes an NI PXIe-4303 device with the specified range for calibration. |
|  | Setup4304 | Initializes an NI PXIe-4304 device with the specified range for calibration. |
|  | Setup4305 | Initializes an NI PXIe-4305 device with the specified range for calibration. |
|  | Setup4322 | Configures the calibration task for an NI 4322 device. |
|  | Setup4339 | Initializes an NI PXIe 4339 device with the specified mode, range, and exitation for calibration. |
|  | Setup433x | Configures the calibration task for an NI PXIe-433x device. |
|  | Setup9218 | Sets up external calibration for an NI 9218 device. |
|  | Setup9219 | Sets up external calibration for an NI 9219 device. |
|  | Setup9242 | Reads the specified value from the ADC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9242AdjustmentPoints. |
|  | Setup9244 | Reads the specified value from the ADC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9244AdjustmentPoints. |
|  | Setup9260 | Writes the specified binary value to the DAC on the specified physical channel. This modules requires a sweep of DAC values obtained from the Get9260AdjustmentPoints. |
|  | Setup9262 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9262AdjustmentPoints. |
|  | Setup9263 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9263AdjustmentPoints. |
|  | Setup9264 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9264AdjustmentPoints. |
|  | Setup9265 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9265AdjustmentPoints. |
|  | Setup9266 | Applies the specified DAC value to the AO channels, such that it can then be measured by a DMM |
|  | Setup9269 | Writes the specified binary value to the DAC on the specified physical channel. This method requires a sweep of DAC values obtained from Get9269AdjustmentPoints. |
|  | SetupDsa4463 | Generates a specified voltage from the DSA device. |
|  | SetupDsa4480 | Generates a specified voltage from the DSA device. |
|  | SetupDsaAOTimebase | Generates a sine wave of a fixed frequency from the DSA device. You must measure the frequency of the generated sine wave and pass that value into AdjustDsaAOTimebase(Double, Boolean). |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Remarks

StartExternalCalibration(String)

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_filterresponse.htm language=enus -->
## TOPIC 00562: FilterResponse Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_filterresponse.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_filterresponse.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

FilterResponse Enumeration

### FilterResponse Enumeration

Specifies the digital filter response.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum FilterResponse
```

```text
Public Enumeration FilterResponse
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ConstantGroupDelay | 16075 | Constant group delay filter response. |
|  | Butterworth | 16076 | Butterworth filter response. |
|  | Elliptical | 16077 | Elliptical filter response. |
|  | HardwareDefined | 10191 | Use the hardware-defined filter response. |

##### Remarks

DigitalFilterResponse

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_filtertype.htm language=enus -->
## TOPIC 00563: FilterType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_filtertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_filtertype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

FilterType Enumeration

### FilterType Enumeration

Specifies the digital filter type.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum FilterType
```

```text
Public Enumeration FilterType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Lowpass | 16071 | Lowpass filter. |
|  | Highpass | 16072 | Highpass filter. |
|  | Bandpass | 16073 | Bandpass filter. |
|  | Notch | 16074 | Notch filter. |
|  | Custom | 10137 | Custom filter. |

##### Remarks

DigitalFilterType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_firstsampleclocktimescale.htm language=enus -->
## TOPIC 00564: FirstSampleClockTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_firstsampleclocktimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_firstsampleclocktimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

FirstSampleClockTimescale Enumeration

### FirstSampleClockTimescale Enumeration

FirstSampleClockTime

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum FirstSampleClockTimescale
```

```text
Public Enumeration FirstSampleClockTimescale
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HostTime | 16126 | Use the host device. |
|  | IODeviceTime | 16127 | Use the I/O device. |

##### Remarks

FirstSampleClockTime

FirstSampleClockTimescale

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_firstsampletimestamptimescale.htm language=enus -->
## TOPIC 00565: FirstSampleTimestampTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_firstsampletimestamptimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_firstsampletimestamptimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

FirstSampleTimestampTimescale Enumeration

### FirstSampleTimestampTimescale Enumeration

Specifies the timescale to be used for the first sample timestamp.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum FirstSampleTimestampTimescale
```

```text
Public Enumeration FirstSampleTimestampTimescale
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HostTime | 16126 | Use the host device. |
|  | IODeviceTime | 16127 | Use the I/O device. |

##### Remarks

FirstSampleTimestampTimescale

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventinterlockedassertedlevel.htm language=enus -->
## TOPIC 00566: HandshakeEventInterlockedAssertedLevel Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventinterlockedassertedlevel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventinterlockedassertedlevel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeEventInterlockedAssertedLevel Enumeration

### HandshakeEventInterlockedAssertedLevel Enumeration

HandshakeEventOutputBehavior

Interlocked

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum HandshakeEventInterlockedAssertedLevel
```

```text
Public Enumeration HandshakeEventInterlockedAssertedLevel
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | High | 10192 | High state. |
|  | Low | 10214 | Low state. |

##### Remarks

HandshakeEventOutputBehavior

Interlocked

HandshakeEventInterlockedAssertedLevel

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventoutputbehavior.htm language=enus -->
## TOPIC 00567: HandshakeEventOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeEventOutputBehavior Enumeration

### HandshakeEventOutputBehavior Enumeration

Specifies the output behavior of the Handshake Event.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum HandshakeEventOutputBehavior
```

```text
Public Enumeration HandshakeEventOutputBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Interlocked | 12549 | Handshake Event deasserts after the Handshake Trigger asserts, plus the amount of time specified with HandshakeEventInterlockedDeassertDelay. |
|  | Pulse | 10265 | Handshake Event pulses with the pulse width specified in HandshakeEventPulseWidth. |

##### Remarks

HandshakeEventOutputBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventpulsepolarity.htm language=enus -->
## TOPIC 00568: HandshakeEventPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakeeventpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeEventPulsePolarity Enumeration

### HandshakeEventPulsePolarity Enumeration

HandshakeEventOutputBehavior

Pulse

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum HandshakeEventPulsePolarity
```

```text
Public Enumeration HandshakeEventPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

HandshakeEventOutputBehavior

Pulse

HandshakeEventPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakesampleinputdatacondition.htm language=enus -->
## TOPIC 00569: HandshakeSampleInputDataCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakesampleinputdatacondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakesampleinputdatacondition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeSampleInputDataCondition Enumeration

### HandshakeSampleInputDataCondition Enumeration

Specifies on which edge of the Handshake Trigger an input task latches the data from the peripheral device.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum HandshakeSampleInputDataCondition
```

```text
Public Enumeration HandshakeSampleInputDataCondition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HandshakeTriggerAsserts | 12552 | Latch data when the Handshake Trigger asserts. |
|  | HandshakeTriggerDeasserts | 12553 | Latch data when the Handshake Trigger deasserts. |

##### Remarks

HandshakeSampleInputDataCondition

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakestartcondition.htm language=enus -->
## TOPIC 00570: HandshakeStartCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakestartcondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshakestartcondition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeStartCondition Enumeration

### HandshakeStartCondition Enumeration

Specifies the point in the handshake cycle that the device is in when the task starts.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum HandshakeStartCondition
```

```text
Public Enumeration HandshakeStartCondition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Immediate | 10198 | Device is waiting for space in the FIFO (for acquisition) or waiting for samples (for generation). |
|  | WaitForHandshakeTriggerAssert | 12550 | Device is waiting for the Handshake Trigger to assert. |
|  | WaitForHandshakeTriggerDeassert | 12551 | Device is waiting for the Handshake Trigger to deassert. |

##### Remarks

HandshakeStartCondition

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshaketrigger.htm language=enus -->
## TOPIC 00571: HandshakeTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshaketrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_handshaketrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

HandshakeTrigger Class

### HandshakeTrigger Class

handshake trigger signals on a task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class HandshakeTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class HandshakeTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The HandshakeTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Interlocked | Gets the InterlockedHandshakeTrigger. |
|  | Type | Specifies the type of Handshake Trigger to use. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureInterlockedTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal reaches the level you specify; and the device acquires all post-trigger samples. |
|  | ConfigureNone | Disables handshake triggering for the measurement. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ifilteredtypedescriptor.htm language=enus -->
## TOPIC 00572: IFilteredTypeDescriptor Interface

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ifilteredtypedescriptor.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_ifilteredtypedescriptor.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

IFilteredTypeDescriptor Interface

### IFilteredTypeDescriptor Interface

Task

ICustomTypeDescriptor

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public interface IFilteredTypeDescriptor
```

```text
Public Interface IFilteredTypeDescriptor
```

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | GetFilteredTypeDescriptor(PropertyFilterType) | Returns a list of filtered properties that belong to the Task subobject, according to the specified filtering type. |
|  | GetFilteredTypeDescriptor(PropertyFilterType, PropertyFilterFlags) | Returns a list of filtered properties that belong to the Task subobject, according to the specified filtering type and filter flags. |

Top

##### Remarks

The following [Task](t_nationalinstruments_daqmx_task.htm) subobjects currently implement this interface:

- AdvanceTrigger
- AIChannel
- AnalogEdgeReferenceTrigger
- AnalogEdgeStartTrigger
- AnalogLevelPauseTrigger
- AnalogWindowPauseTrigger
- AnalogWindowReferenceTrigger
- AnalogWindowStartTrigger
- AOChannel
- ArmStartTrigger
- CIChannel
- COChannel
- DaqBuffer
- DaqStream
- DIChannel
- DigitalEdgeAdvanceTrigger
- DigitalEdgeArmStartTrigger
- DigitalEdgeReferenceTrigger
- DigitalEdgeStartTrigger
- DigitalEdgeWatchdogExpirationTrigger
- DigitalLevelPauseTrigger
- DigitalPatternReferenceTrigger
- DigitalPatternStartTrigger
- DOChannel
- ExportSignals
- HandshakeTrigger
- InterlockedHandshakeTrigger
- PauseTrigger
- ReferenceTrigger
- SinglePoint
- StartTrigger
- SwitchScan
- Timing
- Watchdog
- WatchdogExpirationTrigger

Visit the DAQmx Professional Developer Tools Web site for more information and examples of programmatically determining device capabilities.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_implicitunderflowbehavior.htm language=enus -->
## TOPIC 00573: ImplicitUnderflowBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_implicitunderflowbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_implicitunderflowbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ImplicitUnderflowBehavior Enumeration

### ImplicitUnderflowBehavior Enumeration

Specifies the action to take when the onboard memory of the device becomes empty.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ImplicitUnderflowBehavior
```

```text
Public Enumeration ImplicitUnderflowBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HaltOutputAndError | 14615 | Stop generating samples and return an error. |
|  | PauseUntilDataAvailable | 14616 | Pause the task until samples are available in the FIFO. |

##### Remarks

ImplicitUnderflowBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_inputcalibrationsource.htm language=enus -->
## TOPIC 00574: InputCalibrationSource Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_inputcalibrationsource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_inputcalibrationsource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

InputCalibrationSource Enumeration

### InputCalibrationSource Enumeration

Specifies the input source selection.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum InputCalibrationSource
```

```text
Public Enumeration InputCalibrationSource
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Loopback | 0 | Loopback the internal excitation voltage with 0 degree phase shift. |
|  | CrossoverLoopback | 1 | Loopback the internal excitation voltage with 180 degree phase shift. |
|  | Ground | 2 | Connect the channel to ground. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_interlockedhandshaketrigger.htm language=enus -->
## TOPIC 00575: InterlockedHandshakeTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_interlockedhandshaketrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_interlockedhandshaketrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

InterlockedHandshakeTrigger Class

### InterlockedHandshakeTrigger Class

HandshakeTrigger

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class InterlockedHandshakeTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class InterlockedHandshakeTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The InterlockedHandshakeTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AssertedLevel | Specifies the asserted level of the Handshake Trigger. |
|  | Source | Specifies the source terminal of the Handshake Trigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_interlockedhandshaketriggerassertedlevel.htm language=enus -->
## TOPIC 00576: InterlockedHandshakeTriggerAssertedLevel Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_interlockedhandshaketriggerassertedlevel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_interlockedhandshaketriggerassertedlevel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

InterlockedHandshakeTriggerAssertedLevel Enumeration

### InterlockedHandshakeTriggerAssertedLevel Enumeration

Handshake Trigger

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum InterlockedHandshakeTriggerAssertedLevel
```

```text
Public Enumeration InterlockedHandshakeTriggerAssertedLevel
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | High | 10192 | High state. |
|  | Low | 10214 | Low state. |

##### Remarks

Handshake Trigger

AssertedLevel

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_linearscale.htm language=enus -->
## TOPIC 00577: LinearScale Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_linearscale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_linearscale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

LinearScale Class

### LinearScale Class

custom scale

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class LinearScale : Scale
```

```text
Public Class LinearScale
	Inherits Scale
```

The LinearScale type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | LinearScale | Initializes a new instance of the LinearScale class that scales values using the equation y = mx + b, where x is the prescaled value, and y is the scaled value. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Specifies a description for the scale. (Inherited from Scale.) |
|  | Name | Gets the name of the scale. (Inherited from Scale.) |
|  | PreScaledUnits | Specifies the units of the values that you want to scale. (Inherited from Scale.) |
|  | ScaledUnits | Specifies the units to use for scaled values. You can use an arbitrary string. (Inherited from Scale.) |
|  | Slope | Specifies the slope, m, in the equation y=mx+b. |
|  | Type | Gets the type of scale. (Inherited from Scale.) |
|  | YIntercept | Specifies the y-intercept, b, in the equation y=mx+b. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Scale. (Inherited from Scale.) |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Scale or optionally releases only the unmanaged resources. (Inherited from Scale.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Inherited from Scale.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_loggingmode.htm language=enus -->
## TOPIC 00578: LoggingMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_loggingmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_loggingmode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

LoggingMode Enumeration

### LoggingMode Enumeration

logging

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum LoggingMode
```

```text
Public Enumeration LoggingMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Off | 10231 | Disable logging for the task. |
|  | Log | 15844 | Enable logging for the task. You cannot read data using reading from the task when using this mode. If you require access to the data, read from the TDMS file. |
|  | LogAndRead | 15842 | Enable both logging and reading data for the task. You must use reading from the task to read samples for NI-DAQmx to stream them to disk. |

##### Remarks

logging

LoggingMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_logicfamily.htm language=enus -->
## TOPIC 00579: LogicFamily Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_logicfamily.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_logicfamily.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

LogicFamily Enumeration

### LogicFamily Enumeration

Specifies the logic family to use for generation and acquisition.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum LogicFamily
```

```text
Public Enumeration LogicFamily
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | TwoPointFiveVolts | 14620 | Compatible with CMOS signals. |
|  | ThreePointThreeVolts | 14621 | Compatible with LVTTL and LVCMOS signals. |
|  | FiveVolts | 14619 | Compatible with TTL and CMOS signals. |

##### Remarks

A logic family corresponds to voltage thresholds that are compatible with a group of voltage standards. Refer to device documentation for information on the logic high and logic low voltages for these logic families.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetrigger.htm language=enus -->
## TOPIC 00580: PauseTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PauseTrigger Class

### PauseTrigger Class

signals and triggers that pause a task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class PauseTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class PauseTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The PauseTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AnalogLevel | Gets the AnalogLevelPauseTrigger. |
|  | AnalogWindow | Gets the AnalogWindowPauseTrigger. |
|  | DigitalLevel | Gets the DigitalLevelPauseTrigger. |
|  | DigitalPattern | Gets the DigitalPatternPauseTrigger. |
|  | Terminal | Indicates the name of the internal Pause Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
|  | Type | Specifies the type of trigger to use to pause a task. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAnalogLevelTrigger | Configures the task to pause acquisition or generation when an analog signal is above or below a level you specify. |
|  | ConfigureAnalogWindowTrigger | Configures the task to pause acquisition or generation when an analog signal is inside or outside of a range you specify. |
|  | ConfigureDigitalLevelTrigger | Configures the task to pause acquisition or generation based on the level of a digital signal. |
|  | ConfigureDigitalPatternTrigger | Configures a task to pause the acquisition or generation when the device matches a digital pattern. |
|  | ConfigureNone | Disables pause triggering for the task. Once started, samples are acquired or generated until the requested number has been acquired or generated, or the task has stopped. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetriggerlevelactivelevel.htm language=enus -->
## TOPIC 00581: PauseTriggerLevelActiveLevel Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetriggerlevelactivelevel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetriggerlevelactivelevel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PauseTriggerLevelActiveLevel Enumeration

### PauseTriggerLevelActiveLevel Enumeration

Specifies the active level of the exported Pause Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PauseTriggerLevelActiveLevel
```

```text
Public Enumeration PauseTriggerLevelActiveLevel
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

PauseTriggerLevelActiveLevel

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetriggertype.htm language=enus -->
## TOPIC 00582: PauseTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetriggertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_pausetriggertype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PauseTriggerType Enumeration

### PauseTriggerType Enumeration

type

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PauseTriggerType
```

```text
Public Enumeration PauseTriggerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AnalogLevel | 10101 | Pause the measurement or generation while an analog signal is above or below a level. |
|  | AnalogWindow | 10103 | Pause the measurement or generation while an analog signal is either inside or outside of a range of values. |
|  | DigitalLevel | 10152 | Pause the measurement or generation while a digital signal is at either a high or low state. |
|  | DigitalPattern | 10398 | Pause the measurement or generation while digital physical channels either match or do not match a digital pattern. |
|  | None | 10230 | Do not pause the measurement or generation. |

##### Remarks

type

Type

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannel.htm language=enus -->
## TOPIC 00583: PhysicalChannel Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannel Class

### PhysicalChannel Class

channel

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class PhysicalChannel : MarshalByRefObject, 
	IDisposable
```

```text
Public Class PhysicalChannel
	Inherits MarshalByRefObject
	Implements IDisposable
```

The PhysicalChannel type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AIInputSources | Indicates the list of input sources supported by the channel. Channels may support using the signal from the I/O connector or one of several calibration signals. |
|  | AISupportedMeasurementTypes | Gets the measurement types supported by the physical channels of the device. |
|  | AITerminalConfigurations | Indicates the list of input terminal configurations supported by the channel. |
|  | AOManualControlAmplitude | Indicates the current value of the front panel amplitude control for the physical channel in volts. |
|  | AOManualControlEnable | Specifies if you can control the physical channel externally via a manual control located on the device. You cannot simultaneously control a channel manually and with NI-DAQmx. |
|  | AOManualControlFrequency | Indicates the current value of the front panel frequency control for the physical channel in hertz. |
|  | AOManualControlShortDetected | Indicates whether the physical channel is currently disabled due to a short detected on the channel. |
|  | AOPowerAmplifierChannelEnable | Specifies whether to enable or disable a channel for amplification. This property can also be used to check if a channel is enabled. |
|  | AOPowerAmplifierGain | Indicates the calibrated gain of the channel. |
|  | AOPowerAmplifierOffset | Indicates the calibrated offset of the channel in volts. |
|  | AOPowerAmplifierOvercurrent | Indicates if the channel detected an overcurrent condition. |
|  | AOPowerAmplifierScalingCoefficients | Indicates the coefficients of a polynomial equation used to scale from pre-amplified values. |
|  | AOSupportedOutputTypes | Gets the generation types supported by the physical channels of the device. |
|  | AOTerminalConfigurations | Indicates the list of output terminal configurations supported by the channel. |
|  | CISupportedMeasurementTypes | Gets the measurement types supported by the physical channels of the device. |
|  | COSupportedOutputTypes | Gets the generation types supported by the physical channels of the device |
|  | DIChangeDetectionSupported | Indicates if the change detection timing type is supported for the digital input physical channel. |
|  | DIPortWidth | Indicates in bits the width of digital input port. |
|  | DISampleClockSupported | Indicates if the sample clock timing type is supported for the digital input physical channel. |
|  | DISampleModes | Gets the sample modes supported by the physical channels that support sample clocked digital input. |
|  | DOPortWidth | Indicates in bits the width of digital output port. |
|  | DOSampleClockSupported | Indicates if the sample clock timing type is supported for the digital output physical channel. |
|  | DOSampleModes | Gets the sample modes supported by physical channels that support sample clocked digital output. |
|  | PhysicalChannelName | Gets the name of the physical channel. |
|  | PowerControlEnable | Specifies whether to turn on the sensor's power supply. |
|  | PowerControlType | Specifies the type of power supplied to the sensor. |
|  | PowerControlVoltage | Specifies the voltage level for the sensor's power supply. |
|  | SensorPowerOpenChannel | Indicates whether there is an open channel or undercurrent condition on the channel. |
|  | SensorPowerOvercurrent | Indicates whether there is an overcurrent condition on the channel. |
|  | SensorPowerTypes | Indicates the types of power supplied to the sensor supported by this channel. |
|  | SensorPowerVoltageRangeValues | Indicates pairs of sensor power voltage ranges supported by this channel. Each pair consists of the low value followed by the high value. |
|  | TedsBitStream | Indicates the TEDS binary bitstream without checksums. |
|  | TedsManufacturerID | Indicates the manufacturer ID of the sensor. |
|  | TedsModelNumber | Indicates the model number of the sensor. |
|  | TedsSerialNumber | Indicates the serial number of the sensor. |
|  | TedsTemplateIDs | Indicates the IDs of the templates in the bitstream in TedsBitStream. |
|  | TedsVersionLetter | Indicates the version letter of the sensor. |
|  | TedsVersionNumber | Indicates the version number of the sensor. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ClearTeds | Removes TEDS information from the physical channel you specify. |
|  | ConfigureTeds | Associates TEDS information with the physical channel you specify, using a TEDS sensor connected to the physical channel. |
|  | ConfigureTeds(String) | Associates TEDS information with the physical channel you specify. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by PhysicalChannel. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by PhysicalChannel or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WriteTedsData(Byte, BasicTedsDataOption) | Write TEDS data from a Byte array to a sensor on the physical channel you specify. |
|  | WriteTedsData(String, BasicTedsDataOption) | Write TEDS data from a virtual TEDS file to a sensor on the physical channel you specify. |

Top

##### Remarks

LoadPhysicalChannel(String)

Local

DaqSystem

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaccess.htm language=enus -->
## TOPIC 00584: PhysicalChannelAccess Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaccess.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaccess.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannelAccess Enumeration

### PhysicalChannelAccess Enumeration

Specifies the physical channel access types to include when requesting a list of 
physical channels.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum PhysicalChannelAccess
```

```text
<FlagsAttribute>
Public Enumeration PhysicalChannelAccess
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | External | 8192 | Physical channels with an external connector on the device. |
|  | Internal | 16384 | Physical channels internal to the device. |
|  | All | 24576 | Both internal and external channels. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaipowercontroltype.htm language=enus -->
## TOPIC 00585: PhysicalChannelAIPowerControlType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaipowercontroltype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaipowercontroltype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannelAIPowerControlType Enumeration

### PhysicalChannelAIPowerControlType Enumeration

Specifies the type of power supplied to the sensor.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PhysicalChannelAIPowerControlType
```

```text
Public Enumeration PhysicalChannelAIPowerControlType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DC | 10050 | Sensor power supply generates a single DC voltage level. |
|  | AC | 10045 | Sensor power supply generates an AC voltage. |
|  | BipolarDC | 16147 | Sensor power supply generates a pair of DC voltage levels. |

##### Remarks

PowerControlType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaisensorpowertype.htm language=enus -->
## TOPIC 00586: PhysicalChannelAISensorPowerType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaisensorpowertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchannelaisensorpowertype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannelAISensorPowerType Enumeration

### PhysicalChannelAISensorPowerType Enumeration

Indicates the types of power supplied to the sensor supported by this channel.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PhysicalChannelAISensorPowerType
```

```text
Public Enumeration PhysicalChannelAISensorPowerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DC | 10050 | Sensor power supply generates a single DC voltage level. |
|  | AC | 10045 | Sensor power supply generates an AC voltage. |
|  | BipolarDC | 16147 | Sensor power supply generates a pair of DC voltage levels. |

##### Remarks

SensorPowerTypes

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchanneltypes.htm language=enus -->
## TOPIC 00587: PhysicalChannelTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchanneltypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_physicalchanneltypes.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PhysicalChannelTypes Enumeration

### PhysicalChannelTypes Enumeration

Specifies the types of physical channels to include when requesting a list of 
physical channels.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum PhysicalChannelTypes
```

```text
<FlagsAttribute>
Public Enumeration PhysicalChannelTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AI | 1 | Analog inputs. |
|  | AO | 2 | Analog outputs. |
|  | DILine | 4 | Digital input lines. |
|  | DIPort | 8 | Digital input ports. |
|  | DOLine | 16 | Digital output lines. |
|  | DOPort | 32 | Digital output ports. |
|  | CI | 64 | Counter inputs. |
|  | CO | 128 | Counter outputs. |
|  | All | 255 | All types of physical channels. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_polynomialdirection.htm language=enus -->
## TOPIC 00588: PolynomialDirection Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_polynomialdirection.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_polynomialdirection.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialDirection Enumeration

### PolynomialDirection Enumeration

Specifies the direction of the conversion the provided polynomial coefficients perform.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PolynomialDirection
```

```text
Public Enumeration PolynomialDirection
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Forward | 0 | The provided coefficients are the coefficients of the forward polynomial. |
|  | Reverse | 1 | The provided coefficients are the coefficients of the reverse polynomial. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_polynomialscale.htm language=enus -->
## TOPIC 00589: PolynomialScale Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_polynomialscale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_polynomialscale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PolynomialScale Class

### PolynomialScale Class

custom scale

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class PolynomialScale : Scale
```

```text
Public Class PolynomialScale
	Inherits Scale
```

The PolynomialScale type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | PolynomialScale(String, Double, Double) | Creates a new instance of the PolynomialScale class with the specified forward and reverse coefficients. |
|  | PolynomialScale(String, PolynomialDirection, Double, Double, Double) | Creates a new instance of the PolynomialScale class with the specified forward or reverse coefficients and automatically computes the other set of coefficients with the same order as the provided coefficients, using 1000 points in the specified range. |
|  | PolynomialScale(String, PolynomialDirection, Double, Double, Double, Int32, Int32) | Creates a new instance of the PolynomialScale class with the specified forward or reverse coefficients and automatically computes the other set of coefficients. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Specifies a description for the scale. (Inherited from Scale.) |
|  | ForwardCoefficients | Specifies an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. |
|  | Name | Gets the name of the scale. (Inherited from Scale.) |
|  | PreScaledUnits | Specifies the units of the values that you want to scale. (Inherited from Scale.) |
|  | ReverseCoefficients | Specifies an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9y^3. |
|  | ScaledUnits | Specifies the units to use for scaled values. You can use an arbitrary string. (Inherited from Scale.) |
|  | Type | Gets the type of scale. (Inherited from Scale.) |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Scale. (Inherited from Scale.) |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Scale or optionally releases only the unmanaged resources. (Inherited from Scale.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Inherited from Scale.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_productcategory.htm language=enus -->
## TOPIC 00590: ProductCategory Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_productcategory.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_productcategory.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ProductCategory Enumeration

### ProductCategory Enumeration

Indicates the product category of the device. This category corresponds to the category displayed in MAX when creating NI-DAQmx simulated devices.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ProductCategory
```

```text
Public Enumeration ProductCategory
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | MSeriesDaq | 14643 | M Series DAQ. |
|  | XSeriesDaq | 15858 | X Series DAQ. |
|  | ESeriesDaq | 14642 | E Series DAQ. |
|  | SSeriesDaq | 14644 | S Series DAQ. |
|  | BSeriesDaq | 14662 | B Series DAQ. |
|  | SCSeriesDaq | 14645 | SC Series DAQ. |
|  | UsbDaq | 14646 | USB DAQ. |
|  | AOSeries | 14647 | AO Series. |
|  | DigitalIO | 14648 | Digital I/O. |
|  | TioSeries | 14661 | TIO Series. |
|  | DynamicSignalAcquisition | 14649 | Dynamic Signal Acquisition. |
|  | Switches | 14650 | Switches. |
|  | CompactDaqChassis | 14658 | CompactDAQ chassis. |
|  | CompactRioChassis | 16144 | CompactRIO Chassis. |
|  | CSeriesModule | 14659 | C Series I/O module. |
|  | ScxiModule | 14660 | SCXI module. |
|  | SccConnectorBlock | 14704 | SCC Connector Block. |
|  | SccModule | 14705 | SCC Module. |
|  | NIElvis | 14755 | NI ELVIS. |
|  | NetworkDAQ | 14829 | Network DAQ. |
|  | SCExpress | 15886 | SC Express. |
|  | FieldDaq | 16151 | FieldDAQ. |
|  | Unknown | 12588 | Unknown category. |

##### Remarks

ProductCategory

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_propertyfilterflags.htm language=enus -->
## TOPIC 00591: PropertyFilterFlags Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_propertyfilterflags.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_propertyfilterflags.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PropertyFilterFlags Enumeration

### PropertyFilterFlags Enumeration

Specifies a set of property filtering options.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum PropertyFilterFlags
```

```text
<FlagsAttribute>
Public Enumeration PropertyFilterFlags
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | No additional filtering options. |
|  | Volatile | 1 | The property filtering only returns properties that can be modified by the DAQmx driver while the task is running. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_propertyfiltertype.htm language=enus -->
## TOPIC 00592: PropertyFilterType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_propertyfiltertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_propertyfiltertype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

PropertyFilterType Enumeration

### PropertyFilterType Enumeration

Specifies the type of property filtering to perform.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum PropertyFilterType
```

```text
Public Enumeration PropertyFilterType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | All | 0 | Returns all of the properties that belong to the Task subobject. |
|  | ConfiguredDevices | 1 | Returns only the properties that apply to the configured devices on the system and belong to the Task subobject. |
|  | DevicesInTask | 2 | Returns only the properties that apply to the devices being used in the task and belong to the Task subobject. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_rangemapscale.htm language=enus -->
## TOPIC 00593: RangeMapScale Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_rangemapscale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_rangemapscale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

RangeMapScale Class

### RangeMapScale Class

custom scale

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class RangeMapScale : Scale
```

```text
Public Class RangeMapScale
	Inherits Scale
```

The RangeMapScale type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | RangeMapScale | Creates a new instance of the RangeMapScale class with the prescaled minimum and maximum values and the scaled minimum and maximum values. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Specifies a description for the scale. (Inherited from Scale.) |
|  | Name | Gets the name of the scale. (Inherited from Scale.) |
|  | PreScaledMax | Specifies the largest value in the range of pre-scaled values. NI-DAQmx maps this value to ScaledMax. |
|  | PreScaledMin | Specifies the smallest value in the range of pre-scaled values. NI-DAQmx maps this value to ScaledMin. |
|  | PreScaledUnits | Specifies the units of the values that you want to scale. (Inherited from Scale.) |
|  | ScaledMax | Specifies the largest value in the range of scaled values. NI-DAQmx maps this value to PreScaledMax. Reads coerce samples that are larger than this value to match this value. Writes generate errors for samples that are larger than this value. |
|  | ScaledMin | Specifies the smallest value in the range of scaled values. NI-DAQmx maps this value to PreScaledMin. Reads coerce samples that are smaller than this value to match this value. Writes generate errors for samples that are smaller than this value. |
|  | ScaledUnits | Specifies the units to use for scaled values. You can use an arbitrary string. (Inherited from Scale.) |
|  | Type | Gets the type of scale. (Inherited from Scale.) |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Scale. (Inherited from Scale.) |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Scale or optionally releases only the unmanaged resources. (Inherited from Scale.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Inherited from Scale.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readoverwritemode.htm language=enus -->
## TOPIC 00594: ReadOverwriteMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readoverwritemode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readoverwritemode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReadOverwriteMode Enumeration

### ReadOverwriteMode Enumeration

Specifies whether to overwrite samples in the buffer that you have not yet read.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReadOverwriteMode
```

```text
Public Enumeration ReadOverwriteMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | OverwriteUnreadSamples | 10252 | When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the unread samples with new ones. You can read the new samples by setting ReadRelativeTo to MostRecentSample and setting ReadOffset to the appropriate number of samples. |
|  | DoNotOverwriteUnreadSamples | 10159 | The acquisition stops when it encounters a sample in the buffer that you have not read. |

##### Remarks

ReadOverwriteMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readrelativeto.htm language=enus -->
## TOPIC 00595: ReadRelativeTo Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readrelativeto.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readrelativeto.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReadRelativeTo Enumeration

### ReadRelativeTo Enumeration

ReadOffset

CurrentReadPosition

Reference Trigger

FirstPretriggerSample

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReadRelativeTo
```

```text
Public Enumeration ReadRelativeTo
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | FirstSample | 10424 | Start reading samples relative to the first sample acquired. |
|  | CurrentReadPosition | 10425 | Start reading samples relative to the last sample returned by the previous read. For the first read operation, this position is the first sample acquired or the first pretrigger sample if you configured a reference trigger for the task. |
|  | ReferenceTrigger | 10426 | Start reading samples relative to the first sample after the reference trigger occurred. |
|  | FirstPretriggerSample | 10427 | Start reading samples relative to the first pretrigger sample. You specify the number of pretrigger samples to acquire when you configure a reference trigger. |
|  | MostRecentSample | 10428 | Start reading samples relative to the next sample acquired. For example, use this value and set ReadOffset to -1 to read the last sample acquired. |

##### Remarks

ReadOffset

CurrentReadPosition

Reference Trigger

FirstPretriggerSample

ReadRelativeTo

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readwaitmode.htm language=enus -->
## TOPIC 00596: ReadWaitMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readwaitmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readwaitmode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReadWaitMode Enumeration

### ReadWaitMode Enumeration

Specifies how reading from the task waits for samples to become available.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReadWaitMode
```

```text
Public Enumeration ReadWaitMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | WaitForInterrupt | 12523 | Check for available samples when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates. |
|  | Poll | 12524 | Repeatedly check for available samples as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |
|  | Yield | 12525 | Repeatedly check for available samples, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency. |
|  | Sleep | 12547 | Check for available samples once per the amount of time specified in ReadSleepTime. |

##### Remarks

ReadWaitMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyforstarteventlevelactivelevel.htm language=enus -->
## TOPIC 00597: ReadyForStartEventLevelActiveLevel Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyforstarteventlevelactivelevel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyforstarteventlevelactivelevel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReadyForStartEventLevelActiveLevel Enumeration

### ReadyForStartEventLevelActiveLevel Enumeration

Specifies the polarity of the exported Ready for Start Event.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReadyForStartEventLevelActiveLevel
```

```text
Public Enumeration ReadyForStartEventLevelActiveLevel
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

ReadyForStartEventLevelActiveLevel

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyfortransfereventdeassertcondition.htm language=enus -->
## TOPIC 00598: ReadyForTransferEventDeassertCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyfortransfereventdeassertcondition.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyfortransfereventdeassertcondition.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReadyForTransferEventDeassertCondition Enumeration

### ReadyForTransferEventDeassertCondition Enumeration

Specifies when the ready for transfer event deasserts.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReadyForTransferEventDeassertCondition
```

```text
Public Enumeration ReadyForTransferEventDeassertCondition
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | OnboardMemoryMoreThanHalfFull | 10237 | Deassert the signal when more than half of the onboard memory of the device fills. |
|  | OnboardMemoryFull | 10236 | Deassert the signal when the onboard memory fills. |
|  | OnboardMemoryCustomThreshold | 12577 | Deassert the signal when the amount of space available in the onboard memory is below the value specified with ReadyForTransferEventDeassertConditionCustomThreshold. |

##### Remarks

ReadyForTransferEventDeassertCondition

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyfortransfereventlevelactivelevel.htm language=enus -->
## TOPIC 00599: ReadyForTransferEventLevelActiveLevel Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyfortransfereventlevelactivelevel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_readyfortransfereventlevelactivelevel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReadyForTransferEventLevelActiveLevel Enumeration

### ReadyForTransferEventLevelActiveLevel Enumeration

Specifies the active level of the exported Ready for Transfer Event.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReadyForTransferEventLevelActiveLevel
```

```text
Public Enumeration ReadyForTransferEventLevelActiveLevel
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

ReadyForTransferEventLevelActiveLevel

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_reallocationpolicy.htm language=enus -->
## TOPIC 00600: ReallocationPolicy Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_reallocationpolicy.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_reallocationpolicy.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReallocationPolicy Enumeration

### ReallocationPolicy Enumeration

Specifies the behavior of a memory-optimized read method operation when the operation yields more samples than the current capacity of the buffer can allocate.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReallocationPolicy
```

```text
Public Enumeration ReallocationPolicy
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | DoNotReallocate | 0 | The read operation is limited to read up to the capacity of the provided buffer. |
|  | ToGrow | 1 | The read operation can request more memory if the operation yields more samples than the capacity of the provided buffer. You must use initialized data; otherwise, your application could throw a DaqException. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetrigger.htm language=enus -->
## TOPIC 00601: ReferenceTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTrigger Class

### ReferenceTrigger Class

reference point between the pretrigger samples and the post-trigger samples

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class ReferenceTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class ReferenceTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The ReferenceTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AnalogEdge | Gets the AnalogEdgeReferenceTrigger. |
|  | AnalogMultiEdge | Gets the AnalogMultiEdgeReferenceTrigger. |
|  | AnalogWindow | Gets the AnalogWindowReferenceTrigger. |
|  | AutoTriggered | Indicates whether a completed acquisition was triggered by the auto trigger. If an acquisition has not completed after the task starts, this property returns . This property is only applicable when AutoTriggerEnable is . |
|  | AutoTriggerEnable | Specifies whether to send a software trigger to the device when a hardware trigger is no longer active in order to prevent a timeout. |
|  | Delay | Specifies in seconds the time to wait after the device receives the Reference Trigger before switching from pretrigger to posttrigger samples. |
|  | DigitalEdge | Gets the DigitalEdgeReferenceTrigger. |
|  | DigitalPattern | Gets the DigitalPatternReferenceTrigger. |
|  | MaximumNumberOfTriggersToDetect | Specifies the maximum number of times the task will detect a reference trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger. |
|  | PretriggerSamples | Specifies the minimum number of pretrigger samples to acquire from each channel before recognizing the reference trigger. Post-trigger samples per channel are equal to SamplesPerChannel minus the number of pretrigger samples per channel. |
|  | Retriggerable | Specifies whether a finite task resets, acquires pretrigger samples, and waits for another Reference Trigger after the task completes. When you set this property to TRUE, the device will acquire post-trigger samples, reset, and acquire pretrigger samples each time the Reference Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring signals. |
|  | RetriggerWindow | Specifies the duration in seconds after each trigger during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. Specifying a Retrigger Window of -1 causes the window to be infinite. |
|  | Terminal | Indicates the name of the internal Reference Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
|  | Timestamp | Gets the reference trigger timestamp. |
|  | TimestampEnable | Specifies whether the reference trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
|  | TimestampTimescale | Specifies the reference trigger timestamp timescale. |
|  | TriggerWindow | Specifies the duration in seconds after the task starts during which the device may trigger. Once the window has passed, the device stops detecting triggers, and the task will stop after the device finishes acquiring post-trigger samples that it already started. If no triggers are detected during the entire period, then no data will be returned. Specifying a Trigger Window of -1 causes the window to be infinite. |
|  | Type | Specifies the type of trigger to use to mark a reference point for the measurement. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAnalogEdgeTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal reaches the level you specify; and the device acquires all post-trigger samples. |
|  | ConfigureAnalogMultiEdgeTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples, any of the configured analog signals reaches the levels you specify, and the device acquires all post-trigger samples. |
|  | ConfigureAnalogWindowTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples; an analog signal enters or leaves a range you specify; and the device acquires all post-trigger samples. |
|  | ConfigureDigitalEdgeTrigger | Configures the task to stop the acquisition when the device acquires all pretrigger samples, detects a rising or falling edge of a digital signal, and acquires all post-trigger samples. |
|  | ConfigureDigitalPatternTrigger | Configures a task to stop the acquisition when the device acquires all pretrigger samples, matches a digital pattern, and acquires all posttrigger samples. |
|  | ConfigureNone | Disables reference triggering for the measurement. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggerpulsepolarity.htm language=enus -->
## TOPIC 00602: ReferenceTriggerPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggerpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggerpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTriggerPulsePolarity Enumeration

### ReferenceTriggerPulsePolarity Enumeration

Specifies the polarity of the exported Reference Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReferenceTriggerPulsePolarity
```

```text
Public Enumeration ReferenceTriggerPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

ReferenceTriggerPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggertimestamptimescale.htm language=enus -->
## TOPIC 00603: ReferenceTriggerTimestampTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggertimestamptimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggertimestamptimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTriggerTimestampTimescale Enumeration

### ReferenceTriggerTimestampTimescale Enumeration

Specifies the reference trigger timestamp timescale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReferenceTriggerTimestampTimescale
```

```text
Public Enumeration ReferenceTriggerTimestampTimescale
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HostTime | 16126 | Use the host device. |
|  | IODeviceTime | 16127 | Use the I/O device. |

##### Remarks

TimestampTimescale

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggertype.htm language=enus -->
## TOPIC 00604: ReferenceTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_referencetriggertype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ReferenceTriggerType Enumeration

### ReferenceTriggerType Enumeration

type

reference

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ReferenceTriggerType
```

```text
Public Enumeration ReferenceTriggerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AnalogEdge | 10099 | Trigger when an analog signal signal crosses a threshold. |
|  | AnalogMultiEdge | 16108 | Trigger when any of the configured analog signals cross their respective thresholds. |
|  | DigitalEdge | 10150 | Trigger on the rising or falling edge of a digital signal. |
|  | DigitalPattern | 10398 | Trigger when digital physical channels match a digital pattern. |
|  | AnalogWindow | 10103 | Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement. |
|  | Time | 15996 | Trigger when a specified time is reached. |
|  | None | 10230 | Disable triggering for the task. |

##### Remarks

type

reference

Type

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockactiveedge.htm language=enus -->
## TOPIC 00605: SampleClockActiveEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockactiveedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockactiveedge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockActiveEdge Enumeration

### SampleClockActiveEdge Enumeration

Specifies on which edge of a clock pulse sampling takes place. This property is useful primarily when the signal you use as the Sample Clock is not a periodic clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockActiveEdge
```

```text
Public Enumeration SampleClockActiveEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

SampleClockActiveEdge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockeventargs.htm language=enus -->
## TOPIC 00606: SampleClockEventArgs Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockeventargs.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockEventArgs Class

### SampleClockEventArgs Class

SampleClock

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class SampleClockEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class SampleClockEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The SampleClockEventArgs type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockeventhandler.htm language=enus -->
## TOPIC 00607: SampleClockEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockeventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockeventhandler.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockEventHandler Delegate

### SampleClockEventHandler Delegate

SampleClock

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void SampleClockEventHandler(
	Object sender,
	SampleClockEventArgs e
)
```

```text
Public Delegate Sub SampleClockEventHandler ( 
	sender As Object,
	e As SampleClockEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxSampleClockEventArgs A SampleClockEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockoutputbehavior.htm language=enus -->
## TOPIC 00608: SampleClockOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockoutputbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockoutputbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockOutputBehavior Enumeration

### SampleClockOutputBehavior Enumeration

Specifies whether the exported Sample Clock issues a pulse at the beginning of a sample or changes to a high state for the duration of the sample.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockOutputBehavior
```

```text
Public Enumeration SampleClockOutputBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Pulse | 10265 | The exported Sample Clock pulses at the beginning of each sample. |
|  | Level | 10210 | The exported Sample Clock goes high at the beginning of the sample and goes low when the last AI Convert begins. |

##### Remarks

SampleClockOutputBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockoverrunbehavior.htm language=enus -->
## TOPIC 00609: SampleClockOverrunBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockoverrunbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockoverrunbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockOverrunBehavior Enumeration

### SampleClockOverrunBehavior Enumeration

Specifies the action to take if Sample Clock edges occur faster than the device can handle them.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockOverrunBehavior
```

```text
Public Enumeration SampleClockOverrunBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | StopTaskAndError | 15862 | Stop task and return an error. |
|  | IgnoreOverruns | 15863 | NI-DAQmx ignores Sample Clock overruns, and the task continues to run. |

##### Remarks

SampleClockOverrunBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockpulsepolarity.htm language=enus -->
## TOPIC 00610: SampleClockPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockPulsePolarity Enumeration

### SampleClockPulsePolarity Enumeration

SampleClockOutputBehavior

Pulse

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockPulsePolarity
```

```text
Public Enumeration SampleClockPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

SampleClockOutputBehavior

Pulse

SampleClockPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclocktimebaseactiveedge.htm language=enus -->
## TOPIC 00611: SampleClockTimebaseActiveEdge Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclocktimebaseactiveedge.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclocktimebaseactiveedge.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockTimebaseActiveEdge Enumeration

### SampleClockTimebaseActiveEdge Enumeration

Specifies on which edge to recognize a Sample Clock Timebase pulse. This property is useful primarily when the signal you use as the Sample Clock Timebase is not a periodic clock.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockTimebaseActiveEdge
```

```text
Public Enumeration SampleClockTimebaseActiveEdge
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Rising | 10280 | Rising edge(s). |
|  | Falling | 10171 | Falling edge(s). |

##### Remarks

SampleClockTimebaseActiveEdge

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclocktimingresponsemode.htm language=enus -->
## TOPIC 00612: SampleClockTimingResponseMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclocktimingresponsemode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclocktimingresponsemode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockTimingResponseMode Enumeration

### SampleClockTimingResponseMode Enumeration

Specifies how the device responds to the sample clock and to triggers.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockTimingResponseMode
```

```text
Public Enumeration SampleClockTimingResponseMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | SingleCycle | 14613 | Device responds by the next sample clock edge. |
|  | Multicycle | 14614 | Device acquires or generates samples on the next sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Refer to device documentation for information about which triggers the multicycle response mode affects. This response mode allows higher data transfer rates at the cost of increased latency for responding to triggers. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockunderflowbehavior.htm language=enus -->
## TOPIC 00613: SampleClockUnderflowBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockunderflowbehavior.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampleclockunderflowbehavior.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleClockUnderflowBehavior Enumeration

### SampleClockUnderflowBehavior Enumeration

Specifies the action to take when the onboard memory of the device becomes empty. In either case, the sample clock does not stop.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleClockUnderflowBehavior
```

```text
Public Enumeration SampleClockUnderflowBehavior
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HaltOutputAndError | 14615 | Stop generating samples and return an error. |
|  | PauseUntilDataAvailable | 14616 | Pause the task until samples are available in the FIFO. |

##### Remarks

SampleClockUnderflowBehavior

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplecompleteeventargs.htm language=enus -->
## TOPIC 00614: SampleCompleteEventArgs Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplecompleteeventargs.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplecompleteeventargs.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleCompleteEventArgs Class

### SampleCompleteEventArgs Class

SampleComplete

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[SerializableAttribute]
public class SampleCompleteEventArgs : EventArgs, 
	ISerializable
```

```text
<SerializableAttribute>
Public Class SampleCompleteEventArgs
	Inherits EventArgs
	Implements ISerializable
```

The SampleCompleteEventArgs type exposes the following members.

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetObjectData | Sets the SerializationInfo object with information about the exception. |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | ToString | Returns a string that represents the current object. (Inherited from Object.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplecompleteeventhandler.htm language=enus -->
## TOPIC 00615: SampleCompleteEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplecompleteeventhandler.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplecompleteeventhandler.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleCompleteEventHandler Delegate

### SampleCompleteEventHandler Delegate

SampleComplete

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public delegate void SampleCompleteEventHandler(
	Object sender,
	SampleCompleteEventArgs e
)
```

```text
Public Delegate Sub SampleCompleteEventHandler ( 
	sender As Object,
	e As SampleCompleteEventArgs
)
```

###### Parameters

- **sender**
  - Type: SystemObject The Task that caused this event.
- **e**
  - Type: NationalInstruments.DAQmxSampleCompleteEventArgs A SampleCompleteEventArgs that contains the event data.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplequantitymode.htm language=enus -->
## TOPIC 00616: SampleQuantityMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplequantitymode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_samplequantitymode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleQuantityMode Enumeration

### SampleQuantityMode Enumeration

Specifies if a task acquires or generates a finite number of samples or if it continuously acquires or generates samples.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleQuantityMode
```

```text
Public Enumeration SampleQuantityMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | FiniteSamples | 10178 | Acquire or generate a finite number of samples. |
|  | ContinuousSamples | 10123 | Acquire or generate samples until you stop the task. |
|  | HardwareTimedSinglePoint | 12522 | Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types. |

##### Remarks

SampleQuantityMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampletimingtype.htm language=enus -->
## TOPIC 00617: SampleTimingType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampletimingtype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_sampletimingtype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SampleTimingType Enumeration

### SampleTimingType Enumeration

type of sample timing

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum SampleTimingType
```

```text
Public Enumeration SampleTimingType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | SampleClock | 10388 | Acquire or generate samples on the specified edge of the sample clock. |
|  | BurstHandshake | 12548 | Determine sample timing using burst handshaking between the device and a peripheral device. |
|  | Handshake | 10389 | Determine sample timing by using digital handshaking between the device and a peripheral device. |
|  | Implicit | 10451 | Configure only the duration of the task. |
|  | OnDemand | 10390 | Acquire or generate a sample on each read or write operation. This timing type is also referred to as static or software-timed. |
|  | ChangeDetection | 12504 | Acquire samples when a change occurs in the state of one or more digital input lines. The lines must be contained within a digital input channel. |
|  | PipelinedSampleClock | 14668 | Device acquires or generates samples on each sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Pipelining allows higher data transfer rates at the cost of increased trigger response latency. Refer to the device documentation for information about which triggers pipelining affects. This timing type allows handshaking with some devices using the Pause trigger, the Ready for Transfer event, or the Data Active event. Refer to the device documentation for more information. |

##### Remarks

type of sample timing

SampleTimingType

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedchannelinfo.htm language=enus -->
## TOPIC 00618: SavedChannelInfo Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedchannelinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedchannelinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedChannelInfo Class

### SavedChannelInfo Class

GetSavedChannelInfo(String)

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class SavedChannelInfo : MarshalByRefObject, 
	IDisposable
```

```text
Public Class SavedChannelInfo
	Inherits MarshalByRefObject
	Implements IDisposable
```

The SavedChannelInfo type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowInteractiveDeletion | Indicates whether the global channel can be deleted through MAX. |
|  | AllowInteractiveEditing | Indicates whether the global channel can be edited in the DAQ Assistant. |
|  | Author | Indicates the author of the global channel. |
|  | Name | Gets the name of the channel. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by SavedChannelInfo. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SavedChannelInfo or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedscaleinfo.htm language=enus -->
## TOPIC 00619: SavedScaleInfo Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedscaleinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedscaleinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedScaleInfo Class

### SavedScaleInfo Class

custom scale

GetSavedScaleInfo(String)

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class SavedScaleInfo : MarshalByRefObject, 
	IDisposable
```

```text
Public Class SavedScaleInfo
	Inherits MarshalByRefObject
	Implements IDisposable
```

The SavedScaleInfo type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowInteractiveDeletion | Indicates whether the custom scale can be deleted through MAX. |
|  | AllowInteractiveEditing | Indicates whether the custom scale can be edited in the DAQ Assistant. |
|  | Author | Indicates the author of the custom scale. |
|  | Name | Gets the name of the scale. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by SavedScaleInfo. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SavedScaleInfo or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedtaskinfo.htm language=enus -->
## TOPIC 00620: SavedTaskInfo Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedtaskinfo.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_savedtaskinfo.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SavedTaskInfo Class

### SavedTaskInfo Class

task

GetSavedTaskInfo(String)

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class SavedTaskInfo : MarshalByRefObject, 
	IDisposable
```

```text
Public Class SavedTaskInfo
	Inherits MarshalByRefObject
	Implements IDisposable
```

The SavedTaskInfo type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AllowInteractiveDeletion | Indicates whether the task can be deleted through MAX. |
|  | AllowInteractiveEditing | Indicates whether the task can be edited in the DAQ Assistant. |
|  | Author | Indicates the author of the task. |
|  | Name | Gets the name of the task. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by SavedTaskInfo. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SavedTaskInfo or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_saveoptions.htm language=enus -->
## TOPIC 00621: SaveOptions Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_saveoptions.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_saveoptions.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SaveOptions Enumeration

### SaveOptions Enumeration

task

local or global channel

custom scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum SaveOptions
```

```text
<FlagsAttribute>
Public Enumeration SaveOptions
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AllowInteractiveEditing | 1 | The saved object may be edited through an interactive tool, such as Measurement Automation Explorer (MAX). |
|  | AllowInteractiveDeletion | 2 | The saved object may be deleted through an interactive tool, such as Measurement Automation Explorer (MAX). |
|  | OverwriteExisting | 4 | If a saved object already exists in Measurement Automation Explorer (MAX) with the same name as the new object, the new object overwrites the old object. |
|  | None | 0 | No options are enabled. |
|  | Default | 3 | The AllowInteractiveDeletion and AllowInteractiveEditing options are enabled. |
|  | All | 7 | All options are enabled. |

##### Remarks

You can specify multiple options by using bitwise or combining individual values.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scale.htm language=enus -->
## TOPIC 00622: Scale Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Scale Class

### Scale Class

custom scale

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public abstract class Scale : MarshalByRefObject, 
	IDisposable
```

```text
Public MustInherit Class Scale
	Inherits MarshalByRefObject
	Implements IDisposable
```

The Scale type exposes the following members.

##### Constructors

|  | Name | Description |
| --- | --- | --- |
|  | Scale | Creates a new instance of the Scale class with the specified scale name. |

Top

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Description | Specifies a description for the scale. |
|  | Name | Gets the name of the scale. |
|  | PreScaledUnits | Specifies the units of the values that you want to scale. |
|  | ScaledUnits | Specifies the units to use for scaled values. You can use an arbitrary string. |
|  | Type | Gets the type of scale. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by Scale. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by Scale or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

Scale is the base class for [LinearScale](t_nationalinstruments_daqmx_linearscale.htm), [PolynomialScale](t_nationalinstruments_daqmx_polynomialscale.htm), [RangeMapScale](t_nationalinstruments_daqmx_rangemapscale.htm), and [TableScale](t_nationalinstruments_daqmx_tablescale.htm). All instances of Scale are of one of the derived class types. Refer to the derived class documentation for more information.

When you create a scale, you must provide the scale with a name because the scale is associated with channels through its name. You can create and configure a scale in Measurement Automation Explorer (MAX) or with the constructor of a class that derives from Scale.

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scaleprescaledunits.htm language=enus -->
## TOPIC 00623: ScalePreScaledUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scaleprescaledunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scaleprescaledunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ScalePreScaledUnits Enumeration

### ScalePreScaledUnits Enumeration

Specifies the units of the values that you want to scale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ScalePreScaledUnits
```

```text
Public Enumeration ScalePreScaledUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Volts | 10348 | Volts. |
|  | Amps | 10342 | Amperes. |
|  | DegreesF | 10144 | Degrees Fahrenheit. |
|  | DegreesC | 10143 | Degrees Celsius. |
|  | DegreesR | 10145 | Degrees Rankine. |
|  | Kelvins | 10325 | Kelvins. |
|  | Strain | 10299 | Strain. |
|  | Ohms | 10384 | Ohms. |
|  | Hertz | 10373 | Hertz. |
|  | Seconds | 10364 | Seconds. |
|  | Meters | 10219 | Meters. |
|  | Inches | 10379 | Inches. |
|  | Degrees | 10146 | Degrees. |
|  | Radians | 10273 | Radians. |
|  | Ticks | 10304 | Ticks. |
|  | RPM | 16080 | Revolutions per minute. |
|  | RadiansPerSecond | 16081 | Radians per second. |
|  | DegreesPerSecond | 16082 | Degrees per second. |
|  | G | 10186 | 1 g is approximately equal to 9.81 m/s/s. |
|  | MetersPerSecondSquared | 12470 | Meters per second per second. |
|  | InchesPerSecondSquared | 12471 | Inches per second per second. |
|  | MetersPerSecond | 15959 | Meters per second. |
|  | InchesPerSecond | 15960 | Inches per second. |
|  | Pascals | 10081 | Pascals. |
|  | Newtons | 15875 | Newtons. |
|  | Pounds | 15876 | Pounds. |
|  | KilogramForce | 15877 | Kilograms-force. |
|  | PoundsPerSquareInch | 15879 | Pounds per square inch. |
|  | Bar | 15880 | Bar. |
|  | NewtonMeters | 15881 | Newton meters. |
|  | InchOunces | 15882 | Ounce-inches. |
|  | InchPounds | 15883 | Pound-inches. |
|  | FootPounds | 15884 | Pound-feet. |
|  | VoltsPerVolt | 15896 | Volts per volt. |
|  | MillivoltsPerVolt | 15897 | Millivolts per volt. |
|  | Coulombs | 16102 | Coulombs. |
|  | PicoCoulombs | 16103 | PicoCoulombs. |
|  | FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

##### Remarks

PreScaledUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scaletype.htm language=enus -->
## TOPIC 00624: ScaleType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scaletype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scaletype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ScaleType Enumeration

### ScaleType Enumeration

custom scale

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ScaleType
```

```text
Public Enumeration ScaleType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Linear | 10447 | Values are scaled linearly. |
|  | Polynomial | 10449 | Values are scaled by using an nth order polynomial equation. |
|  | RangeMap | 10448 | Values are scaled proportionally from a range of raw values to a range of scaled values. |
|  | Table | 10450 | An array of raw values is mapped to an array of corresponding scaled values, with all other values scaled proportionally. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scxi1124range.htm language=enus -->
## TOPIC 00625: Scxi1124Range Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scxi1124range.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_scxi1124range.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Scxi1124Range Enumeration

### Scxi1124Range Enumeration

Specifies the range for the SCXI 1124 calibration values.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum Scxi1124Range
```

```text
Public Enumeration Scxi1124Range
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Range0to1V | 14629 | Range is from 0 volts to 1 volt. |
|  | Range0to5V | 14630 | Range is from 0 volts to 5 volts. |
|  | Range0to10V | 14631 | Range is from 0 volts to 10 volts. |
|  | RangeNeg1to1V | 14632 | Range is from -1 volt to 1 volt. |
|  | RangeNeg5to5V | 14633 | Range is from -5 volts to 5 volts. |
|  | RangeNeg10to10V | 14634 | Range is from -10 volts to 10 volts. |
|  | Range0to20mA | 14635 | Range is from 0 mA to 20 mA. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntcalibrationselect.htm language=enus -->
## TOPIC 00626: ShuntCalibrationSelect Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntcalibrationselect.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntcalibrationselect.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ShuntCalibrationSelect Enumeration

### ShuntCalibrationSelect Enumeration

Specifies the shunt calibration switch(es) to enable.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ShuntCalibrationSelect
```

```text
Public Enumeration ShuntCalibrationSelect
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | A | 12513 | Switch A |
|  | B | 12514 | Switch B |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntelementlocation.htm language=enus -->
## TOPIC 00627: ShuntElementLocation Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntelementlocation.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntelementlocation.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ShuntElementLocation Enumeration

### ShuntElementLocation Enumeration

Specifies which resistor to use to calibrate the channel(s).

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ShuntElementLocation
```

```text
Public Enumeration ShuntElementLocation
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | R1 | 12465 | Resistor 1. |
|  | R2 | 12466 | Resistor 2. |
|  | R3 | 12467 | Resistor 3. |
|  | R4 | 14813 | Resistor 4. |
|  | None | 10230 | No resistor. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntresistorsource.htm language=enus -->
## TOPIC 00628: ShuntResistorSource Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntresistorsource.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_shuntresistorsource.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

ShuntResistorSource Enumeration

### ShuntResistorSource Enumeration

Specifies whether to use internal or external shunt.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum ShuntResistorSource
```

```text
Public Enumeration ShuntResistorSource
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | UserProvided | 10167 | Use an external shunt. |
|  | BuiltIn | 10200 | Use the internal shunt. |
|  | Default | -1 | Use the default shunt. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_signalroutingmodifiers.htm language=enus -->
## TOPIC 00629: SignalRoutingModifiers Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_signalroutingmodifiers.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_signalroutingmodifiers.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SignalRoutingModifiers Enumeration

### SignalRoutingModifiers Enumeration

inverted

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum SignalRoutingModifiers
```

```text
<FlagsAttribute>
Public Enumeration SignalRoutingModifiers
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | InvertPolarity | 1 | The signal is inverted. |

##### Remarks

If the device is not capable of signal inversion or if a previous route reserved the inversion circuitry in an incompatible configuration, attempting to invert the signal causes an error.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_singlepoint.htm language=enus -->
## TOPIC 00630: SinglePoint Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_singlepoint.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_singlepoint.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SinglePoint Class

### SinglePoint Class

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class SinglePoint : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class SinglePoint
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The SinglePoint type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | ConvertLateErrorsToWarnings | Specifies if WaitForNextSampleClock(Double), reading from the task, and writing to the task convert late errors to warnings. NI-DAQmx returns no late warnings or errors until the number of warmup iterations you specify with NumberOfWarmupIterations execute. |
|  | NumberOfWarmupIterations | Specifies the number of loop iterations that must occur before WaitForNextSampleClock(Double) and reading from the task return any late warnings or errors. The system needs a number of iterations to stabilize. During this period, a large amount of jitter occurs, potentially causing reads and writes to be late. The default number of warmup iterations is 100. Specify a larger number if needed to stabilize the system. |
|  | ReportMissedSamples | Specifies whether reading from the task returns lateness errors or warnings when it detects missed Sample Clock pulses. This setting does not affect WaitForNextSampleClock(Double). Set this property to for applications that need to detect lateness without using WaitForNextSampleClock(Double). |
|  | WaitForNextSampleClockWaitMode | Specifies how WaitForNextSampleClock(Double) waits for the next Sample Clock pulse. |
|  | WriteRecoveryMode | Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WaitForNextSampleClock | Waits until the next pulse of the sample clock occurs, with a timeout value of 10 seconds. |
|  | WaitForNextSampleClock(Double) | Waits until the next pulse of the sample clock occurs. |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttrigger.htm language=enus -->
## TOPIC 00631: StartTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTrigger Class

### StartTrigger Class

how the task begins measurement or generation

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class StartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class StartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The StartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AnalogEdge | Gets the AnalogEdgeStartTrigger. |
|  | AnalogMultiEdge | Gets the AnalogMultiEdgeStartTrigger. |
|  | AnalogWindow | Gets the AnalogWindowStartTrigger. |
|  | Delay | Specifies an amount of time to wait after the Start Trigger is received before acquiring or generating the first sample. This value is in the units you specify with DelayUnits. |
|  | DelayUnits | Specifies the units of Delay. |
|  | DigitalEdge | Gets the DigitalEdgeStartTrigger. |
|  | DigitalPattern | Gets the DigitalPatternStartTrigger. |
|  | MaximumNumberOfTriggersToDetect | Specifies the maximum number of times the task will detect a start trigger during the task. The number of times a trigger is detected and acted upon by the module may be less than the specified amount if the task stops early because of trigger/retrigger window expiration. Specifying the Maximum Number of Triggers to Detect to be 0 causes the driver to automatically set this value to the maximum possible number of triggers detectable by the device and configuration combination. Note: The number of detected triggers may be less than number of trigger events occurring, because the devices were unable to respond to the trigger. |
|  | Retriggerable | Specifies whether a finite task resets and waits for another Start Trigger after the task completes. When you set this property to , the device performs a finite acquisition or generation each time the Start Trigger occurs until the task stops. The device ignores a trigger if it is in the process of acquiring or generating signals. |
|  | RetriggerWindow | Specifies the period of time in seconds after each trigger during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples that it already started. Ensure the period of time specified covers the entire time span desired for retrigger detection to avoid missed triggers. Specifying a Retrigger Window of -1 causes the window to be infinite. |
|  | Terminal | Indicates the name of the internal Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
|  | Time | Gets the TimeStartTrigger. |
|  | Timestamp | Gets the start trigger timestamp. |
|  | TimestampEnable | Specifies whether the start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
|  | TimestampTimescale | Specifies the start trigger timestamp timescale. |
|  | TriggerWindow | Specifies the period of time in seconds after the task starts during which the device may trigger. Once the window has expired, the device stops detecting triggers, and the task will finish after the device finishes acquiring post-trigger samples for any triggers detected. If no triggers are detected during the entire period, then no data will be returned. Ensure the period of time specified covers the entire time span desired for trigger detection to avoid missed triggers. Specifying a Trigger Window of -1 causes the window to be infinite. |
|  | Type | Specifies the type of trigger to use to start a task. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | ConfigureAnalogEdgeTrigger | Configures the task to start acquiring or generating samples when an analog signal crosses the level you specify. |
|  | ConfigureAnalogMultiEdgeTrigger | Configures the task to start acquiring or generating samples when any of the configured analog signals cross the respective levels you specify. |
|  | ConfigureAnalogWindowTrigger | Configures the task to start acquiring or generating samples when an analog signal enters or leaves a range you specify. |
|  | ConfigureDigitalEdgeTrigger | Configures the task to start acquiring or generating samples on a rising or falling edge of a digital signal. |
|  | ConfigureDigitalPatternTrigger | Configures the task to start acquiring or generating samples when a digital pattern is matched. |
|  | ConfigureNone | Configures the task to start acquiring or generating samples immediately upon starting the task. |
|  | ConfigureTimeTrigger | Configures the task to start acquiring or generating samples at a the specified triggerTime. |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggerdelayunits.htm language=enus -->
## TOPIC 00632: StartTriggerDelayUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggerdelayunits.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggerdelayunits.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTriggerDelayUnits Enumeration

### StartTriggerDelayUnits Enumeration

Delay

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum StartTriggerDelayUnits
```

```text
Public Enumeration StartTriggerDelayUnits
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | SampleClockPeriods | 10286 | Complete periods of the Sample Clock. |
|  | Seconds | 10364 | Seconds. |
|  | Ticks | 10304 | Timebase ticks. |

##### Remarks

Delay

DelayUnits

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggerpulsepolarity.htm language=enus -->
## TOPIC 00633: StartTriggerPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggerpulsepolarity.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggerpulsepolarity.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTriggerPulsePolarity Enumeration

### StartTriggerPulsePolarity Enumeration

Specifies the polarity of the exported Start Trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum StartTriggerPulsePolarity
```

```text
Public Enumeration StartTriggerPulsePolarity
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | ActiveHigh | 10095 | High state is the active state. |
|  | ActiveLow | 10096 | Low state is the active state. |

##### Remarks

StartTriggerPulsePolarity

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggertimestamptimescale.htm language=enus -->
## TOPIC 00634: StartTriggerTimestampTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggertimestamptimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggertimestamptimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTriggerTimestampTimescale Enumeration

### StartTriggerTimestampTimescale Enumeration

Specifies the start trigger timestamp timescale.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum StartTriggerTimestampTimescale
```

```text
Public Enumeration StartTriggerTimestampTimescale
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HostTime | 16126 | Use the host device. |
|  | IODeviceTime | 16127 | Use the I/O device. |

##### Remarks

TimestampTimescale

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggertype.htm language=enus -->
## TOPIC 00635: StartTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggertype.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_starttriggertype.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

StartTriggerType Enumeration

### StartTriggerType Enumeration

type

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum StartTriggerType
```

```text
Public Enumeration StartTriggerType
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AnalogEdge | 10099 | Trigger when an analog signal signal crosses a threshold. |
|  | AnalogMultiEdge | 16108 | Trigger when any of the configured analog signals cross their respective thresholds. |
|  | DigitalEdge | 10150 | Trigger on the rising or falling edge of a digital signal. |
|  | DigitalPattern | 10398 | Trigger when digital physical channels match a digital pattern. |
|  | AnalogWindow | 10103 | Trigger when an analog signal enters or leaves a range of values. The range is in the units of the measurement. |
|  | Time | 15996 | Trigger when a specified time is reached. |
|  | None | 10230 | Disable triggering for the task. |

##### Remarks

type

Type

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switch.htm language=enus -->
## TOPIC 00636: Switch Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switch.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switch.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Switch Class

### Switch Class

**Note: This API is now obsolete.**

Encapsulates a switch device and contains properties and methods that operate on switch devices outside the context of a task.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This type is obsolete.")]
public class Switch : MarshalByRefObject
```

```text
<ObsoleteAttribute("This type is obsolete.")>
Public Class Switch
	Inherits MarshalByRefObject
```

The Switch type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AutoConnectAnalogBus | Specifies if NI-DAQmx routes multiplexed channels to the analog bus backplane. Only the SCXI-1127 and SCXI-1128 support this property. |
|  | IsSettled | Indicates when SettlingTime has expired. |
|  | NumberOfColumns | Gets the number of columns on a device in a matrix switch topology. This value is always 1 if the device is in a mux topology. |
|  | NumberOfRelays | Indicates the number of relays on the device. This value matches the number of relay names in RelayList. |
|  | NumberOfRows | Indicates the number of rows on a device in a matrix switch topology. Indicates the number of multiplexed channels on a device in a mux topology. |
|  | NumberOfSwitchChannels | Indicates the number of switch channels for the current topology of the device. This value matches the number of channel names in SwitchChannelList. |
|  | PowerDownLatchingRelaysAfterSettling | Specifies if WaitForSettling powers down latching relays after waiting for the device to settle. |
|  | RelayList | Indicates a comma-delimited list of relay names. |
|  | SettlingTime | Specifies in seconds the amount of time to wait for the switch to settle (or debounce). NI-DAQmx adds this time to the settling time of the motherboard. Modify this property only if the switch does not settle within the settling time of the motherboard. Refer to device documentation for supported settling times. |
|  | SupportedTopologies | Gets an array of the names of all switch topologies supported by this switch device. |
|  | SwitchChannelList | Indicates a comma-delimited list of channel names for the current topology of the device. |
|  | Temperature | Indicates the current temperature as read by the Switch module in degrees Celsius. Refer to your device documentation for more information. |
|  | Topology | Indicates the current topology of the device. This value is one of the topology options in SetTopologyAndReset(String). |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | SetTopologyAndReset | Resets a switch device and sets its topology. |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |
|  | WaitForSettling | Waits for the settling time on the device to expire. |

Top

##### Remarks

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchchannel.htm language=enus -->
## TOPIC 00637: SwitchChannel Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchchannel.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchchannel.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannel Class

### SwitchChannel Class

**Note: This API is now obsolete.**

Encapsulates a channel on a switch device and contains properties and methods that operate on switch channels outside the context of a task. This class also defines the intended use of particular switch channels in tasks.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This type is obsolete.")]
public class SwitchChannel : MarshalByRefObject, 
	IDisposable
```

```text
<ObsoleteAttribute("This type is obsolete.")>
Public Class SwitchChannel
	Inherits MarshalByRefObject
	Implements IDisposable
```

The SwitchChannel type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AnalogBusSharingEnable | Specifies whether to enable sharing of an analog bus line so that multiple switch devices can connect to it simultaneously. For each device that will share the analog bus line, set this property to to enable sharing on the channel that connects to the analog bus line. Analog bus sharing is disabled by default. |
|  | Bandwidth | Indicates in Hertz the maximum frequency of a signal that can pass through the switch without significant deterioration. |
|  | Impedance | Indicates in ohms the switch impedance. This value is important in the RF domain and should match the impedance of the sources and loads. |
|  | MaxACCarryCurrent | Indicates in amperes the maximum AC current that the device can carry. |
|  | MaxACCarryPower | Indicates in watts the maximum AC power that the device can carry. |
|  | MaxACSwitchCurrent | Indicates in amperes the maximum AC current that the device can switch. This current is always against an RMS voltage level. |
|  | MaxACSwitchPower | Indicates in watts the maximum AC power that the device can switch. |
|  | MaxACVoltage | Indicates in volts the maximum AC RMS voltage that the device can switch. |
|  | MaxDCCarryCurrent | Indicates in amperes the maximum DC current that the device can carry. |
|  | MaxDCCarryPower | Indicates in watts the maximum DC power that the device can carry. |
|  | MaxDCSwitchCurrent | Indicates in amperes the maximum DC current that the device can switch. This current is always against a DC voltage level. |
|  | MaxDCSwitchPower | Indicates in watts the maximum DC power that the device can switch. |
|  | MaxDCVoltage | Indicates in volts the maximum DC voltage that the device can switch. |
|  | Usage | Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example. |
|  | WireMode | Indicates the number of wires that the channel switches. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Dispose | Releases all resources used by SwitchChannel. |
|  | Dispose(Boolean) | Releases the managed and unmanaged resources used by SwitchChannel or optionally releases only the unmanaged resources. |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

LoadSwitchChannel(String)

Local

DaqSystem

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchchannelusage.htm language=enus -->
## TOPIC 00638: SwitchChannelUsage Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchchannelusage.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchchannelusage.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchChannelUsage Enumeration

### SwitchChannelUsage Enumeration

**Note: This API is now obsolete.**

Specifies how you can use the channel. Using this property acts as a safety mechanism to prevent you from connecting two source channels, for example.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum SwitchChannelUsage
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration SwitchChannelUsage
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Source | 10439 | You can use the channel only as an input for a signal. |
|  | Load | 10440 | You can use the channel only as the output for a signal passing through the switch. |
|  | ReservedForRouting | 10441 | You can use the channel only to complete routes within a switch. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchpathstatus.htm language=enus -->
## TOPIC 00639: SwitchPathStatus Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchpathstatus.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchpathstatus.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchPathStatus Enumeration

### SwitchPathStatus Enumeration

**Note: This API is now obsolete.**

Specifies the status of the requested path.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum SwitchPathStatus
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration SwitchPathStatus
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | PathAvailable | 10431 | A path is available between the channels. |
|  | PathAlreadyExists | 10432 | The channels are already connected. |
|  | PathUnsupported | 10433 | No path is available between the channels. You might need to reserve more channels for routing to create an available path. |
|  | ChannelInUse | 10434 | The path between the two endpoints is unavailable because another connection is already using a channel needed for routing. |
|  | SourceChannelConflict | 10435 | No path is available between the two channels because connecting the channels would directly or indirectly connect two source channels. |
|  | ChannelReservedForRouting | 10436 | One of the endpoint channels is reserved for routing. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchscanbreakmode.htm language=enus -->
## TOPIC 00640: SwitchScanBreakMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchscanbreakmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_switchscanbreakmode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

SwitchScanBreakMode Enumeration

### SwitchScanBreakMode Enumeration

**Note: This API is now obsolete.**

Specifies the action to take between each entry in a scan list.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[ObsoleteAttribute("This enum is obsolete.")]
public enum SwitchScanBreakMode
```

```text
<ObsoleteAttribute("This enum is obsolete.")>
Public Enumeration SwitchScanBreakMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | NoAction | 10227 | When advancing to the next entry in the scan list, leave all previous connections intact. |
|  | BreakBeforeMake | 10110 | When advancing to the next entry in the scan list, disconnect all previous connections before making any new connections. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_terminalconfigurationtypes.htm language=enus -->
## TOPIC 00641: TerminalConfigurationTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_terminalconfigurationtypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_terminalconfigurationtypes.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TerminalConfigurationTypes Enumeration

### TerminalConfigurationTypes Enumeration

Specifies a set of terminal configuration types a physical channel may support.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum TerminalConfigurationTypes
```

```text
<FlagsAttribute>
Public Enumeration TerminalConfigurationTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | Physical channel does not support any terminal configuration types. |
|  | Rse | 1 | Referenced Single-Ended. |
|  | Nrse | 2 | Non-Referenced Single-Ended. |
|  | Differential | 4 | Differential. |
|  | Pseudodifferential | 8 | Pseudodifferential. |

##### Remarks

Specifies a set of terminal configuration types a physical channel may support.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timearmstarttriggertimescale.htm language=enus -->
## TOPIC 00642: TimeArmStartTriggerTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timearmstarttriggertimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timearmstarttriggertimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimeArmStartTriggerTimescale Enumeration

### TimeArmStartTriggerTimescale Enumeration

Specifies the timescale to be used for timestamps used in an arm start time trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum TimeArmStartTriggerTimescale
```

```text
Public Enumeration TimeArmStartTriggerTimescale
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HostTime | 16126 | Use the host device. |
|  | IODeviceTime | 16127 | Use the I/O device. |

##### Remarks

Timescale

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestampevent.htm language=enus -->
## TOPIC 00643: TimestampEvent Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestampevent.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestampevent.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimestampEvent Enumeration

### TimestampEvent Enumeration

Represents the type of timestamp event.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum TimestampEvent
```

```text
Public Enumeration TimestampEvent
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | StartTrigger | 12491 | Start trigger timestamp. |
|  | ReferenceTrigger | 12490 | Reference trigger timestamp. |
|  | ArmStartTrigger | 14641 | Arm start trigger timestamp. |
|  | FirstSample | 16130 | First sample timestamp. |

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestarttrigger.htm language=enus -->
## TOPIC 00644: TimeStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestarttrigger.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestarttrigger.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimeStartTrigger Class

### TimeStartTrigger Class

Provides properties for configuring time start triggers.

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class TimeStartTrigger : MarshalByRefObject, 
	IFilteredTypeDescriptor
```

```text
Public Class TimeStartTrigger
	Inherits MarshalByRefObject
	Implements IFilteredTypeDescriptor
```

The TimeStartTrigger type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | Timescale | Specifies the timescale to be used for timestamps used in a time trigger. |
|  | TriggerTime | Gets or sets when to trigger the start trigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Remarks

Time-Based Features for Network-Synchronized Devices

| Tip |
| --- |
| Example applications are located in the Public Documents\\National Instruments\\NI-DAQ\\Examples\\DotNET4.x directory or in the Start menu at National InstrumentsNI-DAQmxNI-DAQmx Examples. |

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestarttriggertimescale.htm language=enus -->
## TOPIC 00645: TimeStartTriggerTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestarttriggertimescale.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_timestarttriggertimescale.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TimeStartTriggerTimescale Enumeration

### TimeStartTriggerTimescale Enumeration

Specifies the timescale to be used for timestamps used in a time trigger.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum TimeStartTriggerTimescale
```

```text
Public Enumeration TimeStartTriggerTimescale
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | HostTime | 16126 | Use the host device. |
|  | IODeviceTime | 16127 | Use the I/O device. |

##### Remarks

Timescale

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_triggers.htm language=enus -->
## TOPIC 00646: Triggers Class

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_triggers.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_triggers.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

Triggers Class

### Triggers Class

triggers

Task

##### Inheritance Hierarchy

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public class Triggers : MarshalByRefObject
```

```text
Public Class Triggers
	Inherits MarshalByRefObject
```

The Triggers type exposes the following members.

##### Properties

|  | Name | Description |
| --- | --- | --- |
|  | AdvanceTrigger | Gets the AdvanceTrigger. |
|  | ArmStartTrigger | Gets the ArmStartTrigger. |
|  | HandshakeTrigger | Gets the HandshakeTrigger. |
|  | PauseTrigger | Gets the PauseTrigger. |
|  | ReferenceTrigger | Gets the ReferenceTrigger. |
|  | StartTrigger | Gets the StartTrigger. |
|  | SynchronizationType | Specifies the role of the device in a synchronized system. Setting this value to Master or Slave enables trigger skew correction. If you enable trigger skew correction, set this property to Master on only one device, and set this property to Slave on the other devices. |
|  | WatchdogExpirationTrigger | Gets the WatchdogExpirationTrigger. |

Top

##### Methods

|  | Name | Description |
| --- | --- | --- |
|  | CreateObjRef | Creates an object that contains all the relevant information required to generate a proxy used to communicate with a remote object. (Inherited from MarshalByRefObject.) |
|  | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object.) |
|  | Finalize | Allows an object to try to free resources and perform other cleanup operations before it is reclaimed by garbage collection. (Inherited from Object.) |
|  | GetHashCode | Serves as the default hash function. (Inherited from Object.) |
|  | GetLifetimeService | Retrieves the current lifetime service object that controls the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | GetType | Gets the Type of the current instance. (Inherited from Object.) |
|  | InitializeLifetimeService | Obtains a lifetime service object to control the lifetime policy for this instance. (Inherited from MarshalByRefObject.) |
|  | MemberwiseClone | Creates a shallow copy of the current Object. (Inherited from Object.) |
|  | MemberwiseClone(Boolean) | Creates a shallow copy of the current MarshalByRefObject object. (Inherited from MarshalByRefObject.) |
|  | ToString | Returns a string representation of the object. (Overrides ObjectToString.) |

Top

##### Thread Safety

static

Shared

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_triggerusagetypes.htm language=enus -->
## TOPIC 00647: TriggerUsageTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_triggerusagetypes.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_triggerusagetypes.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

TriggerUsageTypes Enumeration

### TriggerUsageTypes Enumeration

Specifies a set of trigger types a device may support.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
[FlagsAttribute]
public enum TriggerUsageTypes
```

```text
<FlagsAttribute>
Public Enumeration TriggerUsageTypes
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | None | 0 | Device supports no trigger types. |
|  | Advance | 1 | Device supports advance triggers. |
|  | Pause | 2 | Device supports pause triggers. |
|  | Reference | 4 | Device supports reference triggers. |
|  | Start | 8 | Device supports start triggers. |
|  | Handshake | 16 | Device supports handshake triggers. |
|  | ArmStart | 32 | Device supports arm start triggers. |

##### Remarks

Specifies a set of trigger types a device may support.

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writerecoverymode.htm language=enus -->
## TOPIC 00648: WriteRecoveryMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writerecoverymode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writerecoverymode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

WriteRecoveryMode Enumeration

### WriteRecoveryMode Enumeration

Specifies how NI-DAQmx attempts to recover after missing a Sample Clock pulse when performing counter writes.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum WriteRecoveryMode
```

```text
Public Enumeration WriteRecoveryMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | WaitForInterrupt | 12523 | Attempt to recover when the system receives an interrupt service request. This mode is the most CPU efficient and best suited for recovery at lower pulse train frequencies. |
|  | Poll | 12524 | Repeatedly attempt to recover as fast as possible. This mode has the highest probability of recovery success at the expense of CPU efficiency. |

##### Remarks

WriteRecoveryMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writeregenerationmode.htm language=enus -->
## TOPIC 00649: WriteRegenerationMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writeregenerationmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writeregenerationmode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

WriteRegenerationMode Enumeration

### WriteRegenerationMode Enumeration

Specifies whether to allow NI-DAQmx to generate the same data multiple times.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum WriteRegenerationMode
```

```text
Public Enumeration WriteRegenerationMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | AllowRegeneration | 10097 | Allow NI-DAQmx to regenerate samples that the device previously generated. When you choose this value, the write marker returns to the beginning of the buffer after the device generates all samples currently in the buffer. |
|  | DoNotAllowRegeneration | 10158 | Do not allow NI-DAQmx to regenerate samples the device previously generated. When you choose this value, NI-DAQmx waits for you to write more samples to the buffer or until the timeout expires. |

##### Remarks

WriteRegenerationMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writerelativeto.htm language=enus -->
## TOPIC 00650: WriteRelativeTo Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writerelativeto.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writerelativeto.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

WriteRelativeTo Enumeration

### WriteRelativeTo Enumeration

WriteOffset

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum WriteRelativeTo
```

```text
Public Enumeration WriteRelativeTo
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | FirstSample | 10424 | Write samples relative to the first sample. |
|  | CurrentWritePosition | 10430 | Write samples relative to the current position in the buffer. |

##### Remarks

WriteOffset

WriteRelativeTo

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.

<!--NI_TOPIC bundle=ni-daqmx-net-framework-45-api-ref path=ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writewaitmode.htm language=enus -->
## TOPIC 00651: WriteWaitMode Enumeration

- bundle_id: `ni-daqmx-net-framework-45-api-ref`
- source_path: `ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writewaitmode.htm`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-45-api-ref/raw/resource/enus/ninetdaqmxfx45ref/html/t_nationalinstruments_daqmx_writewaitmode.htm
- document_id: `ni-daqmx-net-framework-45-api-ref`
- page_type: `leaf`
- content_type: ``

WriteWaitMode Enumeration

### WriteWaitMode Enumeration

Specifies how writing to the task waits for space to become available in the buffer.

Namespace:

NationalInstruments.DAQmx

Assembly:

##### Syntax

C#

VB

```text
public enum WriteWaitMode
```

```text
Public Enumeration WriteWaitMode
```

##### Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Poll | 12524 | Repeatedly check for available buffer space as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency. |
|  | Yield | 12525 | Repeatedly check for available buffer space, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency. |
|  | Sleep | 12547 | Check for available buffer space once per the amount of time specified in WriteSleepTime. |

##### Remarks

WriteWaitMode

##### See Also

###### Reference

NationalInstruments.DAQmx Namespace

Copyright © National Instruments Corporation. All Rights Reserved.
