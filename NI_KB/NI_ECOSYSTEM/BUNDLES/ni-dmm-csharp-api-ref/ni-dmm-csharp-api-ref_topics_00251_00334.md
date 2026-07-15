# NI DOCUMENT BUNDLE: ni-dmm-csharp-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-dmm-csharp-api-ref start=251 end=334 -->
<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-slope.html language=enus -->
## TOPIC 00251: Slope

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-slope.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-slope.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the edge of the signal from the specified trigger source on which the DMM is triggered. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmSlope Slope { get; set; }RemarksSlopeDescriptionPositiveThe driver triggers on the rising edge of the trigger signal.NegativeThe

### Slope

Gets or sets the edge of the signal from the specified trigger source on which the DMM is triggered.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmSlope](nationalinstruments-modularinstruments-nidmm-dmmslope.html) Slope { get; set; }

#### Remarks

| Slope | Description |
| --- | --- |
| Positive | The driver triggers on the rising edge of the trigger signal. |
| Negative | The driver triggers on the falling edge of the trigger signal. |

Parent topic:

DmmTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger-source.html language=enus -->
## TOPIC 00252: Source

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger-source.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the trigger source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmTriggerSource Source { get; set; }RemarksThe following table lists the trigger source and their descriptions. Trigger SourceDescriptionImmediateNo trigger specifiedExternalAUX I/O Connector Trigge

### Source

Gets or sets the trigger source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Source { get; set; }

#### Remarks

| Trigger Source | Description |
| --- | --- |
| Immediate | No trigger specified |
| External | AUX I/O Connector Trigger Line 0 |
| SoftwareTrigger | Software trigger |
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

LabWindows/CVI Trigger Routing

NI Digital Multimeters Help

Initiate

Delay

Note

This property is not supported on the NI 4050.

Parent topic:

DmmTrigger Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtrigger.html language=enus -->
## TOPIC 00253: DmmTrigger Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtrigger.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Customizes the triggering functionality for your application. Derives fromDmmSubObjectIIviDmmTriggerSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmTrigger : DmmSubObject, IIviDmmTriggerRemarksFor more information, refer to the Triggering topic in the NI Digital Multimet

### DmmTrigger Class

Customizes the triggering functionality for your application.

#### Derives from

- DmmSubObject
- IIviDmmTrigger

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmTrigger : DmmSubObject, IIviDmmTrigger

#### Remarks

Triggering

NI Digital Multimeters Help

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Delay | Gets or sets the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. |
| DelayAuto | Gets or sets a value indicating whether the DMM selects the trigger delay automatically. |
| MeasurementCompleteDestination | Gets or sets the destination of the measurement complete (MC) signal. |
| MeasurementCompleteDestinationSlope | Gets or sets the polarity of the generated measurement complete signal. |
| MultiPoint | Gets data on multiple triggers and multiple measurements per trigger. |
| Slope | Gets or sets the edge of the signal from the specified trigger source on which the DMM is triggered. |
| Source | Gets or sets the trigger source. |

#### Methods

| Name | Description |
| --- | --- |
| Configure(DmmTriggerSource, bool) | Configures trigger-related properties. The properties include Source and DelayAuto. |
| Configure(DmmTriggerSource, NationalInstruments.PrecisionTimeSpan) | Configures trigger-related properties. The properties include Source and Delay. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-auxtrig1.html language=enus -->
## TOPIC 00254: AuxTrig1

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-auxtrig1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-auxtrig1.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing Pin 3 on the AUX Connector (AuxTrig1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource AuxTrig1 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, r

### AuxTrig1

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing Pin 3 on the AUX Connector (AuxTrig1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) AuxTrig1 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-equals__object.html language=enus -->
## TOPIC 00255: Equals(object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-equals__object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines whether the specified object is a DmmTriggerSource and is equivalent to this DmmTriggerSource object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectThe System.Object to test. Returnstrue if the spe

### Equals(object)

Determines whether the specified object is a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) and is equivalent to this [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | The System.Object to test. |

#### Returns

true if the specified System.Object is a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) and is equivalent to this [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-external.html language=enus -->
## TOPIC 00256: External

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-external.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-external.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing Pin 9 on the AUX Connector (External). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource External { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, r

### External

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing Pin 9 on the AUX Connector (External).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) External { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-fromstring__string.html language=enus -->
## TOPIC 00257: FromString(string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-fromstring__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-fromstring__string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a DmmTriggerSource object that represents the specified trigger source. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource FromString(string source)ParametersNameTypeDescriptionsourcestringThe trigger source specified as a System.String. ReturnsA DmmT

### FromString(string)

Returns a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object that represents the specified trigger source.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) FromString(string source)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The trigger source specified as a System.String. |

#### Returns

A [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object that represents the specified trigger source.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-gethashcode.html language=enus -->
## TOPIC 00258: GetHashCode()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-gethashcode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a hash code for this DmmTriggerSource object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override int GetHashCode()ReturnsAn integer value that specifies a hash code for this DmmTriggerSource object.

### GetHashCode()

Returns a hash code for this [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override int GetHashCode()

#### Returns

An integer value that specifies a hash code for this [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-immediate.html language=enus -->
## TOPIC 00259: Immediate

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-immediate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-immediate.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing an unspecified trigger sample (Immediate). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Immediate { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each devi

### Immediate

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing an unspecified trigger sample (Immediate).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Immediate { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-lbrtrig1.html language=enus -->
## TOPIC 00260: LbrTrig1

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-lbrtrig1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-lbrtrig1.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing Local Bus Right Trigger Line 1 of the PXI/SCXI combination chassis (LbrTig1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource LbrTrig1 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which

### LbrTrig1

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing Local Bus Right Trigger Line 1 of the PXI/SCXI combination chassis (LbrTig1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) LbrTrig1 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-pxistar.html language=enus -->
## TOPIC 00261: PxiStar

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-pxistar.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-pxistar.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI STAR Trigger Line (PXI Star). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource PxiStar { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer t

### PxiStar

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI STAR Trigger Line (PXI Star).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) PxiStar { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-softwaretrigger.html language=enus -->
## TOPIC 00262: SoftwareTrigger

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-softwaretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-softwaretrigger.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing the software trigger source (Software Trigger). The sample trigger waits until SendSoftwareTrigger is called. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource SoftwareTrigger { get; }RemarksReturns an object of ty

### SoftwareTrigger

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing the software trigger source (Software Trigger). The sample trigger waits until [SendSoftwareTrigger](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-sendsoftwaretrigger.html) is called.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) SoftwareTrigger { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-tostring.html language=enus -->
## TOPIC 00263: ToString()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-tostring.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts this DmmTriggerSource to a human-readable string. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic override string ToString()ReturnsA System.String that corresponds to this DmmTriggerSource.

### ToString()

Converts this [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) to a human-readable string.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public override string ToString()

#### Returns

A System.String that corresponds to this [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl0.html language=enus -->
## TOPIC 00264: Ttl0

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl0.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl0.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI Trigger Line 0 (Ttl0). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Ttl0 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer to the LabV

### Ttl0

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI Trigger Line 0 (Ttl0).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Ttl0 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl1.html language=enus -->
## TOPIC 00265: Ttl1

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl1.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl1.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI Trigger Line 1 (Ttl1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Ttl1 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer to the LabV

### Ttl1

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI Trigger Line 1 (Ttl1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Ttl1 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl2.html language=enus -->
## TOPIC 00266: Ttl2

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl2.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl2.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI Trigger Line 1 (Ttl1). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Ttl2 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer to the LabV

### Ttl2

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI Trigger Line 1 (Ttl1).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Ttl2 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl3.html language=enus -->
## TOPIC 00267: Ttl3

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl3.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl3.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI Trigger Line 3 (Ttl3). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Ttl3 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer to the LabV

### Ttl3

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI Trigger Line 3 (Ttl3).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Ttl3 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl4.html language=enus -->
## TOPIC 00268: Ttl4

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl4.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl4.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI Trigger Line 4 (Ttl4). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Ttl4 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer to the LabV

### Ttl4

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI Trigger Line 4 (Ttl4).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Ttl4 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl5.html language=enus -->
## TOPIC 00269: Ttl5

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl5.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl5.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI Trigger Line 5 (Ttl5). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Ttl5 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer to the LabV

### Ttl5

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI Trigger Line 5 (Ttl5).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Ttl5 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl6.html language=enus -->
## TOPIC 00270: Ttl6

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl6.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl6.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI Trigger Line 6 (Ttl6). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Ttl6 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer to the LabV

### Ttl6

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI Trigger Line 6 (Ttl6).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Ttl6 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl7.html language=enus -->
## TOPIC 00271: Ttl7

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl7.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource-ttl7.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a DmmTriggerSource object representing PXI Trigger Line 7 (Ttl7). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static DmmTriggerSource Ttl7 { get; }RemarksReturns an object of type DmmTriggerSource. To determine which values are supported by each device, refer to the LabV

### Ttl7

Gets a [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) object representing PXI Trigger Line 7 (Ttl7).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html) Ttl7 { get; }

#### Remarks

Returns an object of type [DmmTriggerSource](nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html).

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?context=nidmm_dmm_lvtrigger_routing) topic in the *NI Digital Multimeters Help*.

Parent topic:

DmmTriggerSource Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html language=enus -->
## TOPIC 00272: DmmTriggerSource Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmtriggersource.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a DMM trigger source. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmTriggerSourceRemarksThis class can be used to get a particular DMM trigger source either from the static properties or from a string representation of the trigger source. Thr

### DmmTriggerSource Class

Represents a DMM trigger source.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmTriggerSource

#### Remarks

This class can be used to get a particular DMM trigger source either from the static properties or from a string representation of the trigger source.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| AuxTrig1 | Gets a DmmTriggerSource object representing Pin 3 on the AUX Connector (AuxTrig1). |
| External | Gets a DmmTriggerSource object representing Pin 9 on the AUX Connector (External). |
| Immediate | Gets a DmmTriggerSource object representing an unspecified trigger sample (Immediate). |
| LbrTrig1 | Gets a DmmTriggerSource object representing Local Bus Right Trigger Line 1 of the PXI/SCXI combination chassis (LbrTig1). |
| PxiStar | Gets a DmmTriggerSource object representing PXI STAR Trigger Line (PXI Star). |
| SoftwareTrigger | Gets a DmmTriggerSource object representing the software trigger source (Software Trigger). The sample trigger waits until SendSoftwareTrigger is called. |
| Ttl0 | Gets a DmmTriggerSource object representing PXI Trigger Line 0 (Ttl0). |
| Ttl1 | Gets a DmmTriggerSource object representing PXI Trigger Line 1 (Ttl1). |
| Ttl2 | Gets a DmmTriggerSource object representing PXI Trigger Line 1 (Ttl1). |
| Ttl3 | Gets a DmmTriggerSource object representing PXI Trigger Line 3 (Ttl3). |
| Ttl4 | Gets a DmmTriggerSource object representing PXI Trigger Line 4 (Ttl4). |
| Ttl5 | Gets a DmmTriggerSource object representing PXI Trigger Line 5 (Ttl5). |
| Ttl6 | Gets a DmmTriggerSource object representing PXI Trigger Line 6 (Ttl6). |
| Ttl7 | Gets a DmmTriggerSource object representing PXI Trigger Line 7 (Ttl7). |

#### Methods

| Name | Description |
| --- | --- |
| FromString(string) | Returns a DmmTriggerSource object that represents the specified trigger source. |
| Equals(object) | Determines whether the specified object is a DmmTriggerSource and is equivalent to this DmmTriggerSource object. |
| GetHashCode() | Returns a hash code for this DmmTriggerSource object. |
| ToString() | Converts this DmmTriggerSource to a human-readable string. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwarnings-externalcalibrationbuffertruncated.html language=enus -->
## TOPIC 00273: ExternalCalibrationBufferTruncated

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwarnings-externalcalibrationbuffertruncated.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwarnings-externalcalibrationbuffertruncated.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the string was truncated because it was too large to fit in the EEPROM. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static readonly Guid ExternalCalibrationBufferTruncated

### ExternalCalibrationBufferTruncated

Indicates that the string was truncated because it was too large to fit in the EEPROM.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static readonly Guid ExternalCalibrationBufferTruncated

Parent topic:

DmmWarnings Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwarnings-externalcalibrationselfcalibrationneeded.html language=enus -->
## TOPIC 00274: ExternalCalibrationSelfCalibrationNeeded

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwarnings-externalcalibrationselfcalibrationneeded.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwarnings-externalcalibrationselfcalibrationneeded.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that your data may not be within recommended specifications unless you call SelfCalibrate. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static readonly Guid ExternalCalibrationSelfCalibrationNeeded

### ExternalCalibrationSelfCalibrationNeeded

Indicates that your data may not be within recommended specifications unless you call [SelfCalibrate](nationalinstruments-modularinstruments-nidmm-dmmcalibration-selfcalibrate.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static readonly Guid ExternalCalibrationSelfCalibrationNeeded

Parent topic:

DmmWarnings Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwarnings-overrange.html language=enus -->
## TOPIC 00275: OverRange

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwarnings-overrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwarnings-overrange.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the DMM detected a measurement that was outside of its programmed range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static readonly Guid OverRange

### OverRange

Indicates that the DMM detected a measurement that was outside of its programmed range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static readonly Guid OverRange

Parent topic:

DmmWarnings Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwarnings-resetnotsupported.html language=enus -->
## TOPIC 00276: ResetNotSupported

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwarnings-resetnotsupported.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwarnings-resetnotsupported.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the DMM does not support reset. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static readonly Guid ResetNotSupported

### ResetNotSupported

Indicates that the DMM does *not* support reset.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static readonly Guid ResetNotSupported

Parent topic:

DmmWarnings Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwarnings-simulating.html language=enus -->
## TOPIC 00277: Simulating

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwarnings-simulating.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwarnings-simulating.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the driver is in simulation mode. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static readonly Guid Simulating

### Simulating

Indicates that the driver is in simulation mode.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static readonly Guid Simulating

Parent topic:

DmmWarnings Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwarnings-underrange.html language=enus -->
## TOPIC 00278: UnderRange

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwarnings-underrange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwarnings-underrange.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates that the DMM did not detect a base frequency in the input signal, or the capacitance was too small to be measured accurately. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic static readonly Guid UnderRange

### UnderRange

Indicates that the DMM did *not* detect a base frequency in the input signal, or the capacitance was too small to be measured accurately.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public static readonly Guid UnderRange

Parent topic:

DmmWarnings Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwarnings.html language=enus -->
## TOPIC 00279: DmmWarnings Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwarnings.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwarnings.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides warning codes. Derives fromNoneSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmWarningsRemarksFor more information, refer to the Error and Warning Codes topic in the NI Digital Multimeters Help. Thread SafetyAll members of this type are safe for multithreaded op

### DmmWarnings Class

Provides warning codes.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmWarnings

#### Remarks

For more information, refer to the [Error and Warning Codes](/csh?context=nidmm_dmm_error_codes) topic in the *NI Digital Multimeters Help*.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Fields

| Name | Description |
| --- | --- |
| ExternalCalibrationBufferTruncated | Indicates that the string was truncated because it was too large to fit in the EEPROM. |
| ExternalCalibrationSelfCalibrationNeeded | Indicates that your data may not be within recommended specifications unless you call SelfCalibrate. |
| OverRange | Indicates that the DMM detected a measurement that was outside of its programmed range. |
| ResetNotSupported | Indicates that the DMM does not support reset. |
| Simulating | Indicates that the driver is in simulation mode. |
| UnderRange | Indicates that the DMM did not detect a base frequency in the input signal, or the capacitance was too small to be measured accurately. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-coupling.html language=enus -->
## TOPIC 00280: Coupling

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-coupling.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the coupling during a waveform acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmWaveformCoupling Coupling { get; set; }RemarksValid only for NI 4070/4071/4072. Value is specified by DmmWaveformCoupling. ValueDescriptionACSpecifies AC coupling.DCSpecifi

### Coupling

Gets or sets the coupling during a waveform acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmWaveformCoupling](nationalinstruments-modularinstruments-nidmm-dmmwaveformcoupling.html) Coupling { get; set; }

#### Remarks

Valid only for NI 4070/4071/4072.

DmmWaveformCoupling

| Value | Description |
| --- | --- |
| AC | Specifies AC coupling. |
| DC | Specifies DC coupling. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-dispose.html language=enus -->
## TOPIC 00281: Dispose()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-dispose.html
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

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveform__int-precisiontimespan.html language=enus -->
## TOPIC 00282: FetchWaveform(int, PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveform__int-precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveform__int-precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of values in the form of a waveform datatype from a previously initiated waveform acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic AnalogWaveform< double > FetchWaveform(int pointsToFetch, PrecisionTimeSpan maximumTime)RemarksFor the NI 4070/4071/4072

### FetchWaveform(int, PrecisionTimeSpan)

Returns an array of values in the form of a waveform datatype from a previously initiated waveform acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public AnalogWaveform< double > FetchWaveform(int pointsToFetch, PrecisionTimeSpan maximumTime)

#### Remarks

For the NI 4070/4071/4072 only.

You must call [Initiate](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html) before calling this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. When set to NationalInstruments.PrecisionTimeSpan.MaxValue, the DMM calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of waveform points to return. You specify the total number of points that the DMM acquires in the waveformPoints parameter of ConfigureWaveformAcquisition. The default value is 1. |

#### Returns

Returns an analog waveform datatype which contains the array of values from a previously initiated waveform acquisition and timing information.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value passed for pointsToFetch is out of range. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveformasync__int-precisiontimespan-object.html language=enus -->
## TOPIC 00283: FetchWaveformAsync(int, PrecisionTimeSpan, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveformasync__int-precisiontimespan-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveformasync__int-precisiontimespan-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void FetchWaveformAsync(int pointsToFetch, PrecisionTimeSpan maximumTime, object userState)RemarksFor the NI 4070

### FetchWaveformAsync(int, PrecisionTimeSpan, object)

Asynchronously populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void FetchWaveformAsync(int pointsToFetch, PrecisionTimeSpan maximumTime, object userState)

#### Remarks

For the NI 4070/4071/4072 only.

Two or more asynchronous methods run concurrently on different threads on the same session.

If the user calls dispose on the session object while the asynchronous operation is in progress, the operation completed event will not be raised.

Note

You must call [Initiate](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html) before calling this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. When set to NationalInstruments.PrecisionTimeSpan.MaxValue, the DMM calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of waveform points to return. You specify the total number of points that the DMM acquires in the waveformPoints parameter of ConfigureWaveformAcquisition. The default value is 1. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value passed for parameter pointsToFetch is out of range. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveformcompleted.html language=enus -->
## TOPIC 00284: FetchWaveformCompleted

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveformcompleted.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-fetchwaveformcompleted.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when asynchronous call for fetch waveform operation completes. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic EventHandler< DmmMeasurementEventArgs< AnalogWaveform< double > > > FetchWaveformCompleted

### FetchWaveformCompleted

Occurs when asynchronous call for fetch waveform operation completes.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public EventHandler< [DmmMeasurementEventArgs](nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs.html)< AnalogWaveform< double > > > FetchWaveformCompleted

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedfetchwaveform__int-precisiontimespan-analogwaveform_double..html language=enus -->
## TOPIC 00285: MemoryOptimizedFetchWaveform(int, PrecisionTimeSpan, AnalogWaveform< double >)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedfetchwaveform__int-precisiontimespan-analogwaveform_double..html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedfetchwaveform__int-precisiontimespan-analogwaveform_double..html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic AnalogWaveform< double > MemoryOptimizedFetchWaveform(int pointsToFetch, PrecisionTimeSpan maximumTime, AnalogWaveform< double >

### MemoryOptimizedFetchWaveform(int, PrecisionTimeSpan, AnalogWaveform< double >)

Populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public AnalogWaveform< double > MemoryOptimizedFetchWaveform(int pointsToFetch, PrecisionTimeSpan maximumTime, AnalogWaveform< double > reading)

#### Remarks

For the NI 4070/4071/4072 only.

You must call [Initiate](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html) before calling this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. When set to NationalInstruments.PrecisionTimeSpan.MaxValue, the DMM calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of waveform points to return. You specify the total number of points that the DMM acquires in the waveformPoints parameter of ConfigureWaveformAcquisition. The default value is 1. |
| reading | AnalogWaveform< double > | The pre-allocated Waveform to be used to return the fetch results. This parameter cannot be null. |

#### Returns

Returns an analog waveform datatype which contains the array of values from a previously initiated waveform acquisition and timing information.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value passed for parameter pointsToFetch is not positve. |
| Ivi.Driver.IOTimeoutException | The method does not complete within the time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |
| System.ArgumentNullException | The value for reading is null. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedfetchwaveformasync__int-precisiontimespan-analogwaveform_double_-object.html language=enus -->
## TOPIC 00286: MemoryOptimizedFetchWaveformAsync(int, PrecisionTimeSpan, AnalogWaveform< double >, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedfetchwaveformasync__int-precisiontimespan-analogwaveform_double_-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedfetchwaveformasync__int-precisiontimespan-analogwaveform_double_-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void MemoryOptimizedFetchWaveformAsync(int pointsToFetch, PrecisionTimeSpan maximumTime, AnalogWaveform< double >

### MemoryOptimizedFetchWaveformAsync(int, PrecisionTimeSpan, AnalogWaveform< double >, object)

Asynchronously populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void MemoryOptimizedFetchWaveformAsync(int pointsToFetch, PrecisionTimeSpan maximumTime, AnalogWaveform< double > reading, object userState)

#### Remarks

For the NI 4070/4071/4072 only.

Two or more asynchronous methods run concurrently on different threads on the same session.

If the user calls dispose on the session object while the asynchronous operation is in progress, the operation completed event will not be raised.

Note

You must call [Initiate](nationalinstruments-modularinstruments-nidmm-dmmmeasurement-initiate.html) before calling this method.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. When set to NationalInstruments.PrecisionTimeSpan.MaxValue, the DMM calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of waveform points to return. You specify the total number of points that the DMM acquires in the waveformPoints parameter of ConfigureWaveformAcquisition. The default value is 1. |
| reading | AnalogWaveform< double > | The pre-allocated Waveform to be used to return the fetch results. This parameter cannot be null. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value passed for parameter pointsToFetch is out of range. |
| System.ArgumentNullException | The value for parameter reading is null. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedreadwaveform__int-precisiontimespan-analogwaveform_double..html language=enus -->
## TOPIC 00287: MemoryOptimizedReadWaveform(int, PrecisionTimeSpan, AnalogWaveform< double >)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedreadwaveform__int-precisiontimespan-analogwaveform_double..html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedreadwaveform__int-precisiontimespan-analogwaveform_double..html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires and populates a pre-allocated waveform buffer with values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic AnalogWaveform< double > MemoryOptimizedReadWaveform(int pointsToFetch, PrecisionTimeSpan maximumTime, AnalogWaveform< double > reading)RemarksFor the NI 4070/4071/

### MemoryOptimizedReadWaveform(int, PrecisionTimeSpan, AnalogWaveform< double >)

Acquires and populates a pre-allocated waveform buffer with values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public AnalogWaveform< double > MemoryOptimizedReadWaveform(int pointsToFetch, PrecisionTimeSpan maximumTime, AnalogWaveform< double > reading)

#### Remarks

For the NI 4070/4071/4072 only. The number of elements in the waveform array is determined by the values you specify for the *waveformPoints* parameter in [ConfigureWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-nidmm-configurewaveformacquisition__dmmmeasurementfunction-double-double-int.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. When set to NationalInstruments.PrecisionTimeSpan.MaxValue, the DMM calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of waveform points to return. You specify the total number of points that the DMM acquires in the waveformPoints parameter of ConfigureWaveformAcquisition. The default value is 1. |
| reading | AnalogWaveform< double > | The pre-allocated Waveform to be used to return the read results. This parameter cannot be null. |

#### Returns

Returns an analog waveform datatype which contains the array of values from a previously initiated waveform acquisition and timing information.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IOTimeoutException | The method does not complete within the time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |
| Ivi.Driver.OutOfRangeException | The value passed for parameter pointsToFetch is out of range. |
| System.ArgumentNullException | The value for parameter reading is null. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedreadwaveformasync__int-precisiontimespan-analogwaveform_double_-object.html language=enus -->
## TOPIC 00288: MemoryOptimizedReadWaveformAsync(int, PrecisionTimeSpan, AnalogWaveform< double >, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedreadwaveformasync__int-precisiontimespan-analogwaveform_double_-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-memoryoptimizedreadwaveformasync__int-precisiontimespan-analogwaveform_double_-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously acquires a waveform and fetches values into a pre-allocated waveform buffer. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void MemoryOptimizedReadWaveformAsync(int pointsToFetch, PrecisionTimeSpan maximumTime, AnalogWaveform< double > reading, object userState)R

### MemoryOptimizedReadWaveformAsync(int, PrecisionTimeSpan, AnalogWaveform< double >, object)

Asynchronously acquires a waveform and fetches values into a pre-allocated waveform buffer.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void MemoryOptimizedReadWaveformAsync(int pointsToFetch, PrecisionTimeSpan maximumTime, AnalogWaveform< double > reading, object userState)

#### Remarks

For the NI 4070/4071/4072 only. The number of elements in the waveform array is determined by the values you specify for the *waveformPoints* parameter in [ConfigureWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-nidmm-configurewaveformacquisition__dmmmeasurementfunction-double-double-int.html).

If an asynchronous method is called before the completion of a previous asynchronous method, the operation is queued to occur one after the other. The *userState*  parameter can be used to distinguish between different asynchronous methods.

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. When set to NationalInstruments.PrecisionTimeSpan.MaxValue, the DMM calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of waveform points to return. You specify the total number of points that the DMM acquires in the waveformPoints parameter of ConfigureWaveformAcquisition. The default value is 1. |
| reading | AnalogWaveform< double > | The pre-allocated waveform to be used to return the read results. This parameter cannot be null. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value passed for parameter pointsToFetch is not positve. |
| System.ArgumentNullException | The value for reading is null. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-numberofpoints.html language=enus -->
## TOPIC 00289: NumberOfPoints

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-numberofpoints.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-numberofpoints.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of points to acquire in a waveform acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic int NumberOfPoints { get; set; }RemarksValid only for NI 4070/4071/4072. The number of points to acquire in a waveform acquisition.

### NumberOfPoints

Gets or sets the number of points to acquire in a waveform acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public int NumberOfPoints { get; set; }

#### Remarks

Valid only for NI 4070/4071/4072.

The number of points to acquire in a waveform acquisition.

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-rate.html language=enus -->
## TOPIC 00290: Rate

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-rate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-rate.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the rate of the waveform acquisition in Samples per second (S/s). SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Rate { get; set; }RemarksThe valid Range is 10.0-1,800,000 S/s. Values are coerced to the closest integer divisor of 1,800,000. The default value

### Rate

Gets or sets the rate of the waveform acquisition in Samples per second (S/s).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Rate { get; set; }

#### Remarks

The valid Range is 10.0-1,800,000 S/s. Values are coerced to the closest integer divisor of 1,800,000. The default value is 1,800,000.

Valid only for NI 4070/4071/4072.

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveform__int-precisiontimespan.html language=enus -->
## TOPIC 00291: ReadWaveform(int, PrecisionTimeSpan)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveform__int-precisiontimespan.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveform__int-precisiontimespan.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquires and returns a waveform buffer with values. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic AnalogWaveform< double > ReadWaveform(int pointsToFetch, PrecisionTimeSpan maximumTime)RemarksFor the NI 4070/4071/4072 only. The number of elements in the waveform array is determ

### ReadWaveform(int, PrecisionTimeSpan)

Acquires and returns a waveform buffer with values.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public AnalogWaveform< double > ReadWaveform(int pointsToFetch, PrecisionTimeSpan maximumTime)

#### Remarks

For the NI 4070/4071/4072 only. The number of elements in the waveform array is determined by the values you specify for the *waveformPoints* parameter in [ConfigureWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-nidmm-configurewaveformacquisition__dmmmeasurementfunction-double-double-int.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. When set to NationalInstruments.PrecisionTimeSpan.MaxValue, the DMM calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of waveform points to return. You specify the total number of points that the DMM acquires in the waveformPoints parameter of ConfigureWaveformAcquisition. The default value is 1. |

#### Returns

Returns an analog waveform datatype which contains the array of values from a previously initiated waveform acquisition and timing information.

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.IOTimeoutException | The method does not complete within the time interval. This exception happens if an external trigger has not been received, or if the specified timeout is not long enough for the acquisition to complete. |
| Ivi.Driver.OutOfRangeException | The value passed for parameter pointsToFetch is out of range. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveformasync__int-precisiontimespan-object.html language=enus -->
## TOPIC 00292: ReadWaveformAsync(int, PrecisionTimeSpan, object)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveformasync__int-precisiontimespan-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveformasync__int-precisiontimespan-object.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Asynchronously acquires a waveform and fetches data as a waveform data type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ReadWaveformAsync(int pointsToFetch, PrecisionTimeSpan maximumTime, object userState)RemarksFor the NI 4070/4071/4072 only. The number of elements in

### ReadWaveformAsync(int, PrecisionTimeSpan, object)

Asynchronously acquires a waveform and fetches data as a waveform data type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ReadWaveformAsync(int pointsToFetch, PrecisionTimeSpan maximumTime, object userState)

#### Remarks

For the NI 4070/4071/4072 only. The number of elements in the waveform array is determined by the values you specify for the *waveformPoints* parameter in [ConfigureWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-nidmm-configurewaveformacquisition__dmmmeasurementfunction-double-double-int.html).

If an asynchronous method is called before the completion of a previous asynchronous method, the operation is queued to occur one after the other. The *userState*  parameter can be used to distinguish between different asynchronous methods.

Note

If the user calls dispose on the session object while the asynchronous operation is in progress or before the asynchronous method is called, the operation completed event will not be raised.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximumTime | PrecisionTimeSpan | Specifies the maximum time allowed for this method to complete. The valid range is 0-86400000 milliseconds. When set to NationalInstruments.PrecisionTimeSpan.MaxValue, the DMM calculates the timeout automatically. |
| pointsToFetch | int | Specifies the number of waveform points to return. You specify the total number of points that the DMM acquires in the waveformPoints parameter of ConfigureWaveformAcquisition. The default value is 1. |
| userState | object | An object used to associate client state (such as a task ID) with this particular asynchronous operation. |

#### Exceptions

| Type | Description |
| --- | --- |
| Ivi.Driver.OutOfRangeException | The value passed for parameter pointsToFetch is not positve. |

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveformcompleted.html language=enus -->
## TOPIC 00293: ReadWaveformCompleted

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveformcompleted.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-readwaveformcompleted.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Occurs when asynchronous call for read waveform operation completes. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic EventHandler< DmmMeasurementEventArgs< AnalogWaveform< double > > > ReadWaveformCompleted

### ReadWaveformCompleted

Occurs when asynchronous call for read waveform operation completes.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public EventHandler< [DmmMeasurementEventArgs](nationalinstruments-modularinstruments-nidmm-dmmmeasurementeventargs.html)< AnalogWaveform< double > > > ReadWaveformCompleted

Parent topic:

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-synchronizecallbacks.html language=enus -->
## TOPIC 00294: SynchronizeCallbacks

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition-synchronizecallbacks.html
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

DmmWaveformAcquisition Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition.html language=enus -->
## TOPIC 00295: DmmWaveformAcquisition Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides methods and properties for waveform-related operations. Derives fromDmmSubObjectISupportSynchronizationContextIDisposableSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class DmmWaveformAcquisition : DmmSubObject, ISupportSynchronizationContext, IDisposableRemarksValid o

### DmmWaveformAcquisition Class

Provides methods and properties for waveform-related operations.

#### Derives from

- DmmSubObject
- ISupportSynchronizationContext
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class DmmWaveformAcquisition : DmmSubObject, ISupportSynchronizationContext, IDisposable

#### Remarks

Waveform Acquisition Fundamentals

NI Digital Multimeters Help

Note

System.ObjectDisposedException is returned if the members are accessed after the associated [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Coupling | Gets or sets the coupling during a waveform acquisition. |
| NumberOfPoints | Gets or sets the number of points to acquire in a waveform acquisition. |
| Rate | Gets or sets the rate of the waveform acquisition in Samples per second (S/s). |
| SynchronizeCallbacks | Gets or sets a value indicating whether the events and callback delegates are invoked through the System.Threading.SynchronizationContext.Send or System.Threading.SynchronizationContext.Post methods. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Frees the resources held. |
| FetchWaveform(int, PrecisionTimeSpan) | Returns an array of values in the form of a waveform datatype from a previously initiated waveform acquisition. |
| FetchWaveformAsync(int, PrecisionTimeSpan, object) | Asynchronously populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition. |
| MemoryOptimizedFetchWaveform(int, PrecisionTimeSpan, AnalogWaveform< double >) | Populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition. |
| MemoryOptimizedFetchWaveformAsync(int, PrecisionTimeSpan, AnalogWaveform< double >, object) | Asynchronously populates a pre-allocated waveform buffer with values from a previously initiated waveform acquisition. |
| MemoryOptimizedReadWaveform(int, PrecisionTimeSpan, AnalogWaveform< double >) | Acquires and populates a pre-allocated waveform buffer with values. |
| MemoryOptimizedReadWaveformAsync(int, PrecisionTimeSpan, AnalogWaveform< double >, object) | Asynchronously acquires a waveform and fetches values into a pre-allocated waveform buffer. |
| ReadWaveform(int, PrecisionTimeSpan) | Acquires and returns a waveform buffer with values. |
| ReadWaveformAsync(int, PrecisionTimeSpan, object) | Asynchronously acquires a waveform and fetches data as a waveform data type. |

#### Events

| Name | Description |
| --- | --- |
| FetchWaveformCompleted | Occurs when asynchronous call for fetch waveform operation completes. |
| ReadWaveformCompleted | Occurs when asynchronous call for read waveform operation completes. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-dmmwaveformcoupling.html language=enus -->
## TOPIC 00296: DmmWaveformCoupling Enumeration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-dmmwaveformcoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-dmmwaveformcoupling.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling during waveform acquisition. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic enum DmmWaveformCouplingMembersNameValueDescriptionAC0AC coupled. DC1DC coupled. See AlsoCoupling

### DmmWaveformCoupling Enumeration

Specifies the coupling during waveform acquisition.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public enum DmmWaveformCoupling

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AC | 0 | AC coupled. |
| DC | 1 | DC coupled. |

#### See Also

- Coupling

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-ac.html language=enus -->
## TOPIC 00297: AC

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-ac.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-ac.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets properties applicable to AC measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmAC AC { get; }RemarksReturns an object of type DmmAC.

### AC

Gets properties applicable to AC measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmAC](nationalinstruments-modularinstruments-nidmm-dmmac.html) AC { get; }

#### Remarks

Returns an object of type [DmmAC](nationalinstruments-modularinstruments-nidmm-dmmac.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-advanced.html language=enus -->
## TOPIC 00298: Advanced

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-advanced.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-advanced.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets additional information concerning the instrument driver session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmAdvanced Advanced { get; }RemarksReturns an object of type DmmAdvanced.

### Advanced

Gets additional information concerning the instrument driver session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmAdvanced](nationalinstruments-modularinstruments-nidmm-dmmadvanced.html) Advanced { get; }

#### Remarks

Returns an object of type [DmmAdvanced](nationalinstruments-modularinstruments-nidmm-dmmadvanced.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html language=enus -->
## TOPIC 00299: AutoRange

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the range is set automatically by the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmAuto AutoRange { get; set; }RemarksValueDescriptionOnNI-DMM driver determines whether the range is set automatically by the instrument before acquiring each m

### AutoRange

Gets or sets whether the range is set automatically by the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmAuto](nationalinstruments-modularinstruments-nidmm-dmmauto.html) AutoRange { get; set; }

#### Remarks

| Value | Description |
| --- | --- |
| On | NI-DMM driver determines whether the range is set automatically by the instrument before acquiring each measurement. |
| Off | NI-DMM driver sets the current range value and uses this range for all subsequent measurements until the measurement configuration is changed. |
| Once | NI-DMM driver determines whether the range is set automatically by the instrument before acquiring the measurement. The range value is stored and used for all subsequent measurements until the measurement configuration is changed. |

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-autorangevalue.html language=enus -->
## TOPIC 00300: AutoRangeValue

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-autorangevalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-autorangevalue.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets measurement auto range value. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double AutoRangeValue { get; }RemarksThe value is in units appropriate for the current value of the MeasurementFunction. For example, if MeasurementFunction is set to ACVolts, the units are volts.

### AutoRangeValue

Gets measurement auto range value.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double AutoRangeValue { get; }

#### Remarks

The value is in units appropriate for the current value of the [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html). For example, if [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html) is set to [ACVolts](nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html), the units are volts. The value of this property is only valid if range was set to auto range and a read/fetch has occurred.

Returns the measurement auto range value. The value of this property is only valid if range was set to auto range and a read/fetch has occurred.

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-calibration.html language=enus -->
## TOPIC 00301: Calibration

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-calibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-calibration.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmCalibration sub-object which is used to perform self-calibration or for optional functionality when performing a calibration. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmCalibration Calibration { get; }RemarksReturns an object of type DmmCalibration.

### Calibration

Gets the [DmmCalibration](nationalinstruments-modularinstruments-nidmm-dmmcalibration.html) sub-object which is used to perform self-calibration or for optional functionality when performing a calibration.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmCalibration](nationalinstruments-modularinstruments-nidmm-dmmcalibration.html) Calibration { get; }

#### Remarks

Returns an object of type [DmmCalibration](nationalinstruments-modularinstruments-nidmm-dmmcalibration.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-capacitanceandinductance.html language=enus -->
## TOPIC 00302: CapacitanceAndInductance

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-capacitanceandinductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-capacitanceandinductance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmCapacitanceAndInductance sub-object used to control inductance and capacitance capabilities. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmCapacitanceAndInductance CapacitanceAndInductance { get; }RemarksFor the NI 4072 only. Returns an object of type DmmCapacita

### CapacitanceAndInductance

Gets the [DmmCapacitanceAndInductance](nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance.html) sub-object used to control inductance and capacitance capabilities.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmCapacitanceAndInductance](nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance.html) CapacitanceAndInductance { get; }

#### Remarks

For the NI 4072 only.

Returns an object of type [DmmCapacitanceAndInductance](nationalinstruments-modularinstruments-nidmm-dmmcapacitanceandinductance.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-close.html language=enus -->
## TOPIC 00303: Close()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-close.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-close.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: If not already closed, closes the specified session and deallocates resources that it reserved. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Close()RemarksThe method can be called safely more than once, even if the session has already closed.

### Close()

If not already closed, closes the specified session and deallocates resources that it reserved.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Close()

#### Remarks

The method can be called safely more than once, even if the session has already closed.

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-dmmauto-double.html language=enus -->
## TOPIC 00304: Configure(DmmMeasurementFunction, DmmAuto, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-dmmauto-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-dmmauto-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures measurements with AutoRange on. The configured properties include MeasurementFunction, AutoRange, and Resolution. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Configure(DmmMeasurementFunction measurementFunction, DmmAuto autoRange, double resolutionAbsolute)Rem

### Configure(DmmMeasurementFunction, DmmAuto, double)

Configures measurements with [AutoRange](nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html) on. The configured properties include [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html), [AutoRange](nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html), and [Resolution](nationalinstruments-modularinstruments-nidmm-nidmm-resolution.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Configure(DmmMeasurementFunction measurementFunction, DmmAuto autoRange, double resolutionAbsolute)

#### Remarks

AutoRange

Immediate

Note

NI-DMM ignores the *resolutionDigits* for capacitance and inductance measurements on the NI 4072. To achieve better resolution for such measurements, use [NumberOfAverages](nationalinstruments-modularinstruments-nidmm-dmmadvanced-numberofaverages.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measurementFunction | DmmMeasurementFunction | Specifies the MeasurementFunction used to acquire the measurement. |
| autoRange | DmmAuto | Indicates whether the range is set automatically by the instrument. AutoRange is set to this value. |
| resolutionAbsolute | double | Specifies the Resolution for the measurement. This parameter is ignored when the autoRange parameter is set to On or Once. The default is 0.001 V. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OutOfRangeException | The resolution specified is invalid for the range. |
| Ivi.Driver.ValueNotSupportedException | The parameter enum value specified is not supported. |
| Ivi.Driver.OperationNotSupportedException | The specified device cannot be configured for AutoRange when a trigger is selected. Set Source and/or SampleTrigger to Immediate while autoranging. |

#### See Also

- DmmTrigger

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-double-double.html language=enus -->
## TOPIC 00305: Configure(DmmMeasurementFunction, double, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-double-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures measurements by setting the Range value. The configured properties include MeasurementFunction, Range, and Resolution. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Configure(DmmMeasurementFunction measurementFunction, double range, double resolutionAbsolute)Rem

### Configure(DmmMeasurementFunction, double, double)

Configures measurements by setting the [Range](nationalinstruments-modularinstruments-nidmm-nidmm-range.html) value. The configured properties include [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html), [Range](nationalinstruments-modularinstruments-nidmm-nidmm-range.html), and [Resolution](nationalinstruments-modularinstruments-nidmm-nidmm-resolution.html).

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Configure(DmmMeasurementFunction measurementFunction, double range, double resolutionAbsolute)

#### Remarks

resolutionAbsolute

NumberOfAverages

Note

The NI 4050, NI 4060, and NI 4065 only support [AutoRange](nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html) 
 when the trigger and sample trigger are set to Immediate.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measurementFunction | DmmMeasurementFunction | Specifies the MeasurementFunction used to acquire the measurement. |
| range | double | Specifies the Range for the function specified in the measurementFunction parameter. When frequency is specified in the measurementFunction parameter, you must supply the minimum frequency expected in the range parameter. For example, you must type in 100 Hz if you are measuring 101 Hz or higher. For all other functions, you must supply a range that exceeds the value that you are measuring. For example, you must type in 10 V if you are measuring 9 V. Range values are coerced up to the closest input range. The default value is 0.02 V. |
| resolutionAbsolute | double | Specifies the Resolution for the measurement. The default is 0.001 V. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

#### See Also

- DmmTrigger

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-dmmauto-double.html language=enus -->
## TOPIC 00306: ConfigureMeasurementDigits(DmmMeasurementFunction, DmmAuto, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-dmmauto-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-dmmauto-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures measurements with AutoRange on. The configured properties include MeasurementFunction, Range, and Resolution in digits. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureMeasurementDigits(DmmMeasurementFunction measurementFunction, DmmAuto autoRange, double

### ConfigureMeasurementDigits(DmmMeasurementFunction, DmmAuto, double)

Configures measurements with [AutoRange](nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html) on. The configured properties include [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html), [Range](nationalinstruments-modularinstruments-nidmm-nidmm-range.html), and [Resolution](nationalinstruments-modularinstruments-nidmm-nidmm-resolution.html) in digits.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureMeasurementDigits(DmmMeasurementFunction measurementFunction, DmmAuto autoRange, double resolutionDigits)

#### Remarks

AutoRange

Immediate

Note

NI-DMM ignores the *resolutionDigits* for capacitance and inductance measurements on the NI 4072. To achieve better resolution for such measurements, use [NumberOfAverages](nationalinstruments-modularinstruments-nidmm-dmmadvanced-numberofaverages.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measurementFunction | DmmMeasurementFunction | Specifies the MeasurementFunction used to acquire the measurement. |
| autoRange | DmmAuto | Indicates whether the range is set automatically by the instrument. AutoRange is set to this value. |
| resolutionDigits | double | Specifies the Resolution for the measurement in digits. This parameter is ignored when the range parameter is set to On or Once. The default is 0.001 V. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |
| Ivi.Driver.ValueNotSupportedException | The parameter enum value specified is not supported. |
| Ivi.Driver.OperationNotSupportedException | The specified device cannot be configured for AutoRange when a trigger is selected. Set Source and/or SampleTrigger to Immediate while autoranging. |

#### See Also

- DmmTrigger

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html language=enus -->
## TOPIC 00307: ConfigureMeasurementDigits(DmmMeasurementFunction, double, double)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures measurements by setting Range value. The configured properties include MeasurementFunction, Range, and Resolution in digits. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureMeasurementDigits(DmmMeasurementFunction measurementFunction, double range, double

### ConfigureMeasurementDigits(DmmMeasurementFunction, double, double)

Configures measurements by setting [Range](nationalinstruments-modularinstruments-nidmm-nidmm-range.html) value. The configured properties include [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html), [Range](nationalinstruments-modularinstruments-nidmm-nidmm-range.html), and [Resolution](nationalinstruments-modularinstruments-nidmm-nidmm-resolution.html) in digits.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureMeasurementDigits(DmmMeasurementFunction measurementFunction, double range, double resolutionDigits)

#### Remarks

AutoRange

Note

NI-DMM ignores the *resolutionDigits* for capacitance and inductance measurements on the NI 4072. To achieve better resolution for such measurements, use the [NumberOfAverages](nationalinstruments-modularinstruments-nidmm-dmmadvanced-numberofaverages.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measurementFunction | DmmMeasurementFunction | Specifies the MeasurementFunction used to acquire the measurement. |
| range | double | Specifies the Range for the function specified in the measurementFunction parameter. When frequency is specified in the measurementFunction parameter, you must supply the minimum frequency expected in the range parameter. For example, you must type in 100 Hz if you are measuring 101 Hz or higher. For all other functions, you must supply a range that exceeds the value that you are measuring. For example, you must type in 10 V if you are measuring 9 V. Range values are coerced up to the closest input range. The default value is 0.02 V. |
| resolutionDigits | double | Specifies the Resolution for the measurement in digits. The default is 0.001 V. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |

#### See Also

- DmmTrigger

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-configurewaveformacquisition__dmmmeasurementfunction-double-double-int.html language=enus -->
## TOPIC 00308: ConfigureWaveformAcquisition(DmmMeasurementFunction, double, double, int)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-configurewaveformacquisition__dmmmeasurementfunction-double-double-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-configurewaveformacquisition__dmmmeasurementfunction-double-double-int.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the NI 4070/4071/4072 for waveform acquisitions. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void ConfigureWaveformAcquisition(DmmMeasurementFunction measurementFunction, double range, double rate, int waveformPoints)ParametersNameTypeDescriptionmeasurementFunction

### ConfigureWaveformAcquisition(DmmMeasurementFunction, double, double, int)

Configures the NI 4070/4071/4072 for waveform acquisitions.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void ConfigureWaveformAcquisition(DmmMeasurementFunction measurementFunction, double range, double rate, int waveformPoints)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| measurementFunction | DmmMeasurementFunction | Specifies the MeasurementFunction used in a waveform acquisition. WaveformCurrent and WaveformVoltage are the valid values. |
| range | double | Specifies the expected maximum amplitude of the input signal and sets the range for the measurementFunction. NI-DMM sets Range to this value. Range values are coerced up to the closest input range. The default is 10.0. For valid ranges refer to the topics in Devices. Autoranging is not supported during waveform acquisitions. |
| rate | double | Specifies the rate of the acquisition in samples per second. NI-DMM sets Rate to this value. The valid range is 10.0-1,800,000 S/s. Rate values are coerced to the closest integer divisor of 1,800,000. The default value is 1,800,000. |
| waveformPoints | int | Specifies the number of points to acquire before the waveform acquisition completes. NI-DMM sets NumberOfPoints to this value. To calculate the maximum and minimum number of waveform points that you can acquire in one acquisition, refer to the Waveform Acquisition Measurement Cycle. The default value is 500. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentException | The parameter value passed is invalid. |
| Ivi.Driver.OutOfRangeException | The parameter value passed is out of range. |
| Ivi.Driver.OperationNotSupportedException | The rate selected is invalid with DCNR other than normal. |

#### See Also

- DmmWaveformAcquisition

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-currentsource.html language=enus -->
## TOPIC 00309: CurrentSource

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-currentsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-currentsource.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the current source provided during diode measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double CurrentSource { get; set; }RemarksThe NI 4050 and NI 4060 are not supported. The supported values are 1 microAmp, 10 microAmps, 100 microAmps, and 1 milliAmp

### CurrentSource

Gets or sets the current source provided during diode measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double CurrentSource { get; set; }

#### Remarks

The NI 4050 and NI 4060 are not supported.

The supported values are 1 microAmp, 10 microAmps, 100 microAmps, and 1 milliAmp. Refer to the [Devices](/csh?context=nidmm_dmm_devices) topic in the *NI Digital Multimeters Help*.

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-digitsresolution.html language=enus -->
## TOPIC 00310: DigitsResolution

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-digitsresolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-digitsresolution.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the measurement resolution in digits. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double DigitsResolution { get; set; }RemarksSetting this property to higher values increases the measurement accuracy. Setting this property to lower values increases the measuremen

### DigitsResolution

Gets or sets the measurement resolution in digits.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double DigitsResolution { get; set; }

#### Remarks

Setting this property to higher values increases the measurement accuracy. Setting this property to lower values increases the measurement speed. NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072. To achieve better resolution for such measurements, use [NumberOfAverages](nationalinstruments-modularinstruments-nidmm-dmmadvanced-numberofaverages.html).

| Description | DigitsResolution Value |
| --- | --- |
| 3.5 | Specifies 3.5 digits resolution. |
| 4.5 | Specifies 4.5 digits resolution. |
| 5.5 | Specifies 5.5 digits resolution. |
| 6.5 | Specifies 6.5 digits resolution. |
| 7.5 | Specifies 7.5 digits resolution. |

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-dispose.html language=enus -->
## TOPIC 00311: Dispose()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-dispose.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: If not already disposed, closes the specified session and deallocates resources that it reserved. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic void Dispose()RemarksThe method can be called safely more than once, even if the session has already been disposed.

### Dispose()

If not already disposed, closes the specified session and deallocates resources that it reserved.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public void Dispose()

#### Remarks

The method can be called safely more than once, even if the session has already been disposed.

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-driveridentity.html language=enus -->
## TOPIC 00312: DriverIdentity

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-driveridentity.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-driveridentity.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets identity information about the instrument you are using. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDriverIdentity DriverIdentity { get; }RemarksReturns an object of type DmmDriverIdentity.

### DriverIdentity

Gets identity information about the instrument you are using.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmDriverIdentity](nationalinstruments-modularinstruments-nidmm-dmmdriveridentity.html) DriverIdentity { get; }

#### Remarks

Returns an object of type [DmmDriverIdentity](nationalinstruments-modularinstruments-nidmm-dmmdriveridentity.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-driveroperation.html language=enus -->
## TOPIC 00313: DriverOperation

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-driveroperation.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-driveroperation.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmDriverOperation sub-object used to obtain properties that affect operation of the instrument driver. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDriverOperation DriverOperation { get; }RemarksReturns an object of type DmmDriverOperation.

### DriverOperation

Gets the [DmmDriverOperation](nationalinstruments-modularinstruments-nidmm-dmmdriveroperation.html) sub-object used to obtain properties that affect operation of the instrument driver.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmDriverOperation](nationalinstruments-modularinstruments-nidmm-dmmdriveroperation.html) DriverOperation { get; }

#### Remarks

Returns an object of type [DmmDriverOperation](nationalinstruments-modularinstruments-nidmm-dmmdriveroperation.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-driverutility.html language=enus -->
## TOPIC 00314: DriverUtility

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-driverutility.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-driverutility.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmDriverUtility sub-object. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmDriverUtility DriverUtility { get; }RemarksReturns an object of type DmmDriverUtility.

### DriverUtility

Gets the [DmmDriverUtility](nationalinstruments-modularinstruments-nidmm-dmmdriverutility.html) sub-object.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmDriverUtility](nationalinstruments-modularinstruments-nidmm-dmmdriverutility.html) DriverUtility { get; }

#### Remarks

Returns an object of type [DmmDriverUtility](nationalinstruments-modularinstruments-nidmm-dmmdriverutility.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-frequency.html language=enus -->
## TOPIC 00315: Frequency

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-frequency.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmFrequency sub-object used for controlling frequency capabilities. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmFrequency Frequency { get; }RemarksReturns an object of type DmmFrequency.

### Frequency

Gets the [DmmFrequency](nationalinstruments-modularinstruments-nidmm-dmmfrequency.html) sub-object used for controlling frequency capabilities.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmFrequency](nationalinstruments-modularinstruments-nidmm-dmmfrequency.html) Frequency { get; }

#### Remarks

Returns an object of type [DmmFrequency](nationalinstruments-modularinstruments-nidmm-dmmfrequency.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-getinstrumenthandle.html language=enus -->
## TOPIC 00316: GetInstrumentHandle()

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-getinstrumenthandle.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-getinstrumenthandle.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the System.Runtime.InteropServices.SafeHandle to the NIDmm instrument session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic SafeHandle GetInstrumentHandle()RemarksUsing the System.Runtime.InteropServices.SafeHandle, you can get the System.IntPtr to the session; however, t

### GetInstrumentHandle()

Gets the System.Runtime.InteropServices.SafeHandle to the [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) instrument session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public SafeHandle GetInstrumentHandle()

#### Remarks

Using the System.Runtime.InteropServices.SafeHandle, you can get the System.IntPtr to the session; however, there are risks involved with using the System.IntPtr. It is difficult to know the state of the handle, and the handle could be recycled while you are using it. For more information, refer to System.Runtime.InteropServices.SafeHandle.DangerousGetHandle.

#### Returns

A System.Runtime.InteropServices.SafeHandle to the [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) instrument session.

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-getservice__type.html language=enus -->
## TOPIC 00317: GetService(Type)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-getservice__type.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-getservice__type.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the service object of the specified type. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic object GetService(Type serviceType)ParametersNameTypeDescriptionserviceTypeTypeAn object that specifies the System.Type of the object. ReturnsThe object of System.Type determined by ser

### GetService(Type)

Gets the service object of the specified type.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public object GetService(Type serviceType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| serviceType | Type | An object that specifies the System.Type of the object. |

#### Returns

The object of System.Type determined by *serviceType* .

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-inputresistance.html language=enus -->
## TOPIC 00318: InputResistance

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-inputresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-inputresistance.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the input resistance of the instrument. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double InputResistance { get; set; }RemarksThe NI 4050 and NI 4060 are not supported. The supported values are 1.000000E+6 (1M Ohm), 1.000000E+7 (10M Ohm), and 1.000000E+10 (input

### InputResistance

Gets or sets the input resistance of the instrument.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double InputResistance { get; set; }

#### Remarks

The NI 4050 and NI 4060 are not supported.

The supported values are 1.000000E+6 (1M Ohm), 1.000000E+7 (10M Ohm), and 1.000000E+10 (input resistance greater than 10 G Ohm).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-isdisposed.html language=enus -->
## TOPIC 00319: IsDisposed

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-isdisposed.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-isdisposed.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the session object is disposed or not. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic bool IsDisposed { get; }RemarksIf the value is true, it means that the session has already been disposed. If the value is false, it means that the session is not

### IsDisposed

Gets a value indicating whether the session object is disposed or not.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public bool IsDisposed { get; }

#### Remarks

If the value is true, it means that the session has already been disposed. If the value is false, it means that the session is not disposed.

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-measurement.html language=enus -->
## TOPIC 00320: Measurement

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-measurement.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-measurement.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets data from a measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmMeasurement Measurement { get; }RemarksReturns an object of type DmmMeasurement.

### Measurement

Gets data from a measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmMeasurement](nationalinstruments-modularinstruments-nidmm-dmmmeasurement.html) Measurement { get; }

#### Remarks

Returns an object of type [DmmMeasurement](nationalinstruments-modularinstruments-nidmm-dmmmeasurement.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html language=enus -->
## TOPIC 00321: MeasurementFunction

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the measurement function. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmMeasurementFunction MeasurementFunction { get; set; }RemarksIf you are configuring by setting properties directly, you must set the OperationMode before setting other properties. If the Oper

### MeasurementFunction

Gets or sets the measurement function.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmMeasurementFunction](nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html) MeasurementFunction { get; set; }

#### Remarks

If you are configuring by setting properties directly, you must set the [OperationMode](nationalinstruments-modularinstruments-nidmm-nidmm-operationmode.html) before setting other properties. If the [OperationMode](nationalinstruments-modularinstruments-nidmm-nidmm-operationmode.html) is set to [WaveformMode](nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html), 
 the only valid types are [WaveformVoltage](nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html) and [WaveformCurrent](nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html). Set the [OperationMode](nationalinstruments-modularinstruments-nidmm-nidmm-operationmode.html) to [IviDmmMode](nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html) to set all other values.

For more information, refer to [NIDMM_ATTR_FUNCTION](/csh?context=nidmm_nidmmcref_attribute_function) topic in the *NI Digital Multimeters Help*.

Returns an object of type [DmmMeasurementFunction](nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-measurementperiod.html language=enus -->
## TOPIC 00322: MeasurementPeriod

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-measurementperiod.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-measurementperiod.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of seconds it takes to make one measurement. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double MeasurementPeriod { get; }RemarksUse this right before you begin acquiring data - after you have completely configured the measurement and after all configuration m

### MeasurementPeriod

Gets the number of seconds it takes to make one measurement.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double MeasurementPeriod { get; }

#### Remarks

Use this right before you begin acquiring data - after you have completely configured the measurement and after all configuration methods have been called.

Returns the amount of time in seconds it takes to complete one measurement with the current configuration.

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__intptr.html language=enus -->
## TOPIC 00323: NIDmm(IntPtr)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__intptr.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__intptr.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NIDmm class using an existing intrument session handle. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic NIDmm(IntPtr instrumentHandle)ParametersNameTypeDescriptioninstrumentHandleIntPtrA pointer to the instrument handle.

### NIDmm(IntPtr)

Initializes a new instance of the [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) class using an existing intrument session handle.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public NIDmm(IntPtr instrumentHandle)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| instrumentHandle | IntPtr | A pointer to the instrument handle. |

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool-string-string.html language=enus -->
## TOPIC 00324: NIDmm(string, bool, bool, string, string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool-string-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool-string-string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NIDmm class for GRPC implementation. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic NIDmm(string resourceName, bool idQuery, bool resetDevice, string optionString, string grpcChannelId)RemarksThis constructor is not supported by the .NET 4.0 int

### NIDmm(string, bool, bool, string, string)

Initializes a new instance of the [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) class for GRPC implementation.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public NIDmm(string resourceName, bool idQuery, bool resetDevice, string optionString, string grpcChannelId)

#### Remarks

This constructor is not supported by the .NET 4.0 interface.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | The name of the device to which the session is opened. |
| idQuery | bool | If this parameter is set to true, this method queries the instrument ID and checks that it is valid for this instrument driver. |
| resetDevice | bool | If this parameter is set to true, this method resets the instrument to a known state. Sends initialization commands to set the instrument to the state necessary for the operation of the instrument driver. |
| optionString | string | Sets the initial state of the following session properties: RangeCheck, QueryInstrumentStatus, Cache, Simulate, and RecordValueCoercions. |
| grpcChannelId | string | Specifies the gRPC channel identifier for the remote system. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | The resourceName or optionString is null. |
| System.ArgumentException | Either the device was not recognized, OR the device is not supported for this driver or version, OR the instrument descriptor is invalid, OR the driver setup description is invalid, OR the device is already in use by another process. Verify that all sessions of the device from other processes are properly closed. |
| Ivi.Driver.OperationNotSupportedException | The resource name specified has been opened for a calibration session. |

#### See Also

- DmmDriverOperation

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool-string.html language=enus -->
## TOPIC 00325: NIDmm(string, bool, bool, string)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool-string.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool-string.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NIDmm class representing the instrument driver session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic NIDmm(string resourceName, bool idQuery, bool resetDevice, string optionString)ParametersNameTypeDescriptionresourceNamestringThe name of the

### NIDmm(string, bool, bool, string)

Initializes a new instance of the [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) class representing the instrument driver session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public NIDmm(string resourceName, bool idQuery, bool resetDevice, string optionString)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | The name of the device to which the session is opened. |
| idQuery | bool | If this parameter is set to true, this method queries the instrument ID and checks that it is valid for this instrument driver. |
| resetDevice | bool | If this parameter is set to true, this method resets the instrument to a known state. Sends initialization commands to set the instrument to the state necessary for the operation of the instrument driver. |
| optionString | string | Sets the initial state of the following session properties: RangeCheck, QueryInstrumentStatus, Cache, Simulate, and RecordValueCoercions. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | The resourceName or optionString is null. |
| System.ArgumentException | Either the device was not recognized, OR the device is not supported for this driver or version, OR the instrument descriptor is invalid, OR the driver setup description is invalid, OR the device is already in use by another process. Verify that all sessions of the device from other processes are properly closed. |
| Ivi.Driver.OperationNotSupportedException | The resource name specified has been opened for a calibration session. |

#### See Also

- DmmDriverOperation

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool.html language=enus -->
## TOPIC 00326: NIDmm(string, bool, bool)

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-nidmm__string-bool-bool.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the NIDmm class representing the instrument driver session. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic NIDmm(string resourceName, bool idQuery, bool resetDevice)ParametersNameTypeDescriptionresourceNamestringThe name of the device to which the s

### NIDmm(string, bool, bool)

Initializes a new instance of the [NIDmm](nationalinstruments-modularinstruments-nidmm-nidmm.html) class representing the instrument driver session.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public NIDmm(string resourceName, bool idQuery, bool resetDevice)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| resourceName | string | The name of the device to which the session is opened. |
| idQuery | bool | If this parameter is set to true, this method queries the instrument ID and checks that it is valid for this instrument driver. |
| resetDevice | bool | If this parameter is set to true, this method resets the instrument to a known state. Sends initialization commands to set the instrument to the state necessary for the operation of the instrument driver. |

#### Exceptions

| Type | Description |
| --- | --- |
| System.ArgumentNullException | The resource name passed is null. |
| System.ArgumentException | Either the device was not recognized, OR the device is not supported for this driver or version, OR the instrument descriptor is invalid, OR the driver setup description is invalid, OR the device is already in use by another process. Verify that all sessions of the device from other processes are properly closed. |
| Ivi.Driver.OperationNotSupportedException | The resource name specified has been opened for a calibration session. |

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-operationmode.html language=enus -->
## TOPIC 00327: OperationMode

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-operationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-operationmode.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets how the NI 4065 and NI 4070/4071/4072 acquire data. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmOperationMode OperationMode { get; set; }RemarksOperationMode controls whether the NI-DMM driver takes standard single or multipoint measurements or acquires a wave

### OperationMode

Gets or sets how the NI 4065 and NI 4070/4071/4072 acquire data.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmOperationMode](nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html) OperationMode { get; set; }

#### Remarks

OperationMode controls whether the NI-DMM driver takes standard single or multipoint measurements or acquires a waveform.

If you are configuring the driver by setting the properties manually, set this property before setting the other configuration properties.

When you call [Configure](nationalinstruments-modularinstruments-nidmm-nidmm-configure__dmmmeasurementfunction-double-double.html) or [ConfigureMeasurementDigits](nationalinstruments-modularinstruments-nidmm-nidmm-configuremeasurementdigits__dmmmeasurementfunction-double-double.html), NI-DMM sets this property to [IviDmmMode](nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html). 
 When you call [ConfigureWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-nidmm-configurewaveformacquisition__dmmmeasurementfunction-double-double-int.html), NI-DMM sets this property to [WaveformMode](nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html). The default value is [IviDmmMode](nationalinstruments-modularinstruments-nidmm-dmmoperationmode.html).

#### See Also

- DmmOperationMode

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-range.html language=enus -->
## TOPIC 00328: Range

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-range.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-range.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the measurement range. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Range { get; set; }RemarksUse positive values to represent the absolute value of the maximum expected measurement. The value is in units appropriate for the current value of the Measurement

### Range

Gets or sets the measurement range.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Range { get; set; }

#### Remarks

Use positive values to represent the absolute value of the maximum expected measurement.

The value is in units appropriate for the current value of the [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html). For example, if [MeasurementFunction](nationalinstruments-modularinstruments-nidmm-nidmm-measurementfunction.html) is set to [ACVolts](nationalinstruments-modularinstruments-nidmm-dmmmeasurementfunction.html), the units are volts. The NI 4050 and NI 4060 only support [AutoRange](nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html) when the trigger and sample trigger is set to Immediate. [On](nationalinstruments-modularinstruments-nidmm-dmmauto.html) 
 performs an [AutoRange](nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html) before acquiring the measurement. [Off](nationalinstruments-modularinstruments-nidmm-dmmauto.html) sets the Range to the current Range and uses this range 
 for all subsequent measurements until the measurement configuration is changed. [Once](nationalinstruments-modularinstruments-nidmm-dmmauto.html) performs an [AutoRange](nationalinstruments-modularinstruments-nidmm-nidmm-autorange.html) before acquiring the next measurement. The Range is stored and used for all subsequent measurements until the measurement configuration is changed.

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-resolution.html language=enus -->
## TOPIC 00329: Resolution

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-resolution.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the measurement resolution in absolute units. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic double Resolution { get; set; }RemarksReturns the measurement resolution in absolute units. Setting this property to higher values increases the measurement accuracy. Settin

### Resolution

Gets or sets the measurement resolution in absolute units.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public double Resolution { get; set; }

#### Remarks

Returns the measurement resolution in absolute units.

Setting this property to higher values increases the measurement accuracy. Setting this property to lower values increases the measurement speed. NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072. To achieve better resolution for such measurements, use the [NumberOfAverages](nationalinstruments-modularinstruments-nidmm-dmmadvanced-numberofaverages.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-temperature.html language=enus -->
## TOPIC 00330: Temperature

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-temperature.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets temperature measurements. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmTemperature Temperature { get; }RemarksReturns an object of type DmmTemperature.

### Temperature

Gets temperature measurements.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmTemperature](nationalinstruments-modularinstruments-nidmm-dmmtemperature.html) Temperature { get; }

#### Remarks

Returns an object of type [DmmTemperature](nationalinstruments-modularinstruments-nidmm-dmmtemperature.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-trigger.html language=enus -->
## TOPIC 00331: Trigger

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-trigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-trigger.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmTrigger sub-object used to customize the triggering functionality. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmTrigger Trigger { get; }RemarksReturns an object of type DmmTrigger.

### Trigger

Gets the [DmmTrigger](nationalinstruments-modularinstruments-nidmm-dmmtrigger.html) sub-object used to customize the triggering functionality.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmTrigger](nationalinstruments-modularinstruments-nidmm-dmmtrigger.html) Trigger { get; }

#### Remarks

Returns an object of type [DmmTrigger](nationalinstruments-modularinstruments-nidmm-dmmtrigger.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm-waveformacquisition.html language=enus -->
## TOPIC 00332: WaveformAcquisition

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm-waveformacquisition.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm-waveformacquisition.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DmmWaveformAcquisition sub-object used for waveform-related operations. SyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic DmmWaveformAcquisition WaveformAcquisition { get; }RemarksReturns an object of type DmmWaveformAcquisition.

### WaveformAcquisition

Gets the [DmmWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition.html) sub-object used for waveform-related operations.

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public [DmmWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition.html) WaveformAcquisition { get; }

#### Remarks

Returns an object of type [DmmWaveformAcquisition](nationalinstruments-modularinstruments-nidmm-dmmwaveformacquisition.html).

Parent topic:

NIDmm Class

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm-nidmm.html language=enus -->
## TOPIC 00333: NIDmm Class

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm-nidmm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm-nidmm.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the root class that is used to identify and control the instrument session. In order to interact with the NI-DMM, you must create an instance of this class. Derives fromIIviDmmIIviDriverIDisposableIServiceProviderSyntaxNamespace: NationalInstruments.ModularInstruments.NIDmmpublic class NI

### NIDmm Class

Represents the root class that is used to identify and control the instrument session. In order to interact with the NI-DMM, you must create an instance of this class.

#### Derives from

- IIviDmm
- IIviDriver
- IDisposable
- IServiceProvider

#### Syntax

**Namespace:**[NationalInstruments.ModularInstruments.NIDmm](nationalinstruments-modularinstruments-nidmm.html)

public class NIDmm : IIviDmm, IIviDriver, IDisposable, IServiceProvider

#### Remarks

Programming Flow

NI Digital Multimeters Help

Note

System.ObjectDisposedException is returned if the members are accessed after the associated NIDmm object has been disposed.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| NIDmm(string, bool, bool) | Initializes a new instance of the NIDmm class representing the instrument driver session. |
| NIDmm(string, bool, bool, string) | Initializes a new instance of the NIDmm class representing the instrument driver session. |
| NIDmm(IntPtr) | Initializes a new instance of the NIDmm class using an existing intrument session handle. |
| NIDmm(string, bool, bool, string, string) | Initializes a new instance of the NIDmm class for GRPC implementation. |

#### Properties

| Name | Description |
| --- | --- |
| AC | Gets properties applicable to AC measurements. |
| Advanced | Gets additional information concerning the instrument driver session. |
| AutoRange | Gets or sets whether the range is set automatically by the instrument. |
| AutoRangeValue | Gets measurement auto range value. |
| Calibration | Gets the DmmCalibration sub-object which is used to perform self-calibration or for optional functionality when performing a calibration. |
| CapacitanceAndInductance | Gets the DmmCapacitanceAndInductance sub-object used to control inductance and capacitance capabilities. |
| CurrentSource | Gets or sets the current source provided during diode measurements. |
| DigitsResolution | Gets or sets the measurement resolution in digits. |
| DriverIdentity | Gets identity information about the instrument you are using. |
| DriverOperation | Gets the DmmDriverOperation sub-object used to obtain properties that affect operation of the instrument driver. |
| DriverUtility | Gets the DmmDriverUtility sub-object. |
| Frequency | Gets the DmmFrequency sub-object used for controlling frequency capabilities. |
| InputResistance | Gets or sets the input resistance of the instrument. |
| IsDisposed | Gets a value indicating whether the session object is disposed or not. |
| Measurement | Gets data from a measurement. |
| MeasurementFunction | Gets or sets the measurement function. |
| MeasurementPeriod | Gets the number of seconds it takes to make one measurement. |
| OperationMode | Gets or sets how the NI 4065 and NI 4070/4071/4072 acquire data. |
| Range | Gets or sets the measurement range. |
| Resolution | Gets or sets the measurement resolution in absolute units. |
| Temperature | Gets temperature measurements. |
| Trigger | Gets the DmmTrigger sub-object used to customize the triggering functionality. |
| WaveformAcquisition | Gets the DmmWaveformAcquisition sub-object used for waveform-related operations. |

#### Methods

| Name | Description |
| --- | --- |
| Close() | If not already closed, closes the specified session and deallocates resources that it reserved. |
| Configure(DmmMeasurementFunction, DmmAuto, double) | Configures measurements with AutoRange on. The configured properties include MeasurementFunction, AutoRange, and Resolution. |
| Configure(DmmMeasurementFunction, double, double) | Configures measurements by setting the Range value. The configured properties include MeasurementFunction, Range, and Resolution. |
| ConfigureMeasurementDigits(DmmMeasurementFunction, double, double) | Configures measurements by setting Range value. The configured properties include MeasurementFunction, Range, and Resolution in digits. |
| ConfigureMeasurementDigits(DmmMeasurementFunction, DmmAuto, double) | Configures measurements with AutoRange on. The configured properties include MeasurementFunction, Range, and Resolution in digits. |
| ConfigureWaveformAcquisition(DmmMeasurementFunction, double, double, int) | Configures the NI 4070/4071/4072 for waveform acquisitions. |
| Dispose() | If not already disposed, closes the specified session and deallocates resources that it reserved. |
| GetInstrumentHandle() | Gets the System.Runtime.InteropServices.SafeHandle to the NIDmm instrument session. |
| GetService(Type) | Gets the service object of the specified type. |

Parent topic:

NationalInstruments.ModularInstruments.NIDmm

<!--NI_TOPIC bundle=ni-dmm-csharp-api-ref path=nationalinstruments-modularinstruments-nidmm.html language=enus -->
## TOPIC 00334: NationalInstruments.ModularInstruments.NIDmm

- bundle_id: `ni-dmm-csharp-api-ref`
- source_path: `nationalinstruments-modularinstruments-nidmm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-csharp-api-ref/raw/resource/enus/nationalinstruments-modularinstruments-nidmm.html
- document_id: `ni-dmm-csharp-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionDmmACConfigures properties applicable only to AC measurements. DmmAdvancedConfigures and obtains additional information concerning the instrument driver session. DmmAdvancedCapacitanceAndInductanceProvides additional information specific to capacitance and inductance. DmmCalibr

### NationalInstruments.ModularInstruments.NIDmm

#### Classes

| Name | Description |
| --- | --- |
| DmmAC | Configures properties applicable only to AC measurements. |
| DmmAdvanced | Configures and obtains additional information concerning the instrument driver session. |
| DmmAdvancedCapacitanceAndInductance | Provides additional information specific to capacitance and inductance. |
| DmmCalibration | Defines methods and properties to perform self-calibration or to provide optional functionality when performing a calibration. |
| DmmCapacitanceAndInductance | Provides methods and properties to control inductance and capacitance capabilities. |
| DmmDriverIdentity | Provides identity information about the instrument you are using. |
| DmmDriverLock | Provides synchronization locks obtained on the driver session. |
| DmmDriverOperation | Provides properties that affect the operation of this instrument driver. |
| DmmDriverUtility | Provides additional, optional functionality for NI-DMM in your application. |
| DmmFrequency | Provides information regarding voltage. |
| DmmMeasurement | Provides properties to acquire data from a measurement. |
| DmmMeasurementCompleteDestination | Specifies the destination of the Measurement Complete (MC) signal, which is issued when the DMM completes a single measurement. |
| DmmMeasurementEventArgs | Holds the event data obtained after asynchronous measurement completion. |
| DmmMultiPoint | Provides properties and methods for acquiring data on multiple triggers and acquiring multiple measurements per trigger. |
| DmmOpenCableCompensation | Controls capacitance and inductance open cable compensation. |
| DmmRtd | Configures the RTD (resistance temperature detector) for temperature measurements. |
| DmmSampleTrigger | Represents a DMM trigger source. |
| DmmShortCableCompensation | Controls capacitance and inductance short cable compensation. |
| DmmSubObject | Contains members that are common to all sub-object NI-DMM classes. |
| DmmTemperature | Configures the DMM for temperature measurements. |
| DmmThermocouple | Configures the thermocouple for temperature measurements. |
| DmmTrigger | Customizes the triggering functionality for your application. |
| DmmTriggerSource | Represents a DMM trigger source. |
| DmmWarnings | Provides warning codes. |
| DmmWaveformAcquisition | Provides methods and properties for waveform-related operations. |
| NIDmm | Represents the root class that is used to identify and control the instrument session. In order to interact with the NI-DMM, you must create an instance of this class. |

#### Interfaces

None

#### Structures

| Name | Description |
| --- | --- |
| DmmSelfTestResult | The result of NI-DMM SelfTest. |

#### Enumerations

| Name | Description |
| --- | --- |
| Dmm4022ConfigurationMode | Specifies the operating mode of the NI 4022. |
| DmmAcquisitionStatus | Allows for storing and retrieving the acquisition status. |
| DmmAdcCalibration | Specifies the ADC calibration. Use DmmAdcCalibration for setting AdcCalibration. |
| DmmApertureTimeUnits | Specifies the unit used when measuring aperture time. Use DmmApertureTimeUnits for setting ApertureTimeUnits. |
| DmmAuto | Specifies AutoZero, VoltageAutoRange, and AutoRange. |
| DmmCableCompensationType | Specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. |
| DmmCalibrationType | Specifies whether calibration is external or self-calibration. |
| DmmControlAction | Specifies the control action for the driver to perform. |
| DmmDCBias | Use DmmDCBias to specify the DC bias. |
| DmmDCNoiseRejection | Specifies values for DC noise rejection. |
| DmmDelayMode | Specifies a delay interval after a sample trigger. |
| DmmLCCalculationModel | Specifies the LC calculation model. |
| DmmMeasurementFunction | Specifies the measurement function to be used. |
| DmmOffsetCompensatedOhm | Enables or disables offset compensation Ohms. |
| DmmOperationMode | Specifies the mode in which the device acquires data. |
| DmmReferenceJunctionType | Specifies the type of reference junction to be used. Used for thermocouple measurements. |
| DmmRtdType | Specifies the type of RTD (Resistance Temperature Detector) used. |
| DmmSlope | Specifies the edge of the signal. |
| DmmThermistorType | Specifies the type of thermistor used for measurement. |
| DmmThermocoupleType | Specifies the type of thermocouple used for temperature measurements. |
| DmmTransducerType | Specifies the type of device used for measurement. |
| DmmWaveformCoupling | Specifies the coupling during waveform acquisition. |

#### Delegates

None
