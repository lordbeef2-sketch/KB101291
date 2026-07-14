# NI DOCUMENT BUNDLE: ni-digital-pattern-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-digital-pattern-csharp-api-ref start=1 end=158 -->
<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=api-reference.html language=enus -->
## TOPIC 00001: NI-Digital Pattern Driver C# .NET API Reference

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/api-reference.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This API reference provides information about the programmatic elements available for this product. Looking for Something Else? For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse R

### NI-Digital Pattern Driver C# .NET API Reference

This API reference provides information about the programmatic elements available for this product.

#### Looking for Something Else?

For information not found in the API Reference for your product, such as detailed descriptions of the product functionality and the step by step processes for use, browse *Related Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-createparallel__digitalpinset-string.html language=enus -->
## TOPIC 00002: CreateParallel(DigitalPinSet, string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-createparallel__digitalpinset-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-createparallel__digitalpinset-string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the capture waveform settings for parallel acquisition using DigitalPinSet. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void CreateParallel(DigitalPinSet pinSet, string waveformName)RemarksSettings apply across all sites if multiple sites are configured. You canno

### CreateParallel(DigitalPinSet, string)

Creates the capture waveform settings for parallel acquisition using [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void CreateParallel(DigitalPinSet pinSet, string waveformName)

#### Remarks

Settings apply across all sites if multiple sites are configured. You cannot reconfigure settings after waveforms are created.

The number of waveforms is limited to 512.

Refer to [Working with Pin Sets](/csh?context=niDigital_ninetdigitalfx40_net-pin-sets) for more information.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSet | DigitalPinSet | The set of pins or channels to create the waveform for. |
| waveformName | string | Specifies the waveform name to use. Use the waveformName with the capture_start opcode in your pattern. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |
| System.InvalidOperationException | The pinSet contains a system pin. |
| System.ArgumentException | The value for waveformName is an empty string or contains an invalid character. |
| Ivi.Driver.OutOfRangeException | The number of waveforms in capture memory exceeds the maximum number of waveforms allowed. |

Parent topic:

DigitalCaptureWaveforms Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-fetch__string-string-int-timespan-ref.html language=enus -->
## TOPIC 00003: Fetch(string, string, int, TimeSpan, ref uint)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-fetch__string-string-int-timespan-ref.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-fetch__string-string-int-timespan-ref.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches a defined number of samples for a specified list of sites. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic uint[][] Fetch(string siteList, string waveformName, int samplesToRead, TimeSpan maxTime, ref uint[][] data)RemarksIn order to get best performance, consider fet

### Fetch(string, string, int, TimeSpan, ref uint)

Fetches a defined number of samples for a specified list of sites.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public uint[][] Fetch(string siteList, string waveformName, int samplesToRead, TimeSpan maxTime, ref uint[][] data)

#### Remarks

In order to get best performance, consider fetching fewer samples multiple times rather than fetching large samples at once. This method only returns data from sites that are enabled when fetch is called.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| siteList | string | The comma-delimited list of sites on which to burst the pattern (for example, "<tt>site0,site1</tt>"). Sites that are not on this list are disabled. All sites are enabled for pattern bursting if the string is empty. |
| waveformName | string | The name of the waveform to fetch. Use the waveformName with the capture_start opcode in your pattern. |
| samplesToRead | int | The number of samples to fetch. |
| maxTime | TimeSpan | The maximum amount of time allowed for this method to complete in seconds. An exception is thrown if the method does not complete within this time span. |
| data | ref uint | The samples fetched from the capture waveform data for specified sites. The size of this array can be less than or equal to the number of sites specified in the siteList parameter, depending on whether sites are disabled. |

#### Returns

The captured data for each site specified. If a site is disabled, not enabled for burst, or the current instrument does not include any capture pins, the method does not return data for that site. Use [SortSiteResultsBySite(NIDigital[], string, SiteResultType, uint[][][], out int[])](nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortsiteresultsbysite__nidigital_arr1-string-siteresulttype-uint_arr1_arr1_arr1-out.html) to order and combine the data to match the *siteList* . You can also use [GetSiteResultsSiteNumbers](nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getsiteresultssitenumbers__string-siteresulttype.html) to obtain a sorted list of returned sites.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | The value for siteList contains an invalid site. |
| System.ArgumentException | The waveform name specified by waveformName does not exist. |
| System.InvalidOperationException | Fetch is called before bursting a pattern. |

Parent topic:

DigitalCaptureWaveforms Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms.html language=enus -->
## TOPIC 00004: DigitalCaptureWaveforms Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides operations to create and fetch capture waveforms with the NI-Digital Pattern Driver. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalCaptureWaveforms : DigitalSubObjectRemarksUse this class to create and fetch waveforms. You c

### DigitalCaptureWaveforms Class

Provides operations to create and fetch capture waveforms with the NI-Digital Pattern Driver.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalCaptureWaveforms : DigitalSubObject

#### Remarks

Use this class to create and fetch waveforms. You can create parallel data or serial data.

For more information on capture functionality, refer to [Capture](/csh?context=niDigital_digipat6570_capture) in the *Digital Pattern Help*.

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory or in the **Start** menu at **National Instruments » NI Digital Pattern Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Methods

| Name | Description |
| --- | --- |
| CreateFromFile(string, string) | Creates a capture waveform using the configuration information from a .digicapture file. |
| CreateParallel(DigitalPinSet, string) | Creates the capture waveform settings for parallel acquisition using DigitalPinSet. |
| CreateParallel(string, string) | Creates the capture waveform settings for parallel acquisition using a comma-delimited string of pins or channels. |
| CreateSerial(string, string, uint, BitOrder) | Creates the capture waveform settings for serial acquisition using a comma-delimited string of pins or channels. |
| CreateSerial(DigitalPinSet, string, uint, BitOrder) | Creates the capture waveform settings for serial acquisition using DigitalPinSet. |
| Fetch(string, string, int, TimeSpan, ref uint) | Fetches a defined number of samples for a specified list of sites. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-abort.html language=enus -->
## TOPIC 00005: Abort()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-abort.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-abort.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops clock generation on the specified channel(s) or pin(s) and pin group(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Abort()ExceptionsTypeDescriptionIvi.Driver.SelectorNameExceptionAn instance of DigitalPinSet references a pin or pin group name not loaded in th

### Abort()

Stops clock generation on the specified channel(s) or pin(s) and pin group(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Abort()

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | Abort was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalClockGenerator Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-frequency.html language=enus -->
## TOPIC 00006: Frequency

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-frequency.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the frequency of the free-running clock. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic double Frequency { get; set; }ReturnsSpecifies the clock frequency in Hz. ExceptionsTypeDescriptionIvi.Driver.SelectorNameExceptionAn instance of DigitalPinSet references a p

### Frequency

Gets or sets the frequency of the free-running clock.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public double Frequency { get; set; }

#### Returns

Specifies the clock frequency in Hz.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for Frequency is invalid. |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | Frequency was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalClockGenerator Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-generateclock__double-bool.html language=enus -->
## TOPIC 00007: GenerateClock(double, bool)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-generateclock__double-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalclockgenerator-generateclock__double-bool.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures and initiates clock generation on the specified channel(s), or pin(s) and pin group(s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void GenerateClock(double frequency, bool selectDigitalFunction)ParametersNameTypeDescriptionfrequencydoubleSpecifies the clock f

### GenerateClock(double, bool)

Configures and initiates clock generation on the specified channel(s), or pin(s) and pin group(s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void GenerateClock(double frequency, bool selectDigitalFunction)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| frequency | double | Specifies the clock frequency in Hz. |
| selectDigitalFunction | bool | If true, sets the SelectedFunction of the pins to Digital. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| System.InvalidOperationException | GenerateClock is called while the specified channel(s) is in use in a pattern burst or clock generator. |
| Ivi.Driver.OutOfRangeException | The value for frequency is invalid. |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | GenerateClock was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalClockGenerator Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger-terminalname.html language=enus -->
## TOPIC 00008: TerminalName

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger-terminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger-terminalname.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the terminal name of the DigitalConditionalJumpTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string TerminalName { get; }RemarksYou can use this terminal name as an input signal source for another trigger. ReturnsThe terminal name of the Di

### TerminalName

Gets a string containing the terminal name of the [DigitalConditionalJumpTrigger](nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string TerminalName { get; }

#### Remarks

You can use this terminal name as an input signal source for another trigger.

#### Returns

The terminal name of the [DigitalConditionalJumpTrigger](nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger.html).

Parent topic:

DigitalConditionalJumpTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-identifier.html language=enus -->
## TOPIC 00009: Identifier

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-identifier.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-identifier.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the case-sensitive unique identifier of the NI-Digital Pattern Driver software. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string Identifier { get; }ReturnsCase-sensitive unique identifier of the NI-Digital Pattern Driver software.

### Identifier

Gets a string containing the case-sensitive unique identifier of the NI-Digital Pattern Driver software.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string Identifier { get; }

#### Returns

Case-sensitive unique identifier of the NI-Digital Pattern Driver software.

Parent topic:

DigitalDriverIdentity Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-instrumentfirmwarerevision.html language=enus -->
## TOPIC 00010: InstrumentFirmwareRevision

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-instrumentfirmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-instrumentfirmwarerevision.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the firmware revision information for the digital pattern instrument currently in use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string InstrumentFirmwareRevision { get; }ReturnsFirmware revision information for the digital pattern instrument cu

### InstrumentFirmwareRevision

Gets a string containing the firmware revision information for the digital pattern instrument currently in use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string InstrumentFirmwareRevision { get; }

#### Returns

Firmware revision information for the digital pattern instrument currently in use. This value depends on the digital pattern instrument the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session is connected to.

Parent topic:

DigitalDriverIdentity Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-revision.html language=enus -->
## TOPIC 00011: Revision

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriveridentity-revision.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing any additional version information about the NI-Digital Pattern Driver software. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string Revision { get; }ReturnsAdditional version information about the NI-Digital Pattern Driver software. This value dep

### Revision

Gets a string containing any additional version information about the NI-Digital Pattern Driver software.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string Revision { get; }

#### Returns

Additional version information about the NI-Digital Pattern Driver software. This value depends on the digital pattern instrument the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session is connected to.

Parent topic:

DigitalDriverIdentity Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriveridentity.html language=enus -->
## TOPIC 00012: DigitalDriverIdentity Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriveridentity.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriveridentity.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides information about the instrument and the NI-Digital Pattern Driver software. Derives fromDigitalSubObjectIIviDriverIdentitySyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalDriverIdentity : DigitalSubObject, IIviDriverIdentityRemarksUse this class to get i

### DigitalDriverIdentity Class

Provides information about the instrument and the NI-Digital Pattern Driver software.

#### Derives from

- DigitalSubObject
- IIviDriverIdentity

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalDriverIdentity : DigitalSubObject, IIviDriverIdentity

#### Remarks

Use this class to get information about the instrument, such as the vendor, manufacturer, or revision.

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory or in the **Start** menu at **National Instruments » NI Digital Pattern Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Description | Gets a string containing a description of the specific NI-Digital Pattern Driver software. |
| Identifier | Gets a string containing the case-sensitive unique identifier of the NI-Digital Pattern Driver software. |
| InstrumentFirmwareRevision | Gets a string containing the firmware revision information for the digital pattern instrument currently in use. |
| InstrumentManufacturer | Gets a string containing the name of the manufacturer for the digital pattern instrument currently in use. |
| InstrumentModel | Gets a string containing the model number or name of the digital pattern instrument currently in use. |
| Revision | Gets a string containing any additional version information about the NI-Digital Pattern Driver software. |
| SerialNumber | Gets a string containing the serial number of the digital pattern instrument currently in use. |
| SpecificationMajorVersion | Gets an integer that specifies the major version number of the class specification in accordance with which the NIDigital .NET class library was developed. |
| SpecificationMinorVersion | Gets an integer that specifies the minor version number of the class specification in accordance with which the NIDigital .NET class library was developed. |
| Vendor | Gets a string containing the name of the vendor that supplies the NI-Digital Pattern Driver software. |

#### Methods

| Name | Description |
| --- | --- |
| GetGroupCapabilities() | Returns an array of strings containing the names of the IVI class capability groups, or standard methods and properties, that the NI-Digital Pattern Driver software implements. |
| GetSupportedInstrumentModels() | Returns an array of strings containing the names of the instrument models with which the NI-Digital Pattern Driver software is compatible. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-driversetup.html language=enus -->
## TOPIC 00013: DriverSetup

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-driversetup.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-driversetup.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the string used to set the initial values for NIDigital properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string DriverSetup { get; }ReturnsThe driver setup string is used to set the initial values for properties that are specific to NIDigital. This value is de

### DriverSetup

Gets the string used to set the initial values for [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string DriverSetup { get; }

#### Returns

The driver setup string is used to set the initial values for properties that are specific to [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html). This value is determined by the option string used to initialize the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session with the instrument.

Parent topic:

DigitalDriverOperation Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-queryinstrumentstatus.html language=enus -->
## TOPIC 00014: QueryInstrumentStatus

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-queryinstrumentstatus.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether the NI-Digital Pattern driver software queries the instrument status after each operation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool QueryInstrumentStatus { get; set; }RemarksThe NI-Digital Pattern Driver software can ignore

### QueryInstrumentStatus

Gets or sets a value indicating whether the NI-Digital Pattern driver software queries the instrument status after each operation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool QueryInstrumentStatus { get; set; }

#### Remarks

The NI-Digital Pattern Driver software can ignore status checking for particular properties, regardless of the setting of this property. This value is determined by the option string used to initialize the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session with the instrument.

#### Returns

true, if the instrument driver software queries the instrument status after each operation; otherwise, false. The default value is true.

Parent topic:

DigitalDriverOperation Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-rangecheck.html language=enus -->
## TOPIC 00015: RangeCheck

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriveroperation-rangecheck.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether to validate values and method parameters. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool RangeCheck { get; set; }RemarksIf you enable this property, the NI-Digital Pattern Driver software validates the parameter values that you pa

### RangeCheck

Gets or sets a value indicating whether to validate values and method parameters.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool RangeCheck { get; set; }

#### Remarks

If you enable this property, the NI-Digital Pattern Driver software validates the parameter values that you pass to methods. This value is determined by the option string used to initialize the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session with the instrument.

#### Returns

true, if the instrument driver validates values and method parameters; otherwise, false. The default value is true.

Parent topic:

DigitalDriverOperation Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-errorquery.html language=enus -->
## TOPIC 00016: ErrorQuery()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-errorquery.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-errorquery.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads an error code and the associated message from the NI-Digital Pattern Driver software error queue. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic ErrorQueryResult ErrorQuery()ReturnsThe error query result.

### ErrorQuery()

Reads an error code and the associated message from the NI-Digital Pattern Driver software error queue.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public ErrorQueryResult ErrorQuery()

#### Returns

The error query result.

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getchannelnamefromstring__string.html language=enus -->
## TOPIC 00017: GetChannelNameFromString(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getchannelnamefromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getchannelnamefromstring__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a comma-separated channel name list given a System.String index list. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string GetChannelNameFromString(string index)ParametersNameTypeDescriptionindexstringIndex list for the desired channels in the session. Valid values

### GetChannelNameFromString(string)

Returns a comma-separated channel name list given a System.String index list.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string GetChannelNameFromString(string index)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | string | Index list for the desired channels in the session. Valid values are from zero to one less than the number of channels in the session. The input string can be in one of the following formats: A comma-separated list—for example, "0,1,2,3"; a range using a hyphen—for example, "0-3"; or a range using a colon—for example, "0:3." You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated values are supported ("2,3,0","1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing. |

#### Returns

Returns a System.String populated with the corresponding name for each index in the same order the indexes appear in the input string.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | The GetChannelNameFromString method was called after the associated NIDigital or DigitalDriverUtility object was disposed. |
| ArgumentException | If one of the indexes in the list is out of range (less than zero or greater than number of channels minus one) |
| Ivi.Driver.SelectorNameException | If the input list does not have a valid format |
| Ivi.Driver.IviCDriverException | If the input list is empty or null |

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getpinresultspininformation__digitalpinset.html language=enus -->
## TOPIC 00018: GetPinResultsPinInformation(DigitalPinSet)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getpinresultspininformation__digitalpinset.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getpinresultspininformation__digitalpinset.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of pins or channels corresponding to the specified pin set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalPinInformation[] GetPinResultsPinInformation(DigitalPinSet pinSet)ParametersNameTypeDescriptionpinSetDigitalPinSetThe set of pins or channels for w

### GetPinResultsPinInformation(DigitalPinSet)

Gets an array of pins or channels corresponding to the specified pin set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalPinInformation](nationalinstruments-modularinstruments-nidigital-digitalpininformation.html)[] GetPinResultsPinInformation(DigitalPinSet pinSet)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSet | DigitalPinSet | The set of pins or channels for which to get pin information. |

#### Returns

A one-dimensional array of [DigitalPinInformation](nationalinstruments-modularinstruments-nidigital-digitalpininformation.html) that contains information for mapped pins.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetattribute__string-int.html language=enus -->
## TOPIC 00019: ResetAttribute(string, int)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetattribute__string-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetattribute__string-int.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a driver attribute to its default state using a string to specify pins, pin groups, or channels. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ResetAttribute(string pinSetString, int attributeId)ParametersNameTypeDescriptionpinSetStringstringThe pin set string r

### ResetAttribute(string, int)

Resets a driver attribute to its default state using a string to specify pins, pin groups, or channels.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ResetAttribute(string pinSetString, int attributeId)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSetString | string | The pin set string representing the pins, pin groups, or channels to reset the attribute for. |
| attributeId | int | The attribute to reset. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OperationNotSupportedException | The value for attributeId is not a valid attribute identifier. |

#### See Also

- ResetAttribute(DigitalPinSet, int)
- ResetAttribute(int)

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetdevice.html language=enus -->
## TOPIC 00020: ResetDevice()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetdevice.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetdevice.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the digital pattern instrument to a known state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ResetDevice()RemarksThis method performs the following tasks on the digital pattern instrument: Clears over-temperature and over-power conditions; Aborts pattern exec

### ResetDevice()

Returns the digital pattern instrument to a known state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ResetDevice()

#### Remarks

- Clears over-temperature and over-power conditions;
- Aborts pattern execution;
- Clears pin maps, time sets, source and capture waveforms, and patterns;
- Resets all properties to default values, including setting [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) to [Disconnect](nationalinstruments-modularinstruments-nidigital-selectedfunction.html), causing the I/O switches to open; and
- Stops export of all external signals and events.

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetwithdefaults.html language=enus -->
## TOPIC 00021: ResetWithDefaults()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetwithdefaults.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-resetwithdefaults.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the digital pattern instrument to a known state, while also resetting properties and settings to the initial values specified during the construction of the NIDigital session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ResetWithDefaults()

### ResetWithDefaults()

Resets the digital pattern instrument to a known state, while also resetting properties and settings to the initial values specified during the construction of the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ResetWithDefaults()

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortpinresultsbysite__nidigital_arr1-string-byte_arr1_arr1-out-out.html language=enus -->
## TOPIC 00022: SortPinResultsBySite(NIDigital[], string, byte, out string[], out int[])

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortpinresultsbysite__nidigital_arr1-string-byte_arr1_arr1-out-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortpinresultsbysite__nidigital_arr1-string-byte_arr1_arr1-out-out.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Organizes data read from multiple digital pattern instruments by grouping the data by site number. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic static byte[] SortPinResultsBySite(NIDigital[] sessions, string pinSetString, byte[][] resultsToSort, out string[] pinNames, out

### SortPinResultsBySite(NIDigital[], string, byte, out string[], out int[])

Organizes data read from multiple digital pattern instruments by grouping the data by site number.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public static byte[] SortPinResultsBySite(NIDigital[] sessions, string pinSetString, byte[][] resultsToSort, out string[] pinNames, out int[] siteNumbers)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessions | NIDigital[] | The instrument sessions to return data for. |
| pinSetString | string | The pin set from which to read data. |
| resultsToSort | byte | The data read from the digital pattern instruments, combined into a two-dimensional array. |
| pinNames | out string[] | An array of DUT pin names corresponding to the values in DUT pin results. |
| siteNumbers | out int[] | An array of site numbers corresponding to the values in DUT pin results. |

#### Returns

Returns the sorted and merged results as a one-dimensional array. Each element in this array represents a pin result corresponding to the pin at the same element of the *pinNames*  parameter.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortsiteresultsbysite__nidigital_arr1-string-siteresulttype-bool_arr1_arr1-out.html language=enus -->
## TOPIC 00023: SortSiteResultsBySite(NIDigital[], string, SiteResultType, bool, out int[])

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortsiteresultsbysite__nidigital_arr1-string-siteresulttype-bool_arr1_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortsiteresultsbysite__nidigital_arr1-string-siteresulttype-bool_arr1_arr1-out.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Orders site data read from multiple instruments to match the site list you specify, and combines data from instruments mapped to the same site. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic static bool[] SortSiteResultsBySite(NIDigital[] sessions, string siteList, SiteResul

### SortSiteResultsBySite(NIDigital[], string, SiteResultType, bool, out int[])

Orders site data read from multiple instruments to match the site list you specify, and combines data from instruments mapped to the same site.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public static bool[] SortSiteResultsBySite(NIDigital[] sessions, string siteList, SiteResultType siteResultType, bool[][] resultsToSort, out int[] siteNumbers)

#### Remarks

Each instrument returns data using the [Fetch](nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-fetch__string-string-int-timespan-ref.html) method for the enabled sites on which the instrument is configured to capture waveforms. Disabled sites return an empty array. The method returns the sorted results in the same order as the captured waveforms.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessions | NIDigital[] | The instrument sessions to return data for. |
| siteList | string | The comma-delimited list of strings of form site N, where N is the site number. |
| siteResultType | SiteResultType | The type of data in the results array. |
| resultsToSort | bool | The data in the results array sorted by the order in the siteList , along with the site number that corresponds to each value. |
| siteNumbers | out int[] | An array of site numbers corresponding to the values in DUT pin results. |

#### Returns

Returns the sorted and merged results as a one-dimensional array.

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortsiteresultsbysite__nidigital_arr1-string-siteresulttype-uint_arr1_arr1_arr1-out.html language=enus -->
## TOPIC 00024: SortSiteResultsBySite(NIDigital[], string, SiteResultType, uint, out int[])

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortsiteresultsbysite__nidigital_arr1-string-siteresulttype-uint_arr1_arr1_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaldriverutility-sortsiteresultsbysite__nidigital_arr1-string-siteresulttype-uint_arr1_arr1_arr1-out.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Orders site data read from multiple instruments to match the site list you specify, and combines data from instruments mapped to the same site. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic static uint[][] SortSiteResultsBySite(NIDigital[] sessions, string siteList, SiteRes

### SortSiteResultsBySite(NIDigital[], string, SiteResultType, uint, out int[])

Orders site data read from multiple instruments to match the site list you specify, and combines data from instruments mapped to the same site.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public static uint[][] SortSiteResultsBySite(NIDigital[] sessions, string siteList, SiteResultType siteResultType, uint[][][] waveformsToSort, out int[] siteNumbers)

#### Remarks

Each instrument returns data using the [Fetch](nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-fetch__string-string-int-timespan-ref.html) method for the enabled sites on which the instrument is configured to capture waveforms. Disabled sites return an empty array. The method returns the sorted results in the same order as the captured waveforms.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sessions | NIDigital[] | The instrument sessions to return data for. |
| siteList | string | The comma-delimited list of strings of form site N, where N is the site number. |
| siteResultType | SiteResultType | The type of data in the results array. |
| waveformsToSort | uint | The waveform data to read from the digital pattern instruments. |
| siteNumbers | out int[] | An array of site numbers corresponding to the values in DUT pin results. |

#### Returns

Returns the sorted and merged results.

Parent topic:

DigitalDriverUtility Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaledge.html language=enus -->
## TOPIC 00025: DigitalEdge Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaledge.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the start trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum DigitalEdgeMembersNameValueDescriptionRising1800Asserts the trigger when the signal transitions from low level to high level. Falling1801Asserts the trigger when the signal t

### DigitalEdge Enumeration

Specifies the active edge for the start trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum DigitalEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rising | 1800 | Asserts the trigger when the signal transitions from low level to high level. |
| Falling | 1801 | Asserts the trigger when the signal transitions from high level to low level. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger-configure__string-digitaledge.html language=enus -->
## TOPIC 00026: Configure(string, DigitalEdge)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger-configure__string-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger-configure__string-digitaledge.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the TriggerType to Software, and configures the DigitalEdge and Edge properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Configure(string source, DigitalEdge type)ParametersNameTypeDescriptionsourcestringThe value to set Source to.typeDigitalEdgeThe va

### Configure(string, DigitalEdge)

Configures the [TriggerType](nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger-triggertype.html) to [Software](nationalinstruments-modularinstruments-nidigital-triggertype.html), and configures the [DigitalEdge](nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger-digitaledge.html) and [Edge](nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger-edge.html) properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Configure(string source, DigitalEdge type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The value to set Source to. |
| type | DigitalEdge | The value to set Edge to. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for type is invalid. |

Parent topic:

DigitalEdgeConditionalJumpTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger-edge.html language=enus -->
## TOPIC 00027: Edge

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger-edge.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the active edge for the Conditional Jump Trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalEdge Edge { get; set; }ReturnsThe active edge for the Conditional Jump Trigger. This property is used when TriggerType is set to DigitalEdge. The default valu

### Edge

Gets or sets the active edge for the Conditional Jump Trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalEdge](nationalinstruments-modularinstruments-nidigital-digitaledge.html) Edge { get; set; }

#### Returns

The active edge for the Conditional Jump Trigger. This property is used when [TriggerType](nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger-triggertype.html) is set to [DigitalEdge](nationalinstruments-modularinstruments-nidigital-triggertype.html). The default value is [Rising](nationalinstruments-modularinstruments-nidigital-digitaledge.html).

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for Edge is invalid. |

Parent topic:

DigitalEdgeConditionalJumpTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger.html language=enus -->
## TOPIC 00028: DigitalEdgeConditionalJumpTrigger Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaledgeconditionaljumptrigger.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods to configure and control a conditional jump trigger as a digital edge conditional jump trigger. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalEdgeConditionalJumpTrigger : DigitalSubObjectThread SafetyA

### DigitalEdgeConditionalJumpTrigger Class

Contains properties and methods to configure and control a conditional jump trigger as a digital edge conditional jump trigger.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalEdgeConditionalJumpTrigger : DigitalSubObject

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Edge | Gets or sets the active edge for the Conditional Jump Trigger. |
| Source | Gets or sets the source terminal for the Conditional Jump Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(string, DigitalEdge) | Configures the TriggerType to Software, and configures the DigitalEdge and Edge properties. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaledgestarttrigger-edge.html language=enus -->
## TOPIC 00029: Edge

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaledgestarttrigger-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaledgestarttrigger-edge.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the active edge for the start trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalEdge Edge { get; set; }ReturnsThe active edge for the start trigger. This property is used when TriggerType is set to DigitalEdge. The default value is Rising. Exception

### Edge

Gets or sets the active edge for the start trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalEdge](nationalinstruments-modularinstruments-nidigital-digitaledge.html) Edge { get; set; }

#### Returns

The active edge for the start trigger. This property is used when [TriggerType](nationalinstruments-modularinstruments-nidigital-digitalstarttrigger-triggertype.html) is set to [DigitalEdge](nationalinstruments-modularinstruments-nidigital-triggertype.html). The default value is [Rising](nationalinstruments-modularinstruments-nidigital-digitaledge.html).

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for Edge is invalid. |

Parent topic:

DigitalEdgeStartTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalevent.html language=enus -->
## TOPIC 00030: DigitalEvent Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalevent.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains functionality for configuring events. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalEvent : DigitalSubObjectThread SafetyAll members of this type are safe for multithreaded operations.PropertiesNameDescriptionPatternOpcodeEv

### DigitalEvent Class

Contains functionality for configuring events.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalEvent : DigitalSubObject

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| PatternOpcodeEvents | Gets the DigitalPatternOpcodeEvent objects used to configure and control pattern opcode events. |
| RIOEvents | Gets the DigitalRIOEvent objects used to configure and control RIO events. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalfirstfailurehistoryramtrigger-configure__int.html language=enus -->
## TOPIC 00031: Configure(int)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalfirstfailurehistoryramtrigger-configure__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalfirstfailurehistoryramtrigger-configure__int.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the TriggerType to FirstFailure and configures PretriggerSamples. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Configure(int pretriggerSamples)ParametersNameTypeDescriptionpretriggerSamplesintThe number of samples to acquire before the DigitalHistoryRamTrig

### Configure(int)

Configures the [TriggerType](nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-triggertype.html) to [FirstFailure](nationalinstruments-modularinstruments-nidigital-historyramtriggertype.html) and configures [PretriggerSamples](nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-pretriggersamples.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Configure(int pretriggerSamples)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pretriggerSamples | int | The number of samples to acquire before the DigitalHistoryRamTrigger. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for pretriggerSamples is invalid. |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | Configure was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalFirstFailureHistoryRamTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalfrequencycounter-ishysteresisenabled.html language=enus -->
## TOPIC 00032: IsHysteresisEnabled

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalfrequencycounter-ishysteresisenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalfrequencycounter-ishysteresisenabled.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether frequency counter measurement hysteresis should be enabled. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool IsHysteresisEnabled { get; set; }RemarksHysteresis is available only when MeasurementMode is set to parallel. ReturnsThe de

### IsHysteresisEnabled

Gets or sets a value indicating whether frequency counter measurement hysteresis should be enabled.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool IsHysteresisEnabled { get; set; }

#### Remarks

Note

Hysteresis is available only when [MeasurementMode](nationalinstruments-modularinstruments-nidigital-digitalfrequencycounter-measurementmode.html) is set to parallel.

#### Returns

The default value is true. If true, the frequency counter uses hysteresis when measuring.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | IsHysteresisEnabled was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalFrequencyCounter Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryram-fetchcycleinformation__string-digitalpinset-long-long.html language=enus -->
## TOPIC 00033: FetchCycleInformation(string, DigitalPinSet, long, long)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryram-fetchcycleinformation__string-digitalpinset-long-long.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryram-fetchcycleinformation__string-digitalpinset-long-long.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the pattern information acquired for the specified History RAM samples. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalHistoryRamCycleInformation[] FetchCycleInformation(string site, DigitalPinSet pinSet, long position, long samplesToRead)Remarks - or - The po

### FetchCycleInformation(string, DigitalPinSet, long, long)

Fetches the pattern information acquired for the specified History RAM samples.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalHistoryRamCycleInformation](nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation.html)[] FetchCycleInformation(string site, DigitalPinSet pinSet, long position, long samplesToRead)

#### Remarks

- or -

The position or the number of samples to read exceeded the number of samples available.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| site | string | The site to query. |
| pinSet | DigitalPinSet | The set of pins or channels for which to fetch pattern information. |
| position | long | The position from which to start fetching pattern information. |
| samplesToRead | long | The number of samples to read. Use -1 to fetch all samples. |

#### Returns

An array of cycle information specified by [DigitalHistoryRamCycleInformation](nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation.html) that provides pattern information for the specified History RAM samples.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |
| System.InvalidOperationException | The pinSet contains a system pin. |
| Ivi.Driver.OperationPendingException | The specified operation cannot be performed during a pattern burst. |
| System.ArgumentException | The value for site is invalid. The value for position is invalid. The value for samplesToRead is invalid. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | FetchCycleInformation(string, DigitalPinSet, long, long) was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalHistoryRam Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-actualpinstates.html language=enus -->
## TOPIC 00034: ActualPinStates

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-actualpinstates.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-actualpinstates.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pin state acquired by History RAM in the order specified in pinList. Pins without defined edges in the specified DUT cycle will return NotAPinState. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic PinState[][] ActualPinStates { get; }RemarksThe first dimension is the

### ActualPinStates

Gets the pin state acquired by History RAM in the order specified in pinList. Pins without defined edges in the specified DUT cycle will return NotAPinState.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [PinState](nationalinstruments-modularinstruments-nidigital-pinstate.html)[][] ActualPinStates { get; }

#### Remarks

The first dimension is the DUT cycle index and the second dimension is the actual pin states. Only the first row will have actual pin states if the edge multiplier is 1. If the edge multiplier is greater than one, additional rows will be populated.

#### Returns

Actual pin states for the cycle information.

Parent topic:

DigitalHistoryRamCycleInformation Data Structure

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-cyclenumber.html language=enus -->
## TOPIC 00035: CycleNumber

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-cyclenumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-cyclenumber.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic long CycleNumber { get; }ReturnsCycle number for the cycle information.

### CycleNumber

Gets the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public long CycleNumber { get; }

#### Returns

Cycle number for the cycle information.

Parent topic:

DigitalHistoryRamCycleInformation Data Structure

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-perpinpassfail.html language=enus -->
## TOPIC 00036: PerPinPassFail

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-perpinpassfail.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-perpinpassfail.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pass fail information for pins in the order specified in pinList. Pins without defined edges in a DUT cycle will return pass (True). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool[][] PerPinPassFail { get; }RemarksThe first dimension is the DUT cycle index and

### PerPinPassFail

Gets the pass fail information for pins in the order specified in pinList. Pins without defined edges in a DUT cycle will return pass (True).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool[][] PerPinPassFail { get; }

#### Remarks

The first dimension is the DUT cycle index and the second dimension is the per pin pass fail. Only the first row will have per pin pass fail values if the edge multiplier is 1. If the edge multiplier is greater than one, additional rows will be populated.

#### Returns

Per pin pass fail for the cycle information.

Parent topic:

DigitalHistoryRamCycleInformation Data Structure

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-timesetname.html language=enus -->
## TOPIC 00037: TimeSetName

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-timesetname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation-timesetname.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time set for the acquired cycle. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string TimeSetName { get; }ReturnsTimeSet name for the cycle information.

### TimeSetName

Gets the time set for the acquired cycle.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string TimeSetName { get; }

#### Returns

TimeSet name for the cycle information.

Parent topic:

DigitalHistoryRamCycleInformation Data Structure

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation.html language=enus -->
## TOPIC 00038: DigitalHistoryRamCycleInformation Data Structure

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramcycleinformation.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a cycle acquired from History RAM. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic struct DigitalHistoryRamCycleInformationRemarksTo acquire cycle information from History RAM, call FetchCycleInformation(string, DigitalPinSet, long, long)- or - Fetc

### DigitalHistoryRamCycleInformation Data Structure

Represents a cycle acquired from History RAM.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public struct DigitalHistoryRamCycleInformation

#### Remarks

To acquire cycle information from History RAM, call [FetchCycleInformation(string, DigitalPinSet, long, long)](nationalinstruments-modularinstruments-nidigital-digitalhistoryram-fetchcycleinformation__string-digitalpinset-long-long.html)

- or -

[FetchCycleInformation(string, string, long, long)](nationalinstruments-modularinstruments-nidigital-digitalhistoryram-fetchcycleinformation__string-string-long-long.html).

#### Properties

| Name | Description |
| --- | --- |
| ActualPinStates | Gets the pin state acquired by History RAM in the order specified in pinList. Pins without defined edges in the specified DUT cycle will return NotAPinState. |
| CycleNumber | Gets the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst. |
| ExpectedPinStates | Gets the pin state as expected by the loaded pattern in the order specified in pinList. Pins without defined edges in the specified DUT cycle will return NotAPinState. |
| PatternName | Gets the pattern name for the acquired cycle. |
| PerPinPassFail | Gets the pass fail information for pins in the order specified in pinList. Pins without defined edges in a DUT cycle will return pass (True). |
| TimeSetName | Gets the time set for the acquired cycle. |
| VectorNumber | Gets the vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-patternlabel.html language=enus -->
## TOPIC 00039: PatternLabel

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-patternlabel.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-patternlabel.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalPatternLabelHistoryRamTrigger object used to configure the History RAM trigger as a pattern label History RAM trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalPatternLabelHistoryRamTrigger PatternLabel { get; }ReturnsObject used to configure and

### PatternLabel

Gets the [DigitalPatternLabelHistoryRamTrigger](nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger.html) object used to configure the History RAM trigger as a pattern label History RAM trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalPatternLabelHistoryRamTrigger](nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger.html) PatternLabel { get; }

#### Returns

Object used to configure and control the History RAM trigger as a pattern label History RAM trigger. This object is created when the [DigitalHistoryRamTrigger](nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger.html) object is created.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | PatternLabel was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalHistoryRamTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-pretriggersamples.html language=enus -->
## TOPIC 00040: PretriggerSamples

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-pretriggersamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-pretriggersamples.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of samples to acquire before the History RAM trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic int PretriggerSamples { get; set; }ReturnsThe number of samples to acquire before the History RAM trigger. The default value is 0. ExceptionsTypeDescr

### PretriggerSamples

Gets or sets the number of samples to acquire before the History RAM trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public int PretriggerSamples { get; set; }

#### Returns

The number of samples to acquire before the History RAM trigger. The default value is 0.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for PretriggerSamples is invalid. |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | PretriggerSamples was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalHistoryRamTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-triggertype.html language=enus -->
## TOPIC 00041: TriggerType

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-triggertype.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the trigger type of the DigitalHistoryRamTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic HistoryRamTriggerType TriggerType { get; set; }RemarksThe digital pattern instrument waits for this trigger after you initiate a pattern burst and does not acquire p

### TriggerType

Gets or sets the trigger type of the [DigitalHistoryRamTrigger](nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [HistoryRamTriggerType](nationalinstruments-modularinstruments-nidigital-historyramtriggertype.html) TriggerType { get; set; }

#### Remarks

The digital pattern instrument waits for this trigger after you initiate a pattern burst and does not acquire pattern information until it receives this trigger.

#### Returns

The trigger type of the [DigitalHistoryRamTrigger](nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger.html). The default value is [FirstFailure](nationalinstruments-modularinstruments-nidigital-historyramtriggertype.html).

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for TriggerType is invalid. |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | TriggerType was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalHistoryRamTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger.html language=enus -->
## TOPIC 00042: DigitalHistoryRamTrigger Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides configuration and controls for History RAM triggers that affect when to acquire pattern information. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalHistoryRamTrigger : DigitalSubObjectRemarksExample applications are located i

### DigitalHistoryRamTrigger Class

Provides configuration and controls for History RAM triggers that affect when to acquire pattern information.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalHistoryRamTrigger : DigitalSubObject

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory or in the **Start** menu at **National Instruments » NI Digital Pattern Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| CycleNumber | Gets the DigitalCycleNumberHistoryRamTrigger object used to configure the History RAM trigger as a cycle number History RAM trigger. |
| FirstFailure | Gets the DigitalFirstFailureHistoryRamTrigger object used to configure the History RAM trigger as a first failure History RAM trigger. |
| PatternLabel | Gets the DigitalPatternLabelHistoryRamTrigger object used to configure the History RAM trigger as a pattern label History RAM trigger. |
| PretriggerSamples | Gets or sets the number of samples to acquire before the History RAM trigger. |
| TriggerType | Gets or sets the trigger type of the DigitalHistoryRamTrigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitallevels-configurevoltagelevels__double-double-double-double-double.html language=enus -->
## TOPIC 00043: ConfigureVoltageLevels(double, double, double, double, double)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitallevels-configurevoltagelevels__double-double-double-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitallevels-configurevoltagelevels__double-double-double-double-double.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the high and low logic levels for voltage as well as the termination mode input voltage. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigureVoltageLevels(double vil, double vih, double vol, double voh, double vterm)RemarksThese voltages apply to the pin

### ConfigureVoltageLevels(double, double, double, double, double)

Configures the high and low logic levels for voltage as well as the termination mode input voltage.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigureVoltageLevels(double vil, double vih, double vol, double voh, double vterm)

#### Remarks

These voltages apply to the pin set when the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-selectedfunction.html) is [Digital](nationalinstruments-modularinstruments-nidigital-selectedfunction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| vil | double | The voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic low (0). |
| vih | double | The voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1). |
| vol | double | The output voltage below which the comparator on the pin driver interprets a logic low (L). |
| voh | double | The output voltage above which the comparator on the pin driver interprets a logic high (H). |
| vterm | double | The termination voltage the instrument applies during non-drive cycles when the termination mode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for vil is invalid. The value for vih is invalid. The value for vol is invalid. The value for voh is invalid. |
| System.ArgumentException | The value for vterm is invalid. |

Parent topic:

DigitalLevels Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitallevels-terminationmode.html language=enus -->
## TOPIC 00044: TerminationMode

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitallevels-terminationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitallevels-terminationmode.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the behavior of the pin when pin driver is in a non-drive cycle. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic TerminationMode TerminationMode { get; set; }RemarksThe TerminationMode of a pin or list of pins only affects the pin or pins when the SelectedFunctio

### TerminationMode

Gets or sets the behavior of the pin when pin driver is in a non-drive cycle.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [TerminationMode](nationalinstruments-modularinstruments-nidigital-terminationmode.html) TerminationMode { get; set; }

#### Remarks

The [TerminationMode](nationalinstruments-modularinstruments-nidigital-terminationmode.html) of a pin or list of pins only affects the pin or pins when the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-selectedfunction.html) of one or more pins is set to [Digital](nationalinstruments-modularinstruments-nidigital-selectedfunction.html).

#### Returns

The behavior of the pin when the driver is not driving a 0 or 1. The default value is [HighZ](nationalinstruments-modularinstruments-nidigital-terminationmode.html).

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for TerminationMode is invalid. |

Parent topic:

DigitalLevels Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitallevels-voh.html language=enus -->
## TOPIC 00045: Voh

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitallevels-voh.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitallevels-voh.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic double Voh { get; set; }RemarksThis property is only applicable if SelectedFunction is set to Digital fo

### Voh

Gets or sets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public double Voh { get; set; }

#### Remarks

This property is only applicable if [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) is set to [Digital](nationalinstruments-modularinstruments-nidigital-selectedfunction.html) for the pin set.

#### Returns

The output voltage for a logic high input. The default value is 1.7.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for Voh is invalid. |

Parent topic:

DigitalLevels Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitallevels-vol.html language=enus -->
## TOPIC 00046: Vol

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitallevels-vol.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitallevels-vol.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic double Vol { get; set; }RemarksThis property is only applicable if SelectedFunction is set to Digital for

### Vol

Gets or sets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public double Vol { get; set; }

#### Remarks

This property is only applicable if [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) is set to [Digital](nationalinstruments-modularinstruments-nidigital-selectedfunction.html) for the pin set.

#### Returns

The maximum output voltage for a logic low output. The default value is 1.6.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for Vol is invalid. |

Parent topic:

DigitalLevels Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitallevels.html language=enus -->
## TOPIC 00047: DigitalLevels Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitallevels.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitallevels.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents all the current and voltage levels applicable to pattern bursting. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalLevels : DigitalSubObjectRemarksThese voltages and currents apply to the pin set when the SelectedFunction is

### DigitalLevels Class

Represents all the current and voltage levels applicable to pattern bursting.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalLevels : DigitalSubObject

#### Remarks

SelectedFunction

Digital

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory or in the **Start** menu at **National Instruments » NI Digital Pattern Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Ioh | Gets or sets the current that the DUT sources to the active load while outputting a voltage above Vcom. |
| Iol | Gets or sets the current that the DUT sinks from the active load while outputting a voltage below Vcom. |
| TerminationMode | Gets or sets the behavior of the pin when pin driver is in a non-drive cycle. |
| Vcom | Gets or sets the commutating voltage at which the active load circuit switches between between sourcing current and sinking current. |
| Vih | Gets or sets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic high (1). |
| Vil | Gets or sets the input voltage that the digital pattern instrument applies to the input of the DUT when the test instrument drives a logic low (0). |
| Voh | Gets or sets the output voltage from the DUT above which the comparator on the test instrument interprets a logic high (H). |
| Vol | Gets or sets the output voltage from the DUT below which the comparator on the test instrument interprets a logic low (L). |
| Vterm | Gets or sets the termination voltage the instrument applies during non-drive cycles when the TerminationMode is set to Vterm. The instrument applies the termination voltage through a 50 Ω parallel termination resistance. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureActiveLoadLevels(double, double, double) | Configures the Ioh, Iol, and Vcom values. |
| ConfigureVoltageLevels(double, double, double, double, double) | Configures the high and low logic levels for voltage as well as the termination mode input voltage. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-configurepatternburstsites__string.html language=enus -->
## TOPIC 00048: ConfigurePatternBurstSites(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-configurepatternburstsites__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-configurepatternburstsites__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures which sites will be burst on the next call of Initiate. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigurePatternBurstSites(string siteList)RemarksThe sites enabled for pattern burst can also be modified through the siteList parameter in BurstPattern(st

### ConfigurePatternBurstSites(string)

Configures which sites will be burst on the next call of [Initiate](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-initiate.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigurePatternBurstSites(string siteList)

#### Remarks

The sites enabled for pattern burst can also be modified through the *siteList* parameter in [BurstPattern(string, string, bool, TimeSpan)](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-burstpattern__string-string-bool-timespan.html). If a site has been disabled through the [DisableSites](nationalinstruments-modularinstruments-nidigital-nidigital-disablesites__string.html), the site does not burst a pattern even if included in pattern burst sites.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| siteList | string | The comma-delimited list of strings of the form of siteN, where N is the site number to include in the list of pattern burst sites. If the string is empty, all sites are configured for pattern bursting. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The value for siteList contains an invalid site. |

Parent topic:

DigitalPatternControl Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-iskeepaliveactive.html language=enus -->
## TOPIC 00049: IsKeepAliveActive

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-iskeepaliveactive.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-iskeepaliveactive.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the instrument is driving a keep alive pattern. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool IsKeepAliveActive { get; }RemarksFor more information, refer to the Keep Alive Patterns topic of the Digital Pattern Help. Returnstrue, if

### IsKeepAliveActive

Gets a value that indicates whether the instrument is driving a keep alive pattern.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool IsKeepAliveActive { get; }

#### Remarks

For more information, refer to the [Keep Alive Patterns](/csh?context=niDigital_digipat_keep-alive-patterns) topic of the *Digital Pattern Help*.

#### Returns

true, if the instrument is driving a keep alive pattern; otherwise, false.

Parent topic:

DigitalPatternControl Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-readsequencerflag__string.html language=enus -->
## TOPIC 00050: ReadSequencerFlag(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-readsequencerflag__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-readsequencerflag__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the System.Boolean state of a pattern sequencer flag. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool ReadSequencerFlag(string flag)RemarksUse pattern sequencer flags to coordinate execution between the pattern sequencer and a run-time test program. ParametersNameT

### ReadSequencerFlag(string)

Reads the System.Boolean state of a pattern sequencer flag.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool ReadSequencerFlag(string flag)

#### Remarks

Use pattern sequencer flags to coordinate execution between the pattern sequencer and a run-time test program.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| flag | string | The name of the pattern sequencer flag to read. Possible values include "<tt>seqflag0</tt>", "<tt>seqflag1</tt>", "<tt>seqflag2</tt>", or "<tt>seqflag3</tt>". |

#### Returns

The state of the specified pattern sequencer flag.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The value for flag is invalid. |

Parent topic:

DigitalPatternControl Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-startlabel.html language=enus -->
## TOPIC 00051: StartLabel

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-startlabel.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-startlabel.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the pattern name or exported pattern label from which to start bursting the pattern. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string StartLabel { get; set; }ReturnsThe start label used when bursting a pattern. ExceptionsTypeDescriptionSystem.ArgumentExcept

### StartLabel

Gets or sets the pattern name or exported pattern label from which to start bursting the pattern.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string StartLabel { get; set; }

#### Returns

The start label used when bursting a pattern.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The value for StartLabel is invalid. |

Parent topic:

DigitalPatternControl Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-writesequencerflag__string-bool.html language=enus -->
## TOPIC 00052: WriteSequencerFlag(string, bool)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-writesequencerflag__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-writesequencerflag__string-bool.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a System.Boolean value to a pattern sequencer flag. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void WriteSequencerFlag(string flag, bool value)RemarksUse pattern sequencer flags to coordinate execution between the pattern sequencer and a run-time test program. Par

### WriteSequencerFlag(string, bool)

Writes a System.Boolean value to a pattern sequencer flag.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void WriteSequencerFlag(string flag, bool value)

#### Remarks

Use pattern sequencer flags to coordinate execution between the pattern sequencer and a run-time test program.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| flag | string | The name of the pattern sequencer flag to which you would like to write the specified value. Possible values include "<tt>seqflag0</tt>", "<tt>seqflag1</tt>", "<tt>seqflag2</tt>", or "<tt>seqflag3</tt>". |
| value | bool | The state to assign to the specified pattern sequencer flag. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The value for flag is invalid. |

Parent topic:

DigitalPatternControl Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger-cycleoffset.html language=enus -->
## TOPIC 00053: CycleOffset

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger-cycleoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger-cycleoffset.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of cycles following the pattern label specified by Label and vector offset specified by VectorOffset where History RAM will start acquiring pattern information. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic long CycleOffset { get; set; }ReturnsThe cy

### CycleOffset

Gets or sets the number of cycles following the pattern label specified by [Label](nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger-label.html) and vector offset specified by [VectorOffset](nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger-vectoroffset.html) where History RAM will start acquiring pattern information.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public long CycleOffset { get; set; }

#### Returns

The cycle offset specified by CycleOffset following the pattern label specified by [Label](nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger-label.html) and vector offset specified by [VectorOffset](nationalinstruments-modularinstruments-nidigital-digitalpatternlabelhistoryramtrigger-vectoroffset.html) for the [DigitalHistoryRamTrigger](nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger.html). This property is used when [TriggerType](nationalinstruments-modularinstruments-nidigital-digitalhistoryramtrigger-triggertype.html) is set to [PatternLabel](nationalinstruments-modularinstruments-nidigital-historyramtriggertype.html). The default value is 0.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | CycleOffset was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalPatternLabelHistoryRamTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpatternopcodeevent-terminalname.html language=enus -->
## TOPIC 00054: TerminalName

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpatternopcodeevent-terminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpatternopcodeevent-terminalname.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the terminal name of the DigitalPatternOpcodeEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string TerminalName { get; }RemarksYou can use this terminal name as an input signal source for another trigger. ReturnsThe terminal name of the Digita

### TerminalName

Gets a string containing the terminal name of the [DigitalPatternOpcodeEvent](nationalinstruments-modularinstruments-nidigital-digitalpatternopcodeevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string TerminalName { get; }

#### Remarks

You can use this terminal name as an input signal source for another trigger.

#### Returns

The terminal name of the [DigitalPatternOpcodeEvent](nationalinstruments-modularinstruments-nidigital-digitalpatternopcodeevent.html).

Parent topic:

DigitalPatternOpcodeEvent Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpatternopcodeevent.html language=enus -->
## TOPIC 00055: DigitalPatternOpcodeEvent Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpatternopcodeevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpatternopcodeevent.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides configuration and controls for pattern opcode events. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalPatternOpcodeEvent : DigitalSubObjectThread SafetyAll members of this type are safe for multithreaded operations.PropertiesN

### DigitalPatternOpcodeEvent Class

Provides configuration and controls for pattern opcode events.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalPatternOpcodeEvent : DigitalSubObject

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| OutputTerminal | Gets or sets the destination terminal for exporting the DigitalPatternOpcodeEvent. |
| TerminalName | Gets a string containing the terminal name of the DigitalPatternOpcodeEvent. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-createchannelmap__int.html language=enus -->
## TOPIC 00056: CreateChannelMap(int)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-createchannelmap__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-createchannelmap__int.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a channel map, which translates the pin maps and sites to the instrument channels. You must create the pin map using CreatePinMap before calling this method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void CreateChannelMap(int numberOfSites)RemarksUse this method

### CreateChannelMap(int)

Creates a channel map, which translates the pin maps and sites to the instrument channels. You must create the pin map using [CreatePinMap](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-createpinmap__string_arr1-string_arr1.html) before calling this method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void CreateChannelMap(int numberOfSites)

#### Remarks

Use this method if you are not loading a pin map file using [LoadPinMap](nationalinstruments-modularinstruments-nidigital-nidigital-loadpinmap__string.html).

You cannot modify the channel map within an instrument session after you load patterns or waveforms on the digital pattern instrument.

After calling this method, you can create channel map connections using [MapPinToChannel](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-mappintochannel__string-int-string.html). You must call [EndChannelMap](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-endchannelmap.html) to finish creating a channel map.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSites | int | Number of sites in the channel map. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The value for numberOfSites is invalid. |
| System.InvalidOperationException | The channel map has already been configured. The channel map configuration is not complete. |

Parent topic:

DigitalPinAndChannelMap Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-endchannelmap.html language=enus -->
## TOPIC 00057: EndChannelMap()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-endchannelmap.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-endchannelmap.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Completes the channel map configuration. No further changes can be made to the channel map or connections after calling this method. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void EndChannelMap()RemarksCall this method to indicate that the channel map configuration is c

### EndChannelMap()

Completes the channel map configuration. No further changes can be made to the channel map or connections after calling this method.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void EndChannelMap()

#### Remarks

Call this method to indicate that the channel map configuration is complete after you create channel map connections using [MapPinToChannel](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-mappintochannel__string-int-string.html).

You must use [CreateChannelMap](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-createchannelmap__int.html) to begin creating a channel map, and you must call EndChannelMap to finalize the creation of that channel map.

#### Exceptions

| Type | Description |
| --- | --- |
| System.InvalidOperationException | EndChannelMap is called before calling CreateChannelMap. |

Parent topic:

DigitalPinAndChannelMap Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-mappintochannel__string-int-string.html language=enus -->
## TOPIC 00058: MapPinToChannel(string, int, string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-mappintochannel__string-int-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-mappintochannel__string-int-string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Maps a pin to a digital pattern instrument channel. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void MapPinToChannel(string pin, int site, string channel)RemarksThis does not affect the pin and channel map files. For a DUT pin, call this method once for each site. For sys

### MapPinToChannel(string, int, string)

Maps a pin to a digital pattern instrument channel.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void MapPinToChannel(string pin, int site, string channel)

#### Remarks

This does not affect the pin and channel map files.

For a DUT pin, call this method once for each site. For system pins, call this method only once per pin because the method ignores the *site*  parameter for system pins. You must call [CreateChannelMap](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-createchannelmap__int.html) before you call this method, and call [EndChannelMap](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-endchannelmap.html) after creating all connections.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pin | string | The name of the pin. |
| site | int | The index of the site of the pin to map. This parameter is ignored if the specified pin is a system pin. |
| channel | string | The name of the channel. Specify channel names using the channel number, for example, "0" or "31." To specify channels used in multi-instrument sessions, use the form PXI1Slot2/0 or PXI1Slot2/31. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The value for pin is not a valid pin name. The value for channel is not a valid channel name. |
| System.ArgumentException | The value for site is invalid. |

Parent topic:

DigitalPinAndChannelMap Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap.html language=enus -->
## TOPIC 00059: DigitalPinAndChannelMap Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods to configure NIDigital pin and channel maps. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalPinAndChannelMap : DigitalSubObjectRemarksUse this class to programatically create pins and map them to channels. Example app

### DigitalPinAndChannelMap Class

Provides methods to configure [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) pin and channel maps.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalPinAndChannelMap : DigitalSubObject

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory or in the **Start** menu at **National Instruments » NI Digital Pattern Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Methods

| Name | Description |
| --- | --- |
| CreateChannelMap(int) | Creates a channel map, which translates the pin maps and sites to the instrument channels. You must create the pin map using CreatePinMap before calling this method. |
| CreatePinGroup(string, string[]) | Creates a pin group with the specified name. The pin group serves as an alias for a list of pins. |
| CreatePinMap(string[], string[]) | Creates and loads a pin map. Use this method if you are not loading a pin map file using LoadPinMap. |
| EndChannelMap() | Completes the channel map configuration. No further changes can be made to the channel map or connections after calling this method. |
| GetPinSet(string) | Returns a DigitalPinSet object representing a set of either channels or pins. |
| MapPinToChannel(string, int, string) | Maps a pin to a digital pattern instrument channel. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpininformation-gethashcode.html language=enus -->
## TOPIC 00060: GetHashCode()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpininformation-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpininformation-gethashcode.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the hash code for this instance. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic override int GetHashCode()ReturnsA 32-bit signed integer that is the hash code for this instance.

### GetHashCode()

Gets the hash code for this instance.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public override int GetHashCode()

#### Returns

A 32-bit signed integer that is the hash code for this instance.

Parent topic:

DigitalPinInformation Data Structure

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpininformation-pinname.html language=enus -->
## TOPIC 00061: PinName

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpininformation-pinname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpininformation-pinname.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pin name. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string PinName { get; set; }ReturnsThe pin name.

### PinName

Gets the pin name.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string PinName { get; set; }

#### Returns

The pin name.

Parent topic:

DigitalPinInformation Data Structure

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinset-applytdroffsets__precisiontimespan_arr1.html language=enus -->
## TOPIC 00062: ApplyTdrOffsets(PrecisionTimeSpan[])

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinset-applytdroffsets__precisiontimespan_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinset-applytdroffsets__precisiontimespan_arr1.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies the correction for propagation delay offsets to a digital pattern instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ApplyTdrOffsets(PrecisionTimeSpan[] offsets)RemarksUse this method to apply TDR offsets that are stored from a past measurement or are me

### ApplyTdrOffsets(PrecisionTimeSpan[])

Applies the correction for propagation delay offsets to a digital pattern instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ApplyTdrOffsets(PrecisionTimeSpan[] offsets)

#### Remarks

Use this method to apply TDR offsets that are stored from a past measurement or are measured by means other than [Tdr](nationalinstruments-modularinstruments-nidigital-digitalpinset-tdr__bool.html). Also use this method to apply correction for offsets if the apply offsets input of the [Tdr](nationalinstruments-modularinstruments-nidigital-digitalpinset-tdr__bool.html) was set to false at the time of measurement.

For more information, refer to [TDR](/csh?context=niDigital_digipat6570_tdr) in the *Digital Pattern Help*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| offsets | PrecisionTimeSpan[] | The Time-Domain Reflectometry (TDR) offsets to write to the digital pattern instrument. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalPinSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinset-digitallevels.html language=enus -->
## TOPIC 00063: DigitalLevels

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinset-digitallevels.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinset-digitallevels.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalLevels object containing the properties used to set the levels when the SelectedFunction for this pin set is Digital. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalLevels DigitalLevels { get; }ReturnsThis object contains the properties used to set the

### DigitalLevels

Gets the [DigitalLevels](nationalinstruments-modularinstruments-nidigital-digitallevels.html) object containing the properties used to set the levels when the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-selectedfunction.html) for this pin set is [Digital](nationalinstruments-modularinstruments-nidigital-selectedfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalLevels](nationalinstruments-modularinstruments-nidigital-digitallevels.html) DigitalLevels { get; }

#### Returns

This object contains the properties used to set the levels when the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) is set to [Digital](nationalinstruments-modularinstruments-nidigital-selectedfunction.html). This object is created when the [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html) is created.

Parent topic:

DigitalPinSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinset-frequencycounter.html language=enus -->
## TOPIC 00064: FrequencyCounter

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinset-frequencycounter.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinset-frequencycounter.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalFrequencyCounter object containing the properties used to measure the frequency and set the measurement time and mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalFrequencyCounter FrequencyCounter { get; }RemarksYou can use this property to begin me

### FrequencyCounter

Gets the [DigitalFrequencyCounter](nationalinstruments-modularinstruments-nidigital-digitalfrequencycounter.html) object containing the properties used to measure the frequency and set the measurement time and mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalFrequencyCounter](nationalinstruments-modularinstruments-nidigital-digitalfrequencycounter.html) FrequencyCounter { get; }

#### Remarks

You can use this property to begin measuring frequency.

#### Returns

Object used to configure and control the frequency counter. This object is created when the [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html) is created.

Parent topic:

DigitalPinSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinset-getfailcount.html language=enus -->
## TOPIC 00065: GetFailCount()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinset-getfailcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinset-getfailcount.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the comparison fail count for each of the pins specified in the DigitalPinSet. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic long[] GetFailCount()ReturnsArray of fail comparison results per pin. If a site is disabled or not enabled for burst no data will be returned fo

### GetFailCount()

Gets the comparison fail count for each of the pins specified in the [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public long[] GetFailCount()

#### Returns

Array of fail comparison results per pin. If a site is disabled or not enabled for burst no data will be returned for that site.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalPinSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinset-maskcompare.html language=enus -->
## TOPIC 00066: MaskCompare

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinset-maskcompare.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinset-maskcompare.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the pattern comparisons are masked or not. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool MaskCompare { get; set; }ReturnsWhen set to true, failures on pins specified in the DigitalPinSet will be masked. When set to false, failures will not be masked.

### MaskCompare

Specifies whether the pattern comparisons are masked or not.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool MaskCompare { get; set; }

#### Returns

When set to true, failures on pins specified in the [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html) will be masked. When set to false, failures will not be masked. The default value is false.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | DigitalPinSet was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

DigitalPinSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinset-ppmu.html language=enus -->
## TOPIC 00067: Ppmu

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinset-ppmu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinset-ppmu.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalPpmu object containing the properties used to set the PPMU voltage and current levels, aperture time, and output function when the SelectedFunction for this pin set is Ppmu. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalPpmu Ppmu { get; }RemarksYou ca

### Ppmu

Gets the [DigitalPpmu](nationalinstruments-modularinstruments-nidigital-digitalppmu.html) object containing the properties used to set the PPMU voltage and current levels, aperture time, and output function when the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) for this pin set is [Ppmu](nationalinstruments-modularinstruments-nidigital-selectedfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalPpmu](nationalinstruments-modularinstruments-nidigital-digitalppmu.html) Ppmu { get; }

#### Remarks

You can use this property to begin sourcing or measuring current and voltage.

#### Returns

Object used to configure and control PPMU. This object is created when the [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html) is created.

Parent topic:

DigitalPinSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalpinset-readstatic.html language=enus -->
## TOPIC 00068: ReadStatic()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalpinset-readstatic.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalpinset-readstatic.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the current state of comparators for the specified channels or pins. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic PinState[] ReadStatic()RemarksIf there are any changes to DigitalLevels or TerminationMode that have not yet been committed, this method commits them pri

### ReadStatic()

Reads the current state of comparators for the specified channels or pins.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [PinState](nationalinstruments-modularinstruments-nidigital-pinstate.html)[] ReadStatic()

#### Remarks

If there are any changes to [DigitalLevels](nationalinstruments-modularinstruments-nidigital-digitalpinset-digitallevels.html) or [TerminationMode](nationalinstruments-modularinstruments-nidigital-digitallevels-terminationmode.html) that have not yet been committed, this method commits them prior to reading.

#### Returns

An array of digital states in the order specified by the *pinSetString* parameter specified when this [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html) object was created using [GetPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-getpinset__string.html). If a site is disabled, the method does not return data for that site. Use NationalInstruments.ModularInstruments.NIDigital.DigitalDriverUtility.SortPinResultsBySite(NIDigital[], string, byte[][], out string[], out int[]) to order and combine the data to match the channel list. You can also use [GetPinResultsPinInformation(string)](nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getpinresultspininformation__string.html) to obtain a sorted list of returned sites and channels.

Possible values are a logic low pin state ([L](nationalinstruments-modularinstruments-nidigital-pinstate.html)), a logic high pin state ([H](nationalinstruments-modularinstruments-nidigital-pinstate.html)), a midband pin state ([M](nationalinstruments-modularinstruments-nidigital-pinstate.html)), or a value that is above Voh and below Vol, which can occur when you set Vol higher than Voh (V).

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalPinSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalppmu-dccurrent.html language=enus -->
## TOPIC 00069: DCCurrent

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalppmu-dccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalppmu-dccurrent.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalSourceDCCurrent object containing the configuration for a PPMU for which the OutputFunction is DCCurrent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalSourceDCCurrent DCCurrent { get; }ReturnsThe object containing the configuration for a PPMU for whi

### DCCurrent

Gets the [DigitalSourceDCCurrent](nationalinstruments-modularinstruments-nidigital-digitalsourcedccurrent.html) object containing the configuration for a PPMU for which the [OutputFunction](nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html) is [DCCurrent](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalSourceDCCurrent](nationalinstruments-modularinstruments-nidigital-digitalsourcedccurrent.html) DCCurrent { get; }

#### Returns

The object containing the configuration for a PPMU for which the [OutputFunction](nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html) is [DCCurrent](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html). This object is created when the [DigitalPpmu](nationalinstruments-modularinstruments-nidigital-digitalppmu.html) is created.

Parent topic:

DigitalPpmu Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalppmu-dcvoltage.html language=enus -->
## TOPIC 00070: DCVoltage

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalppmu-dcvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalppmu-dcvoltage.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalSourceDCVoltage object containing the configuration for a PPMU for which the OutputFunction is DCVoltage. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalSourceDCVoltage DCVoltage { get; }ReturnsThe object containing the configuration for a PPMU for whi

### DCVoltage

Gets the [DigitalSourceDCVoltage](nationalinstruments-modularinstruments-nidigital-digitalsourcedcvoltage.html) object containing the configuration for a PPMU for which the [OutputFunction](nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html) is [DCVoltage](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalSourceDCVoltage](nationalinstruments-modularinstruments-nidigital-digitalsourcedcvoltage.html) DCVoltage { get; }

#### Returns

The object containing the configuration for a PPMU for which the [OutputFunction](nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html) is [DCVoltage](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html). This object is created when the [DigitalPpmu](nationalinstruments-modularinstruments-nidigital-digitalppmu.html) is created.

Parent topic:

DigitalPpmu Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalppmu-measure__ppmumeasurementtype.html language=enus -->
## TOPIC 00071: Measure(PpmuMeasurementType)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalppmu-measure__ppmumeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalppmu-measure__ppmumeasurementtype.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Instructs the PPMU to measure voltage or current. You can call this method to take a voltage measurement even if SelectedFunction is not set to Ppmu. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic double[] Measure(PpmuMeasurementType measurementType)RemarksThe method returns

### Measure(PpmuMeasurementType)

Instructs the PPMU to measure voltage or current. You can call this method to take a voltage measurement even if [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) is not set to [Ppmu](nationalinstruments-modularinstruments-nidigital-selectedfunction.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public double[] Measure(PpmuMeasurementType measurementType)

#### Remarks

The method returns site numbers in the same order as values read using [BurstPattern(string, string, bool, TimeSpan)](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-burstpattern__string-string-bool-timespan.html), [GetSitePassFail](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-getsitepassfail__string.html), and [Fetch](nationalinstruments-modularinstruments-nidigital-digitalcapturewaveforms-fetch__string-string-int-timespan-ref.html). Use this method to match values those methods return with site numbers.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measurementType | PpmuMeasurementType | The type of measurement: Voltage or Current. |

#### Returns

The measurements taken, ordered according to the *pinSetString* parameter used when calling [GetPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-getpinset__string.html) to create the pin set. If a site is disabled, the method does not return data for that site. Use NationalInstruments.ModularInstruments.NIDigital.DigitalDriverUtility.SortPinResultsBySite(NIDigital[], string, double[][], out string[], out int[]) to order and combine the data to match the channel list. You can also use [GetPinResultsPinInformation(string)](nationalinstruments-modularinstruments-nidigital-digitaldriverutility-getpinresultspininformation__string.html) to obtain a sorted list of returned sites and channels.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| System.ArgumentException | The value for measurementType is invalid. |

Parent topic:

DigitalPpmu Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html language=enus -->
## TOPIC 00072: OutputFunction

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the PPMU sources DC voltage or DC current. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic PpmuOutputFunction OutputFunction { get; set; }RemarksThis property is only applicable if the SelectedFunction of the pin set is set to Ppmu. Changing this property

### OutputFunction

Gets or sets whether the PPMU sources DC voltage or DC current.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [PpmuOutputFunction](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html) OutputFunction { get; set; }

#### Remarks

This property is only applicable if the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) of the pin set is set to [Ppmu](nationalinstruments-modularinstruments-nidigital-selectedfunction.html).

Changing this property does not take effect until you call [Source](nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html). You must call [Source](nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html) to commit your changes even if the PPMU is already sourcing.

#### Returns

The output of the PPMU as either DC voltage or DC current. The default value is [DCVoltage](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html).

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for OutputFunction is invalid. |

Parent topic:

DigitalPpmu Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html language=enus -->
## TOPIC 00073: Source()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts the sourcing voltage or current from the PPMU. This method automatically selects the Ppmu function. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Source()RemarksAll changes to the PPMU source settings do not take effect until this method is called. If you modify

### Source()

Starts the sourcing voltage or current from the PPMU. This method automatically selects the [Ppmu](nationalinstruments-modularinstruments-nidigital-selectedfunction.html) function.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Source()

#### Remarks

All changes to the PPMU source settings do not take effect until this method is called. If you modify source settings after you call this method, you must call this method again for changes in the configuration to take effect.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalPpmu Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalppmu.html language=enus -->
## TOPIC 00074: DigitalPpmu Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalppmu.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalppmu.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures current and voltage levels that the PPMU outputs to or measures from the DUT. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalPpmu : DigitalSubObjectRemarksUse this class to set aperture time, output function, and voltage an

### DigitalPpmu Class

Configures current and voltage levels that the PPMU outputs to or measures from the DUT.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalPpmu : DigitalSubObject

#### Remarks

Use this class to set aperture time, output function, and voltage and current levels for the PPMU. You can also use this class to initiate sourcing or measuring from the PPMU.

Refer to [Pin Parametric Measurement Unit (PPMU)](/csh?context=niDigital_digipat6570_ppmu-overview) for more information on using the PPMU.

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory or in the **Start** menu at **National Instruments » NI Digital Pattern Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AllowExtendedVoltageRange | Gets or sets whether the instrument is allowed to operate in the extended voltage range where instrument specifications may differ from standard ranges. |
| ApertureTime | Gets the measurement aperture time for the PPMU. |
| ApertureTimeUnits | Gets the units of the measurement aperture time. |
| DCCurrent | Gets the DigitalSourceDCCurrent object containing the configuration for a PPMU for which the OutputFunction is DCCurrent. |
| DCVoltage | Gets the DigitalSourceDCVoltage object containing the configuration for a PPMU for which the OutputFunction is DCVoltage. |
| OutputFunction | Gets or sets whether the PPMU sources DC voltage or DC current. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureApertureTime(double, PpmuApertureTimeUnits) | Sets the aperture time for the PPMU measurement. |
| Measure(PpmuMeasurementType) | Instructs the PPMU to measure voltage or current. You can call this method to take a voltage measurement even if SelectedFunction is not set to Ppmu. |
| Source() | Starts the sourcing voltage or current from the PPMU. This method automatically selects the Ppmu function. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalrioevent-outputterminal.html language=enus -->
## TOPIC 00075: OutputTerminal

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalrioevent-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalrioevent-outputterminal.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination terminal for exporting the DigitalRIOEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string OutputTerminal { get; set; }RemarksYou can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal i

### OutputTerminal

Gets or sets the destination terminal for exporting the [DigitalRIOEvent](nationalinstruments-modularinstruments-nidigital-digitalrioevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string OutputTerminal { get; set; }

#### Remarks

You can specify terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

#### Returns

The destination terminal for exporting the [DigitalRIOEvent](nationalinstruments-modularinstruments-nidigital-digitalrioevent.html). The default value is "".

Parent topic:

DigitalRIOEvent Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalrioevent-terminalname.html language=enus -->
## TOPIC 00076: TerminalName

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalrioevent-terminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalrioevent-terminalname.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the terminal name of the DigitalRIOEvent. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string TerminalName { get; }RemarksYou can use this terminal name as an input signal source for another trigger. ReturnsThe terminal name of the DigitalRIOEvent.

### TerminalName

Gets a string containing the terminal name of the [DigitalRIOEvent](nationalinstruments-modularinstruments-nidigital-digitalrioevent.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string TerminalName { get; }

#### Remarks

You can use this terminal name as an input signal source for another trigger.

#### Returns

The terminal name of the [DigitalRIOEvent](nationalinstruments-modularinstruments-nidigital-digitalrioevent.html).

Parent topic:

DigitalRIOEvent Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalrioevent.html language=enus -->
## TOPIC 00077: DigitalRIOEvent Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalrioevent.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalrioevent.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides configuration and controls for RIO events. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalRIOEvent : DigitalSubObjectThread SafetyAll members of this type are safe for multithreaded operations.PropertiesNameDescriptionOutputT

### DigitalRIOEvent Class

Provides configuration and controls for RIO events.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalRIOEvent : DigitalSubObject

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| OutputTerminal | Gets or sets the destination terminal for exporting the DigitalRIOEvent. |
| TerminalName | Gets a string containing the terminal name of the DigitalRIOEvent. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalriotrigger-digitaledge.html language=enus -->
## TOPIC 00078: DigitalEdge

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalriotrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalriotrigger-digitaledge.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalEdgeRIOTrigger object used to configure and control the RIO Trigger as a digital edge RIO trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalEdgeRIOTrigger DigitalEdge { get; }ReturnsObject used to configure and control the RIO Trigger as a digita

### DigitalEdge

Gets the [DigitalEdgeRIOTrigger](nationalinstruments-modularinstruments-nidigital-digitaledgeriotrigger.html) object used to configure and control the RIO Trigger as a digital edge RIO trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalEdgeRIOTrigger](nationalinstruments-modularinstruments-nidigital-digitaledgeriotrigger.html) DigitalEdge { get; }

#### Returns

Object used to configure and control the RIO Trigger as a digital edge RIO trigger. This object is created when this [DigitalRIOTrigger](nationalinstruments-modularinstruments-nidigital-digitalriotrigger.html) object is created.

Parent topic:

DigitalRIOTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalriotrigger-disable.html language=enus -->
## TOPIC 00079: Disable()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalriotrigger-disable.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalriotrigger-disable.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables a previously configured RIO trigger and sets TriggerType to None. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Disable()

### Disable()

Disables a previously configured RIO trigger and sets [TriggerType](nationalinstruments-modularinstruments-nidigital-digitalriotrigger-triggertype.html) to [None](nationalinstruments-modularinstruments-nidigital-triggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Disable()

Parent topic:

DigitalRIOTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalriotrigger-terminalname.html language=enus -->
## TOPIC 00080: TerminalName

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalriotrigger-terminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalriotrigger-terminalname.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the terminal name of the DigitalRIOTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string TerminalName { get; }RemarksYou can use this terminal name as an input signal source for another trigger. ReturnsThe terminal name of the DigitalRIOTrig

### TerminalName

Gets a string containing the terminal name of the [DigitalRIOTrigger](nationalinstruments-modularinstruments-nidigital-digitalriotrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string TerminalName { get; }

#### Remarks

You can use this terminal name as an input signal source for another trigger.

#### Returns

The terminal name of the [DigitalRIOTrigger](nationalinstruments-modularinstruments-nidigital-digitalriotrigger.html).

Parent topic:

DigitalRIOTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalriotrigger-triggertype.html language=enus -->
## TOPIC 00081: TriggerType

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalriotrigger-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalriotrigger-triggertype.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the trigger type of the DigitalRIOTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic TriggerType TriggerType { get; set; }ReturnsThe trigger type of the DigitalRIOTrigger. The default value is None. ExceptionsTypeDescriptionIvi.Driver.OutOfRangeExceptionThe

### TriggerType

Gets or sets the trigger type of the [DigitalRIOTrigger](nationalinstruments-modularinstruments-nidigital-digitalriotrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [TriggerType](nationalinstruments-modularinstruments-nidigital-triggertype.html) TriggerType { get; set; }

#### Returns

The trigger type of the [DigitalRIOTrigger](nationalinstruments-modularinstruments-nidigital-digitalriotrigger.html). The default value is [None](nationalinstruments-modularinstruments-nidigital-triggertype.html).

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for TriggerType is invalid. |

Parent topic:

DigitalRIOTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalriotrigger.html language=enus -->
## TOPIC 00082: DigitalRIOTrigger Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalriotrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalriotrigger.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides configuration and controls for RIO triggers. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalRIOTrigger : DigitalSubObjectThread SafetyAll members of this type are safe for multithreaded operations.PropertiesNameDescriptionDig

### DigitalRIOTrigger Class

Provides configuration and controls for RIO triggers.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalRIOTrigger : DigitalSubObject

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DigitalEdgeRIOTrigger object used to configure and control the RIO Trigger as a digital edge RIO trigger. |
| TerminalName | Gets a string containing the terminal name of the DigitalRIOTrigger. |
| TriggerType | Gets or sets the trigger type of the DigitalRIOTrigger. |

#### Methods

| Name | Description |
| --- | --- |
| Disable() | Disables a previously configured RIO trigger and sets TriggerType to None. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsequencerflagtrigger-terminalname.html language=enus -->
## TOPIC 00083: TerminalName

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsequencerflagtrigger-terminalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsequencerflagtrigger-terminalname.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a string containing the terminal name of the DigitalSequencerFlagTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string TerminalName { get; }RemarksYou can use this terminal name as an input signal source for another trigger. ReturnsThe terminal name of the Digi

### TerminalName

Gets a string containing the terminal name of the [DigitalSequencerFlagTrigger](nationalinstruments-modularinstruments-nidigital-digitalsequencerflagtrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string TerminalName { get; }

#### Remarks

You can use this terminal name as an input signal source for another trigger.

#### Returns

The terminal name of the [DigitalSequencerFlagTrigger](nationalinstruments-modularinstruments-nidigital-digitalsequencerflagtrigger.html).

Parent topic:

DigitalSequencerFlagTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsequencerflagtrigger.html language=enus -->
## TOPIC 00084: DigitalSequencerFlagTrigger Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsequencerflagtrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsequencerflagtrigger.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides the configuration for the sequencer flag trigger. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalSequencerFlagTrigger : DigitalSubObjectThread SafetyAll members of this type are safe for multithreaded operations.PropertiesNam

### DigitalSequencerFlagTrigger Class

Provides the configuration for the sequencer flag trigger.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalSequencerFlagTrigger : DigitalSubObject

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| TerminalName | Gets a string containing the terminal name of the DigitalSequencerFlagTrigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger-configure.html language=enus -->
## TOPIC 00085: Configure()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger-configure.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger-configure.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the TriggerType for Software triggering. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Configure()RemarksUse Send to send the Software Trigger to the digital pattern instrument.

### Configure()

Configures the [TriggerType](nationalinstruments-modularinstruments-nidigital-digitalconditionaljumptrigger-triggertype.html) for [Software](nationalinstruments-modularinstruments-nidigital-triggertype.html) triggering.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Configure()

#### Remarks

Use [Send](nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger-send.html) to send the Software Trigger to the digital pattern instrument.

Parent topic:

DigitalSoftwareConditionalJumpTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger-send.html language=enus -->
## TOPIC 00086: Send()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger-send.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger-send.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the Software Conditional Jump Trigger to a digital pattern instrument, forcing the Conditional Jump Trigger to assert, regardless of how the Conditional Jump Trigger is configured. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Send()

### Send()

Sends the Software Conditional Jump Trigger to a digital pattern instrument, forcing the Conditional Jump Trigger to assert, regardless of how the Conditional Jump Trigger is configured.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Send()

Parent topic:

DigitalSoftwareConditionalJumpTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger.html language=enus -->
## TOPIC 00087: DigitalSoftwareConditionalJumpTrigger Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsoftwareconditionaljumptrigger.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods to configure and control a conditional jump trigger for software triggering. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalSoftwareConditionalJumpTrigger : DigitalSubObjectThread SafetyAll members of t

### DigitalSoftwareConditionalJumpTrigger Class

Contains properties and methods to configure and control a conditional jump trigger for software triggering.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalSoftwareConditionalJumpTrigger : DigitalSubObject

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Methods

| Name | Description |
| --- | --- |
| Configure() | Configures the TriggerType for Software triggering. |
| Send() | Sends the Software Conditional Jump Trigger to a digital pattern instrument, forcing the Conditional Jump Trigger to assert, regardless of how the Conditional Jump Trigger is configured. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsoftwarestarttrigger-configure.html language=enus -->
## TOPIC 00088: Configure()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsoftwarestarttrigger-configure.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsoftwarestarttrigger-configure.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the TriggerType for Software triggering. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Configure()RemarksThe digital pattern instrument waits for a software trigger after you call Initiate or you burst a pattern, and does not burst a pattern until it receive

### Configure()

Configures the [TriggerType](nationalinstruments-modularinstruments-nidigital-digitalstarttrigger-triggertype.html) for [Software](nationalinstruments-modularinstruments-nidigital-triggertype.html) triggering.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Configure()

#### Remarks

The digital pattern instrument waits for a software trigger after you call [Initiate](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-initiate.html) or you burst a pattern, and does not burst a pattern until it receives the trigger. Use [Send](nationalinstruments-modularinstruments-nidigital-digitalsoftwarestarttrigger-send.html) to send the software trigger to the digital pattern instrument.

Parent topic:

DigitalSoftwareStartTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsoftwarestarttrigger-send.html language=enus -->
## TOPIC 00089: Send()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsoftwarestarttrigger-send.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsoftwarestarttrigger-send.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends the software start trigger to a digital pattern instrument, forcing the start trigger to assert, regardless of how the start trigger is configured. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Send()

### Send()

Sends the software start trigger to a digital pattern instrument, forcing the start trigger to assert, regardless of how the start trigger is configured.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Send()

Parent topic:

DigitalSoftwareStartTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsourcedccurrent-configurevoltagelimits__double-double.html language=enus -->
## TOPIC 00090: ConfigureVoltageLimits(double, double)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsourcedccurrent-configurevoltagelimits__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsourcedccurrent-configurevoltagelimits__double-double.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage limit high, or high clamp voltage (Vch), and voltage limit low, or low clamp voltage (Vcl) for the pin set when forcing current. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigureVoltageLimits(double voltageLimitLow, double voltageLimitHigh)R

### ConfigureVoltageLimits(double, double)

Specifies the voltage limit high, or high clamp voltage (Vch), and voltage limit low, or low clamp voltage (Vcl) for the pin set when forcing current.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigureVoltageLimits(double voltageLimitLow, double voltageLimitHigh)

#### Remarks

The upper and lower voltage limits apply when you set the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) of the pin set to [Ppmu](nationalinstruments-modularinstruments-nidigital-selectedfunction.html).

When forcing current by setting the PPMU [OutputFunction](nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html) to [DCCurrent](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html), the voltage is clamped to the specified voltage limits. Select the smallest voltage limits appropriate for the DUT.

If the voltage required by the DUT exceeds the specified voltage limits, the current output may not meet the specified current level. Choose larger voltage limits as needed and appropriate for the DUT.

Changing this property does not take affect until you call [Source](nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html). You can call [Source](nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html) to commit your changes even if the PPMU is already sourcing.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| voltageLimitLow | double | The nominal voltage at the pin at which the low side voltage clamp activates when the PPMU forces current to the DUT. |
| voltageLimitHigh | double | The nominal voltage at the pin at which the high side voltage clamp activates when the PPMU forces current to the DUT. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for voltageLimitLow is invalid. The value for voltageLimitHigh is invalid. |

Parent topic:

DigitalSourceDCCurrent Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsourcedccurrent-currentlevel.html language=enus -->
## TOPIC 00091: CurrentLevel

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsourcedccurrent-currentlevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsourcedccurrent-currentlevel.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the current level, in amps, that the PPMU forces to the DUT. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic double CurrentLevel { get; set; }RemarksThis property is only applicable when you set the SelectedFunction of the pin set to Ppmu and set the PPMU OutputF

### CurrentLevel

Gets or sets the current level, in amps, that the PPMU forces to the DUT.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public double CurrentLevel { get; set; }

#### Remarks

This property is only applicable when you set the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) of the pin set to [Ppmu](nationalinstruments-modularinstruments-nidigital-selectedfunction.html) and set the PPMU [OutputFunction](nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html) to [DCCurrent](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html).

Changing this property does not take affect until you call [Source](nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html). You can call [Source](nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html) to commit your changes even if the PPMU is already sourcing.

#### Returns

The current level, in amps, forced to the DUT. The default value is 0.0.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for CurrentLevel is invalid. |

Parent topic:

DigitalSourceDCCurrent Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsourcedcvoltage-currentlimitrange.html language=enus -->
## TOPIC 00092: CurrentLimitRange

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsourcedcvoltage-currentlimitrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsourcedcvoltage-currentlimitrange.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic double CurrentLimitRange { get; set; }RemarksThis property is only applicable when you set the SelectedFuncti

### CurrentLimitRange

Gets or sets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public double CurrentLimitRange { get; set; }

#### Remarks

This property is only applicable when you set the [SelectedFunction](nationalinstruments-modularinstruments-nidigital-digitalpinset-selectedfunction.html) of the pin set to [Ppmu](nationalinstruments-modularinstruments-nidigital-selectedfunction.html) and set the PPMU [OutputFunction](nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html) to [DCVoltage](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html).

Changing this property does not take affect until you call [Source](nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html). You can call [Source](nationalinstruments-modularinstruments-nidigital-digitalppmu-source.html) to commit your changes even if the PPMU is already sourcing.

#### Returns

Maximum current in amps that can be set. The default value is 2e-6.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | An instance of DigitalPinSet references a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for CurrentLimitRange is invalid. |

Parent topic:

DigitalSourceDCVoltage Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsourcedcvoltage.html language=enus -->
## TOPIC 00093: DigitalSourceDCVoltage Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsourcedcvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsourcedcvoltage.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a PPMU when the OutputFunction is DCVoltage. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalSourceDCVoltage : DigitalSubObjectRemarksThis class allows you to set the voltage level, current limit range, and current limit for

### DigitalSourceDCVoltage Class

Configures a PPMU when the [OutputFunction](nationalinstruments-modularinstruments-nidigital-digitalppmu-outputfunction.html) is [DCVoltage](nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html).

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalSourceDCVoltage : DigitalSubObject

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory or in the **Start** menu at **National Instruments » NI Digital Pattern Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| CurrentLimit | Gets or sets the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. |
| CurrentLimitBehavior | Gets or sets the current limit behavior, which controls how the output current reacts when the current limit is reached. |
| CurrentLimitRange | Gets or sets the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. |
| IsCurrentLimitSupported | Gets a value indicating whether the instrument supports configuration of a current limit when you set the PPMU OutputFunction to DCVoltage. |
| VoltageLevel | Gets or sets the voltage level, in volts, that the PPMU forces to the DUT. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureCurrentLimit(PpmuCurrentLimitBehavior, double) | Configures the current limit for the pin set when forcing voltage. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalsourcewaveforms-createserial__digitalpinset-string-sourcedatamapping-uint-bitorder.html language=enus -->
## TOPIC 00094: CreateSerial(DigitalPinSet, string, SourceDataMapping, uint, BitOrder)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalsourcewaveforms-createserial__digitalpinset-string-sourcedatamapping-uint-bitorder.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalsourcewaveforms-createserial__digitalpinset-string-sourcedatamapping-uint-bitorder.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the source waveform settings used to source serial waveforms using a specified DigitalPinSet. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void CreateSerial(DigitalPinSet pinSet, string waveformName, SourceDataMapping dataMapping, uint sampleWidth, BitOrder bitOrde

### CreateSerial(DigitalPinSet, string, SourceDataMapping, uint, BitOrder)

Creates the source waveform settings used to source serial waveforms using a specified [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void CreateSerial(DigitalPinSet pinSet, string waveformName, SourceDataMapping dataMapping, uint sampleWidth, BitOrder bitOrder)

#### Remarks

The number of waveforms is limited to 512.

You cannot reconfigure settings after waveforms are created.

For more information, refer to [Opcodes](/csh?context=niDigital_digipat_opcodes) and [Source Waveform Configurations](/csh?context=niDigital_digipat_source-waveform-config) in the *Digital Pattern Help*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSet | DigitalPinSet | The set of pins or channels for which to create the waveform. The pinSet must match the source pins in the pattern that references the waveform. The pin order in the pin set determines the bit positions of the data written using one of the write waveform methods on the DigitalSourceWaveforms object. |
| waveformName | string | The name of the waveform to use in the pattern file. Waveform names must be unique. Use the waveformName with source_start opcode in your pattern. |
| dataMapping | SourceDataMapping | Specifies whether the waveform is broadcast to all sites or a unique waveform is sourced per site. |
| sampleWidth | uint | The width in bits of each serial sample. Valid values are between 1 and 32. |
| bitOrder | BitOrder | The bit order significance. This can be most significant bit first or least significant bit first. MostSignificantBitFirst is the default value. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |
| System.ArgumentException | The value for waveformName is an empty string or contains an invalid character. |
| Ivi.Driver.OutOfRangeException | The value for dataMapping is invalid. The value for sampleWidth is invalid. The value for bitOrder is invalid. The number of waveforms in source memory exceeds maximum number of waveforms allowed. |

Parent topic:

DigitalSourceWaveforms Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalstarttrigger-outputterminal.html language=enus -->
## TOPIC 00095: OutputTerminal

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalstarttrigger-outputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalstarttrigger-outputterminal.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the destination terminal for exporting the start trigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic string OutputTerminal { get; set; }RemarksTerminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is

### OutputTerminal

Gets or sets the destination terminal for exporting the start trigger.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public string OutputTerminal { get; set; }

#### Remarks

Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

#### Returns

The destination terminal for exporting the start trigger. The default value is "".

Parent topic:

DigitalStartTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitalstarttrigger-triggertype.html language=enus -->
## TOPIC 00096: TriggerType

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitalstarttrigger-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitalstarttrigger-triggertype.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the trigger type of the DigitalStartTrigger. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic TriggerType TriggerType { get; set; }RemarksThe digital pattern instrument waits for this trigger after you initiate a pattern burst and does not burst a pattern until th

### TriggerType

Gets or sets the trigger type of the [DigitalStartTrigger](nationalinstruments-modularinstruments-nidigital-digitalstarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [TriggerType](nationalinstruments-modularinstruments-nidigital-triggertype.html) TriggerType { get; set; }

#### Remarks

The digital pattern instrument waits for this trigger after you initiate a pattern burst and does not burst a pattern until this trigger is received.

#### Returns

The trigger type of the [DigitalStartTrigger](nationalinstruments-modularinstruments-nidigital-digitalstarttrigger.html). The default value is [None](nationalinstruments-modularinstruments-nidigital-triggertype.html).

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for TriggerType is invalid. |

Parent topic:

DigitalStartTrigger Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__digitalpinset-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan-pr...d267e593.html language=enus -->
## TOPIC 00097: ConfigureDriveEdges(DigitalPinSet, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__digitalpinset-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan-pr...d267e593.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__digitalpinset-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan-pr...d267e593.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive format and drive edge placement for the specified pin set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigureDriveEdges(DigitalPinSet pinSet, DriveFormat format, PrecisionTimeSpan driveOnEdge, PrecisionTimeSpan driveDataEdge, PrecisionTimeSpan

### ConfigureDriveEdges(DigitalPinSet, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan)

Configures the drive format and drive edge placement for the specified pin set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigureDriveEdges(DigitalPinSet pinSet, DriveFormat format, PrecisionTimeSpan driveOnEdge, PrecisionTimeSpan driveDataEdge, PrecisionTimeSpan driveReturnEdge, PrecisionTimeSpan driveOffEdge, PrecisionTimeSpan driveData2Edge, PrecisionTimeSpan driveReturn2Edge)

#### Remarks

Not all edges apply to all drive formats.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSet | DigitalPinSet | The pin set for which to configure the time set edges. |
| format | DriveFormat | The drive format of the time set. |
| driveOnEdge | PrecisionTimeSpan | The delay from the beginning of the vector period for turning on the pin driver. This option applies only when the prior vector left the pin in a non-drive PinState (L, H, X, V, M, E). For the SurroundByComplement format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven. |
| driveDataEdge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pattern data is driven to the pattern value. The ending state from the previous vector persists until this point. |
| driveReturnEdge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format. |
| driveOffEdge | PrecisionTimeSpan | The delay from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive PinState (L, H, X, V, M, E). |
| driveData2Edge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pattern data is driven to the second pattern value. The ending state from the previous pattern value persists until this point. To use this edge you must specify a second pin state in the pattern and configure an edge multiplier greater than one in the time set. |
| driveReturn2Edge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pin changes from the second pattern data to the return value, as specified in the format. To use this edge, you must specify a second pin state in the pattern and configure an edge multiplier greater than one in the time set. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | An instance of DigitalTimeSet represents a time set name that has not yet been applied. The pinSet contains a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for format is invalid. The value for driveOnEdge is invalid. The value for driveDataEdge is invalid. The value for driveReturnEdge is invalid. The value for driveOffEdge is invalid. The value for driveData2Edge is invalid. The value for driveReturn2Edge is invalid. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__string-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan-precision...d267e757.html language=enus -->
## TOPIC 00098: ConfigureDriveEdges(string, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__string-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan-precision...d267e757.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__string-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan-precision...d267e757.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive format and the drive edge placement for the specified pins. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigureDriveEdges(string pinSetString, DriveFormat format, PrecisionTimeSpan driveOnEdge, PrecisionTimeSpan driveDataEdge, PrecisionTimeSpan

### ConfigureDriveEdges(string, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan)

Configures the drive format and the drive edge placement for the specified pins.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigureDriveEdges(string pinSetString, DriveFormat format, PrecisionTimeSpan driveOnEdge, PrecisionTimeSpan driveDataEdge, PrecisionTimeSpan driveReturnEdge, PrecisionTimeSpan driveOffEdge, PrecisionTimeSpan driveData2Edge, PrecisionTimeSpan driveReturn2Edge)

#### Remarks

Not all edges apply to all drive formats.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSetString | string | The pin set specified as a comma-delimited list of pins for which to configure the time set edges. |
| format | DriveFormat | The drive format of the time set. |
| driveOnEdge | PrecisionTimeSpan | The delay from the beginning of the vector period for turning on the pin driver. This option applies only when the prior vector left the pin in a non-drive PinState (L, H, X, V, M, E). For the SurroundByComplement format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven. |
| driveDataEdge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pattern data is driven to the pattern value. The ending state from the previous vector persists until this point. |
| driveReturnEdge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format. |
| driveOffEdge | PrecisionTimeSpan | The delay from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive PinState (L, H, X, V, M, E). |
| driveData2Edge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pattern data is driven to the second pattern value. The ending state from the previous pattern value persists until this point. To use this edge you must specify a second pin state in the pattern and configure an edge multiplier greater than one in the time set. |
| driveReturn2Edge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pin changes from the second pattern data to the return value, as specified in the format. To use this edge you must specify a second pin state in the pattern and configure an edge multiplier greater than one in the time set. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | An instance of DigitalTimeSet represents a time set name that has not yet been applied. The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for format is invalid. The value for driveOnEdge is invalid. The value for driveDataEdge is invalid. The value for driveReturnEdge is invalid. The value for driveOffEdge is invalid. The value for driveData2Edge is invalid. The value for driveReturn2Edge is invalid. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__string-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan.html language=enus -->
## TOPIC 00099: ConfigureDriveEdges(string, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__string-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveedges__string-driveformat-precisiontimespan-precisiontimespan-precisiontimespan-precisiontimespan.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive format and the drive edge placement for the specified pins. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigureDriveEdges(string pinSetString, DriveFormat format, PrecisionTimeSpan driveOnEdge, PrecisionTimeSpan driveDataEdge, PrecisionTimeSpan

### ConfigureDriveEdges(string, DriveFormat, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan, PrecisionTimeSpan)

Configures the drive format and the drive edge placement for the specified pins.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigureDriveEdges(string pinSetString, DriveFormat format, PrecisionTimeSpan driveOnEdge, PrecisionTimeSpan driveDataEdge, PrecisionTimeSpan driveReturnEdge, PrecisionTimeSpan driveOffEdge)

#### Remarks

Not all edges apply to all drive formats.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSetString | string | The pin set specified as a comma-delimited list of pins for which to configure the time set edges. |
| format | DriveFormat | The drive format of the time set. |
| driveOnEdge | PrecisionTimeSpan | The delay from the beginning of the vector period for turning on the pin driver. This option applies only when the prior vector left the pin in a non-drive PinState (L, H, X, V, M, E). For the SurroundByComplement format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven. |
| driveDataEdge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pattern data is driven to the pattern value. The ending state from the previous vector persists until this point. |
| driveReturnEdge | PrecisionTimeSpan | The delay from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format. |
| driveOffEdge | PrecisionTimeSpan | The delay from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive PinState (L, H, X, V, M, E). |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | An instance of DigitalTimeSet represents a time set name that has not yet been applied. The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for format is invalid. The value for driveOnEdge is invalid. The value for driveDataEdge is invalid. The value for driveReturnEdge is invalid. The value for driveOffEdge is invalid. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveformat__string-driveformat.html language=enus -->
## TOPIC 00100: ConfigureDriveFormat(string, DriveFormat)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveformat__string-driveformat.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-configuredriveformat__string-driveformat.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the drive format of a time set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigureDriveFormat(string pinSetString, DriveFormat driveFormat)ParametersNameTypeDescriptionpinSetStringstringThe pin set specified as a comma-delimited list of pins for which t

### ConfigureDriveFormat(string, DriveFormat)

Configures the drive format of a time set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigureDriveFormat(string pinSetString, DriveFormat driveFormat)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSetString | string | The pin set specified as a comma-delimited list of pins for which to configure the drive format. |
| driveFormat | DriveFormat | The drive format of the time set. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for driveFormat is invalid. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-configureedge__digitalpinset-timesetedge-precisiontimespan.html language=enus -->
## TOPIC 00101: ConfigureEdge(DigitalPinSet, TimeSetEdge, PrecisionTimeSpan)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-configureedge__digitalpinset-timesetedge-precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-configureedge__digitalpinset-timesetedge-precisiontimespan.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the edge of a time set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigureEdge(DigitalPinSet pinSet, TimeSetEdge edge, PrecisionTimeSpan time)ParametersNameTypeDescriptionpinSetDigitalPinSetThe pin set for which to configure the edge. edgeTimeSetEdgeThe

### ConfigureEdge(DigitalPinSet, TimeSetEdge, PrecisionTimeSpan)

Configures the edge of a time set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigureEdge(DigitalPinSet pinSet, TimeSetEdge edge, PrecisionTimeSpan time)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSet | DigitalPinSet | The pin set for which to configure the edge. |
| edge | TimeSetEdge | The edge of the time set to configure. |
| time | PrecisionTimeSpan | The time of the edge to configure. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-configureedgemultiplier__digitalpinset-int.html language=enus -->
## TOPIC 00102: ConfigureEdgeMultiplier(DigitalPinSet, int)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-configureedgemultiplier__digitalpinset-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-configureedgemultiplier__digitalpinset-int.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the edge multiplier of a time set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ConfigureEdgeMultiplier(DigitalPinSet pinSet, int edgeMultiplier)ParametersNameTypeDescriptionpinSetDigitalPinSetThe pin set for which to configure the edge multiplier. edgeMult

### ConfigureEdgeMultiplier(DigitalPinSet, int)

Configures the edge multiplier of a time set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ConfigureEdgeMultiplier(DigitalPinSet pinSet, int edgeMultiplier)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSet | DigitalPinSet | The pin set for which to configure the edge multiplier. |
| edgeMultiplier | int | The edge multiplier of the time set. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |
| Ivi.Driver.OutOfRangeException | The value for edgeMultiplier is invalid. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-getdriveformat__string.html language=enus -->
## TOPIC 00103: GetDriveFormat(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-getdriveformat__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-getdriveformat__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the drive format of a time set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DriveFormat GetDriveFormat(string pinSetString)ParametersNameTypeDescriptionpinSetStringstringThe pin set specified as a comma-delimited list of pins for which to get the drive format. Return

### GetDriveFormat(string)

Gets the drive format of a time set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DriveFormat](nationalinstruments-modularinstruments-nidigital-driveformat.html) GetDriveFormat(string pinSetString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSetString | string | The pin set specified as a comma-delimited list of pins for which to get the drive format. |

#### Returns

The drive format of the time set to get.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-getedge__digitalpinset-timesetedge.html language=enus -->
## TOPIC 00104: GetEdge(DigitalPinSet, TimeSetEdge)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-getedge__digitalpinset-timesetedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-getedge__digitalpinset-timesetedge.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the edge time of a time set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic PrecisionTimeSpan GetEdge(DigitalPinSet pinSet, TimeSetEdge edge)ParametersNameTypeDescriptionpinSetDigitalPinSetThe pin set for which to get the edge. edgeTimeSetEdgeThe edge of the time set to

### GetEdge(DigitalPinSet, TimeSetEdge)

Gets the edge time of a time set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public PrecisionTimeSpan GetEdge(DigitalPinSet pinSet, TimeSetEdge edge)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSet | DigitalPinSet | The pin set for which to get the edge. |
| edge | TimeSetEdge | The edge of the time set to get. |

#### Returns

The time of the edge specified.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The pinSet contains a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-getedgemultiplier__string.html language=enus -->
## TOPIC 00105: GetEdgeMultiplier(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-getedgemultiplier__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-getedgemultiplier__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the edge multiplier of a time set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic int GetEdgeMultiplier(string pinSetString)ParametersNameTypeDescriptionpinSetStringstringThe pin set specified as a comma-delimited list of pins for which to get the edge multiplier. Retur

### GetEdgeMultiplier(string)

Gets the edge multiplier of a time set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public int GetEdgeMultiplier(string pinSetString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| pinSetString | string | The pin set specified as a comma-delimited list of pins for which to get the edge multiplier. |

#### Returns

The edge multiplier of the time set.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.SelectorNameException | The value for pinSetString contains a pin or pin group name not loaded in the pin map. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltimeset-period.html language=enus -->
## TOPIC 00106: Period

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltimeset-period.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltimeset-period.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the period of the time set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic PrecisionTimeSpan Period { get; set; }ReturnsSpecifies the period of the time set in seconds. ExceptionsTypeDescriptionIvi.Driver.OutOfRangeExceptionThe value for the time set period is i

### Period

Gets or sets the period of the time set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public PrecisionTimeSpan Period { get; set; }

#### Returns

Specifies the period of the time set in seconds.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value for the time set period is invalid. |

Parent topic:

DigitalTimeSet Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltiming-absolutedelayenabled.html language=enus -->
## TOPIC 00107: AbsoluteDelayEnabled

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltiming-absolutedelayenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltiming-absolutedelayenabled.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets a value indicating whether Absolute Delay should be applied to the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool AbsoluteDelayEnabled { get; set; }RemarksInstruments with Semiconductor Test System (STS) timing calibration should not enable Abso

### AbsoluteDelayEnabled

Gets or sets a value indicating whether Absolute Delay should be applied to the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool AbsoluteDelayEnabled { get; set; }

#### Remarks

Instruments with Semiconductor Test System (STS) timing calibration should not enable Absolute Delay.

#### Returns

If true, the time delay value specified in Absolute Delay is applied to the instrument; otherwise, Absolute Delay has no effect.

Parent topic:

DigitalTiming Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-digitaltiming.html language=enus -->
## TOPIC 00108: DigitalTiming Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-digitaltiming.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-digitaltiming.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides functionality for creating and getting time sets and adjusting board-level timing. Derives fromDigitalSubObjectSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class DigitalTiming : DigitalSubObjectRemarksUse this class to create a time set and adjust board-level timi

### DigitalTiming Class

Provides functionality for creating and getting time sets and adjusting board-level timing.

#### Derives from

- DigitalSubObject

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class DigitalTiming : DigitalSubObject

#### Remarks

Use this class to create a time set and adjust board-level timing.

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory, or, in the **Start** menu, navigate to **NI Digital Pattern Examples** in the **National Instruments** folder.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AbsoluteDelay | Gets or sets the time delay applied to the instrument in addition to TDR and calibration adjustments. |
| AbsoluteDelayEnabled | Gets or sets a value indicating whether Absolute Delay should be applied to the instrument. |
| TdrEndpointTermination | Gets or sets the endpoint termination used for TDR. |

#### Methods

| Name | Description |
| --- | --- |
| CreateTimeSet(string) | Creates and returns a DigitalTimeSet. Use this method to create time set values after applying a timing sheet with ApplyLevelsAndTiming(string, string, string), or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to ApplyLevelsAndTiming(string, string, string), it only affects the values of the current timing context. |
| DeleteAllTimeSets() | Deletes all loaded and created time sets. |
| GetTimeSet(string) | Returns a DigitalTimeSet specified by a name. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-applylevelsandtiming__string-string-string.html language=enus -->
## TOPIC 00109: ApplyLevelsAndTiming(string, string, string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-applylevelsandtiming__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-applylevelsandtiming__string-string-string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies digital levels and timing defined in the loaded levels and timing sheets. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ApplyLevelsAndTiming(string siteList, string levelsSheet, string timingSheet)RemarksAny levels not specified in the levels sheet remain uncha

### ApplyLevelsAndTiming(string, string, string)

Applies digital levels and timing defined in the loaded levels and timing sheets.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ApplyLevelsAndTiming(string siteList, string levelsSheet, string timingSheet)

#### Remarks

Any levels not specified in the levels sheet remain unchanged.

When applying a timing sheet, all existing time sets are deleted before the new time sets are loaded.

For more information, refer to [Levels](/csh?context=niDigital_digipat_levels) and [Timing](/csh?context=niDigital_digipat_timing) in the *Digital Pattern Help*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| siteList | string | A comma-delimited list of strings of the form siteN, where N is the site number. Passing an empty string specifies all sites. |
| levelsSheet | string | The name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path used in the LoadLevels(string) method. The name of the levels sheet is the file name without the directory and the file extension. |
| timingSheet | string | The name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you used in the LoadTiming(string) method. The name of the timing sheet is the file name without the directory and file extension. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | The specified siteList contains an invalid site. |
| System.InvalidOperationException | The levels sheet specified by levelsSheet is not loaded. The timing sheet specified by timingSheet is not loaded. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-disablesites__string.html language=enus -->
## TOPIC 00110: DisableSites(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-disablesites__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-disablesites__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the specified sites. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void DisableSites(string siteList)RemarksDisabled sites are not included in pattern bursts initiated by the Initiate or BurstPattern(string, string, bool, TimeSpan) methods, even if the site is spec

### DisableSites(string)

Disables the specified sites.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void DisableSites(string siteList)

#### Remarks

Disabled sites are not included in pattern bursts initiated by the [Initiate](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-initiate.html) or [BurstPattern(string, string, bool, TimeSpan)](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol-burstpattern__string-string-bool-timespan.html) methods, even if the site is specified in the list of pattern burst sites. Additionally, if you specify a list of pin or pin group names for a *pinSetString* parameter to an NI-Digital Pattern Driver API method, digital pattern instrument channels mapped to disabled sites are not affected by the method. Methods that return per-pin data, such as the PPMU [Measure](nationalinstruments-modularinstruments-nidigital-digitalppmu-measure__ppmumeasurementtype.html) method, do not return data for channels mapped to disabled sites.

The digital pattern instrument channels mapped to the sites specified are left in their current state.

NI TestStand Semiconductor Module requires all sites to always be enabled and manages the set of active sites without disabling the sites in the digital pattern instrument session. Do not use this method with the Semiconductor Module.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| siteList | string | A comma-delimited list of strings of the form siteN, where N is the site number. All sites are disabled if the string is empty. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | The specified siteList contains an invalid site. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-dispose.html language=enus -->
## TOPIC 00111: Dispose()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-dispose.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disposes the NIDigital session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void Dispose()

### Dispose()

Disposes the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void Dispose()

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-driveroperation.html language=enus -->
## TOPIC 00112: DriverOperation

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-driveroperation.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-driveroperation.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalDriverOperation object containing methods and properties that manage the operation of the driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalDriverOperation DriverOperation { get; }ReturnsThe methods and properties that manage the operation of the

### DriverOperation

Gets the [DigitalDriverOperation](nationalinstruments-modularinstruments-nidigital-digitaldriveroperation.html) object containing methods and properties that manage the operation of the driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalDriverOperation](nationalinstruments-modularinstruments-nidigital-digitaldriveroperation.html) DriverOperation { get; }

#### Returns

The methods and properties that manage the operation of the driver. This object is generated when you create an [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-enablesites__string.html language=enus -->
## TOPIC 00113: EnableSites(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-enablesites__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-enablesites__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the specified sites. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void EnableSites(string siteList)RemarksOperations such as bursting a pattern or sourcing a PPMU apply to enabled sites. NI TestStand Semiconductor Module requires all sites to always be enabled and

### EnableSites(string)

Enables the specified sites.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void EnableSites(string siteList)

#### Remarks

Operations such as bursting a pattern or sourcing a PPMU apply to enabled sites.

NI TestStand Semiconductor Module requires all sites to always be enabled and manages the set of active sites without disabling the sites in the digital pattern instrument session. Do not use this method with the Semiconductor Module.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| siteList | string | A comma-delimited list of strings of the form siteN, where N is the site number. All sites are enabled if the string is empty. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| Ivi.Driver.SelectorNameException | The specified siteList contains an invalid site. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-event.html language=enus -->
## TOPIC 00114: Event

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-event.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-event.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalEvent object that contains the events for the NIDigital session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalEvent Event { get; }ReturnsAn object containing the events for the NIDigital session. This object is generated when you create an NIDigital

### Event

Gets the [DigitalEvent](nationalinstruments-modularinstruments-nidigital-digitalevent.html) object that contains the events for the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalEvent](nationalinstruments-modularinstruments-nidigital-digitalevent.html) Event { get; }

#### Returns

An object containing the events for the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session. This object is generated when you create an [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-exportsignal__signaltype-string-string.html language=enus -->
## TOPIC 00115: ExportSignal(SignalType, string, string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-exportsignal__signaltype-string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-exportsignal__signaltype-string-string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes trigger and event signals to the specified outputTerminal . SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void ExportSignal(SignalType signal, string signalId, string outputTerminal)RemarksFor more information, refer to Opcodes, Triggers and Events, and Signal Routin

### ExportSignal(SignalType, string, string)

Routes trigger and event signals to the specified *outputTerminal* .

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void ExportSignal(SignalType signal, string signalId, string outputTerminal)

#### Remarks

For more information, refer to [Opcodes](/csh?context=niDigital_digipat_opcodes), [Triggers and Events](/csh?context=niDigital_digipat6570_6570-triggers-events), and [Signal Routing](/csh?context=niDigital_digipat6570_signal-routing) in the *Digital Pattern Help*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signal | SignalType | The type of signal to export. |
| signalId | string | The instance of the selected signal to export. Possible values include "<tt>patternOpcodeEvent0</tt>", "<tt>patternOpcodeEvent1</tt>", "<tt>patternOpcodeEvent2</tt>", or "<tt>patternOpcodeEvent3</tt>". |
| outputTerminal | string | The terminal to which to export the signal. Possible values include but are not limited to "<tt>PXI_Trig0</tt>", "<tt>PXI_Trig1</tt>", "<tt>PXI_Trig2</tt>", "<tt>PXI_Trig3</tt>", "<tt>PXI_Trig4</tt>", "<tt>PXI_Trig5</tt>", "<tt>PXI_Trig6</tt>", or "<tt>PXI_Trig7</tt>". |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |
| System.ArgumentException | The value for signal is invalid. The value for signalId is invalid. The value for outputTerminal is invalid. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-getinstrumenthandle.html language=enus -->
## TOPIC 00116: GetInstrumentHandle()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-getinstrumenthandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-getinstrumenthandle.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the System.Runtime.InteropServices.SafeHandle to the NIDigital instrument session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic SafeHandle GetInstrumentHandle()RemarksUsing the System.Runtime.InteropServices.SafeHandle, you can get the System.IntPtr to the session; ho

### GetInstrumentHandle()

Gets the System.Runtime.InteropServices.SafeHandle to the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) instrument session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public SafeHandle GetInstrumentHandle()

#### Remarks

Using the System.Runtime.InteropServices.SafeHandle, you can get the System.IntPtr to the session; however, there are risks involved with using the System.IntPtr. It is difficult to know the state of the handle, and the handle could be recycled while you are using it. For more information, refer to System.Runtime.InteropServices.SafeHandle.DangerousGetHandle.

#### Returns

A System.Runtime.InteropServices.SafeHandle to [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) instrument session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-getservice__type.html language=enus -->
## TOPIC 00117: GetService(Type)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-getservice__type.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-getservice__type.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the service object of the specified type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic object GetService(Type serviceType)ParametersNameTypeDescriptionserviceTypeTypeAn object that specifies the System.Type of the object. ReturnsThe object of System.Type determined by

### GetService(Type)

Gets the service object of the specified type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public object GetService(Type serviceType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| serviceType | Type | An object that specifies the System.Type of the object. |

#### Returns

The object of System.Type determined by *serviceType* .

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-historyram.html language=enus -->
## TOPIC 00118: HistoryRam

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-historyram.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-historyram.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalHistoryRam object containing methods for configuring and fetching History RAM contents. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalHistoryRam HistoryRam { get; }ReturnsThe object that encapsulates the functionality for configuring and fetching Hist

### HistoryRam

Gets the [DigitalHistoryRam](nationalinstruments-modularinstruments-nidigital-digitalhistoryram.html) object containing methods for configuring and fetching History RAM contents.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalHistoryRam](nationalinstruments-modularinstruments-nidigital-digitalhistoryram.html) HistoryRam { get; }

#### Returns

The object that encapsulates the functionality for configuring and fetching History RAM contents. This object is generated when you create a [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

#### Exceptions

| Type | Description |
| --- | --- |
| System.ObjectDisposedException | DigitalHistoryRam was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-identity.html language=enus -->
## TOPIC 00119: Identity

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-identity.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-identity.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalDriverIdentity object, which contains properties that return information about the identity of the NI-Digital Pattern Driver software. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalDriverIdentity Identity { get; }ReturnsThe identity of the NI-Digital

### Identity

Gets the [DigitalDriverIdentity](nationalinstruments-modularinstruments-nidigital-digitaldriveridentity.html) object, which contains properties that return information about the identity of the NI-Digital Pattern Driver software.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalDriverIdentity](nationalinstruments-modularinstruments-nidigital-digitaldriveridentity.html) Identity { get; }

#### Returns

The identity of the NI-Digital Pattern Driver software. This object is generated when you create an [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-isdisposed.html language=enus -->
## TOPIC 00120: IsDisposed

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-isdisposed.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the NIDigital session has been disposed. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool IsDisposed { get; }Returnstrue, if the NIDigital session is disposed; false, if the NIDigital session is not disposed. The default value is false.

### IsDisposed

Gets a value indicating whether the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool IsDisposed { get; }

#### Returns

true, if the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session is disposed; false, if the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session is not disposed. The default value is false.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-issiteenabled__string.html language=enus -->
## TOPIC 00121: IsSiteEnabled(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-issiteenabled__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-issiteenabled__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether the specified site is enabled or disabled. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic bool IsSiteEnabled(string site)ParametersNameTypeDescriptionsitestringThe site to check.Returnstrue, if the site is enabled; false, if the site is disabled.ExceptionsTyp

### IsSiteEnabled(string)

Returns whether the specified site is enabled or disabled.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public bool IsSiteEnabled(string site)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| site | string | The site to check. |

#### Returns

true, if the site is enabled; false, if the site is disabled.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-loadlevels__ienumerable_string..html language=enus -->
## TOPIC 00122: LoadLevels(IEnumerable< string >)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-loadlevels__ienumerable_string..html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-loadlevels__ienumerable_string..html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads levels sheets from a list of pin levels files. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void LoadLevels(IEnumerable< string > filePaths)RemarksIf a levels sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before

### LoadLevels(IEnumerable< string >)

Loads levels sheets from a list of pin levels files.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void LoadLevels(IEnumerable< string > filePaths)

#### Remarks

If a levels sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before calling this method. The formulas are evaluated at load time.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePaths | IEnumerable< string > | The absolute file paths to the pin levels files. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-loadlevels__string.html language=enus -->
## TOPIC 00123: LoadLevels(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-loadlevels__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-loadlevels__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a levels sheet from file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void LoadLevels(string filePath)RemarksIf the levels sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before calling this method. The formulas

### LoadLevels(string)

Loads a levels sheet from file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void LoadLevels(string filePath)

#### Remarks

If the levels sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before calling this method. The formulas are evaluated at load time.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The absolute file path to the pin levels file. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-loadpattern__string.html language=enus -->
## TOPIC 00124: LoadPattern(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-loadpattern__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-loadpattern__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a pattern to the hardware from a pattern file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void LoadPattern(string filePath)ParametersNameTypeDescriptionfilePathstringThe absolute file path to the pattern file. ExceptionsTypeDescriptionIvi.Driver.IviCDriverException

### LoadPattern(string)

Loads a pattern to the hardware from a pattern file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void LoadPattern(string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The absolute file path to the pattern file. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-loadpinmap__string.html language=enus -->
## TOPIC 00125: LoadPinMap(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-loadpinmap__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-loadpinmap__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a pin map file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void LoadPinMap(string filePath)RemarksYou can load only a single pin map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the Reset method. For more inform

### LoadPinMap(string)

Loads a pin map file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void LoadPinMap(string filePath)

#### Remarks

You can load only a single pin map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the [Reset](nationalinstruments-modularinstruments-nidigital-digitaldriverutility-reset.html) method.

For more information on using pin maps, refer to [Pin and Channel Map Editor](/csh?context=niDigital_digipat_pin-channel-map-editor) in the *Digital Pattern Help*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The absolute file path to the pin map file. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-loadspecifications__ienumerable_string..html language=enus -->
## TOPIC 00126: LoadSpecifications(IEnumerable< string >)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-loadspecifications__ienumerable_string..html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-loadspecifications__ienumerable_string..html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads specifications sheets from a list of specifications files. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void LoadSpecifications(IEnumerable< string > filePaths)ParametersNameTypeDescriptionfilePathsIEnumerable< string >The absolute file paths to the specifications fi

### LoadSpecifications(IEnumerable< string >)

Loads specifications sheets from a list of specifications files.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void LoadSpecifications(IEnumerable< string > filePaths)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePaths | IEnumerable< string > | The absolute file paths to the specifications files. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-loadspecifications__string.html language=enus -->
## TOPIC 00127: LoadSpecifications(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-loadspecifications__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-loadspecifications__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a specifications sheet from file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void LoadSpecifications(string filePath)ParametersNameTypeDescriptionfilePathstringThe absolute file path to the specifications file. ExceptionsTypeDescriptionIvi.Driver.IviCDriverExceptio

### LoadSpecifications(string)

Loads a specifications sheet from file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void LoadSpecifications(string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The absolute file path to the specifications file. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-loadtiming__ienumerable_string..html language=enus -->
## TOPIC 00128: LoadTiming(IEnumerable< string >)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-loadtiming__ienumerable_string..html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-loadtiming__ienumerable_string..html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads one or more time sets from a list of timing sheet files. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void LoadTiming(IEnumerable< string > filePaths)RemarksIf a timing sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variab

### LoadTiming(IEnumerable< string >)

Loads one or more time sets from a list of timing sheet files.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void LoadTiming(IEnumerable< string > filePaths)

#### Remarks

If a timing sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before calling this method. The formulas are evaluated at load time.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePaths | IEnumerable< string > | The absolute file paths to the timing sheet files. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-loadtiming__string.html language=enus -->
## TOPIC 00129: LoadTiming(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-loadtiming__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-loadtiming__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads one or more time sets from a timing sheet file. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void LoadTiming(string filePath)RemarksIf the timing sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before calling this

### LoadTiming(string)

Loads one or more time sets from a timing sheet file.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void LoadTiming(string filePath)

#### Remarks

If the timing sheet loaded uses variables, you must load the specifications sheet(s) that define(s) those variables before calling this method. The formulas are evaluated at load time.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The absolute file path to the timing sheet file. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__intptr.html language=enus -->
## TOPIC 00130: NIDigital(IntPtr)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__intptr.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__intptr.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NIDigital class. Initializes an instrument driver session from an existing instrument handle. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic NIDigital(IntPtr instrumentHandle)ParametersNameTypeDescriptioninstrumentHandleIntPtrA pointer to an

### NIDigital(IntPtr)

Initializes a new instance of the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) class. Initializes an instrument driver session from an existing instrument handle.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public NIDigital(IntPtr instrumentHandle)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrumentHandle | IntPtr | A pointer to an existing instrument handle. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__string-bool-bool-string.html language=enus -->
## TOPIC 00131: NIDigital(string, bool, bool, string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__string-bool-bool-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__string-bool-bool-string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NIDigital class. This overload is reserved for future use. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic NIDigital(string resourceName, bool idQuery, bool reset, string optionString)RemarksThe recommended constructor overload is NIDigital(s

### NIDigital(string, bool, bool, string)

Initializes a new instance of the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) class. This overload is reserved for future use.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public NIDigital(string resourceName, bool idQuery, bool reset, string optionString)

#### Remarks

The recommended constructor overload is [NIDigital(string resourceName, bool idQuery, bool reset)](nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__string-bool-bool.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | The resource name assigned by Measurement & Automation Explorer (MAX) to a digital pattern instrument; for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where PXI1Slot2 is one instrument name and PXI1Slot3 is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map. Note: You can only specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and a PXIe-6571. The instruments must be in the same chassis. The resourceName can also be a logical IVI name. |
| idQuery | bool | true to verify that the instrument you initialize is supported by the NI-Digital Pattern Driver. The NI-Digital Pattern Driver performs verification regardless of the value of this parameter. |
| reset | bool | true to reset the digital pattern instrument to a known state when the session is initialized. |
| optionString | string | A list of initial values of certain attributes for the session. Pass String.Empty for the default behavior. You can use the DriverSetup flag to simulate a digital pattern instrument. When simulating a digital pattern instrument, you must specify the model you want to simulate. For example, Simulate = 1, DriverSetup = Model:6570. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__string-bool-bool.html language=enus -->
## TOPIC 00132: NIDigital(string, bool, bool)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__string-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-nidigital__string-bool-bool.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NIDigital class. Initializes a digital pattern instrument driver session and sets the initial state of session properties. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic NIDigital(string resourceName, bool idQuery, bool reset)ParametersNameT

### NIDigital(string, bool, bool)

Initializes a new instance of the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) class. Initializes a digital pattern instrument driver session and sets the initial state of session properties.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public NIDigital(string resourceName, bool idQuery, bool reset)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | The resource name assigned by Measurement & Automation Explorer (MAX) to a digital pattern instrument; for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where PXI1Slot2 is one instrument name and PXI1Slot3 is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map. Note: You can only specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and a PXIe-6571. The instruments must be in the same chassis. The resourceName can also be a logical IVI name. |
| idQuery | bool | true to verify that the instrument you initialize is supported by the NI-Digital Pattern Driver. The NI-Digital Pattern Driver performs verification regardless of the value of this parameter. |
| reset | bool | true to reset the digital pattern instrument to a known state when the session is initialized. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-numberofchannels.html language=enus -->
## TOPIC 00133: NumberOfChannels

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-numberofchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-numberofchannels.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of channels on the digital pattern instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic int NumberOfChannels { get; }ReturnsThe number of channels on the digital pattern instrument. This value depends on the digital pattern instrument for which the sess

### NumberOfChannels

Gets the number of channels on the digital pattern instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public int NumberOfChannels { get; }

#### Returns

The number of channels on the digital pattern instrument. This value depends on the digital pattern instrument for which the session is opened.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-patterncontrol.html language=enus -->
## TOPIC 00134: PatternControl

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-patterncontrol.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-patterncontrol.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalPatternControl control object, containing properties and methods for setting up and bursting a pattern. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalPatternControl PatternControl { get; }ReturnsThe control object containing properties and methods for

### PatternControl

Gets the [DigitalPatternControl](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol.html) control object, containing properties and methods for setting up and bursting a pattern.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalPatternControl](nationalinstruments-modularinstruments-nidigital-digitalpatterncontrol.html) PatternControl { get; }

#### Returns

The control object containing properties and methods for setting up and bursting a pattern. This object is generated when you create an [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-pinandchannelmap.html language=enus -->
## TOPIC 00135: PinAndChannelMap

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-pinandchannelmap.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-pinandchannelmap.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalPinAndChannelMap object that stores all the pin mapping information for the NIDigital session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalPinAndChannelMap PinAndChannelMap { get; }RemarksUse PinAndChannelMap to create DigitalPinSet objects for cont

### PinAndChannelMap

Gets the [DigitalPinAndChannelMap](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap.html) object that stores all the pin mapping information for the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalPinAndChannelMap](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap.html) PinAndChannelMap { get; }

#### Remarks

Use PinAndChannelMap to create [DigitalPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinset.html) objects for controlling pins or channels using [GetPinSet](nationalinstruments-modularinstruments-nidigital-digitalpinandchannelmap-getpinset__string.html).

#### Returns

An object storing all the pin mapping information for the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session. This object is generated when you create an [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-selfcalibrate.html language=enus -->
## TOPIC 00136: SelfCalibrate()

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-selfcalibrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-selfcalibrate.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a self-calibration on a digital pattern instrument. This operation may take several minutes to complete. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void SelfCalibrate()RemarksFor more information on capture functionality, refer to Self-Calibration in the Digital

### SelfCalibrate()

Performs a self-calibration on a digital pattern instrument. This operation may take several minutes to complete.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void SelfCalibrate()

#### Remarks

For more information on capture functionality, refer to [Self-Calibration](/csh?context=niDigital_digipat6570_self-cal) in the *Digital Pattern Help*.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-sourcewaveforms.html language=enus -->
## TOPIC 00137: SourceWaveforms

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-sourcewaveforms.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-sourcewaveforms.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalSourceWaveforms object containing the functionality for creating and writing source waveforms. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalSourceWaveforms SourceWaveforms { get; }RemarksFor more information on source and capture functionality, refer

### SourceWaveforms

Gets the [DigitalSourceWaveforms](nationalinstruments-modularinstruments-nidigital-digitalsourcewaveforms.html) object containing the functionality for creating and writing source waveforms.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalSourceWaveforms](nationalinstruments-modularinstruments-nidigital-digitalsourcewaveforms.html) SourceWaveforms { get; }

#### Remarks

For more information on source and capture functionality, refer to [Source and Capture](/csh?context=niDigital_digipat6570_source-capture) in the *Digital Pattern Help*.

#### Returns

The object encapsulating the functionality for creating, writing, and fetching waveforms. This object is generated when you create an [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-timing.html language=enus -->
## TOPIC 00138: Timing

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-timing.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-timing.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalTiming object that stores the time sets for the NIDigital session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalTiming Timing { get; }ReturnsAn object containing all the time sets for the NIDigital session. This object is generated when you create an

### Timing

Gets the [DigitalTiming](nationalinstruments-modularinstruments-nidigital-digitaltiming.html) object that stores the time sets for the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalTiming](nationalinstruments-modularinstruments-nidigital-digitaltiming.html) Timing { get; }

#### Returns

An object containing all the time sets for the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session. This object is generated when you create an [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-trigger.html language=enus -->
## TOPIC 00139: Trigger

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-trigger.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalTrigger object that contains the triggers for the NIDigital session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalTrigger Trigger { get; }ReturnsAn object containing the triggers for the NIDigital session. This object is generated when you create an

### Trigger

Gets the [DigitalTrigger](nationalinstruments-modularinstruments-nidigital-digitaltrigger.html) object that contains the triggers for the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalTrigger](nationalinstruments-modularinstruments-nidigital-digitaltrigger.html) Trigger { get; }

#### Returns

An object containing the triggers for the [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session. This object is generated when you create an [NIDigital](nationalinstruments-modularinstruments-nidigital-nidigital.html) session.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-unloadallpatterns__bool.html language=enus -->
## TOPIC 00140: UnloadAllPatterns(bool)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-unloadallpatterns__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-unloadallpatterns__bool.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void UnloadAllPatterns(bool unloadKeepAlivePattern)ParametersNameTypeDescriptionunloadKeepAlivePatternboolSpecifies whether to unlo

### UnloadAllPatterns(bool)

Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void UnloadAllPatterns(bool unloadKeepAlivePattern)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| unloadKeepAlivePattern | bool | Specifies whether to unload any loaded keep alive patterns. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The NI-Digital Pattern Driver returned an error. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-unloadspecifications__ienumerable_string..html language=enus -->
## TOPIC 00141: UnloadSpecifications(IEnumerable< string >)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-unloadspecifications__ienumerable_string..html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-unloadspecifications__ienumerable_string..html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unloads the given specifications sheets present in the previously loaded specifications files that you select. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void UnloadSpecifications(IEnumerable< string > filePaths)RemarksYou must call the LoadSpecifications(IEnumerable<str

### UnloadSpecifications(IEnumerable< string >)

Unloads the given specifications sheets present in the previously loaded specifications files that you select.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void UnloadSpecifications(IEnumerable< string > filePaths)

#### Remarks

You must call the [LoadSpecifications(IEnumerable<string>)](nationalinstruments-modularinstruments-nidigital-nidigital-loadspecifications__ienumerable_string..html) method to reload the files with updated specifications values. You must then call the [ApplyLevelsAndTiming(string, string, string)](nationalinstruments-modularinstruments-nidigital-nidigital-applylevelsandtiming__string-string-string.html) method in order to apply the levels and timing values that reference the updated specifications values.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePaths | IEnumerable< string > | The absolute file paths to loaded specifications files. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | UnloadSpecifications(IEnumerable<string>) was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-unloadspecifications__string.html language=enus -->
## TOPIC 00142: UnloadSpecifications(string)

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-unloadspecifications__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-unloadspecifications__string.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unloads the given specifications sheet present in the previously loaded specifications file that you select. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic void UnloadSpecifications(string filePath)RemarksYou must call the LoadSpecifications(string) method to reload the file

### UnloadSpecifications(string)

Unloads the given specifications sheet present in the previously loaded specifications file that you select.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public void UnloadSpecifications(string filePath)

#### Remarks

You must call the [LoadSpecifications(string)](nationalinstruments-modularinstruments-nidigital-nidigital-loadspecifications__string.html) method to reload the file with updated specifications values. You must then call the [ApplyLevelsAndTiming(string, string, string)](nationalinstruments-modularinstruments-nidigital-nidigital-applylevelsandtiming__string-string-string.html) method in order to apply the levels and timing values that reference the updated specifications values.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The absolute file path to a loaded specifications file. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IviCDriverException | The underlying NI-Digital driver returned an error. |
| System.ObjectDisposedException | UnloadSpecifications(string) was accessed after the associated NIDigital or DigitalDriverUtility object was disposed. |

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital-utility.html language=enus -->
## TOPIC 00143: Utility

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital-utility.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital-utility.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalDriverUtility object containing methods providing utility operations for the NI-Digital Pattern Driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic DigitalDriverUtility Utility { get; }ReturnsThe object containing methods providing utility operations for t

### Utility

Gets the [DigitalDriverUtility](nationalinstruments-modularinstruments-nidigital-digitaldriverutility.html) object containing methods providing utility operations for the NI-Digital Pattern Driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public [DigitalDriverUtility](nationalinstruments-modularinstruments-nidigital-digitaldriverutility.html) Utility { get; }

#### Returns

The object containing methods providing utility operations for the NI-Digital Pattern Driver.

Parent topic:

NIDigital Class

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-nidigital.html language=enus -->
## TOPIC 00144: NIDigital Class

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-nidigital.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-nidigital.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a digital pattern instrument session. Derives fromIDisposableIServiceProviderIIviDriverITClockSynchronizableDeviceSyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic class NIDigital : IDisposable, IServiceProvider, IIviDriver, ITClockSynchronizableDeviceRemarksUse this

### NIDigital Class

Represents a digital pattern instrument session.

#### Derives from

- IDisposable
- IServiceProvider
- IIviDriver
- ITClockSynchronizableDevice

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public class NIDigital : IDisposable, IServiceProvider, IIviDriver, ITClockSynchronizableDevice

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-Digital\Examples\DotNET 4.*x* directory or in the **Start** menu at **National Instruments » NI Digital Pattern Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| NIDigital(string, bool, bool, string) | Initializes a new instance of the NIDigital class. This overload is reserved for future use. |
| NIDigital(IntPtr) | Initializes a new instance of the NIDigital class. Initializes an instrument driver session from an existing instrument handle. |
| NIDigital(string, bool, bool) | Initializes a new instance of the NIDigital class. Initializes a digital pattern instrument driver session and sets the initial state of session properties. |

#### Properties

| Name | Description |
| --- | --- |
| CaptureWaveforms | Gets the DigitalCaptureWaveforms object containing methods for creating and fetching capture waveforms. |
| DriverOperation | Gets the DigitalDriverOperation object containing methods and properties that manage the operation of the driver. |
| Event | Gets the DigitalEvent object that contains the events for the NIDigital session. |
| HistoryRam | Gets the DigitalHistoryRam object containing methods for configuring and fetching History RAM contents. |
| Identity | Gets the DigitalDriverIdentity object, which contains properties that return information about the identity of the NI-Digital Pattern Driver software. |
| IsDisposed | Gets a value indicating whether the NIDigital session has been disposed. |
| NumberOfChannels | Gets the number of channels on the digital pattern instrument. |
| PatternControl | Gets the DigitalPatternControl control object, containing properties and methods for setting up and bursting a pattern. |
| PinAndChannelMap | Gets the DigitalPinAndChannelMap object that stores all the pin mapping information for the NIDigital session. |
| SourceWaveforms | Gets the DigitalSourceWaveforms object containing the functionality for creating and writing source waveforms. |
| Timing | Gets the DigitalTiming object that stores the time sets for the NIDigital session. |
| Trigger | Gets the DigitalTrigger object that contains the triggers for the NIDigital session. |
| Utility | Gets the DigitalDriverUtility object containing methods providing utility operations for the NI-Digital Pattern Driver. |

#### Methods

| Name | Description |
| --- | --- |
| ApplyLevelsAndTiming(string, string, string) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
| ApplyLevelsAndTiming(string, string, string, string, string, string) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
| ApplyLevelsAndTiming(string, string, string, DigitalPinSet, DigitalPinSet, DigitalPinSet) | Applies digital levels and timing defined in the loaded levels and timing sheets. |
| Close() | Closes the session with the digital pattern instrument. |
| DisableSites(string) | Disables the specified sites. |
| Dispose() | Disposes the NIDigital session. |
| EnableSites(string) | Enables the specified sites. |
| ExportSignal(SignalType, string, string) | Routes trigger and event signals to the specified outputTerminal . |
| GetInstrumentHandle() | Gets the System.Runtime.InteropServices.SafeHandle to the NIDigital instrument session. |
| GetService(Type) | Gets the service object of the specified type. |
| IsSiteEnabled(string) | Returns whether the specified site is enabled or disabled. |
| LoadLevels(IEnumerable< string >) | Loads levels sheets from a list of pin levels files. |
| LoadLevels(string) | Loads a levels sheet from file. |
| LoadPattern(string) | Loads a pattern to the hardware from a pattern file. |
| LoadPinMap(string) | Loads a pin map file. |
| LoadSpecifications(IEnumerable< string >) | Loads specifications sheets from a list of specifications files. |
| LoadSpecifications(string) | Loads a specifications sheet from file. |
| LoadTiming(IEnumerable< string >) | Loads one or more time sets from a list of timing sheet files. |
| LoadTiming(string) | Loads one or more time sets from a timing sheet file. |
| SelfCalibrate() | Performs a self-calibration on a digital pattern instrument. This operation may take several minutes to complete. |
| UnloadAllPatterns(bool) | Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument. |
| UnloadSpecifications(IEnumerable< string >) | Unloads the given specifications sheets present in the previously loaded specifications files that you select. |
| UnloadSpecifications(string) | Unloads the given specifications sheet present in the previously loaded specifications file that you select. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-pinstate.html language=enus -->
## TOPIC 00145: PinState Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-pinstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-pinstate.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The digital state of the pin. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum PinStateMembersNameValueDescription_00A digital state of 0. This state can be used for WriteStatic. _11A digital state of 1. This state can be used for WriteStatic. L3A digital state of L (low)

### PinState Enumeration

The digital state of the pin.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum PinState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| _0 | 0 | A digital state of 0. This state can be used for WriteStatic. |
| _1 | 1 | A digital state of 1. This state can be used for WriteStatic. |
| L | 3 | A digital state of L (low). This state should not be used with WriteStatic. |
| H | 4 | A digital state of H (high). This state should not be used with WriteStatic. |
| X | 5 | A digital state of X (non-drive state). This state can be used for WriteStatic. |
| M | 6 | A digital state of M (midband). This state should not be used with WriteStatic. |
| V | 7 | A digital state of V (compare high or low, not midband; store results from capture functionality if configured). This state should not be used with WriteStatic. |
| D | 8 | A digital state of D (drive data from source functionality if configured). This state should not be used with WriteStatic. |
| NotAPinState | 254 | Not a pin state is used for non-existent DUT cycles. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-ppmuaperturetimeunits.html language=enus -->
## TOPIC 00146: PpmuApertureTimeUnits Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-ppmuaperturetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-ppmuaperturetimeunits.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit of the aperture time. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum PpmuApertureTimeUnitsMembersNameValueDescriptionSeconds2100Unit in seconds.

### PpmuApertureTimeUnits Enumeration

Specifies the unit of the aperture time.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum PpmuApertureTimeUnits

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Seconds | 2100 | Unit in seconds. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-ppmucurrentlimitbehavior.html language=enus -->
## TOPIC 00147: PpmuCurrentLimitBehavior Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-ppmucurrentlimitbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-ppmucurrentlimitbehavior.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The output current's behavior when the current limit is reached. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum PpmuCurrentLimitBehaviorMembersNameValueDescriptionCurrentRegulate3100Controls output current so that it does not exceed the current limit. Power continues to

### PpmuCurrentLimitBehavior Enumeration

The output current's behavior when the current limit is reached.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum PpmuCurrentLimitBehavior

#### Members

| Name | Value | Description |
| --- | --- | --- |
| CurrentRegulate | 3100 | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-ppmumeasurementtype.html language=enus -->
## TOPIC 00148: PpmuMeasurementType Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-ppmumeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-ppmumeasurementtype.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the PPMU measures voltage or current. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum PpmuMeasurementTypeMembersNameValueDescriptionCurrent2400The PPMU measures current. Voltage2401The PPMU measures voltage.

### PpmuMeasurementType Enumeration

Specifies whether the PPMU measures voltage or current.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum PpmuMeasurementType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Current | 2400 | The PPMU measures current. |
| Voltage | 2401 | The PPMU measures voltage. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html language=enus -->
## TOPIC 00149: PpmuOutputFunction Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-ppmuoutputfunction.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether one or more pins functioning as a PPMU is forcing voltage or current to the DUT. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum PpmuOutputFunctionMembersNameValueDescriptionDCVoltage1300The PPMU forces voltage to the DUT. DCCurrent1301The PPMU forces c

### PpmuOutputFunction Enumeration

Specifies whether one or more pins functioning as a PPMU is forcing voltage or current to the DUT.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum PpmuOutputFunction

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DCVoltage | 1300 | The PPMU forces voltage to the DUT. |
| DCCurrent | 1301 | The PPMU forces current to the DUT. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-selectedfunction.html language=enus -->
## TOPIC 00150: SelectedFunction Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-selectedfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-selectedfunction.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which instrument function controls the pin(s). By default, all pins are set to Disconnect. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum SelectedFunctionMembersNameValueDescriptionDigital1100The pattern sequencer controls the specified pin(s). If a pattern is

### SelectedFunction Enumeration

Specifies which instrument function controls the pin(s). By default, all pins are set to Disconnect.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum SelectedFunction

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Digital | 1100 | The pattern sequencer controls the specified pin(s). If a pattern is currently bursting, the pin immediately switches to bursting the pattern. This option disconnects the PPMU. |
| Ppmu | 1101 | The PPMU controls the specified pin(s) and connects the PPMU. The pin driver is in a non-drive state, and the active load is disabled. The PPMU does not start sourcing or measuring until Source or Measure is called. |
| Off | 1102 | Puts the digital driver in a non-drive state, disables the active load, disconnects the PPMU, and closes the I/O switch connecting the instrument channel. |
| Disconnect | 1103 | The I/O switch connecting the instrument channel is open to the I/O connector. If the PPMU is sourcing, it is stopped prior to opening the I/O switch. |
| Rio | 1104 | Yields control of the specified pin(s) to LabVIEW FPGA. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-signaltype.html language=enus -->
## TOPIC 00151: SignalType Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-signaltype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-signaltype.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of signal to route. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum SignalTypeMembersNameValueDescriptionStartTrigger2000Overrides the start trigger. ConditionalJumpTrigger2001Specifies to route a conditional jump trigger. PatternOpcodeEvent2002Specifi

### SignalType Enumeration

Specifies the type of signal to route.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum SignalType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| StartTrigger | 2000 | Overrides the start trigger. |
| ConditionalJumpTrigger | 2001 | Specifies to route a conditional jump trigger. |
| PatternOpcodeEvent | 2002 | Specifies to route a pattern opcode event signal. |
| RIOEvent | 2004 | Specifies to route a RIO event signal. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-siteresulttype.html language=enus -->
## TOPIC 00152: SiteResultType Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-siteresulttype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-siteresulttype.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The type of data in the results array. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum SiteResultTypeMembersNameValueDescriptionPassFail3300Pass/fail site result. CaptureWaveform3301Capture waveform site result.

### SiteResultType Enumeration

The type of data in the results array.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum SiteResultType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PassFail | 3300 | Pass/fail site result. |
| CaptureWaveform | 3301 | Capture waveform site result. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-sourcedatamapping.html language=enus -->
## TOPIC 00153: SourceDataMapping Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-sourcedatamapping.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-sourcedatamapping.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to map data on multiple sites. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum SourceDataMappingMembersNameValueDescriptionBroadcast2600Broadcasts the waveform you specify to all sites. SiteUnique2601Sources unique waveform data to each site.

### SourceDataMapping Enumeration

Specifies how to map data on multiple sites.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum SourceDataMapping

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Broadcast | 2600 | Broadcasts the waveform you specify to all sites. |
| SiteUnique | 2601 | Sources unique waveform data to each site. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-tdrendpointtermination.html language=enus -->
## TOPIC 00154: TdrEndpointTermination Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-tdrendpointtermination.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-tdrendpointtermination.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether TDR channels are connected to an open circuit or a short to ground. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum TdrEndpointTerminationMembersNameValueDescriptionTdrToOpenCircuit3600TDR channels are connected to an open circuit. TdrToShortToGround360

### TdrEndpointTermination Enumeration

Specifies whether TDR channels are connected to an open circuit or a short to ground.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum TdrEndpointTermination

#### Members

| Name | Value | Description |
| --- | --- | --- |
| TdrToOpenCircuit | 3600 | TDR channels are connected to an open circuit. |
| TdrToShortToGround | 3601 | TDR channels are connected to a short to ground. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-terminationmode.html language=enus -->
## TOPIC 00155: TerminationMode Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-terminationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-terminationmode.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the behavior of one or more pins when the driver is in a non-drive state. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum TerminationModeMembersNameValueDescriptionActiveLoad1200The active load provides a constant current to a commutating voltage (Vcom). Vterm1

### TerminationMode Enumeration

Specifies the behavior of one or more pins when the driver is in a non-drive state.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum TerminationMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveLoad | 1200 | The active load provides a constant current to a commutating voltage (Vcom). |
| Vterm | 1201 | The pin driver drives Vterm. |
| HighZ | 1202 | The pin driver is in a non-drive state (in a high-impedance state) and the active load is disabled. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-timesetedge.html language=enus -->
## TOPIC 00156: TimeSetEdge Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-timesetedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-timesetedge.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the edge of the time set. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum TimeSetEdgeMembersNameValueDescriptionDriveOn2800Specifies the drive on edge of the time set. DriveData2801Specifies the drive data edge of the time set. DriveReturn2802Specifies the driv

### TimeSetEdge Enumeration

Specifies the edge of the time set.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum TimeSetEdge

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DriveOn | 2800 | Specifies the drive on edge of the time set. |
| DriveData | 2801 | Specifies the drive data edge of the time set. |
| DriveReturn | 2802 | Specifies the drive return edge of the time set. |
| DriveOff | 2803 | Specifies the drive off edge of the time set. |
| CompareStrobe | 2804 | Specifies the compare strobe of the time set. |
| DriveData2 | 2805 | Specifies the drive data 2 edge of the time set. |
| DriveReturn2 | 2806 | Specifies the drive return 2 edge of the time set. |
| CompareStrobe2 | 2807 | Specifies the compare strobe 2 of the time set. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital-triggertype.html language=enus -->
## TOPIC 00157: TriggerType Enumeration

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital-triggertype.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start trigger type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDigitalpublic enum TriggerTypeMembersNameValueDescriptionNone1700Disables the start trigger. DigitalEdge1701Digital edge trigger. Software1702Software start trigger.

### TriggerType Enumeration

Specifies the start trigger type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDigital](nationalinstruments-modularinstruments-nidigital.html)

public enum TriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 1700 | Disables the start trigger. |
| DigitalEdge | 1701 | Digital edge trigger. |
| Software | 1702 | Software start trigger. |

Parent topic:

NationalInstruments.ModularInstruments.NIDigital

<!--NI_TOPIC bundle=ni-digital-pattern-csharp-api-ref path=nationalinstruments-modularinstruments-nidigital.html language=enus -->
## TOPIC 00158: NationalInstruments.ModularInstruments.NIDigital

- bundle_id: `ni-digital-pattern-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidigital.html`
- source_url: https://docs-be.ni.com/bundle/ni-digital-pattern-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidigital.html
- document_id: `ni-digital-pattern-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionDigitalCaptureWaveformsProvides operations to create and fetch capture waveforms with the NI-Digital Pattern Driver. DigitalClockGeneratorDrives a free-running clock that runs independently of the digital pattern on the specified pins. DigitalConditionalJumpTriggerProvides conf

### NationalInstruments.ModularInstruments.NIDigital

#### Classes

| Name | Description |
| --- | --- |
| DigitalCaptureWaveforms | Provides operations to create and fetch capture waveforms with the NI-Digital Pattern Driver. |
| DigitalClockGenerator | Drives a free-running clock that runs independently of the digital pattern on the specified pins. |
| DigitalConditionalJumpTrigger | Provides configuration and controls for conditional jump triggers that affect the logical flow of a pattern. |
| DigitalCycleNumberHistoryRamTrigger | Contains properties and methods for configuring the cycle number History RAM trigger. |
| DigitalDriverIdentity | Provides information about the instrument and the NI-Digital Pattern Driver software. |
| DigitalDriverOperation | Provides properties that control the operation of the NI-Digital Pattern Driver software. |
| DigitalDriverUtility | Provides a basic set of driver utility operations. |
| DigitalEdgeConditionalJumpTrigger | Contains properties and methods to configure and control a conditional jump trigger as a digital edge conditional jump trigger. |
| DigitalEdgeRIOTrigger | Contains properties and methods to configure and control a RIO trigger as a digital edge RIO trigger. |
| DigitalEdgeStartTrigger | Contains properties and methods to configure and control the start trigger as a digital edge start trigger. |
| DigitalEvent | Contains functionality for configuring events. |
| DigitalFirstFailureHistoryRamTrigger | Contains properties and methods for configuring the first failure History RAM trigger. |
| DigitalFrequencyCounter | Configures the measurement time and measures frequency on the specified pins. |
| DigitalHistoryRam | Contains properties and methods to configure and fetch History RAM cycle information. |
| DigitalHistoryRamTrigger | Provides configuration and controls for History RAM triggers that affect when to acquire pattern information. |
| DigitalLevels | Represents all the current and voltage levels applicable to pattern bursting. |
| DigitalPatternControl | Provides the controls for setting up and bursting a pattern. |
| DigitalPatternLabelHistoryRamTrigger | Contains properties and methods for configuring the pattern label History RAM trigger. |
| DigitalPatternOpcodeEvent | Provides configuration and controls for pattern opcode events. |
| DigitalPinAndChannelMap | Provides methods to configure NIDigital pin and channel maps. |
| DigitalPinSet | Represents a set of one or more channels, pins, or pin groups. Call GetPinSet to create a pin set. |
| DigitalPpmu | Configures current and voltage levels that the PPMU outputs to or measures from the DUT. |
| DigitalRIOEvent | Provides configuration and controls for RIO events. |
| DigitalRIOTrigger | Provides configuration and controls for RIO triggers. |
| DigitalSequencerFlagTrigger | Provides the configuration for the sequencer flag trigger. |
| DigitalSoftwareConditionalJumpTrigger | Contains properties and methods to configure and control a conditional jump trigger for software triggering. |
| DigitalSoftwareStartTrigger | Contains properties and methods to configure and control the start trigger for software triggering. |
| DigitalSourceDCCurrent | Configures a PPMU when the OutputFunction is DCCurrent. |
| DigitalSourceDCVoltage | Configures a PPMU when the OutputFunction is DCVoltage. |
| DigitalSourceWaveforms | Contains properties and methods for waveform operations, including creating and writing source waveforms. |
| DigitalStartTrigger | Provides configuration and controls for start triggers that affect how the pattern burst begins. |
| DigitalSubObject | Represents members that are common to all sub-object NIDigital classes. This is an internal class and is not intended for external use. |
| DigitalTimeSet | Represents a time set for a digital pattern instrument. Use this class to modify time set values after applying a timing sheet with ApplyLevelsAndTiming(string, string, string), or to create time sets programmatically without the use of timing sheets. This class does not modify the timing sheet file or the timing sheet contents that will be used in future calls to ApplyLevelsAndTiming(string, string, string), it only affects the values of the current timing context. |
| DigitalTiming | Provides functionality for creating and getting time sets and adjusting board-level timing. |
| DigitalTrigger | Contains functionality for configuring triggers. |
| NIDigital | Represents a digital pattern instrument session. |

#### Interfaces

None

#### Structures

| Name | Description |
| --- | --- |
| DigitalHistoryRamCycleInformation | Represents a cycle acquired from History RAM. |
| DigitalPinInformation | Represents mapped pin information associating a pin name, a channel name, and a site number. |

#### Enumerations

| Name | Description |
| --- | --- |
| BitOrder | Specifies the order of bit significance. |
| DigitalEdge | Specifies the active edge for the start trigger. |
| DriveFormat | Specifies the drive format of the time set. |
| FrequencyMeasurementMode | Specifies the drive format of the time set. |
| HistoryRamCycle | Specifies the History RAM cycles. |
| HistoryRamTriggerType | Specifies the History RAM trigger type. |
| PinState | The digital state of the pin. |
| PpmuApertureTimeUnits | Specifies the unit of the aperture time. |
| PpmuCurrentLimitBehavior | The output current's behavior when the current limit is reached. |
| PpmuMeasurementType | Specifies whether the PPMU measures voltage or current. |
| PpmuOutputFunction | Specifies whether one or more pins functioning as a PPMU is forcing voltage or current to the DUT. |
| SelectedFunction | Specifies which instrument function controls the pin(s). By default, all pins are set to Disconnect. |
| SignalType | Specifies the type of signal to route. |
| SiteResultType | The type of data in the results array. |
| SourceDataMapping | Specifies how to map data on multiple sites. |
| TdrEndpointTermination | Specifies whether TDR channels are connected to an open circuit or a short to ground. |
| TerminationMode | Specifies the behavior of one or more pins when the driver is in a non-drive state. |
| TimeSetEdge | Specifies the edge of the time set. |
| TriggerType | Specifies the start trigger type. |

#### Delegates

None
