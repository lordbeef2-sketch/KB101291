# NI DOCUMENT BUNDLE: ni_rfsg-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni_rfsg-csharp-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-nirfsg-checkgenerationstatus.html language=enus -->
## TOPIC 00001: CheckGenerationStatus()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-nirfsg-checkgenerationstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-nirfsg-checkgenerationstatus.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of signal generation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgGenerationStatus CheckGenerationStatus()RemarksUse this method to check for any errors that might occur during signal generation, or to check whether the device has finished generating th

### CheckGenerationStatus()

Checks the status of signal generation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgGenerationStatus](nationalinstruments-modularinstruments-nirfsg-rfsggenerationstatus.html) CheckGenerationStatus()

#### Remarks

Use this method to check for any errors that might occur during signal generation, or to check whether the device has finished generating the signal.

#### Returns

Returns the [RfsgGenerationStatus](nationalinstruments-modularinstruments-nirfsg-rfsggenerationstatus.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CheckGenerationStatus method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

NIRfsg Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-nirfsg-close.html language=enus -->
## TOPIC 00002: Close()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-nirfsg-close.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-nirfsg-close.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Aborts any signal generation in progress and destroys the instrument driver session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Close()RemarksThis method calls the Dispose method.

### Close()

Aborts any signal generation in progress and destroys the instrument driver session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void Close()

#### Remarks

This method calls the [Dispose](nationalinstruments-modularinstruments-nirfsg-nirfsg-dispose.html) method.

Parent topic:

NIRfsg Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-nirfsg-driveroperation.html language=enus -->
## TOPIC 00003: DriverOperation

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-nirfsg-driveroperation.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-nirfsg-driveroperation.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DriverOperation sub-object that affect operation of the NI-RFSG instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDriverOperation DriverOperation { get; }RemarksReturns an object of type RfsgDriverOperation. ExceptionsTypeDescriptionSystem.ObjectDis

### DriverOperation

Gets the DriverOperation sub-object that affect operation of the NI-RFSG instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgDriverOperation](nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation.html) DriverOperation { get; }

#### Remarks

Returns an object of type [RfsgDriverOperation](nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DriverOperation property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

NIRfsg Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulation.html language=enus -->
## TOPIC 00004: RfsgAnalogModulation Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulation.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulation.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties used to configure analog modulation. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgAnalogModulation : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF Sig

### RfsgAnalogModulation Class

Provides properties used to configure analog modulation.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgAnalogModulation : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| AMSensitivity | Gets or sets an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator. When using the NI PXIe-5654 with NI PXIe-5696, NI-RFSG may coerce AM sensitivity. Coercing the AM sensitivity prevents overpowering conditions at the NI 5696 input. Read this property to determine the coerced value. |
| FMBand | Gets or sets the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100 kHz. Narrowband FM allows for modulating lower frequency signals. |
| FMDeviation | Gets or sets the deviation to use in frequency modulation. |
| FMNarrowbandIntegrator | Gets or sets the narrowband frequency modulation (FM) range to apply, by sending the signal through an integrator. This property is valid only when you set the ModulationType property to FM and the FMBand property to Narrowband. |
| FMSensitivity | Gets or sets an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator. |
| ModulationType | Gets or sets the analog modulation format. |
| PMDeviation | Gets or sets the deviation to use in phase modulation. |
| PMMode | Gets or sets the phase modulation (PM) mode to use. |
| PMSensitivity | Gets or sets an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator. |
| WaveformFrequency | Gets or sets the frequency, in hertz (Hz), of the waveform to use as the message signal in analog modulation. |
| WaveformType | Gets or sets the type of waveform to use as the message signal for analog modulation. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationpmmode.html language=enus -->
## TOPIC 00005: RfsgAnalogModulationPMMode Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationpmmode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationpmmode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use high deviation mode or low phase noise mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgAnalogModulationPMModeMembersNameValueDescriptionHighDeviation19000Specifies high deviation. High deviation comes at the expense of a higher phase noise

### RfsgAnalogModulationPMMode Enumeration

Specifies whether to use high deviation mode or low phase noise mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgAnalogModulationPMMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HighDeviation | 19000 | Specifies high deviation. High deviation comes at the expense of a higher phase noise. |
| LowPhaseNoise | 19001 | Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationtype.html language=enus -->
## TOPIC 00006: RfsgAnalogModulationType Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationtype.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the analog modulation format to use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgAnalogModulationTypeMembersNameValueDescriptionNone(int)0Disables analog modulation. FM(int)2000The analog modulation type is FM. PM(int)2001The analog modulation type is PM.

### RfsgAnalogModulationType Enumeration

Specifies the analog modulation format to use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgAnalogModulationType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | (int)0 | Disables analog modulation. |
| FM | (int)2000 | The analog modulation type is FM. |
| PM | (int)2001 | The analog modulation type is PM. |
| AM | (int)2002 | The analog modulation type is AM. |

#### See Also

- ModulationType

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationwaveformtype.html language=enus -->
## TOPIC 00007: RfsgAnalogModulationWaveformType Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationwaveformtype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsganalogmodulationwaveformtype.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of waveform to use as the message signal for analog modulation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgAnalogModulationWaveformTypeMembersNameValueDescriptionSine(int)3000The analog modulation waveform type is sine. Square(int)3001The analog

### RfsgAnalogModulationWaveformType Enumeration

Specifies the type of waveform to use as the message signal for analog modulation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgAnalogModulationWaveformType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Sine | (int)3000 | The analog modulation waveform type is sine. |
| Square | (int)3001 | The analog modulation waveform type is square. |
| Triangle | (int)3002 | The analog modulation waveform type is triangle. |

#### See Also

- WaveformType

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-allocatewaveform__string-int.html language=enus -->
## TOPIC 00008: AllocateWaveform(string, int)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-allocatewaveform__string-int.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-allocatewaveform__string-int.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Allocates onboard memory space for the waveform. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void AllocateWaveform(string name, int sizeInSamples)RemarksUse this method to specify the total size of a waveform before writing the data. Use this method only if you call WriteWav

### AllocateWaveform(string, int)

Allocates onboard memory space for the waveform.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void AllocateWaveform(string name, int sizeInSamples)

#### Remarks

Use this method to specify the total size of a waveform before writing the data. Use this method only if you call [WriteWaveform](nationalinstruments-modularinstruments-nirfsg-rfsgarb-writewaveform__string-double_arr1-double_arr1.html) multiple times to write a large waveform in blocks.

If you allocate a waveform prior to writing it, NI-RFSG ignores the *moreDataPending* parameter in [WriteWaveform](nationalinstruments-modularinstruments-nirfsg-rfsgarb-writewaveform__string-double_arr1-double_arr1.html).

The NI-RFSG device must be in the Configuration state before you call this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words. |
| sizeInSamples | int | Specifies the number of samples to reserve in the onboard memory for the specified waveform. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AllocateWaveform method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-clearwaveform__string.html language=enus -->
## TOPIC 00009: ClearWaveform(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-clearwaveform__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-clearwaveform__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes the specified waveform from the pool of waveforms defined currently. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ClearWaveform(string name)RemarksThe NI-RFSG device must be in the Configuration state before you call ClearWaveform. ParametersNameTypeDescriptionna

### ClearWaveform(string)

Deletes the specified waveform from the pool of waveforms defined currently.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ClearWaveform(string name)

#### Remarks

The NI-RFSG device must be in the Configuration state before you call ClearWaveform.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Specifies the name of the stored waveform to delete. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ClearWaveform method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-datatransfer.html language=enus -->
## TOPIC 00010: DataTransfer

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-datatransfer.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-datatransfer.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties used to configure streaming or direct DMA. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDataTransfer DataTransfer { get; }RemarksReturns an object of type RfsgDataTransfer. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe DataTransfer property wa

### DataTransfer

Gets properties used to configure streaming or direct DMA.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgDataTransfer](nationalinstruments-modularinstruments-nirfsg-rfsgdatatransfer.html) DataTransfer { get; }

#### Remarks

Returns an object of type [RfsgDataTransfer](nationalinstruments-modularinstruments-nirfsg-rfsgdatatransfer.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DataTransfer property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-digitalpatternenabled.html language=enus -->
## TOPIC 00011: DigitalPatternEnabled

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-digitalpatternenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-digitalpatternenabled.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to enable digital pattern on the arbitrary waveform generator (AWG) module. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool DigitalPatternEnabled { get; set; }Remarkstrue if digital pattern is enabled and false, if digital pattern is disabled. This prop

### DigitalPatternEnabled

Gets or sets whether to enable digital pattern on the arbitrary waveform generator (AWG) module.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool DigitalPatternEnabled { get; set; }

#### Remarks

true if digital pattern is enabled and false, if digital pattern is disabled.

This property must be set to true to enable signal routing to and from the digital data and control connector.

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DigitalPatternEnabled property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-generationmode.html language=enus -->
## TOPIC 00012: GenerationMode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-generationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-generationmode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to generate a continuous wave (CW) signal, the arb waveform specified by SelectedWaveform, or the script specified by SelectedScriptName, on calling Initiate. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgWaveformGenerationMode GenerationMode { get; se

### GenerationMode

Gets or sets whether to generate a continuous wave (CW) signal, the arb waveform specified by [SelectedWaveform](nationalinstruments-modularinstruments-nirfsg-rfsgarb-selectedwaveform.html), or the script specified by [SelectedScriptName](nationalinstruments-modularinstruments-nirfsg-rfsgscripting-selectedscriptname.html), on calling [Initiate](nationalinstruments-modularinstruments-nirfsg-nirfsg-initiate.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgWaveformGenerationMode](nationalinstruments-modularinstruments-nirfsg-rfsgwaveformgenerationmode.html) GenerationMode { get; set; }

#### Remarks

Specifies the [RfsgWaveformGenerationMode](nationalinstruments-modularinstruments-nirfsg-rfsgwaveformgenerationmode.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GenerationMode property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-getscript__string-ref.html language=enus -->
## TOPIC 00013: GetScript(string, ref string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-getscript__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-getscript__string-ref.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the content of specified script. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void GetScript(string scriptName, ref string script)ParametersNameTypeDescriptionscriptNamestringContains the name of the script. scriptref stringContains the script associated with the scri

### GetScript(string, ref string)

Returns the content of specified script.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void GetScript(string scriptName, ref string script)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scriptName | string | Contains the name of the script. |
| script | ref string | Contains the script associated with the scriptName. |

#### Returns

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-power.html language=enus -->
## TOPIC 00014: Power

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-power.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-power.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the output power, in dBm, from the arbitrary waveform generator (AWG) module. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double Power { get; }RemarksReturns a Double representing the output power, in dBm. If an arbitrary waveform is being generated, this property speci

### Power

Gets the output power, in dBm, from the arbitrary waveform generator (AWG) module.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double Power { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the output power, in dBm.

If an arbitrary waveform is being generated, this property specifies either the average power or the peak power of the signal, depending on [PowerLevelType](nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerleveltype.html) setting.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Power property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-prefiltergain.html language=enus -->
## TOPIC 00015: PreFilterGain

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-prefiltergain.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-prefiltergain.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the arbitrary waveform generator (AWG) prefilter gain, in dB. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double PreFilterGain { get; set; }RemarksSpecifies a Double representing the AWG prefilter gain, in dB. Reduce the AWG prefilter gain value to prevent overf

### PreFilterGain

Gets or sets the arbitrary waveform generator (AWG) prefilter gain, in dB.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double PreFilterGain { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the AWG prefilter gain, in dB.

Reduce the AWG prefilter gain value to prevent overflow in the interpolation filters. Other gains on the RF signal generator are automatically adjusted to compensate for non-unity prefilter gain.

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PreFilterGain property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-pulseshaping.html language=enus -->
## TOPIC 00016: PulseShaping

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-pulseshaping.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-pulseshaping.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the PulseShaping sub-object used to configure the arbitrary waveform generator (AWG) filter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgPulseShaping PulseShaping { get; }RemarksReturns an object of type RfsgPulseShaping. ExceptionsTypeDescriptionSystem.ObjectDispos

### PulseShaping

Gets the PulseShaping sub-object used to configure the arbitrary waveform generator (AWG) filter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgPulseShaping](nationalinstruments-modularinstruments-nirfsg-rfsgpulseshaping.html) PulseShaping { get; }

#### Remarks

Returns an object of type [RfsgPulseShaping](nationalinstruments-modularinstruments-nirfsg-rfsgpulseshaping.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PulseShaping property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-setarbwaveformnextwriteposition__string-rfsgarbwaveformrelativewriteposition-int.html language=enus -->
## TOPIC 00017: SetArbWaveformNextWritePosition(string, RfsgArbWaveformRelativeWritePosition, int)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-setarbwaveformnextwriteposition__string-rfsgarbwaveformrelativewriteposition-int.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-setarbwaveformnextwriteposition__string-rfsgarbwaveformrelativewriteposition-int.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start position to use the write a waveform with the next call to the WriteWaveform methods. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void SetArbWaveformNextWritePosition(string name, RfsgArbWaveformRelativeWritePosition relativeTo, int offset)Remarks Define

### SetArbWaveformNextWritePosition(string, RfsgArbWaveformRelativeWritePosition, int)

Configures the start position to use the write a waveform with the next call to the WriteWaveform methods.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void SetArbWaveformNextWritePosition(string name, RfsgArbWaveformRelativeWritePosition relativeTo, int offset)

#### Remarks

Defined values:

- [StartOfWaveform](nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformrelativewriteposition.html) - The reference position is relative to the start of the waveform.
- [CurrentPosition](nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformrelativewriteposition.html) - The reference position is relative to the current position.

This method allows you to write to arbitrary locations within the waveform.

These settings apply only to the next write to the waveform specified by the *name*  of [AllocateWaveform](nationalinstruments-modularinstruments-nirfsg-rfsgarb-allocatewaveform__string-int.html) or one of the WriteWaveform methods. Subsequent writes to that waveform begin where the last write ended, unless this method is called again.

If you use this method to write to the waveform that is currently generating, an undefined output may result.

Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The identity of the waveform. This string is case-insensitive, alphanumeric, and does not use reserved words. |
| relativeTo | RfsgArbWaveformRelativeWritePosition | The reference position in the waveform. The position and offset together determine where to start loading data into the waveform. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| offset | int | The offset for relativeTo at which to start loading the data into the waveform. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SetArbWaveformNextWritePosition method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-waveforms.html language=enus -->
## TOPIC 00018: Waveforms

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-waveforms.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties used to configure Arb Waveform. A waveform name can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgArbWaveformCollection.this[string]. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgArbWaveformCollection Waveforms { get; }Remar

### Waveforms

Gets properties used to configure Arb Waveform. A waveform name can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgArbWaveformCollection.this[string].

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgArbWaveformCollection](nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformcollection.html) Waveforms { get; }

#### Remarks

Returns an object of type [RfsgArbWaveformCollection](nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformcollection.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Waveforms property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarb-writewaveform__string-complexdouble_arr1.html language=enus -->
## TOPIC 00019: WriteWaveform(string, ComplexDouble[])

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarb-writewaveform__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarb-writewaveform__string-complexdouble_arr1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an arbitrary waveform to the NI-RFSG, starting from the position of the last data written in the onboard memory. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void WriteWaveform(string name, ComplexDouble[] data)RemarksThis method takes the data array of a complex baseb

### WriteWaveform(string, ComplexDouble[])

Writes an arbitrary waveform to the NI-RFSG, starting from the position of the last data written in the onboard memory.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void WriteWaveform(string name, ComplexDouble[] data)

#### Remarks

This method takes the data array of a complex baseband signals data as input. If the waveform is large, use the [AllocateWaveform](nationalinstruments-modularinstruments-nirfsg-rfsgarb-allocatewaveform__string-int.html) method.

The NI-RFSG must be in the Configuration state before you call [WriteWaveform](nationalinstruments-modularinstruments-nirfsg-rfsgarb-writewaveform__string-double_arr1-double_arr1.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words. |
| data | ComplexDouble[] | Specifies the array of data to load onto the waveform. The data array passed to this method should be of type NationalInstruments.ComplexDouble. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The WriteWaveform method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArb Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-onboardclockmode.html language=enus -->
## TOPIC 00020: OnboardClockMode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-onboardclockmode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-onboardclockmode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the clock mode on the AWG module. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgOnboardSampleClockMode OnboardClockMode { get; set; }RemarksSpecifies the RfsgOnboardSampleClockMode enumeration.To set this property, the NI-RFSG must be in the Configuration stat

### OnboardClockMode

Gets or sets the clock mode on the AWG module.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgOnboardSampleClockMode](nationalinstruments-modularinstruments-nirfsg-rfsgonboardsampleclockmode.html) OnboardClockMode { get; set; }

#### Remarks

Specifies the [RfsgOnboardSampleClockMode](nationalinstruments-modularinstruments-nirfsg-rfsgonboardsampleclockmode.html) enumeration.

To set this property, the NI-RFSG must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The OnboardClockMode property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArbSampleClock Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-rate.html language=enus -->
## TOPIC 00021: Rate

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-rate.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the rate of the sample clock, in Hertz (Hz), on the arbitrary waveform generator (AWG) module. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double Rate { get; }RemarksReturns a Double representing the rate of the sample clock in Hz. ExceptionsTypeDescriptionSystem.Object

### Rate

Gets the rate of the sample clock, in Hertz (Hz), on the arbitrary waveform generator (AWG) module.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double Rate { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the rate of the sample clock in Hz.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Rate property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArbSampleClock Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-source.html language=enus -->
## TOPIC 00022: Source

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-source.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock-source.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the sample clock source for the arbitrary waveform generator (AWG) module. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgArbSampleClockSource Source { get; set; }RemarksSpecifies an object of type RfsgArbSampleClockSource. To set this property, the NI-RFSG mus

### Source

Gets or sets the sample clock source for the arbitrary waveform generator (AWG) module.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgArbSampleClockSource](nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclocksource.html) Source { get; set; }

#### Remarks

Specifies an object of type [RfsgArbSampleClockSource](nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclocksource.html).

To set this property, the NI-RFSG must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Source property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgArbSampleClock Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock.html language=enus -->
## TOPIC 00023: RfsgArbSampleClock Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarbsampleclock.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides properties used to configure the Arb Sample clock. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgArbSampleClock : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF Si

### RfsgArbSampleClock Class

Provides properties used to configure the Arb Sample clock.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgArbSampleClock : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| OnboardClockMode | Gets or sets the clock mode on the AWG module. |
| OscillatorPhaseDacValue | Gets or sets the oscillator phase digital-to-analog converter (DAC) value. |
| Rate | Gets the rate of the sample clock, in Hertz (Hz), on the arbitrary waveform generator (AWG) module. |
| Source | Gets or sets the sample clock source for the arbitrary waveform generator (AWG) module. |
| Synchronized | Provides the properties used for synchronizing the Sample Clock. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformattributes-runtimescaling.html language=enus -->
## TOPIC 00024: RuntimeScaling

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformattributes-runtimescaling.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformattributes-runtimescaling.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets or gets the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing. /summary> value>Specifies the value of waveform runtime scaling.remarks>Supported Devices: PXIe-5820/5830/5831/5832/5840/5841 /remarks> SyntaxNamespace: Nationa

### RuntimeScaling

Sets or gets the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing. /summary> value>Specifies the value of waveform runtime scaling.

remarks>Supported Devices: PXIe-5820/5830/5831/5832/5840/5841 /remarks>

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double RuntimeScaling { get; set; }

Parent topic:

RfsgArbWaveformAttributes Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformattributes-signalbandwidth.html language=enus -->
## TOPIC 00025: SignalBandwidth

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformattributes-signalbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgarbwaveformattributes-signalbandwidth.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets or gets the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8 × I/Q rate). /summary> value> Specifies the bandwidth of the arbitrary signal. /value> remarks>Supported Devices: PXIe-5820/5830/5831/5832/5840/5841 /remarks> SyntaxNamespace: NationalInstruments.Modula

### SignalBandwidth

Sets or gets the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8 × I/Q rate). /summary> value> Specifies the bandwidth of the arbitrary signal. /value> remarks>Supported Devices: PXIe-5820/5830/5831/5832/5840/5841 /remarks>

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double SignalBandwidth { get; set; }

Parent topic:

RfsgArbWaveformAttributes Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlist-isdone.html language=enus -->
## TOPIC 00026: IsDone

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlist-isdone.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlist-isdone.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the configuration list is still running or done. To read this property, the device must be in the Generation state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool IsDone { get; }Remarkstrue if configuration list is done; otherwise, false. ExceptionsTypeDescrip

### IsDone

Gets whether the configuration list is still running or done. To read this property, the device must be in the Generation state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool IsDone { get; }

#### Remarks

true if configuration list is done; otherwise, false.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The IsDone property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgBasicConfigurationList Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlist-repeat.html language=enus -->
## TOPIC 00027: Repeat

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlist-repeat.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlist-repeat.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the configuration list runs only once or continuously. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgBasicConfigurationListRepeat Repeat { get; set; }RemarksSpecifies the RfsgBasicConfigurationListRepeat enumeration. ExceptionsTypeDescriptionSystem.Obj

### Repeat

Gets or sets whether the configuration list runs only once or continuously.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgBasicConfigurationListRepeat](nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlistrepeat.html) Repeat { get; set; }

#### Remarks

Specifies the [RfsgBasicConfigurationListRepeat](nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlistrepeat.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Repeat property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgBasicConfigurationList Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlistrepeat.html language=enus -->
## TOPIC 00028: RfsgBasicConfigurationListRepeat Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlistrepeat.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgbasicconfigurationlistrepeat.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the configuration list runs continuously. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgBasicConfigurationListRepeatMembersNameValueDescriptionContinuous0NI-RFSG runs the configuration list continuously. Single1NI-RFSG runs the configuration list onl

### RfsgBasicConfigurationListRepeat Enumeration

Specifies whether the configuration list runs continuously.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgBasicConfigurationListRepeat

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Continuous | 0 | NI-RFSG runs the configuration list continuously. |
| Single | 1 | NI-RFSG runs the configuration list only once. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgburstdetection-powerthreshold.html language=enus -->
## TOPIC 00029: PowerThreshold

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgburstdetection-powerthreshold.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgburstdetection-powerthreshold.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets or gets the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this property. para>This prope

### PowerThreshold

Sets or gets the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this property. para>This property is ignored when you disable the RfsgBurstDetectionEnabled property or when you set the RfsgBurstDetectionMode property to Auto.

/summary> value>Specifies the relative power level at which burst start or stop locations are detected.

remarks> Supported Devices: PXIe-5820/5830/5831/5832/5840/5841.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double PowerThreshold { get; set; }

Parent topic:

RfsgBurstDetection Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgburstdetection.html language=enus -->
## TOPIC 00030: RfsgBurstDetection Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgburstdetection.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgburstdetection.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods and properties used to configure the burst properties of a waveform. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgBurstDetection : RfsgSubObjectPropertiesNameDescriptionEnabledEnables the detection of burst start and burst s

### RfsgBurstDetection Class

Provides methods and properties used to configure the burst properties of a waveform.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgBurstDetection : RfsgSubObject

#### Properties

| Name | Description |
| --- | --- |
| Enabled | Enables the detection of burst start and burst stop locations in the waveform. Set this method to Enabled before writing a waveform to RFSG memory for detecting bursts. You can read the detected burst start and burst stop locations using GetWaveformBurstStartLocations and GetWaveformBurstStopLocations methods respectively. blockquote>When you download a waveform using ReadandDownloadWaveformFromfileTDMS and if RFBlankingproperty is enabled, you must set the RfsgBurstDetectionEnabled property to Disable.Note For PXIe-5830/5831/5832, the RF Blanking reserves a PXI trigger line. If you are calling any ResetDevice or RfsaDriverUtility.ResetDevice on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call ResetWithOptions or RfsaDriverUtility.ResetWithOptions. Select Routes in the stepsToOmit parameter./summary> value> Specifies the detection of burst start and burst stop locations in the waveform. /value> |
| MinimumBurstTime | Sets or gets the minimum duration of the detected bursts. Any detected burst with a duration smaller than the value of this property is ignored by NI-RFSG. para>This property is ignored when you disable the RfsgBurstDetectionEnabled property or when you set the RfsgBurstDetectionMode property to Auto./summary> value>Specifies the minimum duration of the detected bursts.remarks> Supported Devices: PXIe-5820/5830/5831/5832/5840/5841. |
| MinimumQuietTime | Sets or gets the time duration for which the signal must be quiet before a valid burst start location or after a valid burst stop location. para>This method is ignored when you disable the RfsgBurstDetectionEnabled or when you set the RfsgBurstDetectionModeproperty to Auto. |
| Mode | Sets or gets the algorithm that NI-RFSG uses to detect the burst start and burst stop locations in the waveform when burst detection is enabled using the RfsgBurstDetectionEnabled property. When you set RfsgBurstDetectionMode to Auto, NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. To fine-tune the burst detection process parameters yourself, you can set this attribute to Manual and specify the burst detection parameters using the MinimumQuietTime, PowerThreshold, and MinimumBurstTime methods. |
| PowerThreshold | Sets or gets the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this property. para>This property is ignored when you disable the RfsgBurstDetectionEnabled property or when you set the RfsgBurstDetectionMode property to Auto./summary> value>Specifies the relative power level at which burst start or stop locations are detected.remarks> Supported Devices: PXIe-5820/5830/5831/5832/5840/5841. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgcalibration-self.html language=enus -->
## TOPIC 00031: Self

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgcalibration-self.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgcalibration-self.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RfsgSelfCalibration sub-object that provides the methods and properties for self-calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgSelfCalibration Self { get; }RemarksReturns an object of type RfsgSelfCalibration.

### Self

Gets the [RfsgSelfCalibration](nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration.html) sub-object that provides the methods and properties for self-calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgSelfCalibration](nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration.html) Self { get; }

#### Remarks

Returns an object of type [RfsgSelfCalibration](nationalinstruments-modularinstruments-nirfsg-rfsgselfcalibration.html).

Parent topic:

RfsgCalibration Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgcalibration.html language=enus -->
## TOPIC 00032: RfsgCalibration Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgcalibration.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the properties to calibrate NI-RFSG device. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgCalibration : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF Signal Gener

### RfsgCalibration Class

Provides the properties to calibrate NI-RFSG device.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgCalibration : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| Self | Gets the RfsgSelfCalibration sub-object that provides the methods and properties for self-calibration. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-configuredeembeddingtableinterpolationlinear__string-rfsglinearinterpolationformat.html language=enus -->
## TOPIC 00033: ConfigureDeembeddingTableInterpolationLinear(string, RfsgLinearInterpolationFormat)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-configuredeembeddingtableinterpolationlinear__string-rfsglinearinterpolationformat.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-configuredeembeddingtableinterpolationlinear__string-rfsglinearinterpolationformat.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the linear interpolation method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ConfigureDeembeddingTableInterpolationLinear(string tableName, RfsgLinearInterpolationFormat format)RemarksIf the carrier frequency does not match a row in the de-embedding table, this

### ConfigureDeembeddingTableInterpolationLinear(string, RfsgLinearInterpolationFormat)

Selects the linear interpolation method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ConfigureDeembeddingTableInterpolationLinear(string tableName, RfsgLinearInterpolationFormat format)

#### Remarks

If the carrier frequency does not match a row in the de-embedding table, this method performs a linear interpolation based on the entries above and below in the de-embedding table to determine the parameters used for de-embedding.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. |
| format | RfsgLinearInterpolationFormat | Specifies the format of parameters to interpolate. |

Parent topic:

RfsgChannelBasedDeembedding Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-configuredeembeddingtableinterpolationspline__string.html language=enus -->
## TOPIC 00034: ConfigureDeembeddingTableInterpolationSpline(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-configuredeembeddingtableinterpolationspline__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-configuredeembeddingtableinterpolationspline__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the spline interpolation method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ConfigureDeembeddingTableInterpolationSpline(string tableName)RemarksIf the carrier frequency does not match a row in the de-embedding table, this method performs a spline interpolation

### ConfigureDeembeddingTableInterpolationSpline(string)

Selects the spline interpolation method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ConfigureDeembeddingTableInterpolationSpline(string tableName)

#### Remarks

If the carrier frequency does not match a row in the de-embedding table, this method performs a spline interpolation based on the entries above and below in the de-embedding table to determine the parameters used for de-embedding.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. The name must be unique for a given port, but not across ports. |

Parent topic:

RfsgChannelBasedDeembedding Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingcompensationgain.html language=enus -->
## TOPIC 00035: DeembeddingCompensationGain

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingcompensationgain.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingcompensationgain.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the de-embedding compensation gain(as double) used to compensate the mismatch on the specified port defined by sParameterTables. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double DeembeddingCompensationGain { get; }RemarksSpecifies a Double representing the de-embeddin

### DeembeddingCompensationGain

Gets the de-embedding compensation gain(as double) used to compensate the mismatch on the specified port defined by sParameterTables.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double DeembeddingCompensationGain { get; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the de-embedding compensation gain.

To use this property, you must set the channelName of the [RfsgChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding.html) sub-object to specify the name of the port to configure for de-embedding.

A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgDeembedding.this[string].

Use the [CreateDeembeddingSParameterTableS2pFile](nationalinstruments-modularinstruments-nirfsg-rfsgdeembedding-createdeembeddingsparametertables2pfile__string-string-rfsgsparameterorientation.html) to create tables.

Parent topic:

RfsgChannelBasedDeembedding Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingselectedtable.html language=enus -->
## TOPIC 00036: DeembeddingSelectedTable

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingselectedtable.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingselectedtable.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the de-embedding table to apply to the measurements on the specified port. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string DeembeddingSelectedTable { get; set; }RemarksSpecifies a String representing the de-embedding type.To use this property, you must set th

### DeembeddingSelectedTable

Gets or sets the de-embedding table to apply to the measurements on the specified port.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string DeembeddingSelectedTable { get; set; }

#### Remarks

Specifies a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the de-embedding type.

To use this property, you must set the channelName of the [RfsgChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding.html) sub-object to specify the name of the port to configure for de-embedding.

A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgDeembedding.this[string].

Use the [CreateDeembeddingSParameterTableS2pFile](nationalinstruments-modularinstruments-nirfsg-rfsgdeembedding-createdeembeddingsparametertables2pfile__string-string-rfsgsparameterorientation.html) to create tables.

Parent topic:

RfsgChannelBasedDeembedding Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingtype.html language=enus -->
## TOPIC 00037: DeembeddingType

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingtype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding-deembeddingtype.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of de-embedding to apply to measurements on the specified port. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDeembeddingType DeembeddingType { get; set; }RemarksTo use this property, you must set the channelName of the RfsgChannelBasedDeembedding sub

### DeembeddingType

Gets or sets the type of de-embedding to apply to measurements on the specified port.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgDeembeddingType](nationalinstruments-modularinstruments-nirfsg-rfsgdeembeddingtype.html) DeembeddingType { get; set; }

#### Remarks

To use this property, you must set the channelName of the [RfsgChannelBasedDeembedding](nationalinstruments-modularinstruments-nirfsg-rfsgchannelbaseddeembedding.html) sub-object to specify the name of the port to configure for de-embedding. A port can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgDeembedding.this[string].

Specifies a [RfsgDeembeddingType](nationalinstruments-modularinstruments-nirfsg-rfsgdeembeddingtype.html) representing the de-embedding type.

Parent topic:

RfsgChannelBasedDeembedding Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasediqoutport-commonmodeoffset.html language=enus -->
## TOPIC 00038: CommonModeOffset

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasediqoutport-commonmodeoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasediqoutport-commonmodeoffset.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the common-mode offset applied to the signals generated at each differential output terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double CommonModeOffset { get; set; }RemarksSpecifies a Double representing the common-mode offset, in volts (V), applied to

### CommonModeOffset

Gets or sets the common-mode offset applied to the signals generated at each differential output terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double CommonModeOffset { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the common-mode offset, in volts (V), applied to the generated signals at each differential output terminal.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CommonModeOffset property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgChannelBasedIQOutPort Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasedlo-loopbandwidth.html language=enus -->
## TOPIC 00039: LoopBandwidth

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasedlo-loopbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasedlo-loopbandwidth.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the loop bandwidth of the tuning phase-locked loops (PLL). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgLoopBandwidth LoopBandwidth { get; set; }RemarksSpecifies the RfsgLoopBandwidth enumeration.To use this property for the PXIe-5830/5831/5832, you must spec

### LoopBandwidth

Gets or sets the loop bandwidth of the tuning phase-locked loops (PLL).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgLoopBandwidth](nationalinstruments-modularinstruments-nirfsg-rfsgloopbandwidth.html) LoopBandwidth { get; set; }

#### Remarks

Specifies the [RfsgLoopBandwidth](nationalinstruments-modularinstruments-nirfsg-rfsgloopbandwidth.html) enumeration.

To use this property for the PXIe-5830/5831/5832, you must specify the the channelName of the [RfsgChannelBasedLO](nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgRFLocalOscillator.this[string]

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LoopBandwidth property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgChannelBasedLO Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptrigger-terminalname.html language=enus -->
## TOPIC 00040: TerminalName

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptrigger-terminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptrigger-terminalname.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fully-qualified signal name. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string TerminalName { get; }RemarksReturns a String representing the fully-qualified signal name. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe TerminalName property was accessed a

### TerminalName

Gets the fully-qualified signal name.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string TerminalName { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the fully-qualified signal name.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The TerminalName property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgConfigurationListStepTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio1.html language=enus -->
## TOPIC 00041: Dio1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgConfigurationListStepTriggerExportedOutputTerminal Dio1 { get; }RemarksReturns an object of type RfsgConfigurationListStepTriggerExportedOutputTermin

### Dio1

Gets the source terminal when the trigger is received on the DIO PFI1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgConfigurationListStepTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal.html) Dio1 { get; }

#### Remarks

Returns an object of type [RfsgConfigurationListStepTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal.html) representing the string "DIO/PFI1".

Parent topic:

RfsgConfigurationListStepTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio4.html language=enus -->
## TOPIC 00042: Dio4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgConfigurationListStepTriggerExportedOutputTerminal Dio4 { get; }RemarksReturns an object of type RfsgConfigurationListStepTriggerExportedOutputTermin

### Dio4

Gets the source terminal when the trigger is received on the DIO PFI4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgConfigurationListStepTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal.html) Dio4 { get; }

#### Remarks

Returns an object of type [RfsgConfigurationListStepTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal.html) representing the string "DIO/PFI4".

Parent topic:

RfsgConfigurationListStepTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio7.html language=enus -->
## TOPIC 00043: Dio7

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-dio7.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgConfigurationListStepTriggerExportedOutputTerminal Dio7 { get; }RemarksReturns an object of type RfsgConfigurationListStepTriggerExportedOutputTermin

### Dio7

Gets the source terminal when the trigger is received on the DIO PFI7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgConfigurationListStepTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal.html) Dio7 { get; }

#### Remarks

Returns an object of type [RfsgConfigurationListStepTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal.html) representing the string "DIO/PFI7".

Parent topic:

RfsgConfigurationListStepTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-operator_eq__rfsgconfigurationliststeptriggerexportedoutputterminal-rfsgconfiguratio...d203e537.html language=enus -->
## TOPIC 00044: operator==(RfsgConfigurationListStepTriggerExportedOutputTerminal, RfsgConfigurationListStepTriggerExportedOutputTerminal)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-operator_eq__rfsgconfigurationliststeptriggerexportedoutputterminal-rfsgconfiguratio...d203e537.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-operator_eq__rfsgconfigurationliststeptriggerexportedoutputterminal-rfsgconfiguratio...d203e537.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgConfigurationListStepTriggerExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgConfigurationListStepTriggerExportedOutputTerminal outputTerminal1, RfsgConfigurationListStepTriggerEx

### operator==(RfsgConfigurationListStepTriggerExportedOutputTerminal, RfsgConfigurationListStepTriggerExportedOutputTerminal)

Checks whether the two instances of [RfsgConfigurationListStepTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgConfigurationListStepTriggerExportedOutputTerminal outputTerminal1, RfsgConfigurationListStepTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsgConfigurationListStepTriggerExportedOutputTerminal | Specifies an RfsgConfigurationListStepTriggerExportedOutputTerminal object. |
| outputTerminal2 | RfsgConfigurationListStepTriggerExportedOutputTerminal | Specifies an RfsgConfigurationListStepTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgConfigurationListStepTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-operator_neq__rfsgconfigurationliststeptriggerexportedoutputterminal-rfsgconfigurati...d203e485.html language=enus -->
## TOPIC 00045: operator!=(RfsgConfigurationListStepTriggerExportedOutputTerminal, RfsgConfigurationListStepTriggerExportedOutputTerminal)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-operator_neq__rfsgconfigurationliststeptriggerexportedoutputterminal-rfsgconfigurati...d203e485.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal-operator_neq__rfsgconfigurationliststeptriggerexportedoutputterminal-rfsgconfigurati...d203e485.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgConfigurationListStepTriggerExportedOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgConfigurationListStepTriggerExportedOutputTerminal outputTerminal1, RfsgConfigurationListStepTrigger

### operator!=(RfsgConfigurationListStepTriggerExportedOutputTerminal, RfsgConfigurationListStepTriggerExportedOutputTerminal)

Checks whether the two instances of [RfsgConfigurationListStepTriggerExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggerexportedoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgConfigurationListStepTriggerExportedOutputTerminal outputTerminal1, RfsgConfigurationListStepTriggerExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsgConfigurationListStepTriggerExportedOutputTerminal | Specifies an RfsgConfigurationListStepTriggerExportedOutputTerminal object. |
| outputTerminal2 | RfsgConfigurationListStepTriggerExportedOutputTerminal | Specifies an RfsgConfigurationListStepTriggerExportedOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsgConfigurationListStepTriggerExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-operator_eq__rfsgconfigurationsettledeventexportedoutputterminal-rfsgconfigurationsettl...d235e357.html language=enus -->
## TOPIC 00046: operator==(RfsgConfigurationSettledEventExportedOutputTerminal, RfsgConfigurationSettledEventExportedOutputTerminal)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-operator_eq__rfsgconfigurationsettledeventexportedoutputterminal-rfsgconfigurationsettl...d235e357.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-operator_eq__rfsgconfigurationsettledeventexportedoutputterminal-rfsgconfigurationsettl...d235e357.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgConfigurationSettledEventExportedOutputTerminal are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgConfigurationSettledEventExportedOutputTerminal outputTerminal1, RfsgConfigurationSettledEventExportedOut

### operator==(RfsgConfigurationSettledEventExportedOutputTerminal, RfsgConfigurationSettledEventExportedOutputTerminal)

Checks whether the two instances of [RfsgConfigurationSettledEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgConfigurationSettledEventExportedOutputTerminal outputTerminal1, RfsgConfigurationSettledEventExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsgConfigurationSettledEventExportedOutputTerminal | Specifies the first instance to be compared. |
| outputTerminal2 | RfsgConfigurationSettledEventExportedOutputTerminal | Specifies the second instance to be compared. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgConfigurationSettledEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-operator_neq__rfsgconfigurationsettledeventexportedoutputterminal-rfsgconfigurationsett...d235e313.html language=enus -->
## TOPIC 00047: operator!=(RfsgConfigurationSettledEventExportedOutputTerminal, RfsgConfigurationSettledEventExportedOutputTerminal)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-operator_neq__rfsgconfigurationsettledeventexportedoutputterminal-rfsgconfigurationsett...d235e313.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-operator_neq__rfsgconfigurationsettledeventexportedoutputterminal-rfsgconfigurationsett...d235e313.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgConfigurationSettledEventExportedOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgConfigurationSettledEventExportedOutputTerminal outputTerminal1, RfsgConfigurationSettledEventExportedO

### operator!=(RfsgConfigurationSettledEventExportedOutputTerminal, RfsgConfigurationSettledEventExportedOutputTerminal)

Checks whether the two instances of [RfsgConfigurationSettledEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgConfigurationSettledEventExportedOutputTerminal outputTerminal1, RfsgConfigurationSettledEventExportedOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsgConfigurationSettledEventExportedOutputTerminal | Specifies the first instance to be compared. |
| outputTerminal2 | RfsgConfigurationSettledEventExportedOutputTerminal | Specifies the second instance to be compared. |

#### Returns

true if the two instances are not equal; otherwise, false.

Parent topic:

RfsgConfigurationSettledEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-triggeroutputterminal.html language=enus -->
## TOPIC 00048: TriggerOutputTerminal

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-triggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal-triggeroutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the TRIG IN/OUT terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgConfigurationSettledEventExportedOutputTerminal TriggerOutputTerminal { get; }RemarksReturns an object of type RfsgConfigurationSettl

### TriggerOutputTerminal

Gets the destination terminal when the signal is exported to the TRIG IN/OUT terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgConfigurationSettledEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal.html) TriggerOutputTerminal { get; }

#### Remarks

Returns an object of type [RfsgConfigurationSettledEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal.html) representing the string "TrigOut".

Parent topic:

RfsgConfigurationSettledEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal.html language=enus -->
## TOPIC 00049: RfsgConfigurationSettledEventExportedOutputTerminal Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationsettledeventexportedoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal for RfsgDoneEvent. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgConfigurationSettledEventExportedOutputTerminalRemarksSee ExportedOutputTerminal. PropertiesNameDescriptionDoNotExportGets the destination terminal when the

### RfsgConfigurationSettledEventExportedOutputTerminal Class

Gets the destination terminal for [RfsgDoneEvent](nationalinstruments-modularinstruments-nirfsg-rfsgdoneevent.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgConfigurationSettledEventExportedOutputTerminal

#### Remarks

See [ExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgdoneevent-exportedoutputterminal.html).

#### Properties

| Name | Description |
| --- | --- |
| DoNotExport | Gets the destination terminal when the signal is not exported. |
| PXIeDStarC | Gets the destination terminal when the signal is exported to the PXIe DStar C trigger line. This value is valid only on the PXIe-5820/5830/5831/5832/5840. |
| PxiTriggerLine0 | Gets the destination terminal when the signal is exported to the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the destination terminal when the signal is exported to the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the destination terminal when the signal is exported to the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the destination terminal when the signal is exported to the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the destination terminal when the signal is exported to the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the destination terminal when the signal is exported to the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the destination terminal when the signal is exported to the PXI trigger line 6. |
| TriggerOutputTerminal | Gets the destination terminal when the signal is exported to the TRIG IN/OUT terminal. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates a RfsgConfigurationSettledEventExportedOutputTerminal object from the specified string. |
| Equals(RfsgConfigurationSettledEventExportedOutputTerminal) | Determines whether the current instance of RfsgConfigurationSettledEventExportedOutputTerminal and the RfsgConfigurationSettledEventExportedOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgConfigurationSettledEventExportedOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgConfigurationSettledEventExportedOutputTerminal. |
| ToString() | Converts the current instance of RfsgConfigurationSettledEventExportedOutputTerminal to equivalent string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgConfigurationSettledEventExportedOutputTerminal(string) | Converts the specified string to equivalent RfsgConfigurationSettledEventExportedOutputTerminal object. |
| operator string(RfsgConfigurationSettledEventExportedOutputTerminal) | Converts the RfsgConfigurationSettledEventExportedOutputTerminal object to equivalent string. |
| operator!=(RfsgConfigurationSettledEventExportedOutputTerminal, RfsgConfigurationSettledEventExportedOutputTerminal) | Checks whether the two instances of RfsgConfigurationSettledEventExportedOutputTerminal are unequal. |
| operator==(RfsgConfigurationSettledEventExportedOutputTerminal, RfsgConfigurationSettledEventExportedOutputTerminal) | Checks whether the two instances of RfsgConfigurationSettledEventExportedOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdatatransfer-directdma.html language=enus -->
## TOPIC 00050: DirectDma

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdatatransfer-directdma.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdatatransfer-directdma.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DirectDma sub-object used to configure direct DMA to transfer waveform data to the RF signal generator onboard memory at rates well beyond the typical 5 MB/s to 30 MB/s range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDirectDma DirectDma { get; }RemarksReturns

### DirectDma

Gets the DirectDma sub-object used to configure direct DMA to transfer waveform data to the RF signal generator onboard memory at rates well beyond the typical 5 MB/s to 30 MB/s range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgDirectDma](nationalinstruments-modularinstruments-nirfsg-rfsgdirectdma.html) DirectDma { get; }

#### Remarks

Returns an object of type [RfsgDirectDma](nationalinstruments-modularinstruments-nirfsg-rfsgdirectdma.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DirectDma property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDataTransfer Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdatatransfer-maximumbandwidth.html language=enus -->
## TOPIC 00051: MaximumBandwidth

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdatatransfer-maximumbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdatatransfer-maximumbandwidth.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum amount of bus bandwidth to use for data transfers. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double MaximumBandwidth { get; set; }RemarksSpecifies a Double representing the maximum amount of bus bandwidth to use for data transfers. ExceptionsTypeDe

### MaximumBandwidth

Gets or sets the maximum amount of bus bandwidth to use for data transfers.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double MaximumBandwidth { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the maximum amount of bus bandwidth to use for data transfers.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The MaximumBandwidth property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDataTransfer Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdeembedding-configuredeembeddingtableinterpolationlinear__string-rfsglinearinterpolationformat.html language=enus -->
## TOPIC 00052: ConfigureDeembeddingTableInterpolationLinear(string, RfsgLinearInterpolationFormat)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdeembedding-configuredeembeddingtableinterpolationlinear__string-rfsglinearinterpolationformat.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdeembedding-configuredeembeddingtableinterpolationlinear__string-rfsglinearinterpolationformat.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the linear interpolation method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ConfigureDeembeddingTableInterpolationLinear(string tableName, RfsgLinearInterpolationFormat format)RemarksIf the carrier frequency does not match a row in the de-embedding table, this

### ConfigureDeembeddingTableInterpolationLinear(string, RfsgLinearInterpolationFormat)

Selects the linear interpolation method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ConfigureDeembeddingTableInterpolationLinear(string tableName, RfsgLinearInterpolationFormat format)

#### Remarks

If the carrier frequency does not match a row in the de-embedding table, this method performs a linear interpolation based on the entries above and below in the de-embedding table to determine the parameters used for de-embedding.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| tableName | string | Specifies the name of the table. |
| format | RfsgLinearInterpolationFormat | Specifies the format of parameters to interpolate. |

Parent topic:

RfsgDeembedding Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdeembedding.html language=enus -->
## TOPIC 00053: RfsgDeembedding Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdeembedding.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdeembedding.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the properties and methods used to configure Deembedding. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgDeembedding : RfsgSubObjectRemarksFor more information, refer to NI RF Signal Generators Help. PropertiesNameDescriptionDeembed

### RfsgDeembedding Class

Represents the properties and methods used to configure Deembedding.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgDeembedding : RfsgSubObject

#### Remarks

For more information, refer to [NI RF Signal Generators Help](https://RFSG.chm::/ProgFLow.html).

#### Properties

| Name | Description |
| --- | --- |
| DeembeddingCompensationGain | Gets the de-embedding compensation gain(as double) used to compensate the mismatch on the specified port defined by sParameterTables. |
| DeembeddingSelectedTable | Gets or sets the de-embedding table to apply to the measurements. |
| DeembeddingType | Gets or sets the type of de-embedding to apply to measurements. |
| this[string channelName] | Gets the RfsgChannelBasedDeembedding sub-object to configure channel based Deembedding properties. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureDeembeddingTableInterpolationLinear(string, RfsgLinearInterpolationFormat) | Selects the linear interpolation method. |
| ConfigureDeembeddingTableInterpolationNearest(string) | Selects the nearest interpolation method. |
| ConfigureDeembeddingTableInterpolationSpline(string) | Selects the spline interpolation method. |
| CreateDeembeddingSParameterTableArray(string, double[], ComplexDouble, RfsgSParameterOrientation) | Creates an s-parameter de-embedding table from the input data. |
| CreateDeembeddingSParameterTableS2pFile(string, string, RfsgSParameterOrientation) | Creates an S-parameter de-embedding table based on the specified S2P file. |
| DeleteAllDeembeddingTables() | Deletes all configured de-embedding tables for the session. |
| DeleteDeembeddingTable(string) | Deletes the selected de-embedding table. |
| GetDeembeddingSParameters(ref ComplexDouble) | Returns the S-parameters used for de-embedding a measurement. This includes interpolation of the parameters based on the configured carrier frequency. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharacteristics-devicetemperature.html language=enus -->
## TOPIC 00054: DeviceTemperature

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharacteristics-devicetemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharacteristics-devicetemperature.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the device temperature in degrees Celsius (°C). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double DeviceTemperature { get; }RemarksReturns a Double representing the device temperature. If the NI-RFSG session is controlling multiple devices, this property returns the te

### DeviceTemperature

Gets the device temperature in degrees Celsius (°C).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double DeviceTemperature { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the device temperature.

If the NI-RFSG session is controlling multiple devices, this property returns the temperature of the primary RF device. The NI-RFSG session is opened using the primary RF device name.

Serial signals between the temperature sensor and the system control unit can modulate the signal being generated, thus causing phase spurs. After the device is thoroughly warmed up, its temperature varies only slightly (less than 1 °C) and slowly, so it is not necessary to constantly poll this temperature sensor.

For more information about device temperature, refer to the [Thermal Management](https://RFSG.chm::/Thermal_management.html) session in the *NI RF Signal Generators Help*.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DeviceTemperature property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDeviceCharacteristics Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharacteristics-lotemperature.html language=enus -->
## TOPIC 00055: LOTemperature

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharacteristics-lotemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharacteristics-lotemperature.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the LO module temperature, in degrees Celsius (°C). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double LOTemperature { get; }RemarksReturns a Double representing the LO module temperature, in degrees Celsius (°C). ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionT

### LOTemperature

Gets the LO module temperature, in degrees Celsius (°C).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double LOTemperature { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the LO module temperature, in degrees Celsius (°C).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOTemperature property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDeviceCharacteristics Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharactersticsoptions-fasttuningoption.html language=enus -->
## TOPIC 00056: FastTuningOption

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharactersticsoptions-fasttuningoption.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharactersticsoptions-fasttuningoption.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the NI RF signal generator has the fast tuning option available. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool FastTuningOption { get; }Remarkstrue if NI RF signal generator has the fast tuning option available; otherwise, false. ExceptionsTypeDescriptionSyst

### FastTuningOption

Gets whether the NI RF signal generator has the fast tuning option available.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool FastTuningOption { get; }

#### Remarks

true if NI RF signal generator has the fast tuning option available; otherwise, false.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The FastTuningOption property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDeviceCharactersticsOptions Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdeviceevents-startedevent.html language=enus -->
## TOPIC 00057: StartedEvent

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdeviceevents-startedevent.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdeviceevents-startedevent.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the StartedEvent sub-object containing properties used to configure Started Events. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgStartedEvent StartedEvent { get; }RemarksReturns object of type RfsgStartedEvent. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionT

### StartedEvent

Gets the StartedEvent sub-object containing properties used to configure Started Events.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgStartedEvent](nationalinstruments-modularinstruments-nirfsg-rfsgstartedevent.html) StartedEvent { get; }

#### Remarks

Returns object of type [RfsgStartedEvent](nationalinstruments-modularinstruments-nirfsg-rfsgstartedevent.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The StartedEvent property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDeviceEvents Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptrigger-configure__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgtriggeredge.html language=enus -->
## TOPIC 00058: Configure(RfsgDigitalEdgeConfigurationListStepTriggerSource, RfsgTriggerEdge)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptrigger-configure__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgtriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptrigger-configure__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgtriggeredge.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Configuration List Step trigger for digital edge triggering. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Configure(RfsgDigitalEdgeConfigurationListStepTriggerSource source, RfsgTriggerEdge edge)RemarksThis method is valid only when TriggerType is set to D

### Configure(RfsgDigitalEdgeConfigurationListStepTriggerSource, RfsgTriggerEdge)

Configures the Configuration List Step trigger for digital edge triggering.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void Configure(RfsgDigitalEdgeConfigurationListStepTriggerSource source, RfsgTriggerEdge edge)

#### Remarks

This method is valid only when [TriggerType](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptrigger-triggertype.html) is set to [DigitalEdge](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsgDigitalEdgeConfigurationListStepTriggerSource | Specifies the trigger source terminal for the digital edge Configuration List Step trigger. NI-RFSG sets Source to this value. Refer to this property for possible values. |
| edge | RfsgTriggerEdge | Specifies the active edge for the digital edge Configuration List Step trigger. NI-RFSG sets Edge to this value. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Configure method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDigitalEdgeConfigurationListStepTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptrigger-source.html language=enus -->
## TOPIC 00059: Source

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptrigger-source.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the source terminal for RfsgConfigurationListStepTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDigitalEdgeConfigurationListStepTriggerSource Source { get; set; }RemarksSpecifies an object of type RfsgDigitalEdgeConfigurationListStepTriggerSource. This

### Source

Gets or sets the source terminal for [RfsgConfigurationListStepTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) Source { get; set; }

#### Remarks

Specifies an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html).

This property is valid only when [TriggerType](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptrigger-triggertype.html) is set to [DigitalEdge](nationalinstruments-modularinstruments-nirfsg-rfsgconfigurationliststeptriggertype.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Source property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDigitalEdgeConfigurationListStepTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio1.html language=enus -->
## TOPIC 00060: Dio1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource Dio1 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStepTriggerSource represe

### Dio1

Gets the source terminal when the trigger is received on the DIO PFI1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) Dio1 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "DIO/PFI1".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio2.html language=enus -->
## TOPIC 00061: Dio2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource Dio2 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStepTriggerSource represe

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "DIO/PFI2".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio6.html language=enus -->
## TOPIC 00062: Dio6

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio6.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource Dio6 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStepTriggerSource represe

### Dio6

Gets the source terminal when the trigger is received on the DIO PFI6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) Dio6 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "DIO/PFI6".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio7.html language=enus -->
## TOPIC 00063: Dio7

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-dio7.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource Dio7 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStepTriggerSource represe

### Dio7

Gets the source terminal when the trigger is received on the DIO PFI7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) Dio7 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "DIO/PFI7".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-marker3event.html language=enus -->
## TOPIC 00064: Marker3Event

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-marker3event.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-marker3event.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on generation of the Marker 3 event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource Marker3Event { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationL

### Marker3Event

Gets the source terminal when the trigger is received on generation of the Marker 3 event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) Marker3Event { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "Marker3Event".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator-rfsgdigitaledgeconfigurationliststeptriggersource__string.html language=enus -->
## TOPIC 00065: operator RfsgDigitalEdgeConfigurationListStepTriggerSource(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator-rfsgdigitaledgeconfigurationliststeptriggersource__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator-rfsgdigitaledgeconfigurationliststeptriggersource__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string representation to its RfsgDigitalEdgeConfigurationListStepTriggerSource equivalent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator RfsgDigitalEdgeConfigurationListStepTriggerSource(string source)ParametersNameTypeDescriptio

### operator RfsgDigitalEdgeConfigurationListStepTriggerSource(string)

Converts the specified string representation to its [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) equivalent.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator RfsgDigitalEdgeConfigurationListStepTriggerSource(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies the string to be converted. |

#### Returns

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html).

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator-string__rfsgdigitaledgeconfigurationliststeptriggersource.html language=enus -->
## TOPIC 00066: operator string(RfsgDigitalEdgeConfigurationListStepTriggerSource)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator-string__rfsgdigitaledgeconfigurationliststeptriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator-string__rfsgdigitaledgeconfigurationliststeptriggersource.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the RfsgDigitalEdgeConfigurationListStepTriggerSource object to its string equivalent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator string(RfsgDigitalEdgeConfigurationListStepTriggerSource source)ParametersNameTypeDescriptionsourceRfsgDigital

### operator string(RfsgDigitalEdgeConfigurationListStepTriggerSource)

Converts the [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) object to its string equivalent.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator string(RfsgDigitalEdgeConfigurationListStepTriggerSource source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsgDigitalEdgeConfigurationListStepTriggerSource | Specifies the RfsgDigitalEdgeConfigurationListStepTriggerSource object to be converted. |

#### Returns

Returns a string equivalent.

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator_eq__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgdigitaledgeconfigurati...d305e642.html language=enus -->
## TOPIC 00067: operator==(RfsgDigitalEdgeConfigurationListStepTriggerSource, RfsgDigitalEdgeConfigurationListStepTriggerSource)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator_eq__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgdigitaledgeconfigurati...d305e642.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator_eq__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgdigitaledgeconfigurati...d305e642.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgDigitalEdgeConfigurationListStepTriggerSource are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgDigitalEdgeConfigurationListStepTriggerSource source1, RfsgDigitalEdgeConfigurationListStepTriggerSource so

### operator==(RfsgDigitalEdgeConfigurationListStepTriggerSource, RfsgDigitalEdgeConfigurationListStepTriggerSource)

Checks whether the two instances of [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgDigitalEdgeConfigurationListStepTriggerSource source1, RfsgDigitalEdgeConfigurationListStepTriggerSource source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsgDigitalEdgeConfigurationListStepTriggerSource | Specifies an RfsgDigitalEdgeConfigurationListStepTriggerSource object. |
| source2 | RfsgDigitalEdgeConfigurationListStepTriggerSource | Specifies an RfsgDigitalEdgeConfigurationListStepTriggerSource object . |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator_neq__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgdigitaledgeconfigurat...d305e590.html language=enus -->
## TOPIC 00068: operator!=(RfsgDigitalEdgeConfigurationListStepTriggerSource, RfsgDigitalEdgeConfigurationListStepTriggerSource)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator_neq__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgdigitaledgeconfigurat...d305e590.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-operator_neq__rfsgdigitaledgeconfigurationliststeptriggersource-rfsgdigitaledgeconfigurat...d305e590.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgDigitalEdgeConfigurationListStepTriggerSource are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgDigitalEdgeConfigurationListStepTriggerSource source1, RfsgDigitalEdgeConfigurationListStepTriggerSource

### operator!=(RfsgDigitalEdgeConfigurationListStepTriggerSource, RfsgDigitalEdgeConfigurationListStepTriggerSource)

Checks whether the two instances of [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgDigitalEdgeConfigurationListStepTriggerSource source1, RfsgDigitalEdgeConfigurationListStepTriggerSource source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsgDigitalEdgeConfigurationListStepTriggerSource | Specifies an RfsgDigitalEdgeConfigurationListStepTriggerSource object. |
| source2 | RfsgDigitalEdgeConfigurationListStepTriggerSource | Specifies an RfsgDigitalEdgeConfigurationListStepTriggerSource object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pfi0.html language=enus -->
## TOPIC 00069: Pfi0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pfi0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource Pfi0 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStepTriggerSource

### Pfi0

Gets the source terminal when the trigger is received on the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PFI0".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pfi1.html language=enus -->
## TOPIC 00070: Pfi1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pfi1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PFI 1 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource Pfi1 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStepTriggerSource

### Pfi1

Gets the source terminal when the trigger is received on the PFI 1 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) Pfi1 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PFI1".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxiedstarb.html language=enus -->
## TOPIC 00071: PXIeDStarB

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxiedstarb.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxiedstarb.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5840. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PXIeDStarB { get; }RemarksReturns an o

### PXIeDStarB

Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5840.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PXIeDStarB { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXIe_DStarB".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline0.html language=enus -->
## TOPIC 00072: PxiTriggerLine0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PxiTriggerLine0 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStep

### PxiTriggerLine0

Gets the source terminal when the trigger is received on the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXI_Trig0".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline1.html language=enus -->
## TOPIC 00073: PxiTriggerLine1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PxiTriggerLine1 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStep

### PxiTriggerLine1

Gets the source terminal when the trigger is received on the PXI trigger line 1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXI_Trig1".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline2.html language=enus -->
## TOPIC 00074: PxiTriggerLine2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PxiTriggerLine2 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStep

### PxiTriggerLine2

Gets the source terminal when the trigger is received on the PXI trigger line 2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PxiTriggerLine2 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXI_Trig2".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline3.html language=enus -->
## TOPIC 00075: PxiTriggerLine3

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline3.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PxiTriggerLine3 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStep

### PxiTriggerLine3

Gets the source terminal when the trigger is received on the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PxiTriggerLine3 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXI_Trig3".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline4.html language=enus -->
## TOPIC 00076: PxiTriggerLine4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PxiTriggerLine4 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStep

### PxiTriggerLine4

Gets the source terminal when the trigger is received on the PXI trigger line 4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PxiTriggerLine4 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXI_Trig4".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline5.html language=enus -->
## TOPIC 00077: PxiTriggerLine5

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline5.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PxiTriggerLine5 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStep

### PxiTriggerLine5

Gets the source terminal when the trigger is received on the PXI trigger line 5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PxiTriggerLine5 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXI_Trig5".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline6.html language=enus -->
## TOPIC 00078: PxiTriggerLine6

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline6.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PxiTriggerLine6 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStep

### PxiTriggerLine6

Gets the source terminal when the trigger is received on the PXI trigger line 6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PxiTriggerLine6 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXI_Trig6".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline7.html language=enus -->
## TOPIC 00079: PxiTriggerLine7

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-pxitriggerline7.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource PxiTriggerLine7 { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStep

### PxiTriggerLine7

Gets the source terminal when the trigger is received on the PXI trigger line 7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) PxiTriggerLine7 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "PXI_Trig7.

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-timerevent.html language=enus -->
## TOPIC 00080: TimerEvent

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-timerevent.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-timerevent.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal for the trigger received when the timer emits an event. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeConfigurationListStepTriggerSource TimerEvent { get; }RemarksReturns an object of type RfsgDigitalEdgeConfigurationListStepTrigg

### TimerEvent

Gets the source terminal for the trigger received when the timer emits an event.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) TimerEvent { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) representing the string "TimerEvent".

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-tostring.html language=enus -->
## TOPIC 00081: ToString()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource-tostring.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsgDigitalEdgeConfigurationListStepTriggerSource to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override string ToString()ReturnsReturns a string equivalent that represents the current instance of RfsgDigitalEdgeConfigurationListStep

### ToString()

Converts the current instance of [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override string ToString()

#### Returns

Returns a string equivalent that represents the current instance of [RfsgDigitalEdgeConfigurationListStepTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html).

Parent topic:

RfsgDigitalEdgeConfigurationListStepTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html language=enus -->
## TOPIC 00082: RfsgDigitalEdgeConfigurationListStepTriggerSource Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptriggersource.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the source terminal for RfsgDigitalEdgeConfigurationListStepTrigger. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgDigitalEdgeConfigurationListStepTriggerSourceRemarksSee Source. PropertiesNameDescriptionDio1Gets the source terminal when th

### RfsgDigitalEdgeConfigurationListStepTriggerSource Class

Represents the source terminal for [RfsgDigitalEdgeConfigurationListStepTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptrigger.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgDigitalEdgeConfigurationListStepTriggerSource

#### Remarks

See [Source](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgeconfigurationliststeptrigger-source.html).

#### Properties

| Name | Description |
| --- | --- |
| Dio1 | Gets the source terminal when the trigger is received on the DIO PFI1. |
| Dio2 | Gets the source terminal when the trigger is received on the DIO PFI2. |
| Dio3 | Gets the source terminal when the trigger is received on the DIO PFI3. |
| Dio4 | Gets the source terminal when the trigger is received on the DIO PFI4. |
| Dio5 | Gets the source terminal when the trigger is received on the DIO PFI5. |
| Dio6 | Gets the source terminal when the trigger is received on the DIO PFI6. |
| Dio7 | Gets the source terminal when the trigger is received on the DIO PFI7. |
| DioO | Gets the source terminal when the trigger is received on the DIO PFI0. |
| Marker0Event | Gets the source terminal when the trigger is received on generation of the Marker 0 event. |
| Marker1Event | Gets the source terminal when the trigger is received on generation of the Marker 1 event. |
| Marker2Event | Gets the source terminal when the trigger is received on generation of the Marker 2 event. |
| Marker3Event | Gets the source terminal when the trigger is received on generation of the Marker 3 event. |
| Pfi0 | Gets the source terminal when the trigger is received on the PFI 0 connector. |
| Pfi1 | Gets the source terminal when the trigger is received on the PFI 1 connector. |
| PXIeDStarB | Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5840. |
| PxiTriggerLine0 | Gets the source terminal when the trigger is received on the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the source terminal when the trigger is received on the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the source terminal when the trigger is received on the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the source terminal when the trigger is received on the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the source terminal when the trigger is received on the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the source terminal when the trigger is received on the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the source terminal when the trigger is received on the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the source terminal when the trigger is received on the PXI trigger line 7. |
| TimerEvent | Gets the source terminal for the trigger received when the timer emits an event. |
| TriggerInputTerminal | Gets the source terminal for the trigger received on the TRIG IN/OUT terminal. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsgDigitalEdgeConfigurationListStepTriggerSource object from the specified string. |
| Equals(RfsgDigitalEdgeConfigurationListStepTriggerSource) | Determines whether the current instance of RfsgDigitalEdgeConfigurationListStepTriggerSource and the RfsgDigitalEdgeConfigurationListStepTriggerSource object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgDigitalEdgeConfigurationListStepTriggerSource and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgDigitalEdgeConfigurationListStepTriggerSource. |
| ToString() | Converts the current instance of RfsgDigitalEdgeConfigurationListStepTriggerSource to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgDigitalEdgeConfigurationListStepTriggerSource(string) | Converts the specified string representation to its RfsgDigitalEdgeConfigurationListStepTriggerSource equivalent. |
| operator string(RfsgDigitalEdgeConfigurationListStepTriggerSource) | Converts the RfsgDigitalEdgeConfigurationListStepTriggerSource object to its string equivalent. |
| operator!=(RfsgDigitalEdgeConfigurationListStepTriggerSource, RfsgDigitalEdgeConfigurationListStepTriggerSource) | Checks whether the two instances of RfsgDigitalEdgeConfigurationListStepTriggerSource are unequal. |
| operator==(RfsgDigitalEdgeConfigurationListStepTriggerSource, RfsgDigitalEdgeConfigurationListStepTriggerSource) | Checks whether the two instances of RfsgDigitalEdgeConfigurationListStepTriggerSource are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttrigger-configure__rfsgdigitaledgescripttriggersource-rfsgtriggeredge.html language=enus -->
## TOPIC 00083: Configure(RfsgDigitalEdgeScriptTriggerSource, RfsgTriggerEdge)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttrigger-configure__rfsgdigitaledgescripttriggersource-rfsgtriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttrigger-configure__rfsgdigitaledgescripttriggersource-rfsgtriggeredge.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the specified Script trigger for digital edge triggering. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Configure(RfsgDigitalEdgeScriptTriggerSource source, RfsgTriggerEdge edge)RemarksThe default value is RisingEdge. ParametersNameTypeDescriptionsourceRfsgDigi

### Configure(RfsgDigitalEdgeScriptTriggerSource, RfsgTriggerEdge)

Configures the specified Script trigger for digital edge triggering.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void Configure(RfsgDigitalEdgeScriptTriggerSource source, RfsgTriggerEdge edge)

#### Remarks

The default value is [RisingEdge](nationalinstruments-modularinstruments-nirfsg-rfsgtriggeredge.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsgDigitalEdgeScriptTriggerSource | Specifies the source terminal for the digital edge Script trigger. NI-RFSG sets Source to this value. |
| edge | RfsgTriggerEdge | Specifies the active edge for the digital edge Script trigger. NI-RFSG sets Edge to this value. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Configure method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDigitalEdgeScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttrigger-edge.html language=enus -->
## TOPIC 00084: Edge

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttrigger-edge.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the active edge for the digital edge Script trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgTriggerEdge Edge { get; set; }RemarksSpecifies the RfsgTriggerEdge enumeration. The default value is RisingEdge. This property is used when TriggerType is set to

### Edge

Gets or sets the active edge for the digital edge Script trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgTriggerEdge](nationalinstruments-modularinstruments-nirfsg-rfsgtriggeredge.html) Edge { get; set; }

#### Remarks

Specifies the [RfsgTriggerEdge](nationalinstruments-modularinstruments-nirfsg-rfsgtriggeredge.html) enumeration. The default value is [RisingEdge](nationalinstruments-modularinstruments-nirfsg-rfsgtriggeredge.html).

This property is used when [TriggerType](nationalinstruments-modularinstruments-nirfsg-rfsgscripttrigger-triggertype.html) is set to [DigitalEdge](nationalinstruments-modularinstruments-nirfsg-rfsgscripttriggertype.html).

This property is not case-sensitive. To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Edge property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDigitalEdgeScriptTrigger Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio1.html language=enus -->
## TOPIC 00085: Dio1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeScriptTriggerSource Dio1 { get; }RemarksReturns an object of type RfsgDigitalEdgeScriptTriggerSource representing the string "DIO/PFI1".

### Dio1

Gets the source terminal when the trigger is received on the DIO PFI1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) Dio1 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) representing the string "DIO/PFI1".

Parent topic:

RfsgDigitalEdgeScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio3.html language=enus -->
## TOPIC 00086: Dio3

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio3.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeScriptTriggerSource Dio3 { get; }RemarksReturns an object of type RfsgDigitalEdgeScriptTriggerSource representing the string "DIO/PFI3".

### Dio3

Gets the source terminal when the trigger is received on the DIO PFI3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) Dio3 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) representing the string "DIO/PFI3".

Parent topic:

RfsgDigitalEdgeScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio4.html language=enus -->
## TOPIC 00087: Dio4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI4. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeScriptTriggerSource Dio4 { get; }RemarksReturns an object of type RfsgDigitalEdgeScriptTriggerSource representing the string "DIO/PFI4".

### Dio4

Gets the source terminal when the trigger is received on the DIO PFI4.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) Dio4 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) representing the string "DIO/PFI4".

Parent topic:

RfsgDigitalEdgeScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio5.html language=enus -->
## TOPIC 00088: Dio5

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio5.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI5. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeScriptTriggerSource Dio5 { get; }RemarksReturns an object of type RfsgDigitalEdgeScriptTriggerSource representing the string "DIO/PFI5".

### Dio5

Gets the source terminal when the trigger is received on the DIO PFI5.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) Dio5 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) representing the string "DIO/PFI5".

Parent topic:

RfsgDigitalEdgeScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio6.html language=enus -->
## TOPIC 00089: Dio6

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio6.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeScriptTriggerSource Dio6 { get; }RemarksReturns an object of type RfsgDigitalEdgeScriptTriggerSource representing the string "DIO/PFI6".

### Dio6

Gets the source terminal when the trigger is received on the DIO PFI6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) Dio6 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) representing the string "DIO/PFI6".

Parent topic:

RfsgDigitalEdgeScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio7.html language=enus -->
## TOPIC 00090: Dio7

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio7.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dio7.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI7. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeScriptTriggerSource Dio7 { get; }RemarksReturns an object of type RfsgDigitalEdgeScriptTriggerSource representing the string "DIO/PFI7".

### Dio7

Gets the source terminal when the trigger is received on the DIO PFI7.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) Dio7 { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) representing the string "DIO/PFI7".

Parent topic:

RfsgDigitalEdgeScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dioo.html language=enus -->
## TOPIC 00091: DioO

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dioo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-dioo.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalEdgeScriptTriggerSource DioO { get; }RemarksReturns an object of type RfsgDigitalEdgeScriptTriggerSource representing the string "DIO/PFI0".

### DioO

Gets the source terminal when the trigger is received on the DIO PFI0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) DioO { get; }

#### Remarks

Returns an object of type [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) representing the string "DIO/PFI0".

Parent topic:

RfsgDigitalEdgeScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-equals__object.html language=enus -->
## TOPIC 00092: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgDigitalEdgeScriptTriggerSource and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to t

### Equals(object)

Determines whether the current instance of [RfsgDigitalEdgeScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitaledgescripttriggersource.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsgDigitalEdgeScriptTriggerSource. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgDigitalEdgeScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-dio6.html language=enus -->
## TOPIC 00093: Dio6

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-dio6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-dio6.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalLevelScriptTriggerSource Dio6 { get; }RemarksReturns an object of type RfsgDigitalLevelScriptTriggerSource representing the string "DIO/PFI6".

### Dio6

Gets the source terminal when the trigger is received on the DIO PFI6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) Dio6 { get; }

#### Remarks

Returns an object of type [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) representing the string "DIO/PFI6".

Parent topic:

RfsgDigitalLevelScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-gethashcode.html language=enus -->
## TOPIC 00094: GetHashCode()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-gethashcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsgDigitalLevelScriptTriggerSource. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsgDigitalLevelScriptTriggerSource.

### GetHashCode()

Returns the hash code for the current instance of [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html).

Parent topic:

RfsgDigitalLevelScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pfi0.html language=enus -->
## TOPIC 00095: Pfi0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pfi0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalLevelScriptTriggerSource Pfi0 { get; }RemarksReturns an object of type RfsgDigitalLevelScriptTriggerSource representing the string "PFI

### Pfi0

Gets the source terminal when the trigger is received on the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) representing the string "PFI0".

Parent topic:

RfsgDigitalLevelScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pfi2.html language=enus -->
## TOPIC 00096: Pfi2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pfi2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pfi2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PFI 2 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalLevelScriptTriggerSource Pfi2 { get; }RemarksReturns an object of type RfsgDigitalLevelScriptTriggerSource representing the string "PFI

### Pfi2

Gets the source terminal when the trigger is received on the PFI 2 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) Pfi2 { get; }

#### Remarks

Returns an object of type [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) representing the string "PFI2".

Parent topic:

RfsgDigitalLevelScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pxitriggerline0.html language=enus -->
## TOPIC 00097: PxiTriggerLine0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pxitriggerline0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalLevelScriptTriggerSource PxiTriggerLine0 { get; }RemarksReturns an object of type RfsgDigitalLevelScriptTriggerSource representing t

### PxiTriggerLine0

Gets the source terminal when the trigger is received on the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) representing the string "PXI_Trig0".

Parent topic:

RfsgDigitalLevelScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pxitriggerline3.html language=enus -->
## TOPIC 00098: PxiTriggerLine3

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pxitriggerline3.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-pxitriggerline3.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the PXI trigger line 3. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalLevelScriptTriggerSource PxiTriggerLine3 { get; }RemarksReturns an object of type RfsgDigitalLevelScriptTriggerSource representing t

### PxiTriggerLine3

Gets the source terminal when the trigger is received on the PXI trigger line 3.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) PxiTriggerLine3 { get; }

#### Remarks

Returns an object of type [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) representing the string "PXI_Trig3".

Parent topic:

RfsgDigitalLevelScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-synchronizationstarttriggerline.html language=enus -->
## TOPIC 00099: SynchronizationStartTriggerLine

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-synchronizationstarttriggerline.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-synchronizationstarttriggerline.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the Synchronization Start trigger line. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDigitalLevelScriptTriggerSource SynchronizationStartTriggerLine { get; }RemarksReturns an object of type RfsgDigitalLevelSc

### SynchronizationStartTriggerLine

Gets the source terminal when the trigger is received on the Synchronization Start trigger line.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) SynchronizationStartTriggerLine { get; }

#### Remarks

Returns an object of type [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) representing the string "Sync_Start".

Parent topic:

RfsgDigitalLevelScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-tostring.html language=enus -->
## TOPIC 00100: ToString()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource-tostring.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsgDigitalLevelScriptTriggerSource to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override string ToString()ReturnsReturns a string that represents the current instance of RfsgDigitalLevelScriptTriggerSource.

### ToString()

Converts the current instance of [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsgDigitalLevelScriptTriggerSource](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html).

Parent topic:

RfsgDigitalLevelScriptTriggerSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html language=enus -->
## TOPIC 00101: RfsgDigitalLevelScriptTriggerSource Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttriggersource.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the source terminal for RfsgDigitalLevelScriptTrigger. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgDigitalLevelScriptTriggerSourceRemarksSee Source. PropertiesNameDescriptionDio1Gets the source terminal when the trigger is received on the

### RfsgDigitalLevelScriptTriggerSource Class

Represents the source terminal for [RfsgDigitalLevelScriptTrigger](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttrigger.html).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgDigitalLevelScriptTriggerSource

#### Remarks

See [Source](nationalinstruments-modularinstruments-nirfsg-rfsgdigitallevelscripttrigger-source.html).

#### Properties

| Name | Description |
| --- | --- |
| Dio1 | Gets the source terminal when the trigger is received on the DIO PFI1. |
| Dio2 | Gets the source terminal when the trigger is received on the DIO PFI2. |
| Dio3 | Gets the source terminal when the trigger is received on the DIO PFI3. |
| Dio4 | Gets the source terminal when the trigger is received on the DIO PFI4. |
| Dio5 | Gets the source terminal when the trigger is received on the DIO PFI5. |
| Dio6 | Gets the source terminal when the trigger is received on the DIO PFI6. |
| Dio7 | Gets the source terminal when the trigger is received on the DIO PFI7. |
| DioO | Gets the source terminal when the trigger is received on the DIO PFI0. |
| Pfi0 | Gets the source terminal when the trigger is received on the PFI 0 connector. |
| Pfi1 | Gets the source terminal when the trigger is received on the PFI 1 connector. |
| Pfi2 | Gets the source terminal when the trigger is received on the PFI 2 connector. |
| Pfi3 | Gets the source terminal when the trigger is received on the PFI 3 connector. |
| PXIeDStarB | Gets the source terminal when the trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840. |
| PxiStarLine | Gets the source terminal when the trigger is received on the PXI Star trigger line. |
| PxiTriggerLine0 | Gets the source terminal when the trigger is received on the PXI trigger line 0. |
| PxiTriggerLine1 | Gets the source terminal when the trigger is received on the PXI trigger line 1. |
| PxiTriggerLine2 | Gets the source terminal when the trigger is received on the PXI trigger line 2. |
| PxiTriggerLine3 | Gets the source terminal when the trigger is received on the PXI trigger line 3. |
| PxiTriggerLine4 | Gets the source terminal when the trigger is received on the PXI trigger line 4. |
| PxiTriggerLine5 | Gets the source terminal when the trigger is received on the PXI trigger line 5. |
| PxiTriggerLine6 | Gets the source terminal when the trigger is received on the PXI trigger line 6. |
| PxiTriggerLine7 | Gets the source terminal when the trigger is received on the PXI trigger line 7. |
| SynchronizationStartTriggerLine | Gets the source terminal when the trigger is received on the Synchronization Start trigger line. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsgDigitalLevelScriptTriggerSource object from the specified string. |
| Equals(RfsgDigitalLevelScriptTriggerSource) | Determines whether the current instance of RfsgDigitalLevelScriptTriggerSource and the RfsgDigitalLevelScriptTriggerSource object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgDigitalLevelScriptTriggerSource and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgDigitalLevelScriptTriggerSource. |
| ToString() | Converts the current instance of RfsgDigitalLevelScriptTriggerSource to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgDigitalLevelScriptTriggerSource(string) | Converts the specified string to equivalent RfsgDigitalLevelScriptTriggerSource object. |
| operator string(RfsgDigitalLevelScriptTriggerSource) | Converts the RfsgDigitalLevelScriptTriggerSource object to equivalent string. |
| operator!=(RfsgDigitalLevelScriptTriggerSource, RfsgDigitalLevelScriptTriggerSource) | Checks whether the two instances of RfsgDigitalLevelScriptTriggerSource are unequal. |
| operator==(RfsgDigitalLevelScriptTriggerSource, RfsgDigitalLevelScriptTriggerSource) | Checks whether the two instances of RfsgDigitalLevelScriptTriggerSource are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdigitalmodulation-configureuserdefinedwaveform__byte_arr1.html language=enus -->
## TOPIC 00102: ConfigureUserDefinedWaveform(byte[])

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdigitalmodulation-configureuserdefinedwaveform__byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdigitalmodulation-configureuserdefinedwaveform__byte_arr1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the message signal used for digital modulation when WaveformType is set to UserDefined. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ConfigureUserDefinedWaveform(byte[] userDefinedWaveform)ParametersNameTypeDescriptionuserDefinedWaveformbyte[]Specifies the user

### ConfigureUserDefinedWaveform(byte[])

Specifies the message signal used for digital modulation when [WaveformType](nationalinstruments-modularinstruments-nirfsg-rfsgdigitalmodulation-waveformtype.html) is set to [UserDefined](nationalinstruments-modularinstruments-nirfsg-rfsgdigitalmodulationwaveformtype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ConfigureUserDefinedWaveform(byte[] userDefinedWaveform)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| userDefinedWaveform | byte[] | Specifies the user-defined message signal used for digital modulation. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ConfigureUserDefinedWaveform method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDigitalModulation Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-dio1.html language=enus -->
## TOPIC 00103: Dio1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-dio1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-dio1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI1. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDoneEventExportedOutputTerminal Dio1 { get; }RemarksReturns an object of type RfsgDoneEventExportedOutputTerminal representing the string "DIO/PFI1".

### Dio1

Gets the source terminal when the trigger is received on the DIO PFI1.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal.html) Dio1 { get; }

#### Remarks

Returns an object of type [RfsgDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal.html) representing the string "DIO/PFI1".

Parent topic:

RfsgDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-pfi4.html language=enus -->
## TOPIC 00104: Pfi4

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-pfi4.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-pfi4.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 4 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDoneEventExportedOutputTerminal Pfi4 { get; }RemarksReturns an object of type RfsgDoneEventExportedOutputTerminal representing the string

### Pfi4

Gets the destination terminal when the signal is exported to the PFI 4 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal.html) Pfi4 { get; }

#### Remarks

Returns an object of type [RfsgDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal.html) representing the string "PFI4".

Parent topic:

RfsgDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00105: PxiTriggerLine0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal-pxitriggerline0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgDoneEventExportedOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type RfsgDoneEventExportedOutputTerminal representi

### PxiTriggerLine0

Gets the destination terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [RfsgDoneEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgdoneeventexportedoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

RfsgDoneEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-getsupportedinstrumentmodels.html language=enus -->
## TOPIC 00106: GetSupportedInstrumentModels()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-getsupportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-getsupportedinstrumentmodels.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of names of instrument models with which the IVI specific driver is compatible. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string[] GetSupportedInstrumentModels()RemarksThe list is returned as an array of strings. ReturnsReturns a String containing the list o

### GetSupportedInstrumentModels()

Returns a list of names of instrument models with which the IVI specific driver is compatible.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string[] GetSupportedInstrumentModels()

#### Remarks

The list is returned as an array of strings.

#### Returns

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) containing the list of names of instrument models with which the NI-RFSG is compatible.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GetSupportedInstrumentModels method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverIdentity Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-identifier.html language=enus -->
## TOPIC 00107: Identifier

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-identifier.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-identifier.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the serial number of the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string Identifier { get; }RemarksReturns a String containing the serial number of the instrument. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Identifier property was accessed

### Identifier

Gets the serial number of the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string Identifier { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) containing the serial number of the instrument.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Identifier property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverIdentity Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-revision.html language=enus -->
## TOPIC 00108: Revision

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-revision.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-revision.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string that contains additional version information about NI-RFSG. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string Revision { get; }RemarksReturns a String that contains additional version information about NI-RFSG. ExceptionsTypeDescriptionSystem.ObjectDisposedExc

### Revision

Gets a string that contains additional version information about NI-RFSG.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string Revision { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) that contains additional version information about NI-RFSG.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Revision property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverIdentity Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-specificationmajorversion.html language=enus -->
## TOPIC 00109: SpecificationMajorVersion

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-specificationmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-specificationmajorversion.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the major version number of this instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic int SpecificationMajorVersion { get; }RemarksReturns an Int32 representing the major version number of the IVI class specification with which NI-RFSG is compliant. Exceptions

### SpecificationMajorVersion

Gets the major version number of this instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public int SpecificationMajorVersion { get; }

#### Remarks

Returns an [Int32](https://learn.microsoft.com/dotnet/api/system.int32) representing the major version number of the IVI class specification with which NI-RFSG is compliant.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SpecificationMajorVersion property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverIdentity Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-vendor.html language=enus -->
## TOPIC 00110: Vendor

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-vendor.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity-vendor.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string that contains the name of the vendor that supplies NI-RFSG driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string Vendor { get; }RemarksReturns a String that contains the name of the vendor that supplies NI-RFSG driver. ExceptionsTypeDescriptionSystem.Objec

### Vendor

Gets a string that contains the name of the vendor that supplies NI-RFSG driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string Vendor { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) that contains the name of the vendor that supplies NI-RFSG driver.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Vendor property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverIdentity Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity.html language=enus -->
## TOPIC 00111: RfsgDriverIdentity Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveridentity.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties that provide identity and version information about the NI-RFSG driver. Derives fromRfsgSubObjectIIviDriverIdentityIIviComponentIdentitySyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgDriverIdentity : RfsgSubObject, IIviDriverIdent

### RfsgDriverIdentity Class

Represents the methods and properties that provide identity and version information about the NI-RFSG driver.

#### Derives from

- RfsgSubObject
- IIviDriverIdentity
- IIviComponentIdentity

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgDriverIdentity : RfsgSubObject, IIviDriverIdentity, IIviComponentIdentity

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| Description | Gets a string that contains a brief description of NI-RFSG driver. |
| Identifier | Gets the serial number of the instrument. |
| InstrumentFirmwareRevision | Gets firmware revision information for the NI-RFSG device you are currently using. |
| InstrumentManufacturer | Gets the name of the manufacturer of the current NI-RFSG device. |
| InstrumentModel | Gets a string that contains the model number or name of the NI-RFSG device that you are currently using. |
| Revision | Gets a string that contains additional version information about NI-RFSG. |
| SpecificationMajorVersion | Gets the major version number of this instrument driver. |
| SpecificationMinorVersion | Gets the minor version number of this instrument driver. |
| SpecificDriverMajorVersion | Gets the major version number of the IVI class specification with which NI-RFSG driver is compliant. |
| SpecificDriverMinorVersion | Gets the minor version number of the class specification with which NI-RFSG driver is compliant. |
| Vendor | Gets a string that contains the name of the vendor that supplies NI-RFSG driver. |

#### Methods

| Name | Description |
| --- | --- |
| GetGroupCapabilities() | Returns a list of names of class capability groups that the IVI specific driver implements. |
| GetSupportedInstrumentModels() | Returns a list of names of instrument models with which the IVI specific driver is compatible. |
| RevisionQuery() | Returns the revision numbers of the NI-RFSG driver and the instrument firmware. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriverlock-rfsgdriverlock__iividriverlock.html language=enus -->
## TOPIC 00112: RfsgDriverLock(IIviDriverLock)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriverlock-rfsgdriverlock__iividriverlock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriverlock-rfsgdriverlock__iividriverlock.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Constructs an NI-RFSG driver lock. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDriverLock(IIviDriverLock iviDriverLock)ParametersNameTypeDescriptioniviDriverLockIIviDriverLockSpecifies the base interface for synchronization locks obtained on the driver session. Exception

### RfsgDriverLock(IIviDriverLock)

Constructs an NI-RFSG driver lock.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public RfsgDriverLock(IIviDriverLock iviDriverLock)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| iviDriverLock | IIviDriverLock | Specifies the base interface for synchronization locks obtained on the driver session. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The RfsgDriverLock method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverLock Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-dispose.html language=enus -->
## TOPIC 00113: Dispose()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-dispose.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Dispose()

### Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void Dispose()

Parent topic:

RfsgDriverOperation Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-driversetup.html language=enus -->
## TOPIC 00114: DriverSetup

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-driversetup.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-driversetup.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the driver setup string that you specified in the IVI configuration store, when the instrument driver session was created or passed in the OptionString parameter of the NIRfsg constructor. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic String DriverSetup { get; }RemarksRet

### DriverSetup

Gets the driver setup string that you specified in the IVI configuration store, when the instrument driver session was created or passed in the *OptionString* parameter of the [NIRfsg](nationalinstruments-modularinstruments-nirfsg-nirfsg.html) constructor.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public String DriverSetup { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the driver setup string that you specified in the IVI configuration store.

Refer to the *[NIRfsg](nationalinstruments-modularinstruments-nirfsg-nirfsg.html) Constructors*for additional information about the *OptionString* parameter. Refer to the*NI RF Signal Generators Getting Started Guide*for more information about MAX setup.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DriverSetup property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverOperation Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-interchangecheck.html language=enus -->
## TOPIC 00115: InterchangeCheck

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-interchangecheck.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to perform interchangeability checking and retrieve interchangeability warnings. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool InterchangeCheck { get; set; }Remarkstrue if interchangeability checking is enabled; otherwise false. The default value is f

### InterchangeCheck

Gets or sets whether to perform interchangeability checking and retrieve interchangeability warnings.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool InterchangeCheck { get; set; }

#### Remarks

true if interchangeability checking is enabled; otherwise false. The default value is false.

This property is currently not supported.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The InterchangeCheck property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverOperation Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-simulate.html language=enus -->
## TOPIC 00116: Simulate

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation-simulate.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether NI-RFSG simulates I/O operations. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic Boolean Simulate { get; set; }Remarkstrue if NI-RFSG simulates instrument driver I/O operations. false if NI-RFSG communicates directly with the instrument. ExceptionsTypeDescriptionSy

### Simulate

Gets whether NI-RFSG simulates I/O operations.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public Boolean Simulate { get; set; }

#### Remarks

true if NI-RFSG simulates instrument driver I/O operations. false if NI-RFSG communicates directly with the instrument.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Simulate property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverOperation Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation.html language=enus -->
## TOPIC 00117: RfsgDriverOperation Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriveroperation.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the methods and properties that provide driver operation functionality. Derives fromRfsgSubObjectIIviDriverOperationIDisposableISupportSynchronizationContextSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgDriverOperation : RfsgSubObject, IIviDriverOperation,

### RfsgDriverOperation Class

Represents the methods and properties that provide driver operation functionality.

#### Derives from

- RfsgSubObject
- IIviDriverOperation
- IDisposable
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgDriverOperation : RfsgSubObject, IIviDriverOperation, IDisposable, ISupportSynchronizationContext

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| Cache | Gets or sets whether to cache the value of properties. |
| DriverSetup | Gets the driver setup string that you specified in the IVI configuration store, when the instrument driver session was created or passed in the OptionString parameter of the NIRfsg constructor. |
| InterchangeCheck | Gets or sets whether to perform interchangeability checking and retrieve interchangeability warnings. |
| IOResourceDescriptor | Gets the resource descriptor that the user specified for the physical device. |
| LogicalName | Gets the IVI logical name specified when you open the current session. |
| QueryInstrumentStatus | Gets or sets whether NI-RFSG queries the device status after each operation. |
| RangeCheck | Gets or sets whether to validate property values and method parameters. |
| RecordCoercions | Gets or sets whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. |
| Simulate | Gets whether NI-RFSG simulates I/O operations. |
| SynchronizeCallbacks | Gets or sets how events and callback delegates are invoked. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. |
| InvalidateAllAttributes() | Invalidates all properties. |
| ResetInterchangeCheck() | Resets the interchangeability checking algorithms of NI-RFSG. |

#### Events

| Name | Description |
| --- | --- |
| Warning | Occurs when the driver generates a warning. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-loadconfigurationsfromfile__string-string.html language=enus -->
## TOPIC 00118: LoadConfigurationsFromFile(string, string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-loadconfigurationsfromfile__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-loadconfigurationsfromfile__string-string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the configurations from the specified file to the NI-RFSG driver session. The VI does an implicit reset before loading the configurations from the file. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Lo

### LoadConfigurationsFromFile(string, string)

Loads the configurations from the specified file to the NI-RFSG driver session. The VI does an implicit reset before loading the configurations from the file. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void LoadConfigurationsFromFile(string channelName, string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelName | string | Specifies the name of the channel. This string is case-insensitive and alphanumeric, and it cannot use reserved words. |
| filePath | string | Specifies the absolute path of the file from which the NI-RFSG loads the configurations. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LoadConfigurationsFromFile method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-lock__ivi.driver.precisiontimespan.html language=enus -->
## TOPIC 00119: Lock(Ivi.Driver.PrecisionTimeSpan)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-lock__ivi.driver.precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-lock__ivi.driver.precisiontimespan.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obtains a multithread lock on the instrument session and specifies the maximum amount of time to wait to acquire the lock. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgDriverLock Lock(Ivi.Driver.PrecisionTimeSpan maxTime)RemarksThis method waits until all other execution

### Lock(Ivi.Driver.PrecisionTimeSpan)

Obtains a multithread lock on the instrument session and specifies the maximum amount of time to wait to acquire the lock.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgDriverLock](nationalinstruments-modularinstruments-nirfsg-rfsgdriverlock.html) Lock(Ivi.Driver.PrecisionTimeSpan maxTime)

#### Remarks

This method waits until all other execution threads have released their locks on the instrument session before it obtains a multithread lock on the instrument session.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maxTime | Ivi.Driver.PrecisionTimeSpan | Specifies the maximum amount of time to wait to acquire the lock. |

#### Returns

An [RfsgDriverLock](nationalinstruments-modularinstruments-nirfsg-rfsgdriverlock.html) object, that has the Unlock method.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Lock method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-reset.html language=enus -->
## TOPIC 00120: Reset()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-reset.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-reset.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all properties to their default values and moves the NI-RFSG device to the Configuration state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Reset()RemarksThis method aborts the generation, clears all routes, and resets session properties to the initial values. Du

### Reset()

Resets all properties to their default values and moves the NI-RFSG device to the Configuration state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void Reset()

#### Remarks

This method aborts the generation, clears all routes, and resets session properties to the initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route. Generally, calling this method instead of [ResetDevice](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetdevice.html) is acceptable. Reset executes faster than the [ResetDevice](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetdevice.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Reset method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetattribute__string-propertyinfo.html language=enus -->
## TOPIC 00121: ResetAttribute(string, PropertyInfo)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetattribute__string-propertyinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetattribute__string-propertyinfo.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the channel specific property to its default value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ResetAttribute(string channelName, PropertyInfo propertyToReset)ParametersNameTypeDescriptionchannelNamestringSpecifies the channel name of the channel specific proper

### ResetAttribute(string, PropertyInfo)

Resets the channel specific property to its default value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ResetAttribute(string channelName, PropertyInfo propertyToReset)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelName | string | Specifies the channel name of the channel specific property. |
| propertyToReset | PropertyInfo | Specifies the property to be reset. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ResetAttribute method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetwithdefaults.html language=enus -->
## TOPIC 00122: ResetWithDefaults()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetwithdefaults.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetwithdefaults.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a software reset of the device, returning it to the default state and applying any initial default settings from the Configuration state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void ResetWithDefaults()ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe R

### ResetWithDefaults()

Performs a software reset of the device, returning it to the default state and applying any initial default settings from the Configuration state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void ResetWithDefaults()

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ResetWithDefaults method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-saveconfigurationstofile__string-string.html language=enus -->
## TOPIC 00123: SaveConfigurationsToFile(string, string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-saveconfigurationstofile__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-saveconfigurationstofile__string-string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the configurations of the session to the specified file. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void SaveConfigurationsToFile(string channelName, string filePath)ParametersNameTypeDescriptionchannelN

### SaveConfigurationsToFile(string, string)

Saves the configurations of the session to the specified file. Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void SaveConfigurationsToFile(string channelName, string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channelName | string | Specifies the name of the channel. This string is case-insensitive and alphanumeric, and it cannot use reserved words. |
| filePath | string | Specifies the absolute path of the file to which the NI-RFSG saves the configurations. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SaveConfigurationsToFile method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgDriverUtility Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal-operator-rfsgexportedpulsemodulationeventoutputterminal__string.html language=enus -->
## TOPIC 00124: operator RfsgExportedPulseModulationEventOutputTerminal(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal-operator-rfsgexportedpulsemodulationeventoutputterminal__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal-operator-rfsgexportedpulsemodulationeventoutputterminal__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Convert the specified string to equivalent RfsgExportedPulseModulationEventOutputTerminal object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator RfsgExportedPulseModulationEventOutputTerminal(string outputTerminal)ParametersNameTypeDescriptionoutputTerm

### operator RfsgExportedPulseModulationEventOutputTerminal(string)

Convert the specified string to equivalent [RfsgExportedPulseModulationEventOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator RfsgExportedPulseModulationEventOutputTerminal(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies the string to be converted to equivalent RfsgExportedPulseModulationEventOutputTerminal object. |

#### Returns

Returns an object of type [RfsgExportedPulseModulationEventOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal.html) from the string passed in the *outputTerminal*.

Parent topic:

RfsgExportedPulseModulationEventOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal-operator_neq__rfsgexportedpulsemodulationeventoutputterminal-rfsgexportedpulsemodulationeventoutputterminal.html language=enus -->
## TOPIC 00125: operator!=(RfsgExportedPulseModulationEventOutputTerminal, RfsgExportedPulseModulationEventOutputTerminal)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal-operator_neq__rfsgexportedpulsemodulationeventoutputterminal-rfsgexportedpulsemodulationeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal-operator_neq__rfsgexportedpulsemodulationeventoutputterminal-rfsgexportedpulsemodulationeventoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgExportedPulseModulationEventOutputTerminal are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgExportedPulseModulationEventOutputTerminal outputTerminal1, RfsgExportedPulseModulationEventOutputTerminal o

### operator!=(RfsgExportedPulseModulationEventOutputTerminal, RfsgExportedPulseModulationEventOutputTerminal)

Checks whether the two instances of [RfsgExportedPulseModulationEventOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgExportedPulseModulationEventOutputTerminal outputTerminal1, RfsgExportedPulseModulationEventOutputTerminal outputTerminal2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal1 | RfsgExportedPulseModulationEventOutputTerminal | Specifies an RfsgExportedPulseModulationEventOutputTerminal object. |
| outputTerminal2 | RfsgExportedPulseModulationEventOutputTerminal | Specifies an RfsgExportedPulseModulationEventOutputTerminal object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsgExportedPulseModulationEventOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal.html language=enus -->
## TOPIC 00126: RfsgExportedPulseModulationEventOutputTerminal Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the output terminal for pulse modulation. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgExportedPulseModulationEventOutputTerminalRemarksSee ExportedPulseModulationEventOutputTerminal. PropertiesNameDescriptionDisableGets the output termina

### RfsgExportedPulseModulationEventOutputTerminal Class

Represents the output terminal for pulse modulation.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgExportedPulseModulationEventOutputTerminal

#### Remarks

See [ExportedPulseModulationEventOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-exportedpulsemodulationeventoutputterminal.html).

#### Properties

| Name | Description |
| --- | --- |
| Disable | Gets the output terminal when pulse modulation is disabled. |
| PulseOut | Gets the output terminal when it is pulseOut. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsgExportedPulseModulationEventOutputTerminal object from the specified string. |
| Equals(RfsgExportedPulseModulationEventOutputTerminal) | Determines whether the current instance of RfsgExportedPulseModulationEventOutputTerminal and the RfsgExportedPulseModulationEventOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgExportedPulseModulationEventOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgExportedPulseModulationEventOutputTerminal. |
| ToString() | Converts the current instance of RfsgExportedPulseModulationEventOutputTerminal to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgExportedPulseModulationEventOutputTerminal(string) | Convert the specified string to equivalent RfsgExportedPulseModulationEventOutputTerminal object. |
| operator string(RfsgExportedPulseModulationEventOutputTerminal) | Converts the RfsgExportedPulseModulationEventOutputTerminal object to equivalent string. |
| operator!=(RfsgExportedPulseModulationEventOutputTerminal, RfsgExportedPulseModulationEventOutputTerminal) | Checks whether the two instances of RfsgExportedPulseModulationEventOutputTerminal are unequal. |
| operator==(RfsgExportedPulseModulationEventOutputTerminal, RfsgExportedPulseModulationEventOutputTerminal) | Checks whether the two instances of RfsgExportedPulseModulationEventOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreference-rate.html language=enus -->
## TOPIC 00127: Rate

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreference-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreference-rate.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frequency of the Reference clock, in hertz (Hz). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double Rate { get; set; }RemarksSpecifies a Double representing the frequency of the Reference clock. To set this property, the NI-RFSG device must be in the Configu

### Rate

Gets or sets the frequency of the Reference clock, in hertz (Hz).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double Rate { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the frequency of the Reference clock.

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Rate property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgFrequencyReference Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreference.html language=enus -->
## TOPIC 00128: RfsgFrequencyReference Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreference.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreference.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the methods and properties used to configure the Frequency Reference clock and the PxiChassisClock10. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgFrequencyReference : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG I

### RfsgFrequencyReference Class

Provides the methods and properties used to configure the Frequency Reference clock and the PxiChassisClock10.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgFrequencyReference : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| ExportedOutputTerminal | Gets or sets the destination terminal to export the Frequency Reference clock on the RF signal generators. |
| ExportedRate | Gets or sets the frequency of the Reference clock export, in hertz (Hz). |
| PxiChassisClock10Source | Gets or sets the clock source to drive the PXI 10 MHz backplane Frequency Reference clock. |
| Rate | Gets or sets the frequency of the Reference clock, in hertz (Hz). |
| Source | Gets or sets the Frequency Reference clock source. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(RfsgFrequencyReferenceSource, double) | Configures the NI-RFSG Frequency Reference clock source and rate. The Frequency Reference clock ensures that the NI-RFSG operates from a common timebase. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal-fromstring__string.html language=enus -->
## TOPIC 00129: FromString(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal-fromstring__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsgFrequencyReferenceExportedOutputTerminal object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgFrequencyReferenceExportedOutputTerminal FromString(string outputTerminal)ParametersNameTypeDescriptionoutputTerminalstringSpecifi

### FromString(string)

Creates an [RfsgFrequencyReferenceExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgFrequencyReferenceExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal.html) FromString(string outputTerminal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| outputTerminal | string | Specifies a string that is the output terminal of RfsgFrequencyReference. |

#### Returns

Returns an object of type [RfsgFrequencyReferenceExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal.html).

Parent topic:

RfsgFrequencyReferenceExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal-referenceout.html language=enus -->
## TOPIC 00130: ReferenceOut

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal-referenceout.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal-referenceout.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the REF IN/OUT terminal on the LO. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgFrequencyReferenceExportedOutputTerminal ReferenceOut { get; }RemarksReturns an object of type RfsgFrequencyReferenceExporte

### ReferenceOut

Gets the destination terminal when the signal is exported to the REF IN/OUT terminal on the LO.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgFrequencyReferenceExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal.html) ReferenceOut { get; }

#### Remarks

Returns an object of type [RfsgFrequencyReferenceExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferenceexportedoutputterminal.html) representing the string "RefOut".

Parent topic:

RfsgFrequencyReferenceExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-clockin.html language=enus -->
## TOPIC 00131: ClockIn

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-clockin.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-clockin.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source when the clock signal present at the front panel CLK IN connector is used as the source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgFrequencyReferenceSource ClockIn { get; }RemarksReturns an object of type RfsgFrequencyReferenceSource representing

### ClockIn

Gets the source when the clock signal present at the front panel CLK IN connector is used as the source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html) ClockIn { get; }

#### Remarks

Returns an object of type [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html) representing the string "ClkIn".

Parent topic:

RfsgFrequencyReferenceSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-gethashcode.html language=enus -->
## TOPIC 00132: GetHashCode()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-gethashcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsgFrequencyReferenceSource. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsgFrequencyReferenceSource.

### GetHashCode()

Returns the hash code for the current instance of [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html).

Parent topic:

RfsgFrequencyReferenceSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-onboardclock.html language=enus -->
## TOPIC 00133: OnboardClock

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-onboardclock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-onboardclock.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source when arbitrary waveform generator (AWG) module onboard clock is used as the clock source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgFrequencyReferenceSource OnboardClock { get; }RemarksReturns an object of type RfsgFrequencyReferenceSource repres

### OnboardClock

Gets the source when arbitrary waveform generator (AWG) module onboard clock is used as the clock source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html) OnboardClock { get; }

#### Remarks

Returns an object of type [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html) representing the string "OnboardClock".

Parent topic:

RfsgFrequencyReferenceSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-operator-rfsgfrequencyreferencesource__string.html language=enus -->
## TOPIC 00134: operator RfsgFrequencyReferenceSource(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-operator-rfsgfrequencyreferencesource__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-operator-rfsgfrequencyreferencesource__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string to equivalent RfsgFrequencyReferenceSource object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator RfsgFrequencyReferenceSource(string source)ParametersNameTypeDescriptionsourcestringSpecifies the string to be converted to e

### operator RfsgFrequencyReferenceSource(string)

Converts the specified string to equivalent [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator RfsgFrequencyReferenceSource(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies the string to be converted to equivalent RfsgFrequencyReferenceSource object. |

#### Returns

Returns an object of type [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html) from the string passed in the *source*.

Parent topic:

RfsgFrequencyReferenceSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-operator_eq__rfsgfrequencyreferencesource-rfsgfrequencyreferencesource.html language=enus -->
## TOPIC 00135: operator==(RfsgFrequencyReferenceSource, RfsgFrequencyReferenceSource)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-operator_eq__rfsgfrequencyreferencesource-rfsgfrequencyreferencesource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource-operator_eq__rfsgfrequencyreferencesource-rfsgfrequencyreferencesource.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgFrequencyReferenceSource are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgFrequencyReferenceSource source1, RfsgFrequencyReferenceSource source2)ParametersNameTypeDescriptionsource1RfsgFrequencyReferenc

### operator==(RfsgFrequencyReferenceSource, RfsgFrequencyReferenceSource)

Checks whether the two instances of [RfsgFrequencyReferenceSource](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreferencesource.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgFrequencyReferenceSource source1, RfsgFrequencyReferenceSource source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsgFrequencyReferenceSource | Specifies the first instance to be compared. |
| source2 | RfsgFrequencyReferenceSource | Specifies the second instance to be compared. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgFrequencyReferenceSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-enabled.html language=enus -->
## TOPIC 00136: Enabled

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-enabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-enabled.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the I/Q impairment is enabled. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool Enabled { get; set; }Remarkstrue if I/Q impairment is enabled; otherwise false. IOffset, QOffset, GainImbalance, and Skew are ignored when this property is set to false. Exce

### Enabled

Gets or sets whether the I/Q impairment is enabled.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool Enabled { get; set; }

#### Remarks

true if I/Q impairment is enabled; otherwise false.

[IOffset](nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-ioffset.html), [QOffset](nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-qoffset.html), [GainImbalance](nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-gainimbalance.html), and [Skew](nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-skew.html) are ignored when this property is set to false.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Enabled property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgIQImpairment Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-gainimbalance.html language=enus -->
## TOPIC 00137: GainImbalance

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-gainimbalance.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgiqimpairment-gainimbalance.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the gain imbalance of the I/Q modulator (I versus Q), in dB. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double GainImbalance { get; set; }RemarksSpecifies a Double representing the gain imbalance of the I/Q modulator (I versus Q), in dB. ExceptionsTypeDescripti

### GainImbalance

Gets or sets the gain imbalance of the I/Q modulator (I versus Q), in dB.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double GainImbalance { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the gain imbalance of the I/Q modulator (I versus Q), in dB.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GainImbalance property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgIQImpairment Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgiqoutport-carrierfrequency.html language=enus -->
## TOPIC 00138: CarrierFrequency

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgiqoutport-carrierfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgiqoutport-carrierfrequency.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frequency of the I/Q OUT Port signal. The onboard signal processing (OSP) applies the specified frequency shift to the I/Q data before the data is sent to the digital-to-analog converter (DAC). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double CarrierFreque

### CarrierFrequency

Gets or sets the frequency of the I/Q OUT Port signal. The onboard signal processing (OSP) applies the specified frequency shift to the I/Q data before the data is sent to the digital-to-analog converter (DAC).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double CarrierFrequency { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the frequency shift, in hertz (Hz), to apply to the I/Q data.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CarrierFrequency property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgIQOutPort Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsglinearinterpolationformat.html language=enus -->
## TOPIC 00139: RfsgLinearInterpolationFormat Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsglinearinterpolationformat.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsglinearinterpolationformat.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the format of parameters to interpolate. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgLinearInterpolationFormatMembersNameValueDescriptionRealAndImaginary(int)26000Results in a linear interpolation of the real portion of the complex number and a separate li

### RfsgLinearInterpolationFormat Enumeration

Specifies the format of parameters to interpolate.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgLinearInterpolationFormat

#### Members

| Name | Value | Description |
| --- | --- | --- |
| RealAndImaginary | (int)26000 | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |
| MagnitudeAndPhase | (int)26001 | Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase. |
| MagnitudeInDecibelAndPhase | (int)26002 | Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgloadconfigurationsfromfileloadoptions.html language=enus -->
## TOPIC 00140: RfsgLoadConfigurationsFromFileLoadOptions Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgloadconfigurationsfromfileloadoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgloadconfigurationsfromfileloadoptions.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configurations to skip to reset while loading configurations from a file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgLoadConfigurationsFromFileLoadOptionsMembersNameValueDescriptionSkipNone(int)0x0NI-RFSG loads all the configurations to the session. S

### RfsgLoadConfigurationsFromFileLoadOptions Enumeration

Specifies the configurations to skip to reset while loading configurations from a file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgLoadConfigurationsFromFileLoadOptions

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SkipNone | (int)0x0 | NI-RFSG loads all the configurations to the session. |
| SkipWaveforms | (int)0x1 | NI-RFSG skips loading the waveform configurations to the session. |
| SkipScripts | (int)0x2 | NI-RFSG skips loading the scripts to the session. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgloadconfigurationsfromfileresetoptions.html language=enus -->
## TOPIC 00141: RfsgLoadConfigurationsFromFileResetOptions Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgloadconfigurationsfromfileresetoptions.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgloadconfigurationsfromfileresetoptions.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configurations to skip while loading from a file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgLoadConfigurationsFromFileResetOptionsMembersNameValueDescriptionSkipNone(int)0x0NI-RFSG resets all configurations. SkipWaveforms(int)0x1NI-RFSG skips resetti

### RfsgLoadConfigurationsFromFileResetOptions Enumeration

Specifies the configurations to skip while loading from a file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgLoadConfigurationsFromFileResetOptions

#### Members

| Name | Value | Description |
| --- | --- | --- |
| SkipNone | (int)0x0 | NI-RFSG resets all configurations. |
| SkipWaveforms | (int)0x1 | NI-RFSG skips resetting the waveform configurations. |
| SkipScripts | (int)0x2 | NI-RFSG skips resetting the scripts. |
| SkipDeembeddingTables | (int)0x8 | NI-RFSG skips resetting the de-embeding tables. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-automaticsgsashared.html language=enus -->
## TOPIC 00142: AutomaticSGSAShared

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-automaticsgsashared.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-automaticsgsashared.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG.This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgLocalOscillatorSource AutomaticSGSAShared { get; }RemarksReturns

### AutomaticSGSAShared

NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG.This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html) AutomaticSGSAShared { get; }

#### Remarks

Returns an object of type [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html).

Parent topic:

RfsgLocalOscillatorSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-equals__object.html language=enus -->
## TOPIC 00143: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgLocalOscillatorSource and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to compared to the current i

### Equals(object)

Determines whether the current instance of [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to compared to the current instance of RfsgLocalOscillatorSource. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgLocalOscillatorSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-equals__rfsglocaloscillatorsource.html language=enus -->
## TOPIC 00144: Equals(RfsgLocalOscillatorSource)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-equals__rfsglocaloscillatorsource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-equals__rfsglocaloscillatorsource.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgLocalOscillatorSource and the RfsgLocalOscillatorSource object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool Equals(RfsgLocalOscillatorSource source)ParametersNameTypeDescriptionsourceRfsgLocalOsci

### Equals(RfsgLocalOscillatorSource)

Determines whether the current instance of [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html) and the [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool Equals(RfsgLocalOscillatorSource source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsgLocalOscillatorSource | Specifies the RfsgLocalOscillatorSource object to be compared to the current instance of RfsgLocalOscillatorSource. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgLocalOscillatorSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-fromstring__string.html language=enus -->
## TOPIC 00145: FromString(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource-fromstring__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsgLocalOscillatorSource object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgLocalOscillatorSource FromString(string source)ParametersNameTypeDescriptionsourcestringSpecifies a string representing the source of RfsgRFLocalOsci

### FromString(string)

Creates an [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html) FromString(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies a string representing the source of RfsgRFLocalOscillator. |

#### Returns

Returns an object of type [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html).

Parent topic:

RfsgLocalOscillatorSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsglopllfractionalmodeenabled.html language=enus -->
## TOPIC 00146: RfsgLOPllFractionalModeEnabled Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsglopllfractionalmodeenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsglopllfractionalmodeenabled.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgLOPllFractionalModeEnabledMembersNameValueDescriptionEnable(int)1Enables fractional mode for the LO PLL. Disable(int)0Disables

### RfsgLOPllFractionalModeEnabled Enumeration

Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgLOPllFractionalModeEnabled

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Enable | (int)1 | Enables fractional mode for the LO PLL. |
| Disable | (int)0 | Disables fractional mode for the LO PLL. |

#### See Also

- PllFractionalModeEnabled

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgmarkerevent-toggleinitialstate.html language=enus -->
## TOPIC 00147: ToggleInitialState

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgmarkerevent-toggleinitialstate.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgmarkerevent-toggleinitialstate.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial state for the Marker Event when you set the OutputBehavior property to Toggle. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgMarkerEventToggleInitialState ToggleInitialState { get; set; }RemarksSpecifies the RfsgMarkerEventToggleInitialState enumer

### ToggleInitialState

Gets or sets the initial state for the Marker Event when you set the [OutputBehavior](nationalinstruments-modularinstruments-nirfsg-rfsgmarkerevent-outputbehavior.html) property to [Toggle](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgMarkerEventToggleInitialState](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventtoggleinitialstate.html) ToggleInitialState { get; set; }

#### Remarks

Specifies the [RfsgMarkerEventToggleInitialState](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventtoggleinitialstate.html) enumeration.

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ToggleInitialState property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgMarkerEvent Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgmarkerevent.html language=enus -->
## TOPIC 00148: RfsgMarkerEvent Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgmarkerevent.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgmarkerevent.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the channel-based properties related to Marker events. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgMarkerEvent : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF

### RfsgMarkerEvent Class

Represents the channel-based properties related to Marker events.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgMarkerEvent : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| ExportedOutputTerminal | Gets or sets the destination terminal for exporting the Marker event. |
| OutputBehavior | Gets or sets the output behavior for the Marker Event. |
| OutputBehaviour | Gets or sets the output behaviour for the Marker Event. |
| PulseWidth | Gets or sets the pulse width value for the Marker Event. |
| PulseWidthUnits | Gets or sets the pulse width units for the Marker Event. |
| TerminalName | Gets the name of the fully-qualified signal name as a string. |
| ToggleInitialState | Gets or sets the initial state for the Marker Event when you set the OutputBehavior property to Toggle. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventcollection.html language=enus -->
## TOPIC 00149: RfsgMarkerEventCollection Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventcollection.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventcollection.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a collection of Marker events. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgMarkerEventCollection : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF Signal Genera

### RfsgMarkerEventCollection Class

Represents a collection of Marker events.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgMarkerEventCollection : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| this[int index] | Gets the Marker event at the particular index. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi0.html language=enus -->
## TOPIC 00150: Pfi0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 0 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgMarkerEventExportedOutputTerminal Pfi0 { get; }RemarksReturns an object of type RfsgMarkerEventExportedOutputTerminal representing the str

### Pfi0

Gets the destination terminal when the signal is exported to the PFI 0 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgMarkerEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal.html) Pfi0 { get; }

#### Remarks

Returns an object of type [RfsgMarkerEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal.html) representing the string "PFI0".

Parent topic:

RfsgMarkerEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi1.html language=enus -->
## TOPIC 00151: Pfi1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 1 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgMarkerEventExportedOutputTerminal Pfi1 { get; }RemarksReturns an object of type RfsgMarkerEventExportedOutputTerminal representing the str

### Pfi1

Gets the destination terminal when the signal is exported to the PFI 1 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgMarkerEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal.html) Pfi1 { get; }

#### Remarks

Returns an object of type [RfsgMarkerEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal.html) representing the string "PFI1".

Parent topic:

RfsgMarkerEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi5.html language=enus -->
## TOPIC 00152: Pfi5

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi5.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pfi5.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PFI 5 connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgMarkerEventExportedOutputTerminal Pfi5 { get; }RemarksReturns an object of type RfsgMarkerEventExportedOutputTerminal representing the str

### Pfi5

Gets the destination terminal when the signal is exported to the PFI 5 connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgMarkerEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal.html) Pfi5 { get; }

#### Remarks

Returns an object of type [RfsgMarkerEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal.html) representing the string "PFI5".

Parent topic:

RfsgMarkerEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00153: PxiTriggerLine0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal-pxitriggerline0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal when the signal is exported to the PXI trigger line 0. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgMarkerEventExportedOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type RfsgMarkerEventExportedOutputTerminal repres

### PxiTriggerLine0

Gets the destination terminal when the signal is exported to the PXI trigger line 0.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgMarkerEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [RfsgMarkerEventExportedOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgmarkereventexportedoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

RfsgMarkerEventExportedOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgmodule.html language=enus -->
## TOPIC 00154: RfsgModule Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgmodule.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgmodule.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the module in the NI-RFSG device. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgModuleMembersNameValueDescriptionPrimaryModule13000The stand-alone device, or the main module in a multi-module device. Awg13001The AWG associated with the primary module. LO1300

### RfsgModule Enumeration

Specifies the module in the NI-RFSG device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgModule

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PrimaryModule | 13000 | The stand-alone device, or the main module in a multi-module device. |
| Awg | 13001 | The AWG associated with the primary module. |
| LO | 13002 | The LO associated with the primary module. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-dio2.html language=enus -->
## TOPIC 00155: Dio2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-dio2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-dio2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgOutputTerminal Dio2 { get; }RemarksReturns an object of type RfsgOutputTerminal representing the string "DIO/PFI2".

### Dio2

Gets the source terminal when the trigger is received on the DIO PFI2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) Dio2 { get; }

#### Remarks

Returns an object of type [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) representing the string "DIO/PFI2".

Parent topic:

RfsgOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-dio6.html language=enus -->
## TOPIC 00156: Dio6

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-dio6.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-dio6.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source terminal when the trigger is received on the DIO PFI6. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgOutputTerminal Dio6 { get; }RemarksReturns an object of type RfsgOutputTerminal representing the string "DIO/PFI6".

### Dio6

Gets the source terminal when the trigger is received on the DIO PFI6.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) Dio6 { get; }

#### Remarks

Returns an object of type [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) representing the string "DIO/PFI6".

Parent topic:

RfsgOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-pxitriggerline0.html language=enus -->
## TOPIC 00157: PxiTriggerLine0

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-pxitriggerline0.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-pxitriggerline0.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a signal to the PXI trigger line 0 terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgOutputTerminal PxiTriggerLine0 { get; }RemarksReturns an object of type RfsgOutputTerminal representing the string "PXI_Trig0".

### PxiTriggerLine0

Exports a signal to the PXI trigger line 0 terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) PxiTriggerLine0 { get; }

#### Remarks

Returns an object of type [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) representing the string "PXI_Trig0".

Parent topic:

RfsgOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-pxitriggerline1.html language=enus -->
## TOPIC 00158: PxiTriggerLine1

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-pxitriggerline1.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-pxitriggerline1.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a signal to the PXI trigger line 1 terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgOutputTerminal PxiTriggerLine1 { get; }RemarksReturns an object of type RfsgOutputTerminal representing the string "PXI_Trig1".

### PxiTriggerLine1

Exports a signal to the PXI trigger line 1 terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) PxiTriggerLine1 { get; }

#### Remarks

Returns an object of type [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) representing the string "PXI_Trig1".

Parent topic:

RfsgOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-triggeroutputterminal.html language=enus -->
## TOPIC 00159: TriggerOutputTerminal

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-triggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal-triggeroutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a signal to the TRIG IN/OUT terminal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgOutputTerminal TriggerOutputTerminal { get; }RemarksReturns an object of type RfsgOutputTerminal representing the string "TrigOut".

### TriggerOutputTerminal

Exports a signal to the TRIG IN/OUT terminal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) TriggerOutputTerminal { get; }

#### Remarks

Returns an object of type [RfsgOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html) representing the string "TrigOut".

Parent topic:

RfsgOutputTerminal Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html language=enus -->
## TOPIC 00160: RfsgOutputTerminal Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal where the signal is exported. You can choose not to export any signal. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgOutputTerminalPropertiesNameDescriptionClockOutExports a signal to the CLK OUT connector. Dio1Gets the source t

### RfsgOutputTerminal Class

Specifies the terminal where the signal is exported. You can choose not to export any signal.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgOutputTerminal

#### Properties

| Name | Description |
| --- | --- |
| ClockOut | Exports a signal to the CLK OUT connector. |
| Dio1 | Gets the source terminal when the trigger is received on the DIO PFI1. |
| Dio2 | Gets the source terminal when the trigger is received on the DIO PFI2. |
| Dio3 | Gets the source terminal when the trigger is received on the DIO PFI3. |
| Dio4 | Gets the source terminal when the trigger is received on the DIO PFI4. |
| Dio5 | Gets the source terminal when the trigger is received on the DIO PFI5. |
| Dio6 | Gets the source terminal when the trigger is received on the DIO PFI6. |
| Dio7 | Gets the source terminal when the trigger is received on the DIO PFI7. |
| DioO | Gets the source terminal when the trigger is received on the DIO PFI0. |
| DoNotExport | Does not export a signal. |
| PFI0 | Exports a signal to the PFI 0 terminal. |
| PFI1 | Exports a signal to the PFI 1 terminal. |
| PFI4 | Exports a signal to the PFI 4 terminal. |
| PFI5 | Exports a signal to the PFI 5 terminal. |
| PXIeDStarC | Exports a signal to the PXIe DStar C trigger line terminal. This value is valid on only the PXIe-5820/5830/5831/5832/5840. |
| PxiStarLine | Exports a signal to the PXI star trigger line terminal. This value is not valid for the PXIe-5644/5645/5646. |
| PxiTriggerLine0 | Exports a signal to the PXI trigger line 0 terminal. |
| PxiTriggerLine1 | Exports a signal to the PXI trigger line 1 terminal. |
| PxiTriggerLine2 | Exports a signal to the PXI trigger line 2 terminal. |
| PxiTriggerLine3 | Exports a signal to the PXI trigger line 3 terminal. |
| PxiTriggerLine4 | Exports a signal to the PXI trigger line 4 terminal. |
| PxiTriggerLine5 | Exports a signal to the PXI trigger line 5 terminal. |
| PxiTriggerLine6 | Exports a signal to the PXI trigger line 6 terminal. |
| ReferenceOut | Exports a signal to the REF OUT connector. |
| ReferenceOut2 | Exports a signal to the REF OUT2 connector, if applicable. |
| TriggerOutputTerminal | Exports a signal to the TRIG IN/OUT terminal. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsgOutputTerminal object from the specified string. |
| Equals(RfsgOutputTerminal) | Determines whether the current instance of RfsgOutputTerminal and the RfsgOutputTerminal object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgOutputTerminal and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgOutputTerminal. |
| ToString() | Converts the current instance of RfsgStartedEventExportedOutputTerminal to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgOutputTerminal(string) | Converts the specified string to equivalent RfsgOutputTerminal object. |
| operator string(RfsgOutputTerminal) | Converts the RfsgOutputTerminal object equivalent string. |
| operator!=(RfsgOutputTerminal, RfsgOutputTerminal) | Checks whether the two instances of RfsgOutputTerminal are unequal. |
| operator==(RfsgOutputTerminal, RfsgOutputTerminal) | Checks whether the two instances of RfsgOutputTerminal are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgoverflowerrorreporting.html language=enus -->
## TOPIC 00161: RfsgOverflowErrorReporting Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgoverflowerrorreporting.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgoverflowerrorreporting.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether NI-RFSG returns a warning when an OSP overflow occurs. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgOverflowErrorReportingMembersNameValueDescriptionWarning1301NI-RFSG returns a warning when an OSP overflow occurs. Disabled1302NI-RFSG does not retur

### RfsgOverflowErrorReporting Enumeration

Specifies whether NI-RFSG returns a warning when an OSP overflow occurs.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgOverflowErrorReporting

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Warning | 1301 | NI-RFSG returns a warning when an OSP overflow occurs. |
| Disabled | 1302 | NI-RFSG does not return an error or a warning when an OSP overflow occurs. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource-operator-rfsgpulsemodulationsource__string.html language=enus -->
## TOPIC 00162: operator RfsgPulseModulationSource(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource-operator-rfsgpulsemodulationsource__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource-operator-rfsgpulsemodulationsource__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Convert the specified string to equivalent RfsgPulseModulationSource object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator RfsgPulseModulationSource(string source)ParametersNameTypeDescriptionsourcestringSpecifies the string to be converted to equivale

### operator RfsgPulseModulationSource(string)

Convert the specified string to equivalent [RfsgPulseModulationSource](nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator RfsgPulseModulationSource(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies the string to be converted to equivalent RfsgPulseModulationSource object. |

#### Returns

Returns an object of type [RfsgPulseModulationSource](nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource.html) from the string passed in the *source*.

Parent topic:

RfsgPulseModulationSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource-tostring.html language=enus -->
## TOPIC 00163: ToString()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource-tostring.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsgPulseModulationSource to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override string ToString()ReturnsReturns a string that represents the current instance of RfsgPulseModulationSource.

### ToString()

Converts the current instance of [RfsgPulseModulationSource](nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsgPulseModulationSource](nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource.html).

Parent topic:

RfsgPulseModulationSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource.html language=enus -->
## TOPIC 00164: RfsgPulseModulationSource Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the source terminal that pulse modulation triggers off of. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgPulseModulationSourceRemarksSee PulseModulationSource. PropertiesNameDescriptionDisableGets the source when pulse modulation is disable

### RfsgPulseModulationSource Class

Represents the source terminal that pulse modulation triggers off of.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgPulseModulationSource

#### Remarks

See [PulseModulationSource](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationsource.html).

#### Properties

| Name | Description |
| --- | --- |
| Disable | Gets the source when pulse modulation is disabled. |
| Marker0 | Gets the source when pulse modulation is tied to marker0. |
| Marker1 | Gets the source when pulse modulation is tied to marker1. |
| Marker2 | Gets the source when pulse modulation is tied to marker2. |
| Marker3 | Gets the source when pulse modulation is tied to marker3. |
| PulseIn | Gets the source when pulse modulation is tied to PulseIn. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsgPulseModulationSource object from the specified string. |
| Equals(RfsgPulseModulationSource) | Determines whether the current instance of RfsgPulseModulationSource and the RfsgPulseModulationSource object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgPulseModulationSource and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgPulseModulationSource. |
| ToString() | Converts the current instance of RfsgPulseModulationSource to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgPulseModulationSource(string) | Convert the specified string to equivalent RfsgPulseModulationSource object. |
| operator string(RfsgPulseModulationSource) | Converts the RfsgPulseModulationSource object to equivalent string. |
| operator!=(RfsgPulseModulationSource, RfsgPulseModulationSource) | Checks whether the two instances of RfsgPulseModulationSource are unequal. |
| operator==(RfsgPulseModulationSource, RfsgPulseModulationSource) | Checks whether the two instances of RfsgPulseModulationSource are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpulseshaping.html language=enus -->
## TOPIC 00165: RfsgPulseShaping Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpulseshaping.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpulseshaping.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the properties used to configure the arbitrary waveform generator (AWG) filter. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgPulseShaping : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming

### RfsgPulseShaping Class

Provides the properties used to configure the arbitrary waveform generator (AWG) filter.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgPulseShaping : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| Filter | Gets or sets pulse-shaping filter type for the arb filter. |
| RaisedCosineAlpha | Gets or sets the alpha value to use in the calculation of the pulse-shaping FIR filter coefficients. You can use this property only when Filter is set to RaisedCosine. |
| RootRaisedCosineAlpha | Gets or sets the alpha value to use in the calculation of the pulse-shaping FIR filter coefficients. You can use this property only when Filter is set to RootRaisedCosine. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-equals__object.html language=enus -->
## TOPIC 00166: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgPxiChassisClock10Source and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to the curr

### Equals(object)

Determines whether the current instance of [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsgPxiChassisClock10Source. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-equals__rfsgpxichassisclock10source.html language=enus -->
## TOPIC 00167: Equals(RfsgPxiChassisClock10Source)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-equals__rfsgpxichassisclock10source.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-equals__rfsgpxichassisclock10source.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgPxiChassisClock10Source object and the RfsgPxiChassisClock10Source object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool Equals(RfsgPxiChassisClock10Source source)ParametersNameTypeDescriptionsource

### Equals(RfsgPxiChassisClock10Source)

Determines whether the current instance of [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) object and the [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool Equals(RfsgPxiChassisClock10Source source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsgPxiChassisClock10Source | Specifies the RfsgPxiChassisClock10Source object to be compared to the current instance of RfsgPxiChassisClock10Source. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-fromstring__string.html language=enus -->
## TOPIC 00168: FromString(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-fromstring__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RfsgPxiChassisClock10Source object from the specified string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgPxiChassisClock10Source FromString(string source)ParametersNameTypeDescriptionsourcestringSpecifies a string representing the output terminal for R

### FromString(string)

Creates an [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) object from the specified string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) FromString(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies a string representing the output terminal for RfsgPxiChassisClock10Source. |

#### Returns

Returns an object of type [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html).

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-gethashcode.html language=enus -->
## TOPIC 00169: GetHashCode()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-gethashcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsgPxiChassisClock10Source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsgPxiChassisClock10Source.

### GetHashCode()

Returns the hash code for the current instance of [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html).

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-none.html language=enus -->
## TOPIC 00170: None

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-none.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-none.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the clock source when the signal is not exported. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgPxiChassisClock10Source None { get; }RemarksReturns an object of type RfsgPxiChassisClock10Source representing the string "None".

### None

Gets the clock source when the signal is not exported.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) None { get; }

#### Remarks

Returns an object of type [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) representing the string "None".

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-onboardclock.html language=enus -->
## TOPIC 00171: OnboardClock

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-onboardclock.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-onboardclock.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the clock source when the highly stable oven-controlled onboard frequency reference is used to drive the PXI_CLK signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgPxiChassisClock10Source OnboardClock { get; }RemarksReturns an object of type RfsgPxiChassisCl

### OnboardClock

Gets the clock source when the highly stable oven-controlled onboard frequency reference is used to drive the PXI_CLK signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) OnboardClock { get; }

#### Remarks

Returns an object of type [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) representing the string "OnboardClock".

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator-rfsgpxichassisclock10source__string.html language=enus -->
## TOPIC 00172: operator RfsgPxiChassisClock10Source(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator-rfsgpxichassisclock10source__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator-rfsgpxichassisclock10source__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the specified string representation of a PXI chassis clock 10 source to its RfsgPxiChassisClock10Source equivalent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator RfsgPxiChassisClock10Source(string source)ParametersNameTypeDescriptionsourcestri

### operator RfsgPxiChassisClock10Source(string)

Converts the specified string representation of a PXI chassis clock 10 source to its [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) equivalent.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator RfsgPxiChassisClock10Source(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies the string to be converted to equivalent RfsgPxiChassisClock10Source object. |

#### Returns

Returns an object of type [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html).

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator-string__rfsgpxichassisclock10source.html language=enus -->
## TOPIC 00173: operator string(RfsgPxiChassisClock10Source)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator-string__rfsgpxichassisclock10source.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator-string__rfsgpxichassisclock10source.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the RfsgPxiChassisClock10Source object to its equivalent string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator string(RfsgPxiChassisClock10Source source)ParametersNameTypeDescriptionsourceRfsgPxiChassisClock10SourceSpecifies the RfsgPxiChassis

### operator string(RfsgPxiChassisClock10Source)

Converts the [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) object to its equivalent string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator string(RfsgPxiChassisClock10Source source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | RfsgPxiChassisClock10Source | Specifies the RfsgPxiChassisClock10Source object to be converted to string. |

#### Returns

Returns a string from the [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) object.

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator_eq__rfsgpxichassisclock10source-rfsgpxichassisclock10source.html language=enus -->
## TOPIC 00174: operator==(RfsgPxiChassisClock10Source, RfsgPxiChassisClock10Source)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator_eq__rfsgpxichassisclock10source-rfsgpxichassisclock10source.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator_eq__rfsgpxichassisclock10source-rfsgpxichassisclock10source.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the two instances of RfsgPxiChassisClock10Source are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgPxiChassisClock10Source source1, RfsgPxiChassisClock10Source source2)ParametersNameTypeDescriptionsource1RfsgPxiChassisClock1

### operator==(RfsgPxiChassisClock10Source, RfsgPxiChassisClock10Source)

Determines whether the two instances of [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgPxiChassisClock10Source source1, RfsgPxiChassisClock10Source source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsgPxiChassisClock10Source | Specifies an RfsgPxiChassisClock10Source object. |
| source2 | RfsgPxiChassisClock10Source | Specifies an RfsgPxiChassisClock10Source object. |

#### Returns

true if the two instances represent the same result; otherwise, false.

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator_neq__rfsgpxichassisclock10source-rfsgpxichassisclock10source.html language=enus -->
## TOPIC 00175: operator!=(RfsgPxiChassisClock10Source, RfsgPxiChassisClock10Source)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator_neq__rfsgpxichassisclock10source-rfsgpxichassisclock10source.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-operator_neq__rfsgpxichassisclock10source-rfsgpxichassisclock10source.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgPxiChassisClock10Source are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgPxiChassisClock10Source source1, RfsgPxiChassisClock10Source source2)ParametersNameTypeDescriptionsource1RfsgPxiChassisClock10S

### operator!=(RfsgPxiChassisClock10Source, RfsgPxiChassisClock10Source)

Checks whether the two instances of [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgPxiChassisClock10Source source1, RfsgPxiChassisClock10Source source2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source1 | RfsgPxiChassisClock10Source | Specifies an RfsgPxiChassisClock10Source object. |
| source2 | RfsgPxiChassisClock10Source | Specifies an RfsgPxiChassisClock10Source object. |

#### Returns

true if the two instances do not represent the same result; otherwise, false.

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-referencein.html language=enus -->
## TOPIC 00176: ReferenceIn

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-referencein.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-referencein.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the clock source when the clock present at the front panel REF IN connector is used to drive the PXI_CLK signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgPxiChassisClock10Source ReferenceIn { get; }RemarksReturns an object of type RfsgPxiChassisClock10Sour

### ReferenceIn

Gets the clock source when the clock present at the front panel REF IN connector is used to drive the PXI_CLK signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) ReferenceIn { get; }

#### Remarks

Returns an object of type [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) representing the string "RefIn".

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-tostring.html language=enus -->
## TOPIC 00177: ToString()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source-tostring.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the current instance of RfsgPxiChassisClock10Source to string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override string ToString()ReturnsReturns a string that represents the current instance of RfsgPxiChassisClock10Source.

### ToString()

Converts the current instance of [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html) to string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override string ToString()

#### Returns

Returns a string that represents the current instance of [RfsgPxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html).

Parent topic:

RfsgPxiChassisClock10Source Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html language=enus -->
## TOPIC 00178: RfsgPxiChassisClock10Source Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgpxichassisclock10source.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the source for the PXI chassis clock. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgPxiChassisClock10SourceRemarksSee PxiChassisClock10Source. PropertiesNameDescriptionNoneGets the clock source when the signal is not exported. OnboardClockG

### RfsgPxiChassisClock10Source Class

Represents the source for the PXI chassis clock.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgPxiChassisClock10Source

#### Remarks

See [PxiChassisClock10Source](nationalinstruments-modularinstruments-nirfsg-rfsgfrequencyreference-pxichassisclock10source.html).

#### Properties

| Name | Description |
| --- | --- |
| None | Gets the clock source when the signal is not exported. |
| OnboardClock | Gets the clock source when the highly stable oven-controlled onboard frequency reference is used to drive the PXI_CLK signal. |
| ReferenceIn | Gets the clock source when the clock present at the front panel REF IN connector is used to drive the PXI_CLK signal. |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Creates an RfsgPxiChassisClock10Source object from the specified string. |
| Equals(RfsgPxiChassisClock10Source) | Determines whether the current instance of RfsgPxiChassisClock10Source object and the RfsgPxiChassisClock10Source object that you specify are equal. |
| Equals(object) | Determines whether the current instance of RfsgPxiChassisClock10Source and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgPxiChassisClock10Source. |
| ToString() | Converts the current instance of RfsgPxiChassisClock10Source to string. |

#### Operators

| Name | Description |
| --- | --- |
| operator RfsgPxiChassisClock10Source(string) | Converts the specified string representation of a PXI chassis clock 10 source to its RfsgPxiChassisClock10Source equivalent. |
| operator string(RfsgPxiChassisClock10Source) | Converts the RfsgPxiChassisClock10Source object to its equivalent string. |
| operator!=(RfsgPxiChassisClock10Source, RfsgPxiChassisClock10Source) | Checks whether the two instances of RfsgPxiChassisClock10Source are unequal. |
| operator==(RfsgPxiChassisClock10Source, RfsgPxiChassisClock10Source) | Determines whether the two instances of RfsgPxiChassisClock10Source are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgreferencepllbandwidth.html language=enus -->
## TOPIC 00179: RfsgReferencePllBandwidth Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgreferencepllbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgreferencepllbandwidth.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the loop bandwidth of the reference phase-locked loops (PLL). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgReferencePllBandwidthMembersNameValueDescriptionLow(int)0The device uses the lowest loop bandwidth setting for the PLL. Medium(int)1The device uses th

### RfsgReferencePllBandwidth Enumeration

Specifies the loop bandwidth of the reference phase-locked loops (PLL).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgReferencePllBandwidth

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Low | (int)0 | The device uses the lowest loop bandwidth setting for the PLL. |
| Medium | (int)1 | The device uses the medium loop bandwidth setting for the PLL. |
| High | (int)2 | The device uses the highest loop bandwidth setting for the PLL. |

#### See Also

- ReferencePllBandwidth

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgresetstepstoomit.html language=enus -->
## TOPIC 00180: RfsgResetStepsToOmit Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgresetstepstoomit.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgresetstepstoomit.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a list of steps to skip during the reset process. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgResetStepsToOmitMembersNameValueDescriptionNone(int)0x0No step is omitted during reset. Waveforms(int)0x1Omits clearing waveforms. Scripts(int)0x2Omits clearing s

### RfsgResetStepsToOmit Enumeration

Specifies a list of steps to skip during the reset process.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgResetStepsToOmit

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | (int)0x0 | No step is omitted during reset. |
| Waveforms | (int)0x1 | Omits clearing waveforms. |
| Scripts | (int)0x2 | Omits clearing scripts. |
| Routes | (int)0x4 | Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset. |
| DeembeddingTables | (int)0x8 | Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-equals__object.html language=enus -->
## TOPIC 00181: Equals(object)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-equals__object.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the current instance of RfsgRevisionQueryResult and the object that you specify are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectSpecifies the object to be compared to the current

### Equals(object)

Determines whether the current instance of [RfsgRevisionQueryResult](nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html) and the object that you specify are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | Specifies the object to be compared to the current instance of RfsgRevisionQueryResult. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-equals__rfsgrevisionqueryresult.html language=enus -->
## TOPIC 00182: Equals(RfsgRevisionQueryResult)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-equals__rfsgrevisionqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-equals__rfsgrevisionqueryresult.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares two RfsgRevisionQueryResult instances for equality. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool Equals(RfsgRevisionQueryResult result)ParametersNameTypeDescriptionresultRfsgRevisionQueryResultSpecifies an RfsgRevisionQueryResult to compare to this instance.Retu

### Equals(RfsgRevisionQueryResult)

Compares two [RfsgRevisionQueryResult](nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html) instances for equality.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool Equals(RfsgRevisionQueryResult result)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result | RfsgRevisionQueryResult | Specifies an RfsgRevisionQueryResult to compare to this instance. |

#### Returns

true if the two instances represent the same result; otherwise, false.

Parent topic:

RfsgRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-firmwarerevision.html language=enus -->
## TOPIC 00183: FirmwareRevision

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-firmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-firmwarerevision.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get a string that contains the firmware revision information for the NI-RFSG device you are currently using. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string FirmwareRevision { get; }RemarksReturns a String containing the instrument firmware revision numbers.

### FirmwareRevision

Get a string that contains the firmware revision information for the NI-RFSG device you are currently using.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string FirmwareRevision { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) containing the instrument firmware revision numbers.

Parent topic:

RfsgRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-gethashcode.html language=enus -->
## TOPIC 00184: GetHashCode()

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-gethashcode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the hash code for the current instance of RfsgRevisionQueryResult. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic override int GetHashCode()ReturnsReturns an Int32 that represents the hash code for the current instance of RfsgRevisionQueryResult.

### GetHashCode()

Returns the hash code for the current instance of [RfsgRevisionQueryResult](nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public override int GetHashCode()

#### Returns

Returns an Int32 that represents the hash code for the current instance of [RfsgRevisionQueryResult](nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html).

Parent topic:

RfsgRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-instrumentrevision.html language=enus -->
## TOPIC 00185: InstrumentRevision

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-instrumentrevision.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-instrumentrevision.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string that contains additional version information about NI-RFSG. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string InstrumentRevision { get; }RemarksReturns a String containing the instrument driver software revision numbers.

### InstrumentRevision

Gets a string that contains additional version information about NI-RFSG.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string InstrumentRevision { get; }

#### Remarks

Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) containing the instrument driver software revision numbers.

Parent topic:

RfsgRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-operator_eq__rfsgrevisionqueryresult-rfsgrevisionqueryresult.html language=enus -->
## TOPIC 00186: operator==(RfsgRevisionQueryResult, RfsgRevisionQueryResult)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-operator_eq__rfsgrevisionqueryresult-rfsgrevisionqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-operator_eq__rfsgrevisionqueryresult-rfsgrevisionqueryresult.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgRevisionQueryResult are equal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator==(RfsgRevisionQueryResult result1, RfsgRevisionQueryResult result2)ParametersNameTypeDescriptionresult1RfsgRevisionQueryResultSpecifies an

### operator==(RfsgRevisionQueryResult, RfsgRevisionQueryResult)

Checks whether the two instances of [RfsgRevisionQueryResult](nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator==(RfsgRevisionQueryResult result1, RfsgRevisionQueryResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | RfsgRevisionQueryResult | Specifies an RfsgRevisionQueryResult object. |
| result2 | RfsgRevisionQueryResult | Specifies an RfsgRevisionQueryResult object. |

#### Returns

true if the two instances are equal; otherwise, false.

Parent topic:

RfsgRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-operator_neq__rfsgrevisionqueryresult-rfsgrevisionqueryresult.html language=enus -->
## TOPIC 00187: operator!=(RfsgRevisionQueryResult, RfsgRevisionQueryResult)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-operator_neq__rfsgrevisionqueryresult-rfsgrevisionqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-operator_neq__rfsgrevisionqueryresult-rfsgrevisionqueryresult.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the two instances of RfsgRevisionQueryResult are unequal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static bool operator!=(RfsgRevisionQueryResult result1, RfsgRevisionQueryResult result2)ParametersNameTypeDescriptionresult1RfsgRevisionQueryResultSpecifies a

### operator!=(RfsgRevisionQueryResult, RfsgRevisionQueryResult)

Checks whether the two instances of [RfsgRevisionQueryResult](nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html) are unequal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static bool operator!=(RfsgRevisionQueryResult result1, RfsgRevisionQueryResult result2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| result1 | RfsgRevisionQueryResult | Specifies an RfsgRevisionQueryResult object. |
| result2 | RfsgRevisionQueryResult | Specifies an RfsgRevisionQueryResult object. |

#### Returns

true if the two instances are unequal; otherwise, false.

Parent topic:

RfsgRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-rfsgrevisionqueryresult__string-string.html language=enus -->
## TOPIC 00188: RfsgRevisionQueryResult(string, string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-rfsgrevisionqueryresult__string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult-rfsgrevisionqueryresult__string-string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of RfsgRevisionQueryResult. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgRevisionQueryResult(string instrumentRevision, string firmwareRevision)ParametersNameTypeDescriptioninstrumentRevisionstringSpecifies the value of the specific driver revis

### RfsgRevisionQueryResult(string, string)

Initializes a new instance of [RfsgRevisionQueryResult](nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public RfsgRevisionQueryResult(string instrumentRevision, string firmwareRevision)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrumentRevision | string | Specifies the value of the specific driver revision. |
| firmwareRevision | string | Specifies the value of the firmware revision. |

Parent topic:

RfsgRevisionQueryResult Data Structure

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html language=enus -->
## TOPIC 00189: RfsgRevisionQueryResult Data Structure

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrevisionqueryresult.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the driver revision. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic struct RfsgRevisionQueryResultRemarksSee the result of RevisionQuery. ConstructorsNameDescriptionRfsgRevisionQueryResult(string, string)Initializes a new instance of RfsgRevisionQuery

### RfsgRevisionQueryResult Data Structure

Represents the driver revision.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public struct RfsgRevisionQueryResult

#### Remarks

See the result of [RevisionQuery](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-revisionquery.html).

#### Constructors

| Name | Description |
| --- | --- |
| RfsgRevisionQueryResult(string, string) | Initializes a new instance of RfsgRevisionQueryResult. |

#### Properties

| Name | Description |
| --- | --- |
| FirmwareRevision | Get a string that contains the firmware revision information for the NI-RFSG device you are currently using. |
| InstrumentRevision | Gets a string that contains additional version information about NI-RFSG. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(RfsgRevisionQueryResult) | Compares two RfsgRevisionQueryResult instances for equality. |
| Equals(object) | Determines whether the current instance of RfsgRevisionQueryResult and the object that you specify are equal. |
| GetHashCode() | Returns the hash code for the current instance of RfsgRevisionQueryResult. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(RfsgRevisionQueryResult, RfsgRevisionQueryResult) | Checks whether the two instances of RfsgRevisionQueryResult are unequal. |
| operator==(RfsgRevisionQueryResult, RfsgRevisionQueryResult) | Checks whether the two instances of RfsgRevisionQueryResult are equal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-advanced.html language=enus -->
## TOPIC 00190: Advanced

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-advanced.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Advanced sub-object that relate only to the RF Advanced. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgRFAdvanced Advanced { get; }RemarksReturns an object of type RfsgRFAdvanced. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Advanced property was acc

### Advanced

Gets the Advanced sub-object that relate only to the RF Advanced.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgRFAdvanced](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced.html) Advanced { get; }

#### Remarks

Returns an object of type [RfsgRFAdvanced](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Advanced property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-configure__double-double.html language=enus -->
## TOPIC 00191: Configure(double, double)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-configure__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-configure__double-double.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency and power level of the RF output signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void Configure(double frequency, double powerLevel)RemarksThe NI-RFSG device must be in the Configuration state before you call this method. ParametersNameTypeDescri

### Configure(double, double)

Configures the frequency and power level of the RF output signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void Configure(double frequency, double powerLevel)

#### Remarks

The NI-RFSG device must be in the Configuration state before you call this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| frequency | double | Specifies the frequency of the generated RF signal. For arbitrary waveform generation, this parameter specifies, in Hz, the center frequency of the signal. NI-RFSG sets Frequency to this value. Refer to the specifications sheet for allowable frequency settings. |
| powerLevel | double | Specifies the power level of the generated RF signal, expressed in dBm. By default, this parameter specifies the average power of the signal. To configure the power level of a waveform with varying power content, set PowerLevelType to PeakPower. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Configure method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-externalgain.html language=enus -->
## TOPIC 00192: ExternalGain

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-externalgain.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-externalgain.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the external amplification or attenuation, if any, between the RF signal generator and the device under test. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double ExternalGain { get; set; }RemarksSpecifies a Double representing the external amplification or attenu

### ExternalGain

Gets or sets the external amplification or attenuation, if any, between the RF signal generator and the device under test.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double ExternalGain { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the external amplification or attenuation, if any, between the RF signal generator and the device under test.

Note

Setting this property adjusts the device output power to compensate for any amplification or attenuation between the RF signal generator and the device under test.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExternalGain property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-frequency.html language=enus -->
## TOPIC 00193: Frequency

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-frequency.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frequency of the generated RF signal, in Hertz (Hz). For arbitrary waveform generation, this property specifies the center frequency of the signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double Frequency { get; set; }RemarksSpecifies a Double representi

### Frequency

Gets or sets the frequency of the generated RF signal, in Hertz (Hz). For arbitrary waveform generation, this property specifies the center frequency of the signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double Frequency { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the frequency of the generated RF signal.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Frequency property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-localoscillator.html language=enus -->
## TOPIC 00194: LocalOscillator

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-localoscillator.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-localoscillator.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the LocalOscillator sub-object that relate only to the local oscillator. An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgRFLocalOscillator.this[string]. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgRFLocalOscillator

### LocalOscillator

Gets the LocalOscillator sub-object that relate only to the local oscillator. An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgRFLocalOscillator.this[string].

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgRFLocalOscillator](nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator.html) LocalOscillator { get; }

#### Remarks

Returns an object of type [RfsgRFLocalOscillator](nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LocalOscillator property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-looutexportconfigurefromrfsa.html language=enus -->
## TOPIC 00195: LOOutExportConfigureFromRfsa

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-looutexportconfigurefromrfsa.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-looutexportconfigurefromrfsa.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgLOOutExportConfigureFromRfsa LOOutExportConfigureFromRfsa { get; set; }RemarksSpecifies the RfsgLOOutExportConfigureFromRfsa enumeration. ExceptionsTypeDe

### LOOutExportConfigureFromRfsa

Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgLOOutExportConfigureFromRfsa](nationalinstruments-modularinstruments-nirfsg-rfsglooutexportconfigurefromrfsa.html) LOOutExportConfigureFromRfsa { get; set; }

#### Remarks

Specifies the [RfsgLOOutExportConfigureFromRfsa](nationalinstruments-modularinstruments-nirfsg-rfsglooutexportconfigurefromrfsa.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOOutExportConfigureFromRfsa property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-outputenabled.html language=enus -->
## TOPIC 00196: OutputEnabled

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-outputenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-outputenabled.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether signal output is enabled or disabled. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool OutputEnabled { get; set; }Remarkstrue if the signal output is enabled and false if disabled. This property can be set in any software state, and it does not change th

### OutputEnabled

Gets or sets whether signal output is enabled or disabled.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool OutputEnabled { get; set; }

#### Remarks

true if the signal output is enabled and false if disabled.

This property can be set in any software state, and it does not change the current state. Setting output enabled to false while in the Generation state stops signal output although generation continues internally.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The OutputEnabled property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-peakpoweradjustment.html language=enus -->
## TOPIC 00197: PeakPowerAdjustment

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-peakpoweradjustment.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-peakpoweradjustment.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the adjustment for PowerLevel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double PeakPowerAdjustment { get; set; }RemarksSpecifies a Double representing the adjustment for the PowerLevelThe value of the PeakPowerAdjustment property adds to the PowerLevel proper

### PeakPowerAdjustment

Gets or sets the adjustment for [PowerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerlevel.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double PeakPowerAdjustment { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the adjustment for the [PowerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerlevel.html)

The value of the PeakPowerAdjustment property adds to the [PowerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerlevel.html) property. The PeakPowerAdjustment property specifies the peak-to-average power ratio (PAPR) of a waveform. If the PAPR is specified, the specified power level becomes the average power level of the waveform, even if [PowerLevelType](nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerleveltype.html) is set to [PeakPower](nationalinstruments-modularinstruments-nirfsg-rfsgrfpowerleveltype.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PeakPowerAdjustment property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-phaseoffset.html language=enus -->
## TOPIC 00198: PhaseOffset

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-phaseoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-phaseoffset.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the phase, in degrees (º) of the RF output signal. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double PhaseOffset { get; set; }RemarksSpecifies a Double representing the phase of the RF output signal. This property can be used to align the RF output of this devi

### PhaseOffset

Gets or sets the phase, in degrees (º) of the RF output signal.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double PhaseOffset { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the phase of the RF output signal.

This property can be used to align the RF output of this device with the phase of another device, as long as the two devices are phase coherent.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PhaseOffset property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerlevel.html language=enus -->
## TOPIC 00199: PowerLevel

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerlevel.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets either the average power level or peak power level of the generated RF signal, depending on PowerLevelType setting. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double PowerLevel { get; set; }RemarksSpecifies a Double representing the power level of the generated

### PowerLevel

Gets or sets either the average power level or peak power level of the generated RF signal, depending on [PowerLevelType](nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerleveltype.html) setting.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double PowerLevel { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the power level of the generated RF signal.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PowerLevel property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerleveltype.html language=enus -->
## TOPIC 00200: PowerLevelType

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerleveltype.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the way the driver interprets the value of PowerLevel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgRFPowerLevelType PowerLevelType { get; set; }RemarksSpecifies the RfsgRFPowerLevelType enumeration. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe

### PowerLevelType

Gets or sets the way the driver interprets the value of [PowerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerlevel.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgRFPowerLevelType](nationalinstruments-modularinstruments-nirfsg-rfsgrfpowerleveltype.html) PowerLevelType { get; set; }

#### Remarks

Specifies the [RfsgRFPowerLevelType](nationalinstruments-modularinstruments-nirfsg-rfsgrfpowerleveltype.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PowerLevelType property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-rfblankingsource.html language=enus -->
## TOPIC 00201: RFBlankingSource

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-rfblankingsource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-rfblankingsource.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Marker event at which RF blanking occurs. For PXIe-5830/5831/5832, the RF Blanking reserves a PXI trigger line. If you are calling any ResetDevice or RfsaDriverUtility.ResetDevice on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you

### RFBlankingSource

Gets or sets the Marker event at which RF blanking occurs.

Note

For PXIe-5830/5831/5832, the RF Blanking reserves a PXI trigger line. If you are calling any [ResetDevice](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetdevice.html) or RfsaDriverUtility.ResetDevice on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call [ResetWithOptions](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-resetwithoptions__rfsgresetstepstoomit.html) or RfsaDriverUtility.ResetWithOptions. Select Routes in the stepsToOmit parameter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

RfsgRFBlankingSource

#### Remarks

RfsgRFBlankingSource

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The RFBlankingSource property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-rfinloexportenabled.html language=enus -->
## TOPIC 00202: RFInLOExportEnabled

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-rfinloexportenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-rfinloexportenabled.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgRFInLOExportEnabled RFInLOExportEnabled { get; set; }RemarksSpecifies the RfsgRFInLOExportEnabled enumeration. ExceptionsTypeDescriptionSystem.ObjectDispos

### RFInLOExportEnabled

Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgRFInLOExportEnabled](nationalinstruments-modularinstruments-nirfsg-rfsgrfinloexportenabled.html) RFInLOExportEnabled { get; set; }

#### Remarks

Specifies the [RfsgRFInLOExportEnabled](nationalinstruments-modularinstruments-nirfsg-rfsgrfinloexportenabled.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The RFInLOExportEnabled property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-upconverter.html language=enus -->
## TOPIC 00203: Upconverter

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-upconverter.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-upconverter.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Upconverter sub-object that relate only to the RF upconverter. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgUpconverter Upconverter { get; }RemarksReturns an object of type RfsgUpconverter. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Upconverter pr

### Upconverter

Gets the Upconverter sub-object that relate only to the RF upconverter.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgUpconverter](nationalinstruments-modularinstruments-nirfsg-rfsgupconverter.html) Upconverter { get; }

#### Remarks

Returns an object of type [RfsgUpconverter](nationalinstruments-modularinstruments-nirfsg-rfsgupconverter.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Upconverter property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf-waveforms.html language=enus -->
## TOPIC 00204: Waveforms

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf-waveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf-waveforms.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RfsgRFWaveformCollection sub-object used to configure channel based waveform attributes. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgRFWaveformCollection Waveforms { get; }RemarksSpecifies an object of type RfsgRFWaveformCollection.ExceptionsTypeDescriptionSyste

### Waveforms

Gets the [RfsgRFWaveformCollection](nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection.html) sub-object used to configure channel based waveform attributes.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgRFWaveformCollection](nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection.html) Waveforms { get; }

#### Remarks

Specifies an object of type [RfsgRFWaveformCollection](nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Waveforms property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRF Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrf.html language=enus -->
## TOPIC 00205: RfsgRF Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrf.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrf.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents all the fundamental properties and method for the RF. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgRF : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF Signal Ge

### RfsgRF Class

Represents all the fundamental properties and method for the RF.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgRF : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| Advanced | Gets the Advanced sub-object that relate only to the RF Advanced. |
| ExternalGain | Gets or sets the external amplification or attenuation, if any, between the RF signal generator and the device under test. |
| Frequency | Gets or sets the frequency of the generated RF signal, in Hertz (Hz). For arbitrary waveform generation, this property specifies the center frequency of the signal. |
| LocalOscillator | Gets the LocalOscillator sub-object that relate only to the local oscillator. An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgRFLocalOscillator.this[string]. |
| LOOutExportConfigureFromRfsa | Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export. |
| OutputEnabled | Gets or sets whether signal output is enabled or disabled. |
| PeakPowerAdjustment | Gets or sets the adjustment for PowerLevel. |
| PhaseOffset | Gets or sets the phase, in degrees (º) of the RF output signal. |
| PowerLevel | Gets or sets either the average power level or peak power level of the generated RF signal, depending on PowerLevelType setting. |
| PowerLevelType | Gets or sets the way the driver interprets the value of PowerLevel. |
| RFBlankingSource | Gets or sets the Marker event at which RF blanking occurs. Note For PXIe-5830/5831/5832, the RF Blanking reserves a PXI trigger line. If you are calling any ResetDevice or RfsaDriverUtility.ResetDevice on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call ResetWithOptions or RfsaDriverUtility.ResetWithOptions. Select Routes in the stepsToOmit parameter. |
| RFInLOExportEnabled | Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840. |
| Upconverter | Gets the Upconverter sub-object that relate only to the RF upconverter. |
| Waveforms | Gets the RfsgRFWaveformCollection sub-object used to configure channel based waveform attributes. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(double, double) | Configures the frequency and power level of the RF output signal. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-alccontrol.html language=enus -->
## TOPIC 00206: AlcControl

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-alccontrol.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-alccontrol.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to enable the automatic leveling control (ALC). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgAlcControl AlcControl { get; set; }RemarksNI 5654 with NI 5696: If you enable this property, the ALC is closed (closed-loop mode) and allows for better amplit

### AlcControl

Gets or sets whether to enable the automatic leveling control (ALC).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgAlcControl](nationalinstruments-modularinstruments-nirfsg-rfsgalccontrol.html) AlcControl { get; set; }

#### Remarks

NI 5654 with NI 5696: If you enable this property, the ALC is closed (closed-loop mode) and allows for better amplitude accuracy and wider amplitude dynamic range. If you disable this property, the ALC is open (open-loop mode), which is ideal when using modulation. Disabling the AlcControl property also allows for NI-RFSG to perform an automatic power search.

NI 5654: [Disable](nationalinstruments-modularinstruments-nirfsg-rfsgalccontrol.html) is the only supported value for this device. NI 5654 does not support the ALC when used as a stand-alone device.

Specifies the [RfsgAlcControl](nationalinstruments-modularinstruments-nirfsg-rfsgalccontrol.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AlcControl property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-allowoutofspecificationusersettings.html language=enus -->
## TOPIC 00207: AllowOutOfSpecificationUserSettings

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-allowoutofspecificationusersettings.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-allowoutofspecificationusersettings.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to allow the frequency and power values beyond the limits of the NI-RFSG device specifications. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool AllowOutOfSpecificationUserSettings { get; set; }Remarkstrue if frequency and power level settings beyond the

### AllowOutOfSpecificationUserSettings

Gets or sets whether to allow the frequency and power values beyond the limits of the NI-RFSG device specifications.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool AllowOutOfSpecificationUserSettings { get; set; }

#### Remarks

true if frequency and power level settings beyond the limits of the NI-RFSG device specifications is allowed; false if not allowed.

This capability allows a wider frequency and power range, but accuracy cannot be guaranteed, and results may vary by unit. To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AllowOutOfSpecificationUserSettings property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-amplificationpath.html language=enus -->
## TOPIC 00208: AmplificationPath

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-amplificationpath.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-amplificationpath.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power. NI-RFSG automatically sets the value of this property based on power and frequency settings. Setting this property ove

### AmplificationPath

Gets or sets the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power. NI-RFSG automatically sets the value of this property based on power and frequency settings. Setting this property overrides the value chosen by the NI-RFSG device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgAmplificationPath](nationalinstruments-modularinstruments-nirfsg-rfsgamplificationpath.html) AmplificationPath { get; set; }

#### Remarks

Note: Resetting this property reverts back to the default behavior.

Specifies the [RfsgAmplificationPath](nationalinstruments-modularinstruments-nirfsg-rfsgamplificationpath.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AmplificationPath property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-amplitudesettling.html language=enus -->
## TOPIC 00209: AmplitudeSettling

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-amplitudesettling.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-amplitudesettling.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amplitude settling accuracy, in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the Initiate method or the WaitUntilSettled method, or prior to advancing to next step if using RF list mode. Any specified amplitude settling value t

### AmplitudeSettling

Gets or sets the amplitude settling accuracy, in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the [Initiate](nationalinstruments-modularinstruments-nirfsg-nirfsg-initiate.html) method or the [WaitUntilSettled](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-waituntilsettled__int.html) method, or prior to advancing to next step if using RF list mode. Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value. NI 5650/5651/5652: This property is for NI internal use only.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double AmplitudeSettling { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the the amplitude settling accuracy in decibels.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AmplitudeSettling property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorholdenabled.html language=enus -->
## TOPIC 00210: AttenuatorHoldEnabled

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorholdenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorholdenabled.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether attenuator hold is enabled or disabled. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool AttenuatorHoldEnabled { get; set; }Remarkstrue if attenuator hold is enabled; otherwise false. While this property is set to true, changing the power level causes NI

### AttenuatorHoldEnabled

Gets or sets whether attenuator hold is enabled or disabled.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool AttenuatorHoldEnabled { get; set; }

#### Remarks

true if attenuator hold is enabled; otherwise false.

true

true

- Power level is less than or equal to the maximum power level set with [AttenuatorHoldMaximumPower](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorholdmaximumpower.html).
- Power level is greater than or equal to -145 dBm.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AttenuatorHoldEnabled property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorholdmaximumpower.html language=enus -->
## TOPIC 00211: AttenuatorHoldMaximumPower

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorholdmaximumpower.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorholdmaximumpower.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum power level, in dBm, of the RF output signal when AttenuatorHoldEnabled is set to true. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double AttenuatorHoldMaximumPower { get; set; }RemarksSpecifies a Double representing the maximum power level of the R

### AttenuatorHoldMaximumPower

Gets or sets the maximum power level, in dBm, of the RF output signal when [AttenuatorHoldEnabled](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorholdenabled.html) is set to true.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double AttenuatorHoldMaximumPower { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the maximum power level of the RF output signal.

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AttenuatorHoldMaximumPower property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorsetting.html language=enus -->
## TOPIC 00212: AttenuatorSetting

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorsetting.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-attenuatorsetting.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the level of attenuation in the attenuator path, in dB. Setting this property overrides the value chosen by NI-RFSG. Not all the power levels are achievable if you set this property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double AttenuatorSetting { get; set

### AttenuatorSetting

Gets or sets the level of attenuation in the attenuator path, in dB. Setting this property overrides the value chosen by NI-RFSG. Not all the power levels are achievable if you set this property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double AttenuatorSetting { get; set; }

#### Remarks

Note: Resetting this property reverts back to the default behavior.

Valid Values: 0 to 110, in steps of 10.

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the level of attenuation in the attenuator path.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AttenuatorSetting property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-automaticthermalcorrection.html language=enus -->
## TOPIC 00213: AutomaticThermalCorrection

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-automaticthermalcorrection.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-automaticthermalcorrection.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the value to enable or disable automatic thermal correction. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool AutomaticThermalCorrection { get; set; }Remarkstrue if automatic thermal correction is enabled and false if disabled. When enabled, settings changes cau

### AutomaticThermalCorrection

Gets or sets the value to enable or disable automatic thermal correction.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool AutomaticThermalCorrection { get; set; }

#### Remarks

true if automatic thermal correction is enabled and false if disabled.

When enabled, settings changes cause NI-RFSG to check whether the device temperature has changed and adjust the settings as needed. When disabled, you must explicitly call [PerformThermalCorrection](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-performthermalcorrection.html) to adjust the device for temperature changes.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AutomaticThermalCorrection property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-autopowersearch.html language=enus -->
## TOPIC 00214: AutoPowerSearch

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-autopowersearch.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-autopowersearch.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the automatic power search. When you set this property to Enable, NI-RFSG performs a power search after you initiate the device, or after you enable output power, or when the frequency or power level changes. When you set this property to Disable, NI-RFSG does not perform a power search

### AutoPowerSearch

Gets or sets the automatic power search. When you set this property to [Enable](nationalinstruments-modularinstruments-nirfsg-rfsgautopowersearch.html), NI-RFSG performs a power search after you initiate the device, or after you enable output power, or when the frequency or power level changes. When you set this property to [Disable](nationalinstruments-modularinstruments-nirfsg-rfsgautopowersearch.html), NI-RFSG does not perform a power search unless you call the [PerformPowerSearch](nationalinstruments-modularinstruments-nirfsg-rfsgdriverutility-performpowersearch.html) method. This property is ignored if you set the [AlcControl](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-alccontrol.html) property to [Enable](nationalinstruments-modularinstruments-nirfsg-rfsgalccontrol.html). NI 5654: [Disable](nationalinstruments-modularinstruments-nirfsg-rfsgautopowersearch.html) is the only supported value for this device.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgAutoPowerSearch](nationalinstruments-modularinstruments-nirfsg-rfsgautopowersearch.html) AutoPowerSearch { get; set; }

#### Remarks

Specifies the [RfsgAutoPowerSearch](nationalinstruments-modularinstruments-nirfsg-rfsgautopowersearch.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The AutoPowerSearch property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-correctiontemperature.html language=enus -->
## TOPIC 00215: CorrectionTemperature

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-correctiontemperature.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-correctiontemperature.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the temperature, in degrees Celsius, to use for adjusting the device settings to correct the temperature changes. If you set this property, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this

### CorrectionTemperature

Gets or sets the temperature, in degrees Celsius, to use for adjusting the device settings to correct the temperature changes. If you set this property, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this property, NI-RFSG sets the current device temperature in the Committed state as the value of this property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double CorrectionTemperature { get; set; }

#### Remarks

Note: Resetting this property reverts the temperature back to the default behavior.

Note: Use this property only when your application requires the same settings to be used every time, regardless of the temperature variation. In these cases, ensure that the temperature does not vary too much.

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the temperature.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CorrectionTemperature property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-exportedpulsemodulationeventactivelevel.html language=enus -->
## TOPIC 00216: ExportedPulseModulationEventActiveLevel

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-exportedpulsemodulationeventactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-exportedpulsemodulationeventactivelevel.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pulse modulation output active level to use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgTriggerLevel ExportedPulseModulationEventActiveLevel { get; set; }RemarksSpecifies the RfsgTriggerLevel enumeration. The default value is ActiveHigh. ExceptionsTypeD

### ExportedPulseModulationEventActiveLevel

Gets or sets the pulse modulation output active level to use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgTriggerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html) ExportedPulseModulationEventActiveLevel { get; set; }

#### Remarks

Specifies the [RfsgTriggerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html) enumeration. The default value is [ActiveHigh](nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportedPulseModulationEventActiveLevel property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-exportedpulsemodulationeventoutputterminal.html language=enus -->
## TOPIC 00217: ExportedPulseModulationEventOutputTerminal

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-exportedpulsemodulationeventoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-exportedpulsemodulationeventoutputterminal.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pulse modulation output terminal to use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgExportedPulseModulationEventOutputTerminal ExportedPulseModulationEventOutputTerminal { get; set; }RemarksA string representing output terminal name. ExceptionsTypeDescr

### ExportedPulseModulationEventOutputTerminal

Gets or sets the pulse modulation output terminal to use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgExportedPulseModulationEventOutputTerminal](nationalinstruments-modularinstruments-nirfsg-rfsgexportedpulsemodulationeventoutputterminal.html) ExportedPulseModulationEventOutputTerminal { get; set; }

#### Remarks

A string representing output terminal name.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ExportedPulseModulationEventOutputTerminal property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencysettlingtime.html language=enus -->
## TOPIC 00218: FrequencySettlingTime

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencysettlingtime.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencysettlingtime.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frequency settling time. Interpretation of this value depends on FrequencySettlingUnits. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double FrequencySettlingTime { get; set; }RemarksSpecifies a Double representing the frequency settling time. ExceptionsTypeD

### FrequencySettlingTime

Gets or sets the frequency settling time. Interpretation of this value depends on [FrequencySettlingUnits](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencysettlingunits.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double FrequencySettlingTime { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the frequency settling time.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The FrequencySettlingTime property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencysettlingunits.html language=enus -->
## TOPIC 00219: FrequencySettlingUnits

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencysettlingunits.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencysettlingunits.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the interpretation of the value passed to FrequencySettlingTime. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgRFFrequencySettlingUnits FrequencySettlingUnits { get; set; }RemarksSpecifies the RfsgRFFrequencySettlingUnits enumeration. ExceptionsTypeDescription

### FrequencySettlingUnits

Gets or sets the interpretation of the value passed to [FrequencySettlingTime](nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencysettlingtime.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgRFFrequencySettlingUnits](nationalinstruments-modularinstruments-nirfsg-rfsgrffrequencysettlingunits.html) FrequencySettlingUnits { get; set; }

#### Remarks

Specifies the [RfsgRFFrequencySettlingUnits](nationalinstruments-modularinstruments-nirfsg-rfsgrffrequencysettlingunits.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The FrequencySettlingUnits property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencytolerance.html language=enus -->
## TOPIC 00220: FrequencyTolerance

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencytolerance.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-frequencytolerance.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum frequency error, in Hertz (Hz) allowed during the software upconversion process. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double FrequencyTolerance { get; set; }RemarksSpecifies a Double representing the maximum frequency error allowed during the

### FrequencyTolerance

Gets or sets the maximum frequency error, in Hertz (Hz) allowed during the software upconversion process.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double FrequencyTolerance { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the maximum frequency error allowed during the software upconversion process.

NI-RFSG may introduce a frequency error up to the specified amount in order to optimize computational speed and onboard memory usage while upconverting phase-continuous signals. If [PhaseContinuityEnabled](nationalinstruments-modularinstruments-nirfsg-rfsgarb-phasecontinuityenabled.html) is set to false, this property is ignored, and the driver does not introduce a frequency error.

To set this property, the NI-RFSG device must be in the Configuration state.

On devices that do not use software upconversion, this property is ignored. NI 5670 always uses software upconversion. NI 5671 uses software upconversion for I/Q rates greater than 8.33 MS/s.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The FrequencyTolerance property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-loopbandwidth.html language=enus -->
## TOPIC 00221: LoopBandwidth

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-loopbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-loopbandwidth.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the loop bandwidth of the tuning phase-locked loops (PLL). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgLoopBandwidth LoopBandwidth { get; set; }RemarksSpecifies the RfsgLoopBandwidth enumeration. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe Loo

### LoopBandwidth

Gets or sets the loop bandwidth of the tuning phase-locked loops (PLL).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgLoopBandwidth](nationalinstruments-modularinstruments-nirfsg-rfsgloopbandwidth.html) LoopBandwidth { get; set; }

#### Remarks

Specifies the [RfsgLoopBandwidth](nationalinstruments-modularinstruments-nirfsg-rfsgloopbandwidth.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LoopBandwidth property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-peakenvelopepower.html language=enus -->
## TOPIC 00222: PeakEnvelopePower

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-peakenvelopepower.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-peakenvelopepower.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the maximum instantaneous power of the current RF output signal in dBm. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double PeakEnvelopePower { get; }RemarksReturns a Double representing the maximum instantaneous power of the current RF output signal. ExceptionsTypeDescr

### PeakEnvelopePower

Gets the maximum instantaneous power of the current RF output signal in dBm.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double PeakEnvelopePower { get; }

#### Remarks

Returns a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the maximum instantaneous power of the current RF output signal.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PeakEnvelopePower property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-peakpoweradjustmentinheritance.html language=enus -->
## TOPIC 00223: PeakPowerAdjustmentInheritance

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-peakpoweradjustmentinheritance.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-peakpoweradjustmentinheritance.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the inheritance behavior of the PeakPowerAdjustment property when a script inherits values from specified waveforms. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgPeakPowerAdjustmentInheritance PeakPowerAdjustmentInheritance { get; set; }RemarksSpecifies the R

### PeakPowerAdjustmentInheritance

Gets or sets the inheritance behavior of the [PeakPowerAdjustment](nationalinstruments-modularinstruments-nirfsg-rfsgrf-peakpoweradjustment.html) property when a script inherits values from specified waveforms.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgPeakPowerAdjustmentInheritance](nationalinstruments-modularinstruments-nirfsg-rfsgpeakpoweradjustmentinheritance.html) PeakPowerAdjustmentInheritance { get; set; }

#### Remarks

Specifies the [RfsgPeakPowerAdjustmentInheritance](nationalinstruments-modularinstruments-nirfsg-rfsgpeakpoweradjustmentinheritance.html) enumeration. The default value is [ExactMatch](nationalinstruments-modularinstruments-nirfsg-rfsgpeakpoweradjustmentinheritance.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PeakPowerAdjustmentInheritance property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationactivelevel.html language=enus -->
## TOPIC 00224: PulseModulationActiveLevel

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationactivelevel.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pulse modulation active level to use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgTriggerLevel PulseModulationActiveLevel { get; set; }RemarksSpecifies the RfsgTriggerLevel enumeration. The default value is ActiveHigh. ExceptionsTypeDescriptionSystem.Obj

### PulseModulationActiveLevel

Gets or sets the pulse modulation active level to use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgTriggerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html) PulseModulationActiveLevel { get; set; }

#### Remarks

Specifies the [RfsgTriggerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html) enumeration. The default value is [ActiveHigh](nationalinstruments-modularinstruments-nirfsg-rfsgtriggerlevel.html).

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PulseModulationActiveLevel property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationenabled.html language=enus -->
## TOPIC 00225: PulseModulationEnabled

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationenabled.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether pulse modulation is enabled or disabled. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool PulseModulationEnabled { get; set; }Remarkstrue if pulse modulation is enabled and false if it is disabled. If this property is enabled and the signal at the PLS MO

### PulseModulationEnabled

Gets or sets whether pulse modulation is enabled or disabled.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool PulseModulationEnabled { get; set; }

#### Remarks

true if pulse modulation is enabled and false if it is disabled.

If this property is enabled and the signal at the PLS MOD connector is high, the device generates a signal. If the signal is low, output generation is disabled.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PulseModulationEnabled property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationmode.html language=enus -->
## TOPIC 00226: PulseModulationMode

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationmode.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pulse modulation mode to use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgPulseModulationMode PulseModulationMode { get; set; }RemarksSpecifies the RfsgPulseModulationMode enumeration. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe PulseModul

### PulseModulationMode

Gets or sets the pulse modulation mode to use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgPulseModulationMode](nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationmode.html) PulseModulationMode { get; set; }

#### Remarks

Specifies the [RfsgPulseModulationMode](nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationmode.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PulseModulationMode property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationsource.html language=enus -->
## TOPIC 00227: PulseModulationSource

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationsource.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-pulsemodulationsource.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pulse modulation source to use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgPulseModulationSource PulseModulationSource { get; set; }RemarksA string representing source terminal name. ExceptionsTypeDescriptionSystem.ObjectDisposedExceptionThe PulseModula

### PulseModulationSource

Gets or sets the pulse modulation source to use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgPulseModulationSource](nationalinstruments-modularinstruments-nirfsg-rfsgpulsemodulationsource.html) PulseModulationSource { get; set; }

#### Remarks

A string representing source terminal name.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The PulseModulationSource property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-referencepllbandwidth.html language=enus -->
## TOPIC 00228: ReferencePllBandwidth

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-referencepllbandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-referencepllbandwidth.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the loop bandwidth of the reference phase-locked loop (PLL). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgReferencePllBandwidth ReferencePllBandwidth { get; set; }RemarksSpecifies the RfsgReferencePllBandwidth enumeration. ExceptionsTypeDescriptionSystem.Obje

### ReferencePllBandwidth

Gets or sets the loop bandwidth of the reference phase-locked loop (PLL).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgReferencePllBandwidth](nationalinstruments-modularinstruments-nirfsg-rfsgreferencepllbandwidth.html) ReferencePllBandwidth { get; set; }

#### Remarks

Specifies the [RfsgReferencePllBandwidth](nationalinstruments-modularinstruments-nirfsg-rfsgreferencepllbandwidth.html) enumeration.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ReferencePllBandwidth property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-thermalcorrectionheadroomrange.html language=enus -->
## TOPIC 00229: ThermalCorrectionHeadroomRange

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-thermalcorrectionheadroomrange.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-thermalcorrectionheadroomrange.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the DeviceTemperature property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double ThermalCorrectionHeadroomRange { get; set; }RemarksThe

### ThermalCorrectionHeadroomRange

Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the [DeviceTemperature](nationalinstruments-modularinstruments-nirfsg-rfsgdevicecharacteristics-devicetemperature.html) property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double ThermalCorrectionHeadroomRange { get; set; }

#### Remarks

The default value for the PXIe-5830/5831/5832 is 5. The default value for the PXIe-5840 is 10.

For example, if this property is set to 5.0, and the device is self-calibrated at 35 degrees Celsius, then you can expect to run the device from 30 degrees Celsius to 40 degrees Celsius with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance or DSP overflows.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ThermalCorrectionHeadroomRange property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-thermalcorrectiontemperatureresolution.html language=enus -->
## TOPIC 00230: ThermalCorrectionTemperatureResolution

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-thermalcorrectiontemperatureresolution.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-thermalcorrectiontemperatureresolution.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double ThermalCorrectionTemperatureResolution { get; set; }Re

### ThermalCorrectionTemperatureResolution

Gets or sets the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double ThermalCorrectionTemperatureResolution { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the temperature change, in degrees Celsius.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The ThermalCorrectionTemperatureResolution property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-yigmaincoildrive.html language=enus -->
## TOPIC 00231: YigMainCoilDrive

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-yigmaincoildrive.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced-yigmaincoildrive.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the dynamics of the current driving the YIG main coil. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgYigMainCoilDriveType YigMainCoilDrive { get; set; }RemarksSpecifies the RfsgYigMainCoilDriveType enumeration. Setting this property to Fast on the NI 5653 allo

### YigMainCoilDrive

Gets or sets the dynamics of the current driving the YIG main coil.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgYigMainCoilDriveType](nationalinstruments-modularinstruments-nirfsg-rfsgyigmaincoildrivetype.html) YigMainCoilDrive { get; set; }

#### Remarks

Specifies the [RfsgYigMainCoilDriveType](nationalinstruments-modularinstruments-nirfsg-rfsgyigmaincoildrivetype.html) enumeration.

Setting this property to [Fast](nationalinstruments-modularinstruments-nirfsg-rfsgyigmaincoildrivetype.html) on the NI 5653 allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The YigMainCoilDrive property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFAdvanced Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced.html language=enus -->
## TOPIC 00232: RfsgRFAdvanced Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfadvanced.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the advanced properties that relate only to the RF. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgRFAdvanced : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF Sig

### RfsgRFAdvanced Class

Represents the advanced properties that relate only to the RF.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgRFAdvanced : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| AlcControl | Gets or sets whether to enable the automatic leveling control (ALC). |
| AllowOutOfSpecificationUserSettings | Gets or sets whether to allow the frequency and power values beyond the limits of the NI-RFSG device specifications. |
| AmplificationPath | Gets or sets the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power. NI-RFSG automatically sets the value of this property based on power and frequency settings. Setting this property overrides the value chosen by the NI-RFSG device. |
| AmplitudeSettling | Gets or sets the amplitude settling accuracy, in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the Initiate method or the WaitUntilSettled method, or prior to advancing to next step if using RF list mode. Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value. NI 5650/5651/5652: This property is for NI internal use only. |
| AttenuatorHoldEnabled | Gets or sets whether attenuator hold is enabled or disabled. |
| AttenuatorHoldMaximumPower | Gets or sets the maximum power level, in dBm, of the RF output signal when AttenuatorHoldEnabled is set to true. |
| AttenuatorSetting | Gets or sets the level of attenuation in the attenuator path, in dB. Setting this property overrides the value chosen by NI-RFSG. Not all the power levels are achievable if you set this property. |
| AutomaticThermalCorrection | Gets or sets the value to enable or disable automatic thermal correction. |
| AutoPowerSearch | Gets or sets the automatic power search. When you set this property to Enable, NI-RFSG performs a power search after you initiate the device, or after you enable output power, or when the frequency or power level changes. When you set this property to Disable, NI-RFSG does not perform a power search unless you call the PerformPowerSearch method. This property is ignored if you set the AlcControl property to Enable. NI 5654: Disable is the only supported value for this device. |
| CorrectionTemperature | Gets or sets the temperature, in degrees Celsius, to use for adjusting the device settings to correct the temperature changes. If you set this property, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this property, NI-RFSG sets the current device temperature in the Committed state as the value of this property. |
| ExportedPulseModulationEventActiveLevel | Gets or sets the pulse modulation output active level to use. |
| ExportedPulseModulationEventOutputTerminal | Gets or sets the pulse modulation output terminal to use. |
| FrequencySettlingTime | Gets or sets the frequency settling time. Interpretation of this value depends on FrequencySettlingUnits. |
| FrequencySettlingUnits | Gets or sets the interpretation of the value passed to FrequencySettlingTime. |
| FrequencyTolerance | Gets or sets the maximum frequency error, in Hertz (Hz) allowed during the software upconversion process. |
| LoopBandwidth | Gets or sets the loop bandwidth of the tuning phase-locked loops (PLL). |
| PeakEnvelopePower | Gets the maximum instantaneous power of the current RF output signal in dBm. |
| PeakPowerAdjustmentInheritance | Gets or sets the inheritance behavior of the PeakPowerAdjustment property when a script inherits values from specified waveforms. |
| PulseModulationActiveLevel | Gets or sets the pulse modulation active level to use. |
| PulseModulationEnabled | Gets or sets whether pulse modulation is enabled or disabled. |
| PulseModulationMode | Gets or sets the pulse modulation mode to use. |
| PulseModulationSource | Gets or sets the pulse modulation source to use. |
| ReferencePllBandwidth | Gets or sets the loop bandwidth of the reference phase-locked loop (PLL). |
| ThermalCorrectionHeadroomRange | Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the DeviceTemperature property. |
| ThermalCorrectionTemperatureResolution | Gets or sets the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state. |
| YigMainCoilDrive | Gets or sets the dynamics of the current driving the YIG main coil. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfblanking.html language=enus -->
## TOPIC 00233: RfsgRFBlanking Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfblanking.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfblanking.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables or disables RF blanking. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgRFBlankingMembersNameValueDescriptionEnabled(int)1RF blanking is enabled. Disabled(int)0RF blanking is enabled.

### RfsgRFBlanking Enumeration

Enables or disables RF blanking.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgRFBlanking

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Enabled | (int)1 | RF blanking is enabled. |
| Disabled | (int)0 | RF blanking is enabled. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-disable.html language=enus -->
## TOPIC 00234: Disable

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-disable.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source when RF blanking is disabled. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgRFBlankingSource Disable { get; }RemarksReturns an object of type RfsgRFBlankingSource representing an empty string.

### Disable

Gets the source when RF blanking is disabled.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

RfsgRFBlankingSource

#### Remarks

RfsgRFBlankingSource

Parent topic:

RfsgRFBlankingSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-marker2.html language=enus -->
## TOPIC 00235: Marker2

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-marker2.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-marker2.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source when RF blanking is tied to marker2. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static RfsgRFBlankingSource Marker2 { get; }RemarksReturns an object of type RfsgRFBlankingSource representing the string "marker2".

### Marker2

Gets the source when RF blanking is tied to marker2.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

RfsgRFBlankingSource

#### Remarks

RfsgRFBlankingSource

Parent topic:

RfsgRFBlankingSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-operator-rfsgrfblankingsource__string.html language=enus -->
## TOPIC 00236: operator RfsgRFBlankingSource(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-operator-rfsgrfblankingsource__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource-operator-rfsgrfblankingsource__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Convert the specified string to equivalent RfsgRFBlankingSource object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic static implicit operator RfsgRFBlankingSource(string source)ParametersNameTypeDescriptionsourcestringSpecifies the string to be converted to equivalent RfsgRFB

### operator RfsgRFBlankingSource(string)

Convert the specified string to equivalent [RfsgRFBlankingSource](nationalinstruments-modularinstruments-nirfsg-rfsgrfblankingsource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public static implicit operator RfsgRFBlankingSource(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Specifies the string to be converted to equivalent RfsgRFBlankingSource object. |

#### Returns

RfsgRFBlankingSource

source

Parent topic:

RfsgRFBlankingSource Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-frequencystepsize.html language=enus -->
## TOPIC 00237: FrequencyStepSize

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-frequencystepsize.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-frequencystepsize.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the step size for tuning the local oscillator (LO) phase-locked loop (PLL). SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double FrequencyStepSize { get; set; }RemarksSpecifies a Double representing the step size, in hertz (Hz), for tuning the local oscillator pha

### FrequencyStepSize

Gets or sets the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double FrequencyStepSize { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the step size, in hertz (Hz), for tuning the local oscillator phase-locked loop.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The FrequencyStepSize property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFLocalOscillator Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-lofrequency.html language=enus -->
## TOPIC 00238: LOFrequency

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-lofrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-lofrequency.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frequency of the LO source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double LOFrequency { get; set; }RemarksSpecifies the frequency of the LO source. This property is read/write if you are using an external LO. Otherwise, this property is read-only.To use

### LOFrequency

Gets or sets the frequency of the LO source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double LOFrequency { get; set; }

#### Remarks

Specifies the frequency of the LO source.

This property is read/write if you are using an external LO. Otherwise, this property is read-only.

To use this property for the PXIe-5830/5831/5832, you must specify the the channelName of the [RfsgChannelBasedLO](nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgRFLocalOscillator.this[string]

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOFrequency property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFLocalOscillator Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-looutenabled.html language=enus -->
## TOPIC 00239: LOOutEnabled

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-looutenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-looutenabled.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the local oscillator signal is present at the front panel LO Out connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool LOOutEnabled { get; set; }Remarkstrue if the local oscillator signal is present at the front panel LO Out connector; otherwise fa

### LOOutEnabled

Gets or sets whether the local oscillator signal is present at the front panel LO Out connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool LOOutEnabled { get; set; }

#### Remarks

true if the local oscillator signal is present at the front panel LO Out connector; otherwise false.

The local oscillator signal remains at the LO Out front panel connector until this property is set to false even if [OutputEnabled](nationalinstruments-modularinstruments-nirfsg-rfsgrf-outputenabled.html) is set to false, [Abort](nationalinstruments-modularinstruments-nirfsg-nirfsg-abort.html) is called, or the NI-RFSG session is closed.

To use this property for the PXIe-5830/5831/5832, you must specify the the channelName of the [RfsgChannelBasedLO](nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgRFLocalOscillator.this[string]

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOOutEnabled property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFLocalOscillator Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-looutpower.html language=enus -->
## TOPIC 00240: LOOutPower

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-looutpower.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-looutpower.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the power level of the signal at the LO OUT front panel connector. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic double LOOutPower { get; set; }RemarksSpecifies a Double representing the power level of the signal at the front panel LO Out connector. To use this pr

### LOOutPower

Gets or sets the power level of the signal at the LO OUT front panel connector.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public double LOOutPower { get; set; }

#### Remarks

Specifies a [Double](https://learn.microsoft.com/dotnet/api/system.double) representing the power level of the signal at the front panel LO Out connector.

To use this property for the PXIe-5830/5831/5832, you must specify the the channelName of the [RfsgChannelBasedLO](nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgRFLocalOscillator.this[string]

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The LOOutPower property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFLocalOscillator Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-source.html language=enus -->
## TOPIC 00241: Source

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-source.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator-source.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to use internal or external local oscillator (LO) source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgLocalOscillatorSource Source { get; set; }RemarksSpecifies an object of type RfsgLocalOscillatorSource. To use this property for the PXIe-5830/5831/

### Source

Gets or sets whether to use internal or external local oscillator (LO) source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html) Source { get; set; }

#### Remarks

Specifies an object of type [RfsgLocalOscillatorSource](nationalinstruments-modularinstruments-nirfsg-rfsglocaloscillatorsource.html).

To use this property for the PXIe-5830/5831/5832, you must specify the the channelName of the [RfsgChannelBasedLO](nationalinstruments-modularinstruments-nirfsg-rfsgchannelbasedlo.html) sub-object to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

An active channel can be passed using the indexer NationalInstruments.ModularInstruments.NIRfsg.RfsgRFLocalOscillator.this[string]

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The Source property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgRFLocalOscillator Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator.html language=enus -->
## TOPIC 00242: RfsgRFLocalOscillator Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrflocaloscillator.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents all the fundamental properties for the RF local oscillator. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgRFLocalOscillator : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic i

### RfsgRFLocalOscillator Class

Represents all the fundamental properties for the RF local oscillator.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgRFLocalOscillator : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| FrequencyStepSize | Gets or sets the step size for tuning the local oscillator (LO) phase-locked loop (PLL). |
| LOFrequency | Gets or sets the frequency of the LO source. |
| LOInPower | Gets or sets the power level of the signal at the front panel LO In connector in dBm. |
| LoopBandwidth | Gets or sets the loop bandwidth of the tuning phase-locked loops (PLL). |
| LOOutEnabled | Gets or sets whether the local oscillator signal is present at the front panel LO Out connector. |
| LOOutPower | Gets or sets the power level of the signal at the LO OUT front panel connector. |
| LOVcoFrequencyStepSize | Gets or sets the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. |
| PllFractionalModeEnabled | Gets or sets whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). This property enables or disables fractional frequency tuning in the LO. |
| Source | Gets or sets whether to use internal or external local oscillator (LO) source. |
| this[string channelName] | Gets the RfsgChannelBasedLO sub-object to configure channel based LO properties. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfpowerleveltype.html language=enus -->
## TOPIC 00243: RfsgRFPowerLevelType Enumeration

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfpowerleveltype.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfpowerleveltype.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how NI-RFSG interprets the value of the PowerLevel property. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic enum RfsgRFPowerLevelTypeMembersNameValueDescriptionAveragePower(int)7000Average power indicates the desired power averaged in time. The driver maximizes the dy

### RfsgRFPowerLevelType Enumeration

Specifies how NI-RFSG interprets the value of the [PowerLevel](nationalinstruments-modularinstruments-nirfsg-rfsgrf-powerlevel.html) property.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public enum RfsgRFPowerLevelType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AveragePower | (int)7000 | Average power indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform. If you write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. |
| PeakPower | (int)7001 | The power level type is peak power. Peak power indicates the maximum power level of the RF signal averaged over one period of the RF carrier signal frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using the peak power level type, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. |

#### See Also

- PowerLevelType

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection-this__string.html language=enus -->
## TOPIC 00244: this[string waveformName]

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection-this__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection-this__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets or gets the name used to store the waveform. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic RfsgRFWaveformAttributes this[string waveformName] { get; }Remarksspecifies the name used to store the waveform.

### this[string waveformName]

Sets or gets the name used to store the waveform.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public [RfsgRFWaveformAttributes](nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformattributes.html) this[string waveformName] { get; }

#### Remarks

specifies the name used to store the waveform.

Parent topic:

RfsgRFWaveformCollection Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection.html language=enus -->
## TOPIC 00245: RfsgRFWaveformCollection Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgrfwaveformcollection.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a collection attributes for configuring waveform properties. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgRFWaveformCollection : RfsgSubObjectPropertiesNameDescriptionthis[string waveformName]Sets or gets the name used to store th

### RfsgRFWaveformCollection Class

Represents a collection attributes for configuring waveform properties.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgRFWaveformCollection : RfsgSubObject

#### Properties

| Name | Description |
| --- | --- |
| this[string waveformName] | Sets or gets the name used to store the waveform. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripting-checkifscriptexists__string.html language=enus -->
## TOPIC 00246: CheckIfScriptExists(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripting-checkifscriptexists__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripting-checkifscriptexists__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks whether the script that you specify as scriptName exists. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic bool CheckIfScriptExists(string scriptName)RemarksSupported Devices: NI 5673/5673E ParametersNameTypeDescriptionscriptNamestringSpecifies the name of the script. This

### CheckIfScriptExists(string)

Checks whether the script that you specify as scriptName exists.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public bool CheckIfScriptExists(string scriptName)

#### Remarks

Supported Devices: NI 5673/5673E

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scriptName | string | Specifies the name of the script. This string is case-insensitive. |

#### Returns

true if the script exists; otherwise, false.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The CheckIfScriptExists method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScripting Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripting-deletescript__string.html language=enus -->
## TOPIC 00247: DeleteScript(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripting-deletescript__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripting-deletescript__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a specified script from the pool of currently defined scripts. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void DeleteScript(string scriptName)RemarksThe NI-RFSG device must be in the Configuration state before you call this method. ParametersNameTypeDescriptionscrip

### DeleteScript(string)

Deletes a specified script from the pool of currently defined scripts.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void DeleteScript(string scriptName)

#### Remarks

The NI-RFSG device must be in the Configuration state before you call this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| scriptName | string | Specifies the name of the script to delete. This string is case-insensitive. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The DeleteScript method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScripting Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripting-selectedscriptname.html language=enus -->
## TOPIC 00248: SelectedScriptName

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripting-selectedscriptname.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripting-selectedscriptname.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the script in the onboard memory to generate on calling Initiate when you set GenerationMode to Script. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic string SelectedScriptName { get; set; }RemarksSpecifies a String representing the name of the script in onboard me

### SelectedScriptName

Gets or sets the script in the onboard memory to generate on calling [Initiate](nationalinstruments-modularinstruments-nirfsg-nirfsg-initiate.html) when you set [GenerationMode](nationalinstruments-modularinstruments-nirfsg-rfsgarb-generationmode.html) to [Script](nationalinstruments-modularinstruments-nirfsg-rfsgwaveformgenerationmode.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public string SelectedScriptName { get; set; }

#### Remarks

Specifies a [String](https://learn.microsoft.com/dotnet/api/system.string) representing the name of the script in onboard memory selected to generate.

This property is ignored when [GenerationMode](nationalinstruments-modularinstruments-nirfsg-rfsgarb-generationmode.html) is set to [ArbitraryWaveform](nationalinstruments-modularinstruments-nirfsg-rfsgwaveformgenerationmode.html) or [ContinuousWave](nationalinstruments-modularinstruments-nirfsg-rfsgwaveformgenerationmode.html).

To set this property, the NI-RFSG device must be in the Configuration state.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The SelectedScriptName property was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScripting Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripting-writescript__string.html language=enus -->
## TOPIC 00249: WriteScript(string)

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripting-writescript__string.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripting-writescript__string.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a script to the device to control waveform generation in script mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic void WriteScript(string script)RemarksUse the GenerationMode property to specify script mode before you call this method. The NI-RFSG device must be in th

### WriteScript(string)

Writes a script to the device to control waveform generation in script mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public void WriteScript(string script)

#### Remarks

Use the [GenerationMode](nationalinstruments-modularinstruments-nirfsg-rfsgarb-generationmode.html) property to specify script mode before you call this method.

The NI-RFSG device must be in the Configuration state before you call this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| script | string | Specifies a string containing a syntactically correct script. NI-RFSG supports multiple scripts that may be selected by name with the SelectedScriptName property. Refer to Scripting Instructions for more information about using scripts. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The WriteScript method was accessed after the associated NIRfsg object was disposed. |

Parent topic:

RfsgScripting Class

<!--NI_TOPIC bundle=ni_rfsg-csharp-api-ref path=nationalinstruments-modularinstruments-nirfsg-rfsgscripting.html language=enus -->
## TOPIC 00250: RfsgScripting Class

- bundle_id: `ni_rfsg-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nirfsg-rfsgscripting.html`
- source_url: https://docs-be.ni.com/bundle/ni_rfsg-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nirfsg-rfsgscripting.html
- document_id: `ni_rfsg-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the methods and properties for scripting. Derives fromRfsgSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIRfsgpublic class RfsgScripting : RfsgSubObjectRemarksFor more information, refer to the NI-RFSG Instrument Driver Programming Flow topic in the NI RF Signal Generator

### RfsgScripting Class

Provides the methods and properties for scripting.

#### Derives from

- RfsgSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIRfsg](nationalinstruments-modularinstruments-nirfsg.html)

public class RfsgScripting : RfsgSubObject

#### Remarks

For more information, refer to the [NI-RFSG Instrument Driver Programming Flow](https://RFSG.chm::/ProgFLow.html) topic in the *NI RF Signal Generators Help*.

#### Properties

| Name | Description |
| --- | --- |
| SelectedScriptName | Gets or sets the script in the onboard memory to generate on calling Initiate when you set GenerationMode to Script. |

#### Methods

| Name | Description |
| --- | --- |
| CheckIfScriptExists(string) | Checks whether the script that you specify as scriptName exists. |
| DeleteScript(string) | Deletes a specified script from the pool of currently defined scripts. |
| WriteScript(string) | Writes a script to the device to control waveform generation in script mode. |

Parent topic:

NationalInstruments.ModularInstruments.NIRfsg
