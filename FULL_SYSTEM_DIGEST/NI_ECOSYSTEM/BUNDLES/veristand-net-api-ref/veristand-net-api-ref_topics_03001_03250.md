# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=3001 end=3250 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-setxvalue__double.html language=enus -->
## TOPIC 03001: SetXValue(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-setxvalue__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-setxvalue__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of x in the comparison of x and y to the specified value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetXValue(double XValue)ParametersNameTypeDescriptionXValuedoubleThe value of x.

### SetXValue(double)

Sets the value of *x* in the comparison of *x* and *y* to the specified value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetXValue(double XValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| XValue | double | The value of x. |

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-setyvalue__basenode.html language=enus -->
## TOPIC 03002: SetYValue(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-setyvalue__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-setyvalue__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of y in the comparison of x and y to the value of the specified channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetYValue(BaseNode YValue)ParametersNameTypeDescriptionYValueBaseNodeThe channel that specifies the value of y.

### SetYValue(BaseNode)

Sets the value of *y* in the comparison of *x* and *y* to the value of the specified channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetYValue(BaseNode YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| YValue | BaseNode | The channel that specifies the value of y. |

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-setyvalue__double.html language=enus -->
## TOPIC 03003: SetYValue(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-setyvalue__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-setyvalue__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of y in the comparison of x and y to the specified value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetYValue(double YValue)ParametersNameTypeDescriptionYValuedoubleThe value of y.

### SetYValue(double)

Sets the value of *y* in the comparison of *x* and *y* to the specified value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetYValue(double YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| YValue | double | The value of y. |

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-xchannelvalue.html language=enus -->
## TOPIC 03004: XChannelValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-xchannelvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-xchannelvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that specifies the value of x in the comparison of x and y. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode XChannelValue { get; }ReturnsA BaseNode reference to the channel, or null if x is a constant.

### XChannelValue

Gets the channel that specifies the value of *x* in the comparison of *x* and *y*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) XChannelValue { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel, or null if *x* is a constant.

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-xconstantvalue.html language=enus -->
## TOPIC 03005: XConstantValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-xconstantvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-xconstantvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of x in the comparison of x and y, regardless of whether x is a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double XConstantValue { get; }ReturnsThe value of x.

### XConstantValue

Gets the constant value of *x* in the comparison of *x* and *y*, regardless of whether *x* is a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double XConstantValue { get; }

#### Returns

The value of *x*.

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-xisconstant.html language=enus -->
## TOPIC 03006: XIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-xisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-xisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the value of x in the comparison of x and y is specified by a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool XIsConstant { get; }Returnstrue if the value of x is specified by a constant. false if it is specified by a channel.

### XIsConstant

Gets whether the value of *x* in the comparison of *x* and *y* is specified by a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool XIsConstant { get; }

#### Returns

true if the value of *x* is specified by a constant. false if it is specified by a channel.

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-ychannelvalue.html language=enus -->
## TOPIC 03007: YChannelValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-ychannelvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-ychannelvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that specifies the value of y in the comparison of x and y. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode YChannelValue { get; }ReturnsA BaseNode reference to the channel, or null if y is a constant.

### YChannelValue

Gets the channel that specifies the value of *y* in the comparison of *x* and *y*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) YChannelValue { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel, or null if *y* is a constant.

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-yconstantvalue.html language=enus -->
## TOPIC 03008: YConstantValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-yconstantvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-yconstantvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of y in the comparison of x and y. regardless of whether x is a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double YConstantValue { get; }ReturnsThe value of y.

### YConstantValue

Gets the constant value of *y* in the comparison of *x* and *y*. regardless of whether *x* is a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double YConstantValue { get; }

#### Returns

The value of *y*.

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum-yisconstant.html language=enus -->
## TOPIC 03009: YIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum-yisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum-yisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the value of y in the comparison of x and y is specified by a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool YIsConstant { get; }Returnstrue if the value of y is specified by a constant. false if it is specified by a channel.

### YIsConstant

Gets whether the value of *y* in the comparison of *x* and *y* is specified by a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool YIsConstant { get; }

#### Returns

true if the value of *y* is specified by a constant. false if it is specified by a channel.

Parent topic:

Maximum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-maximum.html language=enus -->
## TOPIC 03010: Maximum Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-maximum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-maximum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a calculated channel with the Maximum function. This function compares two values (x and y) and returns the larger value. Derives fromCalculatedChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Maximum : CalculatedChannelRemarksAccessing this ClassMaxim

### Maximum Class

Represents a calculated channel with the **Maximum** function. This function compares two values (*x* and *y*) and returns the larger value.

#### Derives from

- CalculatedChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Maximum : CalculatedChannel

#### Remarks

**Accessing this Class**

- Maximum Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Maximum(string, string, double, BaseNode) | Initializes a new instance of Maximum where the value of x is a constant and the value of y is a channel. |
| Maximum(string, string, double, double) | Initializes a new instance of Maximum where the values of x and y are both constants. |
| Maximum(string, string, BaseNode, BaseNode) | Initializes a new instance of Maximum where the values of x and y are both channels. |
| Maximum(string, string, BaseNode, double) | Initializes a new instance of Maximum where the value of x is a channel and the value of y is a constant. |

#### Properties

| Name | Description |
| --- | --- |
| XChannelValue | Gets the channel that specifies the value of x in the comparison of x and y. |
| XConstantValue | Gets the constant value of x in the comparison of x and y, regardless of whether x is a constant or a channel. |
| XIsConstant | Gets whether the value of x in the comparison of x and y is specified by a constant or a channel. |
| YChannelValue | Gets the channel that specifies the value of y in the comparison of x and y. |
| YConstantValue | Gets the constant value of y in the comparison of x and y. regardless of whether x is a constant or a channel. |
| YIsConstant | Gets whether the value of y in the comparison of x and y is specified by a constant or a channel. |

#### Methods

| Name | Description |
| --- | --- |
| SetXValue(BaseNode) | Sets the value of x in the comparison of x and y to the value of the specified channel. |
| SetXValue(double) | Sets the value of x in the comparison of x and y to the specified value. |
| SetYValue(BaseNode) | Sets the value of y in the comparison of x and y to the value of the specified channel. |
| SetYValue(double) | Sets the value of y in the comparison of x and y to the specified value. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-basenode-basenode.html language=enus -->
## TOPIC 03011: Minimum(string, string, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Minimum where the values of x and y are both channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Minimum(string Name, string Description, BaseNode XValue, BaseNode YValue)ParametersNameTypeDescriptionNamestringThe name of the calculated ch

### Minimum(string, string, BaseNode, BaseNode)

Initializes a new instance of [Minimum](nationalinstruments-veristand-systemdefinitionapi-minimum.html) where the values of *x* and *y* are both channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Minimum(string Name, string Description, BaseNode XValue, BaseNode YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| XValue | BaseNode | The channel to be compared. |
| YValue | BaseNode | The channel value to which x is compared. |

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-basenode-double.html language=enus -->
## TOPIC 03012: Minimum(string, string, BaseNode, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-basenode-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-basenode-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Minimum where the value of x is a channel and the value of y is a constant. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Minimum(string Name, string Description, BaseNode XValue, double YValue)ParametersNameTypeDescriptionNamestringThe name o

### Minimum(string, string, BaseNode, double)

Initializes a new instance of [Minimum](nationalinstruments-veristand-systemdefinitionapi-minimum.html) where the value of *x* is a channel and the value of *y* is a constant.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Minimum(string Name, string Description, BaseNode XValue, double YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| XValue | BaseNode | The channel to be compared. |
| YValue | double | The constant value to which x is compared. |

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-double-basenode.html language=enus -->
## TOPIC 03013: Minimum(string, string, double, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-double-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-double-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Minimum where the value of x is a constant and the value of y is a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Minimum(string Name, string Description, double XValue, BaseNode YValue)ParametersNameTypeDescriptionNamestringThe name o

### Minimum(string, string, double, BaseNode)

Initializes a new instance of [Minimum](nationalinstruments-veristand-systemdefinitionapi-minimum.html) where the value of *x* is a constant and the value of *y* is a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Minimum(string Name, string Description, double XValue, BaseNode YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| XValue | double | The constant value to be compared. |
| YValue | BaseNode | The channel value to which x is compared. |

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-double-double.html language=enus -->
## TOPIC 03014: Minimum(string, string, double, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-double-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-minimum__string-string-double-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Minimum where the values of x and y are both constants. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Minimum(string Name, string Description, double XValue, double YValue)ParametersNameTypeDescriptionNamestringThe name of the calculated chann

### Minimum(string, string, double, double)

Initializes a new instance of [Minimum](nationalinstruments-veristand-systemdefinitionapi-minimum.html) where the values of *x* and *y* are both constants.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Minimum(string Name, string Description, double XValue, double YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the calculated channel. |
| Description | string | The description of the calculated channel. |
| XValue | double | The constant value to be compared. |
| YValue | double | The constant value to which x is compared. |

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-setxvalue__basenode.html language=enus -->
## TOPIC 03015: SetXValue(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-setxvalue__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-setxvalue__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of x in the comparison of x and y to the value of the specified channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetXValue(BaseNode XValue)ParametersNameTypeDescriptionXValueBaseNodeThe channel that specifies the value of x.

### SetXValue(BaseNode)

Sets the value of *x* in the comparison of *x* and *y* to the value of the specified channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetXValue(BaseNode XValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| XValue | BaseNode | The channel that specifies the value of x. |

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-setxvalue__double.html language=enus -->
## TOPIC 03016: SetXValue(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-setxvalue__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-setxvalue__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of x in the comparison of x and y to the specified value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetXValue(double XValue)ParametersNameTypeDescriptionXValuedoubleThe value of x.

### SetXValue(double)

Sets the value of *x* in the comparison of *x* and *y* to the specified value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetXValue(double XValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| XValue | double | The value of x. |

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-setyvalue__basenode.html language=enus -->
## TOPIC 03017: SetYValue(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-setyvalue__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-setyvalue__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of y in the comparison of x and y to the value of the specified channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetYValue(BaseNode YValue)ParametersNameTypeDescriptionYValueBaseNodeThe channel that specifies the value of y.

### SetYValue(BaseNode)

Sets the value of *y* in the comparison of *x* and *y* to the value of the specified channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetYValue(BaseNode YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| YValue | BaseNode | The channel that specifies the value of y. |

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-setyvalue__double.html language=enus -->
## TOPIC 03018: SetYValue(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-setyvalue__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-setyvalue__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of y in the comparison of x and y to the specified value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetYValue(double YValue)ParametersNameTypeDescriptionYValuedoubleThe value of y.

### SetYValue(double)

Sets the value of *y* in the comparison of *x* and *y* to the specified value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetYValue(double YValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| YValue | double | The value of y. |

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-xchannelvalue.html language=enus -->
## TOPIC 03019: XChannelValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-xchannelvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-xchannelvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that specifies the value of x in the comparison of x and y. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode XChannelValue { get; }ReturnsA BaseNode reference to the channel, or nullif x is a constant.

### XChannelValue

Gets the channel that specifies the value of *x* in the comparison of *x* and *y*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) XChannelValue { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel, or nullif *x* is a constant.

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-xconstantvalue.html language=enus -->
## TOPIC 03020: XConstantValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-xconstantvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-xconstantvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of x in the comparison of x and y, regardless of whether x is a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double XConstantValue { get; }ReturnsThe value of x.

### XConstantValue

Gets the constant value of *x* in the comparison of *x* and *y*, regardless of whether *x* is a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double XConstantValue { get; }

#### Returns

The value of *x*.

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-xisconstant.html language=enus -->
## TOPIC 03021: XIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-xisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-xisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the value of x in the comparison of x and y is specified by a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool XIsConstant { get; }Returnstrue if the value of x is specified by a constant. false if it is specified by a channel.

### XIsConstant

Gets whether the value of *x* in the comparison of *x* and *y* is specified by a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool XIsConstant { get; }

#### Returns

true if the value of *x* is specified by a constant. false if it is specified by a channel.

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-ychannelvalue.html language=enus -->
## TOPIC 03022: YChannelValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-ychannelvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-ychannelvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that specifies the value of y in the comparison of x and y. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode YChannelValue { get; }ReturnsA BaseNode reference to the channel, or null if y is a constant.

### YChannelValue

Gets the channel that specifies the value of *y* in the comparison of *x* and *y*.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) YChannelValue { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel, or null if *y* is a constant.

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-yconstantvalue.html language=enus -->
## TOPIC 03023: YConstantValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-yconstantvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-yconstantvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant value of y in the comparison of x and y. regardless of whether x is a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double YConstantValue { get; }ReturnsThe value of y.

### YConstantValue

Gets the constant value of *y* in the comparison of *x* and *y*. regardless of whether *x* is a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double YConstantValue { get; }

#### Returns

The value of *y*.

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum-yisconstant.html language=enus -->
## TOPIC 03024: YIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum-yisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum-yisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the value of y in the comparison of x and y is specified by a constant or a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool YIsConstant { get; }Returnstrue if the value of y is specified by a constant. false if it is specified by a channel.

### YIsConstant

Gets whether the value of *y* in the comparison of *x* and *y* is specified by a constant or a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool YIsConstant { get; }

#### Returns

true if the value of *y* is specified by a constant. false if it is specified by a channel.

Parent topic:

Minimum Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-minimum.html language=enus -->
## TOPIC 03025: Minimum Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-minimum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-minimum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a calculated channel with the Minimum function. This function compares two values (x and y) and returns the smaller value. Derives fromCalculatedChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Minimum : CalculatedChannelRemarksAccessing this ClassMini

### Minimum Class

Represents a calculated channel with the **Minimum** function. This function compares two values (*x* and *y*) and returns the smaller value.

#### Derives from

- CalculatedChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Minimum : CalculatedChannel

#### Remarks

**Accessing this Class**

- Minimum Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Minimum(string, string, double, BaseNode) | Initializes a new instance of Minimum where the value of x is a constant and the value of y is a channel. |
| Minimum(string, string, double, double) | Initializes a new instance of Minimum where the values of x and y are both constants. |
| Minimum(string, string, BaseNode, BaseNode) | Initializes a new instance of Minimum where the values of x and y are both channels. |
| Minimum(string, string, BaseNode, double) | Initializes a new instance of Minimum where the value of x is a channel and the value of y is a constant. |

#### Properties

| Name | Description |
| --- | --- |
| XChannelValue | Gets the channel that specifies the value of x in the comparison of x and y. |
| XConstantValue | Gets the constant value of x in the comparison of x and y, regardless of whether x is a constant or a channel. |
| XIsConstant | Gets whether the value of x in the comparison of x and y is specified by a constant or a channel. |
| YChannelValue | Gets the channel that specifies the value of y in the comparison of x and y. |
| YConstantValue | Gets the constant value of y in the comparison of x and y. regardless of whether x is a constant or a channel. |
| YIsConstant | Gets whether the value of y in the comparison of x and y is specified by a constant or a channel. |

#### Methods

| Name | Description |
| --- | --- |
| SetXValue(BaseNode) | Sets the value of x in the comparison of x and y to the value of the specified channel. |
| SetXValue(double) | Sets the value of x in the comparison of x and y to the specified value. |
| SetYValue(BaseNode) | Sets the value of y in the comparison of x and y to the value of the specified channel. |
| SetYValue(double) | Sets the value of y in the comparison of x and y to the specified value. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-mode-adddynamicsignal__string-string-string-double-out.html language=enus -->
## TOPIC 03026: AddDynamicSignal(string, string, string, double, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-mode-adddynamicsignal__string-string-string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-mode-adddynamicsignal__string-string-string-double-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a dynamic signal to the Mode section of an NI-XNET CAN frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDynamicSignal(string signalName, string description, string units, double defaultValue, out Error error)ParametersNameTypeDescriptionsignalNamestringSpe

### AddDynamicSignal(string, string, string, double, out Error)

Adds a dynamic signal to the Mode section of an NI-XNET CAN frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDynamicSignal(string signalName, string description, string units, double defaultValue, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalName | string | Specifies the name of the dynamic signal. |
| description | string | Specifies the description for the dynamic signal. |
| units | string | Specifies the signal units. |
| defaultValue | double | Specifies the default value. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

Returns true if the signal was successfully added.

Parent topic:

Mode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-mode-adddynamicsignal__string-string-string-double.html language=enus -->
## TOPIC 03027: AddDynamicSignal(string, string, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-mode-adddynamicsignal__string-string-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-mode-adddynamicsignal__string-string-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a dynamic signal to the Mode section of an NI-XNET CAN frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddDynamicSignal(string signalName, string description, string units, double defaultValue)ParametersNameTypeDescriptionsignalNamestringSpecifies the name o

### AddDynamicSignal(string, string, string, double)

Adds a dynamic signal to the Mode section of an NI-XNET CAN frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddDynamicSignal(string signalName, string description, string units, double defaultValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalName | string | Specifies the name of the dynamic signal. |
| description | string | Specifies the description for the dynamic signal. |
| units | string | Specifies the signal units. |
| defaultValue | double | Specifies the default value. |

#### Returns

Returns true if the signal was successfully added.

Parent topic:

Mode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-mode-createmodeinformation__out.html language=enus -->
## TOPIC 03028: CreateModeInformation(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-mode-createmodeinformation__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-mode-createmodeinformation__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a ModeInformation section under the frame, which contains channels with timing information for incoming frames. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModeInformation CreateModeInformation(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an

### CreateModeInformation(out Error)

Creates a [ModeInformation](nationalinstruments-veristand-systemdefinitionapi-modeinformation.html) section under the frame, which contains channels with timing information for incoming frames.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModeInformation](nationalinstruments-veristand-systemdefinitionapi-modeinformation.html) CreateModeInformation(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

Mode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-mode-getalldynamicsignals.html language=enus -->
## TOPIC 03029: GetAllDynamicSignals()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-mode-getalldynamicsignals.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-mode-getalldynamicsignals.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses all the dynamic (multiplexed) signals under a Mode section of an NI-XNET CAN frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DynamicSignal[] GetAllDynamicSignals()ReturnsAn array of DynamicSignal objects.

### GetAllDynamicSignals()

Accesses all the dynamic (multiplexed) signals under a Mode section of an NI-XNET CAN frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DynamicSignal](nationalinstruments-veristand-systemdefinitionapi-dynamicsignal.html)[] GetAllDynamicSignals()

#### Returns

An array of [DynamicSignal](nationalinstruments-veristand-systemdefinitionapi-dynamicsignal.html) objects.

Parent topic:

Mode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-mode-getdynamicsignal.html language=enus -->
## TOPIC 03030: GetDynamicSignal()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-mode-getdynamicsignal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-mode-getdynamicsignal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the first dynamic (multiplexed) signal under a Mode section of an NI-XNET CAN frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DynamicSignal GetDynamicSignal()ReturnsA DynamicSignal object.

### GetDynamicSignal()

Accesses the first dynamic (multiplexed) signal under a Mode section of an NI-XNET CAN frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DynamicSignal](nationalinstruments-veristand-systemdefinitionapi-dynamicsignal.html) GetDynamicSignal()

#### Returns

A [DynamicSignal](nationalinstruments-veristand-systemdefinitionapi-dynamicsignal.html) object.

Parent topic:

Mode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-mode-getmodeinformation.html language=enus -->
## TOPIC 03031: GetModeInformation()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-mode-getmodeinformation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-mode-getmodeinformation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Mode Information section of the mode, which contains the ModeReceiveTime and ModeTimeDifference channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModeInformation GetModeInformation()

### GetModeInformation()

Gets the **Mode Information** section of the mode, which contains the [ModeReceiveTime](nationalinstruments-veristand-systemdefinitionapi-modereceivetime.html) and [ModeTimeDifference](nationalinstruments-veristand-systemdefinitionapi-modetimedifference.html) channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModeInformation](nationalinstruments-veristand-systemdefinitionapi-modeinformation.html) GetModeInformation()

Parent topic:

Mode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-mode.html language=enus -->
## TOPIC 03032: Mode Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-mode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-mode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Mode section under a signal format NI-XNET CAN frame. The Mode section organizes dynamic (multiplexed) signals according to their mode values. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Mode : SectionRemarksUse the members of this c

### Mode Class

Represents a **Mode** section under a signal format NI-XNET CAN frame. The **Mode** section organizes dynamic (multiplexed) signals according to their mode values.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Mode : Section

#### Remarks

Use the members of this class to configure the **Mode** section and to access the dynamic signals the section contains.

**Accessing this Class**

- [CreateMode(int, string, string, string, double, out Error)](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createmode__int-string-string-string-double-out.html)
- [GetModeList](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getmodelist.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddDynamicSignal(string, string, string, double) | Adds a dynamic signal to the Mode section of an NI-XNET CAN frame. |
| AddDynamicSignal(string, string, string, double, out Error) | Adds a dynamic signal to the Mode section of an NI-XNET CAN frame. |
| CreateModeInformation(out Error) | Creates a ModeInformation section under the frame, which contains channels with timing information for incoming frames. |
| GetAllDynamicSignals() | Accesses all the dynamic (multiplexed) signals under a Mode section of an NI-XNET CAN frame. |
| GetDynamicSignal() | Accesses the first dynamic (multiplexed) signal under a Mode section of an NI-XNET CAN frame. |
| GetModeInformation() | Gets the Mode Information section of the mode, which contains the ModeReceiveTime and ModeTimeDifference channels. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modeinformation-getreceivetime.html language=enus -->
## TOPIC 03033: GetReceiveTime()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modeinformation-getreceivetime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modeinformation-getreceivetime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Mode Receive Time channel under the current Mode Information section. The Mode Receive Time channel contains the timestamp of the most recently received frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModeReceiveTime GetReceiveTime()

### GetReceiveTime()

Gets the Mode Receive Time channel under the current Mode Information section. The Mode Receive Time channel contains the timestamp of the most recently received frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModeReceiveTime](nationalinstruments-veristand-systemdefinitionapi-modereceivetime.html) GetReceiveTime()

Parent topic:

ModeInformation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modeinformation-gettimedifference.html language=enus -->
## TOPIC 03034: GetTimeDifference()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modeinformation-gettimedifference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modeinformation-gettimedifference.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Mode Time Difference channel under the current Mode Information section. The Mode Time Difference channel contains the difference between the two most recent ModeReceiveTime timestamps. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModeTimeDifference GetTimeDiffer

### GetTimeDifference()

Gets the Mode Time Difference channel under the current Mode Information section. The Mode Time Difference channel contains the difference between the two most recent [ModeReceiveTime](nationalinstruments-veristand-systemdefinitionapi-modereceivetime.html) timestamps.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModeTimeDifference](nationalinstruments-veristand-systemdefinitionapi-modetimedifference.html) GetTimeDifference()

Parent topic:

ModeInformation Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modeinformation.html language=enus -->
## TOPIC 03035: ModeInformation Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modeinformation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modeinformation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Mode Information section under an NI-XNET CAN multiplexer mode. This section contains channels that store information about the mode, such as the timestamp at which it was received. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModeInf

### ModeInformation Class

Represents a **Mode Information** section under an NI-XNET CAN multiplexer mode. This section contains channels that store information about the mode, such as the timestamp at which it was received.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModeInformation : Section

#### Methods

| Name | Description |
| --- | --- |
| GetReceiveTime() | Gets the Mode Receive Time channel under the current Mode Information section. The Mode Receive Time channel contains the timestamp of the most recently received frame. |
| GetTimeDifference() | Gets the Mode Time Difference channel under the current Mode Information section. The Mode Time Difference channel contains the difference between the two most recent ModeReceiveTime timestamps. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-automaticprocessorvalue.html language=enus -->
## TOPIC 03036: AutomaticProcessorValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-automaticprocessorvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-automaticprocessorvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatic Simulation Model Procesor value, which assigns the processor to any available. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const int AutomaticProcessorValue

### AutomaticProcessorValue

Automatic Simulation Model Procesor value, which assigns the processor to any available.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const int AutomaticProcessorValue

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-baserate.html language=enus -->
## TOPIC 03037: BaseRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-baserate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-baserate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the base rate of the model in microseconds. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double BaseRate { get; }RemarksBase Rate = Primary Control Loop rate/Decimation ReturnsThe base rate in microseconds.

### BaseRate

Gets the base rate of the model in microseconds.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double BaseRate { get; }

#### Remarks

Note

Base Rate = Primary Control Loop rate/[Decimation](nationalinstruments-veristand-systemdefinitionapi-model-decimation.html)

#### Returns

The base rate in microseconds.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-companyname.html language=enus -->
## TOPIC 03038: CompanyName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-companyname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-companyname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the company name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string CompanyName { get; }

### CompanyName

Gets the company name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string CompanyName { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-decimation.html language=enus -->
## TOPIC 03039: Decimation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-decimation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-decimation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the decimation applied to the Primary Control Loop rate to determine the BaseRate of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int Decimation { get; set; }RemarksBase Rate = Primary Control Loop rate/Decimation ReturnsThe model decimation.

### Decimation

Gets or sets the decimation applied to the Primary Control Loop rate to determine the [BaseRate](nationalinstruments-veristand-systemdefinitionapi-model-baserate.html) of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int Decimation { get; set; }

#### Remarks

Note

Base Rate = Primary Control Loop rate/Decimation

#### Returns

The model decimation.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-dllpath.html language=enus -->
## TOPIC 03040: DLLPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-dllpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-dllpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the compiled version of the model (.dll file). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile DLLPath { get; }ReturnsA DependentFile reference to the DLL.

### DLLPath

Gets a reference to the compiled version of the model (.dll file).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) DLLPath { get; }

#### Returns

A [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) reference to the DLL.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-dllsize.html language=enus -->
## TOPIC 03041: DLLSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-dllsize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-dllsize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the size, in bytes, of the compiled version of the model (.dll file). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int DLLSize { get; }ReturnsThe DLL size, in bytes.

### DLLSize

Gets the size, in bytes, of the compiled version of the model (.dll file).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int DLLSize { get; }

#### Returns

The DLL size, in bytes.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-dlltimestamp.html language=enus -->
## TOPIC 03042: DLLTimestamp

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-dlltimestamp.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-dlltimestamp.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time at which the model DLL was compiled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double DLLTimestamp { get; }ReturnsThe time at which the model DLL was compiled.

### DLLTimestamp

Gets the time at which the model DLL was compiled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double DLLTimestamp { get; }

#### Returns

The time at which the model DLL was compiled.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-filedescription.html language=enus -->
## TOPIC 03043: FileDescription

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-filedescription.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-filedescription.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the file description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string FileDescription { get; }

### FileDescription

Gets the file description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string FileDescription { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-fileversion.html language=enus -->
## TOPIC 03044: FileVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-fileversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-fileversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the model version. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string FileVersion { get; }

### FileVersion

Gets the model version.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string FileVersion { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-getexecutionsection.html language=enus -->
## TOPIC 03045: GetExecutionSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-getexecutionsection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-getexecutionsection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Execution section, which contains channels that track execution details of the model, such as its current status and the amount of time that has elapsed since it began executing.SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Execution GetExecutionSection()ReturnsAn

### GetExecutionSection()

Gets the [Execution](nationalinstruments-veristand-systemdefinitionapi-execution.html) section, which contains channels that track execution details of the model, such as its current status and the amount of time that has elapsed since it began executing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Execution](nationalinstruments-veristand-systemdefinitionapi-execution.html) GetExecutionSection()

#### Returns

An [Execution](nationalinstruments-veristand-systemdefinitionapi-execution.html) object.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-getinportssection.html language=enus -->
## TOPIC 03046: GetInportsSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-getinportssection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-getinportssection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Inports section, which contains all the Inport and InportGroup objects under the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Inports GetInportsSection()ReturnsAn Inports object.

### GetInportsSection()

Gets the [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) section, which contains all the [Inport](nationalinstruments-veristand-systemdefinitionapi-inport.html) and [InportGroup](nationalinstruments-veristand-systemdefinitionapi-inportgroup.html) objects under the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) GetInportsSection()

#### Returns

An [Inports](nationalinstruments-veristand-systemdefinitionapi-inports.html) object.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-getmodeldetails.html language=enus -->
## TOPIC 03047: GetModelDetails()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-getmodeldetails.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-getmodeldetails.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a dictionary with properties about the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Dictionary< string, string > GetModelDetails()ReturnsA dictionary where the key is the name of the property and the value is the value of the property.

### GetModelDetails()

Creates a dictionary with properties about the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Dictionary](nationalinstruments-veristand-systemdefinitionapi-dictionary.html)< string, string > GetModelDetails()

#### Returns

A dictionary where the key is the name of the property and the value is the value of the property.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-getoutportssection.html language=enus -->
## TOPIC 03048: GetOutportsSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-getoutportssection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-getoutportssection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Outports section, which contains all the Outport and OutportGroup objects under the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Outports GetOutportsSection()ReturnsAn Outports object.

### GetOutportsSection()

Gets the [Outports](nationalinstruments-veristand-systemdefinitionapi-outports.html) section, which contains all the [Outport](nationalinstruments-veristand-systemdefinitionapi-outport.html) and [OutportGroup](nationalinstruments-veristand-systemdefinitionapi-outportgroup.html) objects under the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Outports](nationalinstruments-veristand-systemdefinitionapi-outports.html) GetOutportsSection()

#### Returns

An [Outports](nationalinstruments-veristand-systemdefinitionapi-outports.html) object.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-getparameterssection.html language=enus -->
## TOPIC 03049: GetParametersSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-getparameterssection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-getparameterssection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ModelParameters section, which contains all the ModelParameter and ModelParameterGroup objects under the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameters GetParametersSection()ReturnsA ModelParameters object.

### GetParametersSection()

Gets the [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) section, which contains all the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) and [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) objects under the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) GetParametersSection()

#### Returns

A [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) object.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-getsectionwithallparameters.html language=enus -->
## TOPIC 03050: GetSectionWithAllParameters()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-getsectionwithallparameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-getsectionwithallparameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all parameter, whether they're already imported or not. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameters GetSectionWithAllParameters()RemarksThis section gets cached whenever the model is loaded. If the model hasn't been loaded this session a load from di

### GetSectionWithAllParameters()

Gets all parameter, whether they're already imported or not.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) GetSectionWithAllParameters()

#### Remarks

This section gets cached whenever the model is loaded. If the model hasn't been loaded this session a load from disk will be performed.

#### Returns

Section containing all available parameters

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-getsectionwithallsignals.html language=enus -->
## TOPIC 03051: GetSectionWithAllSignals()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-getsectionwithallsignals.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-getsectionwithallsignals.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all signals, whether they're already imported or not. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignals GetSectionWithAllSignals()RemarksThis section gets cached whenever the model is loaded. If the model hasn't been loaded this session a load from disk will

### GetSectionWithAllSignals()

Gets all signals, whether they're already imported or not.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) GetSectionWithAllSignals()

#### Remarks

This section gets cached whenever the model is loaded. If the model hasn't been loaded this session a load from disk will be performed.

#### Returns

Section containing all available signals

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-getsignalssection.html language=enus -->
## TOPIC 03052: GetSignalsSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-getsignalssection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-getsignalssection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ModelSignals section, which contains all the ModelSignal and ModelSignalGroup objects under the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignals GetSignalsSection()ReturnsA ModelSignals object.

### GetSignalsSection()

Gets the [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) section, which contains all the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) and [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) objects under the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) GetSignalsSection()

#### Returns

A [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) object.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-globalparameterscope.html language=enus -->
## TOPIC 03053: GlobalParameterScope

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-globalparameterscope.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-globalparameterscope.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether global parameters in the current model share their values with other models on the same target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic GlobalParameterScopes GlobalParameterScope { get; set; }RemarksFor more information about global parameters, r

### GlobalParameterScope

Gets or sets whether global parameters in the current model share their values with other models on the same target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [GlobalParameterScopes](nationalinstruments-veristand-systemdefinitionapi-globalparameterscopes.html) GlobalParameterScope { get; set; }

#### Remarks

For more information about global parameters, refer to the *Differences Between Local and Global Parameters* topic of the *NI VeriStand Help*.

#### Returns

An enumeration of [GlobalParameterScopes](nationalinstruments-veristand-systemdefinitionapi-globalparameterscopes.html).

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-importparameters__ienumerable_modelparameter..html language=enus -->
## TOPIC 03054: ImportParameters(IEnumerable< ModelParameter >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-importparameters__ienumerable_modelparameter..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-importparameters__ienumerable_modelparameter..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Import parameters as channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ImportParameters(IEnumerable< ModelParameter > parameters)ParametersNameTypeDescriptionparametersIEnumerable< ModelParameter >parameters to importReturnsTrue if no error occurs, false otherwi

### ImportParameters(IEnumerable< ModelParameter >)

Import parameters as channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ImportParameters(IEnumerable< ModelParameter > parameters)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameters | IEnumerable< ModelParameter > | parameters to import |

#### Returns

True if no error occurs, false otherwise

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-importsignals__ienumerable_modelsignal..html language=enus -->
## TOPIC 03055: ImportSignals(IEnumerable< ModelSignal >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-importsignals__ienumerable_modelsignal..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-importsignals__ienumerable_modelsignal..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Import signals as channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ImportSignals(IEnumerable< ModelSignal > signals)ParametersNameTypeDescriptionsignalsIEnumerable< ModelSignal >signals to importReturnsTrue if no error occurs, false otherwise

### ImportSignals(IEnumerable< ModelSignal >)

Import signals as channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ImportSignals(IEnumerable< ModelSignal > signals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signals | IEnumerable< ModelSignal > | signals to import |

#### Returns

True if no error occurs, false otherwise

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-internalname.html language=enus -->
## TOPIC 03056: InternalName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-internalname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-internalname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the internal name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string InternalName { get; }

### InternalName

Gets the internal name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string InternalName { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-legalcopyright.html language=enus -->
## TOPIC 03057: LegalCopyright

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-legalcopyright.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-legalcopyright.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the legal copyright. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string LegalCopyright { get; }

### LegalCopyright

Gets the legal copyright.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string LegalCopyright { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-loadsuccess.html language=enus -->
## TOPIC 03058: LoadSuccess

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-loadsuccess.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-loadsuccess.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether NI VeriStand loaded the model successfully. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool LoadSuccess { get; private set; }Returnstrue if the model loaded successfully.

### LoadSuccess

Gets whether NI VeriStand loaded the model successfully.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool LoadSuccess { get; private set; }

#### Returns

true if the model loaded successfully.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-md5.html language=enus -->
## TOPIC 03059: MD5

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-md5.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-md5.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the MD5 message-digest for the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string MD5 { get; }ReturnsThe MD5 message-digest.

### MD5

Gets the MD5 message-digest for the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string MD5 { get; }

#### Returns

The MD5 message-digest.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-bool-uint.html language=enus -->
## TOPIC 03060: Model(string, string, string, int, int, ushort, bool, bool, bool, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-bool-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-bool-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Model and sets the network port that an .mdl file uses for communication via TCP. DLLs and .lvmodel files do not require a network port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Model(string Name, string Description, string ModelPath, int

### Model(string, string, string, int, int, ushort, bool, bool, bool, uint)

Initializes a new instance of [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) and sets the network port that an .mdl file uses for communication via TCP. DLLs and .lvmodel files do not require a network port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Model(string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, bool ImportSignals, uint NIVeriStandServerPort)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the model. |
| Description | string | The description of the model. |
| ModelPath | string | The path to the compiled model. |
| Processor | int | The processor on which the model runs. |
| Decimation | int | The decimation of the model. |
| InitialState | ushort | The initial execution state of the model. 0: Running. 1: Paused. |
| SegmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded. |
| ImportParameters | bool | true to import parameters. |
| ImportSignals | bool | true to import signals. |
| NIVeriStandServerPort | uint | The network port that the model uses for communication via TCP. |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-bool.html language=enus -->
## TOPIC 03061: Model(string, string, string, int, int, ushort, bool, bool, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Model(string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, bool ImportSignals)ParametersNameType

### Model(string, string, string, int, int, ushort, bool, bool, bool)

Initializes a new instance of [Model](nationalinstruments-veristand-systemdefinitionapi-model.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Model(string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, bool ImportSignals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the model. |
| Description | string | The description of the model. |
| ModelPath | string | The path to the compiled model. |
| Processor | int | The processor on which the model runs. |
| Decimation | int | The decimation applied to the Primary Control Loop rate to determine the base rate for executing the model. |
| InitialState | ushort | The initial execution state of the model. 0: Running. 1: Paused. |
| SegmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded. |
| ImportParameters | bool | true to import parameters. |
| ImportSignals | bool | true to import signals. |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool-uint.html language=enus -->
## TOPIC 03062: Model(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Model, filters the imported parameters and signals according to the conditions you specify, and sets the network port that an .mdl file uses for communication via TCP. DLLs and .lvmodel files do not require a network port. SyntaxNamespace: NationalInstruments.VeriStand.

### Model(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool, uint)

Initializes a new instance of [Model](nationalinstruments-veristand-systemdefinitionapi-model.html), filters the imported parameters and signals according to the conditions you specify, and sets the network port that an .mdl file uses for communication via TCP. DLLs and .lvmodel files do not require a network port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Model(string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, string ParameterRegularExpression, bool ImportSignals, string SignalRegularExpression, bool ImportOnlyNamedSignals, uint NIVeriStandServerPort)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the model. |
| Description | string | The description of the model. |
| ModelPath | string | The path to the compiled model. |
| Processor | int | The processor on which the model runs. |
| Decimation | int | The decimation of the model. |
| InitialState | ushort | The initial execution state of the model. 0: Running. 1: Paused. |
| SegmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded. |
| ImportParameters | bool | true to import parameters. |
| ParameterRegularExpression | string | The regular expression to use to filter parameters. Parameters that match the regular expression are imported. |
| ImportSignals | bool | true to import signals. |
| SignalRegularExpression | string | The regular expression to use to filter signals. Signals that match the regular expression are imported. |
| ImportOnlyNamedSignals | bool | true to import only named signals. |
| NIVeriStandServerPort | uint | The network port that the model uses for communication via TCP. This parameter is only valid for .mdl files. |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool.html language=enus -->
## TOPIC 03063: Model(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Model and filters the imported parameters and signals according to the conditions you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Model(string Name, string Description, string ModelPath, int Processor, int Decimation, ushort Initial

### Model(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool)

Initializes a new instance of [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) and filters the imported parameters and signals according to the conditions you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Model(string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, string ParameterRegularExpression, bool ImportSignals, string SignalRegularExpression, bool ImportOnlyNamedSignals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the model. |
| Description | string | The description of the model. |
| ModelPath | string | The path to the compiled model. |
| Processor | int | The processor on which the model runs. |
| Decimation | int | The decimation of the model. |
| InitialState | ushort | The initial execution state of the model. 0: Running. 1: Paused. |
| SegmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded. |
| ImportParameters | bool | true to import parameters. |
| ParameterRegularExpression | string | The regular expression to use to filter parameters. Parameters that match the regular expression are imported. |
| ImportSignals | bool | true to import signals. |
| SignalRegularExpression | string | The regular expression to use to filter signals. Signals that match the regular expression are imported. |
| ImportOnlyNamedSignals | bool | true to import only named signals. |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-globalparameterscopes-bool-string-bool-uint.html language=enus -->
## TOPIC 03064: Model(string, string, string, int, int, ushort, bool, bool, string, GlobalParameterScopes, bool, string, bool, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-globalparameterscopes-bool-string-bool-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-model__string-string-string-int-int-ushort-bool-bool-string-globalparameterscopes-bool-string-bool-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Model and filters the imported parameters and signals according to the conditions you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Model(string Name, string Description, string ModelPath, int Processor, int Decimation, ushort Initial

### Model(string, string, string, int, int, ushort, bool, bool, string, GlobalParameterScopes, bool, string, bool, uint)

Initializes a new instance of [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) and filters the imported parameters and signals according to the conditions you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Model(string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, string ParameterRegularExpression, GlobalParameterScopes GlobalParameterScope, bool ImportSignals, string SignalRegularExpression, bool ImportOnlyNamedSignals, uint NIVeriStandServerPort)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the model. |
| Description | string | The description of the model. |
| ModelPath | string | The path to the compiled model. |
| Processor | int | The processor on which the model runs. |
| Decimation | int | The decimation of the model. |
| InitialState | ushort | The initial execution state of the model. 0: Running. 1: Paused. |
| SegmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded. |
| ImportParameters | bool | true to import parameters. |
| ParameterRegularExpression | string | The regular expression to use to filter parameters. Parameters that match the regular expression are imported. |
| GlobalParameterScope | GlobalParameterScopes | The scope of the global parameters. They can be either target or model scoped. |
| ImportSignals | bool | true to import signals. |
| SignalRegularExpression | string | The regular expression to use to filter signals. Signals that match the regular expression are imported. |
| ImportOnlyNamedSignals | bool | true to import only named signals. |
| NIVeriStandServerPort | uint | The network port that the model uses for communication via TCP. This parameter is only valid for .mdl files. |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-modelauthor.html language=enus -->
## TOPIC 03065: ModelAuthor

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-modelauthor.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-modelauthor.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Author of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ModelAuthor { get; }

### ModelAuthor

Author of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ModelAuthor { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-modelbitness.html language=enus -->
## TOPIC 03066: ModelBitness

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-modelbitness.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-modelbitness.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the bitness of the compiled model (32- or 64-bit). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int ModelBitness { get; set; }ReturnsThe bitness of the model.

### ModelBitness

Gets the bitness of the compiled model (32- or 64-bit).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int ModelBitness { get; set; }

#### Returns

The bitness of the model.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-modeldescriptor.html language=enus -->
## TOPIC 03067: ModelDescriptor

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-modeldescriptor.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-modeldescriptor.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the model descriptor. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic IModelDescriptor ModelDescriptor { get; private set; }

### ModelDescriptor

Gets the model descriptor.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [IModelDescriptor](nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor.html) ModelDescriptor { get; private set; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-modelexecutiongroup.html language=enus -->
## TOPIC 03068: ModelExecutionGroup

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-modelexecutiongroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-modelexecutiongroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the model execution group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int ModelExecutionGroup { get; set; }

### ModelExecutionGroup

Gets or sets the model execution group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int ModelExecutionGroup { get; set; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-modelgenerationtoolchainversion.html language=enus -->
## TOPIC 03069: ModelGenerationToolchainVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-modelgenerationtoolchainversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-modelgenerationtoolchainversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the tool that was used to generate the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ModelGenerationToolchainVersion { get; }

### ModelGenerationToolchainVersion

Version of the tool that was used to generate the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ModelGenerationToolchainVersion { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-modelpath.html language=enus -->
## TOPIC 03070: ModelPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-modelpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-modelpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the uncompiled model file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile ModelPath { get; }ReturnsA DependentFile reference to the uncompiled model.

### ModelPath

Gets a reference to the uncompiled model file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) ModelPath { get; }

#### Returns

A [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) reference to the uncompiled model.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-modeltimestamp.html language=enus -->
## TOPIC 03071: ModelTimestamp

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-modeltimestamp.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-modeltimestamp.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the time at which the model was last saved. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double ModelTimestamp { get; }ReturnsThe time at which the model was last saved.

### ModelTimestamp

Gets the time at which the model was last saved.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double ModelTimestamp { get; }

#### Returns

The time at which the model was last saved.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-niveristandserverport.html language=enus -->
## TOPIC 03072: NIVeriStandServerPort

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-niveristandserverport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-niveristandserverport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink ® software. DLLs and .lvmodel files do not require a network port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic u

### NIVeriStandServerPort

Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink ® software. DLLs and .lvmodel files do not require a network port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint NIVeriStandServerPort { get; set; }

#### Returns

The number of the network port.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-processor.html language=enus -->
## TOPIC 03073: Processor

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-processor.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-processor.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to " any available " . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int Processor { get; set; }ReturnsThe processor on which the Model E

### Processor

Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to " any available " .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int Processor { get; set; }

#### Returns

The processor on which the Model Execution Loop executes.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-productname.html language=enus -->
## TOPIC 03074: ProductName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-productname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-productname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the product name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ProductName { get; }

### ProductName

Gets the product name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ProductName { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-refreshmodelinformation__bool-bool-bool.html language=enus -->
## TOPIC 03075: RefreshModelInformation(bool, bool, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-refreshmodelinformation__bool-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-refreshmodelinformation__bool-bool-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reloads a previously imported model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RefreshModelInformation(bool SegmentVectors, bool ImportParameters, bool ImportSignals)ParametersNameTypeDescriptionSegmentVectorsbooltrue to split up vector inputs, outputs, parameters

### RefreshModelInformation(bool, bool, bool)

Reloads a previously imported model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RefreshModelInformation(bool SegmentVectors, bool ImportParameters, bool ImportSignals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| SegmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded. |
| ImportParameters | bool | true to import parameters. |
| ImportSignals | bool | true to import signals. |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-refreshmodelinformation__bool-bool-string-bool-string-bool.html language=enus -->
## TOPIC 03076: RefreshModelInformation(bool, bool, string, bool, string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-refreshmodelinformation__bool-bool-string-bool-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-refreshmodelinformation__bool-bool-string-bool-string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reloads a previously imported model and filters parameters and signals according to the conditions you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RefreshModelInformation(bool SegmentVectors, bool ImportParameters, string ParameterRegularExpression, bool Im

### RefreshModelInformation(bool, bool, string, bool, string, bool)

Reloads a previously imported model and filters parameters and signals according to the conditions you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RefreshModelInformation(bool SegmentVectors, bool ImportParameters, string ParameterRegularExpression, bool ImportSignals, string SignalRegularExpression, bool ImportOnlyNamedSignals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| SegmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded. |
| ImportParameters | bool | true to import parameters. |
| ParameterRegularExpression | string | The regular expression to use to filter parameters. Parameters that match the regular expression are imported. |
| ImportSignals | bool | true to import signals. |
| SignalRegularExpression | string | The regular expression to use to filter signals. Signals that match the regular expression are imported. |
| ImportOnlyNamedSignals | bool | true to import only named signals. |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-reloadmodelfrompath__string-bool-out.html language=enus -->
## TOPIC 03077: ReloadModelFromPath(string, bool, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-reloadmodelfrompath__string-bool-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-reloadmodelfrompath__string-bool-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reload Model from the given path with the specified vector segmentation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ReloadModelFromPath(string newPath, bool segmentVectors, out string[] invalidNames)ParametersNameTypeDescriptionnewPathstringNew path from which to r

### ReloadModelFromPath(string, bool, out string[])

Reload Model from the given path with the specified vector segmentation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ReloadModelFromPath(string newPath, bool segmentVectors, out string[] invalidNames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newPath | string | New path from which to reload the model |
| segmentVectors | bool | Whether to segment vectors or not |
| invalidNames | out string[] | Names of the removed nodes |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-reloadmodelfrompath__string-out.html language=enus -->
## TOPIC 03078: ReloadModelFromPath(string, out string[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-reloadmodelfrompath__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-reloadmodelfrompath__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reloads the model from the given path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ReloadModelFromPath(string newPath, out string[] invalidNames)ParametersNameTypeDescriptionnewPathstringNew path from which to reload the modelinvalidNamesout string[]Names of the rem

### ReloadModelFromPath(string, out string[])

Reloads the model from the given path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ReloadModelFromPath(string newPath, out string[] invalidNames)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| newPath | string | New path from which to reload the model |
| invalidNames | out string[] | Names of the removed nodes |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-removeparameters__ienumerable_modelparameter..html language=enus -->
## TOPIC 03079: RemoveParameters(IEnumerable< ModelParameter >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-removeparameters__ienumerable_modelparameter..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-removeparameters__ienumerable_modelparameter..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remove imported parameters. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveParameters(IEnumerable< ModelParameter > parameters)ParametersNameTypeDescriptionparametersIEnumerable< ModelParameter >parameters to remove

### RemoveParameters(IEnumerable< ModelParameter >)

Remove imported parameters.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveParameters(IEnumerable< ModelParameter > parameters)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameters | IEnumerable< ModelParameter > | parameters to remove |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-removesignals__ienumerable_modelsignal..html language=enus -->
## TOPIC 03080: RemoveSignals(IEnumerable< ModelSignal >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-removesignals__ienumerable_modelsignal..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-removesignals__ienumerable_modelsignal..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Remove imported signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveSignals(IEnumerable< ModelSignal > signals)ParametersNameTypeDescriptionsignalsIEnumerable< ModelSignal >signals to remove

### RemoveSignals(IEnumerable< ModelSignal >)

Remove imported signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveSignals(IEnumerable< ModelSignal > signals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signals | IEnumerable< ModelSignal > | signals to remove |

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-renamenode__string.html language=enus -->
## TOPIC 03081: RenameNode(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-renamenode__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-renamenode__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override bool RenameNode(string NewName)ParametersNameTypeDescriptionNewNamestri

### RenameNode(string)

Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override bool RenameNode(string NewName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| NewName | string | The name of the node. |

#### Returns

true if the node was renamed successfully.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-segmentvectors.html language=enus -->
## TOPIC 03082: SegmentVectors

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-segmentvectors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-segmentvectors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets information about whether or not vector inputs, outputs, parameters, and signals were split up into scalar channels when the model was loaded. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SegmentVectors { get; }Returnstrue if vectors were segmented into scalar c

### SegmentVectors

Gets information about whether or not vector inputs, outputs, parameters, and signals were split up into scalar channels when the model was loaded.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SegmentVectors { get; }

#### Returns

true if vectors were segmented into scalar channels.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-showunnamedsignals.html language=enus -->
## TOPIC 03083: ShowUnnamedSignals

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-showunnamedsignals.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-showunnamedsignals.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether signals without names are visible. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ShowUnnamedSignals { get; }Returnstrue if unnamed signals are visible.

### ShowUnnamedSignals

Gets whether signals without names are visible.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ShowUnnamedSignals { get; }

#### Returns

true if unnamed signals are visible.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-targetplatforms.html language=enus -->
## TOPIC 03084: TargetPlatforms

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-targetplatforms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-targetplatforms.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Target platforms supported by the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string[] TargetPlatforms { get; }

### TargetPlatforms

Target platforms supported by the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string[] TargetPlatforms { get; }

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model-userrate.html language=enus -->
## TOPIC 03085: UserRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model-userrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model-userrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double UserRate { get; }RemarksTHIS PROPERTY IS OBSOLETE in NI VeriStand 2011 SP1 and later. Use BaseRate instead.Gets the user rate of the model. ReturnsThe user rate.

### UserRate

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double UserRate { get; }

#### Remarks

THIS PROPERTY IS OBSOLETE in NI VeriStand 2011 SP1 and later. Use [BaseRate](nationalinstruments-veristand-systemdefinitionapi-model-baserate.html) instead.

Gets the user rate of the model.

#### Returns

The user rate.

Parent topic:

Model Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-model.html language=enus -->
## TOPIC 03086: Model Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-model.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a model, which is a mathematical representation of a real-world system. A model responds to stimuli by producing outputs in a way that emulates the behavior of the modeled item. Models contain inputs and outputs that send and receive data. Models contain parameters you can manipulate and

### Model Class

Represents a model, which is a mathematical representation of a real-world system. A model responds to stimuli by producing outputs in a way that emulates the behavior of the modeled item. Models contain inputs and outputs that send and receive data. Models contain parameters you can manipulate and signals whose values you can view. For example, a model that generates a sine wave contains parameters that adjust the amplitude and frequency of the sine wave. You can view the value of the sine wave using the model signal.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Model : Section

#### Remarks

Use the members or this class to get information about, set the decimation for, or reload a model.

**Accessing this Class**

- Model Constructor

For example code and more information about accessing this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying Models in a System Definition File

C# Walkthrough: Modifying Models in a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Model(string, string, string, int, int, ushort, bool, bool, bool) | Initializes a new instance of Model. |
| Model(string, string, string, int, int, ushort, bool, bool, bool, uint) | Initializes a new instance of Model and sets the network port that an .mdl file uses for communication via TCP. DLLs and .lvmodel files do not require a network port. |
| Model(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool, uint) | Initializes a new instance of Model, filters the imported parameters and signals according to the conditions you specify, and sets the network port that an .mdl file uses for communication via TCP. DLLs and .lvmodel files do not require a network port. |
| Model(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool) | Initializes a new instance of Model and filters the imported parameters and signals according to the conditions you specify. |
| Model(string, string, string, int, int, ushort, bool, bool, string, GlobalParameterScopes, bool, string, bool, uint) | Initializes a new instance of Model and filters the imported parameters and signals according to the conditions you specify. |

#### Fields

| Name | Description |
| --- | --- |
| AutomaticProcessorValue | Automatic Simulation Model Procesor value, which assigns the processor to any available. |

#### Properties

| Name | Description |
| --- | --- |
| BaseRate | Gets the base rate of the model in microseconds. |
| CompanyName | Gets the company name. |
| Decimation | Gets or sets the decimation applied to the Primary Control Loop rate to determine the BaseRate of the model. |
| DLLPath | Gets a reference to the compiled version of the model (.dll file). |
| DLLSize | Gets the size, in bytes, of the compiled version of the model (.dll file). |
| DLLTimestamp | Gets the time at which the model DLL was compiled. |
| FileDescription | Gets the file description. |
| FileVersion | Gets the model version. |
| GlobalParameterScope | Gets or sets whether global parameters in the current model share their values with other models on the same target. |
| InternalName | Gets the internal name. |
| LegalCopyright | Gets the legal copyright. |
| LoadSuccess | Gets whether NI VeriStand loaded the model successfully. |
| MD5 | Gets the MD5 message-digest for the model. |
| ModelAuthor | Author of the model. |
| ModelBitness | Gets the bitness of the compiled model (32- or 64-bit). |
| ModelDescriptor | Gets the model descriptor. |
| ModelExecutionGroup | Gets or sets the model execution group. |
| ModelGenerationToolchainVersion | Version of the tool that was used to generate the model. |
| ModelPath | Gets a reference to the uncompiled model file. |
| ModelTimestamp | Gets the time at which the model was last saved. |
| NIVeriStandServerPort | Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink ® software. DLLs and .lvmodel files do not require a network port. |
| Processor | Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to " any available " . |
| ProductName | Gets the product name. |
| SegmentVectors | Gets information about whether or not vector inputs, outputs, parameters, and signals were split up into scalar channels when the model was loaded. |
| ShowUnnamedSignals | Gets whether signals without names are visible. |
| TargetPlatforms | Target platforms supported by the model. |
| UserRate |  |

#### Methods

| Name | Description |
| --- | --- |
| GetExecutionSection() | Gets the Execution section, which contains channels that track execution details of the model, such as its current status and the amount of time that has elapsed since it began executing. |
| GetInportsSection() | Gets the Inports section, which contains all the Inport and InportGroup objects under the model. |
| GetModelDetails() | Creates a dictionary with properties about the model. |
| GetOutportsSection() | Gets the Outports section, which contains all the Outport and OutportGroup objects under the model. |
| GetParametersSection() | Gets the ModelParameters section, which contains all the ModelParameter and ModelParameterGroup objects under the model. |
| GetSectionWithAllParameters() | Gets all parameter, whether they're already imported or not. |
| GetSectionWithAllSignals() | Gets all signals, whether they're already imported or not. |
| GetSignalsSection() | Gets the ModelSignals section, which contains all the ModelSignal and ModelSignalGroup objects under the model. |
| ImportParameters(IEnumerable< ModelParameter >) | Import parameters as channels. |
| ImportSignals(IEnumerable< ModelSignal >) | Import signals as channels. |
| RefreshModelInformation(bool, bool, string, bool, string, bool) | Reloads a previously imported model and filters parameters and signals according to the conditions you specify. |
| RefreshModelInformation(bool, bool, bool) | Reloads a previously imported model. |
| ReloadModelFromPath(string, out string[]) | Reloads the model from the given path. |
| ReloadModelFromPath(string, bool, out string[]) | Reload Model from the given path with the specified vector segmentation. |
| RemoveParameters(IEnumerable< ModelParameter >) | Remove imported parameters. |
| RemoveSignals(IEnumerable< ModelSignal >) | Remove imported signals. |
| RenameNode(string) | Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelcommand-initialstate.html language=enus -->
## TOPIC 03087: InitialState

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelcommand-initialstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelcommand-initialstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial execution state of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelCommandState InitialState { get; set; }ReturnsAn enumeration value of ModelCommandState.

### InitialState

Gets or sets the initial execution state of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelCommandState](nationalinstruments-veristand-systemdefinitionapi-modelcommandstate.html) InitialState { get; set; }

#### Returns

An enumeration value of [ModelCommandState](nationalinstruments-veristand-systemdefinitionapi-modelcommandstate.html).

Parent topic:

ModelCommand Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelcommand.html language=enus -->
## TOPIC 03088: ModelCommand Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelcommand.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelcommand.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Model Command channel, which you can use to send commands to the model running on the target. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelCommand : ChannelRemarksYou can send the following commands to a model at run-time: ValueC

### ModelCommand Class

Represents a **Model Command** channel, which you can use to send commands to the model running on the target.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelCommand : Channel

#### Remarks

| Value | Command |
| --- | --- |
| 0 | Start |
| 1 | Pause |
| 2 | Reset to the initial model state |
| 3 | Save the model state to a file |
| 4 | Restore the model state from a file |

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Execution.GetModelCommand

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| InitialState | Gets or sets the initial execution state of the model. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelcommandstate.html language=enus -->
## TOPIC 03089: ModelCommandState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelcommandstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelcommandstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current state of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ModelCommandStateMembersNameValueDescriptionStart0Starts running the model. PausePauses the model. ResetResets the model to its initial state. SaveSaves information about the curre

### ModelCommandState Enumeration

Specifies the current state of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ModelCommandState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Start | 0 | Starts running the model. |
| Pause |  | Pauses the model. |
| Reset |  | Resets the model to its initial state. |
| Save |  | Saves information about the current execution state of the model. |
| Restore |  | Restores the model execution state from a file. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modeldefaultgroup.html language=enus -->
## TOPIC 03090: ModelDefaultGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modeldefaultgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modeldefaultgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a parent class for the different types of sub-folders and sections a model can have. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelDefaultGroup : SectionRemarksYou cannot directly call this class, but several classes inherit its mem

### ModelDefaultGroup Class

Represents a parent class for the different types of sub-folders and sections a model can have.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelDefaultGroup : Section

#### Remarks

You cannot directly call this class, but several classes inherit its members.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameter-expression.html language=enus -->
## TOPIC 03091: Expression

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameter-expression.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameter-expression.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the expression of the model parameter. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Expression { get; }ReturnsThe expression.

### Expression

Gets the expression of the model parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Expression { get; }

#### Returns

The expression.

Parent topic:

ModelParameter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameter-index.html language=enus -->
## TOPIC 03092: Index

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameter-index.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameter-index.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the index of the model parameter. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int Index { get; }ReturnsThe parameter index.

### Index

Gets the index of the model parameter.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int Index { get; }

#### Returns

The parameter index.

Parent topic:

ModelParameter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameter-modelparameter__modelparamtype-string.html language=enus -->
## TOPIC 03093: ModelParameter(ModelParamType, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameter-modelparameter__modelparamtype-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameter-modelparameter__modelparamtype-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ModelParameter with the specified parameter and expression. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameter(ModelParamType parameter, string expression)ParametersNameTypeDescriptionparameterModelParamTypeThe model parameter.expres

### ModelParameter(ModelParamType, string)

Initializes a new instance of [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) with the specified parameter and expression.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ModelParameter(ModelParamType parameter, string expression)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameter | ModelParamType | The model parameter. |
| expression | string | The expression of the model parameter. |

Parent topic:

ModelParameter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameter-modelpath.html language=enus -->
## TOPIC 03094: ModelPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameter-modelpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameter-modelpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbolic path to the parameter within the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ModelPath { get; }ReturnsThe path to the symbolic parameter.

### ModelPath

Gets the symbolic path to the parameter within the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ModelPath { get; }

#### Returns

The path to the symbolic parameter.

Parent topic:

ModelParameter Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameter.html language=enus -->
## TOPIC 03095: ModelParameter Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a model parameter. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelParameter : ChannelRemarksUse the members of this class to get the index, expression, and symbolic path of a parameter. Accessing this ClassM:NationalInstruments.VeriS

### ModelParameter Class

Represents a model parameter.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelParameter : Channel

#### Remarks

Use the members of this class to get the index, expression, and symbolic path of a parameter.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameters.GetParameters
- ModelParameter Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ModelParameter(ModelParamType, string) | Initializes a new instance of ModelParameter with the specified parameter and expression. |

#### Properties

| Name | Description |
| --- | --- |
| Expression | Gets the expression of the model parameter. |
| Index | Gets the index of the model parameter. |
| ModelPath | Gets the symbolic path to the parameter within the model. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameter__modelparameter-out.html language=enus -->
## TOPIC 03096: AddModelParameter(ModelParameter, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameter__modelparameter-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameter__modelparameter-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameter to the ModelParameterGroup section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelParameter(ModelParameter modelParameter, out Error error)ParametersNameTypeDescriptionmodelParameterModelParameterThe parameter to add.errorout

### AddModelParameter(ModelParameter, out Error)

Adds the specified [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) to the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelParameter(ModelParameter modelParameter, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameter | ModelParameter | The parameter to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the parameter was added successfully.

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameter__modelparameter.html language=enus -->
## TOPIC 03097: AddModelParameter(ModelParameter)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameter__modelparameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameter__modelparameter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameter to the ModelParameterGroup section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelParameter(ModelParameter modelParameter)ParametersNameTypeDescriptionmodelParameterModelParameterThe parameter to add.Returnstrue if the paramet

### AddModelParameter(ModelParameter)

Adds the specified [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) to the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelParameter(ModelParameter modelParameter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameter | ModelParameter | The parameter to add. |

#### Returns

true if the parameter was added successfully.

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparametergroup__modelparametergroup-out.html language=enus -->
## TOPIC 03098: AddModelParameterGroup(ModelParameterGroup, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparametergroup__modelparametergroup-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparametergroup__modelparametergroup-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameterGroup as a sub-section of the current section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelParameterGroup(ModelParameterGroup modelParameterGroup, out Error error)ParametersNameTypeDescriptionmodelParameterGroupModelParameter

### AddModelParameterGroup(ModelParameterGroup, out Error)

Adds the specified [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) as a sub-section of the current section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelParameterGroup(ModelParameterGroup modelParameterGroup, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameterGroup | ModelParameterGroup | The ModelParameterGroup to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the section was added successfully.

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparametergroup__modelparametergroup.html language=enus -->
## TOPIC 03099: AddModelParameterGroup(ModelParameterGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparametergroup__modelparametergroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparametergroup__modelparametergroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameterGroup as a sub-section of the current section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelParameterGroup(ModelParameterGroup modelParameterGroup)ParametersNameTypeDescriptionmodelParameterGroupModelParameterGroupThe ModelPar

### AddModelParameterGroup(ModelParameterGroup)

Adds the specified [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) as a sub-section of the current section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelParameterGroup(ModelParameterGroup modelParameterGroup)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameterGroup | ModelParameterGroup | The ModelParameterGroup to add. |

#### Returns

true if the section was added successfully.

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameters__modelparameter_arr1-out.html language=enus -->
## TOPIC 03100: AddModelParameters(ModelParameter[], out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameters__modelparameter_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameters__modelparameter_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameter to the ModelParameterGroup section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelParameters(ModelParameter[] modelParameters, out Error error)ParametersNameTypeDescriptionmodelParametersModelParameter[]The parameters to add.e

### AddModelParameters(ModelParameter[], out Error)

Adds the specified [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) to the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelParameters(ModelParameter[] modelParameters, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameters | ModelParameter[] | The parameters to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the parameter was added successfully.

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameters__modelparameter_arr1.html language=enus -->
## TOPIC 03101: AddModelParameters(ModelParameter[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameters__modelparameter_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-addmodelparameters__modelparameter_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameter to the ModelParameterGroup section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelParameters(ModelParameter[] modelParameters)ParametersNameTypeDescriptionmodelParametersModelParameter[]The parameters to add.Returnstrue if the

### AddModelParameters(ModelParameter[])

Adds the specified [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) to the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelParameters(ModelParameter[] modelParameters)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameters | ModelParameter[] | The parameters to add. |

#### Returns

true if the parameter was added successfully.

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getmodelparametergroups.html language=enus -->
## TOPIC 03102: GetModelParameterGroups()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getmodelparametergroups.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getmodelparametergroups.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelParameterGroup elements from the current ModelParameterGroup section. This method gets the subgroups of the current group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameterGroup[] GetModelParameterGroups()RemarksModifications

### GetModelParameterGroups()

Gets an array that contains the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) elements from the current [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) section. This method gets the subgroups of the current group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html)[] GetModelParameterGroups()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) elements from the current [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) section.

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getparameters.html language=enus -->
## TOPIC 03103: GetParameters()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getparameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getparameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelParameter elements from the current ModelParameterGroup. This method gets the defined parameters in the current group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameter[] GetParameters()RemarksModifications you make to the co

### GetParameters()

Gets an array that contains the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) elements from the current [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html). This method gets the defined parameters in the current group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html)[] GetParameters()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) elements from the current [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html).

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getparameters__bool.html language=enus -->
## TOPIC 03104: GetParameters(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getparameters__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getparameters__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelParameter elements from the current ModelParameterGroup. This method gets the defined parameters in the current group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameter[] GetParameters(bool deep)RemarksModifications you make

### GetParameters(bool)

Gets an array that contains the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) elements from the current [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html). This method gets the defined parameters in the current group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html)[] GetParameters(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child ModelParameter element of the ModelParameterGroup section. |

#### Returns

An array that contains the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) elements from the current [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html).

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-modelparametergroup__string.html language=enus -->
## TOPIC 03105: ModelParameterGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-modelparametergroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-modelparametergroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ModelParameterGroup with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameterGroup(string Name)ParametersNameTypeDescriptionNamestringThe name of the ModelParameterGroup.

### ModelParameterGroup(string)

Initializes a new instance of [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ModelParameterGroup(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the ModelParameterGroup. |

Parent topic:

ModelParameterGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html language=enus -->
## TOPIC 03106: ModelParameterGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a sub-section of the ModelParameters section of a model. Parameter groups provide organization within the model. Derives fromModelDefaultGroupSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelParameterGroup : ModelDefaultGroupRemarksUse the members of thi

### ModelParameterGroup Class

Represents a sub-section of the [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) section of a model. Parameter groups provide organization within the model.

#### Derives from

- ModelDefaultGroup

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelParameterGroup : ModelDefaultGroup

#### Remarks

Use the members of this class to get a list of parameters or parameter groups under the current section.

**Accessing this Class**

- [GetModelParameterGroups](nationalinstruments-veristand-systemdefinitionapi-modelparameters-getmodelparametergroups.html)
- [GetModelParameterGroups](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup-getmodelparametergroups.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ModelParameterGroup(string) | Initializes a new instance of ModelParameterGroup with the specified name. |

#### Methods

| Name | Description |
| --- | --- |
| AddModelParameter(ModelParameter) | Adds the specified ModelParameter to the ModelParameterGroup section. |
| AddModelParameter(ModelParameter, out Error) | Adds the specified ModelParameter to the ModelParameterGroup section. |
| AddModelParameterGroup(ModelParameterGroup, out Error) | Adds the specified ModelParameterGroup as a sub-section of the current section. |
| AddModelParameterGroup(ModelParameterGroup) | Adds the specified ModelParameterGroup as a sub-section of the current section. |
| AddModelParameters(ModelParameter[]) | Adds the specified ModelParameter to the ModelParameterGroup section. |
| AddModelParameters(ModelParameter[], out Error) | Adds the specified ModelParameter to the ModelParameterGroup section. |
| GetModelParameterGroups() | Gets an array that contains the ModelParameterGroup elements from the current ModelParameterGroup section. This method gets the subgroups of the current group. |
| GetParameters() | Gets an array that contains the ModelParameter elements from the current ModelParameterGroup. This method gets the defined parameters in the current group. |
| GetParameters(bool) | Gets an array that contains the ModelParameter elements from the current ModelParameterGroup. This method gets the defined parameters in the current group. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-addmodelparametergroup__modelparametergroup-out.html language=enus -->
## TOPIC 03107: AddModelParameterGroup(ModelParameterGroup, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-addmodelparametergroup__modelparametergroup-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-addmodelparametergroup__modelparametergroup-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameterGroup as a sub-section of the Parameters section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelParameterGroup(ModelParameterGroup modelParameterGroup, out Error error)ParametersNameTypeDescriptionmodelParameterGroupModelParame

### AddModelParameterGroup(ModelParameterGroup, out Error)

Adds the specified [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) as a sub-section of the **Parameters** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelParameterGroup(ModelParameterGroup modelParameterGroup, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameterGroup | ModelParameterGroup | The ModelParameterGroup to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the section was added successfully.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-addmodelparametergroup__modelparametergroup.html language=enus -->
## TOPIC 03108: AddModelParameterGroup(ModelParameterGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-addmodelparametergroup__modelparametergroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-addmodelparametergroup__modelparametergroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameterGroup as a sub-section of the Parameters section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelParameterGroup(ModelParameterGroup modelParameterGroup)ParametersNameTypeDescriptionmodelParameterGroupModelParameterGroupThe Model

### AddModelParameterGroup(ModelParameterGroup)

Adds the specified [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) as a sub-section of the **Parameters** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelParameterGroup(ModelParameterGroup modelParameterGroup)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameterGroup | ModelParameterGroup | The ModelParameterGroup to add. |

#### Returns

true if the section was added successfully.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameter__modelparameter-out.html language=enus -->
## TOPIC 03109: AddParameter(ModelParameter, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameter__modelparameter-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameter__modelparameter-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameter to the Parameters section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddParameter(ModelParameter parameter, out Error error)ParametersNameTypeDescriptionparameterModelParameterThe parameter to add.errorout ErrorReturns an National

### AddParameter(ModelParameter, out Error)

Adds the specified [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) to the **Parameters** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddParameter(ModelParameter parameter, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameter | ModelParameter | The parameter to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the parameter was added successfully.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameter__modelparameter.html language=enus -->
## TOPIC 03110: AddParameter(ModelParameter)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameter__modelparameter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameter__modelparameter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameter to the Parameters section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddParameter(ModelParameter parameter)ParametersNameTypeDescriptionparameterModelParameterThe parameter to add.Returnstrue if the parameter was added successfull

### AddParameter(ModelParameter)

Adds the specified [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) to the **Parameters** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddParameter(ModelParameter parameter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| parameter | ModelParameter | The parameter to add. |

#### Returns

true if the parameter was added successfully.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameters__modelparameter_arr1-out.html language=enus -->
## TOPIC 03111: AddParameters(ModelParameter[], out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameters__modelparameter_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameters__modelparameter_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameter to the ModelParameterGroup section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddParameters(ModelParameter[] modelParameters, out Error error)ParametersNameTypeDescriptionmodelParametersModelParameter[]The parameters to add.erroro

### AddParameters(ModelParameter[], out Error)

Adds the specified [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) to the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddParameters(ModelParameter[] modelParameters, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameters | ModelParameter[] | The parameters to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the parameter was added successfully.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameters__modelparameter_arr1.html language=enus -->
## TOPIC 03112: AddParameters(ModelParameter[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameters__modelparameter_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-addparameters__modelparameter_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelParameter to the ModelParameterGroup section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddParameters(ModelParameter[] modelParameters)ParametersNameTypeDescriptionmodelParametersModelParameter[]The parameters to add.Returnstrue if the para

### AddParameters(ModelParameter[])

Adds the specified [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) to the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddParameters(ModelParameter[] modelParameters)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelParameters | ModelParameter[] | The parameters to add. |

#### Returns

true if the parameter was added successfully.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-getmodelparametergroups.html language=enus -->
## TOPIC 03113: GetModelParameterGroups()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-getmodelparametergroups.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-getmodelparametergroups.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelParameterGroup elements from the current ModelParameters section. This method gets the defined groups that organize parameters of a model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameterGroup[] GetModelParameterGroups()Rema

### GetModelParameterGroups()

Gets an array that contains the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) elements from the current [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) section. This method gets the defined groups that organize parameters of a model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html)[] GetModelParameterGroups()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) elements from the current [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) section.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-getparameters.html language=enus -->
## TOPIC 03114: GetParameters()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-getparameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-getparameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelParameter elements from the current ModelParameters section. This method gets the defined parameters of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameter[] GetParameters()RemarksModifications you make to the conten

### GetParameters()

Gets an array that contains the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) elements from the current [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) section. This method gets the defined parameters of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html)[] GetParameters()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) elements from the current [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) section.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters-getparameters__bool.html language=enus -->
## TOPIC 03115: GetParameters(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters-getparameters__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters-getparameters__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelParameter elements from the current ModelParameters section. This method gets the defined parameters of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelParameter[] GetParameters(bool deep)RemarksModifications you make to t

### GetParameters(bool)

Gets an array that contains the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) elements from the current [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) section. This method gets the defined parameters of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html)[] GetParameters(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child ModelParameter element of the ModelParameters section. |

#### Returns

An array that contains the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) elements from the current [ModelParameters](nationalinstruments-veristand-systemdefinitionapi-modelparameters.html) section.

Parent topic:

ModelParameters Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelparameters.html language=enus -->
## TOPIC 03116: ModelParameters Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelparameters.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelparameters.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the top-level Parameters section under a Model. This section contains all the ModelParameter and ModelParameterGroup objects under the model. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelParameters : SectionRemarksUse the members o

### ModelParameters Class

Represents the top-level **Parameters** section under a [Model](nationalinstruments-veristand-systemdefinitionapi-model.html). This section contains all the [ModelParameter](nationalinstruments-veristand-systemdefinitionapi-modelparameter.html) and [ModelParameterGroup](nationalinstruments-veristand-systemdefinitionapi-modelparametergroup.html) objects under the model.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelParameters : Section

#### Remarks

Use the members of this class to get a list of parameters or parameter groups under the current section.

**Accessing this Class**

- [GetParametersSection](nationalinstruments-veristand-systemdefinitionapi-model-getparameterssection.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddModelParameterGroup(ModelParameterGroup) | Adds the specified ModelParameterGroup as a sub-section of the Parameters section. |
| AddModelParameterGroup(ModelParameterGroup, out Error) | Adds the specified ModelParameterGroup as a sub-section of the Parameters section. |
| AddParameter(ModelParameter, out Error) | Adds the specified ModelParameter to the Parameters section. |
| AddParameter(ModelParameter) | Adds the specified ModelParameter to the Parameters section. |
| AddParameters(ModelParameter[]) | Adds the specified ModelParameter to the ModelParameterGroup section. |
| AddParameters(ModelParameter[], out Error) | Adds the specified ModelParameter to the ModelParameterGroup section. |
| GetModelParameterGroups() | Gets an array that contains the ModelParameterGroup elements from the current ModelParameters section. This method gets the defined groups that organize parameters of a model. |
| GetParameters() | Gets an array that contains the ModelParameter elements from the current ModelParameters section. This method gets the defined parameters of the model. |
| GetParameters(bool) | Gets an array that contains the ModelParameter elements from the current ModelParameters section. This method gets the defined parameters of the model. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-models-addmodel__model-out.html language=enus -->
## TOPIC 03117: AddModel(Model, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-models-addmodel__model-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-models-addmodel__model-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Model to the Models section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModel(Model model, out Error error)ParametersNameTypeDescriptionmodelModelThe model to add.ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriSt

### AddModel(Model, out Error)

Adds the specified [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) to the [Models](nationalinstruments-veristand-systemdefinitionapi-models.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModel(Model model, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| model | Model | The model to add. |

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the model was added successfully.

Parent topic:

Models Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-models-addmodel__model.html language=enus -->
## TOPIC 03118: AddModel(Model)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-models-addmodel__model.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-models-addmodel__model.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Model to the Models section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModel(Model model)ParametersNameTypeDescriptionmodelModelThe model to add.Returnstrue if the model was added successfully.

### AddModel(Model)

Adds the specified [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) to the [Models](nationalinstruments-veristand-systemdefinitionapi-models.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModel(Model model)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| model | Model | The model to add. |

#### Returns

true if the model was added successfully.

Parent topic:

Models Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-models-getmodels.html language=enus -->
## TOPIC 03119: GetModels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-models-getmodels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-models-getmodels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Model elements from the current Models section. This method gets the models that have been added to the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Model[] GetModels()RemarksModifications you make to the contents of this

### GetModels()

Gets an array that contains the [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) elements from the current [Models](nationalinstruments-veristand-systemdefinitionapi-models.html) section. This method gets the models that have been added to the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Model](nationalinstruments-veristand-systemdefinitionapi-model.html)[] GetModels()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) elements from the current [Models](nationalinstruments-veristand-systemdefinitionapi-models.html) section.

Parent topic:

Models Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-models.html language=enus -->
## TOPIC 03120: Models Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-models.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-models.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Models section under SimulationModels. This section contains any compiled or uncompiled models you add to the system definition. NI VeriStand supports importing .dll, .mdl, and .lvmodel file types. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpu

### Models Class

Represents the **Models** section under [SimulationModels](nationalinstruments-veristand-systemdefinitionapi-simulationmodels.html). This section contains any compiled or uncompiled models you add to the system definition. NI VeriStand supports importing .dll, .mdl, and .lvmodel file types.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Models : Section

#### Remarks

Use the members of this class to add a model or get a list of existing models.

**Accessing this Class**

- [GetModels](nationalinstruments-veristand-systemdefinitionapi-simulationmodels-getmodels.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddModel(Model, out Error) | Adds the specified Model to the Models section. |
| AddModel(Model) | Adds the specified Model to the Models section. |
| GetModels() | Gets an array that contains the Model elements from the current Models section. This method gets the models that have been added to the system definition. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignal-index.html language=enus -->
## TOPIC 03121: Index

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignal-index.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignal-index.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the index of the model signal. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int Index { get; }ReturnsThe signal index.

### Index

Gets the index of the model signal.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int Index { get; }

#### Returns

The signal index.

Parent topic:

ModelSignal Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignal-modelpath.html language=enus -->
## TOPIC 03122: ModelPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignal-modelpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignal-modelpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the symbolic path to the parameter within the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ModelPath { get; }ReturnsThe path to the symbolic parameter.

### ModelPath

Gets the symbolic path to the parameter within the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ModelPath { get; }

#### Returns

The path to the symbolic parameter.

Parent topic:

ModelSignal Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignal-modelsignal__modelsignaltype.html language=enus -->
## TOPIC 03123: ModelSignal(ModelSignalType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignal-modelsignal__modelsignaltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignal-modelsignal__modelsignaltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ModelSignal with the specified signal. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignal(ModelSignalType signal)ParametersNameTypeDescriptionsignalModelSignalTypeThe model signal.

### ModelSignal(ModelSignalType)

Initializes a new instance of [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) with the specified signal.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ModelSignal(ModelSignalType signal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signal | ModelSignalType | The model signal. |

Parent topic:

ModelSignal Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignal-path.html language=enus -->
## TOPIC 03124: Path

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignal-path.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignal-path.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the model that contains the signal. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Path { get; }ReturnsThe path to the model.

### Path

Gets the path to the model that contains the signal.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Path { get; }

#### Returns

The path to the model.

Parent topic:

ModelSignal Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignal.html language=enus -->
## TOPIC 03125: ModelSignal Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a model signal. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelSignal : ChannelRemarksUse the members of this class to get the index and path of a signal. Accessing this ClassM:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelS

### ModelSignal Class

Represents a model signal.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelSignal : Channel

#### Remarks

Use the members of this class to get the index and path of a signal.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignals.GetSignals
- ModelSignal Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ModelSignal(ModelSignalType) | Initializes a new instance of ModelSignal with the specified signal. |

#### Properties

| Name | Description |
| --- | --- |
| Index | Gets the index of the model signal. |
| ModelPath | Gets the symbolic path to the parameter within the model. |
| Path | Gets the path to the model that contains the signal. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignal__modelsignal-out.html language=enus -->
## TOPIC 03126: AddModelSignal(ModelSignal, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignal__modelsignal-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignal__modelsignal-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelSignal to the ModelSignalGroup section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelSignal(ModelSignal modelSignal, out Error error)ParametersNameTypeDescriptionmodelSignalModelSignalThe signal to add.errorout ErrorReturns an National

### AddModelSignal(ModelSignal, out Error)

Adds the specified [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) to the [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelSignal(ModelSignal modelSignal, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelSignal | ModelSignal | The signal to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the signal was added successfully.

Parent topic:

ModelSignalGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignal__modelsignal.html language=enus -->
## TOPIC 03127: AddModelSignal(ModelSignal)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignal__modelsignal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignal__modelsignal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelSignal to the ModelSignalGroup section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelSignal(ModelSignal modelSignal)ParametersNameTypeDescriptionmodelSignalModelSignalThe signal to add.Returnstrue if the signal was added successfully.

### AddModelSignal(ModelSignal)

Adds the specified [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) to the [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelSignal(ModelSignal modelSignal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelSignal | ModelSignal | The signal to add. |

#### Returns

true if the signal was added successfully.

Parent topic:

ModelSignalGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignalgroup__modelsignalgroup-out.html language=enus -->
## TOPIC 03128: AddModelSignalGroup(ModelSignalGroup, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignalgroup__modelsignalgroup-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignalgroup__modelsignalgroup-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelSignalGroup as a sub-section of the current section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelSignalGroup(ModelSignalGroup modelSignalGroup, out Error error)ParametersNameTypeDescriptionmodelSignalGroupModelSignalGroupThe ModelSign

### AddModelSignalGroup(ModelSignalGroup, out Error)

Adds the specified [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) as a sub-section of the current section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelSignalGroup(ModelSignalGroup modelSignalGroup, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelSignalGroup | ModelSignalGroup | The ModelSignalGroup to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the section was added successfully.

Parent topic:

ModelSignalGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignalgroup__modelsignalgroup.html language=enus -->
## TOPIC 03129: AddModelSignalGroup(ModelSignalGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignalgroup__modelsignalgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-addmodelsignalgroup__modelsignalgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelSignalGroup as a sub-section of the current section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelSignalGroup(ModelSignalGroup modelSignalGroup)ParametersNameTypeDescriptionmodelSignalGroupModelSignalGroupThe ModelSignalGroup to add.Re

### AddModelSignalGroup(ModelSignalGroup)

Adds the specified [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) as a sub-section of the current section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelSignalGroup(ModelSignalGroup modelSignalGroup)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelSignalGroup | ModelSignalGroup | The ModelSignalGroup to add. |

#### Returns

true if the section was added successfully.

Parent topic:

ModelSignalGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getmodelsignalgroups.html language=enus -->
## TOPIC 03130: GetModelSignalGroups()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getmodelsignalgroups.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getmodelsignalgroups.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelSignalGroup elements from the current ModelSignalGroup. This method gets the defined subgroups of the current group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignalGroup[] GetModelSignalGroups()RemarksModifications you make to

### GetModelSignalGroups()

Gets an array that contains the [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) elements from the current [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html). This method gets the defined subgroups of the current group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html)[] GetModelSignalGroups()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) elements from the current [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html).

Parent topic:

ModelSignalGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getsignals.html language=enus -->
## TOPIC 03131: GetSignals()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getsignals.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getsignals.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelSignal elements from the current ModelSignalGroup. This method gets the signals that are categorized under the current group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignal[] GetSignals()RemarksModifications you make to the c

### GetSignals()

Gets an array that contains the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) elements from the current [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html). This method gets the signals that are categorized under the current group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html)[] GetSignals()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) elements from the current [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html).

Parent topic:

ModelSignalGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getsignals__bool.html language=enus -->
## TOPIC 03132: GetSignals(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getsignals__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getsignals__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelSignal elements from the current ModelSignalGroup. This method gets the signals that are categorized under the current group. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignal[] GetSignals(bool deep)RemarksModifications you make

### GetSignals(bool)

Gets an array that contains the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) elements from the current [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html). This method gets the signals that are categorized under the current group.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html)[] GetSignals(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child ModelSignal element of the ModelSignalGroup section. |

#### Returns

An array that contains the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) elements from the current [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html).

Parent topic:

ModelSignalGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-modelsignalgroup__string.html language=enus -->
## TOPIC 03133: ModelSignalGroup(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-modelsignalgroup__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-modelsignalgroup__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ModelSignalGroup with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignalGroup(string Name)ParametersNameTypeDescriptionNamestringThe name of the ModelSignalGroup.

### ModelSignalGroup(string)

Initializes a new instance of [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ModelSignalGroup(string Name)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the ModelSignalGroup. |

Parent topic:

ModelSignalGroup Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html language=enus -->
## TOPIC 03134: ModelSignalGroup Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a sub-section of the ModelSignals section of a model. Signal groups provide organization within the model. Derives fromModelDefaultGroupSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelSignalGroup : ModelDefaultGroupRemarksUse the members of this class t

### ModelSignalGroup Class

Represents a sub-section of the [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) section of a model. Signal groups provide organization within the model.

#### Derives from

- ModelDefaultGroup

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelSignalGroup : ModelDefaultGroup

#### Remarks

Use the members of this class to get a list of signals or signal groups under the current section.

**Accessing this Class**

- [GetModelSignalGroups](nationalinstruments-veristand-systemdefinitionapi-modelsignals-getmodelsignalgroups.html)
- [GetModelSignalGroups](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup-getmodelsignalgroups.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ModelSignalGroup(string) | Initializes a new instance of ModelSignalGroup with the specified name. |

#### Methods

| Name | Description |
| --- | --- |
| AddModelSignal(ModelSignal) | Adds the specified ModelSignal to the ModelSignalGroup section. |
| AddModelSignal(ModelSignal, out Error) | Adds the specified ModelSignal to the ModelSignalGroup section. |
| AddModelSignalGroup(ModelSignalGroup, out Error) | Adds the specified ModelSignalGroup as a sub-section of the current section. |
| AddModelSignalGroup(ModelSignalGroup) | Adds the specified ModelSignalGroup as a sub-section of the current section. |
| GetModelSignalGroups() | Gets an array that contains the ModelSignalGroup elements from the current ModelSignalGroup. This method gets the defined subgroups of the current group. |
| GetSignals() | Gets an array that contains the ModelSignal elements from the current ModelSignalGroup. This method gets the signals that are categorized under the current group. |
| GetSignals(bool) | Gets an array that contains the ModelSignal elements from the current ModelSignalGroup. This method gets the signals that are categorized under the current group. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignals-addmodelsignalgroup__modelsignalgroup-out.html language=enus -->
## TOPIC 03135: AddModelSignalGroup(ModelSignalGroup, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignals-addmodelsignalgroup__modelsignalgroup-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignals-addmodelsignalgroup__modelsignalgroup-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelSignalGroup as a sub-section of the Signals section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelSignalGroup(ModelSignalGroup modelSignalGroup, out Error error)ParametersNameTypeDescriptionmodelSignalGroupModelSignalGroupThe ModelSign

### AddModelSignalGroup(ModelSignalGroup, out Error)

Adds the specified [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) as a sub-section of the **Signals** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelSignalGroup(ModelSignalGroup modelSignalGroup, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelSignalGroup | ModelSignalGroup | The ModelSignalGroup to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the section was added successfully.

Parent topic:

ModelSignals Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignals-addmodelsignalgroup__modelsignalgroup.html language=enus -->
## TOPIC 03136: AddModelSignalGroup(ModelSignalGroup)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignals-addmodelsignalgroup__modelsignalgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignals-addmodelsignalgroup__modelsignalgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelSignalGroup as a sub-section of the Signals section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddModelSignalGroup(ModelSignalGroup modelSignalGroup)ParametersNameTypeDescriptionmodelSignalGroupModelSignalGroupThe ModelSignalGroup to add.Re

### AddModelSignalGroup(ModelSignalGroup)

Adds the specified [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) as a sub-section of the **Signals** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddModelSignalGroup(ModelSignalGroup modelSignalGroup)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelSignalGroup | ModelSignalGroup | The ModelSignalGroup to add. |

#### Returns

true if the section was added successfully.

Parent topic:

ModelSignals Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignals-addsignal__modelsignal-out.html language=enus -->
## TOPIC 03137: AddSignal(ModelSignal, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignals-addsignal__modelsignal-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignals-addsignal__modelsignal-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelSignal to the Signals section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignal(ModelSignal signal, out Error error)ParametersNameTypeDescriptionsignalModelSignalThe ModelSignal to add.errorout ErrorReturns an NationalInstruments.VeriSta

### AddSignal(ModelSignal, out Error)

Adds the specified [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) to the **Signals** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignal(ModelSignal signal, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signal | ModelSignal | The ModelSignal to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the signal was added successfully.

Parent topic:

ModelSignals Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignals-addsignal__modelsignal.html language=enus -->
## TOPIC 03138: AddSignal(ModelSignal)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignals-addsignal__modelsignal.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignals-addsignal__modelsignal.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified ModelSignal to the Signals section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignal(ModelSignal signal)ParametersNameTypeDescriptionsignalModelSignalThe ModelSignal to add.Returnstrue if the signal was added successfully.

### AddSignal(ModelSignal)

Adds the specified [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) to the **Signals** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignal(ModelSignal signal)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signal | ModelSignal | The ModelSignal to add. |

#### Returns

true if the signal was added successfully.

Parent topic:

ModelSignals Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignals-getmodelsignalgroups.html language=enus -->
## TOPIC 03139: GetModelSignalGroups()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignals-getmodelsignalgroups.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignals-getmodelsignalgroups.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelSignalGroup elements from the current ModelSignals section. This method gets the defined groups that organize model signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignalGroup[] GetModelSignalGroups()RemarksModifications you

### GetModelSignalGroups()

Gets an array that contains the [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) elements from the current [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) section. This method gets the defined groups that organize model signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html)[] GetModelSignalGroups()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) elements from the current [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) section.

Parent topic:

ModelSignals Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignals-getsignals.html language=enus -->
## TOPIC 03140: GetSignals()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignals-getsignals.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignals-getsignals.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelSignal elements from the current ModelSignals section. This method gets the defined model signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignal[] GetSignals()RemarksModifications you make to the contents of this list apply

### GetSignals()

Gets an array that contains the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) elements from the current [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) section. This method gets the defined model signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html)[] GetSignals()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) elements from the current [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) section.

Parent topic:

ModelSignals Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignals-getsignals__bool.html language=enus -->
## TOPIC 03141: GetSignals(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignals-getsignals__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignals-getsignals__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the ModelSignal elements from the current ModelSignals section. This method gets the defined model signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ModelSignal[] GetSignals(bool deep)RemarksModifications you make to the contents of this li

### GetSignals(bool)

Gets an array that contains the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) elements from the current [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) section. This method gets the defined model signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html)[] GetSignals(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child ModelSignal element of the ModelSignals section. |

#### Returns

An array that contains the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) elements from the current [ModelSignals](nationalinstruments-veristand-systemdefinitionapi-modelsignals.html) section.

Parent topic:

ModelSignals Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsignals.html language=enus -->
## TOPIC 03142: ModelSignals Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsignals.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsignals.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the top-level Signal section under a Model. This section contains all the ModelSignal and ModelSignalGroup objects under the model. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelSignals : SectionRemarksUse the members of this class

### ModelSignals Class

Represents the top-level **Signal** section under a [Model](nationalinstruments-veristand-systemdefinitionapi-model.html). This section contains all the [ModelSignal](nationalinstruments-veristand-systemdefinitionapi-modelsignal.html) and [ModelSignalGroup](nationalinstruments-veristand-systemdefinitionapi-modelsignalgroup.html) objects under the model.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelSignals : Section

#### Remarks

Use the members of this class to get a list of parameters or parameter groups under the current section.

**Accessing this Class**

- [GetSignalsSection](nationalinstruments-veristand-systemdefinitionapi-model-getsignalssection.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddModelSignalGroup(ModelSignalGroup) | Adds the specified ModelSignalGroup as a sub-section of the Signals section. |
| AddModelSignalGroup(ModelSignalGroup, out Error) | Adds the specified ModelSignalGroup as a sub-section of the Signals section. |
| AddSignal(ModelSignal, out Error) | Adds the specified ModelSignal to the Signals section. |
| AddSignal(ModelSignal) | Adds the specified ModelSignal to the Signals section. |
| GetModelSignalGroups() | Gets an array that contains the ModelSignalGroup elements from the current ModelSignals section. This method gets the defined groups that organize model signals. |
| GetSignals() | Gets an array that contains the ModelSignal elements from the current ModelSignals section. This method gets the defined model signals. |
| GetSignals(bool) | Gets an array that contains the ModelSignal elements from the current ModelSignals section. This method gets the defined model signals. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelstatus.html language=enus -->
## TOPIC 03143: ModelStatus Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelstatus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelstatus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Model Status channel, which you can use to get information about the current status of the model running on the target. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ModelStatus : ChannelRemarksA model can return the following status v

### ModelStatus Class

Represents a **Model Status** channel, which you can use to get information about the current status of the model running on the target.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ModelStatus : Channel

#### Remarks

A model can return the following status values:

| Value | Status |
| --- | --- |
| 0 | Running |
| 1 | Paused |
| 2 | Resetting |
| 3 | Idle |
| 4 | Stopped |
| 5 | Restoring |
| 6 | Saving |

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Execution.GetModelStatus

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-author.html language=enus -->
## TOPIC 03144: Author

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-author.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-author.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Model author. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string Author { get; private set; }

### Author

Model author.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string Author { get; private set; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmiversion.html language=enus -->
## TOPIC 03145: FmiVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmiversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmiversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: FMI version. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string FmiVersion { get; set; }

### FmiVersion

FMI version.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string FmiVersion { get; set; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmufilesize.html language=enus -->
## TOPIC 03146: FmuFileSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmufilesize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmufilesize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Model file size. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic int FmuFileSize { get; }

### FmuFileSize

Model file size.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public int FmuFileSize { get; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmumodeldescriptor__string.html language=enus -->
## TOPIC 03147: FmuModelDescriptor(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmumodeldescriptor__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-fmumodeldescriptor__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the FmuModelDescriptor class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic FmuModelDescriptor(string modelPath)ParametersNameTypeDescriptionmodelPathstringModel File Path

### FmuModelDescriptor(string)

Initializes a new instance of the [FmuModelDescriptor](nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public FmuModelDescriptor(string modelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelPath | string | Model File Path |

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-generationtool.html language=enus -->
## TOPIC 03148: GenerationTool

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-generationtool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-generationtool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Model generation tool. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string GenerationTool { get; set; }

### GenerationTool

Model generation tool.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string GenerationTool { get; set; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modeldescription.html language=enus -->
## TOPIC 03149: ModelDescription

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modeldescription.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modeldescription.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Description of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string ModelDescription { get; private set; }

### ModelDescription

Description of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string ModelDescription { get; private set; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelgenerationtoolchainversion.html language=enus -->
## TOPIC 03150: ModelGenerationToolchainVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelgenerationtoolchainversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelgenerationtoolchainversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the tool that was used to generate the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic Version ModelGenerationToolchainVersion { get; private set; }

### ModelGenerationToolchainVersion

Version of the tool that was used to generate the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public Version ModelGenerationToolchainVersion { get; private set; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelname.html language=enus -->
## TOPIC 03151: ModelName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Name of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string ModelName { get; private set; }

### ModelName

Name of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string ModelName { get; private set; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelversion.html language=enus -->
## TOPIC 03152: ModelVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-modelversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic Version ModelVersion { get; private set; }

### ModelVersion

Version of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public Version ModelVersion { get; private set; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-targetplatforms.html language=enus -->
## TOPIC 03153: TargetPlatforms

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-targetplatforms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor-targetplatforms.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Target platforms supported by the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic IEnumerable< string > TargetPlatforms { get; set; }

### TargetPlatforms

Target platforms supported by the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public IEnumerable< string > TargetPlatforms { get; set; }

Parent topic:

FmuModelDescriptor Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor.html language=enus -->
## TOPIC 03154: FmuModelDescriptor Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-fmumodeldescriptor.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Holds information from the model descriptor. Derives fromIModelDescriptorSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic class FmuModelDescriptor : IModelDescriptorConstructorsNameDescriptionFmuModelDescriptor(string)Initializes a new instance of the FmuModelDes

### FmuModelDescriptor Class

Holds information from the model descriptor.

#### Derives from

- IModelDescriptor

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public class FmuModelDescriptor : IModelDescriptor

#### Constructors

| Name | Description |
| --- | --- |
| FmuModelDescriptor(string) | Initializes a new instance of the FmuModelDescriptor class. |

#### Properties

| Name | Description |
| --- | --- |
| Author | Model author. |
| FmiVersion | FMI version. |
| FmuFileSize | Model file size. |
| GenerationTool | Model generation tool. |
| ModelDescription | Description of the model. |
| ModelGenerationToolchainVersion | Version of the tool that was used to generate the model. |
| ModelName | Name of the model. |
| ModelVersion | Version of the model. |
| TargetPlatforms | Target platforms supported by the model. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-author.html language=enus -->
## TOPIC 03155: Author

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-author.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-author.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Model author. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string Author { get; }

### Author

Model author.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string Author { get; }

Parent topic:

IModelDescriptor Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modeldescription.html language=enus -->
## TOPIC 03156: ModelDescription

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modeldescription.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modeldescription.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Description of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string ModelDescription { get; }

### ModelDescription

Description of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string ModelDescription { get; }

Parent topic:

IModelDescriptor Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelgenerationtoolchainversion.html language=enus -->
## TOPIC 03157: ModelGenerationToolchainVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelgenerationtoolchainversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelgenerationtoolchainversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the tool that was used to generate the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic Version ModelGenerationToolchainVersion { get; }

### ModelGenerationToolchainVersion

Version of the tool that was used to generate the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public Version ModelGenerationToolchainVersion { get; }

Parent topic:

IModelDescriptor Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelname.html language=enus -->
## TOPIC 03158: ModelName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Name of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string ModelName { get; }

### ModelName

Name of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string ModelName { get; }

Parent topic:

IModelDescriptor Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelversion.html language=enus -->
## TOPIC 03159: ModelVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-modelversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic Version ModelVersion { get; }

### ModelVersion

Version of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public Version ModelVersion { get; }

Parent topic:

IModelDescriptor Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-targetplatforms.html language=enus -->
## TOPIC 03160: TargetPlatforms

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-targetplatforms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor-targetplatforms.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Target platforms supported by the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic IEnumerable< string > TargetPlatforms { get; }

### TargetPlatforms

Target platforms supported by the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public IEnumerable< string > TargetPlatforms { get; }

Parent topic:

IModelDescriptor Interface

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor.html language=enus -->
## TOPIC 03161: IModelDescriptor Interface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-imodeldescriptor.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Holds information from the model descriptor. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic interface IModelDescriptorPropertiesNameDescriptionAuthorModel author. ModelDescriptionDescription of the model. ModelGenerationToolchainVersionVersion o

### IModelDescriptor Interface

Holds information from the model descriptor.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public interface IModelDescriptor

#### Properties

| Name | Description |
| --- | --- |
| Author | Model author. |
| ModelDescription | Description of the model. |
| ModelGenerationToolchainVersion | Version of the tool that was used to generate the model. |
| ModelName | Name of the model. |
| ModelVersion | Version of the model. |
| TargetPlatforms | Target platforms supported by the model. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-datatype.html language=enus -->
## TOPIC 03162: DataType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-datatype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-datatype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly int DataType

### DataType

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly int DataType

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-dims.html language=enus -->
## TOPIC 03163: Dims

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-dims.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-dims.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic int[] Dims { get; }

### Dims

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public int[] Dims { get; }

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-enumclassname.html language=enus -->
## TOPIC 03164: EnumClassName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-enumclassname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-enumclassname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: EnumClassName for parameters. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string EnumClassName

### EnumClassName

EnumClassName for parameters.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string EnumClassName

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-enumvaluetable.html language=enus -->
## TOPIC 03165: EnumValueTable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-enumvaluetable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-enumvaluetable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: EnumValueTable for parameters. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic IList< Tuple< string, int > > EnumValueTable { get; set; }

### EnumValueTable

EnumValueTable for parameters.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public IList< Tuple< string, int > > EnumValueTable { get; set; }

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-id.html language=enus -->
## TOPIC 03166: ID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-id.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-id.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string ID

### ID

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string ID

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-idx.html language=enus -->
## TOPIC 03167: Idx

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-idx.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-idx.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly int Idx

### Idx

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly int Idx

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-modelparamtype__int-string-string-int-int_arr1-double_arr1-ilist_tuple_string-int__-string.html language=enus -->
## TOPIC 03168: ModelParamType(int, string, string, int, int[], double[], IList< Tuple< string, int > >, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-modelparamtype__int-string-string-int-int_arr1-double_arr1-ilist_tuple_string-int__-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-modelparamtype__int-string-string-int-int_arr1-double_arr1-ilist_tuple_string-int__-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overload Constructor to set EnumValueTable for parameters. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic ModelParamType(int idx, string id, string name, int type, int[] dims, double[] value, IList< Tuple< string, int > > enumValueTable, string enumClassName)

### ModelParamType(int, string, string, int, int[], double[], IList< Tuple< string, int > >, string)

Overload Constructor to set EnumValueTable for parameters.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public ModelParamType(int idx, string id, string name, int type, int[] dims, double[] value, IList< Tuple< string, int > > enumValueTable, string enumClassName)

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-modelparamtype__int-string-string-int-int_arr1-double_arr1.html language=enus -->
## TOPIC 03169: ModelParamType(int, string, string, int, int[], double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-modelparamtype__int-string-string-int-int_arr1-double_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-modelparamtype__int-string-string-int-int_arr1-double_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic ModelParamType(int idx, string id, string name, int type, int[] dims, double[] value)

### ModelParamType(int, string, string, int, int[], double[])

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public ModelParamType(int idx, string id, string name, int type, int[] dims, double[] value)

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-name.html language=enus -->
## TOPIC 03170: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string Name

### Name

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string Name

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-value.html language=enus -->
## TOPIC 03171: Value

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-value.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype-value.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic double[] Value { get; }

### Value

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public double[] Value { get; }

Parent topic:

ModelParamType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype.html language=enus -->
## TOPIC 03172: ModelParamType Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelparamtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. Wraps model parameter information. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic class ModelParamTypeRemarksThis class is reserved for internal use. Thread SafetyAny members of this type are not guaranteed to be threa

### ModelParamType Class

RESERVED FOR INTERNAL USE. Wraps model parameter information.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public class ModelParamType

#### Remarks

Note

This class is reserved for internal use.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ModelParamType(int, string, string, int, int[], double[], IList< Tuple< string, int > >, string) | Overload Constructor to set EnumValueTable for parameters. |
| ModelParamType(int, string, string, int, int[], double[]) | RESERVED FOR INTERNAL USE. |

#### Fields

| Name | Description |
| --- | --- |
| DataType | RESERVED FOR INTERNAL USE. |
| EnumClassName | EnumClassName for parameters. |
| ID | RESERVED FOR INTERNAL USE. |
| Idx | RESERVED FOR INTERNAL USE. |
| Name | RESERVED FOR INTERNAL USE. |

#### Properties

| Name | Description |
| --- | --- |
| Dims | RESERVED FOR INTERNAL USE. |
| EnumValueTable | EnumValueTable for parameters. |
| Value | RESERVED FOR INTERNAL USE. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-dims.html language=enus -->
## TOPIC 03173: Dims

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-dims.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-dims.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic int[] Dims { get; }

### Dims

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public int[] Dims { get; }

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-enumclassname.html language=enus -->
## TOPIC 03174: EnumClassName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-enumclassname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-enumclassname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: EnumClassName for inports and outports. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string EnumClassName

### EnumClassName

EnumClassName for inports and outports.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string EnumClassName

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-enumvaluetable.html language=enus -->
## TOPIC 03175: EnumValueTable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-enumvaluetable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-enumvaluetable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: EnumValueTable for inports and outports. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic IList< Tuple< string, int > > EnumValueTable { get; set; }

### EnumValueTable

EnumValueTable for inports and outports.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public IList< Tuple< string, int > > EnumValueTable { get; set; }

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-index.html language=enus -->
## TOPIC 03176: Index

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-index.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-index.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly int Index

### Index

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly int Index

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-isinput.html language=enus -->
## TOPIC 03177: IsInput

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-isinput.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-isinput.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly bool IsInput

### IsInput

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly bool IsInput

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-modelporttype__string-int-int-bool-int_arr1-ilist_tuple_string-int__-string.html language=enus -->
## TOPIC 03178: ModelPortType(string, int, int, bool, int[], IList< Tuple< string, int > >, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-modelporttype__string-int-int-bool-int_arr1-ilist_tuple_string-int__-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-modelporttype__string-int-int-bool-int_arr1-ilist_tuple_string-int__-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overload Constructor to set EnumValueTable for inports and outports. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic ModelPortType(string name, int index, int taskID, bool isInput, int[] dims, IList< Tuple< string, int > > enumValueTable, string enumClassName)

### ModelPortType(string, int, int, bool, int[], IList< Tuple< string, int > >, string)

Overload Constructor to set EnumValueTable for inports and outports.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public ModelPortType(string name, int index, int taskID, bool isInput, int[] dims, IList< Tuple< string, int > > enumValueTable, string enumClassName)

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-modelporttype__string-int-int-bool-int_arr1.html language=enus -->
## TOPIC 03179: ModelPortType(string, int, int, bool, int[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-modelporttype__string-int-int-bool-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-modelporttype__string-int-int-bool-int_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic ModelPortType(string name, int index, int taskID, bool isInput, int[] dims)

### ModelPortType(string, int, int, bool, int[])

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public ModelPortType(string name, int index, int taskID, bool isInput, int[] dims)

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-name.html language=enus -->
## TOPIC 03180: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string Name

### Name

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string Name

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-taskid.html language=enus -->
## TOPIC 03181: TaskID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-taskid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype-taskid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly int TaskID

### TaskID

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly int TaskID

Parent topic:

ModelPortType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype.html language=enus -->
## TOPIC 03182: ModelPortType Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelporttype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. Wraps model port information. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic class ModelPortTypeRemarksThis class is reserved for internal use. Thread SafetyAny members of this type are not guaranteed to be thread safe

### ModelPortType Class

RESERVED FOR INTERNAL USE. Wraps model port information.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public class ModelPortType

#### Remarks

Note

This class is reserved for internal use.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ModelPortType(string, int, int, bool, int[], IList< Tuple< string, int > >, string) | Overload Constructor to set EnumValueTable for inports and outports. |
| ModelPortType(string, int, int, bool, int[]) | RESERVED FOR INTERNAL USE. |

#### Fields

| Name | Description |
| --- | --- |
| EnumClassName | EnumClassName for inports and outports. |
| Index | RESERVED FOR INTERNAL USE. |
| IsInput | RESERVED FOR INTERNAL USE. |
| Name | RESERVED FOR INTERNAL USE. |
| TaskID | RESERVED FOR INTERNAL USE. |

#### Properties

| Name | Description |
| --- | --- |
| Dims | RESERVED FOR INTERNAL USE. |
| EnumValueTable | EnumValueTable for inports and outports. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-blockname.html language=enus -->
## TOPIC 03183: BlockName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-blockname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-blockname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string BlockName

### BlockName

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string BlockName

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-datatype.html language=enus -->
## TOPIC 03184: DataType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-datatype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-datatype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly int DataType

### DataType

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly int DataType

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-dims.html language=enus -->
## TOPIC 03185: Dims

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-dims.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-dims.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic int[] Dims { get; }

### Dims

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public int[] Dims { get; }

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-enumclassname.html language=enus -->
## TOPIC 03186: EnumClassName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-enumclassname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-enumclassname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: EnumClassName for signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string EnumClassName

### EnumClassName

EnumClassName for signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string EnumClassName

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-enumvaluetable.html language=enus -->
## TOPIC 03187: EnumValueTable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-enumvaluetable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-enumvaluetable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: EnumValueTable for signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic IList< Tuple< string, int > > EnumValueTable { get; set; }

### EnumValueTable

EnumValueTable for signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public IList< Tuple< string, int > > EnumValueTable { get; set; }

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-id.html language=enus -->
## TOPIC 03188: ID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-id.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-id.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string ID

### ID

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string ID

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-idx.html language=enus -->
## TOPIC 03189: Idx

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-idx.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-idx.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly int Idx

### Idx

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly int Idx

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-modelsignaltype__int-string-string-string-int-int-int_arr1-ilist_tuple_string-int__-string.html language=enus -->
## TOPIC 03190: ModelSignalType(int, string, string, string, int, int, int[], IList< Tuple< string, int > >, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-modelsignaltype__int-string-string-string-int-int-int_arr1-ilist_tuple_string-int__-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-modelsignaltype__int-string-string-string-int-int-int_arr1-ilist_tuple_string-int__-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Overload Constructor to set EnumValueTable for signals. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic ModelSignalType(int idx, string id, string name, string blockName, int portNumber, int datatype, int[] dims, IList< Tuple< string, int > > enumValueTable, str

### ModelSignalType(int, string, string, string, int, int, int[], IList< Tuple< string, int > >, string)

Overload Constructor to set EnumValueTable for signals.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public ModelSignalType(int idx, string id, string name, string blockName, int portNumber, int datatype, int[] dims, IList< Tuple< string, int > > enumValueTable, string enumClassName)

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-modelsignaltype__int-string-string-string-int-int-int_arr1.html language=enus -->
## TOPIC 03191: ModelSignalType(int, string, string, string, int, int, int[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-modelsignaltype__int-string-string-string-int-int-int_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-modelsignaltype__int-string-string-string-int-int-int_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic ModelSignalType(int idx, string id, string name, string blockName, int portNumber, int datatype, int[] dims)

### ModelSignalType(int, string, string, string, int, int, int[])

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public ModelSignalType(int idx, string id, string name, string blockName, int portNumber, int datatype, int[] dims)

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-name.html language=enus -->
## TOPIC 03192: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly string Name

### Name

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly string Name

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-portnumber.html language=enus -->
## TOPIC 03193: PortNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-portnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype-portnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic readonly int PortNumber

### PortNumber

RESERVED FOR INTERNAL USE.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public readonly int PortNumber

Parent topic:

ModelSignalType Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype.html language=enus -->
## TOPIC 03194: ModelSignalType Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-modelsignaltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: RESERVED FOR INTERNAL USE. Wraps signal info from a model. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic class ModelSignalTypeRemarksThis class is reserved for internal use. Thread SafetyAny members of this type are not guaranteed to be thread

### ModelSignalType Class

RESERVED FOR INTERNAL USE. Wraps signal info from a model.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public class ModelSignalType

#### Remarks

Note

This class is reserved for internal use.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ModelSignalType(int, string, string, string, int, int, int[], IList< Tuple< string, int > >, string) | Overload Constructor to set EnumValueTable for signals. |
| ModelSignalType(int, string, string, string, int, int, int[]) | RESERVED FOR INTERNAL USE. |

#### Fields

| Name | Description |
| --- | --- |
| BlockName | RESERVED FOR INTERNAL USE. |
| DataType | RESERVED FOR INTERNAL USE. |
| EnumClassName | EnumClassName for signals. |
| ID | RESERVED FOR INTERNAL USE. |
| Idx | RESERVED FOR INTERNAL USE. |
| Name | RESERVED FOR INTERNAL USE. |
| PortNumber | RESERVED FOR INTERNAL USE. |

#### Properties

| Name | Description |
| --- | --- |
| Dims | RESERVED FOR INTERNAL USE. |
| EnumValueTable | EnumValueTable for signals. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-baudrate.html language=enus -->
## TOPIC 03195: BaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-baudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-baudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CAN baud rate. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic ulong BaudRate { get; set; }

### BaudRate

Gets or sets the CAN baud rate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public ulong BaudRate { get; set; }

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-brsbaudrate.html language=enus -->
## TOPIC 03196: BRSBaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-brsbaudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-brsbaudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CAN-BRS baud rate. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic ulong BRSBaudRate { get; set; }

### BRSBaudRate

Gets or sets the CAN-BRS baud rate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public ulong BRSBaudRate { get; set; }

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-canconfiguration.html language=enus -->
## TOPIC 03197: CANConfiguration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-canconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-canconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterless constructor for CAN Configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic CANConfiguration()

### CANConfiguration()

Parameterless constructor for CAN Configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public CANConfiguration()

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-canconfiguration__icanconfiguration.html language=enus -->
## TOPIC 03198: CANConfiguration(ICANConfiguration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-canconfiguration__icanconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-canconfiguration__icanconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterized constructor for CAN Configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic CANConfiguration(ICANConfiguration other)ParametersNameTypeDescriptionotherICANConfigurationExported CAN Cluster Configuration

### CANConfiguration(ICANConfiguration)

Parameterized constructor for CAN Configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public CANConfiguration(ICANConfiguration other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | ICANConfiguration | Exported CAN Cluster Configuration |

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-connecttorealnetwork.html language=enus -->
## TOPIC 03199: ConnectToRealNetwork

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-connecttorealnetwork.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-connecttorealnetwork.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Value indicating whether to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic bool ConnectToRealNetwork { get; set; }

### ConnectToRealNetwork

Value indicating whether to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public bool ConnectToRealNetwork { get; set; }

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-databasealias.html language=enus -->
## TOPIC 03200: DatabaseAlias

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-databasealias.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-databasealias.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database alias value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string DatabaseAlias { get; set; }

### DatabaseAlias

Database alias value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string DatabaseAlias { get; set; }

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-fdisomode.html language=enus -->
## TOPIC 03201: FDISOMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-fdisomode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-fdisomode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CAN FDISOMode. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic FDISOMode FDISOMode { get; set; }

### FDISOMode

Gets or sets the CAN [FDISOMode](nationalinstruments-veristand-systemdefinitionapi-fdisomode.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public [FDISOMode](nationalinstruments-veristand-systemdefinitionapi-fdisomode.html) FDISOMode { get; set; }

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-iomode.html language=enus -->
## TOPIC 03202: IOMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-iomode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-iomode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CANIOMode. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic CANIOMode IOMode { get; set; }

### IOMode

Gets or sets the [CANIOMode](nationalinstruments-veristand-systemdefinitionapi-caniomode.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public [CANIOMode](nationalinstruments-veristand-systemdefinitionapi-caniomode.html) IOMode { get; set; }

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-transceivertype.html language=enus -->
## TOPIC 03203: TransceiverType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-transceivertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-transceivertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CANTransceiverType. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic CANTransceiverType TransceiverType { get; set; }

### TransceiverType

Gets or sets the [CANTransceiverType](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public [CANTransceiverType](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html) TransceiverType { get; set; }

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-usedatabase.html language=enus -->
## TOPIC 03204: UseDatabase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-usedatabase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-usedatabase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Value indicating whether to use a database. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic bool UseDatabase { get; set; }

### UseDatabase

Value indicating whether to use a database.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public bool UseDatabase { get; set; }

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-xnetinterface.html language=enus -->
## TOPIC 03205: XNETInterface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-xnetinterface.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration-xnetinterface.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET Interface to be used to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string XNETInterface { get; set; }RemarksUse MAX or Hardware Configuration Utility to view your available NI-XNET hardwar

### XNETInterface

Gets or sets the XNET Interface to be used to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string XNETInterface { get; set; }

#### Remarks

Use MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and interfaces.

Parent topic:

CANConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration.html language=enus -->
## TOPIC 03206: CANConfiguration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-canconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the configuration for CAN communication. Derives fromICANConfigurationSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic class CANConfiguration : ICANConfigurationConstructorsNameDescriptionCANConfiguration(ICANConfiguration)Parameteriz

### CANConfiguration Class

Represents the configuration for CAN communication.

#### Derives from

- ICANConfiguration

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public class CANConfiguration : ICANConfiguration

#### Constructors

| Name | Description |
| --- | --- |
| CANConfiguration(ICANConfiguration) | Parameterized constructor for CAN Configuration. |
| CANConfiguration() | Parameterless constructor for CAN Configuration. |

#### Properties

| Name | Description |
| --- | --- |
| BaudRate | Gets or sets the CAN baud rate. |
| BRSBaudRate | Gets or sets the CAN-BRS baud rate. |
| ConnectToRealNetwork | Value indicating whether to connect to the real network. |
| DatabaseAlias | Database alias value. |
| FDISOMode | Gets or sets the CAN FDISOMode. |
| IOMode | Gets or sets the CANIOMode. |
| TransceiverType | Gets or sets the CANTransceiverType. |
| UseDatabase | Value indicating whether to use a database. |
| XNETInterface | Gets or sets the XNET Interface to be used to connect to the real network. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-constants-ecunetworkclusterfileextension.html language=enus -->
## TOPIC 03207: ECUNetworkClusterFileExtension

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-constants-ecunetworkclusterfileextension.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-constants-ecunetworkclusterfileextension.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The default extension for ECU Network Cluster Configuration files. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic const string ECUNetworkClusterFileExtension

### ECUNetworkClusterFileExtension

The default extension for ECU Network Cluster Configuration files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public const string ECUNetworkClusterFileExtension

Parent topic:

Constants Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-constants.html language=enus -->
## TOPIC 03208: Constants Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-constants.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-constants.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains constants for VirtualECU. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic class ConstantsFieldsNameDescriptionECUNetworkClusterFileExtensionThe default extension for ECU Network Cluster Configuration files.

### Constants Class

Contains constants for VirtualECU.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public class Constants

#### Fields

| Name | Description |
| --- | --- |
| ECUNetworkClusterFileExtension | The default extension for ECU Network Cluster Configuration files. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-clustername.html language=enus -->
## TOPIC 03209: ClusterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-clustername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-clustername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the ECU Network Cluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string ClusterName { get; set; }RemarksSet the name of the silver virtual bus as cluster name when using virtual ECUs built using Synopsys Silver®

### ClusterName

Gets or sets the name of the ECU Network Cluster.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string ClusterName { get; set; }

#### Remarks

Set the name of the silver virtual bus as cluster name when using virtual ECUs built using Synopsys Silver®.

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-databasepath.html language=enus -->
## TOPIC 03210: DatabasePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-databasepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-databasepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string DatabasePath { get; set; }

### DatabasePath

Database path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string DatabasePath { get; set; }

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-deserializefrom__string-out.html language=enus -->
## TOPIC 03211: DeserializeFrom(string, out IECUNetworkClusterConfiguration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-deserializefrom__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-deserializefrom__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deserializes the ECUNetworkClusterConfiguration from a JSON file (.nivsecunw file). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic static Error DeserializeFrom(string filePath, out IECUNetworkClusterConfiguration clusterConfiguration)Parameter

### DeserializeFrom(string, out IECUNetworkClusterConfiguration)

Deserializes the [ECUNetworkClusterConfiguration](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration.html) from a JSON file (.nivsecunw file).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public static Error DeserializeFrom(string filePath, out IECUNetworkClusterConfiguration clusterConfiguration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The path to the JSON file from which the configuration will be loaded. |
| clusterConfiguration | out IECUNetworkClusterConfiguration | The deserialized ECU network cluster configuration. |

#### Returns

The error that prevented the deserialization of ECU network cluster configuration, if one occurred.

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-ecunetworkclusterconfiguration.html language=enus -->
## TOPIC 03212: ECUNetworkClusterConfiguration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-ecunetworkclusterconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-ecunetworkclusterconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterless constructor for cluster configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic ECUNetworkClusterConfiguration()

### ECUNetworkClusterConfiguration()

Parameterless constructor for cluster configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public ECUNetworkClusterConfiguration()

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-ecunetworkclusterconfiguration__iecunetworkclusterconfiguration.html language=enus -->
## TOPIC 03213: ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-ecunetworkclusterconfiguration__iecunetworkclusterconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-ecunetworkclusterconfiguration__iecunetworkclusterconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterized constructor for cluster configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration other)ParametersNameTypeDescriptionotherIECUNetworkClusterConfigurationExported

### ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration)

Parameterized constructor for cluster configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | IECUNetworkClusterConfiguration | Exported Ecu Cluster Configuration |

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-linmastermodellinuxpath.html language=enus -->
## TOPIC 03214: LINMasterModelLinuxPath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-linmastermodellinuxpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-linmastermodellinuxpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: LIN Master Model path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string LINMasterModelLinuxPath { get; set; }

### LINMasterModelLinuxPath

LIN Master Model path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string LINMasterModelLinuxPath { get; set; }

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-protocol.html language=enus -->
## TOPIC 03215: Protocol

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-protocol.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-protocol.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CommunicationProtocol used by the ECU network cluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic CommunicationProtocol Protocol { get; set; }

### Protocol

Gets or sets the [CommunicationProtocol](nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html) used by the ECU network cluster.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public [CommunicationProtocol](nationalinstruments-veristand-systemdefinitionapi-communicationprotocol.html) Protocol { get; set; }

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-serializeto__string.html language=enus -->
## TOPIC 03216: SerializeTo(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-serializeto__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-serializeto__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serialize the configuration to json file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic Error SerializeTo(string clusterConfigurationFilePath)ParametersNameTypeDescriptionclusterConfigurationFilePathstringECU Network Cluster Configuration Fil

### SerializeTo(string)

Serialize the configuration to json file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public Error SerializeTo(string clusterConfigurationFilePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| clusterConfigurationFilePath | string | ECU Network Cluster Configuration File Path. |

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-svbconfiguration.html language=enus -->
## TOPIC 03217: SVBConfiguration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-svbconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-svbconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the configuration for Synopsys Virtual Bus (SVB). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic SVBConfiguration SVBConfiguration { get; set; }

### SVBConfiguration

Represents the configuration for Synopsys Virtual Bus (SVB).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public [SVBConfiguration](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration.html) SVBConfiguration { get; set; }

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-timestep.html language=enus -->
## TOPIC 03218: TimeStep

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-timestep.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-timestep.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic double TimeStep { get; set; }RemarksWhen using virtual ECUs built usin

### TimeStep

Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public double TimeStep { get; set; }

#### Remarks

When using virtual ECUs built using Synopsys Silver, set the SVB Step Size to this property.

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-trydeserializefrom__string-out.html language=enus -->
## TOPIC 03219: TryDeserializeFrom(string, out IECUNetworkClusterConfiguration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-trydeserializefrom__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-trydeserializefrom__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Try deserializing the ECUNetworkClusterConfiguration from a JSON file (.nivsecunw file). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic static bool TryDeserializeFrom(string modelPath, out IECUNetworkClusterConfiguration ecuNetworkClusterConfi

### TryDeserializeFrom(string, out IECUNetworkClusterConfiguration)

Try deserializing the [ECUNetworkClusterConfiguration](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration.html) from a JSON file (.nivsecunw file).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public static bool TryDeserializeFrom(string modelPath, out IECUNetworkClusterConfiguration ecuNetworkClusterConfiguration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| modelPath | string | The path to the JSON file from which the configuration will be loaded. |
| ecuNetworkClusterConfiguration | out IECUNetworkClusterConfiguration | The deserialized ECU network cluster configuration. |

#### Returns

true if the desrialization is successful.

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-version.html language=enus -->
## TOPIC 03220: Version

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-version.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-version.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the json file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string Version { get; set; }

### Version

Version of the json file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string Version { get; set; }

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-virtualeculist.html language=enus -->
## TOPIC 03221: VirtualECUList

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-virtualeculist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-virtualeculist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Virtual ECUs that have been added to the cluster. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic IList< string > VirtualECUList { get; set; }

### VirtualECUList

Virtual ECUs that have been added to the cluster.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public IList< string > VirtualECUList { get; set; }

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-virtualecutoolchain.html language=enus -->
## TOPIC 03222: VirtualECUToolchain

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-virtualecutoolchain.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration-virtualecutoolchain.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the VirtualECUToolchain that was used to build virtual ECUs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic VirtualECUToolchain VirtualECUToolchain { get; set; }

### VirtualECUToolchain

Gets or sets the name of the [VirtualECUToolchain](nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html) that was used to build virtual ECUs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public [VirtualECUToolchain](nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html) VirtualECUToolchain { get; set; }

Parent topic:

ECUNetworkClusterConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration.html language=enus -->
## TOPIC 03223: ECUNetworkClusterConfiguration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ecunetworkclusterconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Class for serializing and de-serializing ECU network cluster configuration. Derives fromIECUNetworkClusterConfigurationSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic class ECUNetworkClusterConfiguration : IECUNetworkClusterConfigurationConstru

### ECUNetworkClusterConfiguration Class

Class for serializing and de-serializing ECU network cluster configuration.

#### Derives from

- IECUNetworkClusterConfiguration

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public class ECUNetworkClusterConfiguration : IECUNetworkClusterConfiguration

#### Constructors

| Name | Description |
| --- | --- |
| ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration) | Parameterized constructor for cluster configuration. |
| ECUNetworkClusterConfiguration() | Parameterless constructor for cluster configuration. |

#### Properties

| Name | Description |
| --- | --- |
| ClusterName | Gets or sets the name of the ECU Network Cluster. |
| DatabasePath | Database path. |
| LINMasterModelLinuxPath | LIN Master Model path. |
| Protocol | Gets or sets the CommunicationProtocol used by the ECU network cluster. |
| SVBConfiguration | Represents the configuration for Synopsys Virtual Bus (SVB). |
| TimeStep | Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs. |
| Version | Version of the json file. |
| VirtualECUList | Virtual ECUs that have been added to the cluster. |
| VirtualECUToolchain | Gets or sets the name of the VirtualECUToolchain that was used to build virtual ECUs. |

#### Methods

| Name | Description |
| --- | --- |
| SerializeTo(string) | Serialize the configuration to json file. |
| DeserializeFrom(string, out IECUNetworkClusterConfiguration) | Deserializes the ECUNetworkClusterConfiguration from a JSON file (.nivsecunw file). |
| TryDeserializeFrom(string, out IECUNetworkClusterConfiguration) | Try deserializing the ECUNetworkClusterConfiguration from a JSON file (.nivsecunw file). |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-connecttorealnetwork.html language=enus -->
## TOPIC 03224: ConnectToRealNetwork

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-connecttorealnetwork.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-connecttorealnetwork.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Value indicating whether to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic bool ConnectToRealNetwork { get; set; }

### ConnectToRealNetwork

Value indicating whether to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public bool ConnectToRealNetwork { get; set; }

Parent topic:

EthernetConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-ethernetconfiguration.html language=enus -->
## TOPIC 03225: EthernetConfiguration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-ethernetconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-ethernetconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterless constructor for Ethernet Configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic EthernetConfiguration()

### EthernetConfiguration()

Parameterless constructor for Ethernet Configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public EthernetConfiguration()

Parent topic:

EthernetConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-ethernetconfiguration__iethernetconfiguration.html language=enus -->
## TOPIC 03226: EthernetConfiguration(IEthernetConfiguration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-ethernetconfiguration__iethernetconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-ethernetconfiguration__iethernetconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterized constructor for Ethernet Configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic EthernetConfiguration(IEthernetConfiguration other)ParametersNameTypeDescriptionotherIEthernetConfigurationExported Ethernet Cluster Configura

### EthernetConfiguration(IEthernetConfiguration)

Parameterized constructor for Ethernet Configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public EthernetConfiguration(IEthernetConfiguration other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | IEthernetConfiguration | Exported Ethernet Cluster Configuration |

Parent topic:

EthernetConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-virtualecumacaddresses.html language=enus -->
## TOPIC 03227: VirtualECUMACAddresses

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-virtualecumacaddresses.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-virtualecumacaddresses.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Virtual ECU MAC Addresses. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic IList< string > VirtualECUMACAddresses { get; set; }

### VirtualECUMACAddresses

Virtual ECU MAC Addresses.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public IList< string > VirtualECUMACAddresses { get; set; }

Parent topic:

EthernetConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-xnetinterface.html language=enus -->
## TOPIC 03228: XNETInterface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-xnetinterface.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration-xnetinterface.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET Interface to be used to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string XNETInterface { get; set; }RemarksUse MAX or Hardware Configuration Utility to view your available NI-XNET hardwar

### XNETInterface

Gets or sets the XNET Interface to be used to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string XNETInterface { get; set; }

#### Remarks

Use MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and interfaces.

Parent topic:

EthernetConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration.html language=enus -->
## TOPIC 03229: EthernetConfiguration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-ethernetconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the configuration for Ethernet communication. Derives fromIEthernetConfigurationSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic class EthernetConfiguration : IEthernetConfigurationConstructorsNameDescriptionEthernetConfiguration(IEth

### EthernetConfiguration Class

Represents the configuration for Ethernet communication.

#### Derives from

- IEthernetConfiguration

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public class EthernetConfiguration : IEthernetConfiguration

#### Constructors

| Name | Description |
| --- | --- |
| EthernetConfiguration(IEthernetConfiguration) | Parameterized constructor for Ethernet Configuration. |
| EthernetConfiguration() | Parameterless constructor for Ethernet Configuration. |

#### Properties

| Name | Description |
| --- | --- |
| ConnectToRealNetwork | Value indicating whether to connect to the real network. |
| VirtualECUMACAddresses | Virtual ECU MAC Addresses. |
| XNETInterface | Gets or sets the XNET Interface to be used to connect to the real network. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-baudrate.html language=enus -->
## TOPIC 03230: BaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-baudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-baudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the LIN baud rate. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic ulong BaudRate { get; set; }

### BaudRate

Gets or sets the LIN baud rate.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public ulong BaudRate { get; set; }

Parent topic:

LINConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-connecttorealnetwork.html language=enus -->
## TOPIC 03231: ConnectToRealNetwork

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-connecttorealnetwork.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-connecttorealnetwork.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Value indicating whether to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic bool ConnectToRealNetwork { get; set; }

### ConnectToRealNetwork

Value indicating whether to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public bool ConnectToRealNetwork { get; set; }

Parent topic:

LINConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-databasealias.html language=enus -->
## TOPIC 03232: DatabaseAlias

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-databasealias.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-databasealias.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Database alias value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string DatabaseAlias { get; set; }

### DatabaseAlias

Database alias value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string DatabaseAlias { get; set; }

Parent topic:

LINConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-linconfiguration.html language=enus -->
## TOPIC 03233: LINConfiguration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-linconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-linconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterless constructor for LIN Configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic LINConfiguration()

### LINConfiguration()

Parameterless constructor for LIN Configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public LINConfiguration()

Parent topic:

LINConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-linconfiguration__ilinconfiguration.html language=enus -->
## TOPIC 03234: LINConfiguration(ILINConfiguration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-linconfiguration__ilinconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-linconfiguration__ilinconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterized constructor for LIN Configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic LINConfiguration(ILINConfiguration other)ParametersNameTypeDescriptionotherILINConfigurationExported LIN Cluster Configuration

### LINConfiguration(ILINConfiguration)

Parameterized constructor for LIN Configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public LINConfiguration(ILINConfiguration other)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| other | ILINConfiguration | Exported LIN Cluster Configuration |

Parent topic:

LINConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-usedatabase.html language=enus -->
## TOPIC 03235: UseDatabase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-usedatabase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-usedatabase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Value indicating whether to use a database. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic bool UseDatabase { get; set; }

### UseDatabase

Value indicating whether to use a database.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public bool UseDatabase { get; set; }

Parent topic:

LINConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-virtualtxframeids.html language=enus -->
## TOPIC 03236: VirtualTxFrameIDs

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-virtualtxframeids.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-virtualtxframeids.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Virtual transmission frame IDs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic IList< int > VirtualTxFrameIDs { get; set; }

### VirtualTxFrameIDs

Virtual transmission frame IDs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public IList< int > VirtualTxFrameIDs { get; set; }

Parent topic:

LINConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-xnetinterface.html language=enus -->
## TOPIC 03237: XNETInterface

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-xnetinterface.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration-xnetinterface.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET Interface to be used to connect to the real network. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic string XNETInterface { get; set; }RemarksUse MAX or Hardware Configuration Utility to view your available NI-XNET hardwar

### XNETInterface

Gets or sets the XNET Interface to be used to connect to the real network.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public string XNETInterface { get; set; }

#### Remarks

Use MAX or Hardware Configuration Utility to view your available NI-XNET hardware, including all devices and interfaces.

Parent topic:

LINConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration.html language=enus -->
## TOPIC 03238: LINConfiguration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-linconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the configuration for LIN communication. Derives fromILINConfigurationSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic class LINConfiguration : ILINConfigurationConstructorsNameDescriptionLINConfiguration(ILINConfiguration)Parameteriz

### LINConfiguration Class

Represents the configuration for LIN communication.

#### Derives from

- ILINConfiguration

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public class LINConfiguration : ILINConfiguration

#### Constructors

| Name | Description |
| --- | --- |
| LINConfiguration(ILINConfiguration) | Parameterized constructor for LIN Configuration. |
| LINConfiguration() | Parameterless constructor for LIN Configuration. |

#### Properties

| Name | Description |
| --- | --- |
| BaudRate | Gets or sets the LIN baud rate. |
| ConnectToRealNetwork | Value indicating whether to connect to the real network. |
| DatabaseAlias | Database alias value. |
| UseDatabase | Value indicating whether to use a database. |
| VirtualTxFrameIDs | Virtual transmission frame IDs. |
| XNETInterface | Gets or sets the XNET Interface to be used to connect to the real network. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration-rxfifocapacity.html language=enus -->
## TOPIC 03239: RxFifoCapacity

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration-rxfifocapacity.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration-rxfifocapacity.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Number of frames that can be buffered by the controller's Rx FIFO. If Rx Fifo Capacity is not set, the default capacity is either 2048 or other value set by V-ECUs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic int RxFifoCapacity { get; set;

### RxFifoCapacity

Number of frames that can be buffered by the controller's Rx FIFO.

Note

If Rx Fifo Capacity is not set, the default capacity is either 2048 or other value set by V-ECUs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public int RxFifoCapacity { get; set; }

Parent topic:

SVBConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration-svbconfiguration.html language=enus -->
## TOPIC 03240: SVBConfiguration()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration-svbconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration-svbconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Parameterless constructor for SVB Configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic SVBConfiguration()

### SVBConfiguration()

Parameterless constructor for SVB Configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public SVBConfiguration()

Parent topic:

SVBConfiguration Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration.html language=enus -->
## TOPIC 03241: SVBConfiguration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport-svbconfiguration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the configuration for Synopsys Virtual Bus (SVB). Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupportpublic class SVBConfigurationConstructorsNameDescriptionSVBConfiguration()Parameterless constructor for SVB Configuration. Pro

### SVBConfiguration Class

Represents the configuration for Synopsys Virtual Bus (SVB).

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html)

public class SVBConfiguration

#### Constructors

| Name | Description |
| --- | --- |
| SVBConfiguration() | Parameterless constructor for SVB Configuration. |

#### Properties

| Name | Description |
| --- | --- |
| RxFifoCapacity | Number of frames that can be buffered by the controller's Rx FIFO. Note If Rx Fifo Capacity is not set, the default capacity is either 2048 or other value set by V-ECUs. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html language=enus -->
## TOPIC 03242: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-virtualecusupport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: ClassesNameDescriptionCANConfigurationRepresents the configuration for CAN communication. ConstantsContains constants for VirtualECU. ECUNetworkClusterConfigurationClass for serializing and de-serializing ECU network cluster configuration. EthernetConfigurationRepresents the configuration for Ethern

### NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport

#### Classes

| Name | Description |
| --- | --- |
| CANConfiguration | Represents the configuration for CAN communication. |
| Constants | Contains constants for VirtualECU. |
| ECUNetworkClusterConfiguration | Class for serializing and de-serializing ECU network cluster configuration. |
| EthernetConfiguration | Represents the configuration for Ethernet communication. |
| LINConfiguration | Represents the configuration for LIN communication. |
| SVBConfiguration | Represents the configuration for Synopsys Virtual Bus (SVB). |

#### Interfaces

None

#### Structures

None

#### Enumerations

None

#### Delegates

None

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-author.html language=enus -->
## TOPIC 03243: Author

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-author.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-author.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Author of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string Author { get; private set; }

### Author

Author of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string Author { get; private set; }

Parent topic:

VsModelDescriptorExtended Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-deserializefrom__streamreader.html language=enus -->
## TOPIC 03244: DeserializeFrom(StreamReader)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-deserializefrom__streamreader.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-deserializefrom__streamreader.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates extended vsmodel descriptor from the file stream of the json descriptor. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic static VsModelDescriptorExtended DeserializeFrom(StreamReader streamReader)ParametersNameTypeDescriptionstreamReaderStreamReaderFile

### DeserializeFrom(StreamReader)

Creates extended vsmodel descriptor from the file stream of the json descriptor.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public static [VsModelDescriptorExtended](nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended.html) DeserializeFrom(StreamReader streamReader)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| streamReader | StreamReader | File stream that contains the json descriptor |

Parent topic:

VsModelDescriptorExtended Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-enumvaluetablebyenumclassname.html language=enus -->
## TOPIC 03245: EnumValueTableByEnumClassName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-enumvaluetablebyenumclassname.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-enumvaluetablebyenumclassname.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: EnumValueTable by enum class name of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic IReadOnlyDictionary< string, IList< Tuple< string, int > > > EnumValueTableByEnumClassName { get; set; }

### EnumValueTableByEnumClassName

EnumValueTable by enum class name of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public IReadOnlyDictionary< string, IList< Tuple< string, int > > > EnumValueTableByEnumClassName { get; set; }

Parent topic:

VsModelDescriptorExtended Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modeldescription.html language=enus -->
## TOPIC 03246: ModelDescription

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modeldescription.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modeldescription.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Description of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic string ModelDescription { get; private set; }

### ModelDescription

Description of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public string ModelDescription { get; private set; }

Parent topic:

VsModelDescriptorExtended Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modelgenerationtoolchainversion.html language=enus -->
## TOPIC 03247: ModelGenerationToolchainVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modelgenerationtoolchainversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modelgenerationtoolchainversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the tool that was used to generate the vsmodel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic Version ModelGenerationToolchainVersion { get; private set; }

### ModelGenerationToolchainVersion

Version of the tool that was used to generate the vsmodel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public [Version](nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeljsonfiledescriptor-version.html) ModelGenerationToolchainVersion { get; private set; }

Parent topic:

VsModelDescriptorExtended Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modelversion.html language=enus -->
## TOPIC 03248: ModelVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modelversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-modelversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Version of the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic Version ModelVersion { get; private set; }

### ModelVersion

Version of the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public [Version](nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeljsonfiledescriptor-version.html) ModelVersion { get; private set; }

Parent topic:

VsModelDescriptorExtended Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-targetplatforms.html language=enus -->
## TOPIC 03249: TargetPlatforms

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-targetplatforms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended-targetplatforms.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Target platforms supported by the model. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic IEnumerable< string > TargetPlatforms { get; private set; }

### TargetPlatforms

Target platforms supported by the model.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public IEnumerable< string > TargetPlatforms { get; private set; }

Parent topic:

VsModelDescriptorExtended Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended.html language=enus -->
## TOPIC 03250: VsModelDescriptorExtended Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-modelsupport-vsmodeldescriptorextended.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: VsModel descriptor containing both information needed for deserialization and other vsmodel properties. Derives fromVsModelJsonFileDescriptorIModelDescriptorSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupportpublic class VsModelDescriptorExtended : VsModelJsonFileDescript

### VsModelDescriptorExtended Class

VsModel descriptor containing both information needed for deserialization and other vsmodel properties.

#### Derives from

- VsModelJsonFileDescriptor
- IModelDescriptor

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport](nationalinstruments-veristand-systemdefinitionapi-modelsupport.html)

public class VsModelDescriptorExtended : VsModelJsonFileDescriptor, IModelDescriptor

#### Properties

| Name | Description |
| --- | --- |
| Author | Author of the model. |
| EnumValueTableByEnumClassName | EnumValueTable by enum class name of the model. |
| ModelDescription | Description of the model. |
| ModelGenerationToolchainVersion | Version of the tool that was used to generate the vsmodel. |
| ModelVersion | Version of the model. |
| TargetPlatforms | Target platforms supported by the model. |

#### Methods

| Name | Description |
| --- | --- |
| DeserializeFrom(StreamReader) | Creates extended vsmodel descriptor from the file stream of the json descriptor. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport
