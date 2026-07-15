# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=1251 end=1500 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatafrequency-gethashcode.html language=enus -->
## TOPIC 01251: GetHashCode()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatafrequency-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatafrequency-gethashcode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a hash code for the CODataFrequency object. SyntaxNamespace: NationalInstruments.DAQmxpublic override int GetHashCode()RemarksTwo CODataFrequency objects might have the same hash code even though they represent different values. ReturnsA 32-bit signed integer hash code.

### GetHashCode()

Returns a hash code for the [CODataFrequency](nationalinstruments-daqmx-codatafrequency.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override int GetHashCode()

#### Remarks

Two [CODataFrequency](nationalinstruments-daqmx-codatafrequency.html) objects might have the same hash code even though they represent different values.

#### Returns

A 32-bit signed integer hash code.

Parent topic:

CODataFrequency Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatafrequency-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 01252: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatafrequency-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatafrequency-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStreaming

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

CODataFrequency Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatafrequency-operator_eq__codatafrequency-codatafrequency.html language=enus -->
## TOPIC 01253: operator==(CODataFrequency, CODataFrequency)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatafrequency-operator_eq__codatafrequency-codatafrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatafrequency-operator_eq__codatafrequency-codatafrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two CODataFrequency objects are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator==(CODataFrequency obj1, CODataFrequency obj2)ParametersNameTypeDescriptionobj1CODataFrequencyA CODataFrequency object.obj2CODataFrequencyA CODataFrequency object.Returnstrue i

### operator==(CODataFrequency, CODataFrequency)

Returns true if two [CODataFrequency](nationalinstruments-daqmx-codatafrequency.html) objects are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator==(CODataFrequency obj1, CODataFrequency obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | CODataFrequency | A CODataFrequency object. |
| obj2 | CODataFrequency | A CODataFrequency object. |

#### Returns

true if the values of *obj1*  and *obj2*  are equal.

Parent topic:

CODataFrequency Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatafrequency-operator_neq__codatafrequency-codatafrequency.html language=enus -->
## TOPIC 01254: operator!=(CODataFrequency, CODataFrequency)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatafrequency-operator_neq__codatafrequency-codatafrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatafrequency-operator_neq__codatafrequency-codatafrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two CODataFrequency objects are not equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator!=(CODataFrequency obj1, CODataFrequency obj2)ParametersNameTypeDescriptionobj1CODataFrequencyA CODataFrequency object.obj2CODataFrequencyA CODataFrequency object.Returnstr

### operator!=(CODataFrequency, CODataFrequency)

Returns true if two [CODataFrequency](nationalinstruments-daqmx-codatafrequency.html) objects are not equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator!=(CODataFrequency obj1, CODataFrequency obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | CODataFrequency | A CODataFrequency object. |
| obj2 | CODataFrequency | A CODataFrequency object. |

#### Returns

true if the values of *obj1*  and *obj2*  are not equal.

Parent topic:

CODataFrequency Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatafrequency.html language=enus -->
## TOPIC 01255: CODataFrequency Data Structure

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatafrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatafrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a counter output specified in terms of frequency and duty cycle. Derives fromISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic struct CODataFrequency : ISerializableThread SafetyAny members of this type are not guaranteed to be thread safe.ConstructorsNameDescriptionCODataFr

### CODataFrequency Data Structure

Encapsulates a counter output specified in terms of frequency and duty cycle.

#### Derives from

- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public struct CODataFrequency : ISerializable

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CODataFrequency(double, double) | Initializes a new instance of the CODataFrequency object with the specified initial values. |

#### Properties

| Name | Description |
| --- | --- |
| DutyCycle | Gets or sets the duty cycle of the pulse. |
| Frequency | Gets or sets the frequency of the pulse. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Returns a value indicating if this instance is equal to the specified object. |
| Equals(CODataFrequency) | Returns a value indicating if this instance is equal to the specified CODataFrequency object. |
| GetHashCode() | Returns a hash code for the CODataFrequency object. |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |
| Equals(CODataFrequency, CODataFrequency) | Returns a value indicating if two specified instances of CODataFrequency are equal. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(CODataFrequency, CODataFrequency) | Returns true if two CODataFrequency objects are not equal. |
| operator==(CODataFrequency, CODataFrequency) | Returns true if two CODataFrequency objects are equal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-codataticks__int-int.html language=enus -->
## TOPIC 01256: CODataTicks(int, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-codataticks__int-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-codataticks__int-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CODataTicks object with the specified initial values. SyntaxNamespace: NationalInstruments.DAQmxpublic CODataTicks(int lowTicks, int highTicks)ParametersNameTypeDescriptionlowTicksintThe number of timebase ticks the pulse is low.highTicksintThe number of timebase ti

### CODataTicks(int, int)

Initializes a new instance of the [CODataTicks](nationalinstruments-daqmx-codataticks.html) object with the specified initial values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public CODataTicks(int lowTicks, int highTicks)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| lowTicks | int | The number of timebase ticks the pulse is low. |
| highTicks | int | The number of timebase ticks the pulse is high. |

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-codataticks__uint-uint.html language=enus -->
## TOPIC 01257: CODataTicks(uint, uint)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-codataticks__uint-uint.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-codataticks__uint-uint.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CODataTicks object with the specified unsigned initial values. SyntaxNamespace: NationalInstruments.DAQmxpublic CODataTicks(uint lowTicks, uint highTicks)ParametersNameTypeDescriptionlowTicksuintThe number of timebase ticks the pulse is low.highTicksuintThe number o

### CODataTicks(uint, uint)

Initializes a new instance of the [CODataTicks](nationalinstruments-daqmx-codataticks.html) object with the specified unsigned initial values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public CODataTicks(uint lowTicks, uint highTicks)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| lowTicks | uint | The number of timebase ticks the pulse is low. |
| highTicks | uint | The number of timebase ticks the pulse is high. |

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-equals__codataticks-codataticks.html language=enus -->
## TOPIC 01258: Equals(CODataTicks, CODataTicks)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-equals__codataticks-codataticks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-equals__codataticks-codataticks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if two specified instances of CODataTicks are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool Equals(CODataTicks obj1, CODataTicks obj2)ParametersNameTypeDescriptionobj1CODataTicksA CODataTicks object.obj2CODataTicksA CODataTicks object.Returnstrue if o

### Equals(CODataTicks, CODataTicks)

Returns a value indicating if two specified instances of [CODataTicks](nationalinstruments-daqmx-codataticks.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool Equals(CODataTicks obj1, CODataTicks obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | CODataTicks | A CODataTicks object. |
| obj2 | CODataTicks | A CODataTicks object. |

#### Returns

true if *obj1*  and *obj2*  are equal.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-equals__codataticks.html language=enus -->
## TOPIC 01259: Equals(CODataTicks)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-equals__codataticks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-equals__codataticks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if this instance is equal to the specified CODataTicks object. SyntaxNamespace: NationalInstruments.DAQmxpublic bool Equals(CODataTicks obj)ParametersNameTypeDescriptionobjCODataTicksA CODataTicks object to compare with this instance.Returnstrue if obj has the same low tic

### Equals(CODataTicks)

Returns a value indicating if this instance is equal to the specified [CODataTicks](nationalinstruments-daqmx-codataticks.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool Equals(CODataTicks obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | CODataTicks | A CODataTicks object to compare with this instance. |

#### Returns

true if *obj*  has the same low ticks and high ticks as this instance.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-equals__object.html language=enus -->
## TOPIC 01260: Equals(object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-equals__object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if this instance is equal to the specified object. SyntaxNamespace: NationalInstruments.DAQmxpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectAn object to compare with this instance.Returnstrue if obj is a CODataTicks object that has the same lo

### Equals(object)

Returns a value indicating if this instance is equal to the specified object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | An object to compare with this instance. |

#### Returns

true if *obj*  is a [CODataTicks](nationalinstruments-daqmx-codataticks.html) object that has the same low ticks and high ticks as this instance.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-gethashcode.html language=enus -->
## TOPIC 01261: GetHashCode()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-gethashcode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a hash code for the CODataTicks object. SyntaxNamespace: NationalInstruments.DAQmxpublic override int GetHashCode()RemarksTwo CODataTicks objects might have the same hash code even though they represent different values. ReturnsA 32-bit signed integer hash code.

### GetHashCode()

Returns a hash code for the [CODataTicks](nationalinstruments-daqmx-codataticks.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override int GetHashCode()

#### Remarks

Two [CODataTicks](nationalinstruments-daqmx-codataticks.html) objects might have the same hash code even though they represent different values.

#### Returns

A 32-bit signed integer hash code.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 01262: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStreaming

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-highticksint32.html language=enus -->
## TOPIC 01263: HighTicksInt32

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-highticksint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-highticksint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of timebase ticks the pulse is high. SyntaxNamespace: NationalInstruments.DAQmxpublic int HighTicksInt32 { get; set; }RemarksThe number of timebase ticks the pulse is high.

### HighTicksInt32

Gets or sets the number of timebase ticks the pulse is high.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int HighTicksInt32 { get; set; }

#### Remarks

The number of timebase ticks the pulse is high.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-highticksuint32.html language=enus -->
## TOPIC 01264: HighTicksUInt32

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-highticksuint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-highticksuint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of timebase ticks the pulse is high. SyntaxNamespace: NationalInstruments.DAQmxpublic uint HighTicksUInt32 { get; set; }RemarksThe number of timebase ticks the pulse is high.

### HighTicksUInt32

Gets or sets the number of timebase ticks the pulse is high.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint HighTicksUInt32 { get; set; }

#### Remarks

The number of timebase ticks the pulse is high.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-lowticksint32.html language=enus -->
## TOPIC 01265: LowTicksInt32

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-lowticksint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-lowticksint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of timebase ticks the pulse is low. SyntaxNamespace: NationalInstruments.DAQmxpublic int LowTicksInt32 { get; set; }RemarksThe number of timebase ticks the pulse is low.

### LowTicksInt32

Gets or sets the number of timebase ticks the pulse is low.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int LowTicksInt32 { get; set; }

#### Remarks

The number of timebase ticks the pulse is low.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-lowticksuint32.html language=enus -->
## TOPIC 01266: LowTicksUInt32

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-lowticksuint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-lowticksuint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of timebase ticks the pulse is low. SyntaxNamespace: NationalInstruments.DAQmxpublic uint LowTicksUInt32 { get; set; }RemarksThe number of timebase ticks the pulse is low.

### LowTicksUInt32

Gets or sets the number of timebase ticks the pulse is low.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint LowTicksUInt32 { get; set; }

#### Remarks

The number of timebase ticks the pulse is low.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-operator_eq__codataticks-codataticks.html language=enus -->
## TOPIC 01267: operator==(CODataTicks, CODataTicks)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-operator_eq__codataticks-codataticks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-operator_eq__codataticks-codataticks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two CODataTicks objects are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator==(CODataTicks obj1, CODataTicks obj2)ParametersNameTypeDescriptionobj1CODataTicksA CODataTicks object.obj2CODataTicksA CODataTicks object.Returnstrue if the values of obj1 and obj

### operator==(CODataTicks, CODataTicks)

Returns true if two [CODataTicks](nationalinstruments-daqmx-codataticks.html) objects are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator==(CODataTicks obj1, CODataTicks obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | CODataTicks | A CODataTicks object. |
| obj2 | CODataTicks | A CODataTicks object. |

#### Returns

true if the values of *obj1*  and *obj2*  are equal.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks-operator_neq__codataticks-codataticks.html language=enus -->
## TOPIC 01268: operator!=(CODataTicks, CODataTicks)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks-operator_neq__codataticks-codataticks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks-operator_neq__codataticks-codataticks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two CODataTicks objects are not equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator!=(CODataTicks obj1, CODataTicks obj2)ParametersNameTypeDescriptionobj1CODataTicksA CODataTicks object.obj2CODataTicksA CODataTicks object.Returnstrue if the values of obj1 and

### operator!=(CODataTicks, CODataTicks)

Returns true if two [CODataTicks](nationalinstruments-daqmx-codataticks.html) objects are not equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator!=(CODataTicks obj1, CODataTicks obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | CODataTicks | A CODataTicks object. |
| obj2 | CODataTicks | A CODataTicks object. |

#### Returns

true if the values of *obj1*  and *obj2*  are not equal.

Parent topic:

CODataTicks Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codataticks.html language=enus -->
## TOPIC 01269: CODataTicks Data Structure

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codataticks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codataticks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a counter output specified in terms of timebase ticks. Derives fromISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic struct CODataTicks : ISerializableThread SafetyAny members of this type are not guaranteed to be thread safe.ConstructorsNameDescriptionCODataTicks(uint, uint

### CODataTicks Data Structure

Encapsulates a counter output specified in terms of timebase ticks.

#### Derives from

- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public struct CODataTicks : ISerializable

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CODataTicks(uint, uint) | Initializes a new instance of the CODataTicks object with the specified unsigned initial values. |
| CODataTicks(int, int) | Initializes a new instance of the CODataTicks object with the specified initial values. |

#### Properties

| Name | Description |
| --- | --- |
| HighTicksInt32 | Gets or sets the number of timebase ticks the pulse is high. |
| HighTicksUInt32 | Gets or sets the number of timebase ticks the pulse is high. |
| LowTicksInt32 | Gets or sets the number of timebase ticks the pulse is low. |
| LowTicksUInt32 | Gets or sets the number of timebase ticks the pulse is low. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Returns a value indicating if this instance is equal to the specified object. |
| Equals(CODataTicks) | Returns a value indicating if this instance is equal to the specified CODataTicks object. |
| GetHashCode() | Returns a hash code for the CODataTicks object. |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |
| Equals(CODataTicks, CODataTicks) | Returns a value indicating if two specified instances of CODataTicks are equal. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(CODataTicks, CODataTicks) | Returns true if two CODataTicks objects are not equal. |
| operator==(CODataTicks, CODataTicks) | Returns true if two CODataTicks objects are equal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-codatatime__double-double.html language=enus -->
## TOPIC 01270: CODataTime(double, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-codatatime__double-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-codatatime__double-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CODataTime object with the specified initial values. SyntaxNamespace: NationalInstruments.DAQmxpublic CODataTime(double lowTime, double highTime)ParametersNameTypeDescriptionlowTimedoubleThe amount of time the pulse is low.highTimedoubleThe amount of time the pulse

### CODataTime(double, double)

Initializes a new instance of the [CODataTime](nationalinstruments-daqmx-codatatime.html) object with the specified initial values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public CODataTime(double lowTime, double highTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| lowTime | double | The amount of time the pulse is low. |
| highTime | double | The amount of time the pulse is high. |

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-equals__codatatime-codatatime.html language=enus -->
## TOPIC 01271: Equals(CODataTime, CODataTime)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-equals__codatatime-codatatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-equals__codatatime-codatatime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if two specified instances of CODataTime are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool Equals(CODataTime obj1, CODataTime obj2)ParametersNameTypeDescriptionobj1CODataTimeA CODataTime object.obj2CODataTimeA CODataTime object.Returnstrue if obj1 and

### Equals(CODataTime, CODataTime)

Returns a value indicating if two specified instances of [CODataTime](nationalinstruments-daqmx-codatatime.html) are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool Equals(CODataTime obj1, CODataTime obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | CODataTime | A CODataTime object. |
| obj2 | CODataTime | A CODataTime object. |

#### Returns

true if *obj1*  and *obj2*  are equal.

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-equals__codatatime.html language=enus -->
## TOPIC 01272: Equals(CODataTime)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-equals__codatatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-equals__codatatime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if this instance is equal to the specified CODataTime object. SyntaxNamespace: NationalInstruments.DAQmxpublic bool Equals(CODataTime obj)ParametersNameTypeDescriptionobjCODataTimeA CODataTime object to compare with this instance.Returnstrue if obj has the same low time an

### Equals(CODataTime)

Returns a value indicating if this instance is equal to the specified [CODataTime](nationalinstruments-daqmx-codatatime.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool Equals(CODataTime obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | CODataTime | A CODataTime object to compare with this instance. |

#### Returns

true if *obj*  has the same low time and high time as this instance.

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-equals__object.html language=enus -->
## TOPIC 01273: Equals(object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-equals__object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a value indicating if this instance is equal to the specified object. SyntaxNamespace: NationalInstruments.DAQmxpublic override bool Equals(object obj)ParametersNameTypeDescriptionobjobjectAn object to compare with this instance.Returnstrue if obj is a CODataTime object that has the same low

### Equals(object)

Returns a value indicating if this instance is equal to the specified object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override bool Equals(object obj)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj | object | An object to compare with this instance. |

#### Returns

true if *obj*  is a [CODataTime](nationalinstruments-daqmx-codatatime.html) object that has the same low time and high time as this instance.

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-gethashcode.html language=enus -->
## TOPIC 01274: GetHashCode()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-gethashcode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a hash code for the CODataTime object. SyntaxNamespace: NationalInstruments.DAQmxpublic override int GetHashCode()RemarksTwo CODataTime objects might have the same hash code even though they represent different values. ReturnsA 32-bit signed integer hash code.

### GetHashCode()

Returns a hash code for the [CODataTime](nationalinstruments-daqmx-codatatime.html) object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override int GetHashCode()

#### Remarks

Two [CODataTime](nationalinstruments-daqmx-codatatime.html) objects might have the same hash code even though they represent different values.

#### Returns

A 32-bit signed integer hash code.

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 01275: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxpublic void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStreaming

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-hightime.html language=enus -->
## TOPIC 01276: HighTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-hightime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-hightime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time the pulse is high. SyntaxNamespace: NationalInstruments.DAQmxpublic double HighTime { get; set; }RemarksThe amount of time the pulse is high.

### HighTime

Gets or sets the amount of time the pulse is high.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double HighTime { get; set; }

#### Remarks

The amount of time the pulse is high.

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-lowtime.html language=enus -->
## TOPIC 01277: LowTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-lowtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-lowtime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time the pulse is low. SyntaxNamespace: NationalInstruments.DAQmxpublic double LowTime { get; set; }RemarksThe amount of time the pulse is low.

### LowTime

Gets or sets the amount of time the pulse is low.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double LowTime { get; set; }

#### Remarks

The amount of time the pulse is low.

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-operator_eq__codatatime-codatatime.html language=enus -->
## TOPIC 01278: operator==(CODataTime, CODataTime)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-operator_eq__codatatime-codatatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-operator_eq__codatatime-codatatime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two CODataTime objects are equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator==(CODataTime obj1, CODataTime obj2)ParametersNameTypeDescriptionobj1CODataTimeA CODataTime object.obj2CODataTimeA CODataTime object.Returnstrue if the values of obj1 and obj2 are e

### operator==(CODataTime, CODataTime)

Returns true if two [CODataTime](nationalinstruments-daqmx-codatatime.html) objects are equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator==(CODataTime obj1, CODataTime obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | CODataTime | A CODataTime object. |
| obj2 | CODataTime | A CODataTime object. |

#### Returns

true if the values of *obj1*  and *obj2*  are equal.

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime-operator_neq__codatatime-codatatime.html language=enus -->
## TOPIC 01279: operator!=(CODataTime, CODataTime)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime-operator_neq__codatatime-codatatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime-operator_neq__codatatime-codatatime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if two CODataTime objects are not equal. SyntaxNamespace: NationalInstruments.DAQmxpublic static bool operator!=(CODataTime obj1, CODataTime obj2)ParametersNameTypeDescriptionobj1CODataTimeA CODataTime object.obj2CODataTimeA CODataTime object.Returnstrue if the values of obj1 and obj2 a

### operator!=(CODataTime, CODataTime)

Returns true if two [CODataTime](nationalinstruments-daqmx-codatatime.html) objects are not equal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public static bool operator!=(CODataTime obj1, CODataTime obj2)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| obj1 | CODataTime | A CODataTime object. |
| obj2 | CODataTime | A CODataTime object. |

#### Returns

true if the values of *obj1*  and *obj2*  are not equal.

Parent topic:

CODataTime Data Structure

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatime.html language=enus -->
## TOPIC 01280: CODataTime Data Structure

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates a counter output specified in terms of time. Derives fromISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic struct CODataTime : ISerializableThread SafetyAny members of this type are not guaranteed to be thread safe.ConstructorsNameDescriptionCODataTime(double, double)Initial

### CODataTime Data Structure

Encapsulates a counter output specified in terms of time.

#### Derives from

- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public struct CODataTime : ISerializable

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CODataTime(double, double) | Initializes a new instance of the CODataTime object with the specified initial values. |

#### Properties

| Name | Description |
| --- | --- |
| HighTime | Gets or sets the amount of time the pulse is high. |
| LowTime | Gets or sets the amount of time the pulse is low. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) | Returns a value indicating if this instance is equal to the specified object. |
| Equals(CODataTime) | Returns a value indicating if this instance is equal to the specified CODataTime object. |
| GetHashCode() | Returns a hash code for the CODataTime object. |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |
| Equals(CODataTime, CODataTime) | Returns a value indicating if two specified instances of CODataTime are equal. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(CODataTime, CODataTime) | Returns true if two CODataTime objects are not equal. |
| operator==(CODataTime, CODataTime) | Returns true if two CODataTime objects are equal. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatransfermechanism.html language=enus -->
## TOPIC 01281: CODataTransferMechanism Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CODataTransferMechanismRemarksSpecifies the data transfer mode for the device. For buffered operations, use DM

### CODataTransferMechanism Enumeration

Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CODataTransferMechanism

#### Remarks

Specifies the data transfer mode for the device. For buffered operations, use DMA or USB Bulk. For non-buffered operations, use Polled. Use this enumeration to get or set the value of [DataTransferMechanism](nationalinstruments-daqmx-cochannel-datatransfermechanism.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Dma | 10054 | Direct Memory Access. Data transfers take place independently from the application. |
| Interrupts | 10204 | Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels. |
| ProgrammedIO | 10264 | Data transfers take place when you call reading from the task or writing to the task. |
| UsbBulk | 12590 | Data transfers take place independently from the application using a USB bulk pipe. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-codatatransferrequestcondition.html language=enus -->
## TOPIC 01282: CODataTransferRequestCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-codatatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-codatatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the buffer to the onboard memory of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CODataTransferRequestConditionRemarksSpecifies under what condition to transfer data from the buffer to the onboard memory of the device. Use thi

### CODataTransferRequestCondition Enumeration

Specifies under what condition to transfer data from the buffer to the onboard memory of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CODataTransferRequestCondition

#### Remarks

Specifies under what condition to transfer data from the buffer to the onboard memory of the device. Use this enumeration to get or set the value of [DataTransferRequestCondition](nationalinstruments-daqmx-cochannel-datatransferrequestcondition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnBoardMemoryEmpty | 10235 | Transfer data to the device only when there is no data in the onboard memory of the device. |
| OnBoardMemoryHalfFullOrLess | 10239 | Transfer data to the device any time the onboard memory is less than half full. |
| OnBoardMemoryNotFull | 10242 | Transfer data to the device any time the onboard memory of the device is not full. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cooutputstate.html language=enus -->
## TOPIC 01283: COOutputState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cooutputstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cooutputstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current state of the output terminal of the counter. SyntaxNamespace: NationalInstruments.DAQmxpublic enum COOutputStateRemarksIndicates the current state of the output terminal of the counter. Use this enumeration to get or set the value of OutputState.MembersNameValueDescriptionHigh1

### COOutputState Enumeration

Indicates the current state of the output terminal of the counter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum COOutputState

#### Remarks

Indicates the current state of the output terminal of the counter. Use this enumeration to get or set the value of [OutputState](nationalinstruments-daqmx-cochannel-outputstate.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | High state. |
| Low | 10214 | Low state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cooutputtype.html language=enus -->
## TOPIC 01284: COOutputType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cooutputtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cooutputtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates how to define pulses generated on the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum COOutputTypeRemarksIndicates how to define pulses generated on the channel. Use this enumeration to get or set the value of OutputType.MembersNameValueDescriptionPulseTime10269Generate puls

### COOutputType Enumeration

Indicates how to define pulses generated on the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum COOutputType

#### Remarks

Indicates how to define pulses generated on the channel. Use this enumeration to get or set the value of [OutputType](nationalinstruments-daqmx-cochannel-outputtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PulseTime | 10269 | Generate pulses defined by the time the pulse is at a low state and the time the pulse is at a high state. |
| PulseFrequency | 10119 | Generate digital pulses defined by frequency and duty cycle. |
| PulseTicks | 10268 | Generate digital pulses defined by the number of timebase ticks that the pulse is at a low state and the number of timebase ticks that the pulse is at a high state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-copulsefrequencyunits.html language=enus -->
## TOPIC 01285: COPulseFrequencyUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-copulsefrequencyunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-copulsefrequencyunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units in which to define pulse frequency. SyntaxNamespace: NationalInstruments.DAQmxpublic enum COPulseFrequencyUnitsRemarksSpecifies the units in which to define pulse frequency. Use this enumeration to get or set the value of PulseFrequencyUnits.MembersNameValueDescriptionHertz10373H

### COPulseFrequencyUnits Enumeration

Specifies the units in which to define pulse frequency.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum COPulseFrequencyUnits

#### Remarks

Specifies the units in which to define pulse frequency. Use this enumeration to get or set the value of [PulseFrequencyUnits](nationalinstruments-daqmx-cochannel-pulsefrequencyunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Hertz | 10373 | Hertz. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-copulseidlestate.html language=enus -->
## TOPIC 01286: COPulseIdleState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-copulseidlestate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-copulseidlestate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resting state of the output terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic enum COPulseIdleStateRemarksSpecifies the resting state of the output terminal. Use this enumeration to get or set the value of PulseIdleState.MembersNameValueDescriptionHigh10192High state. Low10214

### COPulseIdleState Enumeration

Specifies the resting state of the output terminal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum COPulseIdleState

#### Remarks

Specifies the resting state of the output terminal. Use this enumeration to get or set the value of [PulseIdleState](nationalinstruments-daqmx-cochannel-pulseidlestate.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | High state. |
| Low | 10214 | Low state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-copulsetimeunits.html language=enus -->
## TOPIC 01287: COPulseTimeUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-copulsetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-copulsetimeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units in which to define high and low pulse time. SyntaxNamespace: NationalInstruments.DAQmxpublic enum COPulseTimeUnitsRemarksSpecifies the units in which to define high and low pulse time. Use this enumeration to get or set the value of PulseTimeUnits.MembersNameValueDescriptionSecon

### COPulseTimeUnits Enumeration

Specifies the units in which to define high and low pulse time.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum COPulseTimeUnits

#### Remarks

Specifies the units in which to define high and low pulse time. Use this enumeration to get or set the value of [PulseTimeUnits](nationalinstruments-daqmx-cochannel-pulsetimeunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Seconds | 10364 | Seconds. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr2-reallocationpolicy.html language=enus -->
## TOPIC 01288: BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(int samplesPerChannel, AsyncCallback callback, object state, double[,] data, ReallocationPol

### BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double, ReallocationPolicy)

Begins an asynchronous read of one or more Double samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(int samplesPerChannel, AsyncCallback callback, object state, double[,] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call

[EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int)](nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html)

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | double | An initialized 2D array of Double samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr2.html language=enus -->
## TOPIC 01289: BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(int samplesPerChannel, AsyncCallback callback, object state, double[,] data)RemarksIf the da

### BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double)

Begins an asynchronous read of one or more Double samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(int samplesPerChannel, AsyncCallback callback, object state, double[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int)](nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | double | An initialized 2D array of Double samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr2-reallocationpolicy.html language=enus -->
## TOPIC 01290: BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(int samplesPerChannel, AsyncCallback callback, object state, int[,] data, ReallocationPolicy p

### BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int, ReallocationPolicy)

Begins an asynchronous read of one or more Int32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(int samplesPerChannel, AsyncCallback callback, object state, int[,] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call

[EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int)](nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specifynullif you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specifynullif you do not need to pass any additional information to the callback. |
| data | int | An initialized 2D array of Int32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr2.html language=enus -->
## TOPIC 01291: BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(int samplesPerChannel, AsyncCallback callback, object state, int[,] data)RemarksIf the data bu

### BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int)

Begins an asynchronous read of one or more Int32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(int samplesPerChannel, AsyncCallback callback, object state, int[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call

[EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int)](nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | int | An initialized 2D array of Int32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr2-reallocationpolicy.html language=enus -->
## TOPIC 01292: BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint, ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr2-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr2-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(int samplesPerChannel, AsyncCallback callback, object state, uint[,] data, ReallocationPolic

### BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint, ReallocationPolicy)

Begins an asynchronous read of one or more UInt32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(int samplesPerChannel, AsyncCallback callback, object state, uint[,] data, ReallocationPolicy policy)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int)](nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specifynullif you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | uint | An initialized 2D array of UInt32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr2.html language=enus -->
## TOPIC 01293: BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr2.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr2.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(int samplesPerChannel, AsyncCallback callback, object state, uint[,] data)RemarksIf the data

### BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint)

Begins an asynchronous read of one or more UInt32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(int samplesPerChannel, AsyncCallback callback, object state, uint[,] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int)](nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | uint | An initialized 2D array of UInt32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampledouble__int-asynccallback-object.html language=enus -->
## TOPIC 01294: BeginReadMultiSampleDouble(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampledouble__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampledouble__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSampleDouble(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions t

### BeginReadMultiSampleDouble(int, AsyncCallback, object)

Begins an asynchronous read of one or more Double samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSampleDouble(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with

BeginReadMultiSampleDouble(int, AsyncCallback, object), call

[EndReadMultiSampleDouble(IAsyncResult)](nationalinstruments-daqmx-countermultichannelreader-endreadmultisampledouble__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampleint32__int-asynccallback-object.html language=enus -->
## TOPIC 01295: BeginReadMultiSampleInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampleint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampleint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSampleInt32(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions tha

### BeginReadMultiSampleInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more Int32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSampleInt32(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with

BeginReadMultiSampleInt32(int, AsyncCallback, object), call [EndReadMultiSampleInt32(IAsyncResult)](nationalinstruments-daqmx-countermultichannelreader-endreadmultisampleint32__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampleuint32__int-asynccallback-object.html language=enus -->
## TOPIC 01296: BeginReadMultiSampleUInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampleuint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampleuint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSampleUInt32(int samplesPerChannel, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions t

### BeginReadMultiSampleUInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more UInt32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSampleUInt32(int samplesPerChannel, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSampleUInt32(int, AsyncCallback, object), call [EndReadMultiSampleUInt32(IAsyncResult)](nationalinstruments-daqmx-countermultichannelreader-endreadmultisampleuint32__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampledouble__asynccallback-object.html language=enus -->
## TOPIC 01297: BeginReadSingleSampleDouble(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampledouble__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampledouble__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single Double sample from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleDouble(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asy

### BeginReadSingleSampleDouble(AsyncCallback, object)

Begins an asynchronous read of a single Double sample from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleDouble(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, object), call [EndReadSingleSampleDouble(IAsyncResult)](nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampledouble__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampleint32__asynccallback-object.html language=enus -->
## TOPIC 01298: BeginReadSingleSampleInt32(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampleint32__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampleint32__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single Int32 sample from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleInt32(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an async

### BeginReadSingleSampleInt32(AsyncCallback, object)

Begins an asynchronous read of a single Int32 sample from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleInt32(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, object), call [EndReadSingleSampleInt32(IAsyncResult)](nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampleint32__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampleuint32__asynccallback-object.html language=enus -->
## TOPIC 01299: BeginReadSingleSampleUInt32(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampleuint32__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampleuint32__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single UInt32 sample from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleUInt32(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asy

### BeginReadSingleSampleUInt32(AsyncCallback, object)

Begins an asynchronous read of a single UInt32 sample from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleUInt32(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with

BeginReadSingleSampleUInt32(AsyncCallback, object), call [EndReadSingleSampleUInt32(IAsyncResult)](nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampleuint32__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx scales the read data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-countermultichannelreader__daqstream.html language=enus -->
## TOPIC 01300: CounterMultiChannelReader(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-countermultichannelreader__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-countermultichannelreader__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the CounterMultiChannelReader class to read from the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterMultiChannelReader(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for readers to access

### CounterMultiChannelReader(DaqStream)

Creates a new instance of the [CounterMultiChannelReader](nationalinstruments-daqmx-countermultichannelreader.html) class to read from the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public CounterMultiChannelReader(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for readers to access the samples generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to read. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html language=enus -->
## TOPIC 01301: EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult asyncResult, out in

### EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[, ])](nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of Double samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html language=enus -->
## TOPIC 01302: EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult asyncResult, out int actual

### EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[, ])](nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of Int32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html language=enus -->
## TOPIC 01303: EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[, ]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult asyncResult, out int ac

### EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[, ])](nationalinstruments-daqmx-countermultichannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr2.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult asyncResult, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If you call this method before the asynchronous read IAsyncResult is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[, ]). |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A 2D array of UInt32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[, ]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endreadmultisampledouble__iasyncresult.html language=enus -->
## TOPIC 01304: EndReadMultiSampleDouble(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endreadmultisampledouble__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endreadmultisampledouble__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] EndReadMultiSampleDouble(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSampleDouble(IAsyn

### EndReadMultiSampleDouble(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSampleDouble(int, AsyncCallback, object)](nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampledouble__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] EndReadMultiSampleDouble(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSampleDouble(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSampleDouble(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSampleDouble(int, AsyncCallback, object) . |

#### Returns

A 2D array of Double samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSampleDouble(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endreadmultisampleint32__iasyncresult.html language=enus -->
## TOPIC 01305: EndReadMultiSampleInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endreadmultisampleint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endreadmultisampleint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] EndReadMultiSampleInt32(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSampleInt32(IAsyncResul

### EndReadMultiSampleInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSampleInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampleint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] EndReadMultiSampleInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSampleInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSampleInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSampleInt32(int, AsyncCallback, object) . |

#### Returns

A 2D array of Int32 samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSampleInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endreadmultisampleuint32__iasyncresult.html language=enus -->
## TOPIC 01306: EndReadMultiSampleUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endreadmultisampleuint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endreadmultisampleuint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] EndReadMultiSampleUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSampleUInt32(IAsyncR

### EndReadMultiSampleUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSampleUInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-countermultichannelreader-beginreadmultisampleuint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] EndReadMultiSampleUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSampleUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSampleUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSampleUInt32(int, AsyncCallback, object) . |

#### Returns

A 2D array of UInt32 samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSampleUInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampledouble__iasyncresult.html language=enus -->
## TOPIC 01307: EndReadSingleSampleDouble(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampledouble__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampledouble__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, object) and retrieves the read sample. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] EndReadSingleSampleDouble(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleDouble(IAsyncRes

### EndReadSingleSampleDouble(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleDouble(AsyncCallback, object)](nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampledouble__asynccallback-object.html) and retrieves the read sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] EndReadSingleSampleDouble(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleDouble(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleDouble(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleDouble(AsyncCallback, object). |

#### Returns

A 1D array of Double samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleDouble(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampleint32__iasyncresult.html language=enus -->
## TOPIC 01308: EndReadSingleSampleInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampleint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampleint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, object) and retrieves the read sample. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] EndReadSingleSampleInt32(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleInt32(IAsyncResult) b

### EndReadSingleSampleInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleInt32(AsyncCallback, object)](nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampleint32__asynccallback-object.html) and retrieves the read sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] EndReadSingleSampleInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleInt32(AsyncCallback, object). |

#### Returns

A 1D array of Int32 samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleInt32(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampleuint32__iasyncresult.html language=enus -->
## TOPIC 01309: EndReadSingleSampleUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampleuint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-endreadsinglesampleuint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, object) and retrieves the read sample. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] EndReadSingleSampleUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleUInt32(IAsyncResul

### EndReadSingleSampleUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleUInt32(AsyncCallback, object)](nationalinstruments-daqmx-countermultichannelreader-beginreadsinglesampleuint32__asynccallback-object.html) and retrieves the read sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] EndReadSingleSampleUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleUInt32(AsyncCallback, object). |

#### Returns

A 1D array of UInt32 samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleUInt32(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampledouble__int-ref-out.html language=enus -->
## TOPIC 01310: MemoryOptimizedReadMultiSampleDouble(int, ref double, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampledouble__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampledouble__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Double samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] MemoryOptimizedReadMultiSampleDouble(int samplesPerChannel, ref double[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the data buffer is large eno

### MemoryOptimizedReadMultiSampleDouble(int, ref double, out int)

Reads one or more Double samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] MemoryOptimizedReadMultiSampleDouble(int samplesPerChannel, ref double[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref double | An initialized 2D array of Double samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampledouble__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01311: MemoryOptimizedReadMultiSampleDouble(int, ref double, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampledouble__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampledouble__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Double samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] MemoryOptimizedReadMultiSampleDouble(int samplesPerChannel, ref double[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)RemarksIf t

### MemoryOptimizedReadMultiSampleDouble(int, ref double, ReallocationPolicy, out int)

Reads one or more Double samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] MemoryOptimizedReadMultiSampleDouble(int samplesPerChannel, ref double[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref double | An initialized 2D array of Double samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleint32__int-ref-out.html language=enus -->
## TOPIC 01312: MemoryOptimizedReadMultiSampleInt32(int, ref int, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleint32__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleint32__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Int32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] MemoryOptimizedReadMultiSampleInt32(int samplesPerChannel, ref int[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the data buffer is large enough to h

### MemoryOptimizedReadMultiSampleInt32(int, ref int, out int)

Reads one or more Int32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] MemoryOptimizedReadMultiSampleInt32(int samplesPerChannel, ref int[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref int | An initialized 2D array of Int32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleint32__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01313: MemoryOptimizedReadMultiSampleInt32(int, ref int, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleint32__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleint32__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Int32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] MemoryOptimizedReadMultiSampleInt32(int samplesPerChannel, ref int[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)RemarksIf the data

### MemoryOptimizedReadMultiSampleInt32(int, ref int, ReallocationPolicy, out int)

Reads one or more Int32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] MemoryOptimizedReadMultiSampleInt32(int samplesPerChannel, ref int[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref int | An initialized 2D array of Int32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleuint32__int-ref-out.html language=enus -->
## TOPIC 01314: MemoryOptimizedReadMultiSampleUInt32(int, ref uint, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleuint32__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleuint32__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more UInt32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] MemoryOptimizedReadMultiSampleUInt32(int samplesPerChannel, ref uint[,] data, out int actualNumberOfSamplesPerChannelRead)RemarksIf the data buffer is large enough

### MemoryOptimizedReadMultiSampleUInt32(int, ref uint, out int)

Reads one or more UInt32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] MemoryOptimizedReadMultiSampleUInt32(int samplesPerChannel, ref uint[,] data, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref uint | An initialized 2D array of UInt32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleuint32__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01315: MemoryOptimizedReadMultiSampleUInt32(int, ref uint, ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleuint32__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-memoryoptimizedreadmultisampleuint32__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more UInt32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] MemoryOptimizedReadMultiSampleUInt32(int samplesPerChannel, ref uint[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)RemarksIf the d

### MemoryOptimizedReadMultiSampleUInt32(int, ref uint, ReallocationPolicy, out int)

Reads one or more UInt32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] MemoryOptimizedReadMultiSampleUInt32(int samplesPerChannel, ref uint[,] data, ReallocationPolicy policy, out int actualNumberOfSamplesPerChannelRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous analog input task.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref uint | An initialized 2D array of UInt32 samples that contains the read data. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in ChannelsToRead. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the read operation. Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesPerChannelRead | out int | The actual number of samples per channel read. This is useful when the reading operation yields fewer samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-readmultisampledouble__int.html language=enus -->
## TOPIC 01316: ReadMultiSampleDouble(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-readmultisampledouble__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-readmultisampledouble__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Double samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[,] ReadMultiSampleDouble(int samplesPerChannel)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to th

### ReadMultiSampleDouble(int)

Reads one or more Double samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[,] ReadMultiSampleDouble(int samplesPerChannel)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of Double samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-readmultisampleint32__int.html language=enus -->
## TOPIC 01317: ReadMultiSampleInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-readmultisampleint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-readmultisampleint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Int32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[,] ReadMultiSampleInt32(int samplesPerChannel)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the cha

### ReadMultiSampleInt32(int)

Reads one or more Int32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[,] ReadMultiSampleInt32(int samplesPerChannel)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of Int32 samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-readmultisampleuint32__int.html language=enus -->
## TOPIC 01318: ReadMultiSampleUInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-readmultisampleuint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-readmultisampleuint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more UInt32 samples from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[,] ReadMultiSampleUInt32(int samplesPerChannel)RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the

### ReadMultiSampleUInt32(int)

Reads one or more UInt32 samples from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[,] ReadMultiSampleUInt32(int samplesPerChannel)

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 2D array of UInt32 samples from the task. Each element in the first dimension of the array corresponds to a channel in the task. Each element in the second dimension of the array corresponds to a sample from each of the channels. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-readsinglesampledouble.html language=enus -->
## TOPIC 01319: ReadSingleSampleDouble()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-readsinglesampledouble.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-readsinglesampledouble.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single Double sample from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] ReadSingleSampleDouble()RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify th

### ReadSingleSampleDouble()

Reads a single Double sample from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] ReadSingleSampleDouble()

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of Double samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-readsinglesampleint32.html language=enus -->
## TOPIC 01320: ReadSingleSampleInt32()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-readsinglesampleint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-readsinglesampleint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single Int32 sample from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] ReadSingleSampleInt32()RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these u

### ReadSingleSampleInt32()

Reads a single Int32 sample from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] ReadSingleSampleInt32()

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of Int32 samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-readsinglesampleuint32.html language=enus -->
## TOPIC 01321: ReadSingleSampleUInt32()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-readsinglesampleuint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-readsinglesampleuint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single UInt32 sample from one or more CIChannel objects in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] ReadSingleSampleUInt32()RemarksNI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify thes

### ReadSingleSampleUInt32()

Reads a single UInt32 sample from one or more [CIChannel](nationalinstruments-daqmx-cichannel.html) objects in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] ReadSingleSampleUInt32()

#### Remarks

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A 1D array of UInt32 samples from the task. Each element in the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task or to the order of the channels you specify in [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-synchronizecallbacks.html language=enus -->
## TOPIC 01322: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-synchronizecallbacks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how events and callback delegates are invoked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SynchronizeCallbacks { get; set; }RemarksIn some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care w

### SynchronizeCallbacks

Specifies how events and callback delegates are invoked.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-synchronizingobject.html language=enus -->
## TOPIC 01323: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-synchronizingobject.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will error if used Gets or sets the object that marshals event-handler and callback calls. SyntaxNamespace: NationalInstruments.DAQmxpublic ISynchronizeInvoke SynchronizingObject { get; set

### SynchronizingObject

**Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will error if used** 
Gets or sets the object that marshals event-handler and callback calls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ISynchronizeInvoke SynchronizingObject { get; set; }

#### Remarks

The ISynchronizeInvoke representing the object that marshals the event-handler and callback calls. The default value is null.

null

Note

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader-tostring.html language=enus -->
## TOPIC 01324: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterMultiChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelreader.html language=enus -->
## TOPIC 01325: CounterMultiChannelReader Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelreader.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelreader.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for reading samples from one or more counter input channels in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class CounterMultiChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupp

### CounterMultiChannelReader Class

Contains methods for reading samples from one or more counter input channels in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class CounterMultiChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| CounterMultiChannelReader(DaqStream) | Creates a new instance of the CounterMultiChannelReader class to read from the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will error if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double, ReallocationPolicy) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int, ReallocationPolicy) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
| BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint, ReallocationPolicy) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
| BeginReadMultiSampleDouble(int, AsyncCallback, object) | Begins an asynchronous read of one or more Double samples from one or more CIChannel objects in a task. |
| BeginReadMultiSampleInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more Int32 samples from one or more CIChannel objects in a task. |
| BeginReadMultiSampleUInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more UInt32 samples from one or more CIChannel objects in a task. |
| BeginReadSingleSampleDouble(AsyncCallback, object) | Begins an asynchronous read of a single Double sample from one or more CIChannel objects in a task. |
| BeginReadSingleSampleInt32(AsyncCallback, object) | Begins an asynchronous read of a single Int32 sample from one or more CIChannel objects in a task. |
| BeginReadSingleSampleUInt32(AsyncCallback, object) | Begins an asynchronous read of a single UInt32 sample from one or more CIChannel objects in a task. |
| EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[, ]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[, ]) and retrieves the read samples. |
| EndReadMultiSampleDouble(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSampleInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSampleUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSampleDouble(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, object) and retrieves the read sample. |
| EndReadSingleSampleInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, object) and retrieves the read sample. |
| EndReadSingleSampleUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, object) and retrieves the read sample. |
| MemoryOptimizedReadMultiSampleDouble(int, ref double, ReallocationPolicy, out int) | Reads one or more Double samples from one or more CIChannel objects in a task. |
| MemoryOptimizedReadMultiSampleDouble(int, ref double, out int) | Reads one or more Double samples from one or more CIChannel objects in a task. |
| MemoryOptimizedReadMultiSampleInt32(int, ref int, ReallocationPolicy, out int) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
| MemoryOptimizedReadMultiSampleInt32(int, ref int, out int) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
| MemoryOptimizedReadMultiSampleUInt32(int, ref uint, out int) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
| MemoryOptimizedReadMultiSampleUInt32(int, ref uint, ReallocationPolicy, out int) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
| ReadMultiSampleDouble(int) | Reads one or more Double samples from one or more CIChannel objects in a task. |
| ReadMultiSampleInt32(int) | Reads one or more Int32 samples from one or more CIChannel objects in a task. |
| ReadMultiSampleUInt32(int) | Reads one or more UInt32 samples from one or more CIChannel objects in a task. |
| ReadSingleSampleDouble() | Reads a single Double sample from one or more CIChannel objects in a task. |
| ReadSingleSampleInt32() | Reads a single Int32 sample from one or more CIChannel objects in a task. |
| ReadSingleSampleUInt32() | Reads a single UInt32 sample from one or more CIChannel objects in a task. |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codatafrequency_arr1-asynccallback-object.html language=enus -->
## TOPIC 01326: BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codatafrequency_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codatafrequency_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single frequency sample to one or more COChannel objects in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency[] data, AsyncCallback callback, obje

### BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object)

Begins an asynchronous write of a single frequency sample to one or more [COChannel](nationalinstruments-daqmx-cochannel.html) objects in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countermultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataFrequency[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codataticks_arr1-asynccallback-object.html language=enus -->
## TOPIC 01327: BeginWriteSingleSample(bool, CODataTicks[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codataticks_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codataticks_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single ticks sample to one or more COChannel objects in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks[] data, AsyncCallback callback, object state

### BeginWriteSingleSample(bool, CODataTicks[], AsyncCallback, object)

Begins an asynchronous write of a single ticks sample to one or more [COChannel](nationalinstruments-daqmx-cochannel.html) objects in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countermultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTicks[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codatatime_arr1-asynccallback-object.html language=enus -->
## TOPIC 01328: BeginWriteSingleSample(bool, CODataTime[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codatatime_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codatatime_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a single time sample to one or more COChannel objects in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime[] data, AsyncCallback callback, object state)R

### BeginWriteSingleSample(bool, CODataTime[], AsyncCallback, object)

Begins an asynchronous write of a single time sample to one or more [COChannel](nationalinstruments-daqmx-cochannel.html) objects in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countermultichannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTime[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-countermultichannelwriter__daqstream.html language=enus -->
## TOPIC 01329: CounterMultiChannelWriter(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-countermultichannelwriter__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-countermultichannelwriter__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CounterMultiChannelWriter class to write to the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterMultiChannelWriter(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for the writer cla

### CounterMultiChannelWriter(DaqStream)

Initializes a new instance of the [CounterMultiChannelWriter](nationalinstruments-daqmx-countermultichannelwriter.html) class to write to the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public CounterMultiChannelWriter(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for the writer classes to provide samples to be generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to write to. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-endwrite__iasyncresult.html language=enus -->
## TOPIC 01330: EndWrite(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-endwrite__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-endwrite__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object). SyntaxNamespace: NationalInstruments.DAQmxpublic void EndWrite(IAsyncResult asyncResult)RemarksIf you call EndWrite(I

### EndWrite(IAsyncResult)

Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as [BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object)](nationalinstruments-daqmx-countermultichannelwriter-beginwritesinglesample__bool-codatafrequency_arr1-asynccallback-object.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void EndWrite(IAsyncResult asyncResult)

#### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](nationalinstruments-daqmx-task-isdone.html) or [WaitUntilDone(TimeSpan)](nationalinstruments-daqmx-task-waituntildone__timespan.html) on the [Task](nationalinstruments-daqmx-task.html) object to determine if a task has generated all of the data that it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling any of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object). |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to one of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| IndexOutOfRangeException | The data provided to one of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object), had a non-zero lower bound. |

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-synchronizecallbacks.html language=enus -->
## TOPIC 01331: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-synchronizecallbacks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how events and callback delegates are invoked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SynchronizeCallbacks { get; set; }RemarksIn some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care w

### SynchronizeCallbacks

Specifies how events and callback delegates are invoked.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-synchronizingobject.html language=enus -->
## TOPIC 01332: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-synchronizingobject.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used Gets or sets the object that marshals event-handler and callback calls. SyntaxNamespace: NationalInstruments.DAQmxpublic ISynchronizeInvoke SynchronizingObject { get; set;

### SynchronizingObject

**Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used** 
Gets or sets the object that marshals event-handler and callback calls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ISynchronizeInvoke SynchronizingObject { get; set; }

#### Remarks

The ISynchronizeInvoke representing the object that marshals the event-handler and callback calls. The default value is null.

null

Note

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-tostring.html language=enus -->
## TOPIC 01333: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codatafrequency_arr1.html language=enus -->
## TOPIC 01334: WriteSingleSample(bool, CODataFrequency[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codatafrequency_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codatafrequency_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single frequency sample to one or more COChannel objects in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency[] data)RemarksNI-DAQmx scales the generated data to the units of the measu

### WriteSingleSample(bool, CODataFrequency[])

Writes a single frequency sample to one or more [COChannel](nationalinstruments-daqmx-cochannel.html) objects in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency[] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataFrequency[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codataticks_arr1.html language=enus -->
## TOPIC 01335: WriteSingleSample(bool, CODataTicks[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codataticks_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codataticks_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single ticks sample to one or more COChannel objects in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks[] data)RemarksNI-DAQmx scales the generated data to the units of the measurement,

### WriteSingleSample(bool, CODataTicks[])

Writes a single ticks sample to one or more [COChannel](nationalinstruments-daqmx-cochannel.html) objects in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks[] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTicks[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codatatime_arr1.html language=enus -->
## TOPIC 01336: WriteSingleSample(bool, CODataTime[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codatatime_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter-writesinglesample__bool-codatatime_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a single time sample to one or more COChannel objects in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime[] data)RemarksNI-DAQmx scales the generated data to the units of the measurement, in

### WriteSingleSample(bool, CODataTime[])

Writes a single time sample to one or more [COChannel](nationalinstruments-daqmx-cochannel.html) objects in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime[] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTime[] | A 1D array of samples to write to the task. Each element of the array corresponds to a channel in the task. The order of the channels in the array corresponds to the order in which you add the channels to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| IndexOutOfRangeException | data has a non-zero lower bound. |

Parent topic:

CounterMultiChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countermultichannelwriter.html language=enus -->
## TOPIC 01337: CounterMultiChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countermultichannelwriter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countermultichannelwriter.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for writing samples to one or more counter output channels in a counter output task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class CounterMultiChannelWriter : MarshalByRefObject, ISynchronizeCa

### CounterMultiChannelWriter Class

Contains methods for writing samples to one or more counter output channels in a counter output task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class CounterMultiChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| CounterMultiChannelWriter(DaqStream) | Initializes a new instance of the CounterMultiChannelWriter class to write to the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginWriteSingleSample(bool, CODataTime[], AsyncCallback, object) | Begins an asynchronous write of a single time sample to one or more COChannel objects in a counter output task. |
| BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object) | Begins an asynchronous write of a single frequency sample to one or more COChannel objects in a counter output task. |
| BeginWriteSingleSample(bool, CODataTicks[], AsyncCallback, object) | Begins an asynchronous write of a single ticks sample to one or more COChannel objects in a counter output task. |
| EndWrite(IAsyncResult) | Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency[], AsyncCallback, object). |
| ToString() | Returns a string representation of the object. |
| WriteSingleSample(bool, CODataFrequency[]) | Writes a single frequency sample to one or more COChannel objects in a counter output task. |
| WriteSingleSample(bool, CODataTime[]) | Writes a single time sample to one or more COChannel objects in a counter output task. |
| WriteSingleSample(bool, CODataTicks[]) | Writes a single ticks sample to one or more COChannel objects in a counter output task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-counteroutputeventargs-counteroutputeventargs.html language=enus -->
## TOPIC 01338: CounterOutputEventArgs()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-counteroutputeventargs-counteroutputeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-counteroutputeventargs-counteroutputeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CounterOutputEventArgs class. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterOutputEventArgs()

### CounterOutputEventArgs()

Initializes a new instance of the [CounterOutputEventArgs](nationalinstruments-daqmx-counteroutputeventargs.html) class.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public CounterOutputEventArgs()

Parent topic:

CounterOutputEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-counteroutputeventargs-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 01339: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-counteroutputeventargs-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-counteroutputeventargs-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxprotected void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.contextStream

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

CounterOutputEventArgs Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-counteroutputeventargs.html language=enus -->
## TOPIC 01340: CounterOutputEventArgs Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-counteroutputeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-counteroutputeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Provides data for the CounterOutput event. Derives fromEventArgsISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class CounterOutputEventArgs : EventArgs, ISerializableRemarksExample applications are located in the <Public Documents>\National Instruments\NI-DAQ\Examples\DotNET4.x direct

### CounterOutputEventArgs Class

Provides data for the [CounterOutput](nationalinstruments-daqmx-task-counteroutput.html) event.

#### Derives from

- EventArgs
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class CounterOutputEventArgs : EventArgs, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| CounterOutputEventArgs() | Initializes a new instance of the CounterOutputEventArgs class. |

#### Methods

| Name | Description |
| --- | --- |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-counteroutputeventhandler__object-counteroutputeventargs.html language=enus -->
## TOPIC 01341: CounterOutputEventHandler Delegate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-counteroutputeventhandler__object-counteroutputeventargs.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-counteroutputeventhandler__object-counteroutputeventargs.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the method that handles the CounterOutput event. SyntaxNamespace: NationalInstrumentspublic delegate void CounterOutputEventHandler(object sender, CounterOutputEventArgs e)ParametersNameTypeDescriptionsenderobjectThe Task that caused this event.eCounterOutputEventArgsA CounterOutputEventA

### CounterOutputEventHandler Delegate

Represents the method that handles the [CounterOutput](nationalinstruments-daqmx-task-counteroutput.html) event.

#### Syntax

**Namespace:**NationalInstruments

public delegate void CounterOutputEventHandler(object sender, CounterOutputEventArgs e)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sender | object | The Task that caused this event. |
| e | CounterOutputEventArgs | A CounterOutputEventArgs that contains the event data. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-counteroutputeventidlestate.html language=enus -->
## TOPIC 01342: CounterOutputEventIdleState Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-counteroutputeventidlestate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-counteroutputeventidlestate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial state of the output terminal of the counter when CounterOutputEventOutputBehavior is Toggle. The terminal enters this state when NI-DAQmx commits the task. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CounterOutputEventIdleStateRemarksSpecifies the initial state of the

### CounterOutputEventIdleState Enumeration

Specifies the initial state of the output terminal of the counter when [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Toggle](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html). The terminal enters this state when NI-DAQmx [commits](/csh?context=nidaqmx_mxcncpts_committedstate) the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CounterOutputEventIdleState

#### Remarks

Specifies the initial state of the output terminal of the counter when [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Toggle](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html). The terminal enters this state when NI-DAQmx [commits](/csh?context=nidaqmx_mxcncpts_committedstate) the task. Use this enumeration to get or set the value of [CounterOutputEventIdleState](nationalinstruments-daqmx-exportsignals-counteroutputeventidlestate.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| High | 10192 | High state. |
| Low | 10214 | Low state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-counteroutputeventoutputbehavior.html language=enus -->
## TOPIC 01343: CounterOutputEventOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-counteroutputeventoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-counteroutputeventoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CounterOutputEventOutputBehaviorRemarksSpecifies whether the exported Counter Output Event pulses or change

### CounterOutputEventOutputBehavior Enumeration

Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CounterOutputEventOutputBehavior

#### Remarks

Specifies whether the exported Counter Output Event pulses or changes from one state to the other when the counter reaches terminal count. Use this enumeration to get or set the value of [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Pulse | 10265 | Send a pulse to the terminal. |
| Toggle | 10307 | Toggle the state of the terminal from low to high or from high to low. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-counteroutputeventpulsepolarity.html language=enus -->
## TOPIC 01344: CounterOutputEventPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-counteroutputeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-counteroutputeventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the pulses at the output terminal of the counter when CounterOutputEventOutputBehavior is Pulse. NI-DAQmx ignores this property if CounterOutputEventOutputBehavior is Toggle. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CounterOutputEventPulsePolarityRemarksSpecifi

### CounterOutputEventPulsePolarity Enumeration

Specifies the polarity of the pulses at the output terminal of the counter when [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html). NI-DAQmx ignores this property if [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Toggle](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CounterOutputEventPulsePolarity

#### Remarks

Specifies the polarity of the pulses at the output terminal of the counter when [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Pulse](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html). NI-DAQmx ignores this property if [CounterOutputEventOutputBehavior](nationalinstruments-daqmx-exportsignals-counteroutputeventoutputbehavior.html) is [Toggle](nationalinstruments-daqmx-counteroutputeventoutputbehavior.html). Use this enumeration to get or set the value of [CounterOutputEventPulsePolarity](nationalinstruments-daqmx-exportsignals-counteroutputeventpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01345: BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(int numberOfSamples, AsyncCallback callback, object state, double[] data, Reallocation

### BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[], ReallocationPolicy)

Begins an asynchronous memory-optimized read of one or more Double samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(int numberOfSamples, AsyncCallback callback, object state, double[] data, ReallocationPolicy policy)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback this is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | double[] | An initialized 1D array of Double samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the data . Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr1.html language=enus -->
## TOPIC 01346: BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(int numberOfSamples, AsyncCallback callback, object state, double[] data)RemarksIf the

### BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[])

Begins an asynchronous memory-optimized read of one or more Double samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleDouble(int numberOfSamples, AsyncCallback callback, object state, double[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | double[] | An initialized 1D array of Double samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01347: BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(int numberOfSamples, AsyncCallback callback, object state, int[] data, ReallocationPolic

### BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[], ReallocationPolicy)

Begins an asynchronous memory-optimized read of one or more Int32 samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(int numberOfSamples, AsyncCallback callback, object state, int[] data, ReallocationPolicy policy)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | int[] | An initialized 1D array of Int32 samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the data . Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr1.html language=enus -->
## TOPIC 01348: BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(int numberOfSamples, AsyncCallback callback, object state, int[] data)RemarksIf the data

### BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[])

Begins an asynchronous memory-optimized read of one or more Int32 samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleInt32(int numberOfSamples, AsyncCallback callback, object state, int[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | int[] | An initialized 1D array of Int32 samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsefrequency__int-asynccallback-object-cidatafrequency_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01349: BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsefrequency__int-asynccallback-object-cidatafrequency_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsefrequency__int-asynccallback-object-cidatafrequency_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseFrequency(int numberOfSamples, AsyncCallback callback, object state, CIDataFreq

### BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[], ReallocationPolicy)

Begins an asynchronous memory-optimized read of one or more [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseFrequency(int numberOfSamples, AsyncCallback callback, object state, CIDataFrequency[] data, ReallocationPolicy policy)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePulseFrequency(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsefrequency__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | CIDataFrequency[] | An initialized 1D array of CIDataFrequency samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the data . Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsefrequency__int-asynccallback-object-cidatafrequency_arr1.html language=enus -->
## TOPIC 01350: BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsefrequency__int-asynccallback-object-cidatafrequency_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsefrequency__int-asynccallback-object-cidatafrequency_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseFrequency(int numberOfSamples, AsyncCallback callback, object state, CIDataFreq

### BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[])

Begins an asynchronous memory-optimized read of one or more [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseFrequency(int numberOfSamples, AsyncCallback callback, object state, CIDataFrequency[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePulseFrequency(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsefrequency__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | CIDataFrequency[] | An initialized 1D array of CIDataFrequency samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulseticks__int-asynccallback-object-cidataticks_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01351: BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulseticks__int-asynccallback-object-cidataticks_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulseticks__int-asynccallback-object-cidataticks_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseTicks(int numberOfSamples, AsyncCallback callback, object state, CIDataTicks[] data

### BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[], ReallocationPolicy)

Begins an asynchronous memory-optimized read of one or more [CIDataTicks](nationalinstruments-daqmx-cidataticks.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseTicks(int numberOfSamples, AsyncCallback callback, object state, CIDataTicks[] data, ReallocationPolicy policy)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePulseTicks(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulseticks__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | CIDataTicks[] | An initialized 1D array of CIDataTicks samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the data . Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulseticks__int-asynccallback-object-cidataticks_arr1.html language=enus -->
## TOPIC 01352: BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulseticks__int-asynccallback-object-cidataticks_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulseticks__int-asynccallback-object-cidataticks_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseTicks(int numberOfSamples, AsyncCallback callback, object state, CIDataTicks[] data

### BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[])

Begins an asynchronous memory-optimized read of one or more [CIDataTicks](nationalinstruments-daqmx-cidataticks.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseTicks(int numberOfSamples, AsyncCallback callback, object state, CIDataTicks[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePulseTicks(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulseticks__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | CIDataTicks[] | An initialized 1D array of CIDataTicks samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsetime__int-asynccallback-object-cidatatime_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01353: BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsetime__int-asynccallback-object-cidatatime_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsetime__int-asynccallback-object-cidatatime_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseTime(int numberOfSamples, AsyncCallback callback, object state, CIDataTime[] data, R

### BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[], ReallocationPolicy)

Begins an asynchronous memory-optimized read of one or more [CIDataTime](nationalinstruments-daqmx-cidatatime.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseTime(int numberOfSamples, AsyncCallback callback, object state, CIDataTime[] data, ReallocationPolicy policy)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePulseTime(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsetime__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | CIDataTime[] | An initialized 1D array of CIDataTime samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the data . Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsetime__int-asynccallback-object-cidatatime_arr1.html language=enus -->
## TOPIC 01354: BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsetime__int-asynccallback-object-cidatatime_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsetime__int-asynccallback-object-cidatatime_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseTime(int numberOfSamples, AsyncCallback callback, object state, CIDataTime[] data)Re

### BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[])

Begins an asynchronous memory-optimized read of one or more [CIDataTime](nationalinstruments-daqmx-cidatatime.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSamplePulseTime(int numberOfSamples, AsyncCallback callback, object state, CIDataTime[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSamplePulseTime(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsetime__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | CIDataTime[] | An initialized 1D array of CIDataTime samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr1-reallocationpolicy.html language=enus -->
## TOPIC 01355: BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[], ReallocationPolicy)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr1-reallocationpolicy.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr1-reallocationpolicy.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(int numberOfSamples, AsyncCallback callback, object state, uint[] data, ReallocationPo

### BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[], ReallocationPolicy)

Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(int numberOfSamples, AsyncCallback callback, object state, uint[] data, ReallocationPolicy policy)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | uint[] | An initialized 1D array of UInt32 samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of the data . Refer to ReallocationPolicy for more information. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr1.html language=enus -->
## TOPIC 01356: BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(int numberOfSamples, AsyncCallback callback, object state, uint[] data)RemarksIf the d

### BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[])

Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginMemoryOptimizedReadMultiSampleUInt32(int numberOfSamples, AsyncCallback callback, object state, uint[] data)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

To get the read data or any exceptions that occurred during an asynchronous read initiated with this method, call [EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int)](nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html) with the returned IAsyncResult.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |
| data | uint[] | An initialized 1D array of UInt32 samples that contains the read data. Each element in the array corresponds to a sample from the channel. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampledouble__int-asynccallback-object.html language=enus -->
## TOPIC 01357: BeginReadMultiSampleDouble(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampledouble__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampledouble__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more Double samples from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSampleDouble(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asyn

### BeginReadMultiSampleDouble(int, AsyncCallback, object)

Begins an asynchronous read of one or more Double samples from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSampleDouble(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSampleDouble(int, AsyncCallback, object), call [EndReadMultiSampleDouble(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampledouble__iasyncresult.html) with the returned IAsyncResult.

Use this method when counter samples are scaled to a floating-point value, such as for frequency and period measurement.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampleint32__int-asynccallback-object.html language=enus -->
## TOPIC 01358: BeginReadMultiSampleInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampleint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampleint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more Int32 samples from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSampleInt32(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asynch

### BeginReadMultiSampleInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more Int32 samples from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSampleInt32(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSampleInt32(int, AsyncCallback, object), call [EndReadMultiSampleInt32(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampleint32__iasyncresult.html) with the returned IAsyncResult.

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulsefrequency__int-asynccallback-object.html language=enus -->
## TOPIC 01359: BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulsefrequency__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulsefrequency__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more pulse samples in terms of frequency from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePulseFrequency(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions

### BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object)

Begins an asynchronous read of one or more pulse samples in terms of frequency from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePulseFrequency(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object), call [EndReadMultiSamplePulseFrequency(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulsefrequency__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulseticks__int-asynccallback-object.html language=enus -->
## TOPIC 01360: BeginReadMultiSamplePulseTicks(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulseticks__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulseticks__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more pulse samples in terms of ticks from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePulseTicks(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that oc

### BeginReadMultiSamplePulseTicks(int, AsyncCallback, object)

Begins an asynchronous read of one or more pulse samples in terms of ticks from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePulseTicks(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePulseTicks(int, AsyncCallback, object), call [EndReadMultiSamplePulseTicks(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulseticks__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulsetime__int-asynccallback-object.html language=enus -->
## TOPIC 01361: BeginReadMultiSamplePulseTime(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulsetime__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulsetime__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more pulse samples in terms of time from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSamplePulseTime(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occu

### BeginReadMultiSamplePulseTime(int, AsyncCallback, object)

Begins an asynchronous read of one or more pulse samples in terms of time from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSamplePulseTime(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSamplePulseTime(int, AsyncCallback, object), call [EndReadMultiSamplePulseTime(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulsetime__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampleuint32__int-asynccallback-object.html language=enus -->
## TOPIC 01362: BeginReadMultiSampleUInt32(int, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampleuint32__int-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampleuint32__int-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of one or more UInt32 samples from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadMultiSampleUInt32(int numberOfSamples, AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asyn

### BeginReadMultiSampleUInt32(int, AsyncCallback, object)

Begins an asynchronous read of one or more UInt32 samples from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadMultiSampleUInt32(int numberOfSamples, AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadMultiSampleUInt32(int, AsyncCallback, object), call [EndReadMultiSampleUInt32(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampleuint32__iasyncresult.html) with the returned IAsyncResult.

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampledouble__asynccallback-object.html language=enus -->
## TOPIC 01363: BeginReadSingleSampleDouble(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampledouble__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampledouble__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a Double sample from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleDouble(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asynchronous read initiated with Be

### BeginReadSingleSampleDouble(AsyncCallback, object)

Begins an asynchronous read of a Double sample from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleDouble(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, object), call [EndReadSingleSampleDouble(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampledouble__iasyncresult.html) with the returned IAsyncResult.

Use this method when counter samples are scaled to a floating-point value, such as for frequency and period measurement.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampleint32__asynccallback-object.html language=enus -->
## TOPIC 01364: BeginReadSingleSampleInt32(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampleint32__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampleint32__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a 32-bit integer sample from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleInt32(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asynchronous read initiated

### BeginReadSingleSampleInt32(AsyncCallback, object)

Begins an asynchronous read of a 32-bit integer sample from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleInt32(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, object), call [EndReadSingleSampleInt32(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampleint32__iasyncresult.html) with the returned IAsyncResult.

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulsefrequency__asynccallback-object.html language=enus -->
## TOPIC 01365: BeginReadSingleSamplePulseFrequency(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulsefrequency__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulsefrequency__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single pulse sample in terms of frequency from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePulseFrequency(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an

### BeginReadSingleSamplePulseFrequency(AsyncCallback, object)

Begins an asynchronous read of a single pulse sample in terms of frequency from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePulseFrequency(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePulseFrequency(AsyncCallback, object), call [EndReadSingleSamplePulseFrequency(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulsefrequency__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulseticks__asynccallback-object.html language=enus -->
## TOPIC 01366: BeginReadSingleSamplePulseTicks(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulseticks__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulseticks__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single pulse sample in terms of ticks from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePulseTicks(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asynchr

### BeginReadSingleSamplePulseTicks(AsyncCallback, object)

Begins an asynchronous read of a single pulse sample in terms of ticks from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePulseTicks(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePulseTicks(AsyncCallback, object), call [EndReadSingleSamplePulseTicks(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulseticks__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulsetime__asynccallback-object.html language=enus -->
## TOPIC 01367: BeginReadSingleSamplePulseTime(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulsetime__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulsetime__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a single pulse sample in terms of time from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSamplePulseTime(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asynchron

### BeginReadSingleSamplePulseTime(AsyncCallback, object)

Begins an asynchronous read of a single pulse sample in terms of time from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSamplePulseTime(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSamplePulseTime(AsyncCallback, object), call [EndReadSingleSamplePulseTime(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulsetime__iasyncresult.html) with the returned IAsyncResult.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampleuint32__asynccallback-object.html language=enus -->
## TOPIC 01368: BeginReadSingleSampleUInt32(AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampleuint32__asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampleuint32__asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous read of a UInt32 sample from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginReadSingleSampleUInt32(AsyncCallback callback, object state)RemarksTo get the read data or any exceptions that occurred during an asynchronous read initiated with Be

### BeginReadSingleSampleUInt32(AsyncCallback, object)

Begins an asynchronous read of a UInt32 sample from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginReadSingleSampleUInt32(AsyncCallback callback, object state)

#### Remarks

To get the read data or any exceptions that occurred during an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, object), call [EndReadSingleSampleUInt32(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampleuint32__iasyncresult.html) with the returned IAsyncResult.

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| callback | AsyncCallback | An optional asynchronous callback that is called when the read is complete. Specify null if you do not want a callback when the read is complete. |
| state | object | A user-provided object that distinguishes this asynchronous read request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-countersinglechannelreader__daqstream.html language=enus -->
## TOPIC 01369: CounterSingleChannelReader(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-countersinglechannelreader__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-countersinglechannelreader__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the CounterSingleChannelReader class to read from the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterSingleChannelReader(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for readers to acce

### CounterSingleChannelReader(DaqStream)

Creates a new instance of the [CounterSingleChannelReader](nationalinstruments-daqmx-countersinglechannelreader.html) class to read from the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public CounterSingleChannelReader(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for readers to access the samples generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to read. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html language=enus -->
## TOPIC 01370: EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampledouble__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult asyncResult, out int a

### EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[])](nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampledouble__int-asynccallback-object-double_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A 1D array of Double samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html language=enus -->
## TOPIC 01371: EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleint32__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult asyncResult, out int actualNum

### EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[])](nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleint32__int-asynccallback-object-int_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A 1D array of Int32 samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsefrequency__iasyncresult-out.html language=enus -->
## TOPIC 01372: EndMemoryOptimizedReadMultiSamplePulseFrequency(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsefrequency__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsefrequency__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataFrequency[] EndMemoryOptimizedReadMultiSamplePulseFrequency(I

### EndMemoryOptimizedReadMultiSamplePulseFrequency(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[])](nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsefrequency__int-asynccallback-object-cidatafrequency_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html)[] EndMemoryOptimizedReadMultiSamplePulseFrequency(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A 1D array of [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html) samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulseticks__iasyncresult-out.html language=enus -->
## TOPIC 01373: EndMemoryOptimizedReadMultiSamplePulseTicks(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulseticks__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulseticks__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTicks[] EndMemoryOptimizedReadMultiSamplePulseTicks(IAsyncResult asyn

### EndMemoryOptimizedReadMultiSamplePulseTicks(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[])](nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulseticks__int-asynccallback-object-cidataticks_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTicks](nationalinstruments-daqmx-cidataticks.html)[] EndMemoryOptimizedReadMultiSamplePulseTicks(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A 1D array of [CIDataTicks](nationalinstruments-daqmx-cidataticks.html) samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsetime__iasyncresult-out.html language=enus -->
## TOPIC 01374: EndMemoryOptimizedReadMultiSamplePulseTime(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsetime__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisamplepulsetime__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTime[] EndMemoryOptimizedReadMultiSamplePulseTime(IAsyncResult asyncRes

### EndMemoryOptimizedReadMultiSamplePulseTime(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[])](nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisamplepulsetime__int-asynccallback-object-cidatatime_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTime](nationalinstruments-daqmx-cidatatime.html)[] EndMemoryOptimizedReadMultiSamplePulseTime(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A 1D array of [CIDataTime](nationalinstruments-daqmx-cidatatime.html) samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html language=enus -->
## TOPIC 01375: EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endmemoryoptimizedreadmultisampleuint32__iasyncresult-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[]) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult asyncResult, out int actua

### EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int)

Handles the end of an asynchronous read initiated with [BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[])](nationalinstruments-daqmx-countersinglechannelreader-beginmemoryoptimizedreadmultisampleuint32__int-asynccallback-object-uint_arr1.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult asyncResult, out int actualNumberOfSamplesRead)

#### Remarks

If you call this method before the asynchronous read is complete, it waits for the read to complete before returning.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[]). |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A 1D array of UInt32 samples that contains the read data. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples; or For asynchronous reads, if asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[]). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampledouble__iasyncresult.html language=enus -->
## TOPIC 01376: EndReadMultiSampleDouble(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampledouble__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampledouble__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] EndReadMultiSampleDouble(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSampleDouble(IAsync

### EndReadMultiSampleDouble(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSampleDouble(int, AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampledouble__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] EndReadMultiSampleDouble(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSampleDouble(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSampleDouble(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSampleDouble(int, AsyncCallback, object). |

#### Returns

A 1D array of Double samples from the task. Each element in the array corresponds to a sample from the channel. NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSampleDouble(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampleint32__iasyncresult.html language=enus -->
## TOPIC 01377: EndReadMultiSampleInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampleint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampleint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] EndReadMultiSampleInt32(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSampleInt32(IAsyncResult

### EndReadMultiSampleInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSampleInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampleint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] EndReadMultiSampleInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSampleInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSampleInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSampleInt32(int, AsyncCallback, object). |

#### Returns

A 1D array of Int32 samples from the task. Each element of the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSampleInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulsefrequency__iasyncresult.html language=enus -->
## TOPIC 01378: EndReadMultiSamplePulseFrequency(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulsefrequency__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulsefrequency__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataFrequency[] EndReadMultiSamplePulseFrequency(IAsyncResult asyncResult)RemarksIf you call EndRea

### EndReadMultiSamplePulseFrequency(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulsefrequency__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html)[] EndReadMultiSamplePulseFrequency(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePulseFrequency(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePulseFrequency(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object). |

#### Returns

A 1D array of pulse samples in terms of frequency from the task. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulseticks__iasyncresult.html language=enus -->
## TOPIC 01379: EndReadMultiSamplePulseTicks(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulseticks__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulseticks__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTicks(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTicks[] EndReadMultiSamplePulseTicks(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSample

### EndReadMultiSamplePulseTicks(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePulseTicks(int, AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulseticks__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTicks](nationalinstruments-daqmx-cidataticks.html)[] EndReadMultiSamplePulseTicks(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePulseTicks(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePulseTicks(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePulseTicks(int, AsyncCallback, object). |

#### Returns

A 1D array of pulse samples in terms of ticks from the task. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePulseTicks(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulsetime__iasyncresult.html language=enus -->
## TOPIC 01380: EndReadMultiSamplePulseTime(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulsetime__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadmultisamplepulsetime__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTime(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTime[] EndReadMultiSamplePulseTime(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSamplePul

### EndReadMultiSamplePulseTime(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSamplePulseTime(int, AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisamplepulsetime__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTime](nationalinstruments-daqmx-cidatatime.html)[] EndReadMultiSamplePulseTime(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSamplePulseTime(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSamplePulseTime(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSamplePulseTime(int, AsyncCallback, object). |

#### Returns

A 1D array of pulse samples in terms of time from the task. Each element in the array corresponds to a sample from the channel.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSamplePulseTime(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampleuint32__iasyncresult.html language=enus -->
## TOPIC 01381: EndReadMultiSampleUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampleuint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadmultisampleuint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(int, AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] EndReadMultiSampleUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadMultiSampleUInt32(IAsyncRe

### EndReadMultiSampleUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadMultiSampleUInt32(int, AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadmultisampleuint32__int-asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] EndReadMultiSampleUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadMultiSampleUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadMultiSampleUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadMultiSampleUInt32(int, AsyncCallback, object). |

#### Returns

A 1D array of UInt32 samples from the task. Each element of the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadMultiSampleUInt32(int, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampledouble__iasyncresult.html language=enus -->
## TOPIC 01382: EndReadSingleSampleDouble(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampledouble__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampledouble__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic double EndReadSingleSampleDouble(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleDouble(IAsyncResu

### EndReadSingleSampleDouble(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleDouble(AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampledouble__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EndReadSingleSampleDouble(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleDouble(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleDouble(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleDouble(AsyncCallback, object). |

#### Returns

A Double sample from the task. NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleDouble(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampleint32__iasyncresult.html language=enus -->
## TOPIC 01383: EndReadSingleSampleInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampleint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampleint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic int EndReadSingleSampleInt32(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleInt32(IAsyncResult) be

### EndReadSingleSampleInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleInt32(AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampleint32__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int EndReadSingleSampleInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleInt32(AsyncCallback, object). |

#### Returns

An Int32 sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleInt32(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulsefrequency__iasyncresult.html language=enus -->
## TOPIC 01384: EndReadSingleSamplePulseFrequency(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulsefrequency__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulsefrequency__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseFrequency(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataFrequency EndReadSingleSamplePulseFrequency(IAsyncResult asyncResult)RemarksIf you call EndReadSing

### EndReadSingleSamplePulseFrequency(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePulseFrequency(AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulsefrequency__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html) EndReadSingleSamplePulseFrequency(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePulseFrequency(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePulseFrequency(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePulseFrequency(AsyncCallback, object). |

#### Returns

A pulse sample in terms of frequency from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePulseFrequency(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulseticks__iasyncresult.html language=enus -->
## TOPIC 01385: EndReadSingleSamplePulseTicks(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulseticks__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulseticks__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTicks(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTicks EndReadSingleSamplePulseTicks(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePuls

### EndReadSingleSamplePulseTicks(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePulseTicks(AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulseticks__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTicks](nationalinstruments-daqmx-cidataticks.html) EndReadSingleSamplePulseTicks(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePulseTicks(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePulseTicks(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePulseTicks(AsyncCallback, object). |

#### Returns

A pulse sample in terms of ticks from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePulseTicks(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulsetime__iasyncresult.html language=enus -->
## TOPIC 01386: EndReadSingleSamplePulseTime(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulsetime__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesamplepulsetime__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTime(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTime EndReadSingleSamplePulseTime(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSamplePulseTi

### EndReadSingleSamplePulseTime(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSamplePulseTime(AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesamplepulsetime__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTime](nationalinstruments-daqmx-cidatatime.html) EndReadSingleSamplePulseTime(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSamplePulseTime(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSamplePulseTime(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSamplePulseTime(AsyncCallback, object). |

#### Returns

A pulse sample in terms of time from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSamplePulseTime(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampleuint32__iasyncresult.html language=enus -->
## TOPIC 01387: EndReadSingleSampleUInt32(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampleuint32__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-endreadsinglesampleuint32__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, object) and retrieves the read samples. SyntaxNamespace: NationalInstruments.DAQmxpublic uint EndReadSingleSampleUInt32(IAsyncResult asyncResult)RemarksIf you call EndReadSingleSampleUInt32(IAsyncResult

### EndReadSingleSampleUInt32(IAsyncResult)

Handles the end of an asynchronous read initiated with [BeginReadSingleSampleUInt32(AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelreader-beginreadsinglesampleuint32__asynccallback-object.html) and retrieves the read samples.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint EndReadSingleSampleUInt32(IAsyncResult asyncResult)

#### Remarks

If you call EndReadSingleSampleUInt32(IAsyncResult) before the asynchronous read represented by the provided IAsyncResult is complete, EndReadSingleSampleUInt32(IAsyncResult) waits for the read to complete before returning.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling BeginReadSingleSampleUInt32(AsyncCallback, object). |

#### Returns

A UInt32 sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to BeginReadSingleSampleUInt32(AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampledouble__int-ref-out.html language=enus -->
## TOPIC 01388: MemoryOptimizedReadMultiSampleDouble(int, ref double[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampledouble__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampledouble__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Double samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] MemoryOptimizedReadMultiSampleDouble(int numberOfSamples, ref double[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to hold the number of

### MemoryOptimizedReadMultiSampleDouble(int, ref double[], out int)

Reads one or more Double samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] MemoryOptimizedReadMultiSampleDouble(int numberOfSamples, ref double[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref double[] | An initialized 1D array of Double samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampledouble__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01389: MemoryOptimizedReadMultiSampleDouble(int, ref double[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampledouble__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampledouble__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Double samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] MemoryOptimizedReadMultiSampleDouble(int numberOfSamples, ref double[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksWhen performing an asynchrono

### MemoryOptimizedReadMultiSampleDouble(int, ref double[], ReallocationPolicy, out int)

Reads one or more Double samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] MemoryOptimizedReadMultiSampleDouble(int numberOfSamples, ref double[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref double[] | An initialized 1D array of Double samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of data . Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleint32__int-ref-out.html language=enus -->
## TOPIC 01390: MemoryOptimizedReadMultiSampleInt32(int, ref int[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleint32__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleint32__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Int32 samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] MemoryOptimizedReadMultiSampleInt32(int numberOfSamples, ref int[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to hold the number of samples

### MemoryOptimizedReadMultiSampleInt32(int, ref int[], out int)

Reads one or more Int32 samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] MemoryOptimizedReadMultiSampleInt32(int numberOfSamples, ref int[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref int[] | An initialized 1D array of Int32 samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleint32__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01391: MemoryOptimizedReadMultiSampleInt32(int, ref int[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleint32__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleint32__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Int32 samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] MemoryOptimizedReadMultiSampleInt32(int numberOfSamples, ref int[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksWhen performing an asynchronous memor

### MemoryOptimizedReadMultiSampleInt32(int, ref int[], ReallocationPolicy, out int)

Reads one or more Int32 samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] MemoryOptimizedReadMultiSampleInt32(int numberOfSamples, ref int[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref int[] | An initialized 1D array of Int32 samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of data . Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsefrequency__int-ref-out.html language=enus -->
## TOPIC 01392: MemoryOptimizedReadMultiSamplePulseFrequency(int, ref CIDataFrequency[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsefrequency__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsefrequency__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more CIDataFrequency samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataFrequency[] MemoryOptimizedReadMultiSamplePulseFrequency(int numberOfSamples, ref CIDataFrequency[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is

### MemoryOptimizedReadMultiSamplePulseFrequency(int, ref CIDataFrequency[], out int)

Reads one or more [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html)[] MemoryOptimizedReadMultiSamplePulseFrequency(int numberOfSamples, ref CIDataFrequency[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref CIDataFrequency[] | An initialized 1D array of CIDataFrequency samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsefrequency__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01393: MemoryOptimizedReadMultiSamplePulseFrequency(int, ref CIDataFrequency[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsefrequency__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsefrequency__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more CIDataFrequency samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataFrequency[] MemoryOptimizedReadMultiSamplePulseFrequency(int numberOfSamples, ref CIDataFrequency[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)R

### MemoryOptimizedReadMultiSamplePulseFrequency(int, ref CIDataFrequency[], ReallocationPolicy, out int)

Reads one or more [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html)[] MemoryOptimizedReadMultiSamplePulseFrequency(int numberOfSamples, ref CIDataFrequency[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref CIDataFrequency[] | An initialized 1D array of CIDataFrequency samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of data . Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulseticks__int-ref-out.html language=enus -->
## TOPIC 01394: MemoryOptimizedReadMultiSamplePulseTicks(int, ref CIDataTicks[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulseticks__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulseticks__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more CIDataTicks samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTicks[] MemoryOptimizedReadMultiSamplePulseTicks(int numberOfSamples, ref CIDataTicks[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to

### MemoryOptimizedReadMultiSamplePulseTicks(int, ref CIDataTicks[], out int)

Reads one or more [CIDataTicks](nationalinstruments-daqmx-cidataticks.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTicks](nationalinstruments-daqmx-cidataticks.html)[] MemoryOptimizedReadMultiSamplePulseTicks(int numberOfSamples, ref CIDataTicks[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref CIDataTicks[] | An initialized 1D array of CIDataTicks samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulseticks__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01395: MemoryOptimizedReadMultiSamplePulseTicks(int, ref CIDataTicks[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulseticks__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulseticks__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more CIDataTicks samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTicks[] MemoryOptimizedReadMultiSamplePulseTicks(int numberOfSamples, ref CIDataTicks[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksWhen perfo

### MemoryOptimizedReadMultiSamplePulseTicks(int, ref CIDataTicks[], ReallocationPolicy, out int)

Reads one or more [CIDataTicks](nationalinstruments-daqmx-cidataticks.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTicks](nationalinstruments-daqmx-cidataticks.html)[] MemoryOptimizedReadMultiSamplePulseTicks(int numberOfSamples, ref CIDataTicks[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref CIDataTicks[] | An initialized 1D array of CIDataTicks samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of data . Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsetime__int-ref-out.html language=enus -->
## TOPIC 01396: MemoryOptimizedReadMultiSamplePulseTime(int, ref CIDataTime[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsetime__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsetime__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more CIDataTime samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTime[] MemoryOptimizedReadMultiSamplePulseTime(int numberOfSamples, ref CIDataTime[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to hol

### MemoryOptimizedReadMultiSamplePulseTime(int, ref CIDataTime[], out int)

Reads one or more [CIDataTime](nationalinstruments-daqmx-cidatatime.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTime](nationalinstruments-daqmx-cidatatime.html)[] MemoryOptimizedReadMultiSamplePulseTime(int numberOfSamples, ref CIDataTime[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref CIDataTime[] | An initialized 1D array of CIDataTime samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsetime__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01397: MemoryOptimizedReadMultiSamplePulseTime(int, ref CIDataTime[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsetime__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisamplepulsetime__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more CIDataTime samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTime[] MemoryOptimizedReadMultiSamplePulseTime(int numberOfSamples, ref CIDataTime[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksWhen performin

### MemoryOptimizedReadMultiSamplePulseTime(int, ref CIDataTime[], ReallocationPolicy, out int)

Reads one or more [CIDataTime](nationalinstruments-daqmx-cidatatime.html) samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTime](nationalinstruments-daqmx-cidatatime.html)[] MemoryOptimizedReadMultiSamplePulseTime(int numberOfSamples, ref CIDataTime[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref CIDataTime[] | An initialized 1D array of CIDataTime samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of data . Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleuint32__int-ref-out.html language=enus -->
## TOPIC 01398: MemoryOptimizedReadMultiSampleUInt32(int, ref uint[], out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleuint32__int-ref-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleuint32__int-ref-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more UInt32 samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] MemoryOptimizedReadMultiSampleUInt32(int numberOfSamples, ref uint[] data, out int actualNumberOfSamplesRead)RemarksIf the data buffer is large enough to hold the number of sam

### MemoryOptimizedReadMultiSampleUInt32(int, ref uint[], out int)

Reads one or more UInt32 samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] MemoryOptimizedReadMultiSampleUInt32(int numberOfSamples, ref uint[] data, out int actualNumberOfSamplesRead)

#### Remarks

If the data buffer is large enough to hold the number of samples requested, this overload attempts to reuse existing memory allocated from the array to acquire data. This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. The memory allocation for the buffer is available to a maximum of 2 GB.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref uint[] | An initialized 1D array of UInt32 samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleuint32__int-ref-reallocationpolicy-out.html language=enus -->
## TOPIC 01399: MemoryOptimizedReadMultiSampleUInt32(int, ref uint[], ReallocationPolicy, out int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleuint32__int-ref-reallocationpolicy-out.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-memoryoptimizedreadmultisampleuint32__int-ref-reallocationpolicy-out.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more UInt32 samples from a single CIChannel in a task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] MemoryOptimizedReadMultiSampleUInt32(int numberOfSamples, ref uint[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)RemarksWhen performing an asynchronous m

### MemoryOptimizedReadMultiSampleUInt32(int, ref uint[], ReallocationPolicy, out int)

Reads one or more UInt32 samples from a single [CIChannel](nationalinstruments-daqmx-cichannel.html) in a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] MemoryOptimizedReadMultiSampleUInt32(int numberOfSamples, ref uint[] data, ReallocationPolicy policy, out int actualNumberOfSamplesRead)

#### Remarks

When performing an asynchronous memory-optimized read, the size of the data buffer dynamically increases if the number of samples read exceeds the existing buffer and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [ToGrow](nationalinstruments-daqmx-reallocationpolicy.html). This results in more efficient memory allocation when performing multiple reads with a continuous counter input task. An ArgumentException is thrown if the buffer is not capable of holding the data and [ReallocationPolicy](nationalinstruments-daqmx-reallocationpolicy.html) is [DoNotReallocate](nationalinstruments-daqmx-reallocationpolicy.html).

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |
| data | ref uint[] | An initialized 1D array of UInt32 samples that contains the read data. Each element in the array corresponds to a sample from the channel. |
| policy | ReallocationPolicy | Dictates the reallocation behavior of data . Refer to ReallocationPolicy for more information. |
| actualNumberOfSamplesRead | out int | The actual number of samples read. This is useful when the reading operation yields fewer or more samples than the actual length of data . |

#### Returns

A reference to the *data*  parameter containing samples from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| ArgumentException | If data is null or is uninitialized; If the first dimension of data does not match the number of channels; or If ReallocationPolicy is not ToGrow, and data is not capable of holding the required number of samples. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readmultisampledouble__int.html language=enus -->
## TOPIC 01400: ReadMultiSampleDouble(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readmultisampledouble__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readmultisampledouble__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Double samples from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] ReadMultiSampleDouble(int numberOfSamples)RemarksUse this method when counter samples are scaled to a floating-point value, such as for frequency and period measurement. NI-DAQmx read and

### ReadMultiSampleDouble(int)

Reads one or more Double samples from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] ReadMultiSampleDouble(int numberOfSamples)

#### Remarks

Use this method when counter samples are scaled to a floating-point value, such as for frequency and period measurement.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of Double samples from the task. Each element in the array corresponds to a sample from the channel. NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readmultisampleint32__int.html language=enus -->
## TOPIC 01401: ReadMultiSampleInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readmultisampleint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readmultisampleint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more Int32 samples from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic int[] ReadMultiSampleInt32(int numberOfSamples)RemarksUse this method when counter samples are returned unscaled, such as for event counting. NI-DAQmx read and write methods time out after the amoun

### ReadMultiSampleInt32(int)

Reads one or more Int32 samples from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int[] ReadMultiSampleInt32(int numberOfSamples)

#### Remarks

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of Int32 samples from the task. Each element of the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulsefrequency__int.html language=enus -->
## TOPIC 01402: ReadMultiSamplePulseFrequency(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulsefrequency__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulsefrequency__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more pulse samples in terms of frequency from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataFrequency[] ReadMultiSamplePulseFrequency(int numberOfSamples)RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout property o

### ReadMultiSamplePulseFrequency(int)

Reads one or more pulse samples in terms of frequency from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html)[] ReadMultiSamplePulseFrequency(int numberOfSamples)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of pulse samples in terms of frequency from the task. Each element of the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulseticks__int.html language=enus -->
## TOPIC 01403: ReadMultiSamplePulseTicks(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulseticks__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulseticks__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more pulse samples in terms of ticks from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTicks[] ReadMultiSamplePulseTicks(int numberOfSamples)RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout property on the task y

### ReadMultiSamplePulseTicks(int)

Reads one or more pulse samples in terms of ticks from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTicks](nationalinstruments-daqmx-cidataticks.html)[] ReadMultiSamplePulseTicks(int numberOfSamples)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of pulse samples in terms of ticks from the task. Each element of the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulsetime__int.html language=enus -->
## TOPIC 01404: ReadMultiSamplePulseTime(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulsetime__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readmultisamplepulsetime__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more pulse samples in terms of time from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTime[] ReadMultiSamplePulseTime(int numberOfSamples)RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout property on the task you

### ReadMultiSamplePulseTime(int)

Reads one or more pulse samples in terms of time from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTime](nationalinstruments-daqmx-cidatatime.html)[] ReadMultiSamplePulseTime(int numberOfSamples)

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of pulse samples in terms of time from the task. Each element of the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readmultisampleuint32__int.html language=enus -->
## TOPIC 01405: ReadMultiSampleUInt32(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readmultisampleuint32__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readmultisampleuint32__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads one or more UInt32 samples from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint[] ReadMultiSampleUInt32(int numberOfSamples)RemarksUse this method when counter samples are returned unscaled, such as for event counting. NI-DAQmx read and write methods time out after the am

### ReadMultiSampleUInt32(int)

Reads one or more UInt32 samples from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint[] ReadMultiSampleUInt32(int numberOfSamples)

#### Remarks

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| numberOfSamples | int | The number of samples to read. If you set numberOfSamples to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set numberOfSamples to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A 1D array of UInt32 samples from the task. Each element of the array corresponds to a sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readsinglesampledouble.html language=enus -->
## TOPIC 01406: ReadSingleSampleDouble()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readsinglesampledouble.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readsinglesampledouble.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a single Double sample from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic double ReadSingleSampleDouble()RemarksUse this method when counter samples are scaled to a floating-point value, such as for frequency and period measurement. NI-DAQmx read and write methods time out a

### ReadSingleSampleDouble()

Reads a single Double sample from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ReadSingleSampleDouble()

#### Remarks

Use this method when counter samples are scaled to a floating-point value, such as for frequency and period measurement.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A Double sample from the task. NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readsinglesampleint32.html language=enus -->
## TOPIC 01407: ReadSingleSampleInt32()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readsinglesampleint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readsinglesampleint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a Int32 sample from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic int ReadSingleSampleInt32()RemarksUse this method when counter samples are returned unscaled, such as for event counting. NI-DAQmx read and write methods time out after the amount of time specified by the Time

### ReadSingleSampleInt32()

Reads a Int32 sample from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int ReadSingleSampleInt32()

#### Remarks

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

An Int32 sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulsefrequency.html language=enus -->
## TOPIC 01408: ReadSingleSamplePulseFrequency()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulsefrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulsefrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a pulse sample in terms of frequency from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataFrequency ReadSingleSamplePulseFrequency()RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout property on the task you are reading from

### ReadSingleSamplePulseFrequency()

Reads a pulse sample in terms of frequency from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataFrequency](nationalinstruments-daqmx-cidatafrequency.html) ReadSingleSamplePulseFrequency()

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A pulse sample in terms of frequency from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulseticks.html language=enus -->
## TOPIC 01409: ReadSingleSamplePulseTicks()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulseticks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulseticks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a pulse sample in terms of ticks from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTicks ReadSingleSamplePulseTicks()RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout property on the task you are reading from or writing

### ReadSingleSamplePulseTicks()

Reads a pulse sample in terms of ticks from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTicks](nationalinstruments-daqmx-cidataticks.html) ReadSingleSamplePulseTicks()

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A pulse sample in terms of ticks from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulsetime.html language=enus -->
## TOPIC 01410: ReadSingleSamplePulseTime()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulsetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readsinglesamplepulsetime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a pulse sample in terms of time from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTime ReadSingleSamplePulseTime()RemarksNI-DAQmx read and write methods time out after the amount of time specified by the Timeout property on the task you are reading from or writing to.

### ReadSingleSamplePulseTime()

Reads a pulse sample in terms of time from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTime](nationalinstruments-daqmx-cidatatime.html) ReadSingleSamplePulseTime()

#### Remarks

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

A pulse sample in terms of time from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-readsinglesampleuint32.html language=enus -->
## TOPIC 01411: ReadSingleSampleUInt32()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-readsinglesampleuint32.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-readsinglesampleuint32.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads an UInt32 sample from a counter task. SyntaxNamespace: NationalInstruments.DAQmxpublic uint ReadSingleSampleUInt32()RemarksUse this method when counter samples are returned unscaled, such as for event counting. NI-DAQmx read and write methods time out after the amount of time specified by the

### ReadSingleSampleUInt32()

Reads an UInt32 sample from a counter task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public uint ReadSingleSampleUInt32()

#### Remarks

Use this method when counter samples are returned unscaled, such as for event counting.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Returns

An UInt32 sample from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-synchronizecallbacks.html language=enus -->
## TOPIC 01412: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-synchronizecallbacks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how events and callback delegates are invoked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SynchronizeCallbacks { get; set; }RemarksIn some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care w

### SynchronizeCallbacks

Specifies how events and callback delegates are invoked.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-synchronizingobject.html language=enus -->
## TOPIC 01413: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-synchronizingobject.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will error if used Gets or sets the object that marshals event-handler and callback calls. SyntaxNamespace: NationalInstruments.DAQmxpublic ISynchronizeInvoke SynchronizingObject { get; set

### SynchronizingObject

**Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will error if used** 
Gets or sets the object that marshals event-handler and callback calls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ISynchronizeInvoke SynchronizingObject { get; set; }

#### Remarks

The ISynchronizeInvoke representing the object that marshals the event-handler and callback calls. The default value is null.

null

Note

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader-tostring.html language=enus -->
## TOPIC 01414: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelReader Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelreader.html language=enus -->
## TOPIC 01415: CounterSingleChannelReader Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelreader.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelreader.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for reading samples from the counter input channel in a task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class CounterSingleChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynch

### CounterSingleChannelReader Class

Contains methods for reading samples from the counter input channel in a task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class CounterSingleChannelReader : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| CounterSingleChannelReader(DaqStream) | Creates a new instance of the CounterSingleChannelReader class to read from the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will error if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[]) | Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[], ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more Double samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[]) | Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[], ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more Int32 samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[]) | Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[], ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataFrequency samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[], ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[]) | Begins an asynchronous memory-optimized read of one or more CIDataTicks samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[], ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[]) | Begins an asynchronous memory-optimized read of one or more CIDataTime samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[]) | Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. |
| BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[], ReallocationPolicy) | Begins an asynchronous memory-optimized read of one or more UInt32 samples from a single CIChannel in a task. |
| BeginReadMultiSampleDouble(int, AsyncCallback, object) | Begins an asynchronous read of one or more Double samples from a counter task. |
| BeginReadMultiSampleInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more Int32 samples from a counter task. |
| BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object) | Begins an asynchronous read of one or more pulse samples in terms of frequency from a counter task. |
| BeginReadMultiSamplePulseTicks(int, AsyncCallback, object) | Begins an asynchronous read of one or more pulse samples in terms of ticks from a counter task. |
| BeginReadMultiSamplePulseTime(int, AsyncCallback, object) | Begins an asynchronous read of one or more pulse samples in terms of time from a counter task. |
| BeginReadMultiSampleUInt32(int, AsyncCallback, object) | Begins an asynchronous read of one or more UInt32 samples from a counter task. |
| BeginReadSingleSampleDouble(AsyncCallback, object) | Begins an asynchronous read of a Double sample from a counter task. |
| BeginReadSingleSampleInt32(AsyncCallback, object) | Begins an asynchronous read of a 32-bit integer sample from a counter task. |
| BeginReadSingleSamplePulseFrequency(AsyncCallback, object) | Begins an asynchronous read of a single pulse sample in terms of frequency from a counter task. |
| BeginReadSingleSamplePulseTicks(AsyncCallback, object) | Begins an asynchronous read of a single pulse sample in terms of ticks from a counter task. |
| BeginReadSingleSamplePulseTime(AsyncCallback, object) | Begins an asynchronous read of a single pulse sample in terms of time from a counter task. |
| BeginReadSingleSampleUInt32(AsyncCallback, object) | Begins an asynchronous read of a UInt32 sample from a counter task. |
| EndMemoryOptimizedReadMultiSampleDouble(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleDouble(int, AsyncCallback, object, double[]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSampleInt32(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleInt32(int, AsyncCallback, object, int[]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePulseFrequency(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseFrequency(int, AsyncCallback, object, CIDataFrequency[]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePulseTicks(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTicks(int, AsyncCallback, object, CIDataTicks[]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSamplePulseTime(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSamplePulseTime(int, AsyncCallback, object, CIDataTime[]) and retrieves the read samples. |
| EndMemoryOptimizedReadMultiSampleUInt32(IAsyncResult, out int) | Handles the end of an asynchronous read initiated with BeginMemoryOptimizedReadMultiSampleUInt32(int, AsyncCallback, object, uint[]) and retrieves the read samples. |
| EndReadMultiSampleDouble(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSampleDouble(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSampleInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSampleInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePulseFrequency(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseFrequency(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePulseTicks(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTicks(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSamplePulseTime(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSamplePulseTime(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadMultiSampleUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadMultiSampleUInt32(int, AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSampleDouble(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleDouble(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSampleInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleInt32(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePulseFrequency(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseFrequency(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePulseTicks(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTicks(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSamplePulseTime(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSamplePulseTime(AsyncCallback, object) and retrieves the read samples. |
| EndReadSingleSampleUInt32(IAsyncResult) | Handles the end of an asynchronous read initiated with BeginReadSingleSampleUInt32(AsyncCallback, object) and retrieves the read samples. |
| MemoryOptimizedReadMultiSampleDouble(int, ref double[], out int) | Reads one or more Double samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSampleDouble(int, ref double[], ReallocationPolicy, out int) | Reads one or more Double samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSampleInt32(int, ref int[], ReallocationPolicy, out int) | Reads one or more Int32 samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSampleInt32(int, ref int[], out int) | Reads one or more Int32 samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSamplePulseFrequency(int, ref CIDataFrequency[], ReallocationPolicy, out int) | Reads one or more CIDataFrequency samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSamplePulseFrequency(int, ref CIDataFrequency[], out int) | Reads one or more CIDataFrequency samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSamplePulseTicks(int, ref CIDataTicks[], out int) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSamplePulseTicks(int, ref CIDataTicks[], ReallocationPolicy, out int) | Reads one or more CIDataTicks samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSamplePulseTime(int, ref CIDataTime[], out int) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSamplePulseTime(int, ref CIDataTime[], ReallocationPolicy, out int) | Reads one or more CIDataTime samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSampleUInt32(int, ref uint[], ReallocationPolicy, out int) | Reads one or more UInt32 samples from a single CIChannel in a task. |
| MemoryOptimizedReadMultiSampleUInt32(int, ref uint[], out int) | Reads one or more UInt32 samples from a single CIChannel in a task. |
| ReadMultiSampleDouble(int) | Reads one or more Double samples from a counter task. |
| ReadMultiSampleInt32(int) | Reads one or more Int32 samples from a counter task. |
| ReadMultiSamplePulseFrequency(int) | Reads one or more pulse samples in terms of frequency from a counter task. |
| ReadMultiSamplePulseTicks(int) | Reads one or more pulse samples in terms of ticks from a counter task. |
| ReadMultiSamplePulseTime(int) | Reads one or more pulse samples in terms of time from a counter task. |
| ReadMultiSampleUInt32(int) | Reads one or more UInt32 samples from a counter task. |
| ReadSingleSampleDouble() | Reads a single Double sample from a counter task. |
| ReadSingleSampleInt32() | Reads a Int32 sample from a counter task. |
| ReadSingleSamplePulseFrequency() | Reads a pulse sample in terms of frequency from a counter task. |
| ReadSingleSamplePulseTicks() | Reads a pulse sample in terms of ticks from a counter task. |
| ReadSingleSamplePulseTime() | Reads a pulse sample in terms of time from a counter task. |
| ReadSingleSampleUInt32() | Reads an UInt32 sample from a counter task. |
| ToString() | Returns a string representation of the object. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codatafrequency_arr1-asynccallback-object.html language=enus -->
## TOPIC 01416: BeginWriteMultiSample(bool, CODataFrequency[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codatafrequency_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codatafrequency_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more frequency samples to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency[] data, AsyncCallback callback, object state

### BeginWriteMultiSample(bool, CODataFrequency[], AsyncCallback, object)

Begins an asynchronous write of one or more frequency samples to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataFrequency[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codataticks_arr1-asynccallback-object.html language=enus -->
## TOPIC 01417: BeginWriteMultiSample(bool, CODataTicks[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codataticks_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codataticks_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more ticks samples to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks[] data, AsyncCallback callback, object state)Remarks

### BeginWriteMultiSample(bool, CODataTicks[], AsyncCallback, object)

Begins an asynchronous write of one or more ticks samples to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTicks[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codatatime_arr1-asynccallback-object.html language=enus -->
## TOPIC 01418: BeginWriteMultiSample(bool, CODataTime[], AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codatatime_arr1-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-beginwritemultisample__bool-codatatime_arr1-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of one or more time samples to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime[] data, AsyncCallback callback, object state)RemarksPa

### BeginWriteMultiSample(bool, CODataTime[], AsyncCallback, object)

Begins an asynchronous write of one or more time samples to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime[] data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTime[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codatafrequency-asynccallback-object.html language=enus -->
## TOPIC 01419: BeginWriteSingleSample(bool, CODataFrequency, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codatafrequency-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codatafrequency-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a frequency sample to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency data, AsyncCallback callback, object state)RemarksPass

### BeginWriteSingleSample(bool, CODataFrequency, AsyncCallback, object)

Begins an asynchronous write of a frequency sample to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataFrequency | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codataticks-asynccallback-object.html language=enus -->
## TOPIC 01420: BeginWriteSingleSample(bool, CODataTicks, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codataticks-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codataticks-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a ticks sample to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks data, AsyncCallback callback, object state)RemarksPass the ret

### BeginWriteSingleSample(bool, CODataTicks, AsyncCallback, object)

Begins an asynchronous write of a ticks sample to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTicks | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codatatime-asynccallback-object.html language=enus -->
## TOPIC 01421: BeginWriteSingleSample(bool, CODataTime, AsyncCallback, object)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codatatime-asynccallback-object.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codatatime-asynccallback-object.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous write of a time sample to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime data, AsyncCallback callback, object state)RemarksPass the retur

### BeginWriteSingleSample(bool, CODataTime, AsyncCallback, object)

Begins an asynchronous write of a time sample to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public IAsyncResult BeginWriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime data, AsyncCallback callback, object state)

#### Remarks

Pass the returned IAsyncResult to [EndWrite(IAsyncResult)](nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html) to get any exceptions that occurred during the asynchronous write or to wait for the write to complete.

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTime | A sample to write to the task. |
| callback | AsyncCallback | An optional asynchronous callback that is called when the write is complete. Specify null if you do not want a callback when the write is complete. |
| state | object | A user-provided object that distinguishes this asynchronous write request from other requests. Use this parameter to provide information to the callback. Specify null if you do not need to pass any additional information to the callback. |

#### Returns

An IAsyncResult that represents the asynchronous call.

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-countersinglechannelwriter__daqstream.html language=enus -->
## TOPIC 01422: CounterSingleChannelWriter(DaqStream)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-countersinglechannelwriter__daqstream.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-countersinglechannelwriter__daqstream.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CounterSingleChannelWriter class to write to the specified DaqStream. SyntaxNamespace: NationalInstruments.DAQmxpublic CounterSingleChannelWriter(DaqStream stream)RemarksEach Task object contains a Stream property that serves as the connection point for the writer c

### CounterSingleChannelWriter(DaqStream)

Initializes a new instance of the [CounterSingleChannelWriter](nationalinstruments-daqmx-countersinglechannelwriter.html) class to write to the specified [DaqStream](nationalinstruments-daqmx-daqstream.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public CounterSingleChannelWriter(DaqStream stream)

#### Remarks

Each [Task](nationalinstruments-daqmx-task.html) object contains a [Stream](nationalinstruments-daqmx-task-stream.html) property that serves as the connection point for the writer classes to provide samples to be generated by that task.

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| stream | DaqStream | The DaqStream to write to. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html language=enus -->
## TOPIC 01423: EndWrite(IAsyncResult)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-endwrite__iasyncresult.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency, AsyncCallback, object). SyntaxNamespace: NationalInstruments.DAQmxpublic void EndWrite(IAsyncResult asyncResult)RemarksIf you call EndWrite(IAs

### EndWrite(IAsyncResult)

Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as [BeginWriteSingleSample(bool, CODataFrequency, AsyncCallback, object)](nationalinstruments-daqmx-countersinglechannelwriter-beginwritesinglesample__bool-codatafrequency-asynccallback-object.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void EndWrite(IAsyncResult asyncResult)

#### Remarks

If you call EndWrite(IAsyncResult) before the asynchronous write represented by the provided IAsyncResult is complete, EndWrite(IAsyncResult) waits for the write to complete before returning. For a write to a buffered task, the write is considered complete when all of the written samples have been transferred to the task buffer. Use [IsDone](nationalinstruments-daqmx-task-isdone.html) or [WaitUntilDone(TimeSpan)](nationalinstruments-daqmx-task-waituntildone__timespan.html) on the [Task](nationalinstruments-daqmx-task.html) object to determine if a task has generated all of the data that it was configured to generate.

NI-DAQmx scales the returned data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

Note

Refer to [Asynchronous Reads and Writes](https://#) for additional information.

Asynchronous Reads and Writes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| asyncResult | IAsyncResult | An IAsyncResult that represents an asynchronous call started by calling any of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency, AsyncCallback, object). |

#### Exceptions

| Type | Description |
| --- | --- |
| ArgumentException | asyncResult is null or is not an instance of IAsyncResult returned from a call to one of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency, AsyncCallback, object). |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error during the asynchronous operation. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-synchronizecallbacks.html language=enus -->
## TOPIC 01424: SynchronizeCallbacks

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-synchronizecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-synchronizecallbacks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how events and callback delegates are invoked. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SynchronizeCallbacks { get; set; }RemarksIn some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care w

### SynchronizeCallbacks

Specifies how events and callback delegates are invoked.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SynchronizeCallbacks { get; set; }

#### Remarks

In some cases, callbacks and event handlers are executed in a different thread than the rest of the program. Therefore, you must take special care when accessing objects that have thread affinity, such as UI controls, from these callbacks and event handlers. For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

Reading and Writing with NI-DAQmx Streams

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-synchronizingobject.html language=enus -->
## TOPIC 01425: SynchronizingObject

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-synchronizingobject.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-synchronizingobject.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used Gets or sets the object that marshals event-handler and callback calls. SyntaxNamespace: NationalInstruments.DAQmxpublic ISynchronizeInvoke SynchronizingObject { get; set;

### SynchronizingObject

**Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if used** 
Gets or sets the object that marshals event-handler and callback calls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public ISynchronizeInvoke SynchronizingObject { get; set; }

#### Remarks

The ISynchronizeInvoke representing the object that marshals the event-handler and callback calls. The default value is null.

null

Note

For more information, refer to Events, Callbacks, and Thread Safety in Measurement Studio .NET Class Libraries.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-tostring.html language=enus -->
## TOPIC 01426: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codatafrequency_arr1.html language=enus -->
## TOPIC 01427: WriteMultiSample(bool, CODataFrequency[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codatafrequency_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codatafrequency_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more frequency samples to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency[] data)RemarksNI-DAQmx scales the generated data to the units of the measurement,

### WriteMultiSample(bool, CODataFrequency[])

Writes one or more frequency samples to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency[] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataFrequency[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codataticks_arr1.html language=enus -->
## TOPIC 01428: WriteMultiSample(bool, CODataTicks[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codataticks_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codataticks_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more ticks samples to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks[] data)RemarksNI-DAQmx scales the generated data to the units of the measurement, includin

### WriteMultiSample(bool, CODataTicks[])

Writes one or more ticks samples to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks[] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTicks[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codatatime_arr1.html language=enus -->
## TOPIC 01429: WriteMultiSample(bool, CODataTime[])

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codatatime_arr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-writemultisample__bool-codatatime_arr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes one or more time samples to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime[] data)RemarksNI-DAQmx scales the generated data to the units of the measurement, including

### WriteMultiSample(bool, CODataTime[])

Writes one or more time samples to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteMultiSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime[] data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTime[] | A 1D array of samples to write to the task. Each element of the array corresponds to a sample to write to the channel. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codatafrequency.html language=enus -->
## TOPIC 01430: WriteSingleSample(bool, CODataFrequency)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codatafrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codatafrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a frequency sample to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency data)RemarksNI-DAQmx scales the generated data to the units of the measurement, including an

### WriteSingleSample(bool, CODataFrequency)

Writes a frequency sample to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataFrequency data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataFrequency | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codataticks.html language=enus -->
## TOPIC 01431: WriteSingleSample(bool, CODataTicks)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codataticks.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codataticks.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a ticks sample to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks data)RemarksNI-DAQmx scales the generated data to the units of the measurement, including any custom

### WriteSingleSample(bool, CODataTicks)

Writes a ticks sample to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTicks data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTicks | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codatatime.html language=enus -->
## TOPIC 01432: WriteSingleSample(bool, CODataTime)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codatatime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter-writesinglesample__bool-codatatime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a time sample to a single COChannel in a counter output task. SyntaxNamespace: NationalInstruments.DAQmxpublic void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime data)RemarksNI-DAQmx scales the generated data to the units of the measurement, including any custom s

### WriteSingleSample(bool, CODataTime)

Writes a time sample to a single [COChannel](nationalinstruments-daqmx-cochannel.html) in a counter output task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void WriteSingleSample([MarshalAs(UnmanagedType.U1)] bool autoStart, CODataTime data)

#### Remarks

NI-DAQmx scales the generated data to the units of the measurement, including any custom scaling you apply to the channel. You specify these units with the create channel methods or the [DAQ Assistant](/csh?context=nidaqmx_taskconfig_daq_config_asst_help).

NI-DAQmx read and write methods time out after the amount of time specified by the [Timeout](nationalinstruments-daqmx-daqstream-timeout.html) property on the task you are reading from or writing to.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| autoStart | bool | If set to true this method automatically calls Start if you do not explicitly call it. You cannot set this parameter to true if you have installed events on the task. |
| data | CODataTime | A sample to write to the task. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CounterSingleChannelWriter Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-countersinglechannelwriter.html language=enus -->
## TOPIC 01433: CounterSingleChannelWriter Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-countersinglechannelwriter.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-countersinglechannelwriter.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains methods for writing samples to a single counter output channel in a counter output task. Derives fromMarshalByRefObjectISynchronizeCallbacksISupportSynchronizationContextSyntaxNamespace: NationalInstruments.DAQmxpublic class CounterSingleChannelWriter : MarshalByRefObject, ISynchronizeCallb

### CounterSingleChannelWriter Class

Contains methods for writing samples to a single counter output channel in a counter output task.

#### Derives from

- MarshalByRefObject
- ISynchronizeCallbacks
- ISupportSynchronizationContext

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class CounterSingleChannelWriter : MarshalByRefObject, ISynchronizeCallbacks, ISupportSynchronizationContext

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| CounterSingleChannelWriter(DaqStream) | Initializes a new instance of the CounterSingleChannelWriter class to write to the specified DaqStream. |

#### Properties

| Name | Description |
| --- | --- |
| SynchronizeCallbacks | Specifies how events and callback delegates are invoked. |
| SynchronizingObject | Obsolete: Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately. Will warn if usedGets or sets the object that marshals event-handler and callback calls. |

#### Methods

| Name | Description |
| --- | --- |
| BeginWriteMultiSample(bool, CODataTime[], AsyncCallback, object) | Begins an asynchronous write of one or more time samples to a single COChannel in a counter output task. |
| BeginWriteMultiSample(bool, CODataFrequency[], AsyncCallback, object) | Begins an asynchronous write of one or more frequency samples to a single COChannel in a counter output task. |
| BeginWriteMultiSample(bool, CODataTicks[], AsyncCallback, object) | Begins an asynchronous write of one or more ticks samples to a single COChannel in a counter output task. |
| BeginWriteSingleSample(bool, CODataTime, AsyncCallback, object) | Begins an asynchronous write of a time sample to a single COChannel in a counter output task. |
| BeginWriteSingleSample(bool, CODataFrequency, AsyncCallback, object) | Begins an asynchronous write of a frequency sample to a single COChannel in a counter output task. |
| BeginWriteSingleSample(bool, CODataTicks, AsyncCallback, object) | Begins an asynchronous write of a ticks sample to a single COChannel in a counter output task. |
| EndWrite(IAsyncResult) | Handles the end of an asynchronous write initiated with any of the counter asynchronous write methods, such as BeginWriteSingleSample(bool, CODataFrequency, AsyncCallback, object). |
| ToString() | Returns a string representation of the object. |
| WriteMultiSample(bool, CODataFrequency[]) | Writes one or more frequency samples to a single COChannel in a counter output task. |
| WriteMultiSample(bool, CODataTime[]) | Writes one or more time samples to a single COChannel in a counter output task. |
| WriteMultiSample(bool, CODataTicks[]) | Writes one or more ticks samples to a single COChannel in a counter output task. |
| WriteSingleSample(bool, CODataFrequency) | Writes a frequency sample to a single COChannel in a counter output task. |
| WriteSingleSample(bool, CODataTime) | Writes a time sample to a single COChannel in a counter output task. |
| WriteSingleSample(bool, CODataTicks) | Writes a ticks sample to a single COChannel in a counter output task. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-couplingtypes.html language=enus -->
## TOPIC 01434: CouplingTypes Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-couplingtypes.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-couplingtypes.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a set of coupling types a device may support. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CouplingTypesRemarksSpecifies a set of coupling types a device may support.MembersNameValueDescriptionNone0x0No coupling types supported by the device. AC0x1Remove the DC offset from the sig

### CouplingTypes Enumeration

Specifies a set of coupling types a device may support.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CouplingTypes

#### Remarks

Specifies a set of coupling types a device may support.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0x0 | No coupling types supported by the device. |
| AC | 0x1 | Remove the DC offset from the signal. |
| DC | 0x2 | Allow NI-DAQmx to measure all of the signal. |
| Ground | 0x4 | Remove the signal from the measurement and measure only ground. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqbuffer-inputbuffersize.html language=enus -->
## TOPIC 01435: InputBufferSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqbuffer-inputbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqbuffer-inputbuffersize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples the input buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic input buffer allocation that NI-DAQmx perfo

### InputBufferSize

Specifies the number of samples the input buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the [automatic input buffer allocation](/csh?context=nidaqmx_mxcncpts_buffersize) that NI-DAQmx performs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long InputBufferSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqBuffer Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqbuffer-inputonboardbuffersize.html language=enus -->
## TOPIC 01436: InputOnBoardBufferSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqbuffer-inputonboardbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqbuffer-inputonboardbuffersize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in samples per channel the size of the onboard input buffer of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long InputOnBoardBufferSize { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### InputOnBoardBufferSize

Indicates in samples per channel the size of the onboard input buffer of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long InputOnBoardBufferSize { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqBuffer Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqbuffer-outputbuffersize.html language=enus -->
## TOPIC 01437: OutputBufferSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqbuffer-outputbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqbuffer-outputbuffersize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples the output buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic output buffer allocation that NI-DAQmx per

### OutputBufferSize

Specifies the number of samples the output buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the [automatic output buffer allocation](/csh?context=nidaqmx_mxcncpts_buffersize) that NI-DAQmx performs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long OutputBufferSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqBuffer Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqbuffer-outputonboardbuffersize.html language=enus -->
## TOPIC 01438: OutputOnBoardBufferSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqbuffer-outputonboardbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqbuffer-outputonboardbuffersize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in samples per channel the size of the onboard output buffer of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long OutputOnBoardBufferSize { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### OutputOnBoardBufferSize

Specifies in samples per channel the size of the onboard output buffer of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long OutputOnBoardBufferSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqBuffer Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqbuffer-tostring.html language=enus -->
## TOPIC 01439: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqbuffer-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqbuffer-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString. ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ToString()

Returns a string representation of the object.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override string ToString()

#### Remarks

Overrides ToString.

#### Returns

A string representation of the object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqBuffer Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqbuffer.html language=enus -->
## TOPIC 01440: DaqBuffer Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqbuffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqbuffer.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Exposes a buffer on a Task that can be used to read or write samples to or from an NI-DAQmx task. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class DaqBuffer : MarshalByRefObject, IFilteredTypeDescriptorRemarksExample applications are located

### DaqBuffer Class

Exposes a [buffer](/csh?context=nidaqmx_mxcncpts_buffering) on a [Task](nationalinstruments-daqmx-task.html) that can be used to read or write samples to or from an NI-DAQmx task.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DaqBuffer : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| InputBufferSize | Specifies the number of samples the input buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic input buffer allocation that NI-DAQmx performs. |
| InputOnBoardBufferSize | Indicates in samples per channel the size of the onboard input buffer of the device. |
| OutputBufferSize | Specifies the number of samples the output buffer can hold for each channel in the task. Zero indicates to allocate no buffer. Use a buffer size of 0 to perform a hardware-timed operation without using a buffer. Setting this property overrides the automatic output buffer allocation that NI-DAQmx performs. |
| OutputOnBoardBufferSize | Specifies in samples per channel the size of the onboard output buffer of the device. |

#### Methods

| Name | Description |
| --- | --- |
| ToString() | Returns a string representation of the object. |

#### See Also

- DaqStream
- Buffer

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception-daqexception.html language=enus -->
## TOPIC 01441: DaqException()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception-daqexception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception-daqexception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DaqException class. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqException()RemarksNI-DAQmx Driver Error Codes

### DaqException()

Initializes a new instance of the [DaqException](nationalinstruments-daqmx-daqexception.html) class.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DaqException()

#### Remarks

NI-DAQmx Driver Error Codes

Parent topic:

DaqException Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception-daqexception__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 01442: DaqException(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception-daqexception__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception-daqexception__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of the DaqException class with serialized data. SyntaxNamespace: NationalInstruments.DAQmxprotected DaqException(SerializationInfo info, StreamingContext context)RemarksThis constructor is called during deserialization to reconstitute the exception object transmitted over a st

### DaqException(SerializationInfo, StreamingContext)

Creates a new instance of the [DaqException](nationalinstruments-daqmx-daqexception.html) class with serialized data.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected DaqException(SerializationInfo info, StreamingContext context)

#### Remarks

This constructor is called during deserialization to reconstitute the exception object transmitted over a stream. For more information, refer to XML and SOAP Serialization in the Microsoft .NET Framework documentation.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | The object that holds the serialized object data. |
| context | StreamingContext | The contextual information about the source or destination. |

Parent topic:

DaqException Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception-daqexception__string-exception.html language=enus -->
## TOPIC 01443: DaqException(string, Exception)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception-daqexception__string-exception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception-daqexception__string-exception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DaqException class with the specified error message and a reference to the inner exception that is the cause of the exception. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqException(string message, Exception inner)Remarks NI-DAQmx Driver Error CodesParameters

### DaqException(string, Exception)

Initializes a new instance of the [DaqException](nationalinstruments-daqmx-daqexception.html) class with the specified error message and a reference to the inner exception that is the cause of the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DaqException(string message, Exception inner)

#### Remarks

NI-DAQmx Driver Error Codes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| message | string | The error message that explains the cause of the exception. |
| inner | Exception | The exception that caused this exception. |

Parent topic:

DaqException Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception-daqexception__string-int-exception.html language=enus -->
## TOPIC 01444: DaqException(string, int, Exception)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception-daqexception__string-int-exception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception-daqexception__string-int-exception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DaqException class with the specified error message, NI-DAQmx driver error code, and reference to the inner exception that is the cause of the exception. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqException(string message, int errorCode, Exception inner)Rem

### DaqException(string, int, Exception)

Initializes a new instance of the [DaqException](nationalinstruments-daqmx-daqexception.html) class with the specified error message, NI-DAQmx driver error code, and reference to the inner exception that is the cause of the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DaqException(string message, int errorCode, Exception inner)

#### Remarks

NI-DAQmx Driver Error Codes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| message | string | The error message that explains the cause of the exception. |
| errorCode | int | The NI-DAQmx driver error code that caused this exception to be thrown. Refer to NI-DAQmx Driver Error Codes for a list of possible values. |
| inner | Exception | The exception that caused this exception. |

Parent topic:

DaqException Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception-daqexception__string-int.html language=enus -->
## TOPIC 01445: DaqException(string, int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception-daqexception__string-int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception-daqexception__string-int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DaqException class with the specified error message and NI-DAQmx driver error code. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqException(string message, int errorCode)Remarks NI-DAQmx Driver Error CodesParametersNameTypeDescriptionmessagestringThe error mes

### DaqException(string, int)

Initializes a new instance of the [DaqException](nationalinstruments-daqmx-daqexception.html) class with the specified error message and NI-DAQmx driver error code.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DaqException(string message, int errorCode)

#### Remarks

NI-DAQmx Driver Error Codes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| message | string | The error message that explains the cause of the exception. |
| errorCode | int | The NI-DAQmx driver error code that caused this exception to be thrown. Refer to NI-DAQmx Driver Error Codes for a list of possible values. |

Parent topic:

DaqException Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception-daqexception__string.html language=enus -->
## TOPIC 01446: DaqException(string)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception-daqexception__string.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception-daqexception__string.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the DaqException class with the specified error message. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqException(string message)Remarks NI-DAQmx Driver Error CodesParametersNameTypeDescriptionmessagestringThe error message that explains the cause of the exception.

### DaqException(string)

Initializes a new instance of the [DaqException](nationalinstruments-daqmx-daqexception.html) class with the specified error message.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DaqException(string message)

#### Remarks

NI-DAQmx Driver Error Codes

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| message | string | The error message that explains the cause of the exception. |

Parent topic:

DaqException Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception-error.html language=enus -->
## TOPIC 01447: Error

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception-error.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception-error.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the NI-DAQmx driver code for the error that occurred. SyntaxNamespace: NationalInstruments.DAQmxpublic int Error { get; }RemarksThe NI-DAQmx driver code for the error that occurred.Refer toNI-DAQmx Driver Error Codes for a list of possible values. NI-DAQmx Driver Error Codes

### Error

Gets the NI-DAQmx driver code for the error that occurred.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int Error { get; }

#### Remarks

The NI-DAQmx driver code for the error that occurred.

Refer to

[NI-DAQmx Driver Error Codes](https://#) for a list of possible values.

NI-DAQmx Driver Error Codes

Parent topic:

DaqException Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception-getobjectdata__serializationinfo-streamingcontext.html language=enus -->
## TOPIC 01448: GetObjectData(SerializationInfo, StreamingContext)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception-getobjectdata__serializationinfo-streamingcontext.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception-getobjectdata__serializationinfo-streamingcontext.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SerializationInfo object with information about the exception. SyntaxNamespace: NationalInstruments.DAQmxpublic override void GetObjectData(SerializationInfo info, StreamingContext context)ParametersNameTypeDescriptioninfoSerializationInfoObject that holds the serialized object data.context

### GetObjectData(SerializationInfo, StreamingContext)

Sets the SerializationInfo object with information about the exception.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void GetObjectData(SerializationInfo info, StreamingContext context)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| info | SerializationInfo | Object that holds the serialized object data. |
| context | StreamingContext | Contextual information about the source or destination. |

Parent topic:

DaqException Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqexception.html language=enus -->
## TOPIC 01449: DaqException Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqexception.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqexception.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the exception that is thrown when an NI-DAQmx driver error occurs. Derives fromSystemExceptionISerializableSyntaxNamespace: NationalInstruments.DAQmxpublic class DaqException : SystemException, ISerializableRemarksExample applications are located in the <Public Documents>\National Instrum

### DaqException Class

Represents the exception that is thrown when an NI-DAQmx driver error occurs.

#### Derives from

- SystemException
- ISerializable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class DaqException : SystemException, ISerializable

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

NI-DAQmx Driver Error Codes

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Constructors

| Name | Description |
| --- | --- |
| DaqException(SerializationInfo, StreamingContext) | Creates a new instance of the DaqException class with serialized data. |
| DaqException(string, int) | Initializes a new instance of the DaqException class with the specified error message and NI-DAQmx driver error code. |
| DaqException(string, int, Exception) | Initializes a new instance of the DaqException class with the specified error message, NI-DAQmx driver error code, and reference to the inner exception that is the cause of the exception. |
| DaqException(string, Exception) | Initializes a new instance of the DaqException class with the specified error message and a reference to the inner exception that is the cause of the exception. |
| DaqException() | Initializes a new instance of the DaqException class. |
| DaqException(string) | Initializes a new instance of the DaqException class with the specified error message. |

#### Properties

| Name | Description |
| --- | --- |
| Error | Gets the NI-DAQmx driver code for the error that occurred. |

#### Methods

| Name | Description |
| --- | --- |
| GetObjectData(SerializationInfo, StreamingContext) | Sets the SerializationInfo object with information about the exception. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-accessoryinsertionorremovaldetected.html language=enus -->
## TOPIC 01450: AccessoryInsertionOrRemovalDetected

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-accessoryinsertionorremovaldetected.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-accessoryinsertionorremovaldetected.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if any device(s) in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read DevicesWithInsertedOrRemovedAccessories. Otherwise, you

### AccessoryInsertionOrRemovalDetected

Indicates if any device(s) in the task detected the insertion or removal of an accessory since the task started. Reading this property clears the accessory change status for all channels in the task. You must read this property before you read [DevicesWithInsertedOrRemovedAccessories](nationalinstruments-daqmx-daqstream-deviceswithinsertedorremovedaccessories.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool AccessoryInsertionOrRemovalDetected { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-availablesamplesperchannel.html language=enus -->
## TOPIC 01451: AvailableSamplesPerChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-availablesamplesperchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-availablesamplesperchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of samples available to read per channel. This value is the same for all channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic long AvailableSamplesPerChannel { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an

### AvailableSamplesPerChannel

Indicates the number of samples available to read per channel. This value is the same for all channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AvailableSamplesPerChannel { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-buffer.html language=enus -->
## TOPIC 01452: Buffer

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-buffer.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-buffer.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the buffer for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic DaqBuffer Buffer { get; }RemarksThe DaqBuffer for the task.

### Buffer

Gets the [buffer](/csh?context=nidaqmx_mxcncpts_buffering) for the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DaqBuffer](nationalinstruments-daqmx-daqbuffer.html) Buffer { get; }

#### Remarks

The [DaqBuffer](nationalinstruments-daqmx-daqbuffer.html) for the task.

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-channelstoread.html language=enus -->
## TOPIC 01453: ChannelsToRead

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-channelstoread.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-channelstoread.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a subset of channels in the task from which to read. SyntaxNamespace: NationalInstruments.DAQmxpublic string ChannelsToRead { get; set; }RemarksThe channels to read from.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ChannelsToRead

Sets a subset of channels in the task from which to read.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ChannelsToRead { get; set; }

#### Remarks

The channels to read from.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-commonmoderangeerrorchannels.html language=enus -->
## TOPIC 01454: CommonModeRangeErrorChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-commonmoderangeerrorchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-commonmoderangeerrorchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read CommonModeRangeErrorChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[]

### CommonModeRangeErrorChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any virtual channels in the task for which the device(s) detected a common mode range violation. You must read [CommonModeRangeErrorChannelsExist](nationalinstruments-daqmx-daqstream-commonmoderangeerrorchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] CommonModeRangeErrorChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-commonmoderangeerrorchannelsexist.html language=enus -->
## TOPIC 01455: CommonModeRangeErrorChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-commonmoderangeerrorchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-commonmoderangeerrorchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected a common mode range violation for any virtual channel in the task. Common mode range violation occurs when the voltage of either the positive terminal or negative terminal to ground are out of range. Reading this property clears the common mode range violation sta

### CommonModeRangeErrorChannelsExist

Indicates if the device(s) detected a common mode range violation for any virtual channel in the task. Common mode range violation occurs when the voltage of either the positive terminal or negative terminal to ground are out of range. Reading this property clears the common mode range violation status for all channels in the task. You must read this property before you read [CommonModeRangeErrorChannels](nationalinstruments-daqmx-daqstream-commonmoderangeerrorchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CommonModeRangeErrorChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-configureinputbuffer__long.html language=enus -->
## TOPIC 01456: ConfigureInputBuffer(long)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-configureinputbuffer__long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-configureinputbuffer__long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overrides the automatic input buffer allocation that NI-DAQmx performs. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureInputBuffer(long bufferSize)RemarksSet bufferSize to 0 to perform a hardware-timed operation without using a buffer.The NI-DAQmx driver does not determine if the req

### ConfigureInputBuffer(long)

Overrides the automatic input [buffer](/csh?context=nidaqmx_mxcncpts_buffering) allocation that NI-DAQmx performs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureInputBuffer(long bufferSize)

#### Remarks

Set *bufferSize*  to 0 to perform a hardware-timed operation without using a buffer.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureInputBuffer(long) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| bufferSize | long | The number of samples the buffer can hold for each channel in the task. Zero indicates that no buffer is allocated. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-configureoutputbuffer__long.html language=enus -->
## TOPIC 01457: ConfigureOutputBuffer(long)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-configureoutputbuffer__long.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-configureoutputbuffer__long.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overrides the automatic output buffer allocation that NI-DAQmx performs. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureOutputBuffer(long bufferSize)RemarksSet bufferSize to 0 to perform a hardware-timed operation without using a buffer.The NI-DAQmx driver does not determine if the r

### ConfigureOutputBuffer(long)

Overrides the automatic output [buffer](/csh?context=nidaqmx_mxcncpts_buffering) allocation that NI-DAQmx performs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureOutputBuffer(long bufferSize)

#### Remarks

Set *bufferSize*  to 0 to perform a hardware-timed operation without using a buffer.

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureOutputBuffer(long) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| bufferSize | long | The number of samples the buffer can hold for each channel in the task. Zero indicates that no buffer is allocated. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-currentreadposition.html language=enus -->
## TOPIC 01458: CurrentReadPosition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-currentreadposition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-currentreadposition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in samples per channel the current position in the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic long CurrentReadPosition { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CurrentReadPosition

Indicates in samples per channel the current position in the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CurrentReadPosition { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-currentwriteposition.html language=enus -->
## TOPIC 01459: CurrentWritePosition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-currentwriteposition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-currentwriteposition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic long CurrentWritePosition { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an

### CurrentWritePosition

Indicates the position in the buffer of the next sample to generate. This value is identical for all channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CurrentWritePosition { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-deviceswithinsertedorremovedaccessories.html language=enus -->
## TOPIC 01460: DevicesWithInsertedOrRemovedAccessories

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-deviceswithinsertedorremovedaccessories.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-deviceswithinsertedorremovedaccessories.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read AccessoryInsertionOrRemovalDetected before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] DevicesWi

### DevicesWithInsertedOrRemovedAccessories

Indicates the names of any devices that detected the insertion or removal of an accessory since the task started. You must read [AccessoryInsertionOrRemovalDetected](nationalinstruments-daqmx-daqstream-accessoryinsertionorremovaldetected.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] DevicesWithInsertedOrRemovedAccessories { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-digitallinesperinputchannel.html language=enus -->
## TOPIC 01461: DigitalLinesPerInputChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-digitallinesperinputchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-digitallinesperinputchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of lines per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra lines are false. SyntaxNamespace: NationalInstruments.DAQmxpublic long DigitalLinesPerInputChannel { get; }ExceptionsTypeDescriptionNationalInstr

### DigitalLinesPerInputChannel

Indicates the number of lines per channel that NI-DAQmx returns in a sample for line-based reads. If a channel has fewer lines than this number, the extra lines are false.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DigitalLinesPerInputChannel { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-digitallinesperoutputchannel.html language=enus -->
## TOPIC 01462: DigitalLinesPerOutputChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-digitallinesperoutputchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-digitallinesperoutputchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of Boolean values expected per channel in a sample for line-based writes. This property is determined by the channel in the task with the most digital lines. If a channel has fewer lines than this number, NI-DAQmx ignores the extra Boolean values. SyntaxNamespace: NationalInstru

### DigitalLinesPerOutputChannel

Indicates the number of Boolean values expected per channel in a sample for line-based writes. This property is determined by the channel in the task with the most digital lines. If a channel has fewer lines than this number, NI-DAQmx ignores the extra Boolean values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DigitalLinesPerOutputChannel { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-loggingfilepath.html language=enus -->
## TOPIC 01463: LoggingFilePath

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-loggingfilepath.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-loggingfilepath.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the path to the TDMS file to which you want to log data. If the file path is changed while the task is running, this takes effect on the next sample interval (if Logging.SampsPerFile has been set) or when DAQmx Start New File is called. New file paths can be specified by ending with "\" or

### LoggingFilePath

Specifies the path to the TDMS file to which you want to [log](/csh?context=nidaqmx_mxcncpts_datalogging) data. If the file path is changed while the task is running, this takes effect on the next sample interval (if Logging.SampsPerFile has been set) or when [DAQmx](nationalinstruments-daqmx.html) Start New File is called. New file paths can be specified by ending with "\" or "/". Files created after specifying a new file path retain the same name and numbering sequence.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string LoggingFilePath { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-loggingfilepreallocationsize.html language=enus -->
## TOPIC 01464: LoggingFilePreallocationSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-loggingfilepreallocationsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-loggingfilepreallocationsize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a size in samples to be used to pre-allocate space on disk. Pre-allocation can improve file I/O performance, especially in situations where multiple files are being written to disk. For finite tasks, the default behavior is to pre-allocate the file based on the number of samples you config

### LoggingFilePreallocationSize

Specifies a size in samples to be used to pre-allocate space on disk. Pre-allocation can improve file I/O performance, especially in situations where multiple files are being written to disk. For finite tasks, the default behavior is to pre-allocate the file based on the number of samples you configure the task to acquire.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long LoggingFilePreallocationSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-loggingfilewritesize.html language=enus -->
## TOPIC 01465: LoggingFileWriteSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-loggingfilewritesize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-loggingfilewritesize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes. SyntaxNamespace: NationalInstruments.DAQmxpublic long LoggingFileWriteSize { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### LoggingFileWriteSize

Specifies the size, in samples, in which data will be written to disk. The size must be evenly divisible by the volume sector size, in bytes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long LoggingFileWriteSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-loggingmode.html language=enus -->
## TOPIC 01466: LoggingMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-loggingmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-loggingmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable logging and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode. SyntaxNamespace: NationalInstruments

### LoggingMode

Specifies whether to enable [logging](/csh?context=nidaqmx_mxcncpts_datalogging) and whether to allow reading data while logging. Log mode allows for the best performance. However, you cannot read data while logging if you specify this mode. If you want to read data while logging, specify Log and Read mode.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [LoggingMode](nationalinstruments-daqmx-loggingmode.html) LoggingMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-loggingpause.html language=enus -->
## TOPIC 01467: LoggingPause

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-loggingpause.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-loggingpause.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether logging is paused while a task is executing. If LoggingMode is set to Log and Read mode, this value is taken into consideration on the next call to DAQmx Read, where data is written to disk. If LoggingMode is set to Log Only mode, this value is taken into consideration the next tim

### LoggingPause

Specifies whether logging is paused while a task is executing. If [LoggingMode](nationalinstruments-daqmx-daqstream-loggingmode.html) is set to Log and Read mode, this value is taken into consideration on the next call to [DAQmx](nationalinstruments-daqmx.html) Read, where data is written to disk. If [LoggingMode](nationalinstruments-daqmx-daqstream-loggingmode.html) is set to Log Only mode, this value is taken into consideration the next time that data is written to disk. A new TDMS group is written when logging is resumed from a paused state.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool LoggingPause { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-loggingsamplesperfile.html language=enus -->
## TOPIC 01468: LoggingSamplesPerFile

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-loggingsamplesperfile.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-loggingsamplesperfile.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how many samples to write to each file. When the file reaches the number of samples specified, a new file is created with the naming convention of <filename>_####.tdms, where #### starts at 0001 and increments automatically with each new file. For example, if the file specified is C:\data.

### LoggingSamplesPerFile

Specifies how many samples to write to each file. When the file reaches the number of samples specified, a new file is created with the naming convention of <filename>_####.tdms, where #### starts at 0001 and increments automatically with each new file. For example, if the file specified is C:\data.tdms, the next file name used is C:\data_0001.tdms. To disable file spanning behavior, set this attribute to 0. If [LoggingFilePath](nationalinstruments-daqmx-daqstream-loggingfilepath.html) is changed while this attribute is set, the new file path takes effect on the next file created.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long LoggingSamplesPerFile { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-numberofinputchannels.html language=enus -->
## TOPIC 01469: NumberOfInputChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-numberofinputchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-numberofinputchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of channels that reading from the task reads from the task. This value is the number of channels in the task or the number of channels you specify with ChannelsToRead. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfInputChannels { get; }ExceptionsTypeDescriptionNa

### NumberOfInputChannels

Indicates the number of channels that reading from the task reads from the task. This value is the number of channels in the task or the number of channels you specify with [ChannelsToRead](nationalinstruments-daqmx-daqstream-channelstoread.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfInputChannels { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-numberofoutputchannels.html language=enus -->
## TOPIC 01470: NumberOfOutputChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-numberofoutputchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-numberofoutputchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of channels that writing to the task writes to the task. This value is the number of channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberOfOutputChannels { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver retu

### NumberOfOutputChannels

Indicates the number of channels that writing to the task writes to the task. This value is the number of channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberOfOutputChannels { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-openthermocouplechannels.html language=enus -->
## TOPIC 01471: OpenThermocoupleChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-openthermocouplechannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-openthermocouplechannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an open thermcouple. You must read OpenThermocoupleChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] OpenThermocou

### OpenThermocoupleChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any virtual channels in the task for which the device(s) detected an open thermcouple. You must read [OpenThermocoupleChannelsExist](nationalinstruments-daqmx-daqstream-openthermocouplechannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] OpenThermocoupleChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-openthermocouplechannelsexist.html language=enus -->
## TOPIC 01472: OpenThermocoupleChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-openthermocouplechannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-openthermocouplechannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read OpenThermocoupleChannels. Otherwise, you will receive an error. S

### OpenThermocoupleChannelsExist

Indicates if the device(s) detected an open thermocouple connected to any virtual channel in the task. Reading this property clears the open thermocouple status for all channels in the task. You must read this property before you read [OpenThermocoupleChannels](nationalinstruments-daqmx-daqstream-openthermocouplechannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool OpenThermocoupleChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-outputbufferspaceavailable.html language=enus -->
## TOPIC 01473: OutputBufferSpaceAvailable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-outputbufferspaceavailable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-outputbufferspaceavailable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in samples per channel the amount of available space in the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic long OutputBufferSpaceAvailable { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### OutputBufferSpaceAvailable

Indicates in samples per channel the amount of available space in the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long OutputBufferSpaceAvailable { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-overloadedinputchannels.html language=enus -->
## TOPIC 01474: OverloadedInputChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-overloadedinputchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-overloadedinputchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any overloaded virtual channels in the task. You must read OverloadedInputChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] OverloadedInputChannels { get; }RemarksThis property ret

### OverloadedInputChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any [overloaded](/csh?context=nidaqmx_mxdevconsid_overloaddetection) virtual channels in the task. You must read [OverloadedInputChannelsExist](nationalinstruments-daqmx-daqstream-overloadedinputchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] OverloadedInputChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-overloadedinputchannelsexist.html language=enus -->
## TOPIC 01475: OverloadedInputChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-overloadedinputchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-overloadedinputchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overload in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read OverloadedInputChannels. Otherwise, you will receive an error. SyntaxNamespace: NationalInstr

### OverloadedInputChannelsExist

Indicates if the device(s) detected an [overload](/csh?context=nidaqmx_mxdevconsid_overloaddetection) in any virtual channel in the task. Reading this property clears the overload status for all channels in the task. You must read this property before you read [OverloadedInputChannels](nationalinstruments-daqmx-daqstream-overloadedinputchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool OverloadedInputChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-phaselockedloopunlockedchannels.html language=enus -->
## TOPIC 01476: PhaseLockedLoopUnlockedChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-phaselockedloopunlockedchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-phaselockedloopunlockedchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the channels that had their PLLs unlock. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] PhaseLockedLoopUnlockedChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of

### PhaseLockedLoopUnlockedChannels

Indicates the channels that had their PLLs unlock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] PhaseLockedLoopUnlockedChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-phaselockedloopunlockedchannelsexist.html language=enus -->
## TOPIC 01477: PhaseLockedLoopUnlockedChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-phaselockedloopunlockedchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-phaselockedloopunlockedchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PhaseLockedLoopUnlockedChannelsExist { get; }ExceptionsTyp

### PhaseLockedLoopUnlockedChannelsExist

Indicates whether the PLL is currently locked, or whether it became unlocked during the previous acquisition. Devices may report PLL Unlock either during acquisition or after acquisition.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PhaseLockedLoopUnlockedChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readallavailablesamples.html language=enus -->
## TOPIC 01478: ReadAllAvailableSamples

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readallavailablesamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readallavailablesamples.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of s

### ReadAllAvailableSamples

Specifies whether subsequent read operations read all samples currently available in the buffer or wait for the buffer to become full before reading. NI-DAQmx uses this setting for finite acquisitions and only when the number of samples to read is -1. For continuous acquisitions when the number of samples to read is -1, a read operation always reads all samples currently available in the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadAllAvailableSamples { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readautostart.html language=enus -->
## TOPIC 01479: ReadAutoStart

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readautostart.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readautostart.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if reading from the task automatically starts the task if you did not start the task explicitly by using starting the task. The default value is true. When reading from the task starts a finite acquisition task, it also stops the task after reading the last sample. SyntaxNamespace: Nationa

### ReadAutoStart

Specifies if reading from the task automatically starts the task if you did not start the task explicitly by using starting the task. The default value is true. When reading from the task starts a finite acquisition task, it also stops the task after reading the last sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadAutoStart { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readauxpowererrorchannels.html language=enus -->
## TOPIC 01480: ReadAuxPowerErrorChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readauxpowererrorchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readauxpowererrorchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which an auxiliary power supply error condition has been detected. You must read the Aux Power Error Channels Exist property before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQ

### ReadAuxPowerErrorChannels

Indicates a list of names of any virtual channels in the task for which an auxiliary power supply error condition has been detected. You must read the Aux Power Error Channels Exist property before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadAuxPowerErrorChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readauxpowererrorchannelsexist.html language=enus -->
## TOPIC 01481: ReadAuxPowerErrorChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readauxpowererrorchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readauxpowererrorchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an auxiliary power supply error condition for any channel in the task. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Aux Power Error Channels property. Otherwise, you will rece

### ReadAuxPowerErrorChannelsExist

Indicates if the device(s) detected an auxiliary power supply error condition for any channel in the task. Reading this property clears the error condition status for all channels in the task. You must read this property before you read the Aux Power Error Channels property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadAuxPowerErrorChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readexcitationfaultchannels.html language=enus -->
## TOPIC 01482: ReadExcitationFaultChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readexcitationfaultchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readexcitationfaultchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an excitation fault condition. You must read ReadExcitationFaultChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[]

### ReadExcitationFaultChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any virtual channels in the task for which the device(s) detected an [excitation fault condition](/csh?context=nidaqmx_mxdevconsid_excitationfaultdetection). You must read [ReadExcitationFaultChannelsExist](nationalinstruments-daqmx-daqstream-readexcitationfaultchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadExcitationFaultChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readexcitationfaultchannelsexist.html language=enus -->
## TOPIC 01483: ReadExcitationFaultChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readexcitationfaultchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readexcitationfaultchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an excitation fault condition for any virtual channel in the task. Reading this property clears the excitation fault status for all channels in the task. You must read this property before you read ReadExcitationFaultChannels. Otherwise, you will receive an error.

### ReadExcitationFaultChannelsExist

Indicates if the device(s) detected an [excitation fault condition](/csh?context=nidaqmx_mxdevconsid_excitationfaultdetection) for any virtual channel in the task. Reading this property clears the excitation fault status for all channels in the task. You must read this property before you read [ReadExcitationFaultChannels](nationalinstruments-daqmx-daqstream-readexcitationfaultchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadExcitationFaultChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readinputlimitsfaultchannels.html language=enus -->
## TOPIC 01484: ReadInputLimitsFaultChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readinputlimitsfaultchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readinputlimitsfaultchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read ReadInputLimitsFaultChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic s

### ReadInputLimitsFaultChannels

Indicates the virtual channels that have detected samples outside the upper or lower limits configured for each channel in the task. You must read [ReadInputLimitsFaultChannelsExist](nationalinstruments-daqmx-daqstream-readinputlimitsfaultchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadInputLimitsFaultChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readinputlimitsfaultchannelsexist.html language=enus -->
## TOPIC 01485: ReadInputLimitsFaultChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readinputlimitsfaultchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readinputlimitsfaultchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read ReadInputLimitsFaultCh

### ReadInputLimitsFaultChannelsExist

Indicates if the device or devices detected a sample that was outside the upper or lower limits configured for each channel in the task. Reading this property clears the input limits fault channel status for all channels in the task. You must read this property before you read [ReadInputLimitsFaultChannels](nationalinstruments-daqmx-daqstream-readinputlimitsfaultchannels.html). Otherwise, you will receive an error. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadInputLimitsFaultChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readoffset.html language=enus -->
## TOPIC 01486: ReadOffset

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readoffset.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with ReadRelativeTo. SyntaxNamespace: NationalInstruments.DAQmxpublic int ReadOffset { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-D

### ReadOffset

Specifies an offset in samples per channel at which to begin a read operation. This offset is relative to the location you specify with [ReadRelativeTo](nationalinstruments-daqmx-daqstream-readrelativeto.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int ReadOffset { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readopencurrentloopchannels.html language=enus -->
## TOPIC 01487: ReadOpenCurrentLoopChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readopencurrentloopchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readopencurrentloopchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an open current loop. You must read ReadOpenCurrentLoopChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] ReadOpenC

### ReadOpenCurrentLoopChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any virtual channels in the task for which the device(s) detected an [open current loop](/csh?context=nidaqmx_mxdevconsid_opencurrent). You must read [ReadOpenCurrentLoopChannelsExist](nationalinstruments-daqmx-daqstream-readopencurrentloopchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadOpenCurrentLoopChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readopencurrentloopchannelsexist.html language=enus -->
## TOPIC 01488: ReadOpenCurrentLoopChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readopencurrentloopchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readopencurrentloopchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an open current loop for any virtual channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read ReadOpenCurrentLoopChannels. Otherwise, you will receive an error. SyntaxN

### ReadOpenCurrentLoopChannelsExist

Indicates if the device(s) detected an [open current loop](/csh?context=nidaqmx_mxdevconsid_opencurrent) for any virtual channel in the task. Reading this property clears the open current loop status for all channels in the task. You must read this property before you read [ReadOpenCurrentLoopChannels](nationalinstruments-daqmx-daqstream-readopencurrentloopchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadOpenCurrentLoopChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readovercurrentchannels.html language=enus -->
## TOPIC 01489: ReadOvercurrentChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readovercurrentchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readovercurrentchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which the device(s) detected an overcurrent condition. You must read ReadOvercurrentChannelsExist before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent chan

### ReadOvercurrentChannels

Indicates a [list of names](/csh?context=nidaqmx_mxcncpts_physchannames) of any virtual channels in the task for which the device(s) detected an [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet). You must read [ReadOvercurrentChannelsExist](nationalinstruments-daqmx-daqstream-readovercurrentchannelsexist.html) before you read this property. Otherwise, you will receive an error. On some devices, you must restart the task for all overcurrent channels to recover.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadOvercurrentChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readovercurrentchannelsexist.html language=enus -->
## TOPIC 01490: ReadOvercurrentChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readovercurrentchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readovercurrentchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overcurrent condition for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read ReadOvercurrentChannels. Otherwise, you will receive an error. SyntaxNamespa

### ReadOvercurrentChannelsExist

Indicates if the device(s) detected an [overcurrent condition](/csh?context=nidaqmx_mxdevconsid_overcurrentdet) for any virtual channel in the task. Reading this property clears the overcurrent status for all channels in the task. You must read this property before you read [ReadOvercurrentChannels](nationalinstruments-daqmx-daqstream-readovercurrentchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadOvercurrentChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readovertemperaturechannels.html language=enus -->
## TOPIC 01491: ReadOvertemperatureChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readovertemperaturechannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readovertemperaturechannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any overtemperature virtual channels. You must read ReadOvertemperatureChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] ReadOvertemperatureChannels { get; }RemarksThis property re

### ReadOvertemperatureChannels

Indicates a list of names of any overtemperature virtual channels. You must read [ReadOvertemperatureChannelsExist](nationalinstruments-daqmx-daqstream-readovertemperaturechannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadOvertemperatureChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readovertemperaturechannelsexist.html language=enus -->
## TOPIC 01492: ReadOvertemperatureChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readovertemperaturechannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readovertemperaturechannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read ReadOvertemperatureChannels. Otherwise, you will receive an error. Sy

### ReadOvertemperatureChannelsExist

Indicates if the device(s) detected an overtemperature condition in any virtual channel in the task. Reading this property clears the overtemperature status for all channels in the task. You must read this property before you read [ReadOvertemperatureChannels](nationalinstruments-daqmx-daqstream-readovertemperaturechannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadOvertemperatureChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readoverwritemode.html language=enus -->
## TOPIC 01493: ReadOverwriteMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readoverwritemode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readoverwritemode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to overwrite samples in the buffer that you have not yet read. SyntaxNamespace: NationalInstruments.DAQmxpublic ReadOverwriteMode ReadOverwriteMode { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReadOverwriteMode

Specifies whether to overwrite samples in the buffer that you have not yet read.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReadOverwriteMode](nationalinstruments-daqmx-readoverwritemode.html) ReadOverwriteMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readpowersupplyfaultchannels.html language=enus -->
## TOPIC 01494: ReadPowerSupplyFaultChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readpowersupplyfaultchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readpowersupplyfaultchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the virtual channels that have detected a power supply fault. You must read WritePowerSupplyFaultChannelsExist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] ReadPowerSupplyFaultChannels { get; }RemarksThis pro

### ReadPowerSupplyFaultChannels

Indicates the virtual channels that have detected a power supply fault. You must read [WritePowerSupplyFaultChannelsExist](nationalinstruments-daqmx-daqstream-writepowersupplyfaultchannelsexist.html) before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadPowerSupplyFaultChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readpowersupplyfaultchannelsexist.html language=enus -->
## TOPIC 01495: ReadPowerSupplyFaultChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readpowersupplyfaultchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readpowersupplyfaultchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read ReadPowerSupplyFaultChannels. Otherwise, you will recei

### ReadPowerSupplyFaultChannelsExist

Indicates if the device or devices detected a power supply fault condition in any virtual channel in the task. Reading this property clears the power supply fault status for all channels in this task. You must read this property before you read [ReadPowerSupplyFaultChannels](nationalinstruments-daqmx-daqstream-readpowersupplyfaultchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadPowerSupplyFaultChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readraw__int.html language=enus -->
## TOPIC 01496: ReadRaw(int)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readraw__int.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readraw__int.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads raw, unprocessed samples from the channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic byte[] ReadRaw(int samplesPerChannel)RemarksThe format of the raw samples depends on the device from which you are reading. Consult your device documentation for more information.You can us

### ReadRaw(int)

Reads [raw](/csh?context=nidaqmx_mxcncpts_rawdata), unprocessed samples from the channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public byte[] ReadRaw(int samplesPerChannel)

#### Remarks

The format of the raw samples depends on the device from which you are reading. Consult your device documentation for more information.

You can use the MemoryStream class to translate the returned byte array data into other types.

Refer to [NI-DAQmx Readers and Writers](https://#) for more information about memory limitations in NI-DAQmx read methods.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| samplesPerChannel | int | The number of samples to read. If you set samplesPerChannel to -1 for a continuous acquisition, the read retrieves all samples available in the buffer at the time of the read. If you set samplesPerChannel to -1 for a finite acquisition, the read behavior is set by the ReadAllAvailableSamples property of the DaqStream you are reading from. |

#### Returns

A byte array of raw data from the task.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |
| OutOfMemoryException | There is not enough memory to carry out this operation. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readrawdatawidth.html language=enus -->
## TOPIC 01497: ReadRawDataWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readrawdatawidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readrawdatawidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bytes the size of a raw sample from the task. SyntaxNamespace: NationalInstruments.DAQmxpublic long ReadRawDataWidth { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ReadRawDataWidth

Indicates in bytes the size of a raw sample from the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long ReadRawDataWidth { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readrelativeto.html language=enus -->
## TOPIC 01498: ReadRelativeTo

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readrelativeto.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readrelativeto.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with ReadOffset, the read operation begins at that offset relative to the point you select with this property. The default value is CurrentReadPosition unless you configure a Reference Trigger for the

### ReadRelativeTo

Specifies the point in the buffer at which to begin a read operation. If you also specify an offset with [ReadOffset](nationalinstruments-daqmx-daqstream-readoffset.html), the read operation begins at that offset relative to the point you select with this property. The default value is [CurrentReadPosition](nationalinstruments-daqmx-readrelativeto.html) unless you configure a [Reference Trigger](/csh?context=nidaqmx_mxcncpts_referencetrigger) for the task. If you configure a Reference Trigger, the default value is [FirstPretriggerSample](nationalinstruments-daqmx-readrelativeto.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ReadRelativeTo](nationalinstruments-daqmx-readrelativeto.html) ReadRelativeTo { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readremotesenseerrorchannels.html language=enus -->
## TOPIC 01499: ReadRemoteSenseErrorChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readremotesenseerrorchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readremotesenseerrorchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any virtual channels in the task for which a remote sense connection error condition has been detected. You must read Remote Sense Error Channels Exist before you read this property. Otherwise, you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic s

### ReadRemoteSenseErrorChannels

Indicates a list of names of any virtual channels in the task for which a remote sense connection error condition has been detected. You must read Remote Sense Error Channels Exist before you read this property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadRemoteSenseErrorChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-daqstream-readremotesenseerrorchannelsexist.html language=enus -->
## TOPIC 01500: ReadRemoteSenseErrorChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-daqstream-readremotesenseerrorchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-daqstream-readremotesenseerrorchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device(s) detected an error condition of the remote sense connection for any channel in the task. You must disable the output and resolve the hardware connection issue to clear the error condition. You must read this property before you read the Remote Sense Error Channels property.

### ReadRemoteSenseErrorChannelsExist

Indicates if the device(s) detected an error condition of the remote sense connection for any channel in the task. You must disable the output and resolve the hardware connection issue to clear the error condition. You must read this property before you read the Remote Sense Error Channels property. Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadRemoteSenseErrorChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

DaqStream Class
