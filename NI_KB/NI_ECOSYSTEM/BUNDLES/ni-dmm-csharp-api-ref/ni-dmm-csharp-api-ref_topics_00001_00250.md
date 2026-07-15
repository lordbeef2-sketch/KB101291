# NI DOCUMENT BUNDLE: ni-dmm-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dmm-csharp-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-DMM C# .NET API Reference

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-DMM C# .NET API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Discussion Forums
- NI Learning Center
- NI-DMM User Manual

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmm4022configurationmode.html language=enus -->
## TOPIC 00002: Dmm4022ConfigurationMode Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmm4022configurationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmm4022configurationmode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the operating mode of the NI 4022. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum Dmm4022ConfigurationModeRemarksBy default, this is set to Guard.For the NI 4022 only. MembersNameValueDescriptionGuard0Enables the internal amplifier to be a unity gain buffer for pe

### Dmm4022ConfigurationMode Enumeration

Specifies the operating mode of the NI 4022.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum Dmm4022ConfigurationMode

#### Remarks

By default, this is set to Guard.

For the NI 4022 only.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Guard | 0 | Enables the internal amplifier to be a unity gain buffer for performing a 6-wire guarded measurement. This is the default operating mode. |
| Current100NanoAmp | 2 | Enables the low current amplifier and applies a gain of 1E8 V/A. |
| Current10MicroAmp | 3 | Enables the low current amplifier and applies a gain of 1E6 V/A. |
| Current1MilliAmp | 7 | Enables the low current amplifier and applies a gain of 1E4 V/A. |
| DisconnectFromAnalogGround | 8 | Disconnects the +INPUT (positive input terminal) from the analog ground. When one of the current amplification ranges is selected, the +INPUT (positive input terminal) of the amplifier is tied to the analog ground by default. You can override this default configuration by selecting this option to disconnect the +INPUT, and allow the user to provide an external reference. Calling one of the current amplification ranges after using this reconnects the +INPUT to analog ground. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmac-configurebandwidth__double-double.html language=enus -->
## TOPIC 00003: ConfigureBandwidth(double, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmac-configurebandwidth__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmac-configurebandwidth__double-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures FrequencyMin and FrequencyMax for AC measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureBandwidth(double minimumFrequency, double maximumFrequency)ParametersNameTypeDescriptionminimumFrequencydoubleThe minimum expected frequency component of th

### ConfigureBandwidth(double, double)

Configures [FrequencyMin](nationalinstruments-modularinstruments-nidmm-dmmac-frequencymin.html) and [FrequencyMax](nationalinstruments-modularinstruments-nidmm-dmmac-frequencymax.html) for AC measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureBandwidth(double minimumFrequency, double maximumFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minimumFrequency | double | The minimum expected frequency component of the input signal in hertz. |
| maximumFrequency | double | The maximum expected frequency component of the input signal in hertz within the device limits. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is not positive. |

#### See Also

- FrequencyMax
- FrequencyMin

Parent topic:

DmmAC Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmac-frequencymax.html language=enus -->
## TOPIC 00004: FrequencyMax

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmac-frequencymax.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmac-frequencymax.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum frequency component of the input signal for AC measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double FrequencyMax { get; set; }RemarksThe valid range is 1 Hz–300 kHz for the NI 4070/4071/4072, 10 Hz–100 kHz for the NI 4065, and 20 Hz–25 kHz

### FrequencyMax

Gets or sets the maximum frequency component of the input signal for AC measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double FrequencyMax { get; set; }

#### Remarks

The valid range is 1 Hz–300 kHz for the NI 4070/4071/4072, 10 Hz–100 kHz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.

This property is used only for error checking. This property verifies that the value of this parameter is less than the maximum frequency of the device. This property affects the DMM only when you set the [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html) to AC measurements.

#### See Also

- DmmMeasurementFunction

Parent topic:

DmmAC Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmac-frequencymin.html language=enus -->
## TOPIC 00005: FrequencyMin

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmac-frequencymin.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmac-frequencymin.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the minimum frequency component of the input signal for AC measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double FrequencyMin { get; set; }RemarksThe valid range is 1 Hz–300 kHz for the NI 4070/4071/4072, 10 Hz–100 kHz for the NI 4065, and 20 Hz–25 kHz

### FrequencyMin

Gets or sets the minimum frequency component of the input signal for AC measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double FrequencyMin { get; set; }

#### Remarks

The valid range is 1 Hz–300 kHz for the NI 4070/4071/4072, 10 Hz–100 kHz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.

This property affects the DMM only when you set the [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html) to AC measurements.

#### See Also

- DmmMeasurementFunction

Parent topic:

DmmAC Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmac.html language=enus -->
## TOPIC 00006: DmmAC Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmac.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmac.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures properties applicable only to AC measurements. Derives fromDmmSubObjectIIviDmmACSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmAC : DmmSubObject, IIviDmmACRemarksUse DmmAC to configure properties applicable only to AC measurements, such as FrequencyMax and Fr

### DmmAC Class

Configures properties applicable only to AC measurements.

#### Derives from

- DmmSubObject
- IIviDmmAC

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmAC : DmmSubObject, IIviDmmAC

#### Remarks

DmmAC

FrequencyMax

FrequencyMin

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| FrequencyMax | Gets or sets the maximum frequency component of the input signal for AC measurements. |
| FrequencyMin | Gets or sets the minimum frequency component of the input signal for AC measurements. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureBandwidth(double, double) | Configures FrequencyMin and FrequencyMax for AC measurements. |

#### See Also

- NationalInstruments.ModularInstruments.NIDmm.DmmAC.ConfigureBandwidth

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmacquisitionstatus.html language=enus -->
## TOPIC 00007: DmmAcquisitionStatus Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmacquisitionstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmacquisitionstatus.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allows for storing and retrieving the acquisition status. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmAcquisitionStatusMembersNameValueDescriptionRunning0The acquisition is in progress. FinishedWithBacklog1The acquisition has finished, with a backlog. The backlog spec

### DmmAcquisitionStatus Enumeration

Allows for storing and retrieving the acquisition status.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmAcquisitionStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Running | 0 | The acquisition is in progress. |
| FinishedWithBacklog | 1 | The acquisition has finished, with a backlog. The backlog specifies the number of measurements available to be read. |
| FinishedWithNoBacklog | 2 | The acquisition has finished, with no backlog. The backlog specifies the number of measurements available to be read. |
| Paused | 3 | The acquisition is paused. |
| NoAcquisitionInProgress | 4 | No acquisition is in progress. |

#### See Also

- ReadStatus

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadccalibration.html language=enus -->
## TOPIC 00008: DmmAdcCalibration Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadccalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadccalibration.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ADC calibration. Use DmmAdcCalibration for setting AdcCalibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmAdcCalibrationRemarksFor more information, refer to the ADC Calibration topic in the NI Digital Multimeters Help. MembersNameValueDescriptionAu

### DmmAdcCalibration Enumeration

Specifies the ADC calibration. Use DmmAdcCalibration for setting [AdcCalibration](nationalinstruments-modularinstruments-nidmm-dmmadvanced-adccalibration.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmAdcCalibration

#### Remarks

For more information, refer to the [ADC Calibration](/csh?context=nidmm_dmm_adc_calibration) topic in the *NI Digital Multimeters Help*.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | -1 | The DMM enables or disables ADC calibration. |
| Off | 0 | The DMM does not compensate for changes to the gain. |
| On | 1 | The DMM measures an internal reference to calculate the correct gain for the measurement. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-adccalibration.html language=enus -->
## TOPIC 00009: AdcCalibration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-adccalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-adccalibration.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the ADC calibration mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmAdcCalibration AdcCalibration { get; set; }RemarksFor the NI 4070/4071/4072 only. AdcCalibration allows the DMM to compensate for gain drift since the last external calibration or self-calib

### AdcCalibration

Gets or sets the ADC calibration mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmAdcCalibration](nationalinstruments-modularinstruments-nidmm-dmmadccalibration.html) AdcCalibration { get; set; }

#### Remarks

For the NI 4070/4071/4072 only.

AdcCalibration allows the DMM to compensate for gain drift since the last external calibration or self-calibration. When AdcCalibration is **ON**, the DMM measures an internal reference to calculate the correct gain for the measurement. When AdcCalibration is **OFF**, the DMM does not compensate for changes to the gain. For more information, refer to the [ADC Calibration](/csh?context=nidmm_dmm_adc_calibration) topic in the *NI Digital Multimeters Help*.

The default is [Auto](nationalinstruments-modularinstruments-nidmm-dmmadccalibration.html).

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetime.html language=enus -->
## TOPIC 00010: ApertureTime

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetime.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the measurement aperture time for the current configuration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double ApertureTime { get; set; }RemarksOn the NI 4070/4071/4072, the minimum aperture time is 8.89 microseconds (µs), and the maximum aperture time is 149 se

### ApertureTime

Gets or sets the measurement aperture time for the current configuration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double ApertureTime { get; set; }

#### Remarks

On the NI 4070/4071/4072, the minimum aperture time is 8.89 microseconds (µs), and the maximum aperture time is 149 seconds (s). Any number of powerline cycles (PLCs) within the minimum and maximum ranges is allowed on the NI 4070/4071/4072.

On the NI 4065, the minimum aperture time is 333 µs, and the maximum aperture time is 78.2 s. If setting the number of averages directly, the total measurement time is aperture time multiplied by the number of averages, which must be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs, or multiples of 1.11 ms - for example 1.11 ms, 2.22 ms, 3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples of 1.11 ms, the value will be coerced up to the next supported aperture time.

On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed are 1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50 Hz, the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.

To override the default aperture, set this property to the desired aperture time after calling [Configure](nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-double-double.html). To return to the default, set this property to -1. For more information, refer to the [Aperture Time](/csh?context=nidmm_dmm_aperture_time) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetimeunits.html language=enus -->
## TOPIC 00011: ApertureTimeUnits

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetimeunits.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the unit of measurement used for aperture time for the current configuration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmApertureTimeUnits ApertureTimeUnits { get; set; }RemarksThe NI 4060 does not support an aperture time set in seconds. The default value is

### ApertureTimeUnits

Gets or sets the unit of measurement used for aperture time for the current configuration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmApertureTimeUnits](nationalinstruments-modularinstruments-nidmm-dmmaperturetimeunits.html) ApertureTimeUnits { get; set; }

#### Remarks

The NI 4060 does not support an aperture time set in seconds.

The default value is [PowerLineCycles](nationalinstruments-modularinstruments-nidmm-dmmaperturetimeunits.html).

#### See Also

- DmmApertureTimeUnits

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-autozero.html language=enus -->
## TOPIC 00012: AutoZero

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-autozero.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-autozero.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the AutoZero mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmAuto AutoZero { get; set; }RemarksConfigures the DMM for AutoZero. When AutoZero is ON, the DMM internally disconnects the input signal and takes a zero reading. It then subtracts the zero reading

### AutoZero

Gets or sets the AutoZero mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmAuto](nationalinstruments-modularinstruments-nidmm-dmmauto.html) AutoZero { get; set; }

#### Remarks

Note

The NI 4050 is not supported.

For more information, refer to the [Auto Zero](/csh?context=nidmm_dmm_auto_zero) topic in the *NI Digital Multimeters Help*.

The default value is Auto.

#### See Also

- DmmAuto

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-dcnoiserejection.html language=enus -->
## TOPIC 00013: DCNoiseRejection

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-dcnoiserejection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-dcnoiserejection.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the DC noise rejection mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDCNoiseRejection DCNoiseRejection { get; set; }RemarksBy default, DCNoiseRejection is set to Auto (–1). When the value is Auto, the driver selects the DCNoiseRejection setting based on th

### DCNoiseRejection

Gets or sets the DC noise rejection mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmDCNoiseRejection](nationalinstruments-modularinstruments-nidmm-dmmdcnoiserejection.html) DCNoiseRejection { get; set; }

#### Remarks

DCNoiseRejection

Auto

DCNoiseRejection

Note

The NI 4050 and NI 4060 are not supported.

For more information, refer to the [DC Noise Rejection](/csh?context=nidmm_dmm_dc_noise_rejection) topic in the *NI Digital Multimeters Help*.

The default value is **Auto**.

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-numberofaverages.html language=enus -->
## TOPIC 00014: NumberOfAverages

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-numberofaverages.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-numberofaverages.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of averages to perform in a measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int NumberOfAverages { get; set; }RemarksThe default is 1. For the NI 4070/4071/4072, applies only when the aperture time is not set to Auto, and AutoZero is On. The N

### NumberOfAverages

Gets or sets the number of averages to perform in a measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int NumberOfAverages { get; set; }

#### Remarks

The default is 1.

Auto

AutoZero

On

Note

The NI 4050 and NI 4060 are not supported.

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-offsetcompensatedohm.html language=enus -->
## TOPIC 00015: OffsetCompensatedOhm

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-offsetcompensatedohm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-offsetcompensatedohm.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the compensated ohms are offset. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmOffsetCompensatedOhm OffsetCompensatedOhm { get; set; }RemarksFor NI 4070/4071/4072 only. The default value is Off. See AlsoDmmOffsetCompensatedOhm

### OffsetCompensatedOhm

Gets or sets whether the compensated ohms are offset.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmOffsetCompensatedOhm](nationalinstruments-modularinstruments-nidmm-dmmoffsetcompensatedohm.html) OffsetCompensatedOhm { get; set; }

#### Remarks

For NI 4070/4071/4072 only.

The default value is **Off**.

#### See Also

- DmmOffsetCompensatedOhm

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-powerlinefrequency.html language=enus -->
## TOPIC 00016: PowerlineFrequency

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-powerlinefrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-powerlinefrequency.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the powerline frequency. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double PowerlineFrequency { get; set; }RemarksWhen setting the ApertureTime, select the number of PLCs for the powerline frequency. For example, if the powerline frequency is 50 Hz (or 20 ms) an

### PowerlineFrequency

Gets or sets the powerline frequency.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double PowerlineFrequency { get; set; }

#### Remarks

When setting the [ApertureTime](nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetime.html), select the number of PLCs for the powerline frequency. For example, if the powerline frequency is 50 Hz (or 20 ms) and aperture time in PLCs is 5, then aperture time in seconds is 20 ms x 5 PLCs, or 100 ms. Similarly, if powerline frequency is 60 Hz (or 16.667 ms) and aperture time in PLCs is 6, then aperture time in seconds is 16.667 ms x 6 PLCs, or 100 ms.

After configuring powerline frequency, set the [ApertureTimeUnits](nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetimeunits.html) to PLCs. The NI 4050 and NI 4060 use this value to select an aperture time to reject powerline noise by selecting the appropriate internal sample clock and filter. The NI 4065 and NI 4070/4071/4072 use this value to select a timebase for setting the [ApertureTime](nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetime.html) property in powerline cycles (PLCs).

For more information, refer to the [niDMM_ConfigurePowerLineFrequency](/csh?context=nidmm_nidmmcref_function_configure_power_line_frequency) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-settletime.html language=enus -->
## TOPIC 00017: SettleTime

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-settletime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-settletime.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the settling time in seconds. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double SettleTime { get; set; }RemarksUse this property to override the default. To return to the default, set this property to Auto (–1). The NI 4050 and NI 4060 are not supported. For mor

### SettleTime

Gets or sets the settling time in seconds.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double SettleTime { get; set; }

#### Remarks

Auto

Note

The NI 4050 and NI 4060 are not supported.

Settling Time

NI Digital Multimeters Help

The default value is **Auto**.

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced-shuntvalue.html language=enus -->
## TOPIC 00018: ShuntValue

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced-shuntvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced-shuntvalue.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the shunt resistance value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double ShuntValue { get; set; }RemarksFor the NI 4050 only. The NI 4050 requires an external shunt resistor for current measurements. The shunt resistance in ohms.

### ShuntValue

Gets or sets the shunt resistance value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double ShuntValue { get; set; }

#### Remarks

Note

The NI 4050 requires an external shunt resistor for current measurements.

The shunt resistance in ohms.

Parent topic:

DmmAdvanced Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvanced.html language=enus -->
## TOPIC 00019: DmmAdvanced Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvanced.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures and obtains additional information concerning the instrument driver session. Derives fromDmmSubObjectIIviDmmAdvancedSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmAdvanced : DmmSubObject, IIviDmmAdvancedRemarksUse this class to configure and obtain additional

### DmmAdvanced Class

Configures and obtains additional information concerning the instrument driver session.

#### Derives from

- DmmSubObject
- IIviDmmAdvanced

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmAdvanced : DmmSubObject, IIviDmmAdvanced

#### Remarks

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AdcCalibration | Gets or sets the ADC calibration mode. |
| ApertureTime | Gets or sets the measurement aperture time for the current configuration. |
| ApertureTimeUnits | Gets or sets the unit of measurement used for aperture time for the current configuration. |
| AutoZero | Gets or sets the AutoZero mode. |
| DCNoiseRejection | Gets or sets the DC noise rejection mode. |
| NumberOfAverages | Gets or sets the number of averages to perform in a measurement. |
| OffsetCompensatedOhm | Gets or sets whether the compensated ohms are offset. |
| PowerlineFrequency | Gets or sets the powerline frequency. |
| SettleTime | Gets or sets the settling time in seconds. |
| ShuntValue | Gets or sets the shunt resistance value. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-dcbias.html language=enus -->
## TOPIC 00020: DCBias

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-dcbias.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-dcbias.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the available DC bias for capacitance measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDCBias DCBias { get; set; }RemarksFor NI 4072 only. When DCBias is On, the high potential appears on the HI terminal. Ensure that the component is polarized correct

### DCBias

Gets or sets the available DC bias for capacitance measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmDCBias](nationalinstruments-modularinstruments-nidmm-dmmdcbias.html) DCBias { get; set; }

#### Remarks

For NI 4072 only. When DCBias is **On**, the high potential appears on the HI terminal. Ensure that the component is polarized correctly by connecting the negative terminal of the component to the LO terminal.

The DC bias voltage is a fixed value and can only be turned on and off. The nominal voltage value is 0.45 V and can be used for any capacitance range. The default setting is off.

#### See Also

- DmmDCBias

Parent topic:

DmmAdvancedCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-lccalculationmodel.html language=enus -->
## TOPIC 00021: LCCalculationModel

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-lccalculationmodel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-lccalculationmodel.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of algorithm the measurement processing uses for capacitance and inductance measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmLCCalculationModel LCCalculationModel { get; set; }RemarksFor the NI 4072 only. The default value is Auto. See AlsoDm

### LCCalculationModel

Gets or sets the type of algorithm the measurement processing uses for capacitance and inductance measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmLCCalculationModel](nationalinstruments-modularinstruments-nidmm-dmmlccalculationmodel.html) LCCalculationModel { get; set; }

#### Remarks

For the NI 4072 only.

The default value is **Auto**.

#### See Also

- DmmLCCalculationModel

Parent topic:

DmmAdvancedCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-numberoflcmeasurementstoaverage.html language=enus -->
## TOPIC 00022: NumberOfLCMeasurementsToAverage

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-numberoflcmeasurementstoaverage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance-numberoflcmeasurementstoaverage.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of LC measurements that are averaged to produce one reading. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int NumberOfLCMeasurementsToAverage { get; set; }RemarksFor the NI 4072 only. The number of LC measurements that are averaged to produce one readin

### NumberOfLCMeasurementsToAverage

Gets or sets the number of LC measurements that are averaged to produce one reading.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int NumberOfLCMeasurementsToAverage { get; set; }

#### Remarks

For the NI 4072 only.

The number of LC measurements that are averaged to produce one reading.

Parent topic:

DmmAdvancedCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance.html language=enus -->
## TOPIC 00023: DmmAdvancedCapacitanceAndInductance Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides additional information specific to capacitance and inductance. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmAdvancedCapacitanceAndInductanceRemarksFor NI 4072 only. System.ObjectDisposedException is returned if the members are accessed after t

### DmmAdvancedCapacitanceAndInductance Class

Provides additional information specific to capacitance and inductance.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmAdvancedCapacitanceAndInductance

#### Remarks

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DCBias | Gets or sets the available DC bias for capacitance measurements. |
| LCCalculationModel | Gets or sets the type of algorithm the measurement processing uses for capacitance and inductance measurements. |
| NumberOfLCMeasurementsToAverage | Gets or sets the number of LC measurements that are averaged to produce one reading. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmaperturetimeunits.html language=enus -->
## TOPIC 00024: DmmApertureTimeUnits Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmaperturetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmaperturetimeunits.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit used when measuring aperture time. Use DmmApertureTimeUnits for setting ApertureTimeUnits. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmApertureTimeUnitsMembersNameValueDescriptionSeconds0Aperture time measured in seconds. PowerLineCycles1Aperture ti

### DmmApertureTimeUnits Enumeration

Specifies the unit used when measuring aperture time. Use DmmApertureTimeUnits for setting [ApertureTimeUnits](nationalinstruments-modularinstruments-nidmm-dmmadvanced-aperturetimeunits.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmApertureTimeUnits

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Seconds | 0 | Aperture time measured in seconds. |
| PowerLineCycles | 1 | Aperture time measured in powerline cycles. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmauto.html language=enus -->
## TOPIC 00025: DmmAuto Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmauto.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmauto.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies AutoZero, VoltageAutoRange, and AutoRange. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmAutoMembersNameValueDescriptionAuto-1The driver chooses the AutoZero setting based on the configured function and resolution. Off0Disables AutoZero. On1The DMM device inte

### DmmAuto Enumeration

Specifies [AutoZero](nationalinstruments-modularinstruments-nidmm-dmmadvanced-autozero.html), [VoltageAutoRange](nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorange.html), and [AutoRange](nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmAuto

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | -1 | The driver chooses the AutoZero setting based on the configured function and resolution. |
| Off | 0 | Disables AutoZero. |
| On | 1 | The DMM device internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading. |
| Once | 2 | The DMM device internally disconnects the input signal for the first measurement and takes a zero reading. It then subtracts the zero reading from the first reading and the following readings. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcablecompensationtype.html language=enus -->
## TOPIC 00026: DmmCableCompensationType Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcablecompensationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcablecompensationtype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmCableCompensationTypeRemarksFor the NI 4072 only. MembersNameValueDescriptionNone0No cable

### DmmCableCompensationType Enumeration

Specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmCableCompensationType

#### Remarks

For the NI 4072 only.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No cable compensation. |
| Open | 1 | Open cable compensation. |
| Short | 2 | Short cable compensation. |
| OpenAndShort | 3 | Open and short cable compensation. |

#### See Also

- CableCompensationType

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-externalcalibrationrecommendedinterval.html language=enus -->
## TOPIC 00027: ExternalCalibrationRecommendedInterval

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-externalcalibrationrecommendedinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-externalcalibrationrecommendedinterval.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the recommended interval between external recalibration in months. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic NationalInstruments.PrecisionTimeSpan ExternalCalibrationRecommendedInterval { get; }RemarksReturns the recommended interval between external recalibration in m

### ExternalCalibrationRecommendedInterval

Gets the recommended interval between external recalibration in months.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public NationalInstruments.PrecisionTimeSpan ExternalCalibrationRecommendedInterval { get; }

#### Remarks

Returns the recommended interval between external recalibration in months.

The NI 4050 and NI 4060 are not supported.

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-getcalibrationcount__dmmcalibrationtype.html language=enus -->
## TOPIC 00028: GetCalibrationCount(DmmCalibrationType)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-getcalibrationcount__dmmcalibrationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-getcalibrationcount__dmmcalibrationtype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the calibration count for the specified type of calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int GetCalibrationCount(DmmCalibrationType calibrationType)RemarksNI 4050 and NI 4060 are not supported. ParametersNameTypeDescriptioncalibrationTypeDmmCalibration

### GetCalibrationCount(DmmCalibrationType)

Returns the calibration count for the specified type of calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int GetCalibrationCount(DmmCalibrationType calibrationType)

#### Remarks

NI 4050 and NI 4060 are not supported.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| calibrationType | DmmCalibrationType | Specifies the type of calibration performed (external or self-calibration). The default value is SelfCalibration. |

#### Returns

The number of times calibration has been performed.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.ValueNotSupportedException | The enum parameter value passed is invalid. |

#### See Also

- DmmCalibrationType

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-getcalibrationdateandtime__dmmcalibrationtype.html language=enus -->
## TOPIC 00029: GetCalibrationDateAndTime(DmmCalibrationType)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-getcalibrationdateandtime__dmmcalibrationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-getcalibrationdateandtime__dmmcalibrationtype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the date and time of the last calibration performed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic PrecisionDateTime GetCalibrationDateAndTime(DmmCalibrationType calibrationType)RemarksThe NI 4065 does not support self-calibration. The NI 4050 and NI 4060 are not supported

### GetCalibrationDateAndTime(DmmCalibrationType)

Gets the date and time of the last calibration performed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public PrecisionDateTime GetCalibrationDateAndTime(DmmCalibrationType calibrationType)

#### Remarks

Note

The NI 4050 and NI 4060 are not supported.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| calibrationType | DmmCalibrationType | Specifies the type of calibration performed (external or self-calibration). The default value is SelfCalibration. |

#### Returns

Returns the date and time of the last calibration performed.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.ValueNotSupportedException | The enum parameter value passed is invalid. |

#### See Also

- DmmCalibrationType

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-getdevicetemperature__string.html language=enus -->
## TOPIC 00030: GetDeviceTemperature(string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-getdevicetemperature__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-getdevicetemperature__string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current temperature of the device in Celsius. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double GetDeviceTemperature(string options)ParametersNameTypeDescriptionoptionsstringReserved for future use. ReturnsThe current temperature of the device in Celsius. Excepti

### GetDeviceTemperature(string)

Returns the current temperature of the device in Celsius.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double GetDeviceTemperature(string options)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| options | string | Reserved for future use. |

#### Returns

The current temperature of the device in Celsius.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | The option string is null. |

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-getlastcalibrationtemperature__dmmcalibrationtype.html language=enus -->
## TOPIC 00031: GetLastCalibrationTemperature(DmmCalibrationType)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-getlastcalibrationtemperature__dmmcalibrationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-getlastcalibrationtemperature__dmmcalibrationtype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature during the last calibration procedure. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double GetLastCalibrationTemperature(DmmCalibrationType calibrationType)RemarksNI 4050 and NI 4060 are not supported. ParametersNameTypeDescriptioncalibrationTypeDmmCali

### GetLastCalibrationTemperature(DmmCalibrationType)

Returns the temperature during the last calibration procedure.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double GetLastCalibrationTemperature(DmmCalibrationType calibrationType)

#### Remarks

NI 4050 and NI 4060 are not supported.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| calibrationType | DmmCalibrationType | Specifies the type of calibration performed (external or self-calibration). The default value is SelfCalibration. |

#### Returns

The temperature during the last calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.ValueNotSupportedException | The enum parameter value passed is invalid. |

#### See Also

- DmmCalibrationType

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-isselfcalibrationsupported.html language=enus -->
## TOPIC 00032: IsSelfCalibrationSupported

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-isselfcalibrationsupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-isselfcalibrationsupported.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the DMM device can perform self-calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool IsSelfCalibrationSupported { get; }RemarksReturns a System.Boolean indicating whether the DMM you are using can perform self-calibration.

### IsSelfCalibrationSupported

Gets a value indicating whether the DMM device can perform self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool IsSelfCalibrationSupported { get; }

#### Remarks

Returns a System.Boolean indicating whether the DMM you are using can perform self-calibration.

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-restorelastexternalcalibrationconstants.html language=enus -->
## TOPIC 00033: RestoreLastExternalCalibrationConstants()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-restorelastexternalcalibrationconstants.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-restorelastexternalcalibrationconstants.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reverts the device to the calibration constants from the last complete external calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void RestoreLastExternalCalibrationConstants()RemarksFor the NI 4070/4071/4072 only. This method recovers the hardware if a fatal system er

### RestoreLastExternalCalibrationConstants()

Reverts the device to the calibration constants from the last complete external calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void RestoreLastExternalCalibrationConstants()

#### Remarks

For the NI 4070/4071/4072 only.

This method recovers the hardware if a fatal system error occurs during an external or self-calibration procedure.

After calling this method, call [SelfCalibrate](nationalinstruments-modularinstruments-nidmm-dmmcalibration-selfcalibrate.html) before taking measurements with the device to adjust the device for any temperature drifts since the last external calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The password is invalid. |

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-selfcalibrate.html language=enus -->
## TOPIC 00034: SelfCalibrate()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-selfcalibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-selfcalibrate.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes the self-calibration routine to maintain measurement accuracy. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void SelfCalibrate()RemarksThis method calls Reset, and any configurations previous to the call will be lost. All properties will be set to their default values

### SelfCalibrate()

Executes the self-calibration routine to maintain measurement accuracy.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void SelfCalibrate()

#### Remarks

Reset

Note

For the NI 4070/4071/4072 only.

For more information, refer to the [Self-Calibration](/csh?context=nidmm_dmm_self-calibration) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-setcalibrationpassword__string-string.html language=enus -->
## TOPIC 00035: SetCalibrationPassword(string, string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-setcalibrationpassword__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-setcalibrationpassword__string-string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the password required to enable external calibration functionality for the specified instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void SetCalibrationPassword(string oldPassword, string newPassword)RemarksThe maximum password string length is eight character

### SetCalibrationPassword(string, string)

Changes the password required to enable external calibration functionality for the specified instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void SetCalibrationPassword(string oldPassword, string newPassword)

#### Remarks

The maximum password string length is eight characters, excluding the termination character. NI is the default password.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| oldPassword | string | Specifies the current password required to enable external calibration functionality. The maximum password string length is eight characters, excluding the termination character. |
| newPassword | string | Specifies the new password required to enable external calibration functionality. The maximum password string length is eight characters, excluding the termination character. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | The parameter value passed is null/empty. |
| System.ArgumentException | The password is invalid. |

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-userdefinedinfo.html language=enus -->
## TOPIC 00036: UserDefinedInfo

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-userdefinedinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-userdefinedinfo.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the user-defined information to be stored in the EEPROM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string UserDefinedInfo { get; set; }RemarksThe information to be stored in the EEPROM can include the operator who performed the calibration operation or system i

### UserDefinedInfo

Gets or sets the user-defined information to be stored in the EEPROM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string UserDefinedInfo { get; set; }

#### Remarks

The information to be stored in the EEPROM can include the operator who performed the calibration operation or system information.

If the string size is larger than the maximum string size, NI-DMM stores as much of the information as possible, truncates the remainder, and returns a warning. The NI 4050 and NI 4060 are not supported.

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration-userdefinedinfomaximumsize.html language=enus -->
## TOPIC 00037: UserDefinedInfoMaximumSize

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration-userdefinedinfomaximumsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration-userdefinedinfomaximumsize.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum string length that can be stored in the EEPROM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int UserDefinedInfoMaximumSize { get; }RemarksThe maximum string length that can be stored in the EEPROM, given in characters. The value does not include the terminati

### UserDefinedInfoMaximumSize

Gets the maximum string length that can be stored in the EEPROM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int UserDefinedInfoMaximumSize { get; }

#### Remarks

The maximum string length that can be stored in the EEPROM, given in characters. The value does not include the termination character.

Use [UserDefinedInfo](nationalinstruments-modularinstruments-nidmm-dmmcalibration-userdefinedinfo.html) to store user-defined information.

Parent topic:

DmmCalibration Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibration.html language=enus -->
## TOPIC 00038: DmmCalibration Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibration.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines methods and properties to perform self-calibration or to provide optional functionality when performing a calibration. Derives fromDmmSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmCalibration : DmmSubObjectRemarksExternal calibration is not supported i

### DmmCalibration Class

Defines methods and properties to perform self-calibration or to provide optional functionality when performing a calibration.

#### Derives from

- DmmSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmCalibration : DmmSubObject

#### Remarks

External calibration is not supported in the .NET framework.

For more information, refer to the [Self-Calibration](/csh?context=nidmm_dmm_self-calibration) topic in the *NI Digital Multimeters Help*.

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| ExternalCalibrationRecommendedInterval | Gets the recommended interval between external recalibration in months. |
| IsSelfCalibrationSupported | Gets a value indicating whether the DMM device can perform self-calibration. |
| UserDefinedInfo | Gets or sets the user-defined information to be stored in the EEPROM. |
| UserDefinedInfoMaximumSize | Gets the maximum string length that can be stored in the EEPROM. |

#### Methods

| Name | Description |
| --- | --- |
| GetCalibrationCount(DmmCalibrationType) | Returns the calibration count for the specified type of calibration. |
| GetCalibrationDateAndTime(DmmCalibrationType) | Gets the date and time of the last calibration performed. |
| GetDeviceTemperature(string) | Returns the current temperature of the device in Celsius. |
| GetLastCalibrationTemperature(DmmCalibrationType) | Returns the temperature during the last calibration procedure. |
| RestoreLastExternalCalibrationConstants() | Reverts the device to the calibration constants from the last complete external calibration. |
| SelfCalibrate() | Executes the self-calibration routine to maintain measurement accuracy. |
| SetCalibrationPassword(string, string) | Changes the password required to enable external calibration functionality for the specified instrument. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcalibrationtype.html language=enus -->
## TOPIC 00039: DmmCalibrationType Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcalibrationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcalibrationtype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether calibration is external or self-calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmCalibrationTypeMembersNameValueDescriptionSelfCalibration0Self-calibration. The NI 4065 does not support self-calibration. External1Calibration is external.

### DmmCalibrationType Enumeration

Specifies whether calibration is external or self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmCalibrationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SelfCalibration | 0 | Self-calibration. The NI 4065 does not support self-calibration. |
| External | 1 | Calibration is external. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-advancedcapacitanceandinductance.html language=enus -->
## TOPIC 00040: AdvancedCapacitanceAndInductance

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-advancedcapacitanceandinductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-advancedcapacitanceandinductance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets additional information specific to capacitance and inductance. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmAdvancedCapacitanceAndInductance AdvancedCapacitanceAndInductance { get; }RemarksReturns an object of type DmmAdvancedCapacitanceAndInductance.

### AdvancedCapacitanceAndInductance

Gets additional information specific to capacitance and inductance.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmAdvancedCapacitanceAndInductance](nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance.html) AdvancedCapacitanceAndInductance { get; }

#### Remarks

Returns an object of type [DmmAdvancedCapacitanceAndInductance](nationalinstruments-modularinstruments-nidmm-dmmadvancedcapacitanceandinductance.html).

Parent topic:

DmmCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-cablecompensationtype.html language=enus -->
## TOPIC 00041: CableCompensationType

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-cablecompensationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-cablecompensationtype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmCableCompensationType CableCompensationType { get; set; }RemarksChanging the function or the

### CableCompensationType

Gets or sets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmCableCompensationType](nationalinstruments-modularinstruments-nidmm-dmmcablecompensationtype.html) CableCompensationType { get; set; }

#### Remarks

Changing the function or the range through this property or through [ConfigureMeasurementDigits](nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html) resets the value of this property to the default value.

The default value is [None](nationalinstruments-modularinstruments-nidmm-dmmcablecompensationtype.html).

Parent topic:

DmmCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-configureopencablecompensation__double-double.html language=enus -->
## TOPIC 00042: ConfigureOpenCableCompensation(double, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-configureopencablecompensation__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-configureopencablecompensation__double-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures Conductance and Susceptance. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureOpenCableCompensation(double conductance, double susceptance)RemarksFor the NI 4072 only. ParametersNameTypeDescriptionconductancedoubleSpecifies the open cable compensation cond

### ConfigureOpenCableCompensation(double, double)

Configures [Conductance](nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation-conductance.html) and [Susceptance](nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation-susceptance.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureOpenCableCompensation(double conductance, double susceptance)

#### Remarks

For the NI 4072 only.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| conductance | double | Specifies the open cable compensation conductance. |
| susceptance | double | Specifies the open cable compensation susceptance. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

#### See Also

- Conductance
- Susceptance

Parent topic:

DmmCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-configureshortcablecompensation__double-double.html language=enus -->
## TOPIC 00043: ConfigureShortCableCompensation(double, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-configureshortcablecompensation__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-configureshortcablecompensation__double-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Resistance and Reactance. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureShortCableCompensation(double resistance, double reactance)RemarksFor the NI 4072 only. ParametersNameTypeDescriptionresistancedoubleSpecifies the short cable compensation resis

### ConfigureShortCableCompensation(double, double)

Configures the [Resistance](nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation-resistance.html) and [Reactance](nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation-reactance.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureShortCableCompensation(double resistance, double reactance)

#### Remarks

For the NI 4072 only.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resistance | double | Specifies the short cable compensation resistance. |
| reactance | double | Specifies the short cable compensation reactance. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

#### See Also

- Reactance
- Resistance

Parent topic:

DmmCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-opencablecompensation.html language=enus -->
## TOPIC 00044: OpenCableCompensation

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-opencablecompensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-opencablecompensation.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmOpenCableCompensation sub-object used to control open cable compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmOpenCableCompensation OpenCableCompensation { get; }RemarksReturns an object of type DmmOpenCableCompensation.

### OpenCableCompensation

Gets the [DmmOpenCableCompensation](nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation.html) sub-object used to control open cable compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmOpenCableCompensation](nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation.html) OpenCableCompensation { get; }

#### Remarks

Returns an object of type [DmmOpenCableCompensation](nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation.html).

Parent topic:

DmmCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-performopencablecompensation__out-out.html language=enus -->
## TOPIC 00045: PerformOpenCableCompensation(out double, out double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-performopencablecompensation__out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-performopencablecompensation__out-out.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the open cable compensation measurements for the current capacitance/inductance range, and returns open cable compensation conductance and susceptance values. You can use the return values of this method as inputs to ConfigureOpenCableCompensation. SyntaxNamespace: NationalInstruments.Modul

### PerformOpenCableCompensation(out double, out double)

Performs the open cable compensation measurements for the current capacitance/inductance range, and returns open cable compensation conductance and susceptance values. You can use the return values of this method as inputs to [ConfigureOpenCableCompensation](nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-configureopencablecompensation__double-double.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void PerformOpenCableCompensation(out double conductance, out double susceptance)

#### Remarks

For the NI 4072 only.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| conductance | out double | Specifies the open cable compensation conductance. |
| susceptance | out double | Specifies the open cable compensation susceptance. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OperationNotSupportedException | MeasurementFunction is not set to Capacitance or Inductance. |

Parent topic:

DmmCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-performshortcablecompensation__out-out.html language=enus -->
## TOPIC 00046: PerformShortCableCompensation(out double, out double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-performshortcablecompensation__out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-performshortcablecompensation__out-out.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the short cable compensation measurements for the current capacitance/inductance range, and returns short cable compensation resistance and reactance values. You can use the return values of this function as inputs to ConfigureShortCableCompensation. SyntaxNamespace: NationalInstruments.Mod

### PerformShortCableCompensation(out double, out double)

Performs the short cable compensation measurements for the current capacitance/inductance range, and returns short cable compensation resistance and reactance values. You can use the return values of this function as inputs to [ConfigureShortCableCompensation](nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-configureshortcablecompensation__double-double.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void PerformShortCableCompensation(out double resistance, out double reactance)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resistance | out double | Specifies the short cable compensation resistance. |
| reactance | out double | Specifies the short cable compensation reactance. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OperationNotSupportedException | MeasurementFunction is not set to Capacitance and Inductance. |

Parent topic:

DmmCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-shortcablecompensation.html language=enus -->
## TOPIC 00047: ShortCableCompensation

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-shortcablecompensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance-shortcablecompensation.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ShortCableCompensation sub-object used to control short cable compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmShortCableCompensation ShortCableCompensation { get; }RemarksReturns an object of type DmmShortCableCompensation.

### ShortCableCompensation

Gets the ShortCableCompensation sub-object used to control short cable compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmShortCableCompensation](nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation.html) ShortCableCompensation { get; }

#### Remarks

Returns an object of type [DmmShortCableCompensation](nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation.html).

Parent topic:

DmmCapacitanceAndInductance Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance.html language=enus -->
## TOPIC 00048: DmmCapacitanceAndInductance Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods and properties to control inductance and capacitance capabilities. Derives fromDmmSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmCapacitanceAndInductance : DmmSubObjectRemarksFor the NI-DMM 4072 only. For more information, refer to the Capacita

### DmmCapacitanceAndInductance Class

Provides methods and properties to control inductance and capacitance capabilities.

#### Derives from

- DmmSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmCapacitanceAndInductance : DmmSubObject

#### Remarks

For the NI-DMM 4072 only.

Capacitance/Inductance

NI Digital Multimeters Help

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AdvancedCapacitanceAndInductance | Gets additional information specific to capacitance and inductance. |
| CableCompensationType | Gets or sets the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. |
| OpenCableCompensation | Gets the DmmOpenCableCompensation sub-object used to control open cable compensation. |
| ShortCableCompensation | Gets the ShortCableCompensation sub-object used to control short cable compensation. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureOpenCableCompensation(double, double) | Configures Conductance and Susceptance. |
| ConfigureShortCableCompensation(double, double) | Configures the Resistance and Reactance. |
| PerformOpenCableCompensation(out double, out double) | Performs the open cable compensation measurements for the current capacitance/inductance range, and returns open cable compensation conductance and susceptance values. You can use the return values of this method as inputs to ConfigureOpenCableCompensation. |
| PerformShortCableCompensation(out double, out double) | Performs the short cable compensation measurements for the current capacitance/inductance range, and returns short cable compensation resistance and reactance values. You can use the return values of this function as inputs to ConfigureShortCableCompensation. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmcontrolaction.html language=enus -->
## TOPIC 00049: DmmControlAction Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmcontrolaction.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmcontrolaction.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the control action for the driver to perform. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmControlActionMembersNameValueDescriptionCommit0Commits to hardware all of the configured attributes associated with the session. See AlsoControl

### DmmControlAction Enumeration

Specifies the control action for the driver to perform.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmControlAction

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Commit | 0 | Commits to hardware all of the configured attributes associated with the session. |

#### See Also

- Control

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdcbias.html language=enus -->
## TOPIC 00050: DmmDCBias Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdcbias.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdcbias.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use DmmDCBias to specify the DC bias. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmDCBiasRemarksFor more information, refer to the DC Bias topic in the NI Digital Multimeters Help. MembersNameValueDescriptionOff0The device does not use the DC bias. On1The device uses t

### DmmDCBias Enumeration

Use DmmDCBias to specify the DC bias.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmDCBias

#### Remarks

For more information, refer to the [DC Bias](/csh?context=nidmm_dmm_4072_dc_bias) topic in the *NI Digital Multimeters Help*.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | The device does not use the DC bias. |
| On | 1 | The device uses the DC bias. |

#### See Also

- DCBias

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdcnoiserejection.html language=enus -->
## TOPIC 00051: DmmDCNoiseRejection Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdcnoiserejection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdcnoiserejection.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies values for DC noise rejection. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmDCNoiseRejectionRemarksFor more information, refer to the DC Noise Rejection topic in the NI Digital Multimeters Help. MembersNameValueDescriptionAuto-1The driver chooses the DC noise

### DmmDCNoiseRejection Enumeration

Specifies values for DC noise rejection.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmDCNoiseRejection

#### Remarks

For more information, refer to the [DC Noise Rejection](/csh?context=nidmm_dmm_dc_noise_rejection) topic in the *NI Digital Multimeters Help*.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | -1 | The driver chooses the DC noise rejection setting based on the configured function and resolution. |
| Normal | 0 | All samples are weighed equally. |
| SecondOrder | 1 | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement using a triangular weighing function. |
| HighOrder | 2 | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement using a bell-curve weighing function. |

#### See Also

- DCNoiseRejection

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdelaymode.html language=enus -->
## TOPIC 00052: DmmDelayMode Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdelaymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdelaymode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a delay interval after a sample trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmDelayModeRemarksFor NI 4060 only. MembersNameValueDescriptionIntervalSampleTrigger0IVI compliant. Used when the sample trigger is set to Interval. AnySampleTrigger1Not IVI C

### DmmDelayMode Enumeration

Specifies a delay interval after a sample trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmDelayMode

#### Remarks

For NI 4060 only.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| IntervalSampleTrigger | 0 | IVI compliant. Used when the sample trigger is set to Interval. |
| AnySampleTrigger | 1 | Not IVI Compliant. Used as a delay after any type of sample trigger. |

#### See Also

- SampleDelayMode

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-description.html language=enus -->
## TOPIC 00053: Description

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-description.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing a description of the specific driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string Description { get; }RemarksA string containing a description of the specific driver.

### Description

Gets a string containing a description of the specific driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string Description { get; }

#### Remarks

A string containing a description of the specific driver.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-getgroupcapabilities.html language=enus -->
## TOPIC 00054: GetGroupCapabilities()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-getgroupcapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-getgroupcapabilities.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the list of the class capability groups implemented by the driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string[] GetGroupCapabilities()RemarksCapability group names are documented in the IVI class specifications. If the driver is not class-compliant, the driver

### GetGroupCapabilities()

Returns the list of the class capability groups implemented by the driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string[] GetGroupCapabilities()

#### Remarks

Capability group names are documented in the IVI class specifications. If the driver is not class-compliant, the driver returns an empty array.

#### Returns

An array of class capability groups.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-getsupportedinstrumentmodels.html language=enus -->
## TOPIC 00055: GetSupportedInstrumentModels()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-getsupportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-getsupportedinstrumentmodels.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the list of instrument models that the IVI-specific driver can control. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string[] GetSupportedInstrumentModels()RemarksThe string does not include an abbreviation for the manufacturer if it is the same for all models. Returns

### GetSupportedInstrumentModels()

Returns the list of instrument models that the IVI-specific driver can control.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string[] GetSupportedInstrumentModels()

#### Remarks

The string does not include an abbreviation for the manufacturer if it is the same for all models.

#### Returns

An array of instrument models.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-identifier.html language=enus -->
## TOPIC 00056: Identifier

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-identifier.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-identifier.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the case-sensitive unique identifier of the instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string Identifier { get; }RemarksCase-sensitive unique identifier of the instrument driver.

### Identifier

Gets the case-sensitive unique identifier of the instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string Identifier { get; }

#### Remarks

Case-sensitive unique identifier of the instrument driver.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentfirmwarerevision.html language=enus -->
## TOPIC 00057: InstrumentFirmwareRevision

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentfirmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentfirmwarerevision.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the instrument firmware revision number. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string InstrumentFirmwareRevision { get; }RemarksA string containing the instrument firmware revision number.

### InstrumentFirmwareRevision

Gets a string containing the instrument firmware revision number.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string InstrumentFirmwareRevision { get; }

#### Remarks

A string containing the instrument firmware revision number.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentmanufacturer.html language=enus -->
## TOPIC 00058: InstrumentManufacturer

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentmanufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentmanufacturer.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the manufacturer of the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string InstrumentManufacturer { get; }RemarksA string containing the manufacturer of the instrument.

### InstrumentManufacturer

Gets a string containing the manufacturer of the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string InstrumentManufacturer { get; }

#### Remarks

A string containing the manufacturer of the instrument.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentmodel.html language=enus -->
## TOPIC 00059: InstrumentModel

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentmodel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-instrumentmodel.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the instrument model. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string InstrumentModel { get; }RemarksA string containing the instrument model.

### InstrumentModel

Gets a string containing the instrument model.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string InstrumentModel { get; }

#### Remarks

A string containing the instrument model.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-revision.html language=enus -->
## TOPIC 00060: Revision

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-revision.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string that contains additional version information about this specific instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string Revision { get; }RemarksA string that contains additional version information about this instrument driver.

### Revision

Gets a string that contains additional version information about this specific instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string Revision { get; }

#### Remarks

A string that contains additional version information about this instrument driver.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-serialnumber.html language=enus -->
## TOPIC 00061: SerialNumber

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-serialnumber.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the serial number of the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string SerialNumber { get; }RemarksThe serial number of the instrument. This value corresponds to the serial number label that is attached to most products.

### SerialNumber

Gets a string containing the serial number of the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string SerialNumber { get; }

#### Remarks

The serial number of the instrument.

This value corresponds to the serial number label that is attached to most products.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificationmajorversion.html language=enus -->
## TOPIC 00062: SpecificationMajorVersion

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificationmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificationmajorversion.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the major version number of the class specification for the specific driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int SpecificationMajorVersion { get; }RemarksReturns an integer of the major version number of the class specification for the specific driver.

### SpecificationMajorVersion

Gets the major version number of the class specification for the specific driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int SpecificationMajorVersion { get; }

#### Remarks

Returns an integer of the major version number of the class specification for the specific driver.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificationminorversion.html language=enus -->
## TOPIC 00063: SpecificationMinorVersion

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificationminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificationminorversion.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minor version number of the class specification for the specific driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int SpecificationMinorVersion { get; }RemarksReturns the minor version number of the class specification for the specific driver.

### SpecificationMinorVersion

Gets the minor version number of the class specification for the specific driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int SpecificationMinorVersion { get; }

#### Remarks

Returns the minor version number of the class specification for the specific driver.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdrivermajorversion.html language=enus -->
## TOPIC 00064: SpecificDriverMajorVersion

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdrivermajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdrivermajorversion.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the major version number of this instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int SpecificDriverMajorVersion { get; }RemarksReturns the major version number of this instrument driver.

### SpecificDriverMajorVersion

Gets the major version number of this instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int SpecificDriverMajorVersion { get; }

#### Remarks

Returns the major version number of this instrument driver.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdriverminorversion.html language=enus -->
## TOPIC 00065: SpecificDriverMinorVersion

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdriverminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdriverminorversion.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the minor version number of this instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int SpecificDriverMinorVersion { get; }RemarksReturns the minor version number of this instrument driver.

### SpecificDriverMinorVersion

Gets the minor version number of this instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int SpecificDriverMinorVersion { get; }

#### Remarks

Returns the minor version number of this instrument driver.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdriverprefix.html language=enus -->
## TOPIC 00066: SpecificDriverPrefix

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdriverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-specificdriverprefix.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the prefix for the specific instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string SpecificDriverPrefix { get; }RemarksA string containing the prefix for the specific instrument driver. The prefix can be a maximum of eight characters.

### SpecificDriverPrefix

Gets the prefix for the specific instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string SpecificDriverPrefix { get; }

#### Remarks

A string containing the prefix for the specific instrument driver. The prefix can be a maximum of eight characters.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-vendor.html language=enus -->
## TOPIC 00067: Vendor

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-vendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity-vendor.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the vendor of the specific driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string Vendor { get; }RemarksA string containing the vendor of the specific driver.

### Vendor

Gets a string containing the vendor of the specific driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string Vendor { get; }

#### Remarks

A string containing the vendor of the specific driver.

Parent topic:

DmmDriverIdentity Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveridentity.html language=enus -->
## TOPIC 00068: DmmDriverIdentity Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveridentity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveridentity.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides identity information about the instrument you are using. Derives fromDmmSubObjectIIviDriverIdentityIIviComponentIdentitySyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmDriverIdentity : DmmSubObject, IIviDriverIdentity, IIviComponentIdentityRemarksProvides identi

### DmmDriverIdentity Class

Provides identity information about the instrument you are using.

#### Derives from

- DmmSubObject
- IIviDriverIdentity
- IIviComponentIdentity

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmDriverIdentity : DmmSubObject, IIviDriverIdentity, IIviComponentIdentity

#### Remarks

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Description | Gets a string containing a description of the specific driver. |
| Identifier | Gets the case-sensitive unique identifier of the instrument driver. |
| InstrumentFirmwareRevision | Gets a string containing the instrument firmware revision number. |
| InstrumentManufacturer | Gets a string containing the manufacturer of the instrument. |
| InstrumentModel | Gets a string containing the instrument model. |
| Revision | Gets a string that contains additional version information about this specific instrument driver. |
| SerialNumber | Gets a string containing the serial number of the instrument. |
| SpecificationMajorVersion | Gets the major version number of the class specification for the specific driver. |
| SpecificationMinorVersion | Gets the minor version number of the class specification for the specific driver. |
| SpecificDriverMajorVersion | Gets the major version number of this instrument driver. |
| SpecificDriverMinorVersion | Gets the minor version number of this instrument driver. |
| SpecificDriverPrefix | Gets the prefix for the specific instrument driver. |
| Vendor | Gets a string containing the vendor of the specific driver. |

#### Methods

| Name | Description |
| --- | --- |
| GetGroupCapabilities() | Returns the list of the class capability groups implemented by the driver. |
| GetSupportedInstrumentModels() | Returns the list of instrument models that the IVI-specific driver can control. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverlock-dmmdriverlock__iividriverlock.html language=enus -->
## TOPIC 00069: DmmDriverLock(IIviDriverLock)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverlock-dmmdriverlock__iividriverlock.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverlock-dmmdriverlock__iividriverlock.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DmmDriverLock class. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDriverLock(IIviDriverLock iviDriverLock)ParametersNameTypeDescriptioniviDriverLockIIviDriverLockBase interface for synchronization locks obtained on the driver session.

### DmmDriverLock(IIviDriverLock)

Initializes a new instance of the [DmmDriverLock](nationalinstruments-modularinstruments-nidmm-dmmdriverlock.html) class.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public DmmDriverLock(IIviDriverLock iviDriverLock)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| iviDriverLock | IIviDriverLock | Base interface for synchronization locks obtained on the driver session. |

Parent topic:

DmmDriverLock Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverlock-unlock.html language=enus -->
## TOPIC 00070: Unlock()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverlock-unlock.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverlock-unlock.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases a driver synchronization lock. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Unlock()

### Unlock()

Releases a driver synchronization lock.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Unlock()

Parent topic:

DmmDriverLock Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverlock.html language=enus -->
## TOPIC 00071: DmmDriverLock Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverlock.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverlock.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides synchronization locks obtained on the driver session. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmDriverLockRemarksThis class is used to obtain a lock on the driver session allowing for thread safety. Thread SafetyAll members of this type are

### DmmDriverLock Class

Provides synchronization locks obtained on the driver session.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmDriverLock

#### Remarks

This class is used to obtain a lock on the driver session allowing for thread safety.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DmmDriverLock(IIviDriverLock) | Initializes a new instance of the DmmDriverLock class. |

#### Methods

| Name | Description |
| --- | --- |
| Unlock() | Releases a driver synchronization lock. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-cache.html language=enus -->
## TOPIC 00072: Cache

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-cache.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to cache the value of properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool Cache { get; set; }RemarksThe default value is True. Use NIDmm to override this value. When caching is enabled, the instrument driver keeps track of the

### Cache

Gets or sets a value indicating whether to cache the value of properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool Cache { get; set; }

#### Remarks

The default value is **True**. Use [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) to override this value.

When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument, which significantly increases execution speed. The instrument driver can always cache or never cache particular attributes regardless of the setting of this property.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-coercion.html language=enus -->
## TOPIC 00073: Coercion

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-coercion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-coercion.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when a property is coerced. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic EventHandler< CoercionEventArgs > CoercionRemarksThis event is triggered only if RecordValueCoercions is set to true.

### Coercion

Occurs when a property is coerced.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public EventHandler< CoercionEventArgs > Coercion

#### Remarks

This event is triggered only if [RecordValueCoercions](nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-recordvaluecoercions.html) is set to true.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-dispose.html language=enus -->
## TOPIC 00074: Dispose()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-dispose.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees the resources held. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Dispose()

### Dispose()

Frees the resources held.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Dispose()

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-driversetup.html language=enus -->
## TOPIC 00075: DriverSetup

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-driversetup.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-driversetup.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the driver setup string that was specified when initializing the driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string DriverSetup { get; }RemarksSome cases exist where the end-user must specify instrument driver options at initialization time. An example of this is

### DriverSetup

Gets the driver setup string that was specified when initializing the driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string DriverSetup { get; }

#### Remarks

Some cases exist where the end-user must specify instrument driver options at initialization time. An example of this is specifying a particular instrument model from among a family of instruments that the driver supports. This is useful when using simulation. You can specify driver-specific options using the *optionString* parameter to [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html).

If the user does not specify a DriverSetup string, this property returns an empty string. Otherwise this property returns the DriverSetup string that was specified when initializing the driver.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-interchangecheck.html language=enus -->
## TOPIC 00076: InterchangeCheck

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-interchangecheck.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to perform interchangeability checking and log interchangeability warnings when you call NI-DMM methods. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool InterchangeCheck { get; set; }RemarksThe default value is False. Using your applic

### InterchangeCheck

Gets or sets a value indicating whether to perform interchangeability checking and log interchangeability warnings when you call NI-DMM methods.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool InterchangeCheck { get; set; }

#### Remarks

The default value is **False**.

Using your application with a different instrument might cause different behavior, as indicated by an interchangeability warning. Interchangeability checking examines the properties in a capability group only if you specify a value for at least one property within that group. Interchangeability warnings occur when a property affects the behavior of the instrument and you have not set that property, or the property has been invalidated since you set it.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-interchangecheckwarning.html language=enus -->
## TOPIC 00077: InterchangeCheckWarning

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-interchangecheckwarning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-interchangecheckwarning.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when an interchange check warning event is raised. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic EventHandler< InterchangeCheckWarningEventArgs > InterchangeCheckWarningRemarksThis event is triggered only if InterchangeCheck is set to true.

### InterchangeCheckWarning

Occurs when an interchange check warning event is raised.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public EventHandler< InterchangeCheckWarningEventArgs > InterchangeCheckWarning

#### Remarks

This event is triggered only if [InterchangeCheck](nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-interchangecheck.html) is set to true.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-invalidateallattributes.html language=enus -->
## TOPIC 00078: InvalidateAllAttributes()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-invalidateallattributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-invalidateallattributes.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Invalidates all attributes such that any values set before calling Commit are discarded. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void InvalidateAllAttributes()

### InvalidateAllAttributes()

Invalidates all attributes such that any values set before calling [Commit](nationalinstruments-modularinstruments-nidmm-dmmcontrolaction.html) are discarded.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void InvalidateAllAttributes()

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-ioresourcedescriptor.html language=enus -->
## TOPIC 00079: IOResourceDescriptor

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-ioresourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-ioresourcedescriptor.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the resource descriptor for the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string IOResourceDescriptor { get; }RemarksA string containing the resource descriptor for the instrument

### IOResourceDescriptor

Gets a string containing the resource descriptor for the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string IOResourceDescriptor { get; }

#### Remarks

A string containing the resource descriptor for the instrument

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-logicalname.html language=enus -->
## TOPIC 00080: LogicalName

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-logicalname.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the logical name of the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string LogicalName { get; }RemarksA string containing the logical name of the instrument.

### LogicalName

Gets a string containing the logical name of the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string LogicalName { get; }

#### Remarks

A string containing the logical name of the instrument.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-queryinstrumentstatus.html language=enus -->
## TOPIC 00081: QueryInstrumentStatus

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-queryinstrumentstatus.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the instrument driver queries the instrument status after each operation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool QueryInstrumentStatus { get; set; }RemarksQuerying the instrument status is useful when debugging. After the user

### QueryInstrumentStatus

Gets or sets a value indicating whether the instrument driver queries the instrument status after each operation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool QueryInstrumentStatus { get; set; }

#### Remarks

Querying the instrument status is useful when debugging. After the user program is validated, this property can be set to false to disable status checking and maximize performance. The instrument driver can choose to ignore status checking for particular properties regardless of the setting of this property. Use [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) to override this value.

The default value is true.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-rangecheck.html language=enus -->
## TOPIC 00082: RangeCheck

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-rangecheck.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to validate property values and method parameters. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool RangeCheck { get; set; }RemarksIf enabled, the instrument driver validates the parameter values passed to driver functions. Range checki

### RangeCheck

Gets or sets a value indicating whether to validate property values and method parameters.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool RangeCheck { get; set; }

#### Remarks

If enabled, the instrument driver validates the parameter values passed to driver functions. Range checking parameters is useful for debugging. After the user program is validated, this property can be set to false to disable range checking and maximize performance. The default value is true. Use [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) override this value.

The default value is true.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-recordvaluecoercions.html language=enus -->
## TOPIC 00083: RecordValueCoercions

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-recordvaluecoercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-recordvaluecoercions.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the IVI engine keeps a list of the value coercions it makes for integer and System.Double values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool RecordValueCoercions { get; set; }RemarksThe default value is false. Use NIDmm to overrid

### RecordValueCoercions

Gets or sets a value indicating whether the IVI engine keeps a list of the value coercions it makes for integer and System.Double values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool RecordValueCoercions { get; set; }

#### Remarks

The default value is false.

Use [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) to override this value.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-resetinterchangecheck.html language=enus -->
## TOPIC 00084: ResetInterchangeCheck()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-resetinterchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-resetinterchangecheck.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the interchangeability checking algorithms of the driver so that methods and properties that executed prior to calling this method have no effect on whether future calls to the driver generate interchangeability warnings. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic voi

### ResetInterchangeCheck()

Resets the interchangeability checking algorithms of the driver so that methods and properties that executed prior to calling this method have no effect on whether future calls to the driver generate interchangeability warnings.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ResetInterchangeCheck()

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-simulate.html language=enus -->
## TOPIC 00085: Simulate

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-simulate.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to simulate instrument driver I/O operations. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool Simulate { get; set; }RemarksThe default value is false. Simulate can only be set within the constructor for NIDmm. The property value cannot

### Simulate

Gets or sets a value indicating whether to simulate instrument driver I/O operations.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool Simulate { get; set; }

#### Remarks

The default value is false.

Simulate can only be set within the constructor for [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html). The property value cannot be changed outside of the constructor.

If simulation is enabled, instrument driver functions perform range checking and get or set properties, but they do not perform instrument I/O. For output parameters that represent instrument data, the instrument driver functions return calculated values. Use [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) to override this setting.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-synchronizecallbacks.html language=enus -->
## TOPIC 00086: SynchronizeCallbacks

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-synchronizecallbacks.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the events and callback delegates are invoked through System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool SynchronizeCallbacks { get; set

### SynchronizeCallbacks

Gets or sets a value indicating whether the events and callback delegates are invoked through System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

true if events and callbacks are invoked through the System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods; otherwise, events and callbacks are invoked directly. The default value is true.

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-warning.html language=enus -->
## TOPIC 00087: Warning

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-warning.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation-warning.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when a warning is generated. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic EventHandler< WarningEventArgs > Warning

### Warning

Occurs when a warning is generated.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public EventHandler< WarningEventArgs > Warning

Parent topic:

DmmDriverOperation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriveroperation.html language=enus -->
## TOPIC 00088: DmmDriverOperation Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriveroperation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriveroperation.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties that affect the operation of this instrument driver. Derives fromDmmSubObjectIIviDriverOperationISupportSynchronizationContextIDisposableSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmDriverOperation : DmmSubObject, IIviDriverOperation, ISupportSynch

### DmmDriverOperation Class

Provides properties that affect the operation of this instrument driver.

#### Derives from

- DmmSubObject
- IIviDriverOperation
- ISupportSynchronizationContext
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmDriverOperation : DmmSubObject, IIviDriverOperation, ISupportSynchronizationContext, IDisposable

#### Remarks

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Cache | Gets or sets a value indicating whether to cache the value of properties. |
| DriverSetup | Gets the driver setup string that was specified when initializing the driver. |
| InterchangeCheck | Gets or sets a value indicating whether to perform interchangeability checking and log interchangeability warnings when you call NI-DMM methods. |
| IOResourceDescriptor | Gets a string containing the resource descriptor for the instrument. |
| LogicalName | Gets a string containing the logical name of the instrument. |
| QueryInstrumentStatus | Gets or sets a value indicating whether the instrument driver queries the instrument status after each operation. |
| RangeCheck | Gets or sets a value indicating whether to validate property values and method parameters. |
| RecordValueCoercions | Gets or sets a value indicating whether the IVI engine keeps a list of the value coercions it makes for integer and System.Double values. |
| Simulate | Gets or sets a value indicating whether to simulate instrument driver I/O operations. |
| SynchronizeCallbacks | Gets or sets a value indicating whether the events and callback delegates are invoked through System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Frees the resources held. |
| InvalidateAllAttributes() | Invalidates all attributes such that any values set before calling Commit are discarded. |
| ResetInterchangeCheck() | Resets the interchangeability checking algorithms of the driver so that methods and properties that executed prior to calling this method have no effect on whether future calls to the driver generate interchangeability warnings. |

#### Events

| Name | Description |
| --- | --- |
| Coercion | Occurs when a property is coerced. |
| InterchangeCheckWarning | Occurs when an interchange check warning event is raised. |
| Warning | Occurs when a warning is generated. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-clearerror.html language=enus -->
## TOPIC 00089: ClearError()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-clearerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-clearerror.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all errors. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ClearError()

### ClearError()

Clears all errors.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ClearError()

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-disable.html language=enus -->
## TOPIC 00090: Disable()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-disable.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Disable()RemarksIf a measurement is in progress when this method is called, the measurement is aborted.

### Disable()

Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Disable()

#### Remarks

If a measurement is in progress when this method is called, the measurement is aborted.

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-errorquery.html language=enus -->
## TOPIC 00091: ErrorQuery()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-errorquery.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-errorquery.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads an error code and message from the DMM error queue. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic ErrorQueryResult ErrorQuery()RemarksNational Instruments DMMs do not contain an error queue. Errors are reported as they occur. Therefore, this method does not detect errors;

### ErrorQuery()

Reads an error code and message from the DMM error queue.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public ErrorQueryResult ErrorQuery()

#### Remarks

National Instruments DMMs do not contain an error queue. Errors are reported as they occur. Therefore, this method does not detect errors; it is included for compliance with the IviDmm Class Specification.

#### Returns

Returns the error query result.

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-exportattributeconfigurationbuffer.html language=enus -->
## TOPIC 00092: ExportAttributeConfigurationBuffer()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-exportattributeconfigurationbuffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-exportattributeconfigurationbuffer.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the attribute configuration of the session to the specified System.Byte array buffer. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic byte[] ExportAttributeConfigurationBuffer()RemarksYou can export and import session attribute configurations only between devices with ide

### ExportAttributeConfigurationBuffer()

Exports the attribute configuration of the session to the specified System.Byte array buffer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public byte[] ExportAttributeConfigurationBuffer()

#### Remarks

You can export and import session attribute configurations only between devices with identical model numbers.

Note

Not supported on the PCMCIA-4050 or the PXI/PCI-4060.

- PXI/PCI/PCIe/USB-4065
- PXI/PCI-4070
- PXI-4071
- PXI-4072

#### Returns

Returns a System.Byte array containing the attribute configuration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportAttributeConfigurationBuffer method was called after the associated NIDmm object was disposed. |
| Ivi.Driver.IviCDriverException | The underlying NI-DMM driver returned an error. |

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-exportattributeconfigurationfile__string.html language=enus -->
## TOPIC 00093: ExportAttributeConfigurationFile(string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-exportattributeconfigurationfile__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-exportattributeconfigurationfile__string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports the attribute configuration of the session to the specified file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ExportAttributeConfigurationFile(string filePath)RemarksYou can export and import session attribute configurations only between devices with identical mo

### ExportAttributeConfigurationFile(string)

Exports the attribute configuration of the session to the specified file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ExportAttributeConfigurationFile(string filePath)

#### Remarks

You can export and import session attribute configurations only between devices with identical model numbers.

Note

Not supported on the PCMCIA-4050 or the PXI/PCI-4060.

- PXI/PCI/PCIe/USB-4065
- PXI/PCI-4070
- PXI-4071
- PXI-4072

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The absolute path to the file to contain the exported attribute configuration. If you specify an empty or relative path, this method returns an error. The default file extension is .nidmmconfig. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportAttributeConfigurationFile method was called after the associated NIDmm object was disposed. |
| Ivi.Driver.IviCDriverException | The underlying NI-DMM driver returned an error. |

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-importattributeconfigurationbuffer__byte_arr1.html language=enus -->
## TOPIC 00094: ImportAttributeConfigurationBuffer(byte[])

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-importattributeconfigurationbuffer__byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-importattributeconfigurationbuffer__byte_arr1.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports an attribute configuration to the session from the specified configuration . SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ImportAttributeConfigurationBuffer(byte[] configuration)RemarksYou can export and import session attribute configurations only between devices

### ImportAttributeConfigurationBuffer(byte[])

Imports an attribute configuration to the session from the specified *configuration* .

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ImportAttributeConfigurationBuffer(byte[] configuration)

#### Remarks

Note

You cannot call this method while the session is in a running state, such as while acquiring a waveform.

Note

Not supported on the PCMCIA-4050 or the PXI/PCI-4060.

- PXI/PCI/PCIe/USB-4065
- PXI/PCI-4070
- PXI-4071
- PXI-4072

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| configuration | byte[] | The byte array that contains the attribute configuration to import. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ImportAttributeConfigurationBuffer method was called after the associated NIDmm object was disposed. |
| Ivi.Driver.IviCDriverException | The underlying NI-DMM driver returned an error. |

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-importattributeconfigurationfile__string.html language=enus -->
## TOPIC 00095: ImportAttributeConfigurationFile(string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-importattributeconfigurationfile__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-importattributeconfigurationfile__string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports an attribute configuration to the session from the specified file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ImportAttributeConfigurationFile(string filePath)RemarksYou can export and import session attribute configurations only between devices with identical m

### ImportAttributeConfigurationFile(string)

Imports an attribute configuration to the session from the specified file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ImportAttributeConfigurationFile(string filePath)

#### Remarks

Note

You cannot call this method while the session is in a running state, such as while acquiring a waveform.

Note

Not supported on the PCMCIA-4050 or the PXI/PCI-4060.

- PXI/PCI/PCIe/USB-4065
- PXI/PCI-4070
- PXI-4071
- PXI-4072

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The absolute path to the file containing the attribute configuration to import. If you specify an empty or relative path, this method returns an error. The default file extension is .nidmmconfig. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ImportAttributeConfigurationFile method was called after the associated NIDmm object was disposed. |
| Ivi.Driver.IviCDriverException | The underlying NI-DMM driver returned an error. |

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-lock.html language=enus -->
## TOPIC 00096: Lock()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-lock.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-lock.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attempts to acquire a synchronization lock on this instance of the driver. The calling thread is blocked indefinitely until the lock is acquired. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDriverLock Lock()RemarksUse this method to gain exclusive access to the driver inst

### Lock()

Attempts to acquire a synchronization lock on this instance of the driver. The calling thread is blocked indefinitely until the lock is acquired.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmDriverLock](nationalinstruments-modularinstruments-nidmm-dmmdriverlock.html) Lock()

#### Remarks

Use this method to gain exclusive access to the driver instance across a series of methods calls. You must call [Unlock](nationalinstruments-modularinstruments-nidmm-dmmdriverlock-unlock.html) on the returned lock to allow other threads to access this instance of the driver.

This is not an I/O lock, such as a VISA lock. It is a thread synchronization lock for this instance of the specific driver in the process.

#### Returns

A reference to the acquired lock.

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-lock__ivi.driver.precisiontimespan.html language=enus -->
## TOPIC 00097: Lock(Ivi.Driver.PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-lock__ivi.driver.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-lock__ivi.driver.precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attempts to acquire a synchronization lock on this instance of the driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDriverLock Lock(Ivi.Driver.PrecisionTimeSpan maximumTime)RemarksThe calling thread is blocked until either the lock is acquired or maximumTime expires. If

### Lock(Ivi.Driver.PrecisionTimeSpan)

Attempts to acquire a synchronization lock on this instance of the driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmDriverLock](nationalinstruments-modularinstruments-nidmm-dmmdriverlock.html) Lock(Ivi.Driver.PrecisionTimeSpan maximumTime)

#### Remarks

The calling thread is blocked until either the lock is acquired or *maximumTime*  expires. If the lock is not acquired within the interval specified by *maximumTime* , an exception is returned. This method is useful for gaining exclusive access to the driver instance across a series of methods calls. The user must call [Unlock](nationalinstruments-modularinstruments-nidmm-dmmdriverlock-unlock.html) on the returned lock to relinquish the lock and allow other threads to access this instance of the driver.

This is not an I/O lock, such as a VISA lock. It is a thread synchronization lock for this instance of the specific driver in the process.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | Ivi.Driver.PrecisionTimeSpan | The maximum amount of time to wait to acquire the lock. |

#### Returns

A reference to the acquired lock.

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-ni4022control__string-dmm4022configurationmode.html language=enus -->
## TOPIC 00098: NI4022Control(string, Dmm4022ConfigurationMode)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-ni4022control__string-dmm4022configurationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-ni4022control__string-dmm4022configurationmode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI 4022 module. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static void NI4022Control(string resourceName, Dmm4022ConfigurationMode configuration)ParametersNameTypeDescriptionresourceNamestringThe resource name of the device to initialize. configurationDmm4022C

### NI4022Control(string, Dmm4022ConfigurationMode)

Configures the NI 4022 module.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static void NI4022Control(string resourceName, Dmm4022ConfigurationMode configuration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | The resource name of the device to initialize. |
| configuration | Dmm4022ConfigurationMode | The operating mode of the 4022 module. |

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-reset.html language=enus -->
## TOPIC 00099: Reset()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-reset.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-reset.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the instrument to a known state and sends initialization commands to the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Reset()RemarksThe initialization commands set instrument settings to the state necessary for the operation of the instrument driver.

### Reset()

Resets the instrument to a known state and sends initialization commands to the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Reset()

#### Remarks

The initialization commands set instrument settings to the state necessary for the operation of the instrument driver.

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-resetwithdefaults.html language=enus -->
## TOPIC 00100: ResetWithDefaults()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-resetwithdefaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-resetwithdefaults.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the instrument to a known state and sends initialization commands to the DMM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ResetWithDefaults()RemarksThe initialization commands set the DMM settings to the state necessary for the operation of NI-DMM. All user-define

### ResetWithDefaults()

Resets the instrument to a known state and sends initialization commands to the DMM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ResetWithDefaults()

#### Remarks

The initialization commands set the DMM settings to the state necessary for the operation of NI-DMM. All user-defined default values associated with a logical name are applied after setting the DMM.

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-revisionquery__out-out.html language=enus -->
## TOPIC 00101: RevisionQuery(out string, out string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-revisionquery__out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-revisionquery__out-out.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the revision numbers of the instrument driver and instrument firmware. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void RevisionQuery(out string instrumentDriverRevision, out string firmwareRevision)ParametersNameTypeDescriptioninstrumentDriverRevisionout stringReturn

### RevisionQuery(out string, out string)

Returns the revision numbers of the instrument driver and instrument firmware.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void RevisionQuery(out string instrumentDriverRevision, out string firmwareRevision)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrumentDriverRevision | out string | Returns a string containing the instrument driver software revision numbers. |
| firmwareRevision | out string | Returns a string containing the instrument firmware revision numbers. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | A failure occurred when reading the firmware revision. |

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html language=enus -->
## TOPIC 00102: SelfTest()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-test on the DMM to ensure that the DMM is functioning properly. Self-test does not calibrate the DMM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmSelfTestResult SelfTest()RemarksThis method calls Reset, and any configurations previous to the call will be lo

### SelfTest()

Performs a self-test on the DMM to ensure that the DMM is functioning properly. Self-test does not calibrate the DMM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmSelfTestResult](nationalinstruments-modularinstruments-nidmm-dmmselftestresult.html) SelfTest()

#### Remarks

This method calls [Reset](nationalinstruments-modularinstruments-nidmm-dmmdriverutility-reset.html), and any configurations previous to the call will be lost. All properties will be set to their default values after the call returns.

#### Returns

Returns error code and self-test status message.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | Either the method failed for AC measurements, OR the method failed for DC measurements, OR the method failed for resistance measurements. |

Parent topic:

DmmDriverUtility Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmdriverutility.html language=enus -->
## TOPIC 00103: DmmDriverUtility Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmdriverutility.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmdriverutility.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides additional, optional functionality for NI-DMM in your application. Derives fromDmmSubObjectIIviDriverUtilitySyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmDriverUtility : DmmSubObject, IIviDriverUtilityRemarksProvides additional, optional functionality for NI-D

### DmmDriverUtility Class

Provides additional, optional functionality for NI-DMM in your application.

#### Derives from

- DmmSubObject
- IIviDriverUtility

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmDriverUtility : DmmSubObject, IIviDriverUtility

#### Remarks

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Methods

| Name | Description |
| --- | --- |
| NI4022Control(string, Dmm4022ConfigurationMode) | Configures the NI 4022 module. |
| ClearError() | Clears all errors. |
| Disable() | Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected. |
| ErrorQuery() | Reads an error code and message from the DMM error queue. |
| ExportAttributeConfigurationBuffer() | Exports the attribute configuration of the session to the specified System.Byte array buffer. |
| ExportAttributeConfigurationFile(string) | Exports the attribute configuration of the session to the specified file. |
| ImportAttributeConfigurationBuffer(byte[]) | Imports an attribute configuration to the session from the specified configuration . |
| ImportAttributeConfigurationFile(string) | Imports an attribute configuration to the session from the specified file. |
| Lock(Ivi.Driver.PrecisionTimeSpan) | Attempts to acquire a synchronization lock on this instance of the driver. |
| Lock() | Attempts to acquire a synchronization lock on this instance of the driver. The calling thread is blocked indefinitely until the lock is acquired. |
| Reset() | Resets the instrument to a known state and sends initialization commands to the instrument. |
| ResetWithDefaults() | Resets the instrument to a known state and sends initialization commands to the DMM. |
| RevisionQuery(out string, out string) | Returns the revision numbers of the instrument driver and instrument firmware. |
| SelfTest() | Performs a self-test on the DMM to ensure that the DMM is functioning properly. Self-test does not calibrate the DMM. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorange.html language=enus -->
## TOPIC 00104: VoltageAutoRange

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorange.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the frequency voltage is auto-ranging. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool VoltageAutoRange { get; set; }Remarkstrue, if the frequency voltage is auto-ranging; false, if it is not. For the NI 4080/4081/4082 and NI 4070/4071

### VoltageAutoRange

Gets or sets a value indicating whether the frequency voltage is auto-ranging.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool VoltageAutoRange { get; set; }

#### Remarks

true, if the frequency voltage is auto-ranging; false, if it is not.

Note

For the NI 4080/4081/4082 and NI 4070/4071/4072 only.

Parent topic:

DmmFrequency Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorangevalue.html language=enus -->
## TOPIC 00105: VoltageAutoRangeValue

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorangevalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorangevalue.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the measurement auto-range value for frequency voltage range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double VoltageAutoRangeValue { get; }RemarksThe value is in units appropriate for the current value of the Ivi.Dmm.MeasurementFunction. For example, if Ivi.Dmm.Measu

### VoltageAutoRangeValue

Gets the measurement auto-range value for frequency voltage range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double VoltageAutoRangeValue { get; }

#### Remarks

The value is in units appropriate for the current value of the Ivi.Dmm.MeasurementFunction. For example, if Ivi.Dmm.MeasurementFunction is set to Ivi.Dmm.MeasurementFunction.ACVolts, the units are volts. The value of this property is only valid if [VoltageAutoRange](nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorange.html) is set to true, and a read or fetch has occurred.

The measurement auto-range value for the frequency voltage range.

Parent topic:

DmmFrequency Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltagerange.html language=enus -->
## TOPIC 00106: VoltageRange

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltagerange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltagerange.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum amplitude of the input signal for frequency measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double VoltageRange { get; set; }RemarksFor the NI 4080/4081/4082 and NI 4070/4071/4072 only. For more information, refer to the Configuring Frequenc

### VoltageRange

Gets or sets the maximum amplitude of the input signal for frequency measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double VoltageRange { get; set; }

#### Remarks

For the NI 4080/4081/4082 and NI 4070/4071/4072 only. For more information, refer to the [Configuring Frequency Measurements](/csh?context=nidmm_dmm_configure_frequency) topic in the *NI Digital Multimeters Help*.

The maximum amplitude of the input signal for frequency measurements.

If [VoltageAutoRange](nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorange.html) is set to true or if VoltageRange is set to -1.0, the DMM is configured to take an auto-range measurement to calculate the voltage range before each frequency or period measurement. If [VoltageAutoRange](nationalinstruments-modularinstruments-nidmm-dmmfrequency-voltageautorange.html) is set to false or if VoltageRange is set to -2.0, auto-ranging is disabled, and NI-DMM sets the voltage range to the last calculated voltage range.

Parent topic:

DmmFrequency Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmfrequency.html language=enus -->
## TOPIC 00107: DmmFrequency Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmfrequency.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides information regarding voltage. Derives fromDmmSubObjectIIviDmmFrequencySyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmFrequency : DmmSubObject, IIviDmmFrequencyRemarksFor more information, refer to the Configuring Frequency Measurements topic in the NI Digital

### DmmFrequency Class

Provides information regarding voltage.

#### Derives from

- DmmSubObject
- IIviDmmFrequency

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmFrequency : DmmSubObject, IIviDmmFrequency

#### Remarks

Configuring Frequency Measurements

NI Digital Multimeters Help

Note

System.ObjectDisposedException is thrown if members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| VoltageAutoRange | Gets or sets a value indicating whether the frequency voltage is auto-ranging. |
| VoltageAutoRangeValue | Gets the measurement auto-range value for frequency voltage range. |
| VoltageRange | Gets or sets the maximum amplitude of the input signal for frequency measurements. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmlccalculationmodel.html language=enus -->
## TOPIC 00108: DmmLCCalculationModel Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmlccalculationmodel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmlccalculationmodel.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LC calculation model. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmLCCalculationModelRemarksFor the NI 4072 only. MembersNameValueDescriptionAuto-1NI-DMM chooses the algorithm based on function and range. Series0NI-DMM uses the series impedance model to c

### DmmLCCalculationModel Enumeration

Specifies the LC calculation model.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmLCCalculationModel

#### Remarks

For the NI 4072 only.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | -1 | NI-DMM chooses the algorithm based on function and range. |
| Series | 0 | NI-DMM uses the series impedance model to calculate capacitance and inductance. |
| Parallel | 1 | NI-DMM uses the parallel admittance model to calculate capacitance and inductance. |

#### See Also

- LCCalculationModel

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-abort.html language=enus -->
## TOPIC 00109: Abort()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-abort.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts a previously initiated measurement and returns the DMM to the idle state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Abort()

### Abort()

Aborts a previously initiated measurement and returns the DMM to the idle state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Abort()

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-control__dmmcontrolaction.html language=enus -->
## TOPIC 00110: Control(DmmControlAction)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-control__dmmcontrolaction.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-control__dmmcontrolaction.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the DMM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Control(DmmControlAction controlAction)RemarksUse this method if you want a parameter change to be immediately reflected in the hardware. Use this method before calling Initiate to make the initiate call as qu

### Control(DmmControlAction)

Controls the DMM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Control(DmmControlAction controlAction)

#### Remarks

Initiate

Note

The NI 4050 and NI 4060 are not supported.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| controlAction | DmmControlAction | The action you want the driver to perform. Only Commit is supported, which commits to hardware all of the configured properties associated with the session. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.ValueNotSupportedException | The parameter value passed is invalid. |
| Ivi.Driver.IOException | Calling this method while the DMM is taking measurements results in an error. After the DMM is finished taking measurements, calling this method will make any unfetched data points unavailable. |

#### See Also

- DmmControlAction

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-dispose.html language=enus -->
## TOPIC 00111: Dispose()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-dispose.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Frees the resources held. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Dispose()

### Dispose()

Frees the resources held.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Dispose()

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetch.html language=enus -->
## TOPIC 00112: Fetch()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetch.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetch.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value from a previously initiated measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Fetch()RemarksYou must call Initiate before calling this method. The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.

### Fetch()

Returns the value from a previously initiated measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Fetch()

#### Remarks

You must call [Initiate](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html) before calling this method. The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue.

#### Returns

The measured value returned from the DMM, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OperationNotSupportedException | You must call Initiate before calling this method. -or- The method is not supported for the given OperationMode. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the acquisition did not complete. The DMM calculates the timeout automatically. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetch__nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00113: Fetch(NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetch__nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetch__nationalinstruments.precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value from a previously initiated measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Fetch(NationalInstruments.PrecisionTimeSpan maximumTime)RemarksYou must call Initiate before calling this method. ParametersNameTypeDescriptionmaximumTimeNationalInst

### Fetch(NationalInstruments.PrecisionTimeSpan)

Returns the value from a previously initiated measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Fetch(NationalInstruments.PrecisionTimeSpan maximumTime)

#### Remarks

You must call [Initiate](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html) before calling this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |

#### Returns

The measured value returned from the DMM, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OperationNotSupportedException | You must call Initiate before calling this method. -or- The method is not supported for the given OperationMode. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__int.html language=enus -->
## TOPIC 00114: FetchMultiPoint(int)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__int.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of values from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] FetchMultiPoint(int pointsToFetch)RemarksThe number of measurements the DMM makes is determined by the values you specify for the triggerCount a

### FetchMultiPoint(int)

Returns an array of values from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] FetchMultiPoint(int pointsToFetch)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters of NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is the (triggerCount x sampleCount) parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |

#### Returns

A System.Double[] array of measured values, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The pointsToFetch parameter value is not positive. |
| Ivi.Driver.OperationNotSupportedException | You must call Initiate to initiate a measurement before calling this method. -or- The method is not supported for the given OperationMode. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger was not received, or if the acquisition did not complete. The DMM calculates the timeout automatically. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__nationalinstruments.precisiontimespan-int.html language=enus -->
## TOPIC 00115: FetchMultiPoint(NationalInstruments.PrecisionTimeSpan, int)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__nationalinstruments.precisiontimespan-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__nationalinstruments.precisiontimespan-int.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of values from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] FetchMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch)RemarksThe number of measurements the DMM makes is determin

### FetchMultiPoint(NationalInstruments.PrecisionTimeSpan, int)

Returns an array of values from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] FetchMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters of NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is the (triggerCount x sampleCount) parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |

#### Returns

A System.Double[] array of measured values, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The pointsToFetch parameter value is not positive. |
| Ivi.Driver.OperationNotSupportedException | You must call Initiate to initiate a measurement before calling this method. -or- The method is not supported for the given OperationMode. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00116: FetchMultiPoint(NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__nationalinstruments.precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of values from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] FetchMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime)RemarksThe number of measurements the DMM makes is determined by the values yo

### FetchMultiPoint(NationalInstruments.PrecisionTimeSpan)

Returns an array of values from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] FetchMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters of NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |

#### Returns

A System.Double[] array of measured values, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OperationNotSupportedException | You must call Initiate to initiate a measurement before calling this method. -or- The method is not supported for the given OperationMode. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__int-object.html language=enus -->
## TOPIC 00117: FetchMultiPointAsync(int, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__int-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__int-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches asynchronously from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void FetchMultiPointAsync(int pointsToFetch, object userState)RemarksThe number of measurements the DMM makes is determined by the values you specify for the

### FetchMultiPointAsync(int, object)

Fetches asynchronously from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void FetchMultiPointAsync(int pointsToFetch, object userState)

#### Remarks

triggerCount

sampleCount

FetchMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

Initiate

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is the (triggerCount x sampleCount) parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__nationalinstruments.precisiontimespan-int-object.html language=enus -->
## TOPIC 00118: FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__nationalinstruments.precisiontimespan-int-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__nationalinstruments.precisiontimespan-int-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches asynchronously from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, object userState)RemarksThe number of measurements the DMM ma

### FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, object)

Fetches asynchronously from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, object userState)

#### Remarks

triggerCount

sampleCount

FetchMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

Initiate

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is the (triggerCount x sampleCount) parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__nationalinstruments.precisiontimespan-object.html language=enus -->
## TOPIC 00119: FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__nationalinstruments.precisiontimespan-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointasync__nationalinstruments.precisiontimespan-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches asynchronously from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, object userState)RemarksThe number of measurements the DMM makes is determined b

### FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, object)

Fetches asynchronously from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, object userState)

#### Remarks

triggerCount

sampleCount

FetchMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

Initiate

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| userState | object | An object used to associate a client state (such as a task ID) with this particular asynchronous operation. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointcompleted.html language=enus -->
## TOPIC 00120: FetchMultiPointCompleted

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointcompleted.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipointcompleted.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when an asynchronous call for a fetch multipoint operation completes. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic EventHandler< DmmMeasurementEventArgs< double[]> > FetchMultiPointCompleted

### FetchMultiPointCompleted

Occurs when an asynchronous call for a fetch multipoint operation completes.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public EventHandler< [DmmMeasurementEventArgs](nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs.html)< double[]> > FetchMultiPointCompleted

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html language=enus -->
## TOPIC 00121: Initiate()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates an acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Initiate()RemarksAfter you call this method, the DMM leaves the Idle state and enters the Wait-for-Trigger state. If trigger is set to Immediate mode, the DMM begins acquiring measurement data. Use Fet

### Initiate()

Initiates an acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Initiate()

#### Remarks

After you call this method, the DMM leaves the Idle state and enters the Wait-for-Trigger state. If trigger is set to Immediate mode, the DMM begins acquiring measurement data. Use [Fetch](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetch.html), [FetchMultiPoint](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__int.html), or [MemoryOptimizedFetchMultiPoint](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipoint__nationalinstruments.precisiontimespan-int-out-ref.html) to retrieve the measurement data, or use [FetchWaveform](nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveform__int-precisiontimespan.html) or [MemoryOptimizedFetchWaveform](nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedfetchwaveform__int-precisiontimespan-analogwaveform_double..html) in [DmmWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition.html).

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-isoverrange__double.html language=enus -->
## TOPIC 00122: IsOverRange(double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-isoverrange__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-isoverrange__double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes a measurement value and determines if the value is a valid measurement or a value indicating that an overrange condition occurred. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool IsOverRange(double measurementValue)ParametersNameTypeDescriptionmeasurementValuedoubleThe

### IsOverRange(double)

Takes a measurement value and determines if the value is a valid measurement or a value indicating that an overrange condition occurred.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool IsOverRange(double measurementValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measurementValue | double | The measured value returned from the DMM. |

#### Returns

A System.Boolean indicating whether the measurement value is a valid measurement or a value indicating an overrange condition.

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-isunderrange__double.html language=enus -->
## TOPIC 00123: IsUnderRange(double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-isunderrange__double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-isunderrange__double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Takes a measurement value and determines if the value is a valid measurement or a value indicating that an underrange condition occurred. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool IsUnderRange(double measurementValue)ParametersNameTypeDescriptionmeasurementValuedoubleT

### IsUnderRange(double)

Takes a measurement value and determines if the value is a valid measurement or a value indicating that an underrange condition occurred.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool IsUnderRange(double measurementValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measurementValue | double | The measured value returned from the DMM. |

#### Returns

A System.Boolean indicating whether the measurement value is a valid measurement or a value indicating an underrange condition.

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipoint__int-out-ref.html language=enus -->
## TOPIC 00124: MemoryOptimizedFetchMultiPoint(int, out int, ref double[])

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipoint__int-out-ref.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipoint__int-out-ref.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of values from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] MemoryOptimizedFetchMultiPoint(int pointsToFetch, out int actualNumberOfPoints, ref double[] reading)RemarksThe number of measurements the DMM m

### MemoryOptimizedFetchMultiPoint(int, out int, ref double[])

Returns an array of values from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] MemoryOptimizedFetchMultiPoint(int pointsToFetch, out int actualNumberOfPoints, ref double[] reading)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters of NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| reading | ref double[] | Specifies the double array where the fetched values will be populated. If the length of reading is less than pointsToFetch , the length is resized to pointsToFetch . |
| actualNumberOfPoints | out int | Specifies the actual number of points fetched. |

#### Returns

A System.Double[] array of measured values, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The pointsToFetch parameter value is not positive. |
| System.ArgumentNullException | The parameter value passed is null. |
| Ivi.Driver.OperationNotSupportedException | You must call Initiate to initiate a measurement before calling this method. -or- The method is not supported for the given OperationMode. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. The DMM calculates the timeout automatically. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipoint__nationalinstruments.precisiontimespan-int-out-ref.html language=enus -->
## TOPIC 00125: MemoryOptimizedFetchMultiPoint(NationalInstruments.PrecisionTimeSpan, int, out int, ref double[])

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipoint__nationalinstruments.precisiontimespan-int-out-ref.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipoint__nationalinstruments.precisiontimespan-int-out-ref.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of values from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] MemoryOptimizedFetchMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, out int actualNumberOfPoints, ref double[]

### MemoryOptimizedFetchMultiPoint(NationalInstruments.PrecisionTimeSpan, int, out int, ref double[])

Returns an array of values from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] MemoryOptimizedFetchMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, out int actualNumberOfPoints, ref double[] reading)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters of NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| reading | ref double[] | Specifies the double array where the fetched values will be populated. If the length of reading is less than pointsToFetch , the length will be resized to pointsToFetch . |
| actualNumberOfPoints | out int | Specifies the actual number of points fetched. |

#### Returns

A System.Double[] array of measured values, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The pointsToFetch parameter value is not positive. |
| System.ArgumentNullException | The parameter value passed is null. |
| Ivi.Driver.OperationNotSupportedException | You must call Initiate to initiate a measurement before calling this method. -or- The method is not supported for the given OperationMode. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipointasync__int-double_arr1-object.html language=enus -->
## TOPIC 00126: MemoryOptimizedFetchMultiPointAsync(int, double[], object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipointasync__int-double_arr1-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipointasync__int-double_arr1-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches asynchronously from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void MemoryOptimizedFetchMultiPointAsync(int pointsToFetch, double[] reading, object userState)RemarksThe number of measurements the DMM makes is determined

### MemoryOptimizedFetchMultiPointAsync(int, double[], object)

Fetches asynchronously from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void MemoryOptimizedFetchMultiPointAsync(int pointsToFetch, double[] reading, object userState)

#### Remarks

triggerCount

sampleCount

FetchMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

Initiate

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| reading | double[] | Specifies the double array where the fetched values will be populated. If the length of reading is less than pointsToFetch , it will be resized to pointsToFetch . |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |
| System.ArgumentNullException | The parameter value passed is null. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipointasync__nationalinstruments.precisiontimespan-int-double_arr1-object.html language=enus -->
## TOPIC 00127: MemoryOptimizedFetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, double[], object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipointasync__nationalinstruments.precisiontimespan-int-double_arr1-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipointasync__nationalinstruments.precisiontimespan-int-double_arr1-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches asynchronously from a previously initiated multipoint measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void MemoryOptimizedFetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, double[] reading, object userState)RemarksThe

### MemoryOptimizedFetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, double[], object)

Fetches asynchronously from a previously initiated multipoint measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void MemoryOptimizedFetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, double[] reading, object userState)

#### Remarks

triggerCount

sampleCount

FetchMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

Initiate

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| reading | double[] | Specifies the double array where the fetched values will be populated. If the length of reading is less than pointsToFetch , it will be resized to pointsToFetch . |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |
| System.ArgumentNullException | The parameter value passed is null. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipoint__int-out-ref.html language=enus -->
## TOPIC 00128: MemoryOptimizedReadMultiPoint(int, out int, ref double[])

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipoint__int-out-ref.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipoint__int-out-ref.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires multiple measurements and returns an array of measured values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] MemoryOptimizedReadMultiPoint(int pointsToFetch, out int actualNumberOfPoints, ref double[] reading)RemarksThe number of measurements the DMM makes is

### MemoryOptimizedReadMultiPoint(int, out int, ref double[])

Acquires multiple measurements and returns an array of measured values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] MemoryOptimizedReadMultiPoint(int pointsToFetch, out int actualNumberOfPoints, ref double[] reading)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| reading | ref double[] | Specifies the double array where the fetched values will be populated. If the length of reading is less than pointsToFetch , the length will be resized to pointsToFetch . |
| actualNumberOfPoints | out int | Specifies the actual number of points fetched. |

#### Returns

Note

The size of the *reading* array must be at least the size that you specify for the *pointsToFetch* parameter.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The pointsToFetch parameter value is not positive. |
| System.ArgumentNullException | The parameter value passed is null. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. The DMM calculates the timeout automatically. |
| Ivi.Driver.OperationNotSupportedException | The method is not supported for the given OperationMode. |
| Ivi.Driver.IviCDriverException | The number of points read is not equal to the number of points requested. -or- The measurement status returned by the hardware is not valid. Try decreasing the acquisition rate or the acquisition size. Alternatively, you can try upgrading the performance of your system by increasing the processor speed, memory, or both. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipoint__nationalinstruments.precisiontimespan-int-out-ref.html language=enus -->
## TOPIC 00129: MemoryOptimizedReadMultiPoint(NationalInstruments.PrecisionTimeSpan, int, out int, ref double[])

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipoint__nationalinstruments.precisiontimespan-int-out-ref.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipoint__nationalinstruments.precisiontimespan-int-out-ref.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires multiple measurements and returns an array of measured values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] MemoryOptimizedReadMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, out int actualNumberOfPoints, ref double[] reading)

### MemoryOptimizedReadMultiPoint(NationalInstruments.PrecisionTimeSpan, int, out int, ref double[])

Acquires multiple measurements and returns an array of measured values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] MemoryOptimizedReadMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, out int actualNumberOfPoints, ref double[] reading)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (*triggerCount* x *sampleCount*).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| reading | ref double[] | Specifies the double array where the fetched values will be populated. If the length of reading is less than pointsToFetch , the length will be resized to pointsToFetch . |
| actualNumberOfPoints | out int | Specifies the actual number of points fetched. |

#### Returns

Note

The size of the *reading* array must be at least the size that you specify for the *pointsToFetch* parameter.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The pointsToFetch parameter value is not positive. |
| System.ArgumentNullException | The parameter value passed is null. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |
| Ivi.Driver.OperationNotSupportedException | The method is not supported for the given OperationMode. |
| Ivi.Driver.IviCDriverException | The number of points read is not equal to the number of points requested. -or- The measurement status returned by the hardware is not valid. Try decreasing the acquisition rate or the acquisition size. Alternatively, you can try upgrading the performance of your system by increasing the processor speed, memory, or both. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipointasync__int-double_arr1-object.html language=enus -->
## TOPIC 00130: MemoryOptimizedReadMultiPointAsync(int, double[], object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipointasync__int-double_arr1-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipointasync__int-double_arr1-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously acquires multiple measurements and fetches an array of measured values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void MemoryOptimizedReadMultiPointAsync(int pointsToFetch, double[] reading, object userState)RemarksReadMultiPointCompleted is raised once this

### MemoryOptimizedReadMultiPointAsync(int, double[], object)

Asynchronously acquires multiple measurements and fetches an array of measured values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void MemoryOptimizedReadMultiPointAsync(int pointsToFetch, double[] reading, object userState)

#### Remarks

ReadMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

A Ivi.Driver.IviCDriverException error occurs if the number of points read is not equal to the number of points requested, or if the measurement status returned by the hardware is not valid.

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| reading | double[] | Specifies the double array where the fetched values will be populated. If the length of reading is less than pointsToFetch , the length will be resized to pointsToFetch . |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |
| System.ArgumentNullException | The parameter value passed is null. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipointasync__nationalinstruments.precisiontimespan-int-double_arr1-object.html language=enus -->
## TOPIC 00131: MemoryOptimizedReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, double[], object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipointasync__nationalinstruments.precisiontimespan-int-double_arr1-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedreadmultipointasync__nationalinstruments.precisiontimespan-int-double_arr1-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously acquires multiple measurements and returns an array of measured values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void MemoryOptimizedReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, double[] reading, object userState)

### MemoryOptimizedReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, double[], object)

Asynchronously acquires multiple measurements and returns an array of measured values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void MemoryOptimizedReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, double[] reading, object userState)

#### Remarks

ReadMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

A Ivi.Driver.IviCDriverException error occurs if the number of points read is not equal to the number of points requested, or if the measurement status returned by the hardware is not valid.

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| reading | double[] | Specifies the double array where the fetched values will be populated. If the length of reading is less than pointsToFetch , the length will be resized to pointsToFetch . |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |
| System.ArgumentNullException | The parameter value passed is null. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-read.html language=enus -->
## TOPIC 00132: Read()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-read.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-read.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires a single measurement and fetches the measured value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Read()RemarksThe maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue. ReturnsThe measured value returned from

### Read()

Acquires a single measurement and fetches the measured value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Read()

#### Remarks

The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue.

#### Returns

The measured value returned from the DMM, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. The DMM calculates the timeout automatically. |
| Ivi.Driver.OperationNotSupportedException | The method is not supported for the given OperationMode. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-read__nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00133: Read(NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-read__nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-read__nationalinstruments.precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires a single measurement and returns the measured value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Read(NationalInstruments.PrecisionTimeSpan maximumTime)ParametersNameTypeDescriptionmaximumTimeNationalInstruments.PrecisionTimeSpanSpecifies the maximum time allo

### Read(NationalInstruments.PrecisionTimeSpan)

Acquires a single measurement and returns the measured value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Read(NationalInstruments.PrecisionTimeSpan maximumTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |

#### Returns

The measured value returned from the DMM, in base units.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |
| Ivi.Driver.OperationNotSupportedException | The method is not supported for the given OperationMode. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readasync__nationalinstruments.precisiontimespan-object.html language=enus -->
## TOPIC 00134: ReadAsync(NationalInstruments.PrecisionTimeSpan, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readasync__nationalinstruments.precisiontimespan-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readasync__nationalinstruments.precisiontimespan-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires a single measurement and returns the measured value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ReadAsync(NationalInstruments.PrecisionTimeSpan maximumTime, object userState)RemarksReadCompleted is raised once this operation completes. If an asynchronous method

### ReadAsync(NationalInstruments.PrecisionTimeSpan, object)

Acquires a single measurement and returns the measured value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ReadAsync(NationalInstruments.PrecisionTimeSpan maximumTime, object userState)

#### Remarks

ReadCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readasync__object.html language=enus -->
## TOPIC 00135: ReadAsync(object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readasync__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readasync__object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously acquires a single measurement and returns the measured value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ReadAsync(object userState)RemarksReadCompleted is raised after this operation completes. If an asynchronous method is called before the completion of

### ReadAsync(object)

Asynchronously acquires a single measurement and returns the measured value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ReadAsync(object userState)

#### Remarks

ReadCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readcompleted.html language=enus -->
## TOPIC 00136: ReadCompleted

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readcompleted.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readcompleted.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when an asynchronous call for the read singlepoint operation completes. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic EventHandler< DmmMeasurementEventArgs< double > > ReadCompleted

### ReadCompleted

Occurs when an asynchronous call for the read singlepoint operation completes.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public EventHandler< [DmmMeasurementEventArgs](nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs.html)< double > > ReadCompleted

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__int.html language=enus -->
## TOPIC 00137: ReadMultiPoint(int)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__int.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires multiple measurements and returns an array of values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] ReadMultiPoint(int pointsToFetch)RemarksThe number of measurements the DMM makes is determined by the values you specify for the triggerCount and sampleCount pa

### ReadMultiPoint(int)

Acquires multiple measurements and returns an array of values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] ReadMultiPoint(int pointsToFetch)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |

#### Returns

Note

The size of the reading array must be at least the size that you specify for the *pointsToFetch* parameter.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The pointsToFetch parameter value is not positive. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. The DMM calculates the timeout automatically. |
| Ivi.Driver.OperationNotSupportedException | The method is not supported for the given OperationMode. |
| Ivi.Driver.IviCDriverException | The number of points read is not equal to the number of points requested. -or- The measurement status returned by the hardware is not valid. Try decreasing the acquisition rate or the acquisition size. Alternatively, you can try upgrading the performance of your system by increasing the processor speed, memory, or both. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__nationalinstruments.precisiontimespan-int.html language=enus -->
## TOPIC 00138: ReadMultiPoint(NationalInstruments.PrecisionTimeSpan, int)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__nationalinstruments.precisiontimespan-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__nationalinstruments.precisiontimespan-int.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires multiple measurements and returns an array of values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] ReadMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch)RemarksThe number of measurements the DMM makes is determined by the values

### ReadMultiPoint(NationalInstruments.PrecisionTimeSpan, int)

Acquires multiple measurements and returns an array of values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] ReadMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |

#### Returns

Note

The size of the *reading* array must be at least the size that you specify for the *pointsToFetch* parameter.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The pointsToFetch parameter value is not positive. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |
| Ivi.Driver.OperationNotSupportedException | The method is not supported for the given OperationMode. |
| Ivi.Driver.IviCDriverException | The number of points read is not equal to the number of points requested. -or- The measurement status returned by the hardware is not valid. Try decreasing the acquisition rate or the acquisition size. Alternatively, you can try upgrading the performance of your system by increasing the processor speed, memory, or both. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00139: ReadMultiPoint(NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipoint__nationalinstruments.precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires multiple measurements and returns an array of values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double[] ReadMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime)RemarksThe number of measurements the DMM makes is determined by the values you specify for the

### ReadMultiPoint(NationalInstruments.PrecisionTimeSpan)

Acquires multiple measurements and returns an array of values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double[] ReadMultiPoint(NationalInstruments.PrecisionTimeSpan maximumTime)

#### Remarks

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |

#### Returns

Note

The size of the *reading* array must be at least the size that you specify for the *pointsToFetch* parameter.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IOTimeoutException | The method does not complete within the specified time interval. This exception happens if the specified timeout is not long enough for the acquisition to complete. |
| Ivi.Driver.OperationNotSupportedException | The method is not supported for the given OperationMode. |
| Ivi.Driver.IviCDriverException | The number of points read is not equal to the number of points requested. -or- The measurement status returned by the hardware is not valid. Try decreasing the acquisition rate or the acquisition size. Alternatively, you can try upgrading the performance of your system by increasing the processor speed, memory, or both. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__int-object.html language=enus -->
## TOPIC 00140: ReadMultiPointAsync(int, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__int-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__int-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously acquires multiple measurements and returns an array of values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ReadMultiPointAsync(int pointsToFetch, object userState)RemarksReadMultiPointCompleted is raised once this operation completes. If an asynchronous me

### ReadMultiPointAsync(int, object)

Asynchronously acquires multiple measurements and returns an array of values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ReadMultiPointAsync(int pointsToFetch, object userState)

#### Remarks

ReadMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

A Ivi.Driver.IviCDriverException error occurs if the number of points read is not equal to the number of points requested, or if the measurement status returned by the hardware is not valid.

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. The maximum time allowed for this method to complete is set to NationalInstruments.PrecisionTimeSpan.MaxValue.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__nationalinstruments.precisiontimespan-int-object.html language=enus -->
## TOPIC 00141: ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__nationalinstruments.precisiontimespan-int-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__nationalinstruments.precisiontimespan-int-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously acquires multiple measurements and returns an array of values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, object userState)RemarksReadMultiPointCompleted is raised o

### ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, object)

Asynchronously acquires multiple measurements and returns an array of values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, int pointsToFetch, object userState)

#### Remarks

ReadMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

A Ivi.Driver.IviCDriverException error occurs if the number of points read is not equal to the number of points requested, or if the measurement status returned by the hardware is not valid.

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of measurements to acquire. The maximum number of measurements for a finite acquisition is determined by the parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure (triggerCount x sampleCount). For continuous acquisitions, up to 100,000 points can be returned at once. The number of measurements can be a subset. The valid range is any positive integer. The default value is 1. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__nationalinstruments.precisiontimespan-object.html language=enus -->
## TOPIC 00142: ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__nationalinstruments.precisiontimespan-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointasync__nationalinstruments.precisiontimespan-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously acquires multiple measurements and returns an array of values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, object userState)RemarksReadMultiPointCompleted is raised once this operation

### ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, object)

Asynchronously acquires multiple measurements and returns an array of values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan maximumTime, object userState)

#### Remarks

ReadMultiPointCompleted

userState

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

A Ivi.Driver.IviCDriverException error occurs if the number of points read is not equal to the number of points requested, or if the measurement status returned by the hardware is not valid.

The number of measurements the DMM makes is determined by the values you specify for the *triggerCount* and *sampleCount* parameters in NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | NationalInstruments.PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. If maximumTime is set to NationalInstruments.PrecisionTimeSpan.MaxValue, the NI-DMM driver calculates the timeout automatically. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointcompleted.html language=enus -->
## TOPIC 00143: ReadMultiPointCompleted

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointcompleted.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readmultipointcompleted.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when an asynchronous call for the read multipoint operation completes. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic EventHandler< DmmMeasurementEventArgs< double[]> > ReadMultiPointCompleted

### ReadMultiPointCompleted

Occurs when an asynchronous call for the read multipoint operation completes.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public EventHandler< [DmmMeasurementEventArgs](nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs.html)< double[]> > ReadMultiPointCompleted

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readstatus__out.html language=enus -->
## TOPIC 00144: ReadStatus(out int)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readstatus__out.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-readstatus__out.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns measurement backlog and acquisition status. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmAcquisitionStatus ReadStatus(out int acquisitionBacklog)RemarksUse this method to determine how many measurements are available before calling Fetch, FetchMultiPoint, MemoryOpti

### ReadStatus(out int)

Returns measurement backlog and acquisition status.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmAcquisitionStatus](nationalinstruments-modularinstruments-nidmm-dmmacquisitionstatus.html) ReadStatus(out int acquisitionBacklog)

#### Remarks

Use this method to determine how many measurements are available before calling [Fetch](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetch.html), [FetchMultiPoint](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-fetchmultipoint__int.html), [MemoryOptimizedFetchMultiPoint](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-memoryoptimizedfetchmultipoint__nationalinstruments.precisiontimespan-int-out-ref.html), [FetchWaveform](nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveform__int-precisiontimespan.html), or [MemoryOptimizedFetchWaveform](nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedfetchwaveform__int-precisiontimespan-analogwaveform_double..html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| acquisitionBacklog | out int | The number of measurements available to be read. If the backlog continues to increase, data is eventually overwritten, resulting in an error. Note On the NI 4060, the backlog does not increase when autoranging. On the NI 4065, the backlog does not increase when AutoRange is On, or before the first point is fetched when AutoRange is Once. These behaviors are due to the autorange model of the devices. |

#### Returns

Indicates the status of the acquisition.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The measurement status returned by the hardware is not valid. Try decreasing the acquisition rate or the acquisition size. Alternatively, you can try upgrading the performance of your system by increasing the processor speed, memory, or both. |

#### See Also

- DmmAcquisitionStatus

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-sendsoftwaretrigger.html language=enus -->
## TOPIC 00145: SendSoftwareTrigger()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-sendsoftwaretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-sendsoftwaretrigger.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a command to trigger the DMM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void SendSoftwareTrigger()RemarksCall this method if you have configured either the Source or SampleTrigger. If the Source or SampleTrigger is set to External or TTLn, you can use this method to o

### SendSoftwareTrigger()

Sends a command to trigger the DMM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void SendSoftwareTrigger()

#### Remarks

Call this method if you have configured either the [Source](nationalinstruments-modularinstruments-nidmm-dmmtrigger-source.html) or [SampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampletrigger.html). If the [Source](nationalinstruments-modularinstruments-nidmm-dmmtrigger-source.html) or [SampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampletrigger.html) is set to External or TTLn, you can use this method to override the trigger source that you configured and trigger the NI 4065 and NI 4070/4071/4072.

#### See Also

- DmmTrigger
- DmmMultiPoint

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement-synchronizecallbacks.html language=enus -->
## TOPIC 00146: SynchronizeCallbacks

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement-synchronizecallbacks.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the events and callback delegates are invoked through the System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool SynchronizeCallbacks { get;

### SynchronizeCallbacks

Gets or sets a value indicating whether the events and callback delegates are invoked through the System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

true if events and callbacks are invoked through the System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods; otherwise, events and callbacks are invoked directly. The default value is true.

Parent topic:

DmmMeasurement Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurement.html language=enus -->
## TOPIC 00147: DmmMeasurement Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurement.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties to acquire data from a measurement. Derives fromDmmSubObjectIIviDmmMeasurementISupportSynchronizationContextIDisposableSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmMeasurement : DmmSubObject, IIviDmmMeasurement, ISupportSynchronizationContext, IDis

### DmmMeasurement Class

Provides properties to acquire data from a measurement.

#### Derives from

- DmmSubObject
- IIviDmmMeasurement
- ISupportSynchronizationContext
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmMeasurement : DmmSubObject, IIviDmmMeasurement, ISupportSynchronizationContext, IDisposable

#### Remarks

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Gets or sets a value indicating whether the events and callback delegates are invoked through the System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods. |

#### Methods

| Name | Description |
| --- | --- |
| Abort() | Aborts a previously initiated measurement and returns the DMM to the idle state. |
| Control(DmmControlAction) | Controls the DMM. |
| Dispose() | Frees the resources held. |
| Fetch(NationalInstruments.PrecisionTimeSpan) | Returns the value from a previously initiated measurement. |
| Fetch() | Returns the value from a previously initiated measurement. |
| FetchMultiPoint(NationalInstruments.PrecisionTimeSpan, int) | Returns an array of values from a previously initiated multipoint measurement. |
| FetchMultiPoint(int) | Returns an array of values from a previously initiated multipoint measurement. |
| FetchMultiPoint(NationalInstruments.PrecisionTimeSpan) | Returns an array of values from a previously initiated multipoint measurement. |
| FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, object) | Fetches asynchronously from a previously initiated multipoint measurement. |
| FetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, object) | Fetches asynchronously from a previously initiated multipoint measurement. |
| FetchMultiPointAsync(int, object) | Fetches asynchronously from a previously initiated multipoint measurement. |
| Initiate() | Initiates an acquisition. |
| IsOverRange(double) | Takes a measurement value and determines if the value is a valid measurement or a value indicating that an overrange condition occurred. |
| IsUnderRange(double) | Takes a measurement value and determines if the value is a valid measurement or a value indicating that an underrange condition occurred. |
| MemoryOptimizedFetchMultiPoint(int, out int, ref double[]) | Returns an array of values from a previously initiated multipoint measurement. |
| MemoryOptimizedFetchMultiPoint(NationalInstruments.PrecisionTimeSpan, int, out int, ref double[]) | Returns an array of values from a previously initiated multipoint measurement. |
| MemoryOptimizedFetchMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, double[], object) | Fetches asynchronously from a previously initiated multipoint measurement. |
| MemoryOptimizedFetchMultiPointAsync(int, double[], object) | Fetches asynchronously from a previously initiated multipoint measurement. |
| MemoryOptimizedReadMultiPoint(int, out int, ref double[]) | Acquires multiple measurements and returns an array of measured values. |
| MemoryOptimizedReadMultiPoint(NationalInstruments.PrecisionTimeSpan, int, out int, ref double[]) | Acquires multiple measurements and returns an array of measured values. |
| MemoryOptimizedReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, double[], object) | Asynchronously acquires multiple measurements and returns an array of measured values. |
| MemoryOptimizedReadMultiPointAsync(int, double[], object) | Asynchronously acquires multiple measurements and fetches an array of measured values. |
| Read(NationalInstruments.PrecisionTimeSpan) | Acquires a single measurement and returns the measured value. |
| Read() | Acquires a single measurement and fetches the measured value. |
| ReadAsync(NationalInstruments.PrecisionTimeSpan, object) | Acquires a single measurement and returns the measured value. |
| ReadAsync(object) | Asynchronously acquires a single measurement and returns the measured value. |
| ReadMultiPoint(int) | Acquires multiple measurements and returns an array of values. |
| ReadMultiPoint(NationalInstruments.PrecisionTimeSpan, int) | Acquires multiple measurements and returns an array of values. |
| ReadMultiPoint(NationalInstruments.PrecisionTimeSpan) | Acquires multiple measurements and returns an array of values. |
| ReadMultiPointAsync(int, object) | Asynchronously acquires multiple measurements and returns an array of values. |
| ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, object) | Asynchronously acquires multiple measurements and returns an array of values. |
| ReadMultiPointAsync(NationalInstruments.PrecisionTimeSpan, int, object) | Asynchronously acquires multiple measurements and returns an array of values. |
| ReadStatus(out int) | Returns measurement backlog and acquisition status. |
| SendSoftwareTrigger() | Sends a command to trigger the DMM. |

#### Events

| Name | Description |
| --- | --- |
| FetchMultiPointCompleted | Occurs when an asynchronous call for a fetch multipoint operation completes. |
| ReadCompleted | Occurs when an asynchronous call for the read singlepoint operation completes. |
| ReadMultiPointCompleted | Occurs when an asynchronous call for the read multipoint operation completes. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-equals__object.html language=enus -->
## TOPIC 00148: Equals(object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-equals__object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified object is a DmmMeasurementCompleteDestination and is equivalent to this DmmMeasurementCompleteDestination object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectThe System.Obje

### Equals(object)

Determines whether the specified object is a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) and is equivalent to this [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The System.Object to test. |

#### Returns

true if the specified System.Object is a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) and is equivalent to this [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-external.html language=enus -->
## TOPIC 00149: External

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-external.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-external.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing pin 6 on the AUX connector (External). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination External { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To det

### External

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing pin 6 on the AUX connector (External).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) External { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-fromstring__string.html language=enus -->
## TOPIC 00150: FromString(string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-fromstring__string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a DmmMeasurementCompleteDestination object that represents the specified trigger source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination FromString(string source)ParametersNameTypeDescriptionsourcestringThe trigger source specified

### FromString(string)

Returns a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object that represents the specified trigger source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) FromString(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The trigger source specified as a System.String. |

#### Returns

A [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object that represents the specified trigger destination.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-gethashcode.html language=enus -->
## TOPIC 00151: GetHashCode()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-gethashcode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a hash code for this DmmMeasurementCompleteDestination object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override int GetHashCode()ReturnsAn integer value that specifies a hash code for this DmmMeasurementCompleteDestination object.

### GetHashCode()

Returns a hash code for this [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override int GetHashCode()

#### Returns

An integer value that specifies a hash code for this [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-lbrtrig0.html language=enus -->
## TOPIC 00152: LbrTrig0

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-lbrtrig0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-lbrtrig0.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing the Local Bus Right Trigger Line 0 of a PXI/SCXI combination chassis (LbrTig1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination LbrTrig0 { get; }RemarksReturns an object of type

### LbrTrig0

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing the Local Bus Right Trigger Line 0 of a PXI/SCXI combination chassis (LbrTig1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) LbrTrig0 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-none.html language=enus -->
## TOPIC 00153: None

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-none.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-none.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing no specific trigger destination (None). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination None { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determ

### None

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing no specific trigger destination (None).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) None { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-tostring.html language=enus -->
## TOPIC 00154: ToString()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-tostring.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts this DmmMeasurementCompleteDestination to a human-readable string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override string ToString()ReturnsA System.String that corresponds to this DmmMeasurementCompleteDestination.

### ToString()

Converts this [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) to a human-readable string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override string ToString()

#### Returns

A System.String that corresponds to this [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl0.html language=enus -->
## TOPIC 00155: Ttl0

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl0.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 0 (Ttl0). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination Ttl0 { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determine which val

### Ttl0

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing PXI Trigger Line 0 (Ttl0).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) Ttl0 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl1.html language=enus -->
## TOPIC 00156: Ttl1

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl1.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 1 (Ttl1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination Ttl1 { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determine which val

### Ttl1

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing PXI Trigger Line 1 (Ttl1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) Ttl1 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl2.html language=enus -->
## TOPIC 00157: Ttl2

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl2.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 2 (Ttl2). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination Ttl2 { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determine which val

### Ttl2

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing PXI Trigger Line 2 (Ttl2).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) Ttl2 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl3.html language=enus -->
## TOPIC 00158: Ttl3

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl3.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 3 (Ttl3). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination Ttl3 { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determine which val

### Ttl3

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing PXI Trigger Line 3 (Ttl3).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) Ttl3 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl4.html language=enus -->
## TOPIC 00159: Ttl4

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl4.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 4 (Ttl4). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination Ttl4 { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determine which val

### Ttl4

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing PXI Trigger Line 4 (Ttl4).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) Ttl4 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl5.html language=enus -->
## TOPIC 00160: Ttl5

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl5.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 5 (Ttl5). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination Ttl5 { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determine which val

### Ttl5

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing PXI Trigger Line 5 (Ttl5).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) Ttl5 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl6.html language=enus -->
## TOPIC 00161: Ttl6

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl6.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 6 (Ttl6). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination Ttl6 { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determine which val

### Ttl6

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing PXI Trigger Line 6 (Ttl6).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) Ttl6 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl7.html language=enus -->
## TOPIC 00162: Ttl7

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination-ttl7.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 7 (Ttl7). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmMeasurementCompleteDestination Ttl7 { get; }RemarksReturns an object of type DmmMeasurementCompleteDestination. To determine which val

### Ttl7

Gets a [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) object representing PXI Trigger Line 7 (Ttl7).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) Ttl7 { get; }

#### Remarks

Returns an object of type [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMeasurementCompleteDestination Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html language=enus -->
## TOPIC 00163: DmmMeasurementCompleteDestination Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination of the Measurement Complete (MC) signal, which is issued when the DMM completes a single measurement. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmMeasurementCompleteDestinationRemarksA digital trigger generated after taking a

### DmmMeasurementCompleteDestination Class

Specifies the destination of the Measurement Complete (MC) signal, which is issued when the DMM completes a single measurement.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmMeasurementCompleteDestination

#### Remarks

A digital trigger generated after taking a measurement is called Measurement Complete (MC).

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| External | Gets a DmmMeasurementCompleteDestination object representing pin 6 on the AUX connector (External). |
| LbrTrig0 | Gets a DmmMeasurementCompleteDestination object representing the Local Bus Right Trigger Line 0 of a PXI/SCXI combination chassis (LbrTig1). |
| None | Gets a DmmMeasurementCompleteDestination object representing no specific trigger destination (None). |
| Ttl0 | Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 0 (Ttl0). |
| Ttl1 | Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 1 (Ttl1). |
| Ttl2 | Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 2 (Ttl2). |
| Ttl3 | Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 3 (Ttl3). |
| Ttl4 | Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 4 (Ttl4). |
| Ttl5 | Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 5 (Ttl5). |
| Ttl6 | Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 6 (Ttl6). |
| Ttl7 | Gets a DmmMeasurementCompleteDestination object representing PXI Trigger Line 7 (Ttl7). |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Returns a DmmMeasurementCompleteDestination object that represents the specified trigger source. |
| Equals(object) | Determines whether the specified object is a DmmMeasurementCompleteDestination and is equivalent to this DmmMeasurementCompleteDestination object. |
| GetHashCode() | Returns a hash code for this DmmMeasurementCompleteDestination object. |
| ToString() | Converts this DmmMeasurementCompleteDestination to a human-readable string. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-actualnumberofpoints.html language=enus -->
## TOPIC 00164: ActualNumberOfPoints

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-actualnumberofpoints.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-actualnumberofpoints.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of measurement points obtained from the async measurement operation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int ActualNumberOfPoints { get; }RemarksYou can use this property for multipoint methods that take a reading array as a parameter. This property is

### ActualNumberOfPoints

Gets the number of measurement points obtained from the async measurement operation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int ActualNumberOfPoints { get; }

#### Remarks

You can use this property for multipoint methods that take a reading array as a parameter. This property is 1 for single point measurement and contains the length of the reading array for multipoint methods that do not take a reading array as a parameter.

The number of measured values actually retrieved from the DMM.

Parent topic:

DmmMeasurementEventArgs<T> Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-dmmmeasurementeventargs__exception-bool-object-t-int.html language=enus -->
## TOPIC 00165: DmmMeasurementEventArgs(Exception, bool, object, T, int)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-dmmmeasurementeventargs__exception-bool-object-t-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-dmmmeasurementeventargs__exception-bool-object-t-int.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NationalInstruments.ModularInstruments.NIDmm.DmmMeasurementEventArgs<T> class. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmMeasurementEventArgs(Exception error, bool canceled, object userState, T reading, int numberOfPoints)ParametersNameT

### DmmMeasurementEventArgs(Exception, bool, object, T, int)

Initializes a new instance of the NationalInstruments.ModularInstruments.NIDmm.DmmMeasurementEventArgs<T> class.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public DmmMeasurementEventArgs(Exception error, bool canceled, object userState, T reading, int numberOfPoints)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | Exception | The exception that is returned during the operation. |
| canceled | bool | Specifies whether the operation was completed or canceled. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |
| reading | T | Reading obtained from the measurement operation. |
| numberOfPoints | int | Number of points obtained from the measurement operation. |

Parent topic:

DmmMeasurementEventArgs<T> Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-reading.html language=enus -->
## TOPIC 00166: Reading

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-reading.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs-reading.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the resulting reading from the measurement operation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic T Reading { get; }RemarksReading contains a single value for a single point measurement, an array of values for a multipoint measurement, or a waveform datatype for a wavefo

### Reading

Gets the resulting reading from the measurement operation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [T](nationalinstruments-modularinstruments-nidmm-dmmthermocoupletype.html) Reading { get; }

#### Remarks

Reading contains a single value for a single point measurement, an array of values for a multipoint measurement, or a waveform datatype for a waveform measurement.

Parent topic:

DmmMeasurementEventArgs<T> Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs.html language=enus -->
## TOPIC 00167: DmmMeasurementEventArgs<T> Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Holds the event data obtained after asynchronous measurement completion. Derives fromAsyncCompletedEventArgsSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmMeasurementEventArgs : AsyncCompletedEventArgsRemarksThis class derives from System.ComponentModel.AsyncCompletedEv

### DmmMeasurementEventArgs<T> Class

Holds the event data obtained after asynchronous measurement completion.

#### Derives from

- AsyncCompletedEventArgs

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmMeasurementEventArgs : AsyncCompletedEventArgs

#### Remarks

This class derives from System.ComponentModel.AsyncCompletedEventArgs that contains System.ComponentModel.AsyncCompletedEventArgs.Error and System.ComponentModel.AsyncCompletedEventArgs.Cancelled. System.ComponentModel.AsyncCompletedEventArgs.Error contains the exception that was returned during that operation. System.ComponentModel.AsyncCompletedEventArgs.Cancelled is used to indicate whether the operation was completed or cancelled. This class also contains readings that are obtained as a result of the operation.

#### Type Parameters

| Name | Description |
| --- | --- |
| T | Refers to System.Double[] when used with FetchMultiPointAsync, MemoryOptimizedFetchMultiPointAsync, ReadMultiPointAsync, or MemoryOptimizedReadMultiPointAsync. Refers to NationalInstruments.AnalogWaveform<TData> when used with FetchWaveformAsync, MemoryOptimizedFetchWaveformAsync, ReadWaveformAsync, or MemoryOptimizedReadWaveformAsync. |

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DmmMeasurementEventArgs(Exception, bool, object, T, int) | Initializes a new instance of the NationalInstruments.ModularInstruments.NIDmm.DmmMeasurementEventArgs<T> class. |

#### Properties

| Name | Description |
| --- | --- |
| ActualNumberOfPoints | Gets the number of measurement points obtained from the async measurement operation. |
| Reading | Gets the resulting reading from the measurement operation. |

#### See Also

- DmmTrigger

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html language=enus -->
## TOPIC 00168: DmmMeasurementFunction Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement function to be used. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmMeasurementFunctionRemarksFor more information, refer to the NIDMM_ATTR_FUNCTION topic in the NI Digital Multimeters Help. MembersNameValueDescriptionDCVolts1DC voltage. ACVolts

### DmmMeasurementFunction Enumeration

Specifies the measurement function to be used.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmMeasurementFunction

#### Remarks

For more information, refer to the [NIDMM_ATTR_FUNCTION](/csh?context=nidmm_nidmmcref_attribute_function) topic in the *NI Digital Multimeters Help*.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DCVolts | 1 | DC voltage. |
| ACVolts | 2 | AC voltage. |
| DCCurrent | 3 | DC current. |
| ACCurrent | 4 | AC current. |
| TwoWireResistance | 5 | 2-wire resistance. |
| FourWireResistance | 101 | 4-wire resistance. |
| Frequency | 104 | Frequency. |
| Period | 105 | Period. |
| Temperature | 108 | IVI spec enum value from IviDmm.h IVIDMM_VAL_TEMPERATURE. |
| ACVoltsDCCoupled | 1001 | AC voltage with DC coupling. |
| Diode | 1002 | Diode. |
| Capacitance | 1005 | Capacitance. |
| Inductance | 1006 | Inductance. |
| WaveformVoltage | 1003 | Waveform voltage. |
| WaveformCurrent | 1004 | Waveform current. |

#### See Also

- MeasurementFunction
- Configure
- ConfigureMeasurementDigits
- ConfigureWaveformAcquisition

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-buffersize.html language=enus -->
## TOPIC 00169: BufferSize

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-buffersize.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-buffersize.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the size in samples of the internal data buffer. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int BufferSize { get; set; }RemarksMaximum is 134,217,727 (Ox7FFFFFF) samples. When set to -1, NI-DMM chooses the buffer size.

### BufferSize

Gets or sets the size in samples of the internal data buffer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int BufferSize { get; set; }

#### Remarks

Maximum is 134,217,727 (Ox7FFFFFF) samples. When set to -1, NI-DMM chooses the buffer size.

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-configure__int-int-dmmsampletrigger-precisiontimespan.html language=enus -->
## TOPIC 00170: Configure(int, int, DmmSampleTrigger, PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-configure__int-int-dmmsampletrigger-precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-configure__int-int-dmmsampletrigger-precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures properties related to multipoint acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Configure(int triggerCount, int sampleCount, DmmSampleTrigger sampleTrigger, PrecisionTimeSpan sampleInterval)RemarksUse this method to configure the following properties

### Configure(int, int, DmmSampleTrigger, PrecisionTimeSpan)

Configures properties related to multipoint acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Configure(int triggerCount, int sampleCount, DmmSampleTrigger sampleTrigger, PrecisionTimeSpan sampleInterval)

#### Remarks

TriggerCount

SampleCount

SampleTrigger

SampleInterval

TriggerCount

SampleCount

Note

This property is not used on the NI 4050.

LabWindows/CVI Trigger Routing

NI Digital Multimeters Help

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| triggerCount | int | Sets the number of triggers you want the DMM to receive before returning to the Idle state. The driver sets TriggerCount to this value. The default value is 1. |
| sampleCount | int | Sets the number of measurements the DMM makes in each measurement sequence initiated by a trigger. The driver sets SampleCount to this value. The default value is 1. |
| sampleTrigger | DmmSampleTrigger | Specifies the sample trigger source you want to use. The driver sets SampleTrigger to this value. The default is Immediate. |
| sampleInterval | PrecisionTimeSpan | Sets the amount of time in seconds the DMM waits between measurements. The driver sets SampleInterval to this value. Specify a sample interval to add settling time between measurements or to decrease the measurement rate. SampleInterval only applies when the SampleTrigger is set to Interval. On the NI 4060, the SampleInterval value is used as the settling time. When sample interval is set to 0, the DMM does not settle between measurements. The NI 4065 and NI 4070/4071/4072 use the value specified in Sample Interval as additional delay. The default value (PrecisionTimeSpan.MaxValue) ensures that the DMM settles for a recommended time. This is the same as using an Immediate trigger. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OperationNotSupportedException | An acquisition of less than three samples does not support external triggering or an external measurement complete destination. |

#### See Also

- DmmTrigger

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-latency.html language=enus -->
## TOPIC 00171: Latency

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-latency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-latency.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of measurements transferred at a time from the instrument to an internal buffer. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int Latency { get; set; }RemarksWhen set to -1, NI-DMM chooses the transfer size.

### Latency

Gets or sets the number of measurements transferred at a time from the instrument to an internal buffer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int Latency { get; set; }

#### Remarks

When set to -1, NI-DMM chooses the transfer size.

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-samplecount.html language=enus -->
## TOPIC 00172: SampleCount

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-samplecount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-samplecount.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int SampleCount { get; set; }RemarksThe number of measurements the DMM makes in each measurement sequence initiat

### SampleCount

Gets or sets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int SampleCount { get; set; }

#### Remarks

The number of measurements the DMM makes in each measurement sequence initiated by a trigger. The default is 1.

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampledelaymode.html language=enus -->
## TOPIC 00173: SampleDelayMode

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampledelaymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampledelaymode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a delay interval after an sample external trigger for the NI 4060 only. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDelayMode SampleDelayMode { get; set; }RemarksThe default value is 0.

### SampleDelayMode

Gets or sets a delay interval after an sample external trigger for the NI 4060 only.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmDelayMode](nationalinstruments-modularinstruments-nidmm-dmmdelaymode.html) SampleDelayMode { get; set; }

#### Remarks

The default value is 0.

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampleinterval.html language=enus -->
## TOPIC 00174: SampleInterval

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampleinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampleinterval.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time in seconds the DMM waits between measurement cycles. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic NationalInstruments.PrecisionTimeSpan SampleInterval { get; set; }RemarksOn the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.

### SampleInterval

Gets or sets the amount of time in seconds the DMM waits between measurement cycles.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public NationalInstruments.PrecisionTimeSpan SampleInterval { get; set; }

#### Remarks

On the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.72 ns and the valid range is 0-149 s. Only positive values are valid when setting the sample interval.

SampleTrigger

Note

The NI 4050 is not supported.

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampletrigger.html language=enus -->
## TOPIC 00175: SampleTrigger

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampletrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampletrigger.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the sample trigger source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmSampleTrigger SampleTrigger { get; set; }RemarksTo determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in the NI Digital Multimeters Hel

### SampleTrigger

Gets or sets the sample trigger source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) SampleTrigger { get; set; }

#### Remarks

To determine which values are supported by each device, refer to the [LabWindows/CVI Trigger Routing](/csh?context=nidmm_dmm_cvitrigger_routing) section in 
 the *NI Digital Multimeters Help*.

| Trigger Source | Description |
| --- | --- |
| Immediate | No trigger specified |
| External | AUX I/O Connector Trigger Line 0 |
| SoftwareTrigger | Software trigger |
| Interval | Interval trigger |
| Ttl0 | PXI Trigger Line 0 |
| Ttl1 | PXI Trigger Line 1 |
| Ttl2 | PXI Trigger Line 2 |
| Ttl3 | PXI Trigger Line 3 |
| Ttl4 | PXI Trigger Line 4 |
| Ttl5 | PXI Trigger Line 5 |
| Ttl6 | PXI Trigger Line 6 |
| Ttl7 | PXI Trigger Line 7 |
| PxiStar | PXI Star Trigger Line |
| LbrTrig1 | Internal Trigger Line of a PXI/SCXI Combination Chassis |
| AuxTrig1 | AUX I/O Connector Trigger Line 1 |

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampletriggerslope.html language=enus -->
## TOPIC 00176: SampleTriggerSlope

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampletriggerslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-sampletriggerslope.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the edge of the signal from the specified sample trigger source on which the DMM is triggered. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmSlope SampleTriggerSlope { get; set; }RemarksSlopeDescriptionPositiveThe driver triggers on the rising edge of the trigge

### SampleTriggerSlope

Gets or sets the edge of the signal from the specified sample trigger source on which the DMM is triggered.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmSlope](nationalinstruments-modularinstruments-nidmm-dmmslope.html) SampleTriggerSlope { get; set; }

#### Remarks

| Slope | Description |
| --- | --- |
| Positive | The driver triggers on the rising edge of the trigger signal. |
| Negative | The driver triggers on the falling edge of the trigger signal. |

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint-triggercount.html language=enus -->
## TOPIC 00177: TriggerCount

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint-triggercount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint-triggercount.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of triggers the DMM receives before returning to the Idle state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int TriggerCount { get; set; }RemarksThis property can be set to any positive value for the NI 4065 and NI 4070/4071/4072. The NI 4050 and NI 4

### TriggerCount

Gets or sets the number of triggers the DMM receives before returning to the Idle state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int TriggerCount { get; set; }

#### Remarks

This property can be set to any positive value for the NI 4065 and NI 4070/4071/4072.

The NI 4050 and NI 4060 support this property being set to 1. For more information, refer to the [Multiple Point Acquisitions](/csh?context=nidmm_dmm_multi_point) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmMultiPoint Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmmultipoint.html language=enus -->
## TOPIC 00178: DmmMultiPoint Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmmultipoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmmultipoint.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties and methods for acquiring data on multiple triggers and acquiring multiple measurements per trigger. Derives fromDmmSubObjectIIviDmmMultiPointSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmMultiPoint : DmmSubObject, IIviDmmMultiPointRemarksTo configu

### DmmMultiPoint Class

Provides properties and methods for acquiring data on multiple triggers and acquiring multiple measurements per trigger.

#### Derives from

- DmmSubObject
- IIviDmmMultiPoint

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmMultiPoint : DmmSubObject, IIviDmmMultiPoint

#### Remarks

To configure multiple point acquisitions, first configure the function, range, and resolution with the [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object's [Configure](nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-double-double.html), and then configure the number of points to acquire with the DmmMultiPoint object's NationalInstruments.ModularInstruments.NIDmm.DmmMultiPoint.Configure. Multiple point acquisitions are useful when you need to acquire multiple measurements with the same configuration.

For more information, refer to the [Multiple Point Acquisitions](/csh?context=nidmm_dmm_multi_point) topic in the *NI Digital Multimeters Help*.

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| BufferSize | Gets or sets the size in samples of the internal data buffer. |
| Latency | Gets or sets the number of measurements transferred at a time from the instrument to an internal buffer. |
| SampleCount | Gets or sets the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition. |
| SampleDelayMode | Gets or sets a delay interval after an sample external trigger for the NI 4060 only. |
| SampleInterval | Gets or sets the amount of time in seconds the DMM waits between measurement cycles. |
| SampleTrigger | Gets or sets the sample trigger source. |
| SampleTriggerSlope | Gets or sets the edge of the signal from the specified sample trigger source on which the DMM is triggered. |
| TriggerCount | Gets or sets the number of triggers the DMM receives before returning to the Idle state. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(int, int, DmmSampleTrigger, PrecisionTimeSpan) | Configures properties related to multipoint acquisition. |

#### See Also

- DmmTrigger

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmoffsetcompensatedohm.html language=enus -->
## TOPIC 00179: DmmOffsetCompensatedOhm Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmoffsetcompensatedohm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmoffsetcompensatedohm.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables offset compensation Ohms. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmOffsetCompensatedOhmMembersNameValueDescriptionOff0Disables offset compensated Ohms. On1Enables offset compensated Ohms.

### DmmOffsetCompensatedOhm Enumeration

Enables or disables offset compensation Ohms.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmOffsetCompensatedOhm

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Off | 0 | Disables offset compensated Ohms. |
| On | 1 | Enables offset compensated Ohms. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation-conductance.html language=enus -->
## TOPIC 00180: Conductance

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation-conductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation-conductance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the active part (conductance) of the open cable compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Conductance { get; set; }RemarksThe valid range is any real number greater than 0. The default value (-1.0) indicates that compensation has not taken

### Conductance

Gets or sets the active part (conductance) of the open cable compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Conductance { get; set; }

#### Remarks

The valid range is any real number greater than 0. The default value (-1.0) indicates that compensation has not taken place.

For the NI 4072 only. Using this property or [ConfigureMeasurementDigits](nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html) to change the function or the range resets the value of this property to the default value.

Parent topic:

DmmOpenCableCompensation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation-susceptance.html language=enus -->
## TOPIC 00181: Susceptance

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation-susceptance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation-susceptance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the reactive part (susceptance) of the open cable compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Susceptance { get; set; }RemarksThe valid range is any real number greater than 0. The default value (-1.0) indicates that compensation has not take

### Susceptance

Gets or sets the reactive part (susceptance) of the open cable compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Susceptance { get; set; }

#### Remarks

The valid range is any real number greater than 0. The default value (-1.0) indicates that compensation has not taken place.

For the NI 4072 only. Using this property or [ConfigureMeasurementDigits](nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html) to change the function or the range resets the value of this property to the default value.

Parent topic:

DmmOpenCableCompensation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation.html language=enus -->
## TOPIC 00182: DmmOpenCableCompensation Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmopencablecompensation.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls capacitance and inductance open cable compensation. Derives fromDmmSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmOpenCableCompensation : DmmSubObjectRemarksUse DmmOpenCableCompensation to control capacitance and inductance open cable compensation. Sys

### DmmOpenCableCompensation Class

Controls capacitance and inductance open cable compensation.

#### Derives from

- DmmSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmOpenCableCompensation : DmmSubObject

#### Remarks

DmmOpenCableCompensation

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Conductance | Gets or sets the active part (conductance) of the open cable compensation. |
| Susceptance | Gets or sets the reactive part (susceptance) of the open cable compensation. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html language=enus -->
## TOPIC 00183: DmmOperationMode Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mode in which the device acquires data. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmOperationModeMembersNameValueDescriptionIviDmmMode0IviDmm mode. WaveformMode1Waveform acquisition mode. See AlsoOffsetCompensatedOhm

### DmmOperationMode Enumeration

Specifies the mode in which the device acquires data.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmOperationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| IviDmmMode | 0 | IviDmm mode. |
| WaveformMode | 1 | Waveform acquisition mode. |

#### See Also

- OffsetCompensatedOhm

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmreferencejunctiontype.html language=enus -->
## TOPIC 00184: DmmReferenceJunctionType Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmreferencejunctiontype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmreferencejunctiontype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of reference junction to be used. Used for thermocouple measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmReferenceJunctionTypeMembersNameValueDescriptionFixed2Fixed reference junction. See AlsoNationalInstruments.ModularInstruments.NIDmm.Dm

### DmmReferenceJunctionType Enumeration

Specifies the type of reference junction to be used. Used for thermocouple measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmReferenceJunctionType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Fixed | 2 | Fixed reference junction. |

#### See Also

- NationalInstruments.ModularInstruments.NIDmm.DmmThermocouple.Configure

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtd-a.html language=enus -->
## TOPIC 00185: A

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtd-a.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtd-a.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Callendar-Van Dusen A coefficient for RTD scaling when Type is set to Custom. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double A { get; set; }RemarksThe default value is 3.9083e-3 (Pt3851).

### A

Gets or sets the Callendar-Van Dusen A coefficient for RTD scaling when [Type](nationalinstruments-modularinstruments-nidmm-dmmrtd-type.html) is set to [Custom](nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double A { get; set; }

#### Remarks

The default value is 3.9083e-3 (Pt3851).

Parent topic:

DmmRtd Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtd-b.html language=enus -->
## TOPIC 00186: B

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtd-b.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtd-b.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Callendar-Van Dusen B coefficient for RTD scaling when Type is set to Custom. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double B { get; set; }RemarksThe default value is -5.775e-7(Pt3851).

### B

Gets or sets the Callendar-Van Dusen B coefficient for RTD scaling when [Type](nationalinstruments-modularinstruments-nidmm-dmmrtd-type.html) is set to [Custom](nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double B { get; set; }

#### Remarks

The default value is -5.775e-7(Pt3851).

Parent topic:

DmmRtd Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtd-c.html language=enus -->
## TOPIC 00187: C

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtd-c.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtd-c.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Callendar-Van Dusen C coefficient for RTD scaling when Type is set to Custom. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double C { get; set; }RemarksThe default value is -4.183e-12(Pt3851).

### C

Gets or sets the Callendar-Van Dusen C coefficient for RTD scaling when [Type](nationalinstruments-modularinstruments-nidmm-dmmrtd-type.html) is set to [Custom](nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double C { get; set; }

#### Remarks

The default value is -4.183e-12(Pt3851).

Parent topic:

DmmRtd Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtd-configurecustom__double-double-double.html language=enus -->
## TOPIC 00188: ConfigureCustom(double, double, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtd-configurecustom__double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtd-configurecustom__double-double-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the A, B, and C parameters for a custom RTD. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureCustom(double rtdA, double rtdB, double rtdC)ParametersNameTypeDescriptionrtdAdoubleSpecifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD Type

### ConfigureCustom(double, double, double)

Configures the A, B, and C parameters for a custom RTD.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureCustom(double rtdA, double rtdB, double rtdC)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rtdA | double | Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD Type parameter is set to Custom in the ConfigureType. The default is 3.9083e-3 (Pt3851). |
| rtdB | double | Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD Type parameter is set to Custom in the ConfigureType function. The default is -5.775e-7 (Pt3851). |
| rtdC | double | Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD Type parameter is set to Custom in the ConfigureType function. The default is -4.183e-12 (Pt3851). |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

Parent topic:

DmmRtd Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtd-configuretype__dmmrtdtype-double.html language=enus -->
## TOPIC 00189: ConfigureType(DmmRtdType, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtd-configuretype__dmmrtdtype-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtd-configuretype__dmmrtdtype-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RTD type and RTD resistance parameters for an RTD. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureType(DmmRtdType rtdType, double rtdResistance)ParametersNameTypeDescriptionrtdTypeDmmRtdTypeSpecifies the type of RTD used to measure the temperature re

### ConfigureType(DmmRtdType, double)

Configures the RTD type and RTD resistance parameters for an RTD.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureType(DmmRtdType rtdType, double rtdResistance)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rtdType | DmmRtdType | Specifies the type of RTD used to measure the temperature resistance. The default is PT3851. |
| rtdResistance | double | Specifies the RTD resistance in ohms at 0 deg C. The default is PT3851. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

#### See Also

- DmmRtdType

Parent topic:

DmmRtd Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtd-resistance.html language=enus -->
## TOPIC 00190: Resistance

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtd-resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtd-resistance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the RTD resistance at 0 degrees Celsius. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Resistance { get; set; }RemarksThis applies to all supported RTDs, including custom RTDs. The default value is 100 (Ω).

### Resistance

Gets or sets the RTD resistance at 0 degrees Celsius.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Resistance { get; set; }

#### Remarks

This applies to all supported RTDs, including custom RTDs.

The default value is 100 (Ω).

Parent topic:

DmmRtd Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtd-type.html language=enus -->
## TOPIC 00191: Type

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtd-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtd-type.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of RTD used to measure temperature. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmRtdType Type { get; set; }RemarksThe default value is PT3851.Refer to DmmRtdType for additional information about defined values.

### Type

Gets or sets the type of RTD used to measure temperature.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmRtdType](nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html) Type { get; set; }

#### Remarks

The default value is [PT3851](nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html).

Refer to [DmmRtdType](nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html) for additional information about defined values.

Parent topic:

DmmRtd Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtd.html language=enus -->
## TOPIC 00192: DmmRtd Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtd.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtd.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RTD (resistance temperature detector) for temperature measurements. Derives fromDmmSubObjectIIviDmmRtdSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmRtd : DmmSubObject, IIviDmmRtdRemarksUse Rtd to configure the RTD for temperature measurements. System.Obj

### DmmRtd Class

Configures the RTD (resistance temperature detector) for temperature measurements.

#### Derives from

- DmmSubObject
- IIviDmmRtd

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmRtd : DmmSubObject, IIviDmmRtd

#### Remarks

Rtd

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| A | Gets or sets the Callendar-Van Dusen A coefficient for RTD scaling when Type is set to Custom. |
| B | Gets or sets the Callendar-Van Dusen B coefficient for RTD scaling when Type is set to Custom. |
| C | Gets or sets the Callendar-Van Dusen C coefficient for RTD scaling when Type is set to Custom. |
| Resistance | Gets or sets the RTD resistance at 0 degrees Celsius. |
| Type | Gets or sets the type of RTD used to measure temperature. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureCustom(double, double, double) | Configures the A, B, and C parameters for a custom RTD. |
| ConfigureType(DmmRtdType, double) | Configures the RTD type and RTD resistance parameters for an RTD. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html language=enus -->
## TOPIC 00193: DmmRtdType Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmrtdtype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of RTD (Resistance Temperature Detector) used. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmRtdTypeMembersNameValueDescriptionCustom0User defines Callendar-Van Dusen A, B, and C coefficients with the A, B, and C attributes, respectively. PT38512Most

### DmmRtdType Enumeration

Specifies the type of RTD (Resistance Temperature Detector) used.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmRtdType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Custom | 0 | User defines Callendar-Van Dusen A, B, and C coefficients with the A, B, and C attributes, respectively. |
| PT3851 | 2 | Most common RTDs. |
| PT3750 | 1 | Low-cost RTD. |
| PT3916 | 4 | JISC 1604. |
| PT3920 | 5 | US Industrial Standard D-100. |
| PT3911 | 3 | Low-cost RTD. |
| PT3928 | 6 | The definition of temperature. |

#### See Also

- ConfigureType

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-auxtrig1.html language=enus -->
## TOPIC 00194: AuxTrig1

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-auxtrig1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-auxtrig1.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing Pin 3 on the AUX Connector (AuxTrig1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger AuxTrig1 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, r

### AuxTrig1

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing Pin 3 on the AUX Connector (AuxTrig1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) AuxTrig1 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-equals__object.html language=enus -->
## TOPIC 00195: Equals(object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-equals__object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified object is a DmmSampleTrigger and is equivalent to this DmmSampleTrigger object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectThe System.Object to test. Returnstrue if the spe

### Equals(object)

Determines whether the specified object is a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) and is equivalent to this [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The System.Object to test. |

#### Returns

true if the specified System.Object is a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) and is equivalent to this [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-external.html language=enus -->
## TOPIC 00196: External

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-external.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-external.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing Pin 9 on the AUX Connector (External). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger External { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, r

### External

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing Pin 9 on the AUX Connector (External).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) External { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-fromstring__string.html language=enus -->
## TOPIC 00197: FromString(string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-fromstring__string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a DmmSampleTrigger object that represents the specified trigger source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger FromString(string source)ParametersNameTypeDescriptionsourcestringThe trigger source specified as a System.String. ReturnsA DmmS

### FromString(string)

Returns a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object that represents the specified trigger source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) FromString(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The trigger source specified as a System.String. |

#### Returns

A [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object that represents the specified trigger source.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-gethashcode.html language=enus -->
## TOPIC 00198: GetHashCode()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-gethashcode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a hash code for this DmmSampleTrigger object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override int GetHashCode()ReturnsAn integer value that specifies a hash code for this DmmSampleTrigger object.

### GetHashCode()

Returns a hash code for this [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override int GetHashCode()

#### Returns

An integer value that specifies a hash code for this [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-immediate.html language=enus -->
## TOPIC 00199: Immediate

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-immediate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-immediate.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing an unspecified trigger source (Immediate). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Immediate { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each devi

### Immediate

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing an unspecified trigger source (Immediate).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Immediate { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-interval.html language=enus -->
## TOPIC 00200: Interval

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-interval.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-interval.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the Interval trigger source (Interval). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Interval { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device,

### Interval

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the Interval trigger source (Interval).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Interval { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-lbrtrig1.html language=enus -->
## TOPIC 00201: LbrTrig1

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-lbrtrig1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-lbrtrig1.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the Local Bus Right Trigger Line 1 of a PXI/SCXI combination chassis (LbrTig1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger LbrTrig1 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine whi

### LbrTrig1

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the Local Bus Right Trigger Line 1 of a PXI/SCXI combination chassis (LbrTig1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) LbrTrig1 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-pxistar.html language=enus -->
## TOPIC 00202: PxiStar

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-pxistar.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-pxistar.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Star trigger source (PxiStar). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger PxiStar { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, re

### PxiStar

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Star trigger source (PxiStar).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) PxiStar { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-softwaretrigger.html language=enus -->
## TOPIC 00203: SoftwareTrigger

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-softwaretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-softwaretrigger.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the software trigger source (Software Trigger). The sample trigger waits until SendSoftwareTrigger is called. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger SoftwareTrigger { get; }RemarksReturns an object of ty

### SoftwareTrigger

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the software trigger source (Software Trigger). The sample trigger waits until [SendSoftwareTrigger](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-sendsoftwaretrigger.html) is called.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) SoftwareTrigger { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-tostring.html language=enus -->
## TOPIC 00204: ToString()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-tostring.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts this DmmSampleTrigger to a human-readable string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override string ToString()ReturnsA System.String that corresponds to this DmmSampleTrigger.

### ToString()

Converts this [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) to a human-readable string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override string ToString()

#### Returns

A System.String that corresponds to this [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl0.html language=enus -->
## TOPIC 00205: Ttl0

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl0.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Trigger Line 0 source (Ttl0). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Ttl0 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, refer

### Ttl0

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Trigger Line 0 source (Ttl0).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Ttl0 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl1.html language=enus -->
## TOPIC 00206: Ttl1

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl1.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Trigger Line 1 source (Ttl1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Ttl1 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, refer

### Ttl1

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Trigger Line 1 source (Ttl1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Ttl1 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl2.html language=enus -->
## TOPIC 00207: Ttl2

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl2.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Trigger Line 2 source (Ttl2). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Ttl2 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, refer

### Ttl2

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Trigger Line 2 source (Ttl2).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Ttl2 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl3.html language=enus -->
## TOPIC 00208: Ttl3

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl3.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Trigger Line 3 source (Ttl3). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Ttl3 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, refer

### Ttl3

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Trigger Line 3 source (Ttl3).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Ttl3 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl4.html language=enus -->
## TOPIC 00209: Ttl4

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl4.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Trigger Line 4 source (Ttl4). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Ttl4 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, refer

### Ttl4

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Trigger Line 4 source (Ttl4).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Ttl4 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl5.html language=enus -->
## TOPIC 00210: Ttl5

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl5.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Trigger Line 5 source (Ttl5). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Ttl5 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, refer

### Ttl5

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Trigger Line 5 source (Ttl5).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Ttl5 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl6.html language=enus -->
## TOPIC 00211: Ttl6

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl6.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Trigger Line 6 source (Ttl6). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Ttl6 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, refer

### Ttl6

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Trigger Line 6 source (Ttl6).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Ttl6 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl7.html language=enus -->
## TOPIC 00212: Ttl7

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger-ttl7.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmSampleTrigger object representing the PXI Trigger Line 7 source (Ttl7). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmSampleTrigger Ttl7 { get; }RemarksReturns an object of type DmmSampleTrigger. To determine which values are supported by each device, refer

### Ttl7

Gets a [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) object representing the PXI Trigger Line 7 source (Ttl7).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html) Ttl7 { get; }

#### Remarks

Returns an object of type [DmmSampleTrigger](nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmSampleTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html language=enus -->
## TOPIC 00213: DmmSampleTrigger Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsampletrigger.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DMM trigger source. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmSampleTriggerRemarksThis class can be used to get a particular DMM trigger source either from the static properties or from a string representation of the trigger source. Thr

### DmmSampleTrigger Class

Represents a DMM trigger source.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmSampleTrigger

#### Remarks

This class can be used to get a particular DMM trigger source either from the static properties or from a string representation of the trigger source.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| AuxTrig1 | Gets a DmmSampleTrigger object representing Pin 3 on the AUX Connector (AuxTrig1). |
| External | Gets a DmmSampleTrigger object representing Pin 9 on the AUX Connector (External). |
| Immediate | Gets a DmmSampleTrigger object representing an unspecified trigger source (Immediate). |
| Interval | Gets a DmmSampleTrigger object representing the Interval trigger source (Interval). |
| LbrTrig1 | Gets a DmmSampleTrigger object representing the Local Bus Right Trigger Line 1 of a PXI/SCXI combination chassis (LbrTig1). |
| PxiStar | Gets a DmmSampleTrigger object representing the PXI Star trigger source (PxiStar). |
| SoftwareTrigger | Gets a DmmSampleTrigger object representing the software trigger source (Software Trigger). The sample trigger waits until SendSoftwareTrigger is called. |
| Ttl0 | Gets a DmmSampleTrigger object representing the PXI Trigger Line 0 source (Ttl0). |
| Ttl1 | Gets a DmmSampleTrigger object representing the PXI Trigger Line 1 source (Ttl1). |
| Ttl2 | Gets a DmmSampleTrigger object representing the PXI Trigger Line 2 source (Ttl2). |
| Ttl3 | Gets a DmmSampleTrigger object representing the PXI Trigger Line 3 source (Ttl3). |
| Ttl4 | Gets a DmmSampleTrigger object representing the PXI Trigger Line 4 source (Ttl4). |
| Ttl5 | Gets a DmmSampleTrigger object representing the PXI Trigger Line 5 source (Ttl5). |
| Ttl6 | Gets a DmmSampleTrigger object representing the PXI Trigger Line 6 source (Ttl6). |
| Ttl7 | Gets a DmmSampleTrigger object representing the PXI Trigger Line 7 source (Ttl7). |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Returns a DmmSampleTrigger object that represents the specified trigger source. |
| Equals(object) | Determines whether the specified object is a DmmSampleTrigger and is equivalent to this DmmSampleTrigger object. |
| GetHashCode() | Returns a hash code for this DmmSampleTrigger object. |
| ToString() | Converts this DmmSampleTrigger to a human-readable string. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmselftestresult-code.html language=enus -->
## TOPIC 00214: Code

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmselftestresult-code.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmselftestresult-code.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the numeric result from the self-test operation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int Code { get; }Remarks0 = no error (test passed).

### Code

Gets the numeric result from the self-test operation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int Code { get; }

#### Remarks

0 = no error (test passed).

Parent topic:

DmmSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmselftestresult-dmmselftestresult__int-string.html language=enus -->
## TOPIC 00215: DmmSelfTestResult(int, string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmselftestresult-dmmselftestresult__int-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmselftestresult-dmmselftestresult__int-string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DmmSelfTestResult struct. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmSelfTestResult(int code, string message)ParametersNameTypeDescriptioncodeintThe numeric result from the self-test operation. 0 = no error (test passed).messagestringThe

### DmmSelfTestResult(int, string)

Initializes a new instance of the [DmmSelfTestResult](nationalinstruments-modularinstruments-nidmm-dmmselftestresult.html) struct.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public DmmSelfTestResult(int code, string message)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| code | int | The numeric result from the self-test operation. 0 = no error (test passed). |
| message | string | The self-test status message. |

Parent topic:

DmmSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmselftestresult-equals__object.html language=enus -->
## TOPIC 00216: Equals(object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmselftestresult-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmselftestresult-equals__object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares two SelfTest instances for equality. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSelfTest object to compare to.Returnstrue if the two instances represent the same result; otherwise, false.

### Equals(object)

Compares two [SelfTest](nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html) instances for equality.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | SelfTest object to compare to. |

#### Returns

true if the two instances represent the same result; otherwise, false.

Parent topic:

DmmSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmselftestresult-gethashcode.html language=enus -->
## TOPIC 00217: GetHashCode()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmselftestresult-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmselftestresult-gethashcode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the result of the self test. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override int GetHashCode()ReturnsAn Int32 containing the hash value generated for this result.

### GetHashCode()

Returns the hash code for the result of the self test.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override int GetHashCode()

#### Returns

An Int32 containing the hash value generated for this result.

Parent topic:

DmmSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmselftestresult-message.html language=enus -->
## TOPIC 00218: Message

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmselftestresult-message.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmselftestresult-message.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the string returned from the instrument SelfTest. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic string Message { get; }RemarksString returned from the instrument SelfTest.

### Message

Gets the string returned from the instrument [SelfTest](nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public string Message { get; }

#### Remarks

String returned from the instrument [SelfTest](nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html).

Parent topic:

DmmSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmselftestresult-operator_eq__dmmselftestresult-dmmselftestresult.html language=enus -->
## TOPIC 00219: operator==(DmmSelfTestResult, DmmSelfTestResult)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmselftestresult-operator_eq__dmmselftestresult-dmmselftestresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmselftestresult-operator_eq__dmmselftestresult-dmmselftestresult.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether two SelfTest instances have the same value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static bool operator==(DmmSelfTestResult result1, DmmSelfTestResult result2)ParametersNameTypeDescriptionresult1DmmSelfTestResultA DmmSelfTestResult instance to compare

### operator==(DmmSelfTestResult, DmmSelfTestResult)

Determines whether two [SelfTest](nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html) instances have the same value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static bool operator==(DmmSelfTestResult result1, DmmSelfTestResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | DmmSelfTestResult | A DmmSelfTestResult instance to compare with result1. |
| result2 | DmmSelfTestResult | A DmmSelfTestResult instance to compare with result2. |

#### Returns

true if the two instances represent the same result; otherwise, false.

Parent topic:

DmmSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmselftestresult-operator_neq__dmmselftestresult-dmmselftestresult.html language=enus -->
## TOPIC 00220: operator!=(DmmSelfTestResult, DmmSelfTestResult)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmselftestresult-operator_neq__dmmselftestresult-dmmselftestresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmselftestresult-operator_neq__dmmselftestresult-dmmselftestresult.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares two SelfTest instances for equality. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static bool operator!=(DmmSelfTestResult result1, DmmSelfTestResult result2)ParametersNameTypeDescriptionresult1DmmSelfTestResultA DmmSelfTestResult instance to compare with result1. res

### operator!=(DmmSelfTestResult, DmmSelfTestResult)

Compares two [SelfTest](nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html) instances for equality.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static bool operator!=(DmmSelfTestResult result1, DmmSelfTestResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | DmmSelfTestResult | A DmmSelfTestResult instance to compare with result1. |
| result2 | DmmSelfTestResult | A DmmSelfTestResult instance to compare with result2. |

#### Returns

true if the two instances represent the same result; otherwise, false.

Parent topic:

DmmSelfTestResult Data Structure

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmselftestresult.html language=enus -->
## TOPIC 00221: DmmSelfTestResult Data Structure

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmselftestresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmselftestresult.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The result of NI-DMM SelfTest. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic struct DmmSelfTestResultRemarksContains the results of a NI-DMM SelfTest. Use the code and message to determine if there was an error. Thread SafetyAll members of this type are safe for

### DmmSelfTestResult Data Structure

The result of NI-DMM [SelfTest](nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public struct DmmSelfTestResult

#### Remarks

Contains the results of a NI-DMM [SelfTest](nationalinstruments-modularinstruments-nidmm-dmmdriverutility-selftest.html). Use the code and message to determine if there was an error.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DmmSelfTestResult(int, string) | Initializes a new instance of the DmmSelfTestResult struct. |

#### Properties

| Name | Description |
| --- | --- |
| Code | Gets the numeric result from the self-test operation. |
| Message | Gets the string returned from the instrument SelfTest. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Compares two SelfTest instances for equality. |
| GetHashCode() | Returns the hash code for the result of the self test. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(DmmSelfTestResult, DmmSelfTestResult) | Compares two SelfTest instances for equality. |
| operator==(DmmSelfTestResult, DmmSelfTestResult) | Determines whether two SelfTest instances have the same value. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation-reactance.html language=enus -->
## TOPIC 00222: Reactance

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation-reactance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation-reactance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the reactive part (reactance) of the short cable compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Reactance { get; set; }RemarksThe valid range is any real number greater than 0. The default value is -1, which indicates that compensation has not t

### Reactance

Gets or sets the reactive part (reactance) of the short cable compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Reactance { get; set; }

#### Remarks

The valid range is any real number greater than 0. The default value is -1, which indicates that compensation has not taken place.

For the NI 4072 only.

Using this property or [ConfigureMeasurementDigits](nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html) to change the function or the range resets the value of this property to the default value.

Parent topic:

DmmShortCableCompensation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation-resistance.html language=enus -->
## TOPIC 00223: Resistance

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation-resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation-resistance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the active part (resistance) of the short cable compensation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Resistance { get; set; }RemarksThe valid range is any real number greater than 0. The default value is -1, which indicates that compensation has not t

### Resistance

Gets or sets the active part (resistance) of the short cable compensation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Resistance { get; set; }

#### Remarks

The valid range is any real number greater than 0. The default value is -1, which indicates that compensation has not taken place.

For the NI 4072 only.

Using this property or [ConfigureMeasurementDigits](nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html) to change the function or the range resets the value of this property to the default value.

Parent topic:

DmmShortCableCompensation Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation.html language=enus -->
## TOPIC 00224: DmmShortCableCompensation Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmshortcablecompensation.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls capacitance and inductance short cable compensation. Derives fromDmmSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmShortCableCompensation : DmmSubObjectRemarksUse DmmShortCableCompensation to control capacitance and inductance short cable compensation.

### DmmShortCableCompensation Class

Controls capacitance and inductance short cable compensation.

#### Derives from

- DmmSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmShortCableCompensation : DmmSubObject

#### Remarks

DmmShortCableCompensation

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Reactance | Gets or sets the reactive part (reactance) of the short cable compensation. |
| Resistance | Gets or sets the active part (resistance) of the short cable compensation. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmslope.html language=enus -->
## TOPIC 00225: DmmSlope Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmslope.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the edge of the signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmSlopeMembersNameValueDescriptionPositive0Rising edge. Negative1Falling edge. See AlsoSampleTriggerSlope

### DmmSlope Enumeration

Specifies the edge of the signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmSlope

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Positive | 0 | Rising edge. |
| Negative | 1 | Falling edge. |

#### See Also

- SampleTriggerSlope

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmsubobject.html language=enus -->
## TOPIC 00226: DmmSubObject Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmsubobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmsubobject.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains members that are common to all sub-object NI-DMM classes. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmSubObjectRemarksDmmSubObject is a base class for all sub-object NI-DMM classes. Thread SafetyAll members of this type are safe for multithre

### DmmSubObject Class

Contains members that are common to all sub-object NI-DMM classes.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmSubObject

#### Remarks

DmmSubObject is a base class for all sub-object NI-DMM classes.

#### Thread Safety

All members of this type are safe for multithreaded operations.

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature-configurethermistorcustom__double-double-double.html language=enus -->
## TOPIC 00227: ConfigureThermistorCustom(double, double, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature-configurethermistorcustom__double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature-configurethermistorcustom__double-double-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the A, B, and C parameters for a custom thermistor. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureThermistorCustom(double thermistorA, double thermistorB, double thermistorC)ParametersNameTypeDescriptionthermistorAdoubleSpecifies the Steinhart-Hart A co

### ConfigureThermistorCustom(double, double, double)

Configures the A, B, and C parameters for a custom thermistor.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureThermistorCustom(double thermistorA, double thermistorB, double thermistorC)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| thermistorA | double | Specifies the Steinhart-Hart A coefficient for thermistor scaling when Thermistor Type is set to Custom in the ThermistorType. The default is 1.0295e-3 (44006). |
| thermistorB | double | Specifies the Steinhart-Hart B coefficient for thermistor scaling when Thermistor Type is set to Custom in the ThermistorType. The default is 2.391e-4 (44006). |
| thermistorC | double | Specifies the Steinhart-Hart C coefficient for thermistor scaling when Thermistor Type is set to Custom in the ThermistorType. The default is 1.568e-7 (44006). |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

Parent topic:

DmmTemperature Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature-rtd.html language=enus -->
## TOPIC 00228: Rtd

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature-rtd.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature-rtd.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmRtd object used to control RTD-related values for temperature measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmRtd Rtd { get; }RemarksReturns an object of type DmmRtd.

### Rtd

Gets the [DmmRtd](nationalinstruments-modularinstruments-nidmm-dmmrtd.html) object used to control RTD-related values for temperature measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmRtd](nationalinstruments-modularinstruments-nidmm-dmmrtd.html) Rtd { get; }

#### Remarks

Returns an object of type [DmmRtd](nationalinstruments-modularinstruments-nidmm-dmmrtd.html).

Parent topic:

DmmTemperature Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistora.html language=enus -->
## TOPIC 00229: ThermistorA

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistora.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistora.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Steinhart-Hart A coefficient for thermistor scaling when ThermistorType is set to Custom. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double ThermistorA { get; set; }RemarksThe default value is 0.0010295 (44006).

### ThermistorA

Gets or sets the Steinhart-Hart A coefficient for thermistor scaling when [ThermistorType](nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistortype.html) is set to [Custom](nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double ThermistorA { get; set; }

#### Remarks

The default value is 0.0010295 (44006).

Parent topic:

DmmTemperature Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistorb.html language=enus -->
## TOPIC 00230: ThermistorB

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistorb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistorb.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Steinhart-Hart B coefficient for thermistor scaling when ThermistorType is set to Custom. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double ThermistorB { get; set; }RemarksThe default value is 0.0002391 (44006).

### ThermistorB

Gets or sets the Steinhart-Hart B coefficient for thermistor scaling when [ThermistorType](nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistortype.html) is set to [Custom](nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double ThermistorB { get; set; }

#### Remarks

The default value is 0.0002391 (44006).

Parent topic:

DmmTemperature Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistorc.html language=enus -->
## TOPIC 00231: ThermistorC

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistorc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistorc.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Steinhart-Hart C coefficient for thermistor scaling when ThermistorType is set to Custom. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double ThermistorC { get; set; }RemarksThe default value is 1.568e-7 (44006).

### ThermistorC

Gets or sets the Steinhart-Hart C coefficient for thermistor scaling when [ThermistorType](nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistortype.html) is set to [Custom](nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double ThermistorC { get; set; }

#### Remarks

The default value is 1.568e-7 (44006).

Parent topic:

DmmTemperature Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistortype.html language=enus -->
## TOPIC 00232: ThermistorType

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistortype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermistortype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of thermistor used to measure the temperature. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmThermistorType ThermistorType { get; set; }RemarksThe default value is Thermistor44006.Refer to DmmThermistorType topic for additional information about defined

### ThermistorType

Gets or sets the type of thermistor used to measure the temperature.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmThermistorType](nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html) ThermistorType { get; set; }

#### Remarks

The default value is [Thermistor44006](nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html).

Refer to [DmmThermistorType](nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html) topic for additional information about defined values.

Parent topic:

DmmTemperature Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermocouple.html language=enus -->
## TOPIC 00233: Thermocouple

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermocouple.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature-thermocouple.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Thermocouple objects used to control the thermocouple-related values for temperature measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmThermocouple Thermocouple { get; }RemarksReturns an object of type Thermocouple.

### Thermocouple

Gets the Thermocouple objects used to control the thermocouple-related values for temperature measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmThermocouple](nationalinstruments-modularinstruments-nidmm-dmmthermocouple.html) Thermocouple { get; }

#### Remarks

Returns an object of type Thermocouple.

Parent topic:

DmmTemperature Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature-transducertype.html language=enus -->
## TOPIC 00234: TransducerType

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature-transducertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature-transducertype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of transducer. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmTransducerType TransducerType { get; set; }RemarksThe default value is Thermocouple. Transducer TypeDescriptionFourWireRtd4-wire RTDThermistorThermistorThermocoupleThermocoupleTwoWireRtd2-wire

### TransducerType

Gets or sets the type of transducer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmTransducerType](nationalinstruments-modularinstruments-nidmm-dmmtransducertype.html) TransducerType { get; set; }

#### Remarks

The default value is [Thermocouple](nationalinstruments-modularinstruments-nidmm-dmmtransducertype.html).

| Transducer Type | Description |
| --- | --- |
| FourWireRtd | 4-wire RTD |
| Thermistor | Thermistor |
| Thermocouple | Thermocouple |
| TwoWireRtd | 2-wire RTD |

Parent topic:

DmmTemperature Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtemperature.html language=enus -->
## TOPIC 00235: DmmTemperature Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtemperature.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the DMM for temperature measurements. Derives fromDmmSubObjectIIviDmmTemperatureSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmTemperature : DmmSubObject, IIviDmmTemperatureRemarksUse DmmTemperature to configure the DMM for temperature measurements. System.Ob

### DmmTemperature Class

Configures the DMM for temperature measurements.

#### Derives from

- DmmSubObject
- IIviDmmTemperature

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmTemperature : DmmSubObject, IIviDmmTemperature

#### Remarks

DmmTemperature

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Rtd | Gets the DmmRtd object used to control RTD-related values for temperature measurements. |
| ThermistorA | Gets or sets the Steinhart-Hart A coefficient for thermistor scaling when ThermistorType is set to Custom. |
| ThermistorB | Gets or sets the Steinhart-Hart B coefficient for thermistor scaling when ThermistorType is set to Custom. |
| ThermistorC | Gets or sets the Steinhart-Hart C coefficient for thermistor scaling when ThermistorType is set to Custom. |
| ThermistorType | Gets or sets the type of thermistor used to measure the temperature. |
| Thermocouple | Gets the Thermocouple objects used to control the thermocouple-related values for temperature measurements. |
| TransducerType | Gets or sets the type of transducer. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureThermistorCustom(double, double, double) | Configures the A, B, and C parameters for a custom thermistor. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html language=enus -->
## TOPIC 00236: DmmThermistorType Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmthermistortype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of thermistor used for measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmThermistorTypeMembersNameValueDescriptionCustom0Custom. Thermistor44004144004. Thermistor44006244006. Thermistor44007344007. See AlsoThermistorType

### DmmThermistorType Enumeration

Specifies the type of thermistor used for measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmThermistorType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Custom | 0 | Custom. |
| Thermistor44004 | 1 | 44004. |
| Thermistor44006 | 2 | 44006. |
| Thermistor44007 | 3 | 44007. |

#### See Also

- ThermistorType

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmthermocouple-configure__dmmthermocoupletype-dmmreferencejunctiontype.html language=enus -->
## TOPIC 00237: Configure(DmmThermocoupleType, DmmReferenceJunctionType)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmthermocouple-configure__dmmthermocoupletype-dmmreferencejunctiontype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmthermocouple-configure__dmmthermocoupletype-dmmreferencejunctiontype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the thermocouple type and reference junction type for a chosen thermocouple. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Configure(DmmThermocoupleType thermocoupleType, DmmReferenceJunctionType referenceJunctionType)ParametersNameTypeDescriptionthermocoupleTyp

### Configure(DmmThermocoupleType, DmmReferenceJunctionType)

Configures the thermocouple type and reference junction type for a chosen thermocouple.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Configure(DmmThermocoupleType thermocoupleType, DmmReferenceJunctionType referenceJunctionType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| thermocoupleType | DmmThermocoupleType | Specifies the type of thermocouple used to measure the temperature. The default is J. |
| referenceJunctionType | DmmReferenceJunctionType | Specifies the type of reference junction to be used in the reference junction compensation of a thermocouple measurement. The only supported value is Fixed. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

#### See Also

- DmmThermocoupleType
- DmmReferenceJunctionType

Parent topic:

DmmThermocouple Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmthermocouple-fixedreferencejunction.html language=enus -->
## TOPIC 00238: FixedReferenceJunction

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmthermocouple-fixedreferencejunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmthermocouple-fixedreferencejunction.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double FixedReferenceJunction { get; set; }RemarksThe default value is 25.0 (°C).

### FixedReferenceJunction

Gets or sets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double FixedReferenceJunction { get; set; }

#### Remarks

The default value is 25.0 (°C).

Parent topic:

DmmThermocouple Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmthermocouple-referencejunctiontype.html language=enus -->
## TOPIC 00239: ReferenceJunctionType

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmthermocouple-referencejunctiontype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmthermocouple-referencejunctiontype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of reference junction to be used in the reference junction compensation of a thermocouple. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmReferenceJunctionType ReferenceJunctionType { get; set; }RemarksThe only supported value for DmmReferenceJunctionTyp

### ReferenceJunctionType

Gets or sets the type of reference junction to be used in the reference junction compensation of a thermocouple.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmReferenceJunctionType](nationalinstruments-modularinstruments-nidmm-dmmreferencejunctiontype.html) ReferenceJunctionType { get; set; }

#### Remarks

The only supported value for [DmmReferenceJunctionType](nationalinstruments-modularinstruments-nidmm-dmmreferencejunctiontype.html) is [Fixed](nationalinstruments-modularinstruments-nidmm-dmmreferencejunctiontype.html).

| Reference Junction Type | Description |
| --- | --- |
| Fixed | Fixed reference junction. |

#### See Also

- DmmReferenceJunctionType

Parent topic:

DmmThermocouple Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmthermocouple-type.html language=enus -->
## TOPIC 00240: Type

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmthermocouple-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmthermocouple-type.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of thermocouple used to measure the temperature. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmThermocoupleType Type { get; set; }RemarksThe default value is J. See AlsoDmmThermocoupleType

### Type

Gets or sets the type of thermocouple used to measure the temperature.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmThermocoupleType](nationalinstruments-modularinstruments-nidmm-dmmthermocoupletype.html) Type { get; set; }

#### Remarks

The default value is [J](nationalinstruments-modularinstruments-nidmm-dmmthermocoupletype.html).

#### See Also

- DmmThermocoupleType

Parent topic:

DmmThermocouple Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmthermocouple.html language=enus -->
## TOPIC 00241: DmmThermocouple Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmthermocouple.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmthermocouple.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the thermocouple for temperature measurements. Derives fromDmmSubObjectIIviDmmThermocoupleSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmThermocouple : DmmSubObject, IIviDmmThermocoupleRemarksUse DmmThermocouple to configure the thermocouple for temperature m

### DmmThermocouple Class

Configures the thermocouple for temperature measurements.

#### Derives from

- DmmSubObject
- IIviDmmThermocouple

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmThermocouple : DmmSubObject, IIviDmmThermocouple

#### Remarks

DmmThermocouple

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| FixedReferenceJunction | Gets or sets the reference junction temperature when a fixed reference junction is used to take a thermocouple measurement. |
| ReferenceJunctionType | Gets or sets the type of reference junction to be used in the reference junction compensation of a thermocouple. |
| Type | Gets or sets the type of thermocouple used to measure the temperature. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(DmmThermocoupleType, DmmReferenceJunctionType) | Configures the thermocouple type and reference junction type for a chosen thermocouple. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmthermocoupletype.html language=enus -->
## TOPIC 00242: DmmThermocoupleType Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmthermocoupletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmthermocoupletype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of thermocouple used for temperature measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmThermocoupleTypeRemarksFor more information, refer to the niDMM_ConfigureThermocouple and Thermocouples topics in the NI Digital Multimeters Help. Members

### DmmThermocoupleType Enumeration

Specifies the type of thermocouple used for temperature measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmThermocoupleType

#### Remarks

For more information, refer to the [niDMM_ConfigureThermocouple](/csh?context=nidmm_nidmmcref_function_configure_thermocouple) and [Thermocouples](/csh?context=nidmm_dmm_thermocouples) topics in the *NI Digital Multimeters Help*.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| B | 1 | Type B. |
| E | 4 | Type E. |
| J | 6 | Type J. |
| K | 7 | Type K. |
| N | 8 | Type N. |
| R | 9 | Type R. |
| S | 10 | Type S. |
| T | 11 | Type T. |

#### See Also

- NationalInstruments.ModularInstruments.NIDmm.DmmThermocouple.Configure

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtransducertype.html language=enus -->
## TOPIC 00243: DmmTransducerType Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtransducertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtransducertype.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of device used for measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmTransducerTypeMembersNameValueDescriptionTwoWireRtd32-wire RTD. FourWireRtd44-wire RTD. Thermistor2Thermistor. Thermocouple1Thermocouple. See AlsoTransducerType

### DmmTransducerType Enumeration

Specifies the type of device used for measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmTransducerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| TwoWireRtd | 3 | 2-wire RTD. |
| FourWireRtd | 4 | 4-wire RTD. |
| Thermistor | 2 | Thermistor. |
| Thermocouple | 1 | Thermocouple. |

#### See Also

- TransducerType

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-configure__dmmtriggersource-bool.html language=enus -->
## TOPIC 00244: Configure(DmmTriggerSource, bool)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-configure__dmmtriggersource-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-configure__dmmtriggersource-bool.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures trigger-related properties. The properties include Source and DelayAuto. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Configure(DmmTriggerSource triggerSource, bool autoTriggerDelay)ParametersNameTypeDescriptiontriggerSourceDmmTriggerSourceSpecifies the Source

### Configure(DmmTriggerSource, bool)

Configures trigger-related properties. The properties include [Source](nationalinstruments-modularinstruments-nidmm-dmmtrigger-source.html) and [DelayAuto](nationalinstruments-modularinstruments-nidmm-dmmtrigger-delayauto.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Configure(DmmTriggerSource triggerSource, bool autoTriggerDelay)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| triggerSource | DmmTriggerSource | Specifies the Source that initiates the acquisition. Setting Source to Software Trigger configures the DMM to wait until SendSoftwareTrigger is called before triggering the DMM. |
| autoTriggerDelay | bool | Indicates whether the driver automatically calculates the appropriate settling time before taking the measurement. Note When using the NI 4050, DelayAuto must be set to On. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |
| System.NotSupportedException | The parameter enum value specified is not supported. |

#### See Also

- DmmAuto

Parent topic:

DmmTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-configure__dmmtriggersource-nationalinstruments.precisiontimespan.html language=enus -->
## TOPIC 00245: Configure(DmmTriggerSource, NationalInstruments.PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-configure__dmmtriggersource-nationalinstruments.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-configure__dmmtriggersource-nationalinstruments.precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures trigger-related properties. The properties include Source and Delay. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Configure(DmmTriggerSource triggerSource, NationalInstruments.PrecisionTimeSpan triggerDelay)RemarksWhen using the NI 4050, DelayAuto must be set t

### Configure(DmmTriggerSource, NationalInstruments.PrecisionTimeSpan)

Configures trigger-related properties. The properties include [Source](nationalinstruments-modularinstruments-nidmm-dmmtrigger-source.html) and [Delay](nationalinstruments-modularinstruments-nidmm-dmmtrigger-delay.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Configure(DmmTriggerSource triggerSource, NationalInstruments.PrecisionTimeSpan triggerDelay)

#### Remarks

When using the NI 4050, [DelayAuto](nationalinstruments-modularinstruments-nidmm-dmmtrigger-delayauto.html) must be set to [On](nationalinstruments-modularinstruments-nidmm-dmmauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| triggerSource | DmmTriggerSource | Specifies the Source that initiates the acquisition. Setting Source to Software Trigger configures the DMM to wait until SendSoftwareTrigger is called before triggering the DMM. |
| triggerDelay | NationalInstruments.PrecisionTimeSpan | Specifies the time that the DMM waits after it has received a trigger before taking a measurement. The Delay is set to this value. On the NI 4060, if you set Delay to 0, the DMM does not settle before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the value specified in Delay as additional settling time. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

#### See Also

- DmmAuto

Parent topic:

DmmTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-delay.html language=enus -->
## TOPIC 00246: Delay

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-delay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-delay.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic PrecisionTimeSpan Delay { get; set; }RemarksFor the NI 4065 and NI 4070/4071/4072, the valid range for trigger delay

### Delay

Gets or sets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public PrecisionTimeSpan Delay { get; set; }

#### Remarks

For the NI 4065 and NI 4070/4071/4072, the valid range for trigger delay is 0.0-149.0 seconds and the onboard timing resolution is 34.72 ns. On the NI 4060, if this property is set to 0, the DMM does not settle before taking the measurement. On the NI 4060, the valid range for [On](nationalinstruments-modularinstruments-nidmm-dmmauto.html) is 0.0-12.0 seconds and the onboard timing resolution is 100 ms. When using the NI 4050, [DelayAuto](nationalinstruments-modularinstruments-nidmm-dmmtrigger-delayauto.html) must be set to [On](nationalinstruments-modularinstruments-nidmm-dmmauto.html). Use positive values to set the trigger delay in seconds. 
 The default value for [DelayAuto](nationalinstruments-modularinstruments-nidmm-dmmtrigger-delayauto.html) is [On](nationalinstruments-modularinstruments-nidmm-dmmauto.html).

The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional settling time.

Parent topic:

DmmTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-delayauto.html language=enus -->
## TOPIC 00247: DelayAuto

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-delayauto.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-delayauto.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the DMM selects the trigger delay automatically. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool DelayAuto { get; set; }RemarksThe default value is On, which means that the DMM waits before taking the measurement. When using the NI 405

### DelayAuto

Gets or sets a value indicating whether the DMM selects the trigger delay automatically.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool DelayAuto { get; set; }

#### Remarks

The default value is [On](nationalinstruments-modularinstruments-nidmm-dmmauto.html), which means that the DMM waits before taking the measurement. When using the NI 4050, this property must be set to [On](nationalinstruments-modularinstruments-nidmm-dmmauto.html).

#### See Also

- DmmAuto

Parent topic:

DmmTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-measurementcompletedestination.html language=enus -->
## TOPIC 00248: MeasurementCompleteDestination

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-measurementcompletedestination.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-measurementcompletedestination.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination of the measurement complete (MC) signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmMeasurementCompleteDestination MeasurementCompleteDestination { get; set; }RemarksThe following table lists the trigger destination and their descriptions. Tri

### MeasurementCompleteDestination

Gets or sets the destination of the measurement complete (MC) signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmMeasurementCompleteDestination](nationalinstruments-modularinstruments-nidmm-dmmmeasurementcompletedestination.html) MeasurementCompleteDestination { get; set; }

#### Remarks

| Trigger Destination | Description |
| --- | --- |
| None | No trigger specified |
| External | AUX I/O Connector |
| Ttl0 | PXI Trigger Line 0 |
| Ttl1 | PXI Trigger Line 1 |
| Ttl2 | PXI Trigger Line 2 |
| Ttl3 | PXI Trigger Line 3 |
| Ttl4 | PXI Trigger Line 4 |
| Ttl5 | PXI Trigger Line 5 |
| Ttl6 | PXI Trigger Line 6 |
| Ttl7 | PXI Trigger Line 7 |
| LbrTrig0 | Internal Trigger Line of a PXI/SCXI Combination Chassis |

LabWindows/CVI Trigger Routing

NI Digital Multimeters Help

The NI 4050 is not supported.

Parent topic:

DmmTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-measurementcompletedestinationslope.html language=enus -->
## TOPIC 00249: MeasurementCompleteDestinationSlope

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-measurementcompletedestinationslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-measurementcompletedestinationslope.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the polarity of the generated measurement complete signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmSlope MeasurementCompleteDestinationSlope { get; set; }RemarksIf set to Positive the driver triggers on the rising edge of the trigger signal. If set to Nega

### MeasurementCompleteDestinationSlope

Gets or sets the polarity of the generated measurement complete signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmSlope](nationalinstruments-modularinstruments-nidmm-dmmslope.html) MeasurementCompleteDestinationSlope { get; set; }

#### Remarks

If set to [Positive](nationalinstruments-modularinstruments-nidmm-dmmslope.html) the driver triggers on the rising edge of the trigger signal. If set to [Negative](nationalinstruments-modularinstruments-nidmm-dmmslope.html) the driver triggers on the falling edge of the trigger signal.

Parent topic:

DmmTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-multipoint.html language=enus -->
## TOPIC 00250: MultiPoint

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-multipoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-multipoint.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets data on multiple triggers and multiple measurements per trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmMultiPoint MultiPoint { get; }RemarksReturns an object of type DmmMultiPoint.

### MultiPoint

Gets data on multiple triggers and multiple measurements per trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmMultiPoint](nationalinstruments-modularinstruments-nidmm-dmmmultipoint.html) MultiPoint { get; }

#### Remarks

Returns an object of type [DmmMultiPoint](nationalinstruments-modularinstruments-nidmm-dmmmultipoint.html).

Parent topic:

DmmTrigger Class
