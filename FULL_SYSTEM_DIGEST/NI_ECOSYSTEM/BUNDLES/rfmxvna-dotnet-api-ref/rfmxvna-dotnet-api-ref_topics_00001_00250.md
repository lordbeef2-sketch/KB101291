# NI DOCUMENT BUNDLE: rfmxvna-dotnet-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxvna-dotnet-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxvnamxextension-getvnasignalconfiguration__this-string.html language=enus -->
## TOPIC 00001: GetVnaSignalConfiguration(this RFmxInstrMX, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxvnamxextension-getvnasignalconfiguration__this-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxvnamxextension-getvnasignalconfiguration__this-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a Vna signal configuration for specified signal name. Existing Vna signal configuration is returned if specified signal name exists. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxVnaMX GetVnaSignalConfiguration(this RFmxInstrMX instrSession, string signalName)ParametersN

### GetVnaSignalConfiguration(this RFmxInstrMX, string)

Creates a Vna signal configuration for specified signal name. Existing Vna signal configuration is returned if specified signal name exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxVnaMX](nationalinstruments-rfmx-vnamx-rfmxvnamx.html) GetVnaSignalConfiguration(this RFmxInstrMX instrSession, string signalName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an RFmxInstr session. |
| signalName | string | Specifies a signal name. |

#### Returns

Returns an object of type RFmxVnaMX.

Parent topic:

RFmxVnaMXExtension Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxvnamxextension-getvnasignalconfiguration__this.html language=enus -->
## TOPIC 00002: GetVnaSignalConfiguration(this RFmxInstrMX)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxvnamxextension-getvnasignalconfiguration__this.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxvnamxextension-getvnasignalconfiguration__this.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new default Vna signal configuration if it doesn't exist; otherwise, it returns the existing default Vna signal configuration. SyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic static RFmxVnaMX GetVnaSignalConfiguration(this RFmxInstrMX instrSession)ParametersNameTypeDescriptioninstr

### GetVnaSignalConfiguration(this RFmxInstrMX)

Creates a new default Vna signal configuration if it doesn't exist; otherwise, it returns the existing default Vna signal configuration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public static [RFmxVnaMX](nationalinstruments-rfmx-vnamx-rfmxvnamx.html) GetVnaSignalConfiguration(this RFmxInstrMX instrSession)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrSession | this RFmxInstrMX | Specifies an instr session. |

#### Returns

Returns an object of type RFmxVnaMX.

Parent topic:

RFmxVnaMXExtension Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-instrmx-rfmxvnamxextension.html language=enus -->
## TOPIC 00003: RFmxVnaMXExtension Class

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx-rfmxvnamxextension.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx-rfmxvnamxextension.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides extension methods to create Vna signal configuration. These methods are added to RFmxInstrMX class. Derives fromNoneSyntaxNamespace: NationalInstruments.RFmx.InstrMXpublic class RFmxVnaMXExtensionRemarksFor more information about NI-RFmx Instruments, refer to the NI-RFmx Instruments Help.Th

### RFmxVnaMXExtension Class

Provides extension methods to create Vna signal configuration. These methods are added to RFmxInstrMX class.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.RFmx.InstrMX](nationalinstruments-rfmx-instrmx.html)

public class RFmxVnaMXExtension

#### Remarks

For more information about NI-RFmx Instruments, refer to the NI-RFmx Instruments Help.

#### Thread Safety

Any public static members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetVnaSignalConfiguration(this RFmxInstrMX, string) | Creates a Vna signal configuration for specified signal name. Existing Vna signal configuration is returned if specified signal name exists. |
| GetVnaSignalConfiguration(this RFmxInstrMX) | Creates a new default Vna signal configuration if it doesn't exist; otherwise, it returns the existing default Vna signal configuration. |

Parent topic:

NationalInstruments.RFmx.InstrMX

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-instrmx.html language=enus -->
## TOPIC 00004: NationalInstruments.RFmx.InstrMX

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-instrmx.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-instrmx.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionRFmxVnaMXExtensionProvides extension methods to create Vna signal configuration. These methods are added to RFmxInstrMX class. InterfacesNoneStructuresNoneEnumerationsNoneDelegatesNone

### NationalInstruments.RFmx.InstrMX

#### Classes

| Name | Description |
| --- | --- |
| RFmxVnaMXExtension | Provides extension methods to create Vna signal configuration. These methods are added to RFmxInstrMX class. |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-autodetectvcalorientation__string.html language=enus -->
## TOPIC 00005: AutoDetectvCalOrientation(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-autodetectvcalorientation__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-autodetectvcalorientation__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically detects the vCal ports connected to the VNA ports and writes the CorrectionCalibrationCalkitElectronicOrientation property. Call this function before calling the CalibrationInitiate(string) method. Auto detection of vCal orientation initially occurs at the midpoint of the frequency ran

### AutoDetectvCalOrientation(string)

Automatically detects the vCal ports connected to the VNA ports and writes the [CorrectionCalibrationCalkitElectronicOrientation](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property. Call this function before calling the [CalibrationInitiate(string)](nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationinitiate__string.html) method. 
 Auto detection of vCal orientation initially occurs at the midpoint of the frequency range specified for the calibration. If the connection is not detected, it retries at the lowest frequnecy in the configured range. 
 The auto detection may fail if the power level at the vCal module is too low. If it fails, use the [CorrectionCalibrationCalkitElectronicOrientation](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to configure the orientation manually.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int AutoDetectvCalOrientation(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-autoportextensionmeasure__string-rfmxvnamxcorrectionportextensionautostandard-string.html language=enus -->
## TOPIC 00006: AutoPortExtensionMeasure(string, RFmxVnaMXCorrectionPortExtensionAutoStandard, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-autoportextensionmeasure__string-rfmxvnamxcorrectionportextensionautostandard-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-autoportextensionmeasure__string-rfmxvnamxcorrectionportextensionautostandard-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically determine the fixture delay and loss (optional) values by measuring the standard at the configured port. The calculated delay and loss values are used to set the SetCorrectionPortExtensionDelay(string, double), SetCorrectionPortExtensionLossDCLoss(string, double), SetCorrectionPortExte

### AutoPortExtensionMeasure(string, RFmxVnaMXCorrectionPortExtensionAutoStandard, string)

Automatically determine the fixture delay and loss (optional) values by measuring the standard at the configured port. The calculated delay and loss values are used to set the [SetCorrectionPortExtensionDelay(string, double)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondelay__string-double.html), [SetCorrectionPortExtensionLossDCLoss(string, double)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionlossdcloss__string-double.html), [SetCorrectionPortExtensionLoss1(string, double)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss1__string-double.html) and [SetCorrectionPortExtensionLoss2(string, double)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss2__string-double.html) methods. Call this method after calibrating the VNA port, where port extension is required, to obtain more accurate delay and loss estimates. 
 An ideal OPEN and SHORT standard, with zero loss and delay, is assumed. Therefore, the accuracy depends on the quality of the standard. 
 To measure either OPEN or SHORT, call [AutoPortExtensionReset(string)](nationalinstruments-rfmx-vnamx-rfmxvnamx-autoportextensionreset__string.html) before measuring the standard. 
 When both OPEN and SHORT standards are measured, the average of the calculated delay and loss values are entered. 
 You must call [Initiate(string, string)](nationalinstruments-rfmx-vnamx-rfmxvnamx-initiate__string-string.html) afterwards to obtain the compensated measurement results.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int AutoPortExtensionMeasure(string selectorString, RFmxVnaMXCorrectionPortExtensionAutoStandard standard, string port)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| standard | RFmxVnaMXCorrectionPortExtensionAutoStandard | Specifies the standard to be measured. |
| port | string | Specifies the standard to be measured. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-autoportextensionreset__string.html language=enus -->
## TOPIC 00007: AutoPortExtensionReset(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-autoportextensionreset__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-autoportextensionreset__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the measured standard data used for automatic port extension. Before measuring an OPEN or SHORT standard, you must reset any previously measured standard data. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int AutoPortExtensionReset(string selectorString)ParametersNameTypeDescriptions

### AutoPortExtensionReset(string)

Resets the measured standard data used for automatic port extension. 
 Before measuring an OPEN or SHORT standard, you must reset any previously measured standard data.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int AutoPortExtensionReset(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-buildcalibrationelementstring__string-string.html language=enus -->
## TOPIC 00008: BuildCalibrationElementString(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-buildcalibrationelementstring__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-buildcalibrationelementstring__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string specifying the Calibration Element within the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic static string BuildCalibrationElementString(string selectorString, string calibrationElementID)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector st

### BuildCalibrationElementString(string, string)

Creates a selector string specifying the Calibration Element within the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public static string BuildCalibrationElementString(string selectorString, string calibrationElementID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "result::myresult1" You can use the BuildResultString(string) method to build the selector string. |
| calibrationElementID | string | Specifies the ID of the Calibration Element within the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-buildcalstepstring__string-int.html language=enus -->
## TOPIC 00009: BuildCalstepString(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-buildcalstepstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-buildcalstepstring__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the calibration step string to use as the selector string with the CalibrationAcquire(string, double) method.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic static string BuildCalstepString(string selectorString, int calstepNumber)ParametersNameTypeDescriptionselectorStringstringSpecif

### BuildCalstepString(string, int)

Creates the calibration step string to use as the selector string with the [CalibrationAcquire(string, double)](nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationacquire__string-double.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public static string BuildCalstepString(string selectorString, int calstepNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "result::myresult1" You can use the BuildResultString(string) method to build the selector string. |
| calstepNumber | int | Specifies the calibration step number for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-buildmeasurementmemorystring__string-string.html language=enus -->
## TOPIC 00010: BuildMeasurementMemoryString(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-buildmeasurementmemorystring__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-buildmeasurementmemorystring__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string specifying the measurement memory name for use with the get methods. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic static string BuildMeasurementMemoryString(string selectorString, string measurementMemoryName)ParametersNameTypeDescriptionselectorStringstringPass an e

### BuildMeasurementMemoryString(string, string)

Creates selector string specifying the measurement memory name for use with the get methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public static string BuildMeasurementMemoryString(string selectorString, string measurementMemoryName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurementMemoryName | string | specifies the measurement memory name to build the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-buildportstring__string-string.html language=enus -->
## TOPIC 00011: BuildPortString(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-buildportstring__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-buildportstring__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string specifying the port(s) for use with configuration or fetch methods and methods. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic static string BuildPortString(string selectorString, string portString)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector s

### BuildPortString(string, string)

Creates selector string specifying the port(s) for use with configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public static string BuildPortString(string selectorString, string portString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "result::myresult1" You can use the BuildResultString(string) method to build the selector string. |
| portString | string | Specifies the signal name for building the selector string. This input accepts the port name with or without the "port::" prefix. The default value is "" (empty string). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-buildresultstring__string.html language=enus -->
## TOPIC 00012: BuildResultString(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-buildresultstring__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-buildresultstring__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates selector string for use with configuration or fetch. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic static string BuildResultString(string resultName)ParametersNameTypeDescriptionresultNamestringSpecifies the result name for building the selector string. This input accepts the result

### BuildResultString(string)

Creates selector string for use with configuration or fetch.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public static string BuildResultString(string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resultName | string | Specifies the result name for building the selector string. This input accepts the result name with or without the "result::" prefix. Example: "", "result::r1", "r1". |

#### Returns

Upon return, contains the selector string created by this method.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-buildsegmentstring__string-int.html language=enus -->
## TOPIC 00013: BuildSegmentString(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-buildsegmentstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-buildsegmentstring__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string specifying the segment number for use with configuration or fetch methods and methods. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic static string BuildSegmentString(string selectorString, int segmentNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies

### BuildSegmentString(string, int)

Creates a selector string specifying the segment number for use with configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public static string BuildSegmentString(string selectorString, int segmentNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "result::myresult1" You can use the BuildResultString(string) method to build the selector string. |
| segmentNumber | int | Specifies the segment for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-buildsparameterstring__string-int.html language=enus -->
## TOPIC 00014: BuildSParameterString(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-buildsparameterstring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-buildsparameterstring__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the selector string to use with S-Parameter configuration or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic static string BuildSParameterString(string selectorString, int sParameterNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector s

### BuildSParameterString(string, int)

Creates the selector string to use with S-Parameter configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public static string BuildSParameterString(string selectorString, int sParameterNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "result::myresult1" You can use the BuildResultString(string) method to build the selector string. |
| sParameterNumber | int | Specifies the s-parameter index for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-buildwavestring__string-int.html language=enus -->
## TOPIC 00015: BuildWaveString(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-buildwavestring__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-buildwavestring__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the selector string to use with Wave configuration or fetch methods and methods.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic static string BuildWaveString(string selectorString, int waveNumber)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of

### BuildWaveString(string, int)

Creates the selector string to use with Wave configuration or fetch methods and methods.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public static string BuildWaveString(string selectorString, int waveNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "result::myresult1" You can use the BuildResultString(string) method to build the selector string. |
| waveNumber | int | Specifies the wave index for building the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationabort__string.html language=enus -->
## TOPIC 00016: CalibrationAbort(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationabort__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationabort__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the calibration, which was previously initiated by CalibrationInitiate(string) method, for the signal instance that you specify in the selectorString parameter. Calling this method is optional, unless you want to stop a calibration before it is complete. This method executes even if there is a

### CalibrationAbort(string)

Stops the calibration, which was previously initiated by [CalibrationInitiate(string)](nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationinitiate__string.html) method, for the signal instance that you specify in the *selectorString* parameter. Calling this method is optional, unless you want to stop a calibration before it is complete. This method executes even if there is an incoming error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalibrationAbort(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationacquire__string-double.html language=enus -->
## TOPIC 00017: CalibrationAcquire(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationacquire__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationacquire__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures one or more calibration standards for the specified calibration step. You can call this method only after required calibration steps are determined by RFmx when you call CalibrationInitiate(string). One successful call to CalibrationInitiate(string) is sufficient for all subsequent calls to

### CalibrationAcquire(string, double)

Measures one or more calibration standards for the specified calibration step. 
 You can call this method only after required calibration steps are determined by RFmx when you call [CalibrationInitiate(string)](nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationinitiate__string.html). One successful call to [CalibrationInitiate(string)](nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationinitiate__string.html) is sufficient for all subsequent calls to this method. 
 When [CorrectionCalibrationCalkitType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is [Electronic](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html), RFmx uses all relevant 1-port and 2-port calibration standards in the selected electronic calibration module. A single call to this method measures all such cal standards in the electronic calibration module. For example, if you use NI CAL-5501 electronic calkit to calibrate NI PXIe-5633 by using SOLT calibration method, you only need to perform 1 manual connection to connect the 2 cal module ports to 2 VNA ports. After setting up the required connection, a single call to this method measures all relevant cal standards automatically. 
 When [CorrectionCalibrationCalkitType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) is [Mechanical](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html), RFmx can measure for only one cal standard for each cal step. Specify the active cal step in the Selector String. Use [BuildCalstepString(string, int)](nationalinstruments-rfmx-vnamx-rfmxvnamx-buildcalstepstring__string-int.html) method to build cal step string. For example, if you calibrate the NI PXIe-5633 using a mechanical calkit containing a Short, Open, Load and Thru discrete cal standards, then you must perform 7 distinct manual connections, call this method once per cal step, which in-turn instructs you to connect an appropriate 1 or 2-port cal standard to the VNA port(s). 
 You must call this method at least once for each cal step to measure corresponding calibration standard. If you call this method more than once for a given cal step, the cal standard measurement data for the latest call overwrites the previously measured data for the same standard. RFmx stores the cal standard measurement data which is later used to compute error correction terms when you call RFmxVNA Calibration Save method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalibrationAcquire(string selectorString, double timeout)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| timeout | double | Specifies the timeout, in seconds, for acquiring the calibration data. Set this value to an appropriate time, longer than expected for completing acqusition(s) for the speficied calibration step. A value of -1 specifies that the method waits until the acquisition is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationsave__string-string.html language=enus -->
## TOPIC 00018: CalibrationSave(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationsave__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationsave__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes error-correction terms and saves the calset in memory. Call this method after all calibration standards have been measured using CalibrationAcquire(string, double) method. If you do not specify Calset Name input parameter, the calset is saved as default calset for the specified signal and i

### CalibrationSave(string, string)

Computes error-correction terms and saves the calset in memory. Call this method after all calibration standards have been measured using [CalibrationAcquire(string, double)](nationalinstruments-rfmx-vnamx-rfmxvnamx-calibrationacquire__string-double.html) method. 
 If you do not specify Calset Name input parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. 
 To perform another calibration after you call this method, you must call RFmxVNA Calibration Initiate method again.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalibrationSave(string selectorString, string calsetName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calsetName | string | Specifies the name of the calset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitaddcalibrationelement__string-string.html language=enus -->
## TOPIC 00019: CalkitManagerCalkitAddCalibrationElement(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitaddcalibrationelement__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitaddcalibrationelement__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitAddCalibrationElement(string sel

### CalkitManagerCalkitAddCalibrationElement(string, string)

Adds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitAddCalibrationElement(string selectorString, string calibrationElementID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| calibrationElementID | string | Specifies the ID of the Calibration Element within the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitaddconnector__string-string.html language=enus -->
## TOPIC 00020: CalkitManagerCalkitAddConnector(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitaddconnector__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitaddconnector__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitAddConnector(string selectorString, string connectorID)ParametersNameTyp

### CalkitManagerCalkitAddConnector(string, string)

Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitAddConnector(string selectorString, string connectorID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| connectorID | string | Specifies the ID of the Connector within the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementdelaymodelsetdelay__string-double.html language=enus -->
## TOPIC 00021: CalkitManagerCalkitCalibrationElementDelayModelSetDelay(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementdelaymodelsetdelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementdelaymodelsetdelay__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the Delay of a Calibration Element defined by the Delay Model.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementDelayModelSetDelay(string selectorString, double delay)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string c

### CalkitManagerCalkitCalibrationElementDelayModelSetDelay(string, double)

Defines the Delay of a Calibration Element defined by the Delay Model.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementDelayModelSetDelay(string selectorString, double delay)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| delay | double | Specifies the Delay of a Calibration Element defined by the Delay Model. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetdescription__string-out.html language=enus -->
## TOPIC 00022: CalkitManagerCalkitCalibrationElementGetDescription(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetdescription__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetdescription__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the description for a Calibration Element of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementGetDescription(string selectorString, out string description)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector s

### CalkitManagerCalkitCalibrationElementGetDescription(string, out string)

Returns the description for a Calibration Element of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementGetDescription(string selectorString, out string description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| description | out string | Upon return, contains the description for a Calibration Element of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetminimumfrequency__string-out.html language=enus -->
## TOPIC 00023: CalkitManagerCalkitCalibrationElementGetMinimumFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetminimumfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetminimumfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Minimum Frequency of the Calibration Element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementGetMinimumFrequency(string selectorString, out double minimumFrequency)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector strin

### CalkitManagerCalkitCalibrationElementGetMinimumFrequency(string, out double)

Returns the Minimum Frequency of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementGetMinimumFrequency(string selectorString, out double minimumFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| minimumFrequency | out double | Upon return, contains the Minimum Frequency of the Calibration Element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetportconnectors__string-ref.html language=enus -->
## TOPIC 00024: CalkitManagerCalkitCalibrationElementGetPortConnectors(string, ref string[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetportconnectors__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetportconnectors__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of Connectors associated with the Calibration Element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementGetPortConnectors(string selectorString, ref string[] connectorIDs)ParametersNameTypeDescriptionselectorStringstringSpecifies the sel

### CalkitManagerCalkitCalibrationElementGetPortConnectors(string, ref string[])

Returns the array of Connectors associated with the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementGetPortConnectors(string selectorString, ref string[] connectorIDs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| connectorIDs | ref string[] | Upon return, contains the array of Connectors associated with the Calibration Element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetsparameterdefinition__string-out.html language=enus -->
## TOPIC 00025: CalkitManagerCalkitCalibrationElementGetSParameterDefinition(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetsparameterdefinition__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgetsparameterdefinition__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S-Parameter definition of the Calibration Element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementGetSParameterDefinition(string selectorString, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition sParameterDefinition)Para

### CalkitManagerCalkitCalibrationElementGetSParameterDefinition(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition)

Returns the S-Parameter definition of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementGetSParameterDefinition(string selectorString, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition sParameterDefinition)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| sParameterDefinition | out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterDefinition | Upon return, contains the S-Parameter definition of the Calibration Element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgettypes__string-ref.html language=enus -->
## TOPIC 00026: CalkitManagerCalkitCalibrationElementGetTypes(string, ref RFmxVnaMXCalkitManagerCalkitCalibrationElementType[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgettypes__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementgettypes__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the type(s) of the Calibration Element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementGetTypes(string selectorString, ref RFmxVnaMXCalkitManagerCalkitCalibrationElementType[] calibrationElementTypes)ParametersNameTypeDescriptionselectorStringst

### CalkitManagerCalkitCalibrationElementGetTypes(string, ref RFmxVnaMXCalkitManagerCalkitCalibrationElementType[])

Returns the type(s) of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementGetTypes(string selectorString, ref RFmxVnaMXCalkitManagerCalkitCalibrationElementType[] calibrationElementTypes)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| calibrationElementTypes | ref RFmxVnaMXCalkitManagerCalkitCalibrationElementType[] | Upon return, contains the type(s) of the Calibration Element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc0__string-out.html language=enus -->
## TOPIC 00027: CalkitManagerCalkitCalibrationElementReflectModelGetC0(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc0__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc0__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelGetC0(string selectorString, out double c0)ParametersNam

### CalkitManagerCalkitCalibrationElementReflectModelGetC0(string, out double)

Returns the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelGetC0(string selectorString, out double c0)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| c0 | out double | Upon return, contains the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc1__string-out.html language=enus -->
## TOPIC 00028: CalkitManagerCalkitCalibrationElementReflectModelGetC1(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc1__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc1__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelGetC1(string selectorString, out double c1)ParametersNam

### CalkitManagerCalkitCalibrationElementReflectModelGetC1(string, out double)

Returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelGetC1(string selectorString, out double c1)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| c1 | out double | Upon return, contains the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc3__string-out.html language=enus -->
## TOPIC 00029: CalkitManagerCalkitCalibrationElementReflectModelGetC3(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc3__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetc3__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelGetC3(string selectorString, out double c3)ParametersNam

### CalkitManagerCalkitCalibrationElementReflectModelGetC3(string, out double)

Returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelGetC3(string selectorString, out double c3)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| c3 | out double | Upon return, contains the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetmodeltype__string-out.html language=enus -->
## TOPIC 00030: CalkitManagerCalkitCalibrationElementReflectModelGetModelType(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetmodeltype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetmodeltype__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the model type of of the 1-port reflect standard.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelGetModelType(string selectorString, out RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType modelType)ParametersNameTypeDescr

### CalkitManagerCalkitCalibrationElementReflectModelGetModelType(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType)

Returns the model type of of the 1-port reflect standard.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelGetModelType(string selectorString, out RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType modelType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| modelType | out RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType | Upon return, contains the model type of of the 1-port reflect standard. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetoffsetloss__string-out.html language=enus -->
## TOPIC 00031: CalkitManagerCalkitCalibrationElementReflectModelGetOffsetLoss(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetoffsetloss__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetoffsetloss__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the offset loss.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelGetOffsetLoss(string selectorString, out double offsetLoss)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created by this method. The sel

### CalkitManagerCalkitCalibrationElementReflectModelGetOffsetLoss(string, out double)

Returns the offset loss.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelGetOffsetLoss(string selectorString, out double offsetLoss)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| offsetLoss | out double | Upon return, contains the offset loss. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetreferenceimpedance__string-out.html language=enus -->
## TOPIC 00032: CalkitManagerCalkitCalibrationElementReflectModelGetReferenceImpedance(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetreferenceimpedance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelgetreferenceimpedance__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the reference impedance.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelGetReferenceImpedance(string selectorString, out double referenceImpedance)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created

### CalkitManagerCalkitCalibrationElementReflectModelGetReferenceImpedance(string, out double)

Returns the reference impedance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelGetReferenceImpedance(string selectorString, out double referenceImpedance)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| referenceImpedance | out double | Upon return, contains the reference impedance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc1__string-double.html language=enus -->
## TOPIC 00033: CalkitManagerCalkitCalibrationElementReflectModelSetC1(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc1__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc1__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelSetC1(string selectorString, double c1)ParametersNameT

### CalkitManagerCalkitCalibrationElementReflectModelSetC1(string, double)

Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelSetC1(string selectorString, double c1)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| c1 | double | Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc2__string-double.html language=enus -->
## TOPIC 00034: CalkitManagerCalkitCalibrationElementReflectModelSetC2(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc2__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc2__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelSetC2(string selectorString, double c2)ParametersNameT

### CalkitManagerCalkitCalibrationElementReflectModelSetC2(string, double)

Specifies the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelSetC2(string selectorString, double c2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| c2 | double | Specifies the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc3__string-double.html language=enus -->
## TOPIC 00035: CalkitManagerCalkitCalibrationElementReflectModelSetC3(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc3__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetc3__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelSetC3(string selectorString, double c3)ParametersNameT

### CalkitManagerCalkitCalibrationElementReflectModelSetC3(string, double)

Specifies the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelSetC3(string selectorString, double c3)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| c3 | double | Specifies the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetmodeltype__string-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodeltype.html language=enus -->
## TOPIC 00036: CalkitManagerCalkitCalibrationElementReflectModelSetModelType(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetmodeltype__string-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodeltype.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetmodeltype__string-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodeltype.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the model type of the 1-port reflect standard.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelSetModelType(string selectorString, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType modelType)ParametersNameTypeDescriptio

### CalkitManagerCalkitCalibrationElementReflectModelSetModelType(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType)

Specifies the model type of the 1-port reflect standard.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelSetModelType(string selectorString, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType modelType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| modelType | RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelType | Specifies the model type of of the 1-port reflect standard. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetoffsetdelay__string-double.html language=enus -->
## TOPIC 00037: CalkitManagerCalkitCalibrationElementReflectModelSetOffsetDelay(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetoffsetdelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetoffsetdelay__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset delay.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelSetOffsetDelay(string selectorString, double offsetDelay)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created by this method. The se

### CalkitManagerCalkitCalibrationElementReflectModelSetOffsetDelay(string, double)

Specifies the offset delay.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelSetOffsetDelay(string selectorString, double offsetDelay)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| offsetDelay | double | Specifies the offset delay. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetoffsetloss__string-double.html language=enus -->
## TOPIC 00038: CalkitManagerCalkitCalibrationElementReflectModelSetOffsetLoss(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetoffsetloss__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetoffsetloss__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset loss.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelSetOffsetLoss(string selectorString, double offsetLoss)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created by this method. The selec

### CalkitManagerCalkitCalibrationElementReflectModelSetOffsetLoss(string, double)

Specifies the offset loss.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelSetOffsetLoss(string selectorString, double offsetLoss)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| offsetLoss | double | Specifes the offset loss. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetreferenceimpedance__string-double.html language=enus -->
## TOPIC 00039: CalkitManagerCalkitCalibrationElementReflectModelSetReferenceImpedance(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetreferenceimpedance__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetreferenceimpedance__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference impedance.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelSetReferenceImpedance(string selectorString, double referenceImpedance)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created b

### CalkitManagerCalkitCalibrationElementReflectModelSetReferenceImpedance(string, double)

Specifies the reference impedance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelSetReferenceImpedance(string selectorString, double referenceImpedance)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| referenceImpedance | double | Specifies the reference impedance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetsparamavailability__string-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodelsparameteravailability.html language=enus -->
## TOPIC 00040: CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetsparamavailability__string-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodelsparameteravailability.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementreflectmodelsetsparamavailability__string-rfmxvnamxcalkitmanagercalkitcalibrationelementreflectmodelsparameteravailability.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the S-Parameter availability.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability(string selectorString, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability sParameterAvailability)Param

### CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability)

Specifies the S-Parameter availability.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability(string selectorString, RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability sParameterAvailability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| sParameterAvailability | RFmxVnaMXCalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability | Specifies the S-Parameter availability. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsetdescription__string-string.html language=enus -->
## TOPIC 00041: CalkitManagerCalkitCalibrationElementSetDescription(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsetdescription__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsetdescription__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the description for a Calibration Element of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSetDescription(string selectorString, string description)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string c

### CalkitManagerCalkitCalibrationElementSetDescription(string, string)

Sets the description for a Calibration Element of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSetDescription(string selectorString, string description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| description | string | Specifies the description for a Calibration Element of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsetportconnectors__string-string_arr1.html language=enus -->
## TOPIC 00042: CalkitManagerCalkitCalibrationElementSetPortConnectors(string, string[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsetportconnectors__string-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsetportconnectors__string-string_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element.SyntaxNamespace: NationalInstrumen

### CalkitManagerCalkitCalibrationElementSetPortConnectors(string, string[])

Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSetPortConnectors(string selectorString, string[] connectorIDs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| connectorIDs | string[] | Specifies the array of Connectors associated with the Calibration Element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsettypes__string-rfmxvnamxcalkitmanagercalkitcalibrationelementtype_arr1.html language=enus -->
## TOPIC 00043: CalkitManagerCalkitCalibrationElementSetTypes(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementType[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsettypes__string-rfmxvnamxcalkitmanagercalkitcalibrationelementtype_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsettypes__string-rfmxvnamxcalkitmanagercalkitcalibrationelementtype_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the type(s) of the Calibration Element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSetTypes(string selectorString, RFmxVnaMXCalkitManagerCalkitCalibrationElementType[] calibrationElementTypes)ParametersNameTypeDescriptionselectorStringstringSpe

### CalkitManagerCalkitCalibrationElementSetTypes(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementType[])

Sets the type(s) of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSetTypes(string selectorString, RFmxVnaMXCalkitManagerCalkitCalibrationElementType[] calibrationElementTypes)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| calibrationElementTypes | RFmxVnaMXCalkitManagerCalkitCalibrationElementType[] | Specifies the type(s) of the Calibration Element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergetfrequency__string-ref.html language=enus -->
## TOPIC 00044: CalkitManagerCalkitCalibrationElementSParameterGetFrequency(string, ref double[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergetfrequency__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergetfrequency__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency array for the S-Parameter definition of the Calibration Element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterGetFrequency(string selectorString, ref double[] frequency)ParametersNameTypeDescriptionselectorStringstringS

### CalkitManagerCalkitCalibrationElementSParameterGetFrequency(string, ref double[])

Returns the frequency array for the S-Parameter definition of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterGetFrequency(string selectorString, ref double[] frequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| frequency | ref double[] | Upon return, contains the frequency array for the S-Parameter definition of the Calibration Element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets11__string-ref.html language=enus -->
## TOPIC 00045: CalkitManagerCalkitCalibrationElementSParameterGetS11(string, ref ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets11__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets11__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S11 S-Parameter for the calibration element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterGetS11(string selectorString, ref ComplexDouble[] s11)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string create

### CalkitManagerCalkitCalibrationElementSParameterGetS11(string, ref ComplexDouble[])

Returns the S11 S-Parameter for the calibration element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterGetS11(string selectorString, ref ComplexDouble[] s11)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| s11 | ref ComplexDouble[] | Upon return, contains the S11 S-Parameter for the calibration element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets12__string-ref.html language=enus -->
## TOPIC 00046: CalkitManagerCalkitCalibrationElementSParameterGetS12(string, ref ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets12__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets12__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S12 S-Parameter for the calibration element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterGetS12(string selectorString, ref ComplexDouble[] s12)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string create

### CalkitManagerCalkitCalibrationElementSParameterGetS12(string, ref ComplexDouble[])

Returns the S12 S-Parameter for the calibration element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterGetS12(string selectorString, ref ComplexDouble[] s12)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| s12 | ref ComplexDouble[] | Upon return, contains the S12 S-Parameter for the calibration element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets21__string-ref.html language=enus -->
## TOPIC 00047: CalkitManagerCalkitCalibrationElementSParameterGetS21(string, ref ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets21__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets21__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S21 S-Parameter for the calibration element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterGetS21(string selectorString, ref ComplexDouble[] s21)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string create

### CalkitManagerCalkitCalibrationElementSParameterGetS21(string, ref ComplexDouble[])

Returns the S21 S-Parameter for the calibration element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterGetS21(string selectorString, ref ComplexDouble[] s21)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| s21 | ref ComplexDouble[] | Upon return, contains the S21 S-Parameter for the calibration element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets22__string-ref.html language=enus -->
## TOPIC 00048: CalkitManagerCalkitCalibrationElementSParameterGetS22(string, ref ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets22__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergets22__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S22 S-Parameter for the calibration element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterGetS22(string selectorString, ref ComplexDouble[] s22)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string create

### CalkitManagerCalkitCalibrationElementSParameterGetS22(string, ref ComplexDouble[])

Returns the S22 S-Parameter for the calibration element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterGetS22(string selectorString, ref ComplexDouble[] s22)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| s22 | ref ComplexDouble[] | Upon return, contains the S22 S-Parameter for the calibration element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergetsparamavailability__string-out.html language=enus -->
## TOPIC 00049: CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergetsparamavailability__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametergetsparamavailability__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S-Parameter availability.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability(string selectorString, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability sParameterAvailability)ParametersNameTyp

### CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability(string, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability)

Returns the S-Parameter availability.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability(string selectorString, out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability sParameterAvailability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| sParameterAvailability | out RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability | Upon return, contains the S-Parameter availability. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersetfrequency__string-double_arr1.html language=enus -->
## TOPIC 00050: CalkitManagerCalkitCalibrationElementSParameterSetFrequency(string, double[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersetfrequency__string-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersetfrequency__string-double_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the frequency array for the S-Parameter definition of the Calibration Element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterSetFrequency(string selectorString, double[] frequency)ParametersNameTypeDescriptionselectorStringstringSpeci

### CalkitManagerCalkitCalibrationElementSParameterSetFrequency(string, double[])

Defines the frequency array for the S-Parameter definition of the Calibration Element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterSetFrequency(string selectorString, double[] frequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| frequency | double[] | Specifies the frequency array for the S-Parameter definition of the Calibration Element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets11__string-complexdouble_arr1.html language=enus -->
## TOPIC 00051: CalkitManagerCalkitCalibrationElementSParameterSetS11(string, ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets11__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets11__string-complexdouble_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the S11 S-Parameter for the calibration element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterSetS11(string selectorString, ComplexDouble[] s11)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created by th

### CalkitManagerCalkitCalibrationElementSParameterSetS11(string, ComplexDouble[])

Sets the S11 S-Parameter for the calibration element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterSetS11(string selectorString, ComplexDouble[] s11)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| s11 | ComplexDouble[] | Specifies the S11 S-Parameter for the calibration element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets12__string-complexdouble_arr1.html language=enus -->
## TOPIC 00052: CalkitManagerCalkitCalibrationElementSParameterSetS12(string, ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets12__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets12__string-complexdouble_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the S12 S-Parameter for the calibration element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterSetS12(string selectorString, ComplexDouble[] s12)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created by th

### CalkitManagerCalkitCalibrationElementSParameterSetS12(string, ComplexDouble[])

Sets the S12 S-Parameter for the calibration element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterSetS12(string selectorString, ComplexDouble[] s12)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| s12 | ComplexDouble[] | Specifies the S12 S-Parameter for the calibration element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets21__string-complexdouble_arr1.html language=enus -->
## TOPIC 00053: CalkitManagerCalkitCalibrationElementSParameterSetS21(string, ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets21__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets21__string-complexdouble_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the S21 S-Parameter for the calibration element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterSetS21(string selectorString, ComplexDouble[] s21)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created by th

### CalkitManagerCalkitCalibrationElementSParameterSetS21(string, ComplexDouble[])

Sets the S21 S-Parameter for the calibration element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterSetS21(string selectorString, ComplexDouble[] s21)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| s21 | ComplexDouble[] | Specifies the S21 S-Parameter for the calibration element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets22__string-complexdouble_arr1.html language=enus -->
## TOPIC 00054: CalkitManagerCalkitCalibrationElementSParameterSetS22(string, ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets22__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersets22__string-complexdouble_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the S22 S-Parameter for the calibration element.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterSetS22(string selectorString, ComplexDouble[] s22)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string created by th

### CalkitManagerCalkitCalibrationElementSParameterSetS22(string, ComplexDouble[])

Sets the S22 S-Parameter for the calibration element.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterSetS22(string selectorString, ComplexDouble[] s22)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| s22 | ComplexDouble[] | Specifies the S22 S-Parameter for the calibration element. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersetsparamavailability__string-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameteravailability.html language=enus -->
## TOPIC 00055: CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersetsparamavailability__string-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameteravailability.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitcalibrationelementsparametersetsparamavailability__string-rfmxvnamxcalkitmanagercalkitcalibrationelementsparameteravailability.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the S-Parameter availability.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability(string selectorString, RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability sParameterAvailability)ParametersNameTypeDes

### CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability(string, RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability)

Defines the S-Parameter availability.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability(string selectorString, RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability sParameterAvailability)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string created by this method. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the BuildCalibrationElementString(string, string) method to build the selector string. |
| sParameterAvailability | RFmxVnaMXCalkitManagerCalkitCalibrationElementSParameterAvailability | Specifies the S-Parameter availability. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetdescription__string-out.html language=enus -->
## TOPIC 00056: CalkitManagerCalkitConnectorGetDescription(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetdescription__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetdescription__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the description of a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorGetDescription(string selectorString, out string description)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string to address a s

### CalkitManagerCalkitConnectorGetDescription(string, out string)

Returns the description of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorGetDescription(string selectorString, out string description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| description | out string |  |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetgender__string-out.html language=enus -->
## TOPIC 00057: CalkitManagerCalkitConnectorGetGender(string, out RFmxVnaMXCalkitManagerCalkitConnectorGender)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetgender__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetgender__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Gender of a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorGetGender(string selectorString, out RFmxVnaMXCalkitManagerCalkitConnectorGender connectorGender)ParametersNameTypeDescriptionselectorStringstringSpecifies the

### CalkitManagerCalkitConnectorGetGender(string, out RFmxVnaMXCalkitManagerCalkitConnectorGender)

Returns the Gender of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorGetGender(string selectorString, out RFmxVnaMXCalkitManagerCalkitConnectorGender connectorGender)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| connectorGender | out RFmxVnaMXCalkitManagerCalkitConnectorGender | Upon return, contains the Gender of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetimpedance__string-out.html language=enus -->
## TOPIC 00058: CalkitManagerCalkitConnectorGetImpedance(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetimpedance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetimpedance__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Impedance of a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorGetImpedance(string selectorString, out double impedance)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string to address a specifi

### CalkitManagerCalkitConnectorGetImpedance(string, out double)

Returns the Impedance of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorGetImpedance(string selectorString, out double impedance)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| impedance | out double | Upon return, contains the Impedance of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetmaximumfrequency__string-out.html language=enus -->
## TOPIC 00059: CalkitManagerCalkitConnectorGetMaximumFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetmaximumfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetmaximumfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Maximum Frequency of a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorGetMaximumFrequency(string selectorString, out double maximumFrequency)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector strin

### CalkitManagerCalkitConnectorGetMaximumFrequency(string, out double)

Returns the Maximum Frequency of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorGetMaximumFrequency(string selectorString, out double maximumFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| maximumFrequency | out double | Upon return, contains the Maximum Frequency of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetminimumfrequency__string-out.html language=enus -->
## TOPIC 00060: CalkitManagerCalkitConnectorGetMinimumFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetminimumfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgetminimumfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Minimum Frequency of a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorGetMinimumFrequency(string selectorString, out double minimumFrequency)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector strin

### CalkitManagerCalkitConnectorGetMinimumFrequency(string, out double)

Returns the Minimum Frequency of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorGetMinimumFrequency(string selectorString, out double minimumFrequency)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| minimumFrequency | out double | Upon return, contains the Minimum Frequency of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgettype__string-out.html language=enus -->
## TOPIC 00061: CalkitManagerCalkitConnectorGetType(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgettype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorgettype__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Type of a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorGetType(string selectorString, out string connectorType)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string to address a specific Conn

### CalkitManagerCalkitConnectorGetType(string, out string)

Returns the Type of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorGetType(string selectorString, out string connectorType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| connectorType | out string | Upon return, contains the Type of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetdescription__string-string.html language=enus -->
## TOPIC 00062: CalkitManagerCalkitConnectorSetDescription(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetdescription__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetdescription__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the description for a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorSetDescription(string selectorString, string description)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string to address a specifi

### CalkitManagerCalkitConnectorSetDescription(string, string)

Sets the description for a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorSetDescription(string selectorString, string description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| description | string | Specifies the description for a Connector of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetgender__string-rfmxvnamxcalkitmanagercalkitconnectorgender.html language=enus -->
## TOPIC 00063: CalkitManagerCalkitConnectorSetGender(string, RFmxVnaMXCalkitManagerCalkitConnectorGender)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetgender__string-rfmxvnamxcalkitmanagercalkitconnectorgender.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetgender__string-rfmxvnamxcalkitmanagercalkitconnectorgender.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Gender of a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorSetGender(string selectorString, RFmxVnaMXCalkitManagerCalkitConnectorGender connectorGender)ParametersNameTypeDescriptionselectorStringstringSpecifies the select

### CalkitManagerCalkitConnectorSetGender(string, RFmxVnaMXCalkitManagerCalkitConnectorGender)

Sets the Gender of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorSetGender(string selectorString, RFmxVnaMXCalkitManagerCalkitConnectorGender connectorGender)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| connectorGender | RFmxVnaMXCalkitManagerCalkitConnectorGender | Specifies the Gender of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetimpedance__string-double.html language=enus -->
## TOPIC 00064: CalkitManagerCalkitConnectorSetImpedance(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetimpedance__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitconnectorsetimpedance__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Impedance of a Connector of a specific Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitConnectorSetImpedance(string selectorString, double impedance)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string to address a specific Conne

### CalkitManagerCalkitConnectorSetImpedance(string, double)

Sets the Impedance of a Connector of a specific Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitConnectorSetImpedance(string selectorString, double impedance)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the BuildConnectorString(string, string) method to build the selector string. |
| impedance | double | Specifies the Impedance of a Connector of a specific Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetcalibrationelementids__string-ref.html language=enus -->
## TOPIC 00065: CalkitManagerCalkitGetCalibrationElementIDs(string, ref string[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetcalibrationelementids__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetcalibrationelementids__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of Calibration Element IDs of all Calibration Elements of the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitGetCalibrationElementIDs(string selectorString, ref string[] calibrationElementIDs)ParametersNameTypeDescriptionselectorStringstringSpecifi

### CalkitManagerCalkitGetCalibrationElementIDs(string, ref string[])

Returns a list of Calibration Element IDs of all Calibration Elements of the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitGetCalibrationElementIDs(string selectorString, ref string[] calibrationElementIDs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| calibrationElementIDs | ref string[] | Upon return, contains the list of Calibration Element IDs of all Calibration Elements of the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetconnectorids__string-ref.html language=enus -->
## TOPIC 00066: CalkitManagerCalkitGetConnectorIDs(string, ref string[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetconnectorids__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetconnectorids__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the list of Connector IDs for all connectors in the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitGetConnectorIDs(string selectorString, ref string[] connectorIDs)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of

### CalkitManagerCalkitGetConnectorIDs(string, ref string[])

Returns the list of Connector IDs for all connectors in the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitGetConnectorIDs(string selectorString, ref string[] connectorIDs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| connectorIDs | ref string[] | Upon return, contains the list of Connector IDs for all connectors in the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetdescription__string-out.html language=enus -->
## TOPIC 00067: CalkitManagerCalkitGetDescription(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetdescription__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetdescription__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the description of the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitGetDescription(string selectorString, out string calkitDescription)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the Calkit ID. Example: "ck

### CalkitManagerCalkitGetDescription(string, out string)

Returns the description of the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitGetDescription(string selectorString, out string calkitDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| calkitDescription | out string | Upon return, contains the description of the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetlrllineautochar__string-out.html language=enus -->
## TOPIC 00068: CalkitManagerCalkitGetLrlLineAutoChar(string, out bool)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetlrllineautochar__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetlrllineautochar__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns whether line parameters are automatically characterized during LRL calibration. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitGetLrlLineAutoChar(string selectorString, out bool autoCharacterizationEnabled)ParametersNameTypeDescriptionselectorStringstringSpecifi

### CalkitManagerCalkitGetLrlLineAutoChar(string, out bool)

Returns whether line parameters are automatically characterized during LRL calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitGetLrlLineAutoChar(string selectorString, out bool autoCharacterizationEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| autoCharacterizationEnabled | out bool | Upon return, contains whether the line parameters are automatically characterized during LRL calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgettrlreferenceplane__string-out.html language=enus -->
## TOPIC 00069: CalkitManagerCalkitGetTrlReferencePlane(string, out RFmxVnaMXCalkitManagerCalkitTrlReferencePlane)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgettrlreferenceplane__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgettrlreferenceplane__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitGetTrlReferencePlane(string selectorString, out RFmxVnaMXCalkitManagerCalkitTrlReferencePlane re

### CalkitManagerCalkitGetTrlReferencePlane(string, out RFmxVnaMXCalkitManagerCalkitTrlReferencePlane)

Returns the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitGetTrlReferencePlane(string selectorString, out RFmxVnaMXCalkitManagerCalkitTrlReferencePlane referencePlane)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| referencePlane | out RFmxVnaMXCalkitManagerCalkitTrlReferencePlane | Upon return, contains the TRL calibration standard (Thru or Reflect) used to define the reference plane. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetversion__string-out.html language=enus -->
## TOPIC 00070: CalkitManagerCalkitGetVersion(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetversion__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitgetversion__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the version string of the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitGetVersion(string selectorString, out string calkitVersion)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the Calkit ID. Example: "ckit::M

### CalkitManagerCalkitGetVersion(string, out string)

Returns the version string of the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitGetVersion(string selectorString, out string calkitVersion)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| calkitVersion | out string | Upon return, contains the version string of the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitremovecalibrationelement__string-string.html language=enus -->
## TOPIC 00071: CalkitManagerCalkitRemoveCalibrationElement(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitremovecalibrationelement__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitremovecalibrationelement__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the Calibration Element identified by its Calibration Element ID from the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitRemoveCalibrationElement(string selectorString, string calibrationElementID)ParametersNameTypeDescriptionselectorStringstringSpecifies

### CalkitManagerCalkitRemoveCalibrationElement(string, string)

Removes the Calibration Element identified by its Calibration Element ID from the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitRemoveCalibrationElement(string selectorString, string calibrationElementID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| calibrationElementID | string | Specifies the ID of the Calibration Element within the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitremoveconnector__string-string.html language=enus -->
## TOPIC 00072: CalkitManagerCalkitRemoveConnector(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitremoveconnector__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitremoveconnector__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a Connector element from the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitRemoveConnector(string selectorString, string connectorID)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the Calkit ID. Example: "ckit:

### CalkitManagerCalkitRemoveConnector(string, string)

Removes a Connector element from the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitRemoveConnector(string selectorString, string connectorID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| connectorID | string | Specifies the ID of the Connector within the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetdescription__string-string.html language=enus -->
## TOPIC 00073: CalkitManagerCalkitSetDescription(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetdescription__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetdescription__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the description for the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitSetDescription(string selectorString, string calkitDescription)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the Calkit ID. Example: "ckit::My

### CalkitManagerCalkitSetDescription(string, string)

Sets the description for the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitSetDescription(string selectorString, string calkitDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| calkitDescription | string | Specifies the description of the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetlrllineautochar__string-bool.html language=enus -->
## TOPIC 00074: CalkitManagerCalkitSetLrlLineAutoChar(string, bool)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetlrllineautochar__string-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetlrllineautochar__string-bool.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether line parameters are automatically characterized during LRL calibration. LRL line auto characterization is applicable only when the Line standards have the same characteristic impedance.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitSetLrlLineAutoChar(

### CalkitManagerCalkitSetLrlLineAutoChar(string, bool)

Configures whether line parameters are automatically characterized during LRL calibration. LRL line auto characterization is applicable only when the Line standards have the same characteristic impedance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitSetLrlLineAutoChar(string selectorString, bool autoCharacterizationEnabled)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| autoCharacterizationEnabled | bool | Specifies the TRL calibration standard (Thru or Reflect) used to define the reference plane. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsettrlreferenceplane__string-rfmxvnamxcalkitmanagercalkittrlreferenceplane.html language=enus -->
## TOPIC 00075: CalkitManagerCalkitSetTrlReferencePlane(string, RFmxVnaMXCalkitManagerCalkitTrlReferencePlane)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsettrlreferenceplane__string-rfmxvnamxcalkitmanagercalkittrlreferenceplane.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsettrlreferenceplane__string-rfmxvnamxcalkitmanagercalkittrlreferenceplane.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration. Use Reflect, if the Thru standard is uncertainly known and the Reflect standard is well defined. Otherwise use the Thru standard to define the reference plane.SyntaxNamespace:

### CalkitManagerCalkitSetTrlReferencePlane(string, RFmxVnaMXCalkitManagerCalkitTrlReferencePlane)

Sets the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration. Use Reflect, if the Thru standard is uncertainly known and the Reflect standard is well defined. Otherwise use the Thru standard to define the reference plane.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitSetTrlReferencePlane(string selectorString, RFmxVnaMXCalkitManagerCalkitTrlReferencePlane referencePlane)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| referencePlane | RFmxVnaMXCalkitManagerCalkitTrlReferencePlane | Specifies the TRL calibration standard (Thru or Reflect) used to define the reference plane. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetversion__string-string.html language=enus -->
## TOPIC 00076: CalkitManagerCalkitSetVersion(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetversion__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagercalkitsetversion__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the version string for the Calkit.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerCalkitSetVersion(string selectorString, string calkitVersion)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitI

### CalkitManagerCalkitSetVersion(string, string)

Sets the version string for the Calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerCalkitSetVersion(string selectorString, string calkitVersion)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the BuildCalkitString(string, string) method to build the selector string. |
| calkitVersion | string | Specifies the version string of the Calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerexportcalkit__string-string-string.html language=enus -->
## TOPIC 00077: CalkitManagerExportCalkit(string, string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerexportcalkit__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerexportcalkit__string-string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exports a Calkit to file.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerExportCalkit(string selectorString, string calkitID, string calkitFilePath)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal co

### CalkitManagerExportCalkit(string, string, string)

Exports a Calkit to file.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerExportCalkit(string selectorString, string calkitID, string calkitFilePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calkitID | string | Specifies the ID for the Calkit in Calkit Manager. |
| calkitFilePath | string | Specifies the absoulte path to the calkit file (.nckt). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagergetcalkitids__string-ref.html language=enus -->
## TOPIC 00078: CalkitManagerGetCalkitIDs(string, ref string[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagergetcalkitids__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagergetcalkitids__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of Calkit IDs for all Calkits currently loaded in Calkit Manager.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerGetCalkitIDs(string selectorString, ref string[] calkitIDs)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name tha

### CalkitManagerGetCalkitIDs(string, ref string[])

Returns a list of Calkit IDs for all Calkits currently loaded in Calkit Manager.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerGetCalkitIDs(string selectorString, ref string[] calkitIDs)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calkitIDs | ref string[] | Upon return, contains the list of Calkit IDs for all Calkit files currently loaded in Calkit Manager. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerimportcalkit__string-string.html language=enus -->
## TOPIC 00079: CalkitManagerImportCalkit(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerimportcalkit__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerimportcalkit__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports a Calkit file into the Calkit Manager.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerImportCalkit(string selectorString, string calkitFilePath)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signa

### CalkitManagerImportCalkit(string, string)

Imports a Calkit file into the Calkit Manager.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerImportCalkit(string selectorString, string calkitFilePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calkitFilePath | string | Specifies the absoulte path to the calkit file (.nckt). |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerremovecalkit__string-string.html language=enus -->
## TOPIC 00080: CalkitManagerRemoveCalkit(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerremovecalkit__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagerremovecalkit__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a Calkit from Calkit Manager.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerRemoveCalkit(string selectorString, string calkitID)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration

### CalkitManagerRemoveCalkit(string, string)

Removes a Calkit from Calkit Manager.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerRemoveCalkit(string selectorString, string calkitID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calkitID | string | Specifies the ID for the Calkit in Calkit Manager. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagervalidatecalkit__string-string.html language=enus -->
## TOPIC 00081: CalkitManagerValidateCalkit(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagervalidatecalkit__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calkitmanagervalidatecalkit__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Validates the consistency of a Calkit definition and returns the status of the validation.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalkitManagerValidateCalkit(string selectorString, string calkitID)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal nam

### CalkitManagerValidateCalkit(string, string)

Validates the consistency of a Calkit definition and returns the status of the validation.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalkitManagerValidateCalkit(string selectorString, string calkitID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calkitID | string | Specifies the ID for the Calkit in Calkit Manager. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetembedfixtures2p__string-string-string-string-rfmxvnamxsparameterorientation-string.html language=enus -->
## TOPIC 00082: CalsetEmbedFixtureS2p(string, string, string, string, RFmxVnaMXSParameterOrientation, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetembedfixtures2p__string-string-string-string-rfmxvnamxsparameterorientation-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetembedfixtures2p__string-string-string-string-rfmxvnamxsparameterorientation-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Embeds the inverse of a given fixture network into a specified calset. The typical use case for this utility is to remove the effect of an adapter that was present during calibration but is not present during later measurements from the Calset itself such that corrected measurements can be performed

### CalsetEmbedFixtureS2p(string, string, string, string, RFmxVnaMXSParameterOrientation, string)

Embeds the inverse of a given fixture network into a specified calset. 
The typical use case for this utility is to remove the effect of an adapter that was present during calibration but is not present during later measurements from the Calset itself such that corrected measurements can be performed without considering the calibration adapter in the measurement de-embedding.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalsetEmbedFixtureS2p(string selectorString, string calsetName, string fixtureS2pFilePath, string vnaPort, RFmxVnaMXSParameterOrientation sParameterOrientation, string newCalsetName)

#### Remarks

- Both Calset Name and New Calset Name are "" (empty string): RFmx modifies the default calset of the signal instance specified in the Selector String, with embedding data. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is "" (empty string) and New Calset Name is non-empty string: RFmx creates a new named calset with the name specified by New Calset Name from the default calset of the signal instance specified in the Selector String and modifies the new named calset with embedding data. This newly created named calset is made accessible across all signals. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string and New Calset Name is "" (empty string): If you do not specify a Signal Name, then RFmx modifies the existing named calset with embedding data. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.
- Both Calset Name and New Calset Name are non-empty string: If you do not specify a Signal Name, then RFmx creates a new named calset with the name specified by New Calset Name from the existing named calset specified by Calset Name and modifies the new named calset with embedding data. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calsetName | string | Specifies the name of the calset. |
| fixtureS2pFilePath | string | Specifies the path to the s2p file containing the fixture S-parameters. |
| vnaPort | string | Specifies the port name of the Calset VNA port. |
| sParameterOrientation | RFmxVnaMXSParameterOrientation | Specifies the orientation of the configured fixture network with respect to VNA port. |
| newCalsetName | string | Specifies the name under which the result Calset (with updated error coefficients) is to be saved. If empty string is provided, the updated Calset is saved back into the original Calset. That is, the original Calset is overwritten. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetgeterrorterm__string-string-rfmxvnamxcalerrorterm-string-string-ref.html language=enus -->
## TOPIC 00083: CalsetGetErrorTerm(string, string, RFmxVnaMXCalErrorTerm, string, string, ref ComplexSingle[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetgeterrorterm__string-string-rfmxvnamxcalerrorterm-string-string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetgeterrorterm__string-string-rfmxvnamxcalerrorterm-string-string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values for a specific error term from either the default calset of the specified signal or a named calset accessible across all signals. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalsetGetErrorTerm(string selectorString, string calsetName, RFmxVnaMXCalErrorTerm errorTermIdent

### CalsetGetErrorTerm(string, string, RFmxVnaMXCalErrorTerm, string, string, ref ComplexSingle[])

Returns values for a specific error term from either the default calset of the specified signal or a named calset accessible across all signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalsetGetErrorTerm(string selectorString, string calsetName, RFmxVnaMXCalErrorTerm errorTermIdentifier, string measurementPort, string sourcePort, ref ComplexSingle[] errorTerm)

#### Remarks

- Calset Name is "" (empty string): RFmx returns the error term values from the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx returns the error term values from the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calsetName | string | Specifies the name of the calset. |
| errorTermIdentifier | RFmxVnaMXCalErrorTerm | Specifies the type of error term in the calset. The error term can take the following values: |
| measurementPort | string | Specifies the VNA port name corresponding to the errorTerm you queried. |
| sourcePort | string | Specifies the VNA port name for which the errorTerm is queried. This parameter is only required to query Error Term defined by port pairs. The valid values of the parameter Error Term Identifier defined for port pairs are transmissionTracking and loadMatch. |
| errorTerm | ref ComplexSingle[] | Upon return, contains the computed error term from the calset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetgetfrequencygrid__string-string-rfmxvnamxcalfrequencygrid-ref.html language=enus -->
## TOPIC 00084: CalsetGetFrequencyGrid(string, string, RFmxVnaMXCalFrequencyGrid, ref double[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetgetfrequencygrid__string-string-rfmxvnamxcalfrequencygrid-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetgetfrequencygrid__string-string-rfmxvnamxcalfrequencygrid-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalsetGetFrequencyGrid(string selectorString, string calsetName, RFmxVnaMXCalFrequencyGrid errorTerm

### CalsetGetFrequencyGrid(string, string, RFmxVnaMXCalFrequencyGrid, ref double[])

Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalsetGetFrequencyGrid(string selectorString, string calsetName, RFmxVnaMXCalFrequencyGrid errorTermIdentifier, ref double[] frequencyGrid)

#### Remarks

- Calset Name is "" (empty string): RFmx returns the error term values from the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx returns the error term values from the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calsetName | string | Specifies the name of the calset. |
| errorTermIdentifier | RFmxVnaMXCalFrequencyGrid | Specifies the type of error term in the calset. The error term can take the following values: |
| frequencyGrid | ref double[] | Upon return, contains the calibration frequency grid from the calset. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetloadfromfile__string-string-string.html language=enus -->
## TOPIC 00085: CalsetLoadFromFile(string, string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetloadfromfile__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetloadfromfile__string-string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads calset from a calset file (*.ncst), either to the default calset of the specified signal or to a named calset accessible across all signals.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalsetLoadFromFile(string selectorString, string calsetName, string calsetFilePath)RemarksBehavi

### CalsetLoadFromFile(string, string, string)

Loads calset from a calset file (*.ncst), either to the default calset of the specified signal or to a named calset accessible across all signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalsetLoadFromFile(string selectorString, string calsetName, string calsetFilePath)

#### Remarks

- Calset Name is "" (empty string): RFmx loads calset from file to the default calset of the signal instance specified in the Selector String and selects the default calset as active calset for the signal. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx loads calset from file to a named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calsetName | string | Specifies the name of the calset. |
| calsetFilePath | string | Specifies the complete path to the file with .ncst extension from which the calset is to be loaded. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetsavetofile__string-string-string.html language=enus -->
## TOPIC 00086: CalsetSaveToFile(string, string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetsavetofile__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-calsetsavetofile__string-string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves to a calset file (*.ncst), either the default calset of the specified signal or a named calset accessible across all signals and corresponding relevant stimulus settings that were used to perform calibration.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CalsetSaveToFile(string sele

### CalsetSaveToFile(string, string, string)

Saves to a calset file (*.ncst), either the default calset of the specified signal or a named calset accessible across all signals and corresponding relevant stimulus settings that were used to perform calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CalsetSaveToFile(string selectorString, string calsetName, string calsetFilePath)

#### Remarks

- Calset Name is "" (empty string): RFmx saves to file, the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx saves the named calset to file. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

SelectActiveCalset(string, string, RFmxVnaMXRestoreConfiguration)

restoreConfiguration

- SweepType=*List*: IF Bandwidth, Power Level per Port, Test Receiver Attenuation per Port, Frequency List
- *SweepType=Linear*: IF Bandwidth, Power Level per Port, Test Receiver Attenuation per Port, Start Frequency, Stop Frequency and Number of Points
- *SweepType=Segment*: Segment IF Bandwidth, Segment Power Level per Port, Segment Test Receiver Attenuation per Port, Segment Start Frequency, Segment Stop Frequency and Segment Number of Points
- *SweepType=CW Time*: IF Bandwidth, Power Level per Port, Test Receiver Attenuation per Port, CW Frequency and Number of Points

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calsetName | string | Specifies the name of the calset. |
| calsetFilePath | string | Specifies the absolute path to the calset file (*.ncst). If the path you specified does not end with '.ncst' file extension, then RFmx automatically adds the extension before saving the file to disk. If the path you specify points to an already existing calset file, then RFmx overwrites that file without warning. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-checkmeasurementstatus__string-out.html language=enus -->
## TOPIC 00087: CheckMeasurementStatus(string, out bool)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-checkmeasurementstatus__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-checkmeasurementstatus__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CheckMeasurementStatus(string selectorString, out bool

### CheckMeasurementStatus(string, out bool)

Checks the status of the measurement. Use this method to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CheckMeasurementStatus(string selectorString, out bool isDone)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildSParameterString(string, int) method to build the selector string. |
| isDone | out bool | Indicates whether the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-clearallnamedresults__string.html language=enus -->
## TOPIC 00088: ClearAllNamedResults(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-clearallnamedresults__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-clearallnamedresults__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the current signal instance.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ClearAllNamedResults(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is used

### ClearAllNamedResults(string)

Clears all results for the current signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ClearAllNamedResults(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-clearcalset__string-string.html language=enus -->
## TOPIC 00089: ClearCalset(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-clearcalset__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-clearcalset__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears either the default calset of the specified signal or a named calset accessible across all signals.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ClearCalset(string selectorString, string calsetName)RemarksBehaviors for different combinations of Calset Name and Signal Name strings a

### ClearCalset(string, string)

Clears either the default calset of the specified signal or a named calset accessible across all signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ClearCalset(string selectorString, string calsetName)

#### Remarks

- Calset Name is "" (empty string): RFmx clears the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx clears the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calsetName | string | Specifies the name of the calset. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-clearmeasurementmemorynames__string.html language=enus -->
## TOPIC 00090: ClearMeasurementMemoryNames(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-clearmeasurementmemorynames__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-clearmeasurementmemorynames__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the measurement memory for the measurement number specified by the Selector String. If Measurement memory name is "" (empty string): RFmx clears all the measurement memories associated with the measurement number. If measurement memory name is non-empty string: RFmx clears the specified measu

### ClearMeasurementMemoryNames(string)

Clears the measurement memory for the measurement number specified by the Selector String. 
 If Measurement memory name is "" (empty string): RFmx clears all the measurement memories associated with the measurement number. 
 If measurement memory name is non-empty string: RFmx clears the specified measurement memory.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ClearMeasurementMemoryNames(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | specifies a selector string comprising of measurement number and the measurement memory name. You must specify the measurement number. Example: sparam0/measmem::(measMemoryName) sparam0 You can use the BuildMeasurementMemoryString(string, string) along with BuildSParameterString(string, int) method to build the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-clearnamedresult__string.html language=enus -->
## TOPIC 00091: ClearNamedResult(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-clearnamedresult__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-clearnamedresult__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ClearNamedResult(string selectorString)ParametersNameTypeDescriptionselectorStringstringSpecifies a selector string comprising of the result name. If you

### ClearNamedResult(string)

Clears a result instance specified by the result name in the Selector String parameter.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ClearNamedResult(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the result name. If you do not specify the result name, the default result instance is used. Example: "" "" "result::r1" You can use the BuildSParameterString(string, int) method to build the selector string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-clonesignalconfiguration__string-out.html language=enus -->
## TOPIC 00092: CloneSignalConfiguration(string, out RFmxVnaMX)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-clonesignalconfiguration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-clonesignalconfiguration__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the property values from an existing signal instance. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CloneSignalConfiguration(string newSignalName, out RFmxVnaMX signalConfiguration)ParametersNameTypeDescriptionnewSignalNamestringSpecifies

### CloneSignalConfiguration(string, out RFmxVnaMX)

Creates a new instance of a signal by copying all the property values from an existing signal instance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CloneSignalConfiguration(string newSignalName, out RFmxVnaMX signalConfiguration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newSignalName | string | Specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example:"signal::NewSigName""NewSigName" |
| signalConfiguration | out RFmxVnaMX | Upon return, contains a new VNA signal instance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-commit__string.html language=enus -->
## TOPIC 00093: Commit(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-commit__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-commit__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this method is optional. RFmxVNA commits settings to the hardware when you call the Initiate(string, string) method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int Commit(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass

### Commit(string)

Commits settings to the hardware. Calling this method is optional. RFmxVNA commits settings to the hardware when you call the [Initiate(string, string)](nationalinstruments-rfmx-vnamx-rfmxvnamx-initiate__string-string.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int Commit(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-configurecalfixturedata__string-double_arr1-complexdouble_arr1-complexdouble_arr1-complexdouble_arr1-complexdouble_arr1-rfmxvnamxcorrectioncalib...d21e4731.html language=enus -->
## TOPIC 00094: ConfigureCalFixtureData(string, double[], ComplexDouble[], ComplexDouble[], ComplexDouble[], ComplexDouble[], RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-configurecalfixturedata__string-double_arr1-complexdouble_arr1-complexdouble_arr1-complexdouble_arr1-complexdouble_arr1-rfmxvnamxcorrectioncalib...d21e4731.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-configurecalfixturedata__string-double_arr1-complexdouble_arr1-complexdouble_arr1-complexdouble_arr1-complexdouble_arr1-rfmxvnamxcorrectioncalib...d21e4731.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ConfigureCalFixtureData(string selectorString, double[] frequency, ComplexDouble[] s11, ComplexDouble[] s21, ComplexDouble[] s12, ComplexDouble[] s22, RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation sParameterOrientation)

### ConfigureCalFixtureData(string, double[], ComplexDouble[], ComplexDouble[], ComplexDouble[], ComplexDouble[], RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureCalFixtureData(string selectorString, double[] frequency, ComplexDouble[] s11, ComplexDouble[] s21, ComplexDouble[] s12, ComplexDouble[] s22, RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation sParameterOrientation)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-configurecorrectionportsubset__string-string_arr1.html language=enus -->
## TOPIC 00095: ConfigureCorrectionPortSubset(string, string[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-configurecorrectionportsubset__string-string_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-configurecorrectionportsubset__string-string_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the subset of ports, that are selected for correction when you set CorrectionEnabled method to True and CorrectionPortSubsetEnabled method to True.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ConfigureCorrectionPortSubset(string selectorString, string[] portSubset)ParametersN

### ConfigureCorrectionPortSubset(string, string[])

Configures the subset of ports, that are selected for correction when you set [CorrectionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionenabled.html) and [CorrectionPortSubsetEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportsubsetenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ConfigureCorrectionPortSubset(string selectorString, string[] portSubset)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| portSubset | string[] | Specifies subset of ports to be corrected as an array of port names. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-copycalset__string-string-string.html language=enus -->
## TOPIC 00096: CopyCalset(string, string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-copycalset__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-copycalset__string-string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies into a new calset either from the default calset of the specified signal or a named calset accessible across all signals.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int CopyCalset(string selectorString, string sourceCalsetName, string newCalsetName)RemarksBehaviors for different com

### CopyCalset(string, string, string)

Copies into a new calset either from the default calset of the specified signal or a named calset accessible across all signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int CopyCalset(string selectorString, string sourceCalsetName, string newCalsetName)

#### Remarks

- Source Calset Name is "" (empty string): RFmx copies the default calset of the signal instance specified in the Selector String into the New Calset you specify. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx copies the named calset into the New Calset you specify. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| sourceCalsetName | string | Specifies the name of the source calset from which calset data will be copied. |
| newCalsetName | string | Specifies the name of the new calset to which calset data will be copied. You must specify this parameter to a non-empty string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getacquisitionchunksize__string-out.html language=enus -->
## TOPIC 00097: GetAcquisitionChunkSize(string, out int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getacquisitionchunksize__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getacquisitionchunksize__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetAcquisitionChunkSize(string selectorString, out int value)

### GetAcquisitionChunkSize(string, out int)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetAcquisitionChunkSize(string selectorString, out int value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getallcalsetnames__string-ref.html language=enus -->
## TOPIC 00098: GetAllCalsetNames(string, ref string[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getallcalsetnames__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getallcalsetnames__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of calset names of all the available named calsets which are accessible across all signals. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetAllCalsetNames(string selectorString, ref string[] calsetNames)ParametersNameTypeDescriptionselectorStringstringIs ignored current

### GetAllCalsetNames(string, ref string[])

Returns an array of calset names of all the available named calsets which are accessible across all signals.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetAllCalsetNames(string selectorString, ref string[] calsetNames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Is ignored currently by this method. |
| calsetNames | ref string[] | Returns an array of calset names for all the available named calsets. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributedouble__string-int-out.html language=enus -->
## TOPIC 00099: GetAttributeDouble(string, int, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributedouble__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributedouble__string-int-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetAttributeDouble(string selectorString, int attributeIdentifier, out double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to th

### GetAttributeDouble(string, int, out double)

Gets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetAttributeDouble(string selectorString, int attributeIdentifier, out double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string. |
| attributeIdentifier | int | Passes the ID of an attribute. |
| value | out double | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributedoublearray__string-int-ref.html language=enus -->
## TOPIC 00100: GetAttributeDoubleArray(string, int, ref double[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributedoublearray__string-int-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributedoublearray__string-int-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a double array attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetAttributeDoubleArray(string selectorString, int attributeIdentifier, ref double[] value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read

### GetAttributeDoubleArray(string, int, ref double[])

Gets the value of a double array attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetAttributeDoubleArray(string selectorString, int attributeIdentifier, ref double[] value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the RFmx SpecAn Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | ref double[] | Contains the value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributeint__string-int-out.html language=enus -->
## TOPIC 00101: GetAttributeInt(string, int, out int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributeint__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributeint__string-int-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of an RFmx 32-bit integer (int32) attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being r

### GetAttributeInt(string, int, out int)

Gets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetAttributeInt(string selectorString, int attributeIdentifier, out int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out int | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributestring__string-int-out.html language=enus -->
## TOPIC 00102: GetAttributeString(string, int, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributestring__string-int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getattributestring__string-int-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of a of an RFmx string. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetAttributeString(string selectorString, int attributeIdentifier, out string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being read. Refer to t

### GetAttributeString(string, int, out string)

Gets the value of a of an RFmx string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetAttributeString(string selectorString, int attributeIdentifier, out string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being read. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | out string | Upon return, contains a value of the specified attribute ID. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getautoifbandwidthscalingenabled__string-out.html language=enus -->
## TOPIC 00103: GetAutoIFBandwidthScalingEnabled(string, out RFmxVnaMXAutoIFBandwidthScalingEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getautoifbandwidthscalingenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getautoifbandwidthscalingenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether IF Bandwidth is scaled down at low frequencies. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetAutoIFBandwidthScalingEnabled(string selectorString, out RFmxVnaMXAutoIFBandwidthScalingEnabled value)RemarksThis method gets the value of AutoIFBandwidthScalingEnabled attribute

### GetAutoIFBandwidthScalingEnabled(string, out RFmxVnaMXAutoIFBandwidthScalingEnabled)

Gets whether IF Bandwidth is scaled down at low frequencies.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetAutoIFBandwidthScalingEnabled(string selectorString, out RFmxVnaMXAutoIFBandwidthScalingEnabled value)

#### Remarks

This method gets the value of [AutoIFBandwidthScalingEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-vnamx-rfmxvnamxautoifbandwidthscalingenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out RFmxVnaMXAutoIFBandwidthScalingEnabled | Upon return, contains whether IF Bandwidth is scaled down at low frequencies. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getaveragingcount__string-out.html language=enus -->
## TOPIC 00104: GetAveragingCount(string, out int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getaveragingcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getaveragingcount__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of times each measurement is repeated and averaged-over. This method is used only when you set the AveragingEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetAveragingCount(string selectorString, out int value)RemarksThis method gets the value of Av

### GetAveragingCount(string, out int)

Gets the number of times each measurement is repeated and averaged-over. This method is used only when you set the [AveragingEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetAveragingCount(string selectorString, out int value)

#### Remarks

This method gets the value of [AveragingCount](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of times each measurement is repeated and averaged-over. This method is used only when you set the AveragingEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationcalkitelectronicorientation__string-out.html language=enus -->
## TOPIC 00105: GetCorrectionCalibrationCalkitElectronicOrientation(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationcalkitelectronicorientation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationcalkitelectronicorientation__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the orientation of the vCal fixture ports with respect to vCal ports. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationCalkitElectronicOrientation(string selectorString, out string value)RemarksThis method gets the value of CorrectionCalibrationCalkitElectronicO

### GetCorrectionCalibrationCalkitElectronicOrientation(string, out string)

Gets the orientation of the vCal fixture ports with respect to vCal ports.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationCalkitElectronicOrientation(string selectorString, out string value)

#### Remarks

This method gets the value of [CorrectionCalibrationCalkitElectronicOrientation](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the orientation of the vCal fixture ports with respect to vCal ports. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationcalkitmechanicalname__string-out.html language=enus -->
## TOPIC 00106: GetCorrectionCalibrationCalkitMechanicalName(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationcalkitmechanicalname__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationcalkitmechanicalname__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the mechanical calkit used for measurement calibration when you set CorrectionCalibrationCalkitType method to Mechanical. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationCalkitMechanicalName(string selectorString, out string value)RemarksThis method

### GetCorrectionCalibrationCalkitMechanicalName(string, out string)

Gets the name of the mechanical calkit used for measurement calibration when you set [CorrectionCalibrationCalkitType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [Mechanical](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationCalkitMechanicalName(string selectorString, out string value)

#### Remarks

This method gets the value of [CorrectionCalibrationCalkitMechanicalName](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out string | Upon return, contains the name of the mechanical calkit used for measurement calibration when you set CorrectionCalibrationCalkitType method to Mechanical. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationestimatedthrudelay__string-out.html language=enus -->
## TOPIC 00107: GetCorrectionCalibrationEstimatedThruDelay(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationestimatedthrudelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationestimatedthrudelay__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the estimated Thru Delay when Thru Method is set to Undefined Thru or Undefined Thru Using Defined Thru. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationEstimatedThruDelay(string selectorString, out double value)RemarksThis method gets the value of CorrectionCa

### GetCorrectionCalibrationEstimatedThruDelay(string, out double)

Gets the estimated Thru Delay when Thru Method is set to *Undefined Thru* or *Undefined Thru Using Defined Thru*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationEstimatedThruDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [CorrectionCalibrationEstimatedThruDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the estimated Thru Delay when Thru Method is set to Undefined Thru or Undefined Thru Using Defined Thru. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures11__string-ref.html language=enus -->
## TOPIC 00108: GetCorrectionCalibrationFixtureS11(string, ref ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures11__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures11__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationFixtureS11(string selectorString, ref ComplexDouble[] value)

### GetCorrectionCalibrationFixtureS11(string, ref ComplexDouble[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationFixtureS11(string selectorString, ref ComplexDouble[] value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures12__string-ref.html language=enus -->
## TOPIC 00109: GetCorrectionCalibrationFixtureS12(string, ref ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures12__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures12__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationFixtureS12(string selectorString, ref ComplexDouble[] value)

### GetCorrectionCalibrationFixtureS12(string, ref ComplexDouble[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationFixtureS12(string selectorString, ref ComplexDouble[] value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures21__string-ref.html language=enus -->
## TOPIC 00110: GetCorrectionCalibrationFixtureS21(string, ref ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures21__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures21__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationFixtureS21(string selectorString, ref ComplexDouble[] value)

### GetCorrectionCalibrationFixtureS21(string, ref ComplexDouble[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationFixtureS21(string selectorString, ref ComplexDouble[] value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures22__string-ref.html language=enus -->
## TOPIC 00111: GetCorrectionCalibrationFixtureS22(string, ref ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures22__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixtures22__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationFixtureS22(string selectorString, ref ComplexDouble[] value)

### GetCorrectionCalibrationFixtureS22(string, ref ComplexDouble[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationFixtureS22(string selectorString, ref ComplexDouble[] value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixturesparameterorientation__string-out.html language=enus -->
## TOPIC 00112: GetCorrectionCalibrationFixtureSParameterOrientation(string, out RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixturesparameterorientation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationfixturesparameterorientation__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationFixtureSParameterOrientation(string selectorString, out RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation value)

### GetCorrectionCalibrationFixtureSParameterOrientation(string, out RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationFixtureSParameterOrientation(string selectorString, out RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationports__string-out.html language=enus -->
## TOPIC 00113: GetCorrectionCalibrationPorts(string, out string[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationports__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ports requested for calibration. Use comma-separated list of ports to specify multiple ports. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationPorts(string selectorString, out string[] value)RemarksThis method gets the value of CorrectionCalibrationPorts att

### GetCorrectionCalibrationPorts(string, out string[])

Gets the ports requested for calibration. Use comma-separated list of ports to specify multiple ports.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationPorts(string selectorString, out string[] value)

#### Remarks

This method gets the value of [CorrectionCalibrationPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out string[] | Upon return, contains the ports requested for calibration. Use comma-separated list of ports to specify multiple ports. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepcount__string-out.html language=enus -->
## TOPIC 00114: GetCorrectionCalibrationStepCount(string, out int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepcount__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepcount__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of steps required to perform calibration. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationStepCount(string selectorString, out int value)RemarksThis method gets the value of CorrectionCalibrationStepCount attribute.ParametersNameTypeDescriptionselect

### GetCorrectionCalibrationStepCount(string, out int)

Gets the number of steps required to perform calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationStepCount(string selectorString, out int value)

#### Remarks

This method gets the value of [CorrectionCalibrationStepCount](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of steps required to perform calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepdescription__string-out.html language=enus -->
## TOPIC 00115: GetCorrectionCalibrationStepDescription(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepdescription__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepdescription__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the description the calibration step. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationStepDescription(string selectorString, out string value)RemarksThis method gets the value of CorrectionCalibrationStepDescription attribute.ParametersNameTypeDescriptionselect

### GetCorrectionCalibrationStepDescription(string, out string)

Gets the description the calibration step.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationStepDescription(string selectorString, out string value)

#### Remarks

This method gets the value of [CorrectionCalibrationStepDescription](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the calstep number. Example: "" or "calstep0". You can use the BuildCalstepString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the description the calibration step. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepportassignment__string-out.html language=enus -->
## TOPIC 00116: GetCorrectionCalibrationStepPortAssignment(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepportassignment__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepportassignment__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationStepPortAssignment(string selectorString, out string value)

### GetCorrectionCalibrationStepPortAssignment(string, out string)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationStepPortAssignment(string selectorString, out string value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepvcalorientation__string-out.html language=enus -->
## TOPIC 00117: GetCorrectionCalibrationStepVCalOrientation(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepvcalorientation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationstepvcalorientation__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationStepVCalOrientation(string selectorString, out string value)

### GetCorrectionCalibrationStepVCalOrientation(string, out string)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationStepVCalOrientation(string selectorString, out string value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationthrucoaxdelay__string-out.html language=enus -->
## TOPIC 00118: GetCorrectionCalibrationThruCoaxDelay(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationthrucoaxdelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationthrucoaxdelay__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the delay of the Thru mechanical standard when CorrectionCalibrationCalkitType method is set to Mechanical and Thru Method method is set to Auto or Undefined Thru. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationThruCoaxDelay

### GetCorrectionCalibrationThruCoaxDelay(string, out double)

Gets the delay of the Thru mechanical standard when [CorrectionCalibrationCalkitType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [Mechanical](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html) and Thru Method method is set to *Auto* or *Undefined Thru*. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationThruCoaxDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [CorrectionCalibrationThruCoaxDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the delay of the Thru mechanical standard when CorrectionCalibrationCalkitType method is set to Mechanical and Thru Method method is set to Auto or Undefined Thru. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationthrumethod__string-out.html language=enus -->
## TOPIC 00119: GetCorrectionCalibrationThruMethod(string, out RFmxVnaMXCorrectionCalibrationThruMethod)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationthrumethod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectioncalibrationthrumethod__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Thru calibration method when Calibration Method method is set to SOLT. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionCalibrationThruMethod(string selectorString, out RFmxVnaMXCorrectionCalibrationThruMethod value)RemarksThis method gets the value of CorrectionCalibr

### GetCorrectionCalibrationThruMethod(string, out RFmxVnaMXCorrectionCalibrationThruMethod)

Gets the Thru calibration method when Calibration Method method is set to *SOLT*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionCalibrationThruMethod(string selectorString, out RFmxVnaMXCorrectionCalibrationThruMethod value)

#### Remarks

This method gets the value of [CorrectionCalibrationThruMethod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationthrumethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXCorrectionCalibrationThruMethod | Upon return, contains the Thru calibration method when Calibration Method method is set to SOLT. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautofrequencymode__string-out.html language=enus -->
## TOPIC 00120: GetCorrectionPortExtensionAutoFrequencyMode(string, out RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautofrequencymode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautofrequencymode__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency mode over which the delay and loss (optional) values are determined. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionPortExtensionAutoFrequencyMode(string selectorString, out RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode value)RemarksThis method gets the

### GetCorrectionPortExtensionAutoFrequencyMode(string, out RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode)

Gets the frequency mode over which the delay and loss (optional) values are determined.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionAutoFrequencyMode(string selectorString, out RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode value)

#### Remarks

This method gets the value of [CorrectionPortExtensionAutoFrequencyMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Sweep](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautofrequencymode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode | Upon return, contains the frequency mode over which the delay and loss (optional) values are determined. The default is Sweep. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautolossenabled__string-out.html language=enus -->
## TOPIC 00121: GetCorrectionPortExtensionAutoLossEnabled(string, out RFmxVnaMXCorrectionPortExtensionAutoLossEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautolossenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautolossenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. SyntaxNam

### GetCorrectionPortExtensionAutoLossEnabled(string, out RFmxVnaMXCorrectionPortExtensionAutoLossEnabled)

Gets whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionAutoLossEnabled(string selectorString, out RFmxVnaMXCorrectionPortExtensionAutoLossEnabled value)

#### Remarks

This method gets the value of [CorrectionPortExtensionAutoLossEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautolossenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXCorrectionPortExtensionAutoLossEnabled | Upon return, contains whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautoregularizationenabled__string-out.html language=enus -->
## TOPIC 00122: GetCorrectionPortExtensionAutoRegularizationEnabled(string, out RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautoregularizationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautoregularizationenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the SetC

### GetCorrectionPortExtensionAutoRegularizationEnabled(string, out RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled)

Gets whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the [SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautolossenabled__string-rfmxvnamxcorrectionportextensionautolossenabled.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautoregularizationenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionAutoRegularizationEnabled(string selectorString, out RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled value)

#### Remarks

This method gets the value of [CorrectionPortExtensionAutoRegularizationEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautoregularizationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled | Upon return, contains whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautostartfrequency__string-out.html language=enus -->
## TOPIC 00123: GetCorrectionPortExtensionAutoStartFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautostartfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautostartfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the start frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int Ge

### GetCorrectionPortExtensionAutoStartFrequency(string, out double)

Gets the start frequency of the user span. This method is used only when you set the [SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautofrequencymode__string-rfmxvnamxcorrectionportextensionautofrequencymode.html) method to *User Span*. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionAutoStartFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [CorrectionPortExtensionAutoStartFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1 GHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the start frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautostopfrequency__string-out.html language=enus -->
## TOPIC 00124: GetCorrectionPortExtensionAutoStopFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautostopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionautostopfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the stop frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int Get

### GetCorrectionPortExtensionAutoStopFrequency(string, out double)

Gets the stop frequency of the user span. This method is used only when you set the [SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautofrequencymode__string-rfmxvnamxcorrectionportextensionautofrequencymode.html) method to *User Span*. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionAutoStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [CorrectionPortExtensionAutoStopFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 2 GHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the stop frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondelay__string-out.html language=enus -->
## TOPIC 00125: GetCorrectionPortExtensionDelay(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondelay__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionPortExtensionDelay(string selectorString, out double value)RemarksThis method gets the value of Correctio

### GetCorrectionPortExtensionDelay(string, out double)

Gets the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [CorrectionPortExtensionDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out double | Upon return, contains the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondelaydomain__string-out.html language=enus -->
## TOPIC 00126: GetCorrectionPortExtensionDelayDomain(string, out RFmxVnaMXCorrectionPortExtensionDelayDomain)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondelaydomain__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondelaydomain__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the delay domain of the port extension when the Port Extension Enabled is set to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionPortExtensionDelayDomain(string selectorString, out RFmxVnaMXCorrectionPortExtensionDelayDomain value)RemarksThis method gets the value o

### GetCorrectionPortExtensionDelayDomain(string, out RFmxVnaMXCorrectionPortExtensionDelayDomain)

Gets the delay domain of the port extension when the Port Extension Enabled is set to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionDelayDomain(string selectorString, out RFmxVnaMXCorrectionPortExtensionDelayDomain value)

#### Remarks

This method gets the value of [CorrectionPortExtensionDelayDomain](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Delay](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondelaydomain.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out RFmxVnaMXCorrectionPortExtensionDelayDomain | Upon return, contains the delay domain of the port extension when the Port Extension Enabled is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondistance__string-out.html language=enus -->
## TOPIC 00127: GetCorrectionPortExtensionDistance(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondistance__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondistance__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is expressed in unit specified by CorrectionPortExtensionDistanceUnit. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionPor

### GetCorrectionPortExtensionDistance(string, out double)

Gets the port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is expressed in unit specified by [CorrectionPortExtensionDistanceUnit](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionDistance(string selectorString, out double value)

#### Remarks

This method gets the value of [CorrectionPortExtensionDistance](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out double | Upon return, contains the port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is expressed in unit specified by Port Extension Distance Unit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondistanceunit__string-out.html language=enus -->
## TOPIC 00128: GetCorrectionPortExtensionDistanceUnit(string, out RFmxVnaMXCorrectionPortExtensionDistanceUnit)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondistanceunit__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensiondistanceunit__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the unit of port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionPortExtensionDistanceUnit(string selectorString, out RFmxVnaMXCorrectionPortE

### GetCorrectionPortExtensionDistanceUnit(string, out RFmxVnaMXCorrectionPortExtensionDistanceUnit)

Gets the unit of port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionDistanceUnit(string selectorString, out RFmxVnaMXCorrectionPortExtensionDistanceUnit value)

#### Remarks

This method gets the value of [CorrectionPortExtensionDistanceUnit](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Meters](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondistanceunit.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out RFmxVnaMXCorrectionPortExtensionDistanceUnit | Upon return, contains the unit of port extension delay in physical length when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss1__string-out.html language=enus -->
## TOPIC 00129: GetCorrectionPortExtensionLoss1(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss1__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss1__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension. If the DC loss and one additional frequency loss, Loss1 at the frequency f1 is known, the total loss at frequency f can be approximated by: Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^0.5) This meth

### GetCorrectionPortExtensionLoss1(string, out double)

Gets the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension. 
 If the DC loss and one additional frequency loss, Loss1 at the frequency f1 is known, the total loss at frequency f can be approximated by: 
 Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^0.5) 
 This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html) and the [CorrectionPortExtensionLoss1Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html). This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionLoss1(string selectorString, out double value)

#### Remarks

This method gets the value of [CorrectionPortExtensionLoss1](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out double | Upon return, contains the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension. If the DC loss and one additional frequency loss, Loss1 at the frequency f1 is known, the total loss at frequency f can be approximated by: Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^0.5) This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss1enabled__string-out.html language=enus -->
## TOPIC 00130: GetCorrectionPortExtensionLoss1Enabled(string, out RFmxVnaMXCorrectionPortExtensionLoss1Enabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss1enabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss1enabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to compensate for the frequency-dependent loss, Loss1, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionPortExtensionLoss1Enabled(string selectorStri

### GetCorrectionPortExtensionLoss1Enabled(string, out RFmxVnaMXCorrectionPortExtensionLoss1Enabled)

Gets whether to compensate for the frequency-dependent loss, Loss1, as part of port extension. This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionLoss1Enabled(string selectorString, out RFmxVnaMXCorrectionPortExtensionLoss1Enabled value)

#### Remarks

This method gets the value of [CorrectionPortExtensionLoss1Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out RFmxVnaMXCorrectionPortExtensionLoss1Enabled | Upon return, contains whether to compensate for the frequency-dependent loss, Loss1, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss2enabled__string-out.html language=enus -->
## TOPIC 00131: GetCorrectionPortExtensionLoss2Enabled(string, out RFmxVnaMXCorrectionPortExtensionLoss2Enabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss2enabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionloss2enabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to compensate for the frequency-dependent loss, Loss2, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpub

### GetCorrectionPortExtensionLoss2Enabled(string, out RFmxVnaMXCorrectionPortExtensionLoss2Enabled)

Gets whether to compensate for the frequency-dependent loss, Loss2, as part of port extension. This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html) and the [CorrectionPortExtensionLoss1Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionLoss2Enabled(string selectorString, out RFmxVnaMXCorrectionPortExtensionLoss2Enabled value)

#### Remarks

This method gets the value of [CorrectionPortExtensionLoss2Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss2enabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out RFmxVnaMXCorrectionPortExtensionLoss2Enabled | Upon return, contains whether to compensate for the frequency-dependent loss, Loss2, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionlossdcloss__string-out.html language=enus -->
## TOPIC 00132: GetCorrectionPortExtensionLossDCLoss(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionlossdcloss__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportextensionlossdcloss__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionPortExtensionLossDCLoss(string selectorString, out dou

### GetCorrectionPortExtensionLossDCLoss(string, out double)

Gets the frequency independent loss to compensate when Port Extension Enabled is set to *True* and Port Extension DC Loss Enabled is set to *True*. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortExtensionLossDCLoss(string selectorString, out double value)

#### Remarks

This method gets the value of [CorrectionPortExtensionLossDCLoss](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out double | Upon return, contains the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetenabled__string-out.html language=enus -->
## TOPIC 00133: GetCorrectionPortSubsetEnabled(string, out RFmxVnaMXCorrectionPortSubsetEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether correction enabled for a subset of ports for which calibration data is avaialble in the calset. This property is used only when you set the CorrectionEnabled property to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionPortSubsetEnabled(string selectorString,

### GetCorrectionPortSubsetEnabled(string, out RFmxVnaMXCorrectionPortSubsetEnabled)

Gets whether correction enabled for a subset of ports for which calibration data is avaialble in the calset. This property is used only when you set the [CorrectionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True**.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortSubsetEnabled(string selectorString, out RFmxVnaMXCorrectionPortSubsetEnabled value)

#### Remarks

This method gets the value of [CorrectionPortSubsetEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is **RFMXVNA_VAL_False**.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXCorrectionPortSubsetEnabled | Upon return, contains whether to enable correction for a subset of set of ports for which calibration data is avaialble. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetfullports__string-out.html language=enus -->
## TOPIC 00134: GetCorrectionPortSubsetFullPorts(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetfullports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetfullports__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the subset of ports, that are selected for full N-Port correction, where N is the number of ports specified in this property. Use comma-separated list of ports to specify multiple ports. The configured measurement is full N-Port corrected if both the measurement receiver and source port are spe

### GetCorrectionPortSubsetFullPorts(string, out string)

Gets the subset of ports, that are selected for full N-Port correction, where N is the number of ports specified in this property. Use comma-separated list of ports to specify multiple ports. The configured measurement is full N-Port corrected if both the measurement receiver and source port are specified using this property. The configured measurement is one-path two-port corrected if one of the measurement ports is specified using this property and another is specified using [CorrectionPortSubsetResponsePorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html). Measurements involving the ports outside [CorrectionPortSubsetFullPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) and [CorrectionPortSubsetResponsePorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) return error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortSubsetFullPorts(string selectorString, out string value)

#### Remarks

This method gets the value of [CorrectionPortSubsetFullPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string. This property is used only when you set the [CorrectionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True** and [CorrectionPortSubsetEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True**.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the subset of ports to be corrected as a comma-separated list of port names when Correction Port Subset Enabled is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetresponseports__string-out.html language=enus -->
## TOPIC 00135: GetCorrectionPortSubsetResponsePorts(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetresponseports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionportsubsetresponseports__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also o

### GetCorrectionPortSubsetResponsePorts(string, out string)

Gets the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also one-path two-port corrected if one of the measurement port is specified using this property and another is specified using [CorrectionPortSubsetFullPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html). Measurements involving the ports outside the [CorrectionPortSubsetResponsePorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) and [CorrectionPortSubsetFullPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) return error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionPortSubsetResponsePorts(string selectorString, out string value)

#### Remarks

This method gets the value of [CorrectionPortSubsetResponsePorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string. This property is used only when you set the [CorrectionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True** and [CorrectionPortSubsetEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True**.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the subset of ports to be corrected as a comma-separated list of port names when Correction Port Subset Enabled is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionswitchportsmultipathcalibration__string-out.html language=enus -->
## TOPIC 00136: GetCorrectionSwitchPortsMultipathCalibration(string, out RFmxVnaMXCorrectionSwitchPortsMultipathCalibration)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionswitchportsmultipathcalibration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getcorrectionswitchportsmultipathcalibration__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetCorrectionSwitchPortsMultipathCalibration(string selectorString, out RFmxVnaMXCorrectionSwitchPortsMultipathCalibration value)

### GetCorrectionSwitchPortsMultipathCalibration(string, out RFmxVnaMXCorrectionSwitchPortsMultipathCalibration)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetCorrectionSwitchPortsMultipathCalibration(string selectorString, out RFmxVnaMXCorrectionSwitchPortsMultipathCalibration value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-geterror__out-out.html language=enus -->
## TOPIC 00137: GetError(out int, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-geterror__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-geterror__out-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest error code and description. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetError(out int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeout intUpon return, contains the latest error code.errorDescriptionout stringUpon return, contains the l

### GetError(out int, out string)

Gets the latest error code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetError(out int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | out int | Upon return, contains the latest error code. |
| errorDescription | out string | Upon return, contains the latest error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-geterrorstring__int-out.html language=enus -->
## TOPIC 00138: GetErrorString(int, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-geterrorstring__int-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-geterrorstring__int-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the status code returned by an RFmxVna function into a string. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetErrorString(int errorCode, out string errorDescription)ParametersNameTypeDescriptionerrorCodeintSpecifies an error or warning code.errorDescriptionout stringUpon retur

### GetErrorString(int, out string)

Converts the status code returned by an RFmxVna function into a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetErrorString(int errorCode, out string errorDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| errorCode | int | Specifies an error or warning code. |
| errorDescription | out string | Upon return, contains the error description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getfrequencylist__string-ref.html language=enus -->
## TOPIC 00139: GetFrequencyList(string, ref double[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getfrequencylist__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getfrequencylist__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list of frequencies at which VNA calibration or measurement (OR just 'VNA measurement') is performed. The frequencies must be in increasing order and must not contain duplicates. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetFrequencyList(string

### GetFrequencyList(string, ref double[])

Gets the list of frequencies at which VNA calibration or measurement (OR just 'VNA measurement') is performed. The frequencies must be in increasing order and must not contain duplicates. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetFrequencyList(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [FrequencyList](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | ref double[] | Upon return, contains the list of frequencies at which VNA calibration or measurement (OR just 'VNA measurement') is performed. The frequencies must be in increasing order and must not contain duplicates. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getgroundterminatedports__string-out.html language=enus -->
## TOPIC 00140: GetGroundTerminatedPorts(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getgroundterminatedports__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getgroundterminatedports__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the instrument port to be ground terminated in case of SM2 devices. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetGroundTerminatedPorts(string selectorString, out string value)RemarksThis method gets the value of GroundTerminatedPorts attribute.ParametersNameTypeDescriptionselecto

### GetGroundTerminatedPorts(string, out string)

Get the instrument port to be ground terminated in case of SM2 devices.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetGroundTerminatedPorts(string selectorString, out string value)

#### Remarks

This method gets the value of [GroundTerminatedPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return contains to be ground terminated in case of SM2 devices. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getifbandwidth__string-out.html language=enus -->
## TOPIC 00141: GetIFBandwidth(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getifbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getifbandwidth__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to a

### GetIFBandwidth(string, out double)

Gets the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetIFBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [IFBandwidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 100kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventlevel__string-out.html language=enus -->
## TOPIC 00142: GetIndexEventLevel(string, out RFmxVnaMXIndexEventLevel)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventlevel__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetIndexEventLevel(string selectorString, out RFmxVnaMXIndexEventLevel value)

### GetIndexEventLevel(string, out RFmxVnaMXIndexEventLevel)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetIndexEventLevel(string selectorString, out RFmxVnaMXIndexEventLevel value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventoutputterminal__string-out.html language=enus -->
## TOPIC 00143: GetIndexEventOutputTerminal(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventoutputterminal__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventoutputterminal__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal for the Index event. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetIndexEventOutputTerminal(string selectorString, out string value)RemarksThis method gets the value of IndexEventOutputTerminal attribute.The default value is "" (empty string).ParametersNa

### GetIndexEventOutputTerminal(string, out string)

Gets the destination terminal for the Index event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetIndexEventOutputTerminal(string selectorString, out string value)

#### Remarks

This method gets the value of [IndexEventOutputTerminal](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "" (empty string).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the destination terminal for exported Index event. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventterminalname__string-out.html language=enus -->
## TOPIC 00144: GetIndexEventTerminalName(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventterminalname__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getindexeventterminalname__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fully qualified signal name as a string. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetIndexEventTerminalName(string selectorString, out string value)RemarksThis method gets the value of IndexEventTerminalName attribute. The default value is "" (empty string).ParametersNameTy

### GetIndexEventTerminalName(string, out string)

Gets the fully qualified signal name as a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetIndexEventTerminalName(string selectorString, out string value)

#### Remarks

This method gets the value of [IndexEventTerminalName](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute. The default value is "" (empty string).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the fully qualified signal name as a string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getlimitedconfigurationchange__string-out.html language=enus -->
## TOPIC 00145: GetLimitedConfigurationChange(string, out RFmxVnaMXLimitedConfigurationChange)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getlimitedconfigurationchange__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getlimitedconfigurationchange__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the set of properties that are considered by NI-RFmx in the locked signal configuration state. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetLimitedConfigurationChange(string selectorString, out RFmxVnaMXLimitedConfigurationChange value)RemarksThis method gets the value of Limite

### GetLimitedConfigurationChange(string, out RFmxVnaMXLimitedConfigurationChange)

Gets the set of properties that are considered by NI-RFmx in the locked signal configuration state.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetLimitedConfigurationChange(string selectorString, out RFmxVnaMXLimitedConfigurationChange value)

#### Remarks

This method gets the value of [LimitedConfigurationChange](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is (format type="bold")RFMXVNA_VAL_Disabled(/format).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXLimitedConfigurationChange | Upon return, contains the set of properties that are considered by NI-RFmx in the locked signal configuration state. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getnumberofsegments__string-out.html language=enus -->
## TOPIC 00146: GetNumberOfSegments(string, out int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getnumberofsegments__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getnumberofsegments__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of segments. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetNumberOfSegments(string selectorString, out int value)RemarksThis method gets the value of NumberOfSegments attribute.The default value is 1.ParametersNameTypeDescriptionselectorStringstringPass an empty string

### GetNumberOfSegments(string, out int)

Gets the number of segments.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetNumberOfSegments(string selectorString, out int value)

#### Remarks

This method gets the value of [NumberOfSegments](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out int | Upon return, contains the number of segments. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpowerlevel__string-out.html language=enus -->
## TOPIC 00147: GetPowerLevel(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpowerlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpowerlevel__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source power level for the VNA port. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPowerLevel(string selectorString, out double value)RemarksThis method gets the value of PowerLevel attribute.The default value is -10.ParametersNameTypeDescripti

### GetPowerLevel(string, out double)

Gets the source power level for the VNA port. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPowerLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [PowerLevel](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is -10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number, signal number and port number. Example: "segment0" or "" or "port0" or "segment0/port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out double | Upon return, contains the source power level for the VNA port. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitionauto__string-out.html language=enus -->
## TOPIC 00148: GetPulseAcquisitionAuto(string, out RFmxVnaMXPulseAcquisitionAuto)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitionauto__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitionauto__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseAcquisitionAuto(string selectorString, out RFmxVnaMXPulseAcquisitionAuto value)RemarksThis

### GetPulseAcquisitionAuto(string, out RFmxVnaMXPulseAcquisitionAuto)

Gets whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulseacquisitionauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseAcquisitionAuto(string selectorString, out RFmxVnaMXPulseAcquisitionAuto value)

#### Remarks

This method gets the value of [PulseAcquisitionAuto](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulseacquisitionauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXPulseAcquisitionAuto | Upon return, contains whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitiondelay__string-out.html language=enus -->
## TOPIC 00149: GetPulseAcquisitionDelay(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitiondelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitiondelay__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True . This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseAcquisition

### GetPulseAcquisitionDelay(string, out double)

Gets the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html) and the [PulseAcquisitionAuto](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html) . This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseAcquisitionDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseAcquisitionDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True . This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitionwidth__string-out.html language=enus -->
## TOPIC 00150: GetPulseAcquisitionWidth(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitionwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseacquisitionwidth__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the width of pulse acquisition when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseAcquisitionWidth(string selectorString, out double value)RemarksThis

### GetPulseAcquisitionWidth(string, out double)

Gets the width of pulse acquisition when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html) and the [PulseAcquisitionAuto](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseAcquisitionWidth(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseAcquisitionWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the width of pulse acquisition when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsedigitaledgetriggersource__string-out.html language=enus -->
## TOPIC 00151: GetPulseDigitalEdgeTriggerSource(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsedigitaledgetriggersource__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsedigitaledgetriggersource__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source of the digital edge pulse trigger. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseDigitalEdgeTriggerSource(string selectorString, out string value)RemarksThis method gets the value of PulseDigitalEdgeTriggerSource attribute.ParametersNameTypeDescriptionselectorStri

### GetPulseDigitalEdgeTriggerSource(string, out string)

Gets the source of the digital edge pulse trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseDigitalEdgeTriggerSource(string selectorString, out string value)

#### Remarks

This method gets the value of [PulseDigitalEdgeTriggerSource](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the source of the digital edge pulse trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratordelay__string-out.html language=enus -->
## TOPIC 00152: GetPulseGeneratorDelay(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratordelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratordelay__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the PulsePeriod method or derived from an external pulse trigger that you specify using the PulseDigitalEdgeTriggerSource

### GetPulseGeneratorDelay(string, out double)

Gets the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the [PulsePeriod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method or derived from an external pulse trigger that you specify using the [PulseDigitalEdgeTriggerSource](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method. You must set the values of the Pulse Generator Delay (s) method and [PulseGeneratorWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method such that Delay + Width does not exceed the value of [PulsePeriod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseGeneratorDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseGeneratorDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the pulsegen number. Example: "" or "pulsegen0". You can use the BuildPulseGeneratorString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the PulsePeriod method or derived from an external pulse trigger that you specify using the PulseDigitalEdgeTriggerSource method. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorenabled__string-out.html language=enus -->
## TOPIC 00153: GetPulseGeneratorEnabled(string, out RFmxVnaMXPulseGeneratorEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable a pulse generator. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseGeneratorEnabled(string selectorString, out RFmxVnaMXPulseGeneratorEnabled value)RemarksThis method gets the value of PulseGeneratorEnabled attribute.The default value is False.ParametersNameT

### GetPulseGeneratorEnabled(string, out RFmxVnaMXPulseGeneratorEnabled)

Gets whether to enable a pulse generator.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseGeneratorEnabled(string selectorString, out RFmxVnaMXPulseGeneratorEnabled value)

#### Remarks

This method gets the value of [PulseGeneratorEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsegeneratorenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the pulsegen number. Example: "" or "pulsegen0". You can use the BuildPulseGeneratorString(string, int) method to build the selector string. |
| value | out RFmxVnaMXPulseGeneratorEnabled | Upon return, contains whether to enable a pulse generator. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorexportoutputterminal__string-out.html language=enus -->
## TOPIC 00154: GetPulseGeneratorExportOutputTerminal(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorexportoutputterminal__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorexportoutputterminal__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal for an exported pulse generator. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseGeneratorExportOutputTerminal(string selectorString, out string value)RemarksThis method gets the value of PulseGeneratorExportOutputTerminal attribute.The default value i

### GetPulseGeneratorExportOutputTerminal(string, out string)

Gets the destination terminal for an exported pulse generator.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseGeneratorExportOutputTerminal(string selectorString, out string value)

#### Remarks

This method gets the value of [PulseGeneratorExportOutputTerminal](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is *Do not export signal*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the pulsegen number. Example: "" or "pulsegen0". You can use the BuildPulseGeneratorString(string, int) method to build the selector string. |
| value | out string | Upon return, contains the destination terminal for an exported pulse generator. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorterminalname__string-out.html language=enus -->
## TOPIC 00155: GetPulseGeneratorTerminalName(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorterminalname__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorterminalname__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fully qualified signal name as a string. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseGeneratorTerminalName(string selectorString, out string value)RemarksThis method gets the value of PulseGeneratorTerminalName attribute.ParametersNameTypeDescriptionselectorStringstrin

### GetPulseGeneratorTerminalName(string, out string)

Gets the fully qualified signal name as a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseGeneratorTerminalName(string selectorString, out string value)

#### Remarks

This method gets the value of [PulseGeneratorTerminalName](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the fully qualified signal name as a string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorwidth__string-out.html language=enus -->
## TOPIC 00156: GetPulseGeneratorWidth(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsegeneratorwidth__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.

### GetPulseGeneratorWidth(string, out double)

Gets the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and [PulseGeneratorWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method such that Delay + Width does not exceed the value of [PulsePeriod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseGeneratorWidth(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseGeneratorWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 100us.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the pulsegen number. Example: "" or "pulsegen0". You can use the BuildPulseGeneratorString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodeenabled__string-out.html language=enus -->
## TOPIC 00157: GetPulseModeEnabled(string, out RFmxVnaMXPulseModeEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodeenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodeenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable pulse mode for VNA measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseModeEnabled(string selectorString, out RFmxVnaMXPulseModeEnabled value)RemarksThis method gets the value of PulseModeEnabled attribute.The default value is False.ParametersNameTyp

### GetPulseModeEnabled(string, out RFmxVnaMXPulseModeEnabled)

Gets whether to enable pulse mode for VNA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseModeEnabled(string selectorString, out RFmxVnaMXPulseModeEnabled value)

#### Remarks

This method gets the value of [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXPulseModeEnabled | Upon return, contains whether to enable pulse mode for VNA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodulatordelay__string-out.html language=enus -->
## TOPIC 00158: GetPulseModulatorDelay(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodulatordelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodulatordelay__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseModulatorDelay(string selectorString, out double value)Rema

### GetPulseModulatorDelay(string, out double)

Gets the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseModulatorDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseModulatorDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodulatorwidth__string-out.html language=enus -->
## TOPIC 00159: GetPulseModulatorWidth(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodulatorwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsemodulatorwidth__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the duration for which the pulse is in ON state when you set the PulseModeEnabled method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseModulatorWidth(string selectorString, out double value)RemarksThis method gets the value of Pul

### GetPulseModulatorWidth(string, out double)

Gets the duration for which the pulse is in ON state when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseModulatorWidth(string selectorString, out double value)

#### Remarks

This method gets the value of [PulseModulatorWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.0001s.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the duration for which the pulse is in ON state when you set the PulseModeEnabled method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseperiod__string-out.html language=enus -->
## TOPIC 00160: GetPulsePeriod(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseperiod__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulseperiod__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulsePeriod(string selectorString, out double value)RemarksThis method gets the value of PulsePeriod attr

### GetPulsePeriod(string, out double)

Gets the interval after which the pulse repeats when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulsePeriod(string selectorString, out double value)

#### Remarks

This method gets the value of [PulsePeriod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.001s.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the interval after which the pulse repeats when you set the PulseModeEnabled method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsetriggertype__string-out.html language=enus -->
## TOPIC 00161: GetPulseTriggerType(string, out RFmxVnaMXPulseTriggerType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsetriggertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getpulsetriggertype__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the pulse trigger type. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetPulseTriggerType(string selectorString, out RFmxVnaMXPulseTriggerType value)RemarksThis method gets the value of PulseTriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStrings

### GetPulseTriggerType(string, out RFmxVnaMXPulseTriggerType)

Gets the pulse trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetPulseTriggerType(string selectorString, out RFmxVnaMXPulseTriggerType value)

#### Remarks

This method gets the value of [PulseTriggerType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsetriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXPulseTriggerType | Upon return, contains the pulse trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventlevel__string-out.html language=enus -->
## TOPIC 00162: GetReadyForTriggerEventLevel(string, out RFmxVnaMXReadyForTriggerEventLevel)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventlevel__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger level for the Ready For Trigger event. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetReadyForTriggerEventLevel(string selectorString, out RFmxVnaMXReadyForTriggerEventLevel value)RemarksThis method gets the value of ReadyForTriggerEventLevel attribute.The default valu

### GetReadyForTriggerEventLevel(string, out RFmxVnaMXReadyForTriggerEventLevel)

Gets the trigger level for the Ready For Trigger event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetReadyForTriggerEventLevel(string selectorString, out RFmxVnaMXReadyForTriggerEventLevel value)

#### Remarks

This method gets the value of [ReadyForTriggerEventLevel](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [ActiveLow](nationalinstruments-rfmx-vnamx-rfmxvnamxreadyfortriggereventlevel.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXReadyForTriggerEventLevel | Upon return, contains the trigger level for the Ready For Trigger event. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventoutputterminal__string-out.html language=enus -->
## TOPIC 00163: GetReadyForTriggerEventOutputTerminal(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventoutputterminal__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventoutputterminal__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the destination terminal for the Ready For Trigger event. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetReadyForTriggerEventOutputTerminal(string selectorString, out string value)RemarksThis method gets the value of ReadyForTriggerEventOutputTerminal attribute.The default value i

### GetReadyForTriggerEventOutputTerminal(string, out string)

Gets the destination terminal for the Ready For Trigger event.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetReadyForTriggerEventOutputTerminal(string selectorString, out string value)

#### Remarks

This method gets the value of [ReadyForTriggerEventOutputTerminal](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is "" (empty string).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the destination terminal for exported Ready For Trigger event. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventterminalname__string-out.html language=enus -->
## TOPIC 00164: GetReadyForTriggerEventTerminalName(string, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventterminalname__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getreadyfortriggereventterminalname__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the fully qualified signal name as a string. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetReadyForTriggerEventTerminalName(string selectorString, out string value)RemarksThis method gets the value of ReadyForTriggerEventTerminalName attribute. The default value is "" (empty stri

### GetReadyForTriggerEventTerminalName(string, out string)

Gets the fully qualified signal name as a string.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetReadyForTriggerEventTerminalName(string selectorString, out string value)

#### Remarks

This method gets the value of [ReadyForTriggerEventTerminalName](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute. The default value is "" (empty string).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out string | Upon return, contains the fully qualified signal name as a string. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getresultfetchtimeout__string-out.html language=enus -->
## TOPIC 00165: GetResultFetchTimeout(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getresultfetchtimeout__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getresultfetchtimeout__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetResultFetchTimeo

### GetResultFetchTimeout(string, out double)

Gets the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetResultFetchTimeout(string selectorString, out double value)

#### Remarks

This method gets the value of [ResultFetchTimeout](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentdwelltime__string-out.html language=enus -->
## TOPIC 00166: GetSegmentDwellTime(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentdwelltime__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentdwelltime__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, r

### GetSegmentDwellTime(string, out double)

Gets the dwell time for the selected segment when Segment Dwell Time Enabled method is set to *True*. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentDwellTime(string selectorString, out double value)

#### Remarks

This method gets the value of [SegmentDwellTime](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the dwell time for the selected segment when Segment Dwell Time Enabled method is set to True. This is the time for which the analyzer waits before acquiring the signal for each measured frequency point of the segment. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentdwelltimeenabled__string-out.html language=enus -->
## TOPIC 00167: GetSegmentDwellTimeEnabled(string, out RFmxVnaMXSegmentDwellTimeEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentdwelltimeenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentdwelltimeenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable individual Dwell Time value configured for each segment by Segment Dwell Time (s) method. If this is set to False, a common value will be used across all segments specified by Dwell Time (s) method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSegmentDwellTimeE

### GetSegmentDwellTimeEnabled(string, out RFmxVnaMXSegmentDwellTimeEnabled)

Gets whether to enable individual Dwell Time value configured for each segment by Segment Dwell Time (s) method. If this is set to [False](nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentdwelltimeenabled.html), a common value will be used across all segments specified by Dwell Time (s) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentDwellTimeEnabled(string selectorString, out RFmxVnaMXSegmentDwellTimeEnabled value)

#### Remarks

This method gets the value of [SegmentDwellTimeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSegmentDwellTimeEnabled | Upon return, contains whether to enable individual Dwell Time value configured for each segment by Segment Dwell Time (s) method. If this is set to False, a common value will be used across all segments specified by Dwell Time (s) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentenabled__string-out.html language=enus -->
## TOPIC 00168: GetSegmentEnabled(string, out RFmxVnaMXSegmentEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable the selected segment for the sweep. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSegmentEnabled(string selectorString, out RFmxVnaMXSegmentEnabled value)RemarksThis method gets the value of SegmentEnabled attribute.The default value is False.ParametersNameTypeD

### GetSegmentEnabled(string, out RFmxVnaMXSegmentEnabled)

Gets whether to enable the selected segment for the sweep.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentEnabled(string selectorString, out RFmxVnaMXSegmentEnabled value)

#### Remarks

This method gets the value of [SegmentEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out RFmxVnaMXSegmentEnabled | Upon return, contains whether to enable the selected segment for the sweep. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentifbandwidth__string-out.html language=enus -->
## TOPIC 00169: GetSegmentIFBandwidth(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentifbandwidth__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentifbandwidth__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 70

### GetSegmentIFBandwidth(string, out double)

Gets the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to *True*. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentIFBandwidth(string selectorString, out double value)

#### Remarks

This method gets the value of [SegmentIFBandwidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 100kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the digital IF filter bandwidth for the selected segment and VNA port when Segment IF Bandwidth Enabled method is set to True. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentifbandwidthenabled__string-out.html language=enus -->
## TOPIC 00170: GetSegmentIFBandwidthEnabled(string, out RFmxVnaMXSegmentIFBandwidthEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentifbandwidthenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentifbandwidthenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSegmentIF

### GetSegmentIFBandwidthEnabled(string, out RFmxVnaMXSegmentIFBandwidthEnabled)

Gets whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to [False](nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentifbandwidthenabled.html), a common value will be used across all segments specified by IF Bandwidth (Hz) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentIFBandwidthEnabled(string selectorString, out RFmxVnaMXSegmentIFBandwidthEnabled value)

#### Remarks

This method gets the value of [SegmentIFBandwidthEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSegmentIFBandwidthEnabled | Upon return, contains whether to enable individual IF bandwidth value configured for each segment by Segment IF Bandwidth (Hz) method. If this is set to False, a common value will be used across all segments specified by IF Bandwidth (Hz) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentnumberoffrequencypoints__string-out.html language=enus -->
## TOPIC 00171: GetSegmentNumberOfFrequencyPoints(string, out int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentnumberoffrequencypoints__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentnumberoffrequencypoints__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of frequency points of the segment at which the measurement needs to be performed. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSegmentNumberOfFrequencyPoints(string selectorString, out int value)RemarksThis method gets the value of SegmentNumberOfFrequencyPoints attr

### GetSegmentNumberOfFrequencyPoints(string, out int)

Gets the number of frequency points of the segment at which the measurement needs to be performed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentNumberOfFrequencyPoints(string selectorString, out int value)

#### Remarks

This method gets the value of [SegmentNumberOfFrequencyPoints](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 21.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out int | Upon return, contains the number of frequency points of the segment at which the measurement needs to be performed. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentpowerlevel__string-out.html language=enus -->
## TOPIC 00172: GetSegmentPowerLevel(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentpowerlevel__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentpowerlevel__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to True. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSegmentPowerLevel(string selectorString, out double value)RemarksThis method gets the

### GetSegmentPowerLevel(string, out double)

Gets the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to *True*. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentPowerLevel(string selectorString, out double value)

#### Remarks

This method gets the value of [SegmentPowerLevel](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is -10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number, signal number and port number. Example: "segment0" or "" or "port0" or "segment0/port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out double | Upon return, contains the source power level for the selected segment and VNA port when Segment Power Level Enabled method is set to True. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentpowerlevelenabled__string-out.html language=enus -->
## TOPIC 00173: GetSegmentPowerLevelEnabled(string, out RFmxVnaMXSegmentPowerLevelEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentpowerlevelenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentpowerlevelenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSegm

### GetSegmentPowerLevelEnabled(string, out RFmxVnaMXSegmentPowerLevelEnabled)

Gets whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to [False](nationalinstruments-rfmx-vnamx-rfmxvnamxsegmentpowerlevelenabled.html), a common value will be used across all segments specified by Power Level(dBm) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentPowerLevelEnabled(string selectorString, out RFmxVnaMXSegmentPowerLevelEnabled value)

#### Remarks

This method gets the value of [SegmentPowerLevelEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSegmentPowerLevelEnabled | Upon return, contains whether to enable individual source power level value configured for each segment by Segment Power Level (dBm) method. If this is set to False, a common value will be used across all segments specified by Power Level(dBm) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentstartfrequency__string-out.html language=enus -->
## TOPIC 00174: GetSegmentStartFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentstartfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentstartfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSegmentStartFrequency(string selectorString, out double value)RemarksThis method gets the value of SegmentStartFrequenc

### GetSegmentStartFrequency(string, out double)

Gets the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentStartFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SegmentStartFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1G.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the lowest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentstopfrequency__string-out.html language=enus -->
## TOPIC 00175: GetSegmentStopFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmentstopfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSegmentStopFrequency(string selectorString, out double value)RemarksThis method gets the value of SegmentStopFrequency

### GetSegmentStopFrequency(string, out double)

Gets the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [SegmentStopFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 2G.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the highest frequency of the segment at which the measurement needs to be performed. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmenttestreceiverattenuation__string-out.html language=enus -->
## TOPIC 00176: GetSegmentTestReceiverAttenuation(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmenttestreceiverattenuation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmenttestreceiverattenuation__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to True. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver.

### GetSegmentTestReceiverAttenuation(string, out double)

Gets the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to *True*. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentTestReceiverAttenuation(string selectorString, out double value)

#### Remarks

This method gets the value of [SegmentTestReceiverAttenuation](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number, signal number and port number. Example: "segment0" or "" or "port0" or "segment0/port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out double | Upon return, contains the test receiver attenuation for the selected segment and VNA port when Segment Test Receiver Attenuation Enabled method is set to True. This is the attenuation value that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmenttestreceiverattenuationenabled__string-out.html language=enus -->
## TOPIC 00177: GetSegmentTestReceiverAttenuationEnabled(string, out RFmxVnaMXSegmentTestReceiverAttenuationEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmenttestreceiverattenuationenabled__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsegmenttestreceiverattenuationenabled__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. SyntaxNamespace: NationalInstru

### GetSegmentTestReceiverAttenuationEnabled(string, out RFmxVnaMXSegmentTestReceiverAttenuationEnabled)

Gets whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to [False](nationalinstruments-rfmx-vnamx-rfmxvnamxsegmenttestreceiverattenuationenabled.html), a common value will be used across all segments specified by Test Receiver Attenuation (dB) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSegmentTestReceiverAttenuationEnabled(string selectorString, out RFmxVnaMXSegmentTestReceiverAttenuationEnabled value)

#### Remarks

This method gets the value of [SegmentTestReceiverAttenuationEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSegmentTestReceiverAttenuationEnabled | Upon return, contains whether to enable individual test receiver attenuation value configured for each segment by Segment Test Receiver Attenuation (dB) method. If this is set to False, a common value will be used across all segments specified by Test Receiver Attenuation (dB) method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsourcepowermode__string-out.html language=enus -->
## TOPIC 00178: GetSourcePowerMode(string, out RFmxVnaMXSourcePowerMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsourcepowermode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsourcepowermode__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether to make VNA measurements with source turned off. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSourcePowerMode(string selectorString, out RFmxVnaMXSourcePowerMode value)RemarksThis method gets the value of SourcePowerMode attribute.The default value is (format type="bold"

### GetSourcePowerMode(string, out RFmxVnaMXSourcePowerMode)

Gets whether to make VNA measurements with source turned off.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSourcePowerMode(string selectorString, out RFmxVnaMXSourcePowerMode value)

#### Remarks

This method gets the value of [SourcePowerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is (format type="bold")RFMXVNA_VAL_Auto(/format).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSourcePowerMode | Upon return, contains whether to make VNA measurements with source turned off. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getstartfrequency__string-out.html language=enus -->
## TOPIC 00179: GetStartFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getstartfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getstartfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetStartFrequency(string selectorString, out double value)RemarksThis method gets the value of StartFrequency attribute.The default value

### GetStartFrequency(string, out double)

Gets the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetStartFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [StartFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1G.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getstopfrequency__string-out.html language=enus -->
## TOPIC 00180: GetStopFrequency(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getstopfrequency__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getstopfrequency__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the highest frequency at which the measurement needs to be performed. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetStopFrequency(string selectorString, out double value)RemarksThis method gets the value of StopFrequency attribute.The default value

### GetStopFrequency(string, out double)

Gets the highest frequency at which the measurement needs to be performed. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetStopFrequency(string selectorString, out double value)

#### Remarks

This method gets the value of [StopFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 2G.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the highest frequency at which the measurement needs to be performed. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweepdelay__string-out.html language=enus -->
## TOPIC 00181: GetSweepDelay(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweepdelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweepdelay__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep delay. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSweepDelay(string selectorString, out double value)RemarksThis method gets the value of SweepDelay attribute.The default value is 0.ParametersNameTypeDescriptionselectorStringstring

### GetSweepDelay(string, out double)

Gets the sweep delay. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSweepDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [SweepDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | out double | Upon return, contains the sweep delay. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweepsequence__string-out.html language=enus -->
## TOPIC 00182: GetSweepSequence(string, out RFmxVnaMXSweepSequence)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweepsequence__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweepsequence__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sequence of acquisitions for various frequency points and source ports. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSweepSequence(string selectorString, out RFmxVnaMXSweepSequence value)RemarksThis method gets the value of SweepSequence attribute.The default value is Standa

### GetSweepSequence(string, out RFmxVnaMXSweepSequence)

Gets the sequence of acquisitions for various frequency points and source ports.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSweepSequence(string selectorString, out RFmxVnaMXSweepSequence value)

#### Remarks

This method gets the value of [SweepSequence](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Standard](nationalinstruments-rfmx-vnamx-rfmxvnamxsweepsequence.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSweepSequence | Upon return, contains the sequence of acquisitions for various frequency points and source ports. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweeptype__string-out.html language=enus -->
## TOPIC 00183: GetSweepType(string, out RFmxVnaMXSweepType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweeptype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getsweeptype__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the sweep type for the measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetSweepType(string selectorString, out RFmxVnaMXSweepType value)RemarksThis method gets the value of SweepType attribute.The default value is List.ParametersNameTypeDescriptionselectorStringstringPass

### GetSweepType(string, out RFmxVnaMXSweepType)

Gets the sweep type for the measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetSweepType(string selectorString, out RFmxVnaMXSweepType value)

#### Remarks

This method gets the value of [SweepType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [List](nationalinstruments-rfmx-vnamx-rfmxvnamxsweeptype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXSweepType | Upon return, contains the sweep type for the measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-gettestreceiverattenuation__string-out.html language=enus -->
## TOPIC 00184: GetTestReceiverAttenuation(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-gettestreceiverattenuation__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-gettestreceiverattenuation__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Te

### GetTestReceiverAttenuation(string, out double)

Gets the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetTestReceiverAttenuation(string selectorString, out double value)

#### Remarks

This method gets the value of [TestReceiverAttenuation](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number, signal number and port number. Example: "segment0" or "" or "port0" or "segment0/port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | out double | Upon return, contains the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggerdelay__string-out.html language=enus -->
## TOPIC 00185: GetTriggerDelay(string, out double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggerdelay__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggerdelay__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger delay. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetTriggerDelay(string selectorString, out double value)RemarksThis method gets the value of TriggerDelay attribute.The default value is 0s.ParametersNameTypeDescriptionselectorStrin

### GetTriggerDelay(string, out double)

Gets the trigger delay. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetTriggerDelay(string selectorString, out double value)

#### Remarks

This method gets the value of [TriggerDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0s.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out double | Upon return, contains the trigger delay. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggermode__string-out.html language=enus -->
## TOPIC 00186: GetTriggerMode(string, out RFmxVnaMXTriggerMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggermode__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggermode__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger mode. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetTriggerMode(string selectorString, out RFmxVnaMXTriggerMode value)RemarksThis method gets the value of TriggerMode attribute.The default value is Signal.ParametersNameTypeDescriptionselectorStringstringPass an empty

### GetTriggerMode(string, out RFmxVnaMXTriggerMode)

Gets the trigger mode.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetTriggerMode(string selectorString, out RFmxVnaMXTriggerMode value)

#### Remarks

This method gets the value of [TriggerMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Signal](nationalinstruments-rfmx-vnamx-rfmxvnamxtriggermode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXTriggerMode | Upon return, contains the trigger mode. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggertype__string-out.html language=enus -->
## TOPIC 00187: GetTriggerType(string, out RFmxVnaMXTriggerType)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggertype__string-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-gettriggertype__string-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the trigger type. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetTriggerType(string selectorString, out RFmxVnaMXTriggerType value)RemarksThis method gets the value of TriggerType attribute.The default value is None.ParametersNameTypeDescriptionselectorStringstringPass an empty st

### GetTriggerType(string, out RFmxVnaMXTriggerType)

Gets the trigger type.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetTriggerType(string selectorString, out RFmxVnaMXTriggerType value)

#### Remarks

This method gets the value of [TriggerType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [None](nationalinstruments-rfmx-vnamx-rfmxvnamxtriggertype.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | out RFmxVnaMXTriggerType | Upon return, contains the trigger type. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getwarning__out-out.html language=enus -->
## TOPIC 00188: GetWarning(out int, out string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getwarning__out-out.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getwarning__out-out.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the latest warning code and description. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetWarning(out int warningCode, out string warningDescription)ParametersNameTypeDescriptionwarningCodeout intUpon return, contains the latest warning code.warningDescriptionout stringUpon return,

### GetWarning(out int, out string)

Gets the latest warning code and description.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetWarning(out int warningCode, out string warningDescription)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| warningCode | out int | Upon return, contains the latest warning code. |
| warningDescription | out string | Upon return, contains the latest warning description. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-getxaxisvalues__string-ref.html language=enus -->
## TOPIC 00189: GetXAxisValues(string, ref double[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-getxaxisvalues__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-getxaxisvalues__string-ref.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the the X-Axis Values (Stimulus) at which VNA calibration or VNA measurement is performed. These values correspond to frequency in Hz for frequency sweeps like List, Linear and Segment sweep. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int GetXAxisValues(string selectorString, ref dou

### GetXAxisValues(string, ref double[])

Gets the the X-Axis Values (Stimulus) at which VNA calibration or VNA measurement is performed. These values correspond to frequency in Hz for frequency sweeps like List, Linear and Segment sweep.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int GetXAxisValues(string selectorString, ref double[] value)

#### Remarks

This method gets the value of [XAxisValues](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | ref double[] | Upon return, contains the the X-Axis Values (Stimulus) at which VNA calibration or VNA measurement is performed. These values correspond to frequency in Hz for frequency sweeps like List, Linear and Segment sweep. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-initiate__string-string.html language=enus -->
## TOPIC 00190: Initiate(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-initiate__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-initiate__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the prope

### Initiate(string, string)

Initiates all enabled measurements. Call this method after configuring the signal and measurement. This method asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [WaitForMeasurementComplete(string, double)](nationalinstruments-rfmx-vnamx-rfmxvnamx-waitformeasurementcomplete__string-double.html) method or [CheckMeasurementStatus(string, out bool)](nationalinstruments-rfmx-vnamx-rfmxvnamx-checkmeasurementstatus__string-out.html) method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int Initiate(string selectorString, string resultName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| resultName | string | Specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-isdisposed.html language=enus -->
## TOPIC 00191: IsDisposed

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-isdisposed.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value that indicates whether the signal has been disposed. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic bool IsDisposed { get; }Remarkstrue if the session is disposed; otherwise, false.

### IsDisposed

Gets a value that indicates whether the signal has been disposed.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public bool IsDisposed { get; }

#### Remarks

true if the session is disposed; otherwise, false.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-loaddatatomeasurementmemoryfromfile__string-string-string-string.html language=enus -->
## TOPIC 00192: LoadDataToMeasurementMemoryFromFile(string, string, string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-loaddatatomeasurementmemoryfromfile__string-string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-loaddatatomeasurementmemoryfromfile__string-string-string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the data from the input file to the measurement memory specified by the Selector String. This method will overwrite the contents of the measurement memory if it already exists. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int LoadDataToMeasurementMemoryFromFile(string selectorString,

### LoadDataToMeasurementMemoryFromFile(string, string, string, string)

Loads the data from the input file to the measurement memory specified by the Selector String. 
 This method will overwrite the contents of the measurement memory if it already exists.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int LoadDataToMeasurementMemoryFromFile(string selectorString, string filePath, string parameter, string measurementMemoryName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies a selector string comprising of the measurement number. You must specify the measurement number. Example: "sparam0" You can use the BuildSParameterString(string, int) method to build the selector string. |
| filePath | string | Specifies the path to the file that contains the measurement data. Example: For S-Parameter measurement use a *.SnP file. |
| parameter | string | Specifies the measurement parameter to load from the file. Example: Specify S11 for an *.S1P file. Specify 'S11 or S12 or S21 or S22 for an *.S2P file. |
| measurementMemoryName | string | Measurement Memory Name specifies the name to associate with the data you load to the measurement memory. Provide a unique name. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-marker.html language=enus -->
## TOPIC 00193: Marker

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-marker.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-marker.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the RFmxVnaMXMarker instance that represents the Marker measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic RFmxVnaMXMarker Marker { get; }

### Marker

Gets the [RFmxVnaMXMarker](nationalinstruments-rfmx-vnamx-rfmxvnamxmarker.html) instance that represents the Marker measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public [RFmxVnaMXMarker](nationalinstruments-rfmx-vnamx-rfmxvnamxmarker.html) Marker { get; }

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-resetattribute__string-rfmxvnamxpropertyid.html language=enus -->
## TOPIC 00194: ResetAttribute(string, RFmxVnaMXPropertyId)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-resetattribute__string-rfmxvnamxpropertyid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-resetattribute__string-rfmxvnamxpropertyid.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the attribute to its default value. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ResetAttribute(string selectorString, RFmxVnaMXPropertyId attributeId)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the property being reset. Refer to the Using a

### ResetAttribute(string, RFmxVnaMXPropertyId)

Resets the attribute to its default value.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ResetAttribute(string selectorString, RFmxVnaMXPropertyId attributeId)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the property being reset. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string. |
| attributeId | RFmxVnaMXPropertyId | Specifies an attribute identifier. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-resettodefault__string.html language=enus -->
## TOPIC 00195: ResetToDefault(string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-resettodefault__string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-resettodefault__string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int ResetToDefault(string selectorString)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name that is passed when creating the signal configuration is used.ReturnsReturns th

### ResetToDefault(string)

Resets a signal to the default values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int ResetToDefault(string selectorString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-selectactivecalset__string-string-rfmxvnamxrestoreconfiguration.html language=enus -->
## TOPIC 00196: SelectActiveCalset(string, string, RFmxVnaMXRestoreConfiguration)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-selectactivecalset__string-string-rfmxvnamxrestoreconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-selectactivecalset__string-string-rfmxvnamxrestoreconfiguration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects either the default calset of the specified signal or a named calset accessible across all signals as active calset for the specified signal.SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SelectActiveCalset(string selectorString, string calsetName, RFmxVnaMXRestoreConfiguration res

### SelectActiveCalset(string, string, RFmxVnaMXRestoreConfiguration)

Selects either the default calset of the specified signal or a named calset accessible across all signals as active calset for the specified signal.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SelectActiveCalset(string selectorString, string calsetName, RFmxVnaMXRestoreConfiguration restoreConfiguration)

#### Remarks

- Calset Name is "" (empty string): RFmx selects the default calset as the active calset for the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: RFmx selects the named calset as the active calset for the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| calsetName | string | Specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. |
| restoreConfiguration | RFmxVnaMXRestoreConfiguration | Specifies whether the stimulus settings from the specified calset should be applied to the signal. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-selectmeasurements__string-rfmxvnamxmeasurementtypes-bool.html language=enus -->
## TOPIC 00197: SelectMeasurements(string, RFmxVnaMXMeasurementTypes, bool)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-selectmeasurements__string-rfmxvnamxmeasurementtypes-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-selectmeasurements__string-rfmxvnamxmeasurementtypes-bool.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SelectMeasurements(string selectorString, RFmxVnaMXMeasurementTypes measurement, bool enableAllTraces)ParametersNameTypeDescriptionselectorStringstringPass an empty string. The signal name t

### SelectMeasurements(string, RFmxVnaMXMeasurementTypes, bool)

Specifies the measurements that you want to enable.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SelectMeasurements(string selectorString, RFmxVnaMXMeasurementTypes measurement, bool enableAllTraces)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| measurement | RFmxVnaMXMeasurementTypes | Specifies the measurement to perform. |
| enableAllTraces | bool | True to enable all traces for the selected measurement; otherwise False. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setacquisitionchunksize__string-int.html language=enus -->
## TOPIC 00198: SetAcquisitionChunkSize(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setacquisitionchunksize__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setacquisitionchunksize__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetAcquisitionChunkSize(string selectorString, int value)

### SetAcquisitionChunkSize(string, int)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetAcquisitionChunkSize(string selectorString, int value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributebool__string-int-bool.html language=enus -->
## TOPIC 00199: SetAttributeBool(string, int, bool)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributebool__string-int-bool.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributebool__string-int-bool.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Bool attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a S

### SetAttributeBool(string, int, bool)

Sets the value of a Bool attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetAttributeBool(string selectorString, int attributeIdentifier, bool value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | bool | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributedouble__string-int-double.html language=enus -->
## TOPIC 00200: SetAttributeDouble(string, int, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributedouble__string-int-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributedouble__string-int-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Double attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Usi

### SetAttributeDouble(string, int, double)

Sets the value of a Double attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetAttributeDouble(string selectorString, int attributeIdentifier, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | double | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributeint__string-int-int.html language=enus -->
## TOPIC 00201: SetAttributeInt(string, int, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributeint__string-int-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributeint__string-int-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a Int attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetAttributeInt(string selectorString, int attributeIdentifier, int value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Using a Sele

### SetAttributeInt(string, int, int)

Sets the value of a Int attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetAttributeInt(string selectorString, int attributeIdentifier, int value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | int | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributestring__string-int-string.html language=enus -->
## TOPIC 00202: SetAttributeString(string, int, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributestring__string-int-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setattributestring__string-int-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of a String attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetAttributeString(string selectorString, int attributeIdentifier, string value)ParametersNameTypeDescriptionselectorStringstringSpecifies the selector string for the attribute being set. Refer to the Usi

### SetAttributeString(string, int, string)

Sets the value of a String attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetAttributeString(string selectorString, int attributeIdentifier, string value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the selector string for the attribute being set. Refer to the Using a Selector String (.NET) topic in the NI-RFmx Vna Help for more information about configuring the selector string. |
| attributeIdentifier | int | Specifies the ID of an attribute. |
| value | string | Specifies the value to which you want to set the attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setaveragingcount__string-int.html language=enus -->
## TOPIC 00203: SetAveragingCount(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setaveragingcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setaveragingcount__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of times each measurement is repeated and averaged-over. This method is used only when you set the AveragingEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetAveragingCount(string selectorString, int value)RemarksThis method sets the value of Averag

### SetAveragingCount(string, int)

Sets the number of times each measurement is repeated and averaged-over. This method is used only when you set the [AveragingEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxaveragingenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetAveragingCount(string selectorString, int value)

#### Remarks

This method sets the value of [AveragingCount](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | int | Specifies the number of times each measurement is repeated and averaged-over. This method is used only when you set the AveragingEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitelectronicorientation__string-string.html language=enus -->
## TOPIC 00204: SetCorrectionCalibrationCalkitElectronicOrientation(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitelectronicorientation__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitelectronicorientation__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the orientation of the vCal fixture ports with respect to vCal ports. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationCalkitElectronicOrientation(string selectorString, string value)RemarksThis method sets the value of CorrectionCalibrationCalkitElectronicOrien

### SetCorrectionCalibrationCalkitElectronicOrientation(string, string)

Sets the orientation of the vCal fixture ports with respect to vCal ports.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationCalkitElectronicOrientation(string selectorString, string value)

#### Remarks

This method sets the value of [CorrectionCalibrationCalkitElectronicOrientation](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the orientation of the vCal fixture ports with respect to vCal ports. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitelectronicresourcename__string-string.html language=enus -->
## TOPIC 00205: SetCorrectionCalibrationCalkitElectronicResourceName(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitelectronicresourcename__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitelectronicresourcename__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the resource name of the electronic calibration module (vCal) used for calibration. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationCalkitElectronicResourceName(string selectorString, string value)RemarksThis method sets the value of CorrectionCalibrationCalkit

### SetCorrectionCalibrationCalkitElectronicResourceName(string, string)

Sets the resource name of the electronic calibration module (vCal) used for calibration.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationCalkitElectronicResourceName(string selectorString, string value)

#### Remarks

This method sets the value of [CorrectionCalibrationCalkitElectronicResourceName](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | string | Specifies the resource name of the electronic calibration module (vCal) used for calibration. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitmechanicalname__string-string.html language=enus -->
## TOPIC 00206: SetCorrectionCalibrationCalkitMechanicalName(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitmechanicalname__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationcalkitmechanicalname__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the name of the mechanical calkit used for measurement calibration when you set CorrectionCalibrationCalkitType method to Mechanical. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationCalkitMechanicalName(string selectorString, string value)RemarksThis method set

### SetCorrectionCalibrationCalkitMechanicalName(string, string)

Sets the name of the mechanical calkit used for measurement calibration when you set [CorrectionCalibrationCalkitType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [Mechanical](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationCalkitMechanicalName(string selectorString, string value)

#### Remarks

This method sets the value of [CorrectionCalibrationCalkitMechanicalName](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | string | Specifies the name of the mechanical calkit used for measurement calibration when you set CorrectionCalibrationCalkitType method to Mechanical. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationconnectortype__string-string.html language=enus -->
## TOPIC 00207: SetCorrectionCalibrationConnectorType(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationconnectortype__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationconnectortype__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the connector type of the DUT. The specified connector type must match be same as that of the selected calkit. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationConnectorType(string selectorString, string value)RemarksThis method sets the value of CorrectionCalib

### SetCorrectionCalibrationConnectorType(string, string)

Sets the connector type of the DUT. The specified connector type must match be same as that of the selected calkit.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationConnectorType(string selectorString, string value)

#### Remarks

This method sets the value of [CorrectionCalibrationConnectorType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | string | Specifies the connector type of the DUT. The specified connector type must match be same as that of the selected calkit. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures11__string-complexdouble_arr1.html language=enus -->
## TOPIC 00208: SetCorrectionCalibrationFixtureS11(string, ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures11__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures11__string-complexdouble_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationFixtureS11(string selectorString, ComplexDouble[] value)

### SetCorrectionCalibrationFixtureS11(string, ComplexDouble[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationFixtureS11(string selectorString, ComplexDouble[] value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures12__string-complexdouble_arr1.html language=enus -->
## TOPIC 00209: SetCorrectionCalibrationFixtureS12(string, ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures12__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures12__string-complexdouble_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationFixtureS12(string selectorString, ComplexDouble[] value)

### SetCorrectionCalibrationFixtureS12(string, ComplexDouble[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationFixtureS12(string selectorString, ComplexDouble[] value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures21__string-complexdouble_arr1.html language=enus -->
## TOPIC 00210: SetCorrectionCalibrationFixtureS21(string, ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures21__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures21__string-complexdouble_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationFixtureS21(string selectorString, ComplexDouble[] value)

### SetCorrectionCalibrationFixtureS21(string, ComplexDouble[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationFixtureS21(string selectorString, ComplexDouble[] value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures22__string-complexdouble_arr1.html language=enus -->
## TOPIC 00211: SetCorrectionCalibrationFixtureS22(string, ComplexDouble[])

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures22__string-complexdouble_arr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixtures22__string-complexdouble_arr1.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationFixtureS22(string selectorString, ComplexDouble[] value)

### SetCorrectionCalibrationFixtureS22(string, ComplexDouble[])

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationFixtureS22(string selectorString, ComplexDouble[] value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixturesparameterorientation__string-rfmxvnamxcorrectioncalibrationfixturesparameterorientation.html language=enus -->
## TOPIC 00212: SetCorrectionCalibrationFixtureSParameterOrientation(string, RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixturesparameterorientation__string-rfmxvnamxcorrectioncalibrationfixturesparameterorientation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationfixturesparameterorientation__string-rfmxvnamxcorrectioncalibrationfixturesparameterorientation.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationFixtureSParameterOrientation(string selectorString, RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation value)

### SetCorrectionCalibrationFixtureSParameterOrientation(string, RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationFixtureSParameterOrientation(string selectorString, RFmxVnaMXCorrectionCalibrationFixtureSParameterOrientation value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationmethod__string-rfmxvnamxcorrectioncalibrationmethod.html language=enus -->
## TOPIC 00213: SetCorrectionCalibrationMethod(string, RFmxVnaMXCorrectionCalibrationMethod)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationmethod__string-rfmxvnamxcorrectioncalibrationmethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationmethod__string-rfmxvnamxcorrectioncalibrationmethod.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the calibration method. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationMethod(string selectorString, RFmxVnaMXCorrectionCalibrationMethod value)RemarksThis method sets the value of CorrectionCalibrationMethod attribute.The default value is (format type="bold")

### SetCorrectionCalibrationMethod(string, RFmxVnaMXCorrectionCalibrationMethod)

Sets the calibration method.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationMethod(string selectorString, RFmxVnaMXCorrectionCalibrationMethod value)

#### Remarks

This method sets the value of [CorrectionCalibrationMethod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is (format type="bold")RFMXVNA_VAL_Sol(/format).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXCorrectionCalibrationMethod | Specifies the calibration method. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepcount__string-int.html language=enus -->
## TOPIC 00214: SetCorrectionCalibrationStepCount(string, int)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepcount__string-int.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepcount__string-int.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationStepCount(string selectorString, int value)

### SetCorrectionCalibrationStepCount(string, int)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationStepCount(string selectorString, int value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepportassignment__string-string.html language=enus -->
## TOPIC 00215: SetCorrectionCalibrationStepPortAssignment(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepportassignment__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepportassignment__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationStepPortAssignment(string selectorString, string value)

### SetCorrectionCalibrationStepPortAssignment(string, string)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationStepPortAssignment(string selectorString, string value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepvcalorientation__string-string.html language=enus -->
## TOPIC 00216: SetCorrectionCalibrationStepVCalOrientation(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepvcalorientation__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationstepvcalorientation__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationStepVCalOrientation(string selectorString, string value)

### SetCorrectionCalibrationStepVCalOrientation(string, string)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationStepVCalOrientation(string selectorString, string value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationthrucoaxdelay__string-double.html language=enus -->
## TOPIC 00217: SetCorrectionCalibrationThruCoaxDelay(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationthrucoaxdelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationthrucoaxdelay__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the delay of the Thru mechanical standard when CorrectionCalibrationCalkitType method is set to Mechanical and Thru Method method is set to Auto or Undefined Thru. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationThruCoaxDelay

### SetCorrectionCalibrationThruCoaxDelay(string, double)

Sets the delay of the Thru mechanical standard when [CorrectionCalibrationCalkitType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [Mechanical](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationcalkittype.html) and Thru Method method is set to *Auto* or *Undefined Thru*. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationThruCoaxDelay(string selectorString, double value)

#### Remarks

This method sets the value of [CorrectionCalibrationThruCoaxDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the delay of the Thru mechanical standard when CorrectionCalibrationCalkitType method is set to Mechanical and Thru Method method is set to Auto or Undefined Thru. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationthrumethod__string-rfmxvnamxcorrectioncalibrationthrumethod.html language=enus -->
## TOPIC 00218: SetCorrectionCalibrationThruMethod(string, RFmxVnaMXCorrectionCalibrationThruMethod)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationthrumethod__string-rfmxvnamxcorrectioncalibrationthrumethod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectioncalibrationthrumethod__string-rfmxvnamxcorrectioncalibrationthrumethod.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Thru calibration method when Calibration Method method is set to SOLT. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionCalibrationThruMethod(string selectorString, RFmxVnaMXCorrectionCalibrationThruMethod value)RemarksThis method sets the value of CorrectionCalibratio

### SetCorrectionCalibrationThruMethod(string, RFmxVnaMXCorrectionCalibrationThruMethod)

Sets the Thru calibration method when Calibration Method method is set to *SOLT*.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionCalibrationThruMethod(string selectorString, RFmxVnaMXCorrectionCalibrationThruMethod value)

#### Remarks

This method sets the value of [CorrectionCalibrationThruMethod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Auto](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectioncalibrationthrumethod.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXCorrectionCalibrationThruMethod | Specifies the Thru calibration method when Calibration Method method is set to SOLT. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautofrequencymode__string-rfmxvnamxcorrectionportextensionautofrequencymode.html language=enus -->
## TOPIC 00219: SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautofrequencymode__string-rfmxvnamxcorrectionportextensionautofrequencymode.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautofrequencymode__string-rfmxvnamxcorrectionportextensionautofrequencymode.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency mode over which the delay and loss (optional) values are determined. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortExtensionAutoFrequencyMode(string selectorString, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode value)RemarksThis method sets the val

### SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode)

Sets the frequency mode over which the delay and loss (optional) values are determined.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionAutoFrequencyMode(string selectorString, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode value)

#### Remarks

This method sets the value of [CorrectionPortExtensionAutoFrequencyMode](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Sweep](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautofrequencymode.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode | Specifies the frequency mode over which the delay and loss (optional) values are determined. The default is Sweep. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautolossenabled__string-rfmxvnamxcorrectionportextensionautolossenabled.html language=enus -->
## TOPIC 00220: SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautolossenabled__string-rfmxvnamxcorrectionportextensionautolossenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautolossenabled__string-rfmxvnamxcorrectionportextensionautolossenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. SyntaxNam

### SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled)

Sets whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionAutoLossEnabled(string selectorString, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled value)

#### Remarks

This method sets the value of [CorrectionPortExtensionAutoLossEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautolossenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXCorrectionPortExtensionAutoLossEnabled | Specifies whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautoregularizationenabled__string-rfmxvnamxcorrectionportextensionautoregularizationenabled.html language=enus -->
## TOPIC 00221: SetCorrectionPortExtensionAutoRegularizationEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautoregularizationenabled__string-rfmxvnamxcorrectionportextensionautoregularizationenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautoregularizationenabled__string-rfmxvnamxcorrectionportextensionautoregularizationenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the SetC

### SetCorrectionPortExtensionAutoRegularizationEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled)

Sets whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the [SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautolossenabled__string-rfmxvnamxcorrectionportextensionautolossenabled.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautoregularizationenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionAutoRegularizationEnabled(string selectorString, RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled value)

#### Remarks

This method sets the value of [CorrectionPortExtensionAutoRegularizationEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionautoregularizationenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXCorrectionPortExtensionAutoRegularizationEnabled | Specifies whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This method is used only when you set the SetCorrectionPortExtensionAutoLossEnabled(string, RFmxVnaMXCorrectionPortExtensionAutoLossEnabled) method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautostartfrequency__string-double.html language=enus -->
## TOPIC 00222: SetCorrectionPortExtensionAutoStartFrequency(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautostartfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautostartfrequency__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int Se

### SetCorrectionPortExtensionAutoStartFrequency(string, double)

Sets the start frequency of the user span. This method is used only when you set the [SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautofrequencymode__string-rfmxvnamxcorrectionportextensionautofrequencymode.html) method to *User Span*. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionAutoStartFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [CorrectionPortExtensionAutoStartFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 1 GHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the start frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautostopfrequency__string-double.html language=enus -->
## TOPIC 00223: SetCorrectionPortExtensionAutoStopFrequency(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautostopfrequency__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautostopfrequency__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the stop frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int Set

### SetCorrectionPortExtensionAutoStopFrequency(string, double)

Sets the stop frequency of the user span. This method is used only when you set the [SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode)](nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionautofrequencymode__string-rfmxvnamxcorrectionportextensionautofrequencymode.html) method to *User Span*. This value is expressed in Hz.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionAutoStopFrequency(string selectorString, double value)

#### Remarks

This method sets the value of [CorrectionPortExtensionAutoStopFrequency](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 2 GHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the stop frequency of the user span. This method is used only when you set the SetCorrectionPortExtensionAutoFrequencyMode(string, RFmxVnaMXCorrectionPortExtensionAutoFrequencyMode) method to User Span. This value is expressed in Hz. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondclossenabled__string-rfmxvnamxcorrectionportextensiondclossenabled.html language=enus -->
## TOPIC 00224: SetCorrectionPortExtensionDCLossEnabled(string, RFmxVnaMXCorrectionPortExtensionDCLossEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondclossenabled__string-rfmxvnamxcorrectionportextensiondclossenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondclossenabled__string-rfmxvnamxcorrectionportextensiondclossenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to compensate for the frequency-independent loss when Port Extension Enabled is set to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortExtensionDCLossEnabled(string selectorString, RFmxVnaMXCorrectionPortExtensionDCLossEnabled value)RemarksThis method se

### SetCorrectionPortExtensionDCLossEnabled(string, RFmxVnaMXCorrectionPortExtensionDCLossEnabled)

Sets whether to compensate for the frequency-independent loss when Port Extension Enabled is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondclossenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionDCLossEnabled(string selectorString, RFmxVnaMXCorrectionPortExtensionDCLossEnabled value)

#### Remarks

This method sets the value of [CorrectionPortExtensionDCLossEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondclossenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | RFmxVnaMXCorrectionPortExtensionDCLossEnabled | Specifies whether to compensate for the frequency-independent loss when Port Extension Enabled is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondelay__string-double.html language=enus -->
## TOPIC 00225: SetCorrectionPortExtensionDelay(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondelay__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortExtensionDelay(string selectorString, double value)RemarksThis method sets the value of CorrectionPor

### SetCorrectionPortExtensionDelay(string, double)

Sets the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionDelay(string selectorString, double value)

#### Remarks

This method sets the value of [CorrectionPortExtensionDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondelaydomain__string-rfmxvnamxcorrectionportextensiondelaydomain.html language=enus -->
## TOPIC 00226: SetCorrectionPortExtensionDelayDomain(string, RFmxVnaMXCorrectionPortExtensionDelayDomain)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondelaydomain__string-rfmxvnamxcorrectionportextensiondelaydomain.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensiondelaydomain__string-rfmxvnamxcorrectionportextensiondelaydomain.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the delay domain of the port extension when the Port Extension Enabled is set to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortExtensionDelayDomain(string selectorString, RFmxVnaMXCorrectionPortExtensionDelayDomain value)RemarksThis method sets the value of Co

### SetCorrectionPortExtensionDelayDomain(string, RFmxVnaMXCorrectionPortExtensionDelayDomain)

Sets the delay domain of the port extension when the Port Extension Enabled is set to True.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionDelayDomain(string selectorString, RFmxVnaMXCorrectionPortExtensionDelayDomain value)

#### Remarks

This method sets the value of [CorrectionPortExtensionDelayDomain](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [Delay](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensiondelaydomain.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | RFmxVnaMXCorrectionPortExtensionDelayDomain | Specifies the delay domain of the port extension when the Port Extension Enabled is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionenabled__string-rfmxvnamxcorrectionportextensionenabled.html language=enus -->
## TOPIC 00227: SetCorrectionPortExtensionEnabled(string, RFmxVnaMXCorrectionPortExtensionEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionenabled__string-rfmxvnamxcorrectionportextensionenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionenabled__string-rfmxvnamxcorrectionportextensionenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable port extension for the VNA port. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortExtensionEnabled(string selectorString, RFmxVnaMXCorrectionPortExtensionEnabled value)RemarksThis method sets the value of CorrectionPortExtensionEnabled attribute.The d

### SetCorrectionPortExtensionEnabled(string, RFmxVnaMXCorrectionPortExtensionEnabled)

Sets whether to enable port extension for the VNA port.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionEnabled(string selectorString, RFmxVnaMXCorrectionPortExtensionEnabled value)

#### Remarks

This method sets the value of [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | RFmxVnaMXCorrectionPortExtensionEnabled | Specifies whether to enable port extension for the VNA port. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss1__string-double.html language=enus -->
## TOPIC 00228: SetCorrectionPortExtensionLoss1(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss1__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss1__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension. If the DC loss and one additional frequency loss, Loss1 at the frequency f1 is known, the total loss at frequency f can be approximated by: Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^0.5) This meth

### SetCorrectionPortExtensionLoss1(string, double)

Sets the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension. 
 If the DC loss and one additional frequency loss, Loss1 at the frequency f1 is known, the total loss at frequency f can be approximated by: 
 Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^0.5) 
 This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html) and the [CorrectionPortExtensionLoss1Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html). This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionLoss1(string selectorString, double value)

#### Remarks

This method sets the value of [CorrectionPortExtensionLoss1](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension. If the DC loss and one additional frequency loss, Loss1 at the frequency f1 is known, the total loss at frequency f can be approximated by: Total loss (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^0.5) This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss1enabled__string-rfmxvnamxcorrectionportextensionloss1enabled.html language=enus -->
## TOPIC 00229: SetCorrectionPortExtensionLoss1Enabled(string, RFmxVnaMXCorrectionPortExtensionLoss1Enabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss1enabled__string-rfmxvnamxcorrectionportextensionloss1enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss1enabled__string-rfmxvnamxcorrectionportextensionloss1enabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to compensate for the frequency-dependent loss, Loss1, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortExtensionLoss1Enabled(string selectorStri

### SetCorrectionPortExtensionLoss1Enabled(string, RFmxVnaMXCorrectionPortExtensionLoss1Enabled)

Sets whether to compensate for the frequency-dependent loss, Loss1, as part of port extension. This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionLoss1Enabled(string selectorString, RFmxVnaMXCorrectionPortExtensionLoss1Enabled value)

#### Remarks

This method sets the value of [CorrectionPortExtensionLoss1Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | RFmxVnaMXCorrectionPortExtensionLoss1Enabled | Specifies whether to compensate for the frequency-dependent loss, Loss1, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss2__string-double.html language=enus -->
## TOPIC 00230: SetCorrectionPortExtensionLoss2(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss2__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss2__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency-dependent loss, Loss2 in dB, to compensate as part of port extension. If in addition to the DC loss and frequency-dependent loss at one frequency (Loss1 at the frequency f1), the loss at a second frequency, Loss2 at frequency f2 is also known, the total loss at frequency f can be

### SetCorrectionPortExtensionLoss2(string, double)

Sets the frequency-dependent loss, Loss2 in dB, to compensate as part of port extension. 
 If in addition to the DC loss and frequency-dependent loss at one frequency (Loss1 at the frequency f1), the loss at a second frequency, Loss2 at frequency f2 is also known, the total loss at frequency f can be approximated by: 
 L (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^b) 
 , where b = log[(abs((Loss1 - DC Loss) / (Loss2 - DC Loss)))] / log(f1 / f2) 
 This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html), the [CorrectionPortExtensionLoss1Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html) and the [CorrectionPortExtensionLoss2Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss2enabled.html). This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionLoss2(string selectorString, double value)

#### Remarks

This method sets the value of [CorrectionPortExtensionLoss2](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0 dB.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the frequency-dependent loss, Loss2 in dB, to compensate as part of port extension. If in addition to the DC loss and frequency-dependent loss at one frequency (Loss1 at the frequency f1), the loss at a second frequency, Loss2 at frequency f2 is also known, the total loss at frequency f can be approximated by: L (f) = DC Loss + ((Loss1 - DC Loss) x (f / f1)^b) , where b = log[(abs((Loss1 - DC Loss) / (Loss2 - DC Loss)))] / log(f1 / f2) This method is used only when you set the CorrectionPortExtensionEnabled method to True, the CorrectionPortExtensionLoss1Enabled method is set to True and the CorrectionPortExtensionLoss2Enabled method is set to True. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss2enabled__string-rfmxvnamxcorrectionportextensionloss2enabled.html language=enus -->
## TOPIC 00231: SetCorrectionPortExtensionLoss2Enabled(string, RFmxVnaMXCorrectionPortExtensionLoss2Enabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss2enabled__string-rfmxvnamxcorrectionportextensionloss2enabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionloss2enabled__string-rfmxvnamxcorrectionportextensionloss2enabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to compensate for the frequency-dependent loss, Loss2, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpub

### SetCorrectionPortExtensionLoss2Enabled(string, RFmxVnaMXCorrectionPortExtensionLoss2Enabled)

Sets whether to compensate for the frequency-dependent loss, Loss2, as part of port extension. This method is used only when you set the [CorrectionPortExtensionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionenabled.html) and the [CorrectionPortExtensionLoss1Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method is set to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss1enabled.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionLoss2Enabled(string selectorString, RFmxVnaMXCorrectionPortExtensionLoss2Enabled value)

#### Remarks

This method sets the value of [CorrectionPortExtensionLoss2Enabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxcorrectionportextensionloss2enabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | RFmxVnaMXCorrectionPortExtensionLoss2Enabled | Specifies whether to compensate for the frequency-dependent loss, Loss2, as part of port extension. This method is used only when you set the CorrectionPortExtensionEnabled method to True and the CorrectionPortExtensionLoss1Enabled method is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionlossdcloss__string-double.html language=enus -->
## TOPIC 00232: SetCorrectionPortExtensionLossDCLoss(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionlossdcloss__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionlossdcloss__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortExtensionLossDCLoss(string selectorString, double

### SetCorrectionPortExtensionLossDCLoss(string, double)

Sets the frequency independent loss to compensate when Port Extension Enabled is set to *True* and Port Extension DC Loss Enabled is set to *True*. This value is expressed in dB.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionLossDCLoss(string selectorString, double value)

#### Remarks

This method sets the value of [CorrectionPortExtensionLossDCLoss](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionvelocityfactor__string-double.html language=enus -->
## TOPIC 00233: SetCorrectionPortExtensionVelocityFactor(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionvelocityfactor__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportextensionvelocityfactor__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the velocity factor of port extension medium when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is unitless. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortExtensionVelocityFactor(string selectorString, double va

### SetCorrectionPortExtensionVelocityFactor(string, double)

Sets the velocity factor of port extension medium when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is unitless.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortExtensionVelocityFactor(string selectorString, double value)

#### Remarks

This method sets the value of [CorrectionPortExtensionVelocityFactor](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute. Velocity Factor of 1 represents speed of light in vacuum. This property is used in conjunction with Port Extension Distance property to compute electrical delay. The default value is 1.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the port number. Example: "" or "port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the velocity factor of port extension medium when Port Extension Enabled is set to True and Port Extension Delay Domain is set to Distance. This value is unitless. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetenabled__string-rfmxvnamxcorrectionportsubsetenabled.html language=enus -->
## TOPIC 00234: SetCorrectionPortSubsetEnabled(string, RFmxVnaMXCorrectionPortSubsetEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetenabled__string-rfmxvnamxcorrectionportsubsetenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetenabled__string-rfmxvnamxcorrectionportsubsetenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable correction for a subset of ports for which calibration data is avaialble in the calset. This property is used only when you set the CorrectionEnabled property to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionPortSubsetEnabled(string selectorStrin

### SetCorrectionPortSubsetEnabled(string, RFmxVnaMXCorrectionPortSubsetEnabled)

Sets whether to enable correction for a subset of ports for which calibration data is avaialble in the calset. This property is used only when you set the [CorrectionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True**.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortSubsetEnabled(string selectorString, RFmxVnaMXCorrectionPortSubsetEnabled value)

#### Remarks

This method sets the value of [CorrectionPortSubsetEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is **RFMXVNA_VAL_False**.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXCorrectionPortSubsetEnabled | Specifies whether to enable correction for a subset of set of ports for which calibration data is avaialble. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetfullports__string-string.html language=enus -->
## TOPIC 00235: SetCorrectionPortSubsetFullPorts(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetfullports__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetfullports__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the subset of ports, that are selected for full N-Port correction, where N is the number of ports specified in this property. Use comma-separated list of ports to specify multiple ports. The configured measurement is full N-Port corrected if both the measurement receiver and source port are spe

### SetCorrectionPortSubsetFullPorts(string, string)

Sets the subset of ports, that are selected for full N-Port correction, where N is the number of ports specified in this property. Use comma-separated list of ports to specify multiple ports. The configured measurement is full N-Port corrected if both the measurement receiver and source port are specified using this property. The configured measurement is one-path two-port corrected if one of the measurement ports is specified using this property and another is specified using [CorrectionPortSubsetResponsePorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html). Measurements involving the ports outside [CorrectionPortSubsetFullPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) and [CorrectionPortSubsetResponsePorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) return error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortSubsetFullPorts(string selectorString, string value)

#### Remarks

This method sets the value of [CorrectionPortSubsetFullPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string. This property is used only when you set the [CorrectionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True** and [CorrectionPortSubsetEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True**. 
 For example, when performing S11 error-corrected measurement for a 1-port DUT using a 2-port VNA and a 2-port calset, VNA generally acquires data by setting the source to port1 first and then to port2. In this case, to achieve faster measurement speed, set this property to **port1**, which lets the VNA acquire data using only source port1 and skips acquiring data with source port2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the subset of ports to be corrected as a comma-separated list of port names when Correction Port Subset Enabled is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetresponseports__string-string.html language=enus -->
## TOPIC 00236: SetCorrectionPortSubsetResponsePorts(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetresponseports__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionportsubsetresponseports__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also o

### SetCorrectionPortSubsetResponsePorts(string, string)

Sets the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also one-path two-port corrected if one of the measurement port is specified using this property and another is specified using [CorrectionPortSubsetFullPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html). Measurements involving the ports outside the [CorrectionPortSubsetResponsePorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) and [CorrectionPortSubsetFullPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) return error.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionPortSubsetResponsePorts(string selectorString, string value)

#### Remarks

This method sets the value of [CorrectionPortSubsetResponsePorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is an empty string. This property is used only when you set the [CorrectionEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True** and [CorrectionPortSubsetEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) property to **True**. 
 For example, when performing S21 error-corrected measurement for a 2-port DUT using a 2-port VNA and a 2-port calset, VNA generally acquires data by setting the source to port1 first and then to port2. To perform S21 one-path two-port error corrected measurement and to achieve faster measurement speed, set this property to **port1, port2**. VNA then acquires data using source port1 and skips acquiring data with source port2.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the subset of ports to be corrected as a comma-separated list of port names when Correction Port Subset Enabled is set to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionswitchportsmultipathcalibration__string-rfmxvnamxcorrectionswitchportsmultipathcalibration.html language=enus -->
## TOPIC 00237: SetCorrectionSwitchPortsMultipathCalibration(string, RFmxVnaMXCorrectionSwitchPortsMultipathCalibration)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionswitchportsmultipathcalibration__string-rfmxvnamxcorrectionswitchportsmultipathcalibration.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setcorrectionswitchportsmultipathcalibration__string-rfmxvnamxcorrectionswitchportsmultipathcalibration.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetCorrectionSwitchPortsMultipathCalibration(string selectorString, RFmxVnaMXCorrectionSwitchPortsMultipathCalibration value)

### SetCorrectionSwitchPortsMultipathCalibration(string, RFmxVnaMXCorrectionSwitchPortsMultipathCalibration)

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetCorrectionSwitchPortsMultipathCalibration(string selectorString, RFmxVnaMXCorrectionSwitchPortsMultipathCalibration value)

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setdigitaledgetriggersource__string-string.html language=enus -->
## TOPIC 00238: SetDigitalEdgeTriggerSource(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setdigitaledgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setdigitaledgetriggersource__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetDigitalEdgeTriggerSource(string selectorString, string value)RemarksThis method sets the value of DigitalEd

### SetDigitalEdgeTriggerSource(string, string)

Sets the source terminal for the digital edge trigger. This method is used only when you set the [TriggerType](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [DigitalEdge](nationalinstruments-rfmx-vnamx-rfmxvnamxtriggertype.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetDigitalEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [DigitalEdgeTriggerSource](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default of this *property is hardware dependent*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the source terminal for the digital edge trigger. This method is used only when you set the TriggerType method to DigitalEdge. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setdwelltime__string-double.html language=enus -->
## TOPIC 00239: SetDwellTime(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setdwelltime__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setdwelltime__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the dwell time. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetDwellTime(string selectorString, double value)ParametersNameTypeDescriptionselectorStringstringSpecifies the segment number. Example: "" or "segment0". You can use the BuildSegmentSt

### SetDwellTime(string, double)

Sets the dwell time. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetDwellTime(string selectorString, double value)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | double | Specifies the time for which the analyzer waits before acquiring the signal for each measurement point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setgroundterminatedports__string-string.html language=enus -->
## TOPIC 00240: SetGroundTerminatedPorts(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setgroundterminatedports__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setgroundterminatedports__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the instrument port to be ground terminated in case of SM2 devices. The ports passed to this method are mutually exclusive to the ports passed to Selected Ports attribute. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetGroundTerminatedPorts(string selectorString, string value)Rema

### SetGroundTerminatedPorts(string, string)

Sets the instrument port to be ground terminated in case of SM2 devices. The ports passed to this method are mutually exclusive to the ports passed to Selected Ports attribute.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetGroundTerminatedPorts(string selectorString, string value)

#### Remarks

This method sets the value of [GroundTerminatedPorts](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the instrument port to be ground terminated in case of SM2 devices. The ports passed to this method are mutually exclusive to the ports passed to Selected Ports attribute. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setifbandwidth__string-double.html language=enus -->
## TOPIC 00241: SetIFBandwidth(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setifbandwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setifbandwidth__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to a

### SetIFBandwidth(string, double)

Sets the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetIFBandwidth(string selectorString, double value)

#### Remarks

This method sets the value of [IFBandwidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 100kHz.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number. Example: "" or "segment0". You can use the BuildSegmentString(string, int) method to build the selector string. |
| value | double | Specifies the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpowerlevel__string-double.html language=enus -->
## TOPIC 00242: SetPowerLevel(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpowerlevel__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpowerlevel__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source power level for the VNA port. This value is expressed in dBm. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPowerLevel(string selectorString, double value)RemarksThis method sets the value of PowerLevel attribute.The default value is -10.ParametersNameTypeDescriptionse

### SetPowerLevel(string, double)

Sets the source power level for the VNA port. This value is expressed in dBm.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPowerLevel(string selectorString, double value)

#### Remarks

This method sets the value of [PowerLevel](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is -10.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the segment number, signal number and port number. Example: "segment0" or "" or "port0" or "segment0/port0". You can use the BuildPortString(string, string) method to build the selector string. |
| value | double | Specifies the source power level for the VNA port. This value is expressed in dBm. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseacquisitionauto__string-rfmxvnamxpulseacquisitionauto.html language=enus -->
## TOPIC 00243: SetPulseAcquisitionAuto(string, RFmxVnaMXPulseAcquisitionAuto)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseacquisitionauto__string-rfmxvnamxpulseacquisitionauto.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseacquisitionauto__string-rfmxvnamxpulseacquisitionauto.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulseAcquisitionAuto(string selectorString, RFmxVnaMXPulseAcquisitionAuto value)RemarksThis met

### SetPulseAcquisitionAuto(string, RFmxVnaMXPulseAcquisitionAuto)

Sets whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulseacquisitionauto.html).

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseAcquisitionAuto(string selectorString, RFmxVnaMXPulseAcquisitionAuto value)

#### Remarks

This method sets the value of [PulseAcquisitionAuto](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulseacquisitionauto.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXPulseAcquisitionAuto | Specifies whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the PulseModeEnabled method to True. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseacquisitiondelay__string-double.html language=enus -->
## TOPIC 00244: SetPulseAcquisitionDelay(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseacquisitiondelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulseacquisitiondelay__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True . This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulseAcquisition

### SetPulseAcquisitionDelay(string, double)

Sets the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html) and the [PulseAcquisitionAuto](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html) . This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseAcquisitionDelay(string selectorString, double value)

#### Remarks

This method sets the value of [PulseAcquisitionDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the PulseModeEnabled method to True and the PulseAcquisitionAuto method to True . This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsedigitaledgetriggersource__string-string.html language=enus -->
## TOPIC 00245: SetPulseDigitalEdgeTriggerSource(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsedigitaledgetriggersource__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsedigitaledgetriggersource__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the source of the digital edge pulse trigger. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulseDigitalEdgeTriggerSource(string selectorString, string value)RemarksThis method sets the value of PulseDigitalEdgeTriggerSource attribute.ParametersNameTypeDescriptionselectorStringst

### SetPulseDigitalEdgeTriggerSource(string, string)

Sets the source of the digital edge pulse trigger.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseDigitalEdgeTriggerSource(string selectorString, string value)

#### Remarks

This method sets the value of [PulseDigitalEdgeTriggerSource](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | string | Specifies the source of the digital edge pulse trigger. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratordelay__string-double.html language=enus -->
## TOPIC 00246: SetPulseGeneratorDelay(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratordelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratordelay__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the PulsePeriod method or derived from an external pulse trigger that you specify using the PulseDigitalEdgeTriggerSource

### SetPulseGeneratorDelay(string, double)

Sets the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the [PulsePeriod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method or derived from an external pulse trigger that you specify using the [PulseDigitalEdgeTriggerSource](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method. You must set the values of the Pulse Generator Delay (s) method and [PulseGeneratorWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method such that Delay + Width does not exceed the value of [PulsePeriod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseGeneratorDelay(string selectorString, double value)

#### Remarks

This method sets the value of [PulseGeneratorDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the pulsegen number. Example: "" or "pulsegen0". You can use the BuildPulseGeneratorString(string, int) method to build the selector string. |
| value | double | Specifies the delay in the start of the pulse generator relative to the internal pulse trigger. The internal pulse trigger could either be generated independently by the VNA based on the PulsePeriod method or derived from an external pulse trigger that you specify using the PulseDigitalEdgeTriggerSource method. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratorexportoutputterminal__string-string.html language=enus -->
## TOPIC 00247: SetPulseGeneratorExportOutputTerminal(string, string)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratorexportoutputterminal__string-string.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratorexportoutputterminal__string-string.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the destination terminal for an exported pulse generator. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulseGeneratorExportOutputTerminal(string selectorString, string value)RemarksThis method sets the value of PulseGeneratorExportOutputTerminal attribute.The default value is Do

### SetPulseGeneratorExportOutputTerminal(string, string)

Sets the destination terminal for an exported pulse generator.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseGeneratorExportOutputTerminal(string selectorString, string value)

#### Remarks

This method sets the value of [PulseGeneratorExportOutputTerminal](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is *Do not export signal*.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the pulsegen number. Example: "" or "pulsegen0". You can use the BuildPulseGeneratorString(string, int) method to build the selector string. |
| value | string | Specifies the destination terminal for an exported pulse generator. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratorwidth__string-double.html language=enus -->
## TOPIC 00248: SetPulseGeneratorWidth(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratorwidth__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsegeneratorwidth__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.

### SetPulseGeneratorWidth(string, double)

Sets the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and [PulseGeneratorWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method such that Delay + Width does not exceed the value of [PulsePeriod](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method. This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseGeneratorWidth(string selectorString, double value)

#### Remarks

This method sets the value of [PulseGeneratorWidth](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 100us.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Specifies the pulsegen number. Example: "" or "pulsegen0". You can use the BuildPulseGeneratorString(string, int) method to build the selector string. |
| value | double | Specifies the pulse width of the selected pulse generator. You must set the values of the Pulse Generator Delay (s) method and PulseGeneratorWidth method such that Delay + Width does not exceed the value of PulsePeriod method. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodeenabled__string-rfmxvnamxpulsemodeenabled.html language=enus -->
## TOPIC 00249: SetPulseModeEnabled(string, RFmxVnaMXPulseModeEnabled)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodeenabled__string-rfmxvnamxpulsemodeenabled.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodeenabled__string-rfmxvnamxpulsemodeenabled.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether to enable pulse mode for VNA measurement. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulseModeEnabled(string selectorString, RFmxVnaMXPulseModeEnabled value)RemarksThis method sets the value of PulseModeEnabled attribute.The default value is False.ParametersNameTypeDes

### SetPulseModeEnabled(string, RFmxVnaMXPulseModeEnabled)

Sets whether to enable pulse mode for VNA measurement.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseModeEnabled(string selectorString, RFmxVnaMXPulseModeEnabled value)

#### Remarks

This method sets the value of [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is [False](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | RFmxVnaMXPulseModeEnabled | Specifies whether to enable pulse mode for VNA measurement. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class

<!--NI_TOPIC bundle=rfmxvna-dotnet-api-ref path=nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodulatordelay__string-double.html language=enus -->
## TOPIC 00250: SetPulseModulatorDelay(string, double)

- bundle_id: `rfmxvna-dotnet-api-ref`
- source_path: `nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodulatordelay__string-double.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-dotnet-api-ref/raw/resource/enus/nationalinstruments-rfmx-vnamx-rfmxvnamx-setpulsemodulatordelay__string-double.html
- document_id: `rfmxvna-dotnet-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds. SyntaxNamespace: NationalInstruments.RFmx.VnaMXpublic int SetPulseModulatorDelay(string selectorString, double value)RemarksT

### SetPulseModulatorDelay(string, double)

Sets the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the [PulseModeEnabled](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) method to [True](nationalinstruments-rfmx-vnamx-rfmxvnamxpulsemodeenabled.html). This value is expressed in seconds.

#### Syntax

**Namespace:**[NationalInstruments.RFmx.VnaMX](nationalinstruments-rfmx-vnamx.html)

public int SetPulseModulatorDelay(string selectorString, double value)

#### Remarks

This method sets the value of [PulseModulatorDelay](nationalinstruments-rfmx-vnamx-rfmxvnamxpropertyid.html) attribute.The default value is 0.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| selectorString | string | Pass an empty string. The signal name that is passed when creating the signal configuration is used. |
| value | double | Specifies the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the PulseModeEnabled method to True. This value is expressed in seconds. |

#### Returns

Returns the status code of this method. The status code either indicates success or describes a warning condition.

Parent topic:

RFmxVnaMX Class
