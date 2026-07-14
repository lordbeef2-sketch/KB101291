# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=1501 end=1750 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-valueexprisignored.html language=enus -->
## TOPIC 01501: LabVIEWNXGParameter.ValueExprIsIgnored

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-valueexprisignored.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-valueexprisignored.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ValueExprIsIgnored Data Type Boolean Purpose Use this property to determine whether the LabVIEW Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameters that use default values. See Also LabVIE

### LabVIEWNXGParameter.ValueExprIsIgnored

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ValueExprIsIgnored

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the LabVIEW Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameters that use default values.

#### See Also

[LabVIEWNXGParameter.UseDefaultValue](labviewnxgparameter-usedefaultvalue.html)

[LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)

[LabVIEWNXGParameter.ValueExprIsOptional](labviewnxgparameter-valueexprisoptional.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-valueexprisoptional.html language=enus -->
## TOPIC 01502: LabVIEWNXGParameter.ValueExprIsOptional

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-valueexprisoptional.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-valueexprisoptional.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.ValueExprIsOptional Data Type Boolean Purpose Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for output parameters and value expres

### LabVIEWNXGParameter.ValueExprIsOptional

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).ValueExprIsOptional

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for output parameters and value expressions for cluster and array parameters that have parameter elements are optional.

#### See Also

[LabVIEWNXGParameter.Direction](labviewnxgparameter-direction.html)

[LabVIEWNXGParameter.ValueExpr](labviewnxgparameter-valueexpr.html)

[LabVIEWNXGParameter.ValueExprIsIgnored](labviewnxgparameter-valueexprisignored.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter-wirerequirement.html language=enus -->
## TOPIC 01503: LabVIEWNXGParameter.WireRequirement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter-wirerequirement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter-wirerequirement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameter.WireRequirement Data Type LabVIEWNXGParameterWireRequirements Use the following constants with this data type: LabVIEWNXGParamWireReq_Optional –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value. LabVIEWNXGParamWireR

### LabVIEWNXGParameter.WireRequirement

#### Syntax

[LabVIEWNXGParameter](labviewnxgparameter.html).WireRequirement

#### Data Type

[LabVIEWNXGParameterWireRequirements](labviewnxgparameterwirerequirements.html)

Use the following constants with this data type:

- LabVIEWNXGParamWireReq_Optional 
 –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value.
- LabVIEWNXGParamWireReq_Recommended 
 –(Value: 1) Indicates that the module can use the default value for the parameter. However, passing a value is recommended.
- LabVIEWNXGParamWireReq_Required 
 –(Value: 0) Indicates that the module must pass a value for the parameter.

#### Purpose

Indicates whether the parameter is required, recommended, or optional.

#### Remarks

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call
 [Module.LoadPrototype](module-loadprototype.html)
 before retrieving this property.

#### See Also

[LabVIEWNXGParameter.Direction](labviewnxgparameter-direction.html)

[LabVIEWNXGParameterWireRequirements](labviewnxgparameterwirerequirements.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameter.html language=enus -->
## TOPIC 01504: LabVIEWNXGParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNXGParameter class to configure and obtain LabVIEWNXGParameter -specific information for an item in the LabVIEWNXGParameters collection class. Properties ArrayDimensions (Read Only) ArrayElementPrototype (Read Only) Category (Read Only) ComplexImaginaryPartElement (Read O

### LabVIEWNXGParameter

Use objects from the
 LabVIEWNXGParameter
 class to configure and obtain
 LabVIEWNXGParameter
 -specific information for an item in the
 LabVIEWNXGParameters
 collection class.

#### Properties

| ArrayDimensions (Read Only) |
| --- |
| ArrayElementPrototype (Read Only) |
| Category (Read Only) |
| ComplexImaginaryPartElement (Read Only) |
| ComplexRealPartElement (Read Only) |
| DefaultValue (Read Only) |
| Description (Read Only) |
| Direction (Read Only) |
| DisplayType (Read Only) |
| Elements (Read Only) |
| GetArrayElementIndex (Read Only) |
| NodeUsesDefaultValue (Read Only) |
| ParameterName (Read Only) |
| PartiallySpecified (Read Only) |
| PassAsBinaryString |
| Type (Read Only) |
| TypeDisplayString (Read Only) |
| UseDefaultValue |
| UserData (Read Only) |
| ValidEvaluationTypes (Read Only) |
| ValueExpr |
| ValueExprIsIgnored (Read Only) |
| ValueExprIsOptional (Read Only) |
| WireRequirement (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| CreateDefaultArrayElements |
| DeleteArrayElement |
| DeleteArrayElements |
| DisplayCreateCustomDataTypeDialog |
| ExprClusterTypeMismatch |
| GetArrayIndex |
| GetDefaultArrayDimensionSize |
| GetEnumValues |
| InsertArrayElement |
| IsClusterMappingInvalid |
| IsParameterMappingValid |
| UpdateClusterMapping |

#### See Also

[LabVIEWNXGParameters](labviewnxgparameters.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparametercategories.html language=enus -->
## TOPIC 01505: LabVIEWNXGParameterCategories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparametercategories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparametercategories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data type of the NXG parameter. LabVIEWNXGParamCategory_Boolean –(Value: 2) Indicates that the parameter is a Boolean type This category does not have any associated data types. LabVIEWNXGParamCategory_BooleanArray –(Value: 52) Indicates that the parameter is an array of Boolean values

### LabVIEWNXGParameterCategories

Specifies the data type of the NXG parameter.

- LabVIEWNXGParamCategory_Boolean 
 –(Value: 2) Indicates that the parameter is a Boolean type This category does not have any associated data types.
- LabVIEWNXGParamCategory_BooleanArray 
 –(Value: 52) Indicates that the parameter is an array of Boolean values. This category does not have any associated data types.
- LabVIEWNXGParamCategory_Cluster 
 –(Value: 3) Indicates that the parameter is a cluster. Data types associated with this category include
 LabVIEWNXGParamType_DigitalWaveform 
 ,
 LabVIEWNXGParamType_ErrorOut 
 ,
 LabVIEWNXGParamType_IO 
 ,
 LabVIEWNXGParamType_StandardCluster 
 ,
 LabVIEWNXGParamType_AnalogWaveform 
 , and
 LabVIEWNXGParamType_DigitalWaveform 
 .
- LabVIEWNXGParamCategory_ClusterArray 
 –(Value: 53) Indicates that the parameter is an array of clusters. Data types associated with this category include
 LabVIEWNXGParamType_DigitalWaveform 
 ,
 LabVIEWNXGParamType_ErrorOut 
 ,
 LabVIEWNXGParamType_IO 
 ,
 LabVIEWNXGParamType_StandardCluster 
 , and
 LabVIEWNXGParamType_AnalogWaveform 
 .
- LabVIEWNXGParamCategory_Complex 
 –(Value: 6) Indicates that the parameter is a complex numeric data type. This category does not have any associated data types.
- LabVIEWNXGParamCategory_ComplexArray 
 –(Value: 55) Indicates that the parameter is an array of complex numbers. This category does not have any associated data types.
- LabVIEWNXGParamCategory_Enum 
 –(Value: 9) Indicates the parameter is an enumeration. This category does not have any associated data types.
- LabVIEWNXGParamCategory_EnumArray 
 –(Value: 58) Indicates the parameter is an array of enumerations. This category does not have any associated data types.
- LabVIEWNXGParamCategory_Numeric 
 –(Value: 0) Indicates that the parameter is a numeric data type. Numeric data types include enumerations, but do not include complex numbers. Data types associated with this category include
 LabVIEWNXGParamType_Ext 
 ,
 LabVIEWNXGParamType_Int16 
 ,
 LabVIEWNXGParamType_Int32 
 ,
 LabVIEWNXGParamType_Int64 
 ,
 LabVIEWNXGParamType_Int8 
 ,
 LabVIEWNXGParamType_Real32 
 ,
 LabVIEWNXGParamType_Real64 
 ,
 LabVIEWNXGParamType_UInt16 
 ,
 LabVIEWNXGParamType_UInt32 
 ,
 LabVIEWNXGParamType_UInt64 
 , and
 LabVIEWNXGParamType_UInt8 
 .
- LabVIEWNXGParamCategory_NumericArray 
 –(Value: 50) Indicates that the parameter is a an array of numbers. Numeric data types include enumerations, but do not include complex numbers. Data types associated with this category include
 LabVIEWNXGParamType_Ext 
 ,
 LabVIEWNXGParamType_Int16 
 ,
 LabVIEWNXGParamType_Int32 
 ,
 LabVIEWNXGParamType_Int64 
 ,
 LabVIEWNXGParamType_Int8 
 ,
 LabVIEWNXGParamType_Real32 
 ,
 LabVIEWNXGParamType_Real64 
 ,
 LabVIEWNXGParamType_UInt16 
 ,
 LabVIEWNXGParamType_UInt32 
 ,
 LabVIEWNXGParamType_UInt64 
 , and
 LabVIEWNXGParamType_UInt8 
 .
- LabVIEWNXGParamCategory_Reference 
 –(Value: 4) Indicates that the parameter is a reference. Data types associated with this category include
 LabVIEWNXGParamType_ActiveXRef 
 ,
 LabVIEWNXGParamType_OtherRef 
 , and
 LabVIEWNXGParamType_LVNXGObjectRef 
 but do not include
 LabVIEWNXGParamType_IO 
 , which is considered a cluster data type.
- LabVIEWNXGParamCategory_ReferenceArray 
 –(Value: 54) Indicates that the parameter is an array of COM references. Data types associated with this category include
 LabVIEWNXGParamType_ActiveXRef 
 ,
 LabVIEWNXGParamType_OtherRef 
 , and
 LabVIEWNXGParamType_LVNXGObjectRef 
 but do not include
 LabVIEWNXGParamType_IO 
 , which is considered a cluster data type.
- LabVIEWNXGParamCategory_String 
 –(Value: 1) Indicates that the parameter is a string data type. Data types associated with this category include
 LabVIEWNXGParamType_String 
 ,
 LabVIEWNXGParamType_PathString 
 , and
 LabVIEWNXGParamType_TimestampString 
 .
- LabVIEWNXGParamCategory_StringArray 
 –(Value: 51) Indicates that the parameter is an array of strings. Data types associated with this category include
 LabVIEWNXGParamType_BinaryString 
 ,
 LabVIEWNXGParamType_CString 
 ,
 LabVIEWNXGParamType_PathString 
 , and
 LabVIEWNXGParamType_TimestampString 
 .
- LabVIEWNXGParamCategory_Unknown 
 –(Value: 8) Indicates that the parameter has a data type TestStand does not recognize.
- LabVIEWNXGParamCategory_Variant 
 –(Value: 7) Indicates the parameter is a COM Variant. This category does not have any associated data types.
- LabVIEWNXGParamCategory_VariantArray 
 –(Value: 56) Indicates the parameter is an array of COM Variants. This category does not have any associated data types.

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameterdirections.html language=enus -->
## TOPIC 01506: LabVIEWNXGParameterDirections

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameterdirections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameterdirections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEWParameter.Direction property returns one of the following constants to indicate how the module passes the parameter when it executes. LabVIEWNXGParamDirection_In –(Value: 0) Indicates that the parameter is passed to the VI. LabVIEWNXGParamDirection_Out –(Value: 1) Indicates that the param

### LabVIEWNXGParameterDirections

The
 LabVIEWParameter.Direction
 property returns one of the following constants to indicate how the module passes the parameter when it executes.

- LabVIEWNXGParamDirection_In 
 –(Value: 0) Indicates that the parameter is passed to the VI.
- LabVIEWNXGParamDirection_Out 
 –(Value: 1) Indicates that the parameter is returned from the VI.

#### See Also

[LabVIEWParameter.Direction](labviewparameter-direction.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameters-count.html language=enus -->
## TOPIC 01507: LabVIEWNXGParameters.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameters-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameters-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameters.Count Data Type Long Purpose Returns the number of items in the collection. See Also LabVIEWNXGParameter

### LabVIEWNXGParameters.Count

#### Syntax

[LabVIEWNXGParameters](labviewnxgparameters.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[LabVIEWNXGParameter](labviewnxgparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameters-item.html language=enus -->
## TOPIC 01508: LabVIEWNXGParameters.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameters-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameters-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameters.Item( index) Data Type LabVIEWNXGParameter Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the parameter to retrieve. See Also LabVIEWNXGParameter

### LabVIEWNXGParameters.Item

#### Syntax

[LabVIEWNXGParameters](labviewnxgparameters.html).Item( index)

#### Data Type

[LabVIEWNXGParameter](labviewnxgparameter.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to retrieve.

#### See Also

[LabVIEWNXGParameter](labviewnxgparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameters-newarguments.html language=enus -->
## TOPIC 01509: LabVIEWNXGParameters.NewArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameters-newarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameters-newarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGParameters.NewArguments Return Value LabVIEWNXGArguments Purpose Creates and returns a new LabVIEWNXGArguments collection. Use this collection to pass argument values to a LabVIEWNXG module using the LabVIEWNXGModule.Execute method. Remarks The new collection contains the same numbe

### LabVIEWNXGParameters.NewArguments

#### Syntax

[LabVIEWNXGParameters](labviewnxgparameters.html).NewArguments

#### Return Value

[LabVIEWNXGArguments](labviewnxgarguments.html)

#### Purpose

Creates and returns a new
 [LabVIEWNXGArguments](labviewnxgarguments.html)
 collection. Use this collection to pass argument values to a LabVIEWNXG module using the
 [LabVIEWNXGModule.Execute](labviewnxgmodule-execute.html)
 method.

#### Remarks

The new collection contains the same number of items as the
 [LabVIEWNXGParameters](labviewnxgparameters.html)
 collection. To pass a argument value to a VI parameter, set the
 [LabVIEWNXGArgument.Value](labviewnxgargument-value.html)
 property on the item in the
 LabVIEWNXGArguments
 collection that has the same index as the parameter in the
 LabVIEWNXGParameters
 collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameters.html language=enus -->
## TOPIC 01510: LabVIEWNXGParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNXGParameters class to configure and obtain parameters for a module that uses the LabVIEW NXG Adapter. Use the LabVIEWNXGModule.Parameters property to obtain the collection of parameters for a module. Properties Count (Read Only) Item (Read Only) Method NewArguments See A

### LabVIEWNXGParameters

Use objects from the LabVIEWNXGParameters class to configure and obtain parameters for a module that uses the LabVIEW NXG Adapter. Use the
 [LabVIEWNXGModule.Parameters](labviewnxgmodule-parameters.html)
 property to obtain the collection of parameters for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Method

| NewArguments |
| --- |

#### See Also

[LabVIEWNXGModule.Parameters](labviewnxgmodule-parameters.html)

[LabVIEWNXGParameter](labviewnxgparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparametertypes.html language=enus -->
## TOPIC 01511: LabVIEWNXGParameterTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparametertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparametertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEWNXGParameter.Type property returns one of the following constants to indicate the data type of the parameter. Before you get or set the parameter data type, also get or set the category with the LabVIEWNXGParameter.Category property. LabVIEWNXGParamType_ActiveXRef –(Value: 0x40) Indicates

### LabVIEWNXGParameterTypes

The
 [LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)
 property returns one of the following constants to indicate the data type of the parameter. Before you get or set the parameter data type, also get or set the category with the
 [LabVIEWNXGParameter.Category](labviewnxgparameter-category.html)
 property.

- LabVIEWNXGParamType_ActiveXRef 
 –(Value: 0x40) Indicates that the parameter is an ActiveX reference.
- LabVIEWNXGParamType_AnalogWaveform 
 –(Value: 23) Indicates that the parameter is an Analog Waveform type. For parameters of this LabVIEW NXG data type, use the TestStand
 LabVIEWNXGAnalogWaveform 
 data type as a parameter value.
 Note 
 If the Y element representation of an analog waveform is set to Quad or Unsigned Quad, do not use the
 LabVIEWNXGAnalogWaveform
 data type because the representation of the Y element for the type is set to double-precision, 64-bit floating-point, which cannot store a Quad or unsigned Quad value without the risk of losing precision. In these cases, create a new custom data type and set the representation of the Y element to signed 64-bit integer or unsigned 64-bit integer, respectively.
- LabVIEWNXGParamType_DigitalTable 
 –(Value: 22) Indicates that the parameter is an array of digital data.
- LabVIEWNXGParamType_DigitalWaveform 
 –(Value: 24) Indicates that the parameter is a Digital Waveform type. For parameters of this LabVIEW data type, use the TestStand LabVIEWDigitalWaveform data type as a parameter value.
- LabVIEWNXGParamType_ErrorOut 
 –(Value: 0x25) Indicates that the parameter is an
 error out 
 type. For parameters of this LabVIEW data type, use the TestStand Error data type as a parameter value.
- LabVIEWNXGParamType_Ext 
 –(Value: 8) Indicates that the parameter is an extended-precision number. TestStand treats parameters of this type as 64-bit floating point numbers, so some data could be lost.
- LabVIEWNXGParamType_Int16 
 –(Value: 2) Indicates that the parameter is a 16-bit integer.
- LabVIEWNXGParamType_Int32 
 –(Value: 4) Indicates that the parameter is a 32-bit integer.
- LabVIEWNXGParamType_Int64 
 –(Value: 12) Indicates that the parameter is a 64-bit integer.
- LabVIEWNXGParamType_Int8 
 –(Value: 0) Indicates that the parameter is an 8-bit integer.
- LabVIEWNXGParamType_IO 
 –(Value: 21) Indicates that the parameter is an I/O control reference cluster.
- LabVIEWNXGParamType_LVNXGObjectRef 
 –(Value: 0x42) Indicates that the parameter is a LabVIEW NXG VI or application reference. TestStand treats such references as unsigned, numeric long values.
- LabVIEWNXGParamType_OtherRef 
 –(Value: 0x43) Indicates that the parameter is a LabVIEW reference but not an I/O control reference. TestStand treats such references as unsigned, numeric long values.
- LabVIEWNXGParamType_PathString 
 –(Value: 0x62) Indicates that the parameter is a path. TestStand treats paths as C-strings.
- LabVIEWNXGParamType_Real32 
 –(Value: 6) Indicates that the parameter is a 32-bit real number.
- LabVIEWNXGParamType_Real64 
 –(Value: 7) Indicates that the parameter is a 64-bit real number.
- LabVIEWNXGParamType_StandardCluster 
 –(Value: 20) Indicates that the parameter is a standard cluster.
- LabVIEWNXGParamType_String 
 –(Value: 0x60) Indicates that the parameter is a string that contains binary data. Use the
 LabVIEWNXGParameter.PassAsBinaryString 
 property to instruct TestStand to preserve
 NUL 
 bytes by unescaping a TestStand string before assigning a value to a LabVIEW NXG control, and by escaping a binary string from a LabVIEW NXG indicator before storing in TestStand.
- LabVIEWNXGParamType_TimestampString 
 –(Value: 0x63) Indicates that the parameter is a timestamp, which TestStand treats as a C-string.
- LabVIEWNXGParamType_UInt16 
 –(Value: 3) Indicates that the parameter is a 16-bit unsigned integer.
- LabVIEWNXGParamType_UInt32 
 –(Value: 5) Indicates that the parameter is a 32-bit unsigned integer.
- LabVIEWNXGParamType_UInt64 
 –(Value: 13) Indicates that the parameter is a 64-bit unsigned integer.
- LabVIEWNXGParamType_UInt8 
 –(Value: 1) Indicates that the parameter is an 8-bit unsigned integer.
- LabVIEWNXGParamType_Unspecified 
 –(Value: 200) Indicates that the parameter has an unspecified data type because the category does not have any associated data types.

#### See Also

[LabVIEWNXGParameter.Category](labviewnxgparameter-category.html)

[LabVIEWNXGParameter.PassAsBinaryString](labviewnxgparameter-passasbinarystring.html)

[LabVIEWNXGParameter.Type](labviewnxgparameter-type.html)

[LabVIEWNXGParameterCategories](labviewnxgparametercategories.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgparameterwirerequirements.html language=enus -->
## TOPIC 01512: LabVIEWNXGParameterWireRequirements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgparameterwirerequirements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgparameterwirerequirements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEWNXGParameter.WireRequirement property returns one of the following constants to indicate if the module can pass a default value for the parameter. LabVIEWNXGParamWireReq_Optional –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value.

### LabVIEWNXGParameterWireRequirements

The
 [LabVIEWNXGParameter.WireRequirement](labviewnxgparameter-wirerequirement.html)
 property returns one of the following constants to indicate if the module can pass a default value for the parameter.

- LabVIEWNXGParamWireReq_Optional 
 –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value.
- LabVIEWNXGParamWireReq_Recommended 
 –(Value: 1) Indicates that the module can use the default value for the parameter. However, passing a value is recommended.
- LabVIEWNXGParamWireReq_Required 
 –(Value: 0) Indicates that the module must pass a value for the parameter.

#### See Also

[LabVIEWNXGParameter.WireRequirement](labviewnxgparameter-wirerequirement.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgproject-getprojectitems.html language=enus -->
## TOPIC 01513: LabVIEWNXGProject.GetProjectItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgproject-getprojectitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgproject-getprojectitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProject.GetProjectItems Return Value LabVIEWNXGProjectItem Purpose Returns information about the items in the LABVIEW NXG project. Remarks Use the LabVIEWNXGModule.GetProjectReference method on the LabVIEW NXG module to get the LabVIEW NXG project reference from which this method ob

### LabVIEWNXGProject.GetProjectItems

#### Syntax

[LabVIEWNXGProject](labviewnxgproject.html).GetProjectItems

#### Return Value

[LabVIEWNXGProjectItem](labviewnxgprojectitem.html)

#### Purpose

Returns information about the items in the LABVIEW NXG project.

#### Remarks

Use the
 LabVIEWNXGModule.GetProjectReference
 method on the LabVIEW NXG module to get the LabVIEW NXG project reference from which this method obtains the collection of project items for a module.

#### See Also

[LabVIEWNXGModule.GetProjectReference](labviewnxgmodule-getprojectreference.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgproject-name.html language=enus -->
## TOPIC 01514: LabVIEWNXGProject.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgproject-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgproject-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProject.Name Data Type String Purpose Returns the name of the LabVIEW NXG project.

### LabVIEWNXGProject.Name

#### Syntax

[LabVIEWNXGProject](labviewnxgproject.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the LabVIEW NXG project.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgproject.html language=enus -->
## TOPIC 01515: LabVIEWNXGProject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgproject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgproject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the objects in the LabVIEWNXGProject class to obtain information about the items present in the LabVIEW NXG project. Property Name (Read Only) Method GetProjectItems

### LabVIEWNXGProject

Use the objects in the LabVIEWNXGProject class to obtain information about the items present in the LabVIEW NXG project.

#### Property

| Name (Read Only) |
| --- |

#### Method

| GetProjectItems |
| --- |

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitem-componentname.html language=enus -->
## TOPIC 01516: LabVIEWNXGProjectItem.ComponentName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitem-componentname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitem-componentname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProjectItem.ComponentName Data Type String Purpose Returns the component name the VI belongs to, including the .gcomp extension.

### LabVIEWNXGProjectItem.ComponentName

#### Syntax

[LabVIEWNXGProjectItem](labviewnxgprojectitem.html).ComponentName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the component name the VI belongs to, including the
 .gcomp
 extension.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitem-helpdescription.html language=enus -->
## TOPIC 01517: LabVIEWNXGProjectItem.HelpDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitem-helpdescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitem-helpdescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProjectItem.HelpDescription Data Type String Purpose Returns the help content for the configured LabVIEW NXG VI.

### LabVIEWNXGProjectItem.HelpDescription

#### Syntax

[LabVIEWNXGProjectItem](labviewnxgprojectitem.html).HelpDescription

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the help content for the configured LabVIEW NXG VI.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitem-modulequalifiedname.html language=enus -->
## TOPIC 01518: LabVIEWNXGProjectItem.ModuleQualifiedName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitem-modulequalifiedname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitem-modulequalifiedname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProjectItem.ModuleQualifiedName Data Type String Purpose Returns the VI selected from a project in a LabVIEW NXG module. This value specifies the VI that is run when the step is executed in the LabVIEW NXG Development system.

### LabVIEWNXGProjectItem.ModuleQualifiedName

#### Syntax

[LabVIEWNXGProjectItem](labviewnxgprojectitem.html).ModuleQualifiedName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the VI selected from a project in a LabVIEW NXG module. This value specifies the VI that is run when the step is executed in the LabVIEW NXG Development system.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitem-path.html language=enus -->
## TOPIC 01519: LabVIEWNXGProjectItem.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitem-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitem-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProjectItem.Path Data Type String Purpose Returns the absolute path of the LabVIEW NXG project item.

### LabVIEWNXGProjectItem.Path

#### Syntax

[LabVIEWNXGProjectItem](labviewnxgprojectitem.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path of the LabVIEW NXG project item.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitem-targetname.html language=enus -->
## TOPIC 01520: LabVIEWNXGProjectItem.TargetName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitem-targetname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitem-targetname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProjectItem.TargetName Data Type String Purpose Returns the target for which the component ( .gcomp ) is selected to build.

### LabVIEWNXGProjectItem.TargetName

#### Syntax

[LabVIEWNXGProjectItem](labviewnxgprojectitem.html).TargetName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the target for which the component (
 .gcomp
 ) is selected to build.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitem-type.html language=enus -->
## TOPIC 01521: LabVIEWNXGProjectItem.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitem-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitem-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProjectItem.Type Data Type LabVIEWNXGProjectItemTypes Use the following constants with this data type: LabVIEWNXGProjectItemType_Component –(Value: 0x0) The VI is part of a LabVIEW NXG component. LabVIEWNXGProjectItemType_VirtualInstrument –(Value 0x1): The VI is not part of a LabVI

### LabVIEWNXGProjectItem.Type

#### Syntax

[LabVIEWNXGProjectItem](labviewnxgprojectitem.html).Type

#### Data Type

[LabVIEWNXGProjectItemTypes](labviewnxgprojectitemtypes.html)

Use the following constants with this data type:

- LabVIEWNXGProjectItemType_Component 
 –(Value: 0x0) The VI is part of a LabVIEW NXG component.
- LabVIEWNXGProjectItemType_VirtualInstrument 
 –(Value 0x1): The VI is not part of a LabVIEW NXG component.

#### Purpose

Specifies whether the NXG VI is standalone or part of a LabVIEW NXG component.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitem.html language=enus -->
## TOPIC 01522: LabVIEWNXGProjectItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the objects in the LabVIEWNXGProjectItem class to obtain project item details such as path, component name, and so on. Properties ComponentName (Read Only) HelpDescription (Read Only) ModuleQualifiedName (Read Only) Path (Read Only) TargetName (Read Only) Type (Read Only)

### LabVIEWNXGProjectItem

Use the objects in the LabVIEWNXGProjectItem class to obtain project item details such as path, component name, and so on.

#### Properties

| ComponentName (Read Only) |
| --- |
| HelpDescription (Read Only) |
| ModuleQualifiedName (Read Only) |
| Path (Read Only) |
| TargetName (Read Only) |
| Type (Read Only) |

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitems-count.html language=enus -->
## TOPIC 01523: LabVIEWNXGProjectItems.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitems-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitems-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProjectItems.Count Data Type Long Purpose Returns the number of items in the collection.

### LabVIEWNXGProjectItems.Count

#### Syntax

[LabVIEWNXGProjectItems](labviewnxgprojectitems.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitems-item.html language=enus -->
## TOPIC 01524: LabVIEWNXGProjectItems.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitems-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitems-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWNXGProjectItems.Item( index) Return Value LabVIEWNXGProjectItem Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Long [In] Specifies the zero-based index of the project item to retrieve.

### LabVIEWNXGProjectItems.Item

#### Syntax

[LabVIEWNXGProjectItems](labviewnxgprojectitems.html).Item( index)

#### Return Value

[LabVIEWNXGProjectItem](labviewnxgprojectitem.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the project item to retrieve.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitems.html language=enus -->
## TOPIC 01525: LabVIEWNXGProjectItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWNXGProjectItems class to configure and obtain project items for a module that uses the LabVIEW NXG Adapter. Property Count (Read Only) Method Item

### LabVIEWNXGProjectItems

Use objects from the LabVIEWNXGProjectItems class to configure and obtain project items for a module that uses the LabVIEW NXG Adapter.

#### Property

| Count (Read Only) |
| --- |

#### Method

| Item |
| --- |

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgprojectitemtypes.html language=enus -->
## TOPIC 01526: LabVIEWNXGProjectItemTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgprojectitemtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgprojectitemtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify whether the NXG VI is standalone or part of a component in a LabVIEW NXG project. LabVIEWNXGProjectItemType_Component –(Value: 0x0) The VI is part of a LabVIEW NXG component. LabVIEWNXGProjectItemType_VirtualInstrument –(Value 0x1): The VI is not part of a LabVIEW NXG

### LabVIEWNXGProjectItemTypes

Use these constants to specify whether the NXG VI is standalone or part of a component in a LabVIEW NXG project.

- LabVIEWNXGProjectItemType_Component 
 –(Value: 0x0) The VI is part of a LabVIEW NXG component.
- LabVIEWNXGProjectItemType_VirtualInstrument 
 –(Value 0x1): The VI is not part of a LabVIEW NXG component.

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewnxgservertypes.html language=enus -->
## TOPIC 01527: LabVIEWNXGServerTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewnxgservertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewnxgservertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWNXGAdapter.ServerInfo property to determine the type of server the LabVIEW NXG Adapter is using. LabVIEWNXGServer_ExecServer –(Value: 0) Specifies to use a LabVIEW NXG executable server. LabVIEW NXG executable servers include a LabVIEW NXG development environment

### LabVIEWNXGServerTypes

Use these constants with the LabVIEWNXGAdapter.ServerInfo property to determine the type of server the LabVIEW NXG Adapter is using.

- LabVIEWNXGServer_ExecServer 
 –(Value: 0) Specifies to use a LabVIEW NXG executable server. LabVIEW NXG executable servers include a LabVIEW NXG development environment or a LabVIEW NXG application that registers itself as a LabVIEW NXG ActiveX Automation server.
- LabVIEWNXGServer_RTEServer 
 –(Value: 1) Specifies to use a LabVIEW NXG run-time server.

#### See Also

[LabVIEW NXG Adapter Configuration dialog box](../tsref/labview-nxg-adapter-configuration-dialog-box.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-arraydimensions.html language=enus -->
## TOPIC 01528: LabVIEWParameter.ArrayDimensions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-arraydimensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-arraydimensions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ArrayDimensions Data Type Long Purpose Returns the number of dimensions for array parameters. See Also LabVIEWParameter.GetArrayIndex LabVIEWParameter.GetDefaultArrayDimensionSize

### LabVIEWParameter.ArrayDimensions

#### Syntax

[LabVIEWParameter](labviewparameter.html).ArrayDimensions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of dimensions for array parameters.

#### See Also

[LabVIEWParameter.GetArrayIndex](labviewparameter-getarrayindex.html)

[LabVIEWParameter.GetDefaultArrayDimensionSize](labviewparameter-getdefaultarraydimensionsize.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-arrayelementprototype.html language=enus -->
## TOPIC 01529: LabVIEWParameter.ArrayElementPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-arrayelementprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-arrayelementprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ArrayElementPrototype Data Type LabVIEWParameterElement Purpose Returns the cluster prototype for the elements of the array. Remarks This property is valid only for arrays of LabVIEW clusters. Call the LabVIEWParameter.Category property to determine whether the parameter is a

### LabVIEWParameter.ArrayElementPrototype

#### Syntax

[LabVIEWParameter](labviewparameter.html).ArrayElementPrototype

#### Data Type

[LabVIEWParameterElement](labviewparameterelement.html)

#### Purpose

Returns the cluster prototype for the elements of the array.

#### Remarks

This property is valid only for arrays of LabVIEW clusters. Call the
 [LabVIEWParameter.Category](labviewparameter-category.html)
 property to determine whether the parameter is an array of LabVIEW clusters. The array element prototype is a template from which new elements are copied when the size of the array increases. The array element prototype represents the expected structure of elements of the array. You can also use the array element prototype to create a TestStand custom data type that maps to the LabVIEW cluster.

#### See Also

[LabVIEWParameter.Category](labviewparameter-category.html)

[LabVIEWParameterElement](labviewparameterelement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-aspropertyobject.html language=enus -->
## TOPIC 01530: LabVIEWParameter.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the LabVIEWParameter object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### LabVIEWParameter.AsPropertyObject

#### Syntax

[LabVIEWParameter](labviewparameter.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the LabVIEWParameter object.

#### Remarks

Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-category.html language=enus -->
## TOPIC 01531: LabVIEWParameter.Category

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-category.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-category.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.Category Data Type LabVIEWParameterCategories Purpose Returns the group of data types (number, string, and so on) to which this parameter belongs. Remarks After obtaining the category of the parameter, you can obtain the data type with the LabVIEWParameter.Type property. The

### LabVIEWParameter.Category

#### Syntax

[LabVIEWParameter](labviewparameter.html).Category

#### Data Type

[LabVIEWParameterCategories](labviewparametercategories.html)

#### Purpose

Returns the group of data types (number, string, and so on) to which this parameter belongs.

#### Remarks

After obtaining the
 [category](labviewparametercategories.html)
 of the parameter, you can obtain the data type with the
 [LabVIEWParameter.Type](labviewparameter-type.html)
 property.

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[LabVIEWParameter.Type](labviewparameter-type.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-compleximaginarypartelement.html language=enus -->
## TOPIC 01532: LabVIEWParameter.ComplexImaginaryPartElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-compleximaginarypartelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-compleximaginarypartelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ComplexImaginaryPartElement Data Type LabVIEWParameterElement Purpose Returns the imaginary element of a complex number or array. Remarks This method is valid only for a complex number or an array of complex number parameters. See Also LabVIEWParameter.ComplexRealPartElement

### LabVIEWParameter.ComplexImaginaryPartElement

#### Syntax

[LabVIEWParameter](labviewparameter.html).ComplexImaginaryPartElement

#### Data Type

[LabVIEWParameterElement](labviewparameterelement.html)

#### Purpose

Returns the imaginary element of a complex number or array.

#### Remarks

This method is valid only for a complex number or an array of complex number parameters.

#### See Also

[LabVIEWParameter.ComplexRealPartElement](labviewparameter-complexrealpartelement.html)

[LabVIEWParameter.Elements](labviewparameter-elements.html)

[LabVIEWParameterElement](labviewparameterelement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-complexrealpartelement.html language=enus -->
## TOPIC 01533: LabVIEWParameter.ComplexRealPartElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-complexrealpartelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-complexrealpartelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ComplexRealPartElement Data Type LabVIEWParameterElement Purpose Returns the real element of a complex number or array. Remarks This method is valid only for a complex number and array of complex number parameters. See Also LabVIEWParameter.ComplexImaginaryPartElement LabVIEW

### LabVIEWParameter.ComplexRealPartElement

#### Syntax

[LabVIEWParameter](labviewparameter.html).ComplexRealPartElement

#### Data Type

[LabVIEWParameterElement](labviewparameterelement.html)

#### Purpose

Returns the real element of a complex number or array.

#### Remarks

This method is valid only for a complex number and array of complex number parameters.

#### See Also

[LabVIEWParameter.ComplexImaginaryPartElement](labviewparameter-compleximaginarypartelement.html)

[LabVIEWParameter.Elements](labviewparameter-elements.html)

[LabVIEWParameterElement](labviewparameterelement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-createdefaultarrayelements.html language=enus -->
## TOPIC 01534: LabVIEWParameter.CreateDefaultArrayElements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-createdefaultarrayelements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-createdefaultarrayelements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.CreateDefaultArrayElements Return Value Boolean Returns a value that indicates whether the default array elements were created. Purpose Creates all the default array elements of an array parameter. Remarks This method is valid only on array parameters and creates the elements

### LabVIEWParameter.CreateDefaultArrayElements

#### Syntax

[LabVIEWParameter](labviewparameter.html).CreateDefaultArrayElements

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the default array elements were created.

#### Purpose

Creates all the default array elements of an array parameter.

#### Remarks

This method is valid only on array parameters and creates the elements only if the array control on the VI front panel defines default elements. TestStand replaces any existing array elements the parameter previously specified.

#### See Also

[LabVIEWParameter.DeleteArrayElements](labviewparameter-deletearrayelements.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-defaultvalue.html language=enus -->
## TOPIC 01535: LabVIEWParameter.DefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-defaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.DefaultValue Data Type String Purpose Returns a display string that represents the default value defined for the parameter. Remarks Default values apply only to recommended and optional parameters. You must call the LabVIEWModule.LoadVIInfo or Module.LoadPrototype method befo

### LabVIEWParameter.DefaultValue

#### Syntax

[LabVIEWParameter](labviewparameter.html).DefaultValue

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a display string that represents the default value defined for the parameter.

#### Remarks

Default values apply only to recommended and optional parameters. You must call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving the default value. Otherwise, TestStand returns an empty string. The values stay in memory until the sequence file closes.

#### See Also

[LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)

[LabVIEWParameter.UseDefaultValue](labviewparameter-usedefaultvalue.html)

[LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)

[LabVIEWParameter.WireRequirement](labviewparameter-wirerequirement.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-deletearrayelement.html language=enus -->
## TOPIC 01536: LabVIEWParameter.DeleteArrayElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-deletearrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-deletearrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.DeleteArrayElement( index) Purpose Deletes the array element at a specified index. Remarks This method is valid only for one-dimensional array parameters. Use the LabVIEWParameter.ArrayDimensions property to determine the number of array dimensions. Parameters index As Long [

### LabVIEWParameter.DeleteArrayElement

#### Syntax

[LabVIEWParameter](labviewparameter.html).DeleteArrayElement( index)

#### Purpose

Deletes the array element at a specified index.

#### Remarks

This method is valid only for one-dimensional array parameters. Use the
 [LabVIEWParameter.ArrayDimensions](labviewparameter-arraydimensions.html)
 property to determine the number of array dimensions.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index at which to delete the array element. This value must be greater than or equal to
 0
 and less than the number of array elements.

#### See Also

[LabVIEWParameter.ArrayDimensions](labviewparameter-arraydimensions.html)

[LabVIEWParameter.DeleteArrayElements](labviewparameter-deletearrayelements.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-deletearrayelements.html language=enus -->
## TOPIC 01537: LabVIEWParameter.DeleteArrayElements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-deletearrayelements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-deletearrayelements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.DeleteArrayElements Return Value Boolean Purpose Deletes all the array elements. Remarks This method is valid only on array parameters. See Also LabVIEWParameter.DeleteArrayElement LabVIEWParameter.InsertArrayElement LabVIEWParameter.Type

### LabVIEWParameter.DeleteArrayElements

#### Syntax

[LabVIEWParameter](labviewparameter.html).DeleteArrayElements

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Deletes all the array elements.

#### Remarks

This method is valid only on array parameters.

#### See Also

[LabVIEWParameter.DeleteArrayElement](labviewparameter-deletearrayelement.html)

[LabVIEWParameter.InsertArrayElement](labviewparameter-insertarrayelement.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-direction.html language=enus -->
## TOPIC 01538: LabVIEWParameter.Direction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-direction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-direction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.Direction Data Type LabVIEWParameterDirections Use the following constants with this data type: LVParamDirection_In –(Value: 0) Indicates that the parameter is passed to the VI. LVParamDirection_Out –(Value: 1) Indicates that the parameter is returned from the VI. Purpose Ret

### LabVIEWParameter.Direction

#### Syntax

[LabVIEWParameter](labviewparameter.html).Direction

#### Data Type

[LabVIEWParameterDirections](labviewparameterdirections.html)

Use the following constants with this data type:

- LVParamDirection_In 
 –(Value: 0) Indicates that the parameter is passed to the VI.
- LVParamDirection_Out 
 –(Value: 1) Indicates that the parameter is returned from the VI.

#### Purpose

Returns a value that indicates whether the parameter is an
 [input or output](labviewparameterdirections.html)
 parameter.

#### Remarks

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[LabVIEWParameter.WireRequirement](labviewparameter-wirerequirement.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-displaycreatecustomdatatyped.html language=enus -->
## TOPIC 01539: LabVIEWParameter.DisplayCreateCustomDataTypeDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-displaycreatecustomdatatyped.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-displaycreatecustomdatatyped.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.DisplayCreateCustomDataTypeDialog( sequenceContext) Return Value Boolean Returns True if you click OK in the dialog box. False if you click Cancel . Purpose Launches the Create/Update Custom Data Type from Cluster dialog box, in which you configure a new custom data type or u

### LabVIEWParameter.DisplayCreateCustomDataTypeDialog

#### Syntax

[LabVIEWParameter](labviewparameter.html).DisplayCreateCustomDataTypeDialog( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box.
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Create/Update Custom Data Type from Cluster](../tsref/create-update-custom-data-type-from-cluster-d.html)
 dialog box, in which you configure a new custom data type or update an existing custom type.

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context the dialog box uses to obtain information about the sequence file. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context.

#### See Also

[Create/Update Custom Data Type from Cluster dialog box](../tsref/create-update-custom-data-type-from-cluster-d.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-displaytype.html language=enus -->
## TOPIC 01540: LabVIEWParameter.DisplayType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-displaytype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-displaytype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.DisplayType Data Type String The display value of the data type of the parameter. Purpose Returns a localized string that describes the LabVIEW data type for the parameter. Remarks The LabVIEW Adapter persists this property value when you specify a code module for a step. For

### LabVIEWParameter.DisplayType

#### Syntax

[LabVIEWParameter](labviewparameter.html).DisplayType

#### Data Type

[String](data-types-for-teststand.html)

The display value of the data type of the parameter.

#### Purpose

Returns a localized string that describes the LabVIEW data type for the parameter.

#### Remarks

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before you retrieve this property value.

#### See Also

[LabVIEWParameter.Type](labviewparameter-type.html)

[LabVIEWParameter.WireRequirement](labviewparameter-wirerequirement.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-elements.html language=enus -->
## TOPIC 01541: LabVIEWParameter.Elements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-elements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-elements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.Elements Data Type LabVIEWParameterElements Purpose Returns a collection that accesses the members of a parameter that is a cluster, or accesses the elements of a parameter that is an array of clusters. See Also LabVIEWParameterElements

### LabVIEWParameter.Elements

#### Syntax

[LabVIEWParameter](labviewparameter.html).Elements

#### Data Type

[LabVIEWParameterElements](labviewparameterelements.html)

#### Purpose

Returns a collection that accesses the members of a parameter that is a cluster, or accesses the elements of a parameter that is an array of clusters.

#### See Also

[LabVIEWParameterElements](labviewparameterelements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-exprclustertypemismatch.html language=enus -->
## TOPIC 01542: LabVIEWParameter.ExprClusterTypeMismatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-exprclustertypemismatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-exprclustertypemismatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ExprClusterTypeMismatch( sequenceContext) Return Value Boolean Purpose Returns True if you enable cluster mapping for the variable or property the expression value returns and the names or types of cluster elements do not match the LabVIEW cluster the VI specifies. Otherwise

### LabVIEWParameter.ExprClusterTypeMismatch

#### Syntax

[LabVIEWParameter](labviewparameter.html).ExprClusterTypeMismatch( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if you enable cluster mapping for the variable or property the expression value returns and the names or types of cluster elements do not match the LabVIEW cluster the VI specifies. Otherwise this method returns
 False
 .

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the SequenceContext to use to evaluate the parameter expression value.

#### See Also

[LabVIEWParameter.Type](labviewparameter-type.html)

[LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-getarrayindex.html language=enus -->
## TOPIC 01543: LabVIEWParameter.GetArrayIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-getarrayindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-getarrayindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.GetArrayIndex( offset, options) Return Value String An array index string. Array index strings are a list of numbers enclosed in brackets that index each dimension of the array. For example, the following is an array index for a two dimensional array: [0][1] . Purpose Returns

### LabVIEWParameter.GetArrayIndex

#### Syntax

[LabVIEWParameter](labviewparameter.html).GetArrayIndex( offset, options)

#### Return Value

[String](data-types-for-teststand.html)

An array index string. Array index strings are a list of numbers enclosed in brackets that index each dimension of the array. For example, the following is an array index for a two dimensional array:
 [0][1]
 .

#### Purpose

Returns the index of the array element the
 offset
 parameter specifies.

#### Parameters

offset
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based number representing the offset of an array element in the one-dimensional physical storage of the array. The offset is in terms of the number of elements.

options
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use. Pass
 0
 .

#### See Also

[LabVIEWParameter.ArrayDimensions](labviewparameter-arraydimensions.html)

[LabVIEWParameter.GetDefaultArrayDimensionSize](labviewparameter-getdefaultarraydimensionsize.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-getdefaultarraydimensionsize.html language=enus -->
## TOPIC 01544: LabVIEWParameter.GetDefaultArrayDimensionSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-getdefaultarraydimensionsize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-getdefaultarraydimensionsize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.GetDefaultArrayDimensionSize( dimension) Return Value Long Purpose Returns the default size of the array corresponding to the zero-based index passed as input. Remarks The default size corresponds to the default size of the array control in the front panel of a VI. Call the L

### LabVIEWParameter.GetDefaultArrayDimensionSize

#### Syntax

[LabVIEWParameter](labviewparameter.html).GetDefaultArrayDimensionSize( dimension)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Returns the default size of the array corresponding to the zero-based index passed as input.

#### Remarks

The default size corresponds to the default size of the array control in the front panel of a VI. Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method.

#### Parameters

dimension
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index corresponding to one of the array dimensions.

#### See Also

[LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)

[LabVIEWParameter.ArrayDimensions](labviewparameter-arraydimensions.html)

[LabVIEWParameter.GetArrayIndex](labviewparameter-getarrayindex.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-getenumvalues.html language=enus -->
## TOPIC 01545: LabVIEWParameter.GetEnumValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-getenumvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-getenumvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.GetEnumValues Return Value Object Array Returns an array of property objects where each property object represents an enumeration value or a ring control value. Purpose Returns the enumeration constants for an enumeration parameter or returns the ring control values for a rin

### LabVIEWParameter.GetEnumValues

#### Syntax

[LabVIEWParameter](labviewparameter.html).GetEnumValues

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns an array of property objects where each property object represents an enumeration value or a ring control value.

#### Purpose

Returns the enumeration constants for an enumeration parameter or returns the ring control values for a ring control parameter.

#### Remarks

Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 method or the
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method. The values stay in memory until the sequence file closes.

Note

Use the name and value of the property objects in the array this method returns to determine the name and value of the enumeration constants or ring controls.

Pass the return value of this method as the
 additionalConstants
 parameter of
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 when checking the
 [LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)
 property for errors.

If you are using an
 
 [ExpressionEdit](../tsuiref/expressionedit.html)
 control to display the value of the
 LabVIEWParameter.ValueExpr
 property, pass the return value of this method to the
 
 [ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)
 method to instruct the ExpressionEdit control to validate enumeration constants.

#### See Also

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

[LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-insertarrayelement.html language=enus -->
## TOPIC 01546: LabVIEWParameter.InsertArrayElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-insertarrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-insertarrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.InsertArrayElement( index) Purpose Inserts an array element at the specified index. Remarks This method is valid only for one-dimensional array parameters. Use the LabVIEWParameter.ArrayDimensions property to determine the number of array dimensions. Parameters index As Long

### LabVIEWParameter.InsertArrayElement

#### Syntax

[LabVIEWParameter](labviewparameter.html).InsertArrayElement( index)

#### Purpose

Inserts an array element at the specified index.

#### Remarks

This method is valid only for one-dimensional array parameters. Use the
 [LabVIEWParameter.ArrayDimensions](labviewparameter-arraydimensions.html)
 property to determine the number of array dimensions.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index at which to insert the array element. This value must be greater than or equal to
 0
 and less than or equal to the number of array elements.

#### See Also

[LabVIEWParameter.ArrayDimensions](labviewparameter-arraydimensions.html)

[LabVIEWParameter.DeleteArrayElement](labviewparameter-deletearrayelement.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-isclustermappinginvalid.html language=enus -->
## TOPIC 01547: LabVIEWParameter.IsClusterMappingInvalid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-isclustermappinginvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-isclustermappinginvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.IsClusterMappingInvalid( reasonNotValid) Return Value Boolean Returns True when all the following conditions are true: The parameter is a cluster or cluster array The argument expression is valid and non-empty The argument or cluster mapping of the argument is invalid In all

### LabVIEWParameter.IsClusterMappingInvalid

#### Syntax

[LabVIEWParameter](labviewparameter.html).IsClusterMappingInvalid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when all the following conditions are true:

- The parameter is a cluster or cluster array
- The argument expression is valid and non-empty
- The argument or cluster mapping of the argument is invalid

In all other cases, this method returns
 False
 .

#### Purpose

Returns a value that indicates whether the argument you specify for a LabVIEW cluster or cluster array parameter is valid by checking the cluster passing information for any custom data types used to confirm that the information matches the cluster definition stored when you specified the module.

Note

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] When this method returns
 True
 , this parameter returns the reason why the argument is invalid.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-isnodeusingdefault.html language=enus -->
## TOPIC 01548: LabVIEWParameter.IsNodeUsingDefault

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-isnodeusingdefault.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-isnodeusingdefault.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.IsNodeUsingDefault Data Type Boolean Returns True when the parameter is associated with a LabVIEW property configured to use the default value. Purpose Returns a value that indicates whether the parameter is associated with a LabVIEW property configured to use the default val

### LabVIEWParameter.IsNodeUsingDefault

#### Syntax

[LabVIEWParameter](labviewparameter.html).IsNodeUsingDefault

#### Data Type

[Boolean](data-types-for-teststand.html)

Returns
 True
 when the parameter is associated with a LabVIEW property configured to use the default value.

#### Purpose

Returns a value that indicates whether the parameter is associated with a LabVIEW property configured to use the default value in a Property Node call.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-isparametermappingvalid.html language=enus -->
## TOPIC 01549: LabVIEWParameter.IsParameterMappingValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-isparametermappingvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-isparametermappingvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.IsParameterMappingValid( reasonNotValid) Return Value Boolean Returns True when all the following conditions are true: the parameter is a cluster or cluster array or enumeration or enumeration array, the argument expression is valid and not empty, the cluster mapping of the a

### LabVIEWParameter.IsParameterMappingValid

#### Syntax

[LabVIEWParameter](labviewparameter.html).IsParameterMappingValid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when all the following conditions are true:

1. the parameter is a cluster or cluster array or enumeration or enumeration array,
2. the argument expression is valid and not empty,
3. the cluster mapping of the argument is valid if the parameter is a cluster, and
4. the argument value is compatible with the enumeration parameter if the parameter is an enumeration.

In all other cases, returns
 False
 .

#### Purpose

Returns a value that indicates whether the argument you specify for a LabVIEW cluster or cluster array parameter is valid.

#### Remarks

This method checks the cluster passing information for any custom data types used and confirms that the information matches the cluster definition stored when you specified the module. For an enumeration parameter, the method validates that:

1. If the argument is a number or TestStand enumeration type instance, the numeric representation is compatible with the LabVIEW parameters representation.
2. If the argument is a TestStand enumeration type, the enumerators of the TestStand type must match the enumerators of the LabVIEW parameter in
  - Number 
 and
  - Name and value 
 .

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] When this method returns
 False
 , this parameter returns an explanation for why the argument is invalid.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-parametercaption.html language=enus -->
## TOPIC 01550: LabVIEWParameter.ParameterCaption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-parametercaption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-parametercaption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ParameterCaption Data Type String Purpose Returns the caption of the parameter in the VI. Remarks Use the LabVIEWParameter.ParameterName property to determine the label or name of the parameter. See Also LabVIEWParameter.ParameterName Module.LoadPrototype

### LabVIEWParameter.ParameterCaption

#### Syntax

[LabVIEWParameter](labviewparameter.html).ParameterCaption

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the caption of the parameter in the VI.

#### Remarks

Use the
 [LabVIEWParameter.ParameterName](labviewparameter-parametername.html)
 property to determine the label or name of the parameter.

#### See Also

[LabVIEWParameter.ParameterName](labviewparameter-parametername.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-parametername.html language=enus -->
## TOPIC 01551: LabVIEWParameter.ParameterName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-parametername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-parametername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ParameterName Data Type String Purpose Returns the name of the parameter in the VI. Remarks The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the Module.LoadPrototype method before retrieving thi

### LabVIEWParameter.ParameterName

#### Syntax

[LabVIEWParameter](labviewparameter.html).ParameterName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the parameter in the VI.

#### Remarks

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

Use the
 [LabVIEWParameter.ParameterCaption](labviewparameter-parametercaption.html)
 property to determine the caption of the parameter.

#### See Also

[LabVIEWParameter.ParameterCaption](labviewparameter-parametercaption.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-partiallyspecified.html language=enus -->
## TOPIC 01552: LabVIEWParameter.PartiallySpecified

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-partiallyspecified.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-partiallyspecified.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.PartiallySpecified Data Type Boolean Purpose Returns a value that indicates whether the parameter is partially specified. Remarks A parameter is partially specified if some of the parameter elements specify to use default values while other parameter elements specify expressi

### LabVIEWParameter.PartiallySpecified

#### Syntax

[LabVIEWParameter](labviewparameter.html).PartiallySpecified

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the parameter is partially specified.

#### Remarks

A parameter is partially specified if some of the parameter elements specify to use default values while other parameter elements specify expression values.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-passasbinarystring.html language=enus -->
## TOPIC 01553: LabVIEWParameter.PassAsBinaryString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-passasbinarystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-passasbinarystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.PassAsBinaryString Data Type Boolean Purpose Specifies if TestStand preserves NUL bytes when setting and getting LabVIEW string data. Remarks This property applies only when the LabVIEWParameter.Category property of the parameter is LVParamCategory_String or LVParamCategory_S

### LabVIEWParameter.PassAsBinaryString

#### Syntax

[LabVIEWParameter](labviewparameter.html).PassAsBinaryString

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if TestStand preserves NUL bytes when setting and getting LabVIEW string data.

#### Remarks

This property applies only when the
 [LabVIEWParameter.Category](labviewparameter-category.html)
 property of the parameter is
 LVParamCategory_String
 or
 LVParamCategory_StringArray
 and the
 [LabVIEWParameter.Type](labviewparameter-type.html)
 property of the parameter is
 LVParamType_String
 .

TestStand
 [handles the string data in different ways](../tsref/string-parameters-labview-vi-call-parameters.html)
 depending on the version of LabVIEW you are using.

When this property is
 False
 , the LabVIEW Adapter treats strings as C-style strings with a NUL character to indicate the end of the string. C-strings cannot contain binary data.

Call the
 [PropertyObject.GetValBinary](propertyobject-getvalbinary.html)
 method on the variable that stores the binary string to retrieve the raw data in TestStand when the binary data is compressed.

#### See Also

[LabVIEWParameter.Category](labviewparameter-category.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

[LabVIEWParameterCategories](labviewparametercategories.html)

[LabVIEWParameterTypes](labviewparametertypes.html)

[PropertyObject.GetValBinary](propertyobject-getvalbinary.html)

[String Parameters](../tsref/string-parameters-labview-vi-call-parameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-type.html language=enus -->
## TOPIC 01554: LabVIEWParameter.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.Type Data Type LabVIEWParameterTypes Purpose Returns the data type of the parameter element, specifically indicating the type of number, string, and so on. Remarks Obtain the category using the LabVIEWParameter.Category property before obtaining the data type of the parameter

### LabVIEWParameter.Type

#### Syntax

[LabVIEWParameter](labviewparameter.html).Type

#### Data Type

[LabVIEWParameterTypes](labviewparametertypes.html)

#### Purpose

Returns the data type of the parameter element, specifically indicating the type of number, string, and so on.

#### Remarks

Obtain the
 [category](labviewparametercategories.html)
 using the
 [LabVIEWParameter.Category](labviewparameter-category.html)
 property before obtaining the data type of the parameter.

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[LabVIEWParameter.Category](labviewparameter-category.html)

[LabVIEWParameter.TypeDisplayString](labviewparameter-typedisplaystring.html)

[LabVIEWParameterCategories](labviewparametercategories.html)

[LabVIEWParameterTypes](labviewparametertypes.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-typedisplaystring.html language=enus -->
## TOPIC 01555: LabVIEWParameter.TypeDisplayString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-typedisplaystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-typedisplaystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.TypeDisplayString Data Type String Purpose Returns a string that describes the type of the parameter. See Also LabVIEWParameter.Type

### LabVIEWParameter.TypeDisplayString

#### Syntax

[LabVIEWParameter](labviewparameter.html).TypeDisplayString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a string that describes the type of the parameter.

#### See Also

[LabVIEWParameter.Type](labviewparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-updateclustermapping.html language=enus -->
## TOPIC 01556: LabVIEWParameter.UpdateClusterMapping

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-updateclustermapping.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-updateclustermapping.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.UpdateClusterMapping( sequenceContext) Return Value Boolean Returns True if the method updates any expression values for the elements of the cluster parameter. Purpose Updates the expression values for the cluster parameter elements when the parameter specifies an expression

### LabVIEWParameter.UpdateClusterMapping

#### Syntax

[LabVIEWParameter](labviewparameter.html).UpdateClusterMapping( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the method updates any expression values for the elements of the cluster parameter.

#### Purpose

Updates the expression values for the cluster parameter elements when the parameter specifies an expression value that evaluates to a named data type that enables cluster passing.

#### Remarks

This method is valid only on cluster parameters.

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Pass the sequence context that the dialog box uses to evaluate all value expressions. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context.

#### See Also

[Engine.NewEditContext](engine-neweditcontext.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-usedefaultvalue.html language=enus -->
## TOPIC 01557: LabVIEWParameter.UseDefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-usedefaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-usedefaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.UseDefaultValue Data Type Boolean Purpose Specifies whether to use the default value of the parameter when calling the VI. Remarks You can use the default value for recommended or optional parameters. See Also LabVIEWParameter.PartiallySpecified LabVIEWParameter.ValueExpr Lab

### LabVIEWParameter.UseDefaultValue

#### Syntax

[LabVIEWParameter](labviewparameter.html).UseDefaultValue

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to use the default value of the parameter when calling the VI.

#### Remarks

You can use the default value for recommended or optional parameters.

#### See Also

[LabVIEWParameter.PartiallySpecified](labviewparameter-partiallyspecified.html)

[LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)

[LabVIEWParameter.WireRequirement](labviewparameter-wirerequirement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-userdata.html language=enus -->
## TOPIC 01558: LabVIEWParameter.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.UserData Data Type PropertyObject Purpose Holds a data item you associate with the parameter object. Remarks Typically, you do not use this property. See Also PropertyObject

### LabVIEWParameter.UserData

#### Syntax

[LabVIEWParameter](labviewparameter.html).UserData

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Holds a data item you associate with the parameter object.

#### Remarks

Typically, you do not use this property.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-validevaluationtypes.html language=enus -->
## TOPIC 01559: LabVIEWParameter.ValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-validevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-validevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ValidEvaluationTypes Data Type EvaluationTypes Purpose Returns the valid types to which this parameter can evaluate. Remarks You can pass the value of this property to the validEvaluationTypes parameter of the Expression.ValidateEvaluationType method to determine whether the

### LabVIEWParameter.ValidEvaluationTypes

#### Syntax

[LabVIEWParameter](labviewparameter.html).ValidEvaluationTypes

#### Data Type

[EvaluationTypes](evaluationtypes.html)

#### Purpose

Returns the valid types to which this parameter can evaluate.

#### Remarks

You can pass the value of this property to the
 validEvaluationTypes
 parameter of the
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method to determine whether the value of the
 [LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)
 property contains errors.

If you are using an ExpressionEdit control to display the value of the
 LabVIEWParameter.ValueExpr
 property, pass the value of this property to the
 
 [ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)
 method.

#### See Also

[EvaluationTypes](evaluationtypes.html)

[EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.GetValidEvaluationTypes](../tsuiref/expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-valueexpr.html language=enus -->
## TOPIC 01560: LabVIEWParameter.ValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-valueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-valueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ValueExpr Data Type String Purpose Specifies an expression to define the argument to pass for the parameter when calling the VI. Remarks TestStand ignores this parameter if the LabVIEWParameter.UseDefaultValue property is True . Call the LabVIEWModule.LoadVIInfo method before

### LabVIEWParameter.ValueExpr

#### Syntax

[LabVIEWParameter](labviewparameter.html).ValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression to define the argument to pass for the parameter when calling the VI.

#### Remarks

TestStand ignores this parameter if the
 [LabVIEWParameter.UseDefaultValue](labviewparameter-usedefaultvalue.html)
 property is
 True
 .

Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 method before you get or set this property to ensure that LabVIEW parameters, such as enumeration values and ring controls, are updated with their current definitions.

#### See Also

[LabVIEWParameter.DefaultValue](labviewparameter-defaultvalue.html)

[LabVIEWParameter.UseDefaultValue](labviewparameter-usedefaultvalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-valueexprisignored.html language=enus -->
## TOPIC 01561: LabVIEWParameter.ValueExprIsIgnored

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-valueexprisignored.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-valueexprisignored.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ValueExprIsIgnored Data Type Boolean Purpose Use this property to determine whether the LabVIEW Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameters that use default values. See Also LabVIEWPa

### LabVIEWParameter.ValueExprIsIgnored

#### Syntax

[LabVIEWParameter](labviewparameter.html).ValueExprIsIgnored

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the LabVIEW Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameters that use default values.

#### See Also

[LabVIEWParameter.UseDefaultValue](labviewparameter-usedefaultvalue.html)

[LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)

[LabVIEWParameter.ValueExprIsOptional](labviewparameter-valueexprisoptional.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-valueexprisoptional.html language=enus -->
## TOPIC 01562: LabVIEWParameter.ValueExprIsOptional

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-valueexprisoptional.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-valueexprisoptional.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.ValueExprIsOptional Data Type Boolean Purpose Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for output parameters and value expressio

### LabVIEWParameter.ValueExprIsOptional

#### Syntax

[LabVIEWParameter](labviewparameter.html).ValueExprIsOptional

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for output parameters and value expressions for cluster and array parameters that have parameter elements are optional.

#### See Also

[LabVIEWParameter.Direction](labviewparameter-direction.html)

[LabVIEWParameter.ValueExpr](labviewparameter-valueexpr.html)

[LabVIEWParameter.ValueExprIsIgnored](labviewparameter-valueexprisignored.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter-wirerequirement.html language=enus -->
## TOPIC 01563: LabVIEWParameter.WireRequirement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter-wirerequirement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter-wirerequirement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameter.WireRequirement Data Type LabVIEWParameterWireRequirements Use the following constants with this data type: LVParamWireReq_Optional –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value. LVParamWireReq_Recommended –(Value

### LabVIEWParameter.WireRequirement

#### Syntax

[LabVIEWParameter](labviewparameter.html).WireRequirement

#### Data Type

[LabVIEWParameterWireRequirements](labviewparameterwirerequirements.html)

Use the following constants with this data type:

- LVParamWireReq_Optional 
 –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value.
- LVParamWireReq_Recommended 
 –(Value: 1) Indicates that the module can use the default value for the parameter. However, passing a value is recommended.
- LVParamWireReq_Required 
 –(Value: 0) Indicates that the module must pass a value for the parameter.

#### Purpose

Indicates whether the parameter is required, recommended, or optional.

#### Remarks

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call
 [Module.LoadPrototype](module-loadprototype.html)
 before retrieving this property.

#### See Also

[LabVIEWParameter.Direction](labviewparameter-direction.html)

[LabVIEWParameterWireRequirements](labviewparameterwirerequirements.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameter.html language=enus -->
## TOPIC 01564: LabVIEWParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWParameter class to configure and obtain LabVIEWParameter-specific information for an item in the LabVIEWParameters collection class. Properties ArrayDimensions (Read Only) ArrayElementPrototype (Read Only) Category (Read Only) ComplexImaginaryPartElement (Read Only) Compl

### LabVIEWParameter

Use objects from the LabVIEWParameter class to configure and obtain LabVIEWParameter-specific information for an item in the LabVIEWParameters collection class.

#### Properties

| ArrayDimensions (Read Only) |
| --- |
| ArrayElementPrototype (Read Only) |
| Category (Read Only) |
| ComplexImaginaryPartElement (Read Only) |
| ComplexRealPartElement (Read Only) |
| DefaultValue (Read Only) |
| Direction (Read Only) |
| DisplayType (Read Only) |
| Elements (Read Only) |
| IsNodeUsingDefault |
| ParameterCaption (Read Only) |
| ParameterName (Read Only) |
| PartiallySpecified (Read Only) |
| PassAsBinaryString |
| Type (Read Only) |
| TypeDisplayString (Read Only) |
| UseDefaultValue |
| UserData (Read Only) |
| ValidEvaluationTypes (Read Only) |
| ValueExpr |
| ValueExprIsIgnored (Read Only) |
| ValueExprIsOptional (Read Only) |
| WireRequirement (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| CreateDefaultArrayElements |
| DeleteArrayElement |
| DeleteArrayElements |
| DisplayCreateCustomDataTypeDialog |
| ExprClusterTypeMismatch |
| GetArrayIndex |
| GetDefaultArrayDimensionSize |
| GetEnumValues |
| InsertArrayElement |
| IsClusterMappingInvalid |
| IsParameterMappingValid |
| UpdateClusterMapping |

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWParameters](labviewparameters.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparametercategories.html language=enus -->
## TOPIC 01565: LabVIEWParameterCategories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparametercategories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparametercategories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEWParameter.Category and LabVIEWParameterElement.Category properties return one of the following constants to indicate what group of data types the parameter belongs to. After obtaining the category of the parameter, you can obtain the data type with the LabVIEWParameter.Type or LabVIEWPara

### LabVIEWParameterCategories

The
 [LabVIEWParameter.Category](labviewparameter-category.html)
 and
 [LabVIEWParameterElement.Category](labviewparameterelement-category.html)
 properties return one of the following constants to indicate what group of data types the parameter belongs to. After obtaining the category of the parameter, you can obtain the data type with the
 [LabVIEWParameter.Type](labviewparameter-type.html)
 or
 [LabVIEWParameterElement.Type](labviewparameterelement-type.html)
 property. Some categories do not have an associated data type; for these categories, the only valid value for the
 LabVIEWParameter.Type
 property is
 [LVParamType_Unspecified](labviewparametertypes.html)
 .

- LVParamCategory_Boolean 
 –(Value: 2) Indicates that the parameter is a Boolean type This category does not have any associated data types.
- LVParamCategory_BooleanArray 
 –(Value: 52) Indicates that the parameter is an array of Boolean values. This category does not have any associated data types.
- LVParamCategory_Cluster 
 –(Value: 3) Indicates that the parameter is a cluster. Data types associated with this category include
 LVParamType_DigitalData 
 ,
 LVParamType_DigitalWaveform 
 ,
 LVParamType_ErrorOut 
 ,
 LVParamType_IO 
 ,
 LVParamType_Standard 
 ,
 LVParamType_TestData 
 , and
 LVParamType_Waveform 
 .
- LVParamCategory_ClusterArray 
 –(Value: 53) Indicates that the parameter is an array of clusters. Data types associated with this category include
 LVParamType_DigitalData 
 ,
 LVParamType_DigitalWaveform 
 ,
 LVParamType_ErrorOut 
 ,
 LVParamType_IO 
 ,
 LVParamType_Standard 
 ,
 LVParamType_TestData 
 , and
 LVParamType_Waveform 
 .
- LVParamCategory_Complex 
 –(Value: 6) Indicates that the parameter is a complex numeric data type. Data types associated with this category include
 LVParamType_Complex128 
 ,
 LVParamType_Complex64 
 , and
 LVParamType_ComplexEx 
 .
- LVParamCategory_ComplexArray 
 –(Value: 55) Indicates that the parameter is an array of complex numbers. Data types associated with this category include
 LVParamType_Complex128 
 ,
 LVParamType_Complex64 
 , and
 LVParamType_ComplexEx 
 .
- LVParamCategory_Enum 
 –(Value: 9) Indicates that the parameter is an enumeration.
- LVParamCategory_EnumArray 
 –(Value: 58) Indicates that the parameter is an array of enumerations.
- LVParamCategory_Numeric 
 –(Value: 0) Indicates that the parameter is a numeric data type. Numeric data types include enumerations, but do not include complex numbers. Data types associated with this category include
 LVParamType_Ext 
 ,
 LVParamType_Int16 
 ,
 LVParamType_Int32 
 ,
 LVParamType_Int64 
 ,
 LVParamType_Int8 
 ,
 LVParamType_Real32 
 ,
 LVParamType_Real64 
 ,
 LVParamType_UInt16 
 ,
 LVParamType_UInt32 
 ,
 LVParamType_UInt64 
 , and
 LVParamType_UInt8 
 .
- LVParamCategory_NumericArray 
 –(Value: 50) Indicates that the parameter is a an array of numbers. Numeric data types include enumerations, but do not include complex numbers. Data types associated with this category include
 LVParamType_Ext 
 ,
 LVParamType_Int16 
 ,
 LVParamType_Int32 
 ,
 LVParamType_Int64 
 ,
 LVParamType_Int8 
 ,
 LVParamType_Real32 
 ,
 LVParamType_Real64 
 ,
 LVParamType_UInt16 
 ,
 LVParamType_UInt32 
 ,
 LVParamType_UInt64 
 , and
 LVParamType_UInt8 
 .
- LVParamCategory_Reference 
 –(Value: 4) Indicates that the parameter is a reference. Data types associated with this category include
 LVParamType_ActiveXRef 
 ,
 LVParamType_OtherRef 
 , and
 LVParamType_LVClass 
 but do not include
 LVParamType_IOCluster 
 , which is considered a cluster data type.
- LVParamCategory_ReferenceArray 
 –(Value: 54) Indicates that the parameter is an array of COM references. Data types associated with this category include
 LVParamType_ActiveXRef 
 ,
 LVParamType_OtherRef 
 , and
 LVParamType_LVClass 
 but do not include
 LVParamType_IOCluster 
 , which is considered a cluster data type.
- LVParamCategory_Ring 
 –(Value: 10) Indicates that the parameter is a ring.
- LVParamCategory_RingArray 
 –(Value: 59) Indicates that the parameter is a ring array data type.
- LVParamCategory_String 
 –(Value: 1) Indicates that the parameter is a string data type. Data types associated with this category include
 LVParamType_BinaryString 
 ,
 LVParamType_CString 
 ,
 LVParamType_PathString 
 , and
 LVParamType_TimestampString 
 .
- LVParamCategory_StringArray 
 –(Value: 51) Indicates that the parameter is an array of strings. Data types associated with this category include
 LVParamType_BinaryString 
 ,
 LVParamType_CString 
 ,
 LVParamType_PathString 
 , and
 LVParamType_TimestampString 
 .
- LVParamCategory_Unknown 
 –(Value: 8) Indicates that the parameter has a data type TestStand does not recognize.
- LVParamCategory_Variant 
 –(Value: 7) Indicates the parameter is a COM Variant. This category does not have any associated data types.
- LVParamCategory_VariantArray 
 –(Value: 56) Indicates the parameter is an array of COM Variants. This category does not have any associated data types.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWParameter.Category](labviewparameter-category.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

[LabVIEWParameterElement.Category](labviewparameterelement-category.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

[LabVIEWParameterTypes](labviewparametertypes.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterdirections.html language=enus -->
## TOPIC 01566: LabVIEWParameterDirections

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterdirections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterdirections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEWParameter.Direction property returns one of the following constants to indicate how the module passes the parameter when it executes. LVParamDirection_In –(Value: 0) Indicates that the parameter is passed to the VI. LVParamDirection_Out –(Value: 1) Indicates that the parameter is returned

### LabVIEWParameterDirections

The
 [LabVIEWParameter.Direction](labviewparameter-direction.html)
 property returns one of the following constants to indicate how the module passes the parameter when it executes.

- LVParamDirection_In 
 –(Value: 0) Indicates that the parameter is passed to the VI.
- LVParamDirection_Out 
 –(Value: 1) Indicates that the parameter is returned from the VI.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWParameter.Direction](labviewparameter-direction.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-arraydimensions.html language=enus -->
## TOPIC 01567: LabVIEWParameterElement.ArrayDimensions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-arraydimensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-arraydimensions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ArrayDimensions Data Type Long Purpose Returns the number of dimensions for array parameters. See Also LabVIEWParameterElement.GetArrayIndex LabVIEWParameterElement.GetDefaultArrayDimensionSize

### LabVIEWParameterElement.ArrayDimensions

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ArrayDimensions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of dimensions for array parameters.

#### See Also

[LabVIEWParameterElement.GetArrayIndex](labviewparameterelement-getarrayindex.html)

[LabVIEWParameterElement.GetDefaultArrayDimensionSize](labviewparameterelement-getdefaultarraydimens.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-arrayelementprototype.html language=enus -->
## TOPIC 01568: LabVIEWParameterElement.ArrayElementPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-arrayelementprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-arrayelementprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ArrayElementPrototype Data Type LabVIEWParameterElement Purpose Returns the cluster prototype for the elements of the array. Remarks This property is valid only for arrays of LabVIEW clusters. Call the LabVIEWParameterElement.Category property to determine whether the

### LabVIEWParameterElement.ArrayElementPrototype

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ArrayElementPrototype

#### Data Type

[LabVIEWParameterElement](labviewparameterelement.html)

#### Purpose

Returns the cluster prototype for the elements of the array.

#### Remarks

This property is valid only for arrays of LabVIEW clusters. Call the
 [LabVIEWParameterElement.Category](labviewparameterelement-category.html)
 property to determine whether the parameter is an array of LabVIEW clusters. The array element prototype is a template from which new elements are copied when the size of the array increases. The array element prototype represents the expected structure of elements of the array. You can also use the array element prototype to create a TestStand custom data type that maps to the LabVIEW cluster.

#### See Also

[LabVIEWParameterElement](labviewparameterelement.html)

[LabVIEWParameterElement.Category](labviewparameterelement-category.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-aspropertyobject.html language=enus -->
## TOPIC 01569: LabVIEWParameterElement.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the LabVIEWParameterElement object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### LabVIEWParameterElement.AsPropertyObject

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the LabVIEWParameterElement object.

#### Remarks

Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-category.html language=enus -->
## TOPIC 01570: LabVIEWParameterElement.Category

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-category.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-category.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.Category Data Type LabVIEWParameterCategories Purpose Returns which group of data types (number, string, and so on) to which the parameter element belongs. Remarks After obtaining the category of the parameter, you can obtain the data type with the LabVIEWParameterElem

### LabVIEWParameterElement.Category

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).Category

#### Data Type

[LabVIEWParameterCategories](labviewparametercategories.html)

#### Purpose

Returns which group of data types (number, string, and so on) to which the parameter element belongs.

#### Remarks

After obtaining the
 [category](labviewparametercategories.html)
 of the parameter, you can obtain the data type with the
 [LabVIEWParameterElement.Type](labviewparameterelement-type.html)
 property.

#### See Also

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-compleximaginaryparte.html language=enus -->
## TOPIC 01571: LabVIEWParameterElement.ComplexImaginaryPartElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-compleximaginaryparte.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-compleximaginaryparte.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ComplexImaginaryPartElement Data Type LabVIEWParameterElement Purpose Returns the imaginary part element of a complex number or array. Remarks This method is valid only for a complex number or an array of complex number parameter elements. See Also LabVIEWParameterElem

### LabVIEWParameterElement.ComplexImaginaryPartElement

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ComplexImaginaryPartElement

#### Data Type

[LabVIEWParameterElement](labviewparameterelement.html)

#### Purpose

Returns the imaginary part element of a complex number or array.

#### Remarks

This method is valid only for a complex number or an array of complex number parameter elements.

#### See Also

[LabVIEWParameterElement](labviewparameterelement.html)

[LabVIEWParameterElement.ComplexRealPartElement](labviewparameterelement-complexrealpartelemen.html)

[LabVIEWParameterElement.Elements](labviewparameterelement-elements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-complexrealpartelemen.html language=enus -->
## TOPIC 01572: LabVIEWParameterElement.ComplexRealPartElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-complexrealpartelemen.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-complexrealpartelemen.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ComplexRealPartElement Data Type LabVIEWParameterElement Purpose Returns the real part element of a complex number or array. Remarks This method is valid only for a complex number and array of complex number parameter elements. See Also LabVIEWParameterElement LabVIEWP

### LabVIEWParameterElement.ComplexRealPartElement

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ComplexRealPartElement

#### Data Type

[LabVIEWParameterElement](labviewparameterelement.html)

#### Purpose

Returns the real part element of a complex number or array.

#### Remarks

This method is valid only for a complex number and array of complex number parameter elements.

#### See Also

[LabVIEWParameterElement](labviewparameterelement.html)

[LabVIEWParameterElement.ComplexImaginaryPartElement](labviewparameterelement-compleximaginaryparte.html)

[LabVIEWParameterElement.Elements](labviewparameterelement-elements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-createdefaultarrayele.html language=enus -->
## TOPIC 01573: LabVIEWParameterElement.CreateDefaultArrayElements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-createdefaultarrayele.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-createdefaultarrayele.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.CreateDefaultArrayElements Return Value Boolean Returns a value that indicates whether the default array elements were created. Purpose Creates all the default array elements of an array parameter element. Remarks This method is valid only on array parameter elements a

### LabVIEWParameterElement.CreateDefaultArrayElements

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).CreateDefaultArrayElements

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the default array elements were created.

#### Purpose

Creates all the default array elements of an array parameter element.

#### Remarks

This method is valid only on array parameter elements and creates the elements only if the array control on the VI front panel defines default. TestStand replaces any existing array elements the parameter previously specified.

#### See Also

[LabVIEWParameterElement.DeleteArrayElements](labviewparameterelement-deletearrayelements.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-defaultvalue.html language=enus -->
## TOPIC 01574: LabVIEWParameterElement.DefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-defaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.DefaultValue Data Type String Purpose Returns a display string that represents the default value defined for the parameter element. Remarks Default values apply only to recommended and optional parameters. You must call the LabVIEWModule.LoadVIInfo or Module.LoadProtot

### LabVIEWParameterElement.DefaultValue

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).DefaultValue

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a display string that represents the default value defined for the parameter element.

#### Remarks

Default values apply only to recommended and optional parameters. You must call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving the default value. Otherwise, TestStand returns an empty string. The values stay in memory until the sequence file closes.

#### See Also

[LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)

[LabVIEWParameterElement.UseDefaultValue](labviewparameterelement-usedefaultvalue.html)

[LabVIEWParameterElement.ValueExpr](labviewparameterelement-valueexpr.html)

[LabVIEWParameterElement.WireRequirement](labviewparameterelement-wirerequirement.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-deletearrayelement.html language=enus -->
## TOPIC 01575: LabVIEWParameterElement.DeleteArrayElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-deletearrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-deletearrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.DeleteArrayElement( index) Purpose Deletes the array element at the given index. Remarks This method is valid only for one-dimensional array parameter elements. Use the LabVIEWParameterElement.ArrayDimensions property to determine the number of array dimensions. Parame

### LabVIEWParameterElement.DeleteArrayElement

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).DeleteArrayElement( index)

#### Purpose

Deletes the array element at the given index.

#### Remarks

This method is valid only for one-dimensional array parameter elements. Use the
 [LabVIEWParameterElement.ArrayDimensions](labviewparameterelement-arraydimensions.html)
 property to determine the number of array dimensions.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index at which to delete the array element. This value must be greater than or equal to
 0
 and less than the number of array elements.

#### See Also

[LabVIEWParameterElement.ArrayDimensions](labviewparameterelement-arraydimensions.html)

[LabVIEWParameterElement.DeleteArrayElements](labviewparameterelement-deletearrayelements.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-deletearrayelements.html language=enus -->
## TOPIC 01576: LabVIEWParameterElement.DeleteArrayElements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-deletearrayelements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-deletearrayelements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.DeleteArrayElements Return Value Boolean Purpose Deletes all array elements. Remarks This method is valid only on array parameter elements. See Also LabVIEWParameterElement.DeleteArrayElement LabVIEWParameterElement.InsertArrayElement LabVIEWParameterElement.Type

### LabVIEWParameterElement.DeleteArrayElements

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).DeleteArrayElements

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Deletes all array elements.

#### Remarks

This method is valid only on array parameter elements.

#### See Also

[LabVIEWParameterElement.DeleteArrayElement](labviewparameterelement-deletearrayelement.html)

[LabVIEWParameterElement.InsertArrayElement](labviewparameterelement-insertarrayelement.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-direction.html language=enus -->
## TOPIC 01577: LabVIEWParameterElement.Direction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-direction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-direction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.Direction Data Type LabVIEWParameterDirections Use the following constants with this data type: LVParamDirection_In –(Value: 0) Indicates that the parameter is passed to the VI. LVParamDirection_Out –(Value: 1) Indicates that the parameter is returned from the VI. Purp

### LabVIEWParameterElement.Direction

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).Direction

#### Data Type

[LabVIEWParameterDirections](labviewparameterdirections.html)

Use the following constants with this data type:

- LVParamDirection_In 
 –(Value: 0) Indicates that the parameter is passed to the VI.
- LVParamDirection_Out 
 –(Value: 1) Indicates that the parameter is returned from the VI.

#### Purpose

Returns a value that indicates whether the parameter is an input or output parameter.

#### Remarks

This method is for convenience and returns the same value the
 [LabVIEWParameter.Direction](labviewparameter-direction.html)
 property returns when called on the parent LabVIEWParameter object.

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

#### See Also

[LabVIEWParameter.Direction](labviewparameter-direction.html)

[LabVIEWParameterDirections](labviewparameterdirections.html)

[LabVIEWParameterElement.WireRequirement](labviewparameterelement-wirerequirement.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-displaycreatecustomda.html language=enus -->
## TOPIC 01578: LabVIEWParameterElement.DisplayCreateCustomDataTypeDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-displaycreatecustomda.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-displaycreatecustomda.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.DisplayCreateCustomDataTypeDialog( sequenceContext) Return Value Boolean Returns True if you click OK in the dialog box. False if you click Cancel . Purpose Launches the Create/Update Custom Data Type from Cluster dialog box, in which you configure a new custom data ty

### LabVIEWParameterElement.DisplayCreateCustomDataTypeDialog

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).DisplayCreateCustomDataTypeDialog( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box.
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Create/Update Custom Data Type from Cluster](../tsref/create-update-custom-data-type-from-cluster-d.html)
 dialog box, in which you configure a new custom data type or update an existing custom type.

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context the dialog box uses to obtain information about the sequence file. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context.

#### See Also

[Create/Update Custom Data Type from Cluster dialog box](../tsref/create-update-custom-data-type-from-cluster-d.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-displaytype.html language=enus -->
## TOPIC 01579: LabVIEWParameterElement.DisplayType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-displaytype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-displaytype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.DisplayType Data Type String The display value of the data type of the parameter. Purpose Returns a localized string that describes the LabVIEW data type for the parameter element. Remarks The LabVIEW Adapter persists this property value when you specify a code module

### LabVIEWParameterElement.DisplayType

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).DisplayType

#### Data Type

[String](data-types-for-teststand.html)

The display value of the data type of the parameter.

#### Purpose

Returns a localized string that describes the LabVIEW data type for the parameter element.

#### Remarks

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before you retrieve this property value.

#### See Also

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-elementcaption.html language=enus -->
## TOPIC 01580: LabVIEWParameterElement.ElementCaption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-elementcaption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-elementcaption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ElementCaption Data Type String Purpose Returns the caption of the parameter element in the VI. Remarks Use the LabVIEWParameterElement.ElementName property to determine the label or name of the parameter element. See Also LabVIEWParameterElement.ElementName Module.Loa

### LabVIEWParameterElement.ElementCaption

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ElementCaption

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the caption of the parameter element in the VI.

#### Remarks

Use the
 [LabVIEWParameterElement.ElementName](labviewparameterelement-elementname.html)
 property to determine the label or name of the parameter element.

#### See Also

[LabVIEWParameterElement.ElementName](labviewparameterelement-elementname.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-elementname.html language=enus -->
## TOPIC 01581: LabVIEWParameterElement.ElementName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-elementname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-elementname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ElementName Data Type String Purpose Returns the name of the parameter element in the cluster. Returns an error for array elements. Remarks The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must cal

### LabVIEWParameterElement.ElementName

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ElementName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the parameter element in the cluster. Returns an error for array elements.

#### Remarks

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [Module.LoadPrototype](module-loadprototype.html)
 method before retrieving this property.

Use the
 [LabVIEWParameterElement.ElementCaption](labviewparameterelement-elementcaption.html)
 property to determine the caption of the parameter.

#### See Also

[LabVIEWParameterElement.ElementCaption](labviewparameterelement-elementcaption.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-elements.html language=enus -->
## TOPIC 01582: LabVIEWParameterElement.Elements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-elements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-elements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.Elements Data Type LabVIEWParameterElements Purpose If a parameter element is a cluster or array of clusters, this property returns a collection to access sub-elements of the parameter element. See Also LabVIEWParameterElements

### LabVIEWParameterElement.Elements

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).Elements

#### Data Type

[LabVIEWParameterElements](labviewparameterelements.html)

#### Purpose

If a parameter element is a cluster or array of clusters, this property returns a collection to access sub-elements of the parameter element.

#### See Also

[LabVIEWParameterElements](labviewparameterelements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-exprclustertypemismat.html language=enus -->
## TOPIC 01583: LabVIEWParameterElement.ExprClusterTypeMismatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-exprclustertypemismat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-exprclustertypemismat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ExprClusterTypeMismatch( sequenceContext) Return Value Boolean Purpose Returns True if you enable cluster mapping for the variable or property the expression value returns and the names or types of cluster elements do not match the LabVIEW cluster the VI specifies. Oth

### LabVIEWParameterElement.ExprClusterTypeMismatch

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ExprClusterTypeMismatch( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if you enable cluster mapping for the variable or property the expression value returns and the names or types of cluster elements do not match the LabVIEW cluster the VI specifies. Otherwise this method returns
 False
 .

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the SequenceContext to use to evaluate the parameter expression value.

#### See Also

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

[LabVIEWParameterElement.ValueExpr](labviewparameterelement-valueexpr.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-getarrayindex.html language=enus -->
## TOPIC 01584: LabVIEWParameterElement.GetArrayIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-getarrayindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-getarrayindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.GetArrayIndex( offset, options) Return Value String An array index string. Array index strings are a list of numbers enclosed in brackets that index each dimension of the array. For example, the following is an array index for a two dimensional array: [0][1] . Purpose

### LabVIEWParameterElement.GetArrayIndex

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).GetArrayIndex( offset, options)

#### Return Value

[String](data-types-for-teststand.html)

An array index string. Array index strings are a list of numbers enclosed in brackets that index each dimension of the array. For example, the following is an array index for a two dimensional array:
 [0][1]
 .

#### Purpose

Returns the index of the array element the
 offset
 parameter specifies.

#### Parameters

offset
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based number representing the offset of an array element in the one-dimensional physical storage of the array. The offset is in terms of the number of elements.

options
 As
 [Long](data-types-for-teststand.html)

[In] Reserved for future use. Pass
 0
 .

#### See Also

[LabVIEWParameterElement.ArrayDimensions](labviewparameterelement-arraydimensions.html)

[LabVIEWParameterElement.GetDefaultArrayDimensionSize](labviewparameterelement-getdefaultarraydimens.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-getdefaultarraydimens.html language=enus -->
## TOPIC 01585: LabVIEWParameterElement.GetDefaultArrayDimensionSize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-getdefaultarraydimens.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-getdefaultarraydimens.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.GetDefaultArrayDimensionSize( dimension) Return Value Long Purpose Returns the default size of the array corresponding to the zero-based index passed as input. Remarks The default size corresponds to the default size of the array control in the front panel of a VI. Cal

### LabVIEWParameterElement.GetDefaultArrayDimensionSize

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).GetDefaultArrayDimensionSize( dimension)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Returns the default size of the array corresponding to the zero-based index passed as input.

#### Remarks

The default size corresponds to the default size of the array control in the front panel of a VI. Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 or
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method.

#### Parameters

dimension
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index corresponding to one of the array dimensions.

#### See Also

[LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)

[LabVIEWParameterElement.ArrayDimensions](labviewparameterelement-arraydimensions.html)

[LabVIEWParameterElement.GetArrayIndex](labviewparameterelement-getarrayindex.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-getenumvalues.html language=enus -->
## TOPIC 01586: LabVIEWParameterElement.GetEnumValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-getenumvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-getenumvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.GetEnumValues Return Value Object Array Returns an array of property objects where each property object represents an enumeration value or a ring control value. Purpose Returns the enumeration constants for an enumeration parameter or returns the ring control values fo

### LabVIEWParameterElement.GetEnumValues

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).GetEnumValues

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns an array of property objects where each property object represents an enumeration value or a ring control value.

#### Purpose

Returns the enumeration constants for an enumeration parameter or returns the ring control values for a ring control parameter.

#### Remarks

Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 method or the
 [Module.LoadPrototype](module-loadprototype.html)
 method before calling this method. The values stay in memory until the sequence file closes.

Note

Use the name and value of the property objects in the array this method returns to determine the name and value of the enumeration constants or ring controls.

Pass the return value of this method as the
 additionalConstants
 parameter of
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 when checking the
 [LabVIEWParameterElement.ValueExpr](labviewparameterelement-valueexpr.html)
 property for errors.

If you are using an
 
 [ExpressionEdit](../tsuiref/expressionedit.html)
 control to display the value of the
 LabVIEWParameterElement.ValueExpr
 property, pass the return value of this method to the
 
 [ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)
 method to instruct the ExpressionEdit control to validate enumeration constants.

#### See Also

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

[LabVIEWParameterElement.ValueExpr](labviewparameterelement-valueexpr.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-indexstring.html language=enus -->
## TOPIC 01587: LabVIEWParameterElement.IndexString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-indexstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-indexstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.IndexString Data Type String Purpose Returns a string that specifies the multi-dimensional array index of the parameter element in the parent LabVIEWParameterElements object. Remarks You can use this array index string to display the index of an array parameter. See Al

### LabVIEWParameterElement.IndexString

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).IndexString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a string that specifies the multi-dimensional array index of the parameter element in the parent
 [LabVIEWParameterElements](labviewparameterelements.html)
 object.

#### Remarks

You can use this array index string to display the index of an array parameter.

#### See Also

[LabVIEWParameterElements](labviewparameterelements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-insertarrayelement.html language=enus -->
## TOPIC 01588: LabVIEWParameterElement.InsertArrayElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-insertarrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-insertarrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.InsertArrayElement( index) Purpose Inserts an array element at the specified index. Remarks This method is valid only for one-dimensional array parameter elements. Use the LabVIEWParameterElement.ArrayDimensions property to determine the number of array dimensions. Par

### LabVIEWParameterElement.InsertArrayElement

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).InsertArrayElement( index)

#### Purpose

Inserts an array element at the specified index.

#### Remarks

This method is valid only for one-dimensional array parameter elements. Use the
 [LabVIEWParameterElement.ArrayDimensions](labviewparameterelement-arraydimensions.html)
 property to determine the number of array dimensions.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index at which to insert the array element. This value must be greater than or equal to
 0
 and less than or equal to the number of array elements.

#### See Also

[LabVIEWParameterElement.ArrayDimensions](labviewparameterelement-arraydimensions.html)

[LabVIEWParameterElement.DeleteArrayElement](labviewparameterelement-deletearrayelement.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-isclustermappinginval.html language=enus -->
## TOPIC 01589: LabVIEWParameterElement.IsClusterMappingInvalid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-isclustermappinginval.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-isclustermappinginval.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.IsClusterMappingInvalid( reasonNotValid) Return Value Boolean Returns True when all the following conditions are true: The parameter is a cluster or cluster array The argument expression is valid and non-empty The argument or cluster mapping of the argument is invalid

### LabVIEWParameterElement.IsClusterMappingInvalid

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).IsClusterMappingInvalid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when all the following conditions are true:

- The parameter is a cluster or cluster array
- The argument expression is valid and non-empty
- The argument or cluster mapping of the argument is invalid

In all other cases, this method returns
 False
 .

#### Purpose

Returns a value that indicates whether the argument you specify for a LabVIEW cluster or cluster array parameter is valid by checking the cluster passing information for any custom data types used to confirm that the information matches the cluster definition stored when you specified the module.

Note

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] When this method returns
 True
 , this parameter returns the reason why the argument is invalid.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-isnodeusingdefault.html language=enus -->
## TOPIC 01590: LabVIEWParameterElement.IsNodeUsingDefault

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-isnodeusingdefault.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-isnodeusingdefault.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.IsNodeUsingDefault Data Type Boolean Returns True when the parameter is associated with a LabVIEW property configured to use the default value. Purpose Returns a value that indicates whether the parameter is associated with a LabVIEW property configured to use the defa

### LabVIEWParameterElement.IsNodeUsingDefault

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).IsNodeUsingDefault

#### Data Type

[Boolean](data-types-for-teststand.html)

Returns
 True
 when the parameter is associated with a LabVIEW property configured to use the default value.

#### Purpose

Returns a value that indicates whether the parameter is associated with a LabVIEW property configured to use the default value in a Property Node call.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-isparametermappingval.html language=enus -->
## TOPIC 01591: LabVIEWParameterElement.IsParameterMappingValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-isparametermappingval.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-isparametermappingval.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.IsParameterMappingValid( reasonNotValid) Return Value Boolean Returns True when all the following conditions are true: the parameter is a cluster or cluster array or enumeration or enumeration array, the argument expression is valid and not empty, the cluster mapping o

### LabVIEWParameterElement.IsParameterMappingValid

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).IsParameterMappingValid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when all the following conditions are true:

1. the parameter is a cluster or cluster array or enumeration or enumeration array,
2. the argument expression is valid and not empty,
3. the cluster mapping of the argument is valid if the parameter is a cluster, and
4. the argument value is compatible with the enumeration parameter if the parameter is an enumeration.

In all other cases, returns
 False
 .

#### Purpose

Returns a value that indicates whether the argument you specify for a LabVIEW cluster or cluster array parameter is valid.

#### Remarks

This method checks the cluster passing information for any custom data types used and confirms that the information matches the cluster definition stored when you specified the module. For an enumeration parameter, the method validates that:

1. If the argument is a number or TestStand enumeration type instance, the numeric representation is compatible with the LabVIEW parameters representation.
2. If the argument is a TestStand enumeration type, the enumerators of the TestStand type must match the enumerators of the LabVIEW parameter in
  - Number 
 and
  - Name and value 
 .

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] When this method returns
 False
 , this parameter returns an explanation for why the argument is invalid.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-partiallyspecified.html language=enus -->
## TOPIC 01592: LabVIEWParameterElement.PartiallySpecified

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-partiallyspecified.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-partiallyspecified.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.PartiallySpecified Data Type Boolean Purpose Returns a value that indicates whether the parameter element is partially specified. Remarks A parameter element is partially specified if some of the parameter elements specify to use default values while other parameter el

### LabVIEWParameterElement.PartiallySpecified

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).PartiallySpecified

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the parameter element is partially specified.

#### Remarks

A parameter element is partially specified if some of the parameter elements specify to use default values while other parameter elements specify expression values.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-passasbinarystring.html language=enus -->
## TOPIC 01593: LabVIEWParameterElement.PassAsBinaryString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-passasbinarystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-passasbinarystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.PassAsBinaryString Data Type Boolean Purpose Specifies if TestStand preserves NUL bytes when setting and getting LabVIEW string data. Remarks This property applies only when the LabVIEWParameterElement.Category property of the parameter is LVParamCategory_String or LVP

### LabVIEWParameterElement.PassAsBinaryString

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).PassAsBinaryString

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if TestStand preserves NUL bytes when setting and getting LabVIEW string data.

#### Remarks

This property applies only when the
 [LabVIEWParameterElement.Category](labviewparameterelement-category.html)
 property of the parameter is
 LVParamCategory_String
 or
 LVParamCategory_StringArray
 and the
 [LabVIEWParameterElement.Type](labviewparameterelement-type.html)
 property of the parameter is
 LVParamType_String
 .

TestStand
 [handles the string data in different ways](../tsref/string-parameters-labview-vi-call-parameters.html)
 depending on the version of LabVIEW you are using.

When this property is
 False
 , the LabVIEW Adapter treats strings as C-style strings with a NUL character to indicate the end of the string. C-strings cannot contain binary data.

Call the
 [PropertyObject.GetValBinary](propertyobject-getvalbinary.html)
 method on the variable that stores the binary string to retrieve the raw data in TestStand when the binary data is compressed.

#### See Also

[LabVIEWParameterCategories](labviewparametercategories.html)

[LabVIEWParameterElement.Category](labviewparameterelement-category.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

[LabVIEWParameterTypes](labviewparametertypes.html)

[PropertyObject.GetValBinary](propertyobject-getvalbinary.html)

[String Parameters](../tsref/string-parameters-labview-vi-call-parameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-type.html language=enus -->
## TOPIC 01594: LabVIEWParameterElement.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.Type Data Type LabVIEWParameterTypes Purpose Returns the data type of the parameter element. It specifically indicates what type of number, string, etc. Remarks Obtain the category using the LabVIEWParameterElement.Category property before obtaining the data type of th

### LabVIEWParameterElement.Type

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).Type

#### Data Type

[LabVIEWParameterTypes](labviewparametertypes.html)

#### Purpose

Returns the data type of the parameter element. It specifically indicates what type of number, string, etc.

#### Remarks

Obtain the
 [category](labviewparametercategories.html)
 using the
 [LabVIEWParameterElement.Category](labviewparameterelement-category.html)
 property before obtaining the data type of the parameter.

#### See Also

[LabVIEWParameterCategories](labviewparametercategories.html)

[LabVIEWParameterElement.Category](labviewparameterelement-category.html)

[LabVIEWParameterTypes](labviewparametertypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-typedisplaystring.html language=enus -->
## TOPIC 01595: LabVIEWParameterElement.TypeDisplayString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-typedisplaystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-typedisplaystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.TypeDisplayString Data Type String Purpose Returns a string that describes the type of the parameter element. See Also LabVIEWParameterElement.Type

### LabVIEWParameterElement.TypeDisplayString

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).TypeDisplayString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a string that describes the type of the parameter element.

#### See Also

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-updateclustermapping.html language=enus -->
## TOPIC 01596: LabVIEWParameterElement.UpdateClusterMapping

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-updateclustermapping.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-updateclustermapping.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.UpdateClusterMapping( sequenceContext) Return Value Boolean Returns True if the method updates any expression values for the elements of the cluster parameter element. Purpose Updates the expression values for all the cluster parameter elements when the parameter speci

### LabVIEWParameterElement.UpdateClusterMapping

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).UpdateClusterMapping( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the method updates any expression values for the elements of the cluster parameter element.

#### Purpose

Updates the expression values for all the cluster parameter elements when the parameter specifies an expression value that evaluates to a named data type and the data type enables cluster passing.

#### Remarks

This method is valid only on cluster parameter elements.

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context that the dialog box uses to evaluate all value expressions. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context.

#### See Also

[Engine.NewEditContext](engine-neweditcontext.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-usedefaultvalue.html language=enus -->
## TOPIC 01597: LabVIEWParameterElement.UseDefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-usedefaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-usedefaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.UseDefaultValue Data Type Boolean Purpose Specifies to use the default value of the parameter element when calling the VI. Remarks You can use the default value when a parameter is recommended or optional. See Also LabVIEWParameterElement.PartiallySpecified LabVIEWPara

### LabVIEWParameterElement.UseDefaultValue

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).UseDefaultValue

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies to use the default value of the parameter element when calling the VI.

#### Remarks

You can use the default value when a parameter is recommended or optional.

#### See Also

[LabVIEWParameterElement.PartiallySpecified](labviewparameterelement-partiallyspecified.html)

[LabVIEWParameterElement.ValueExpr](labviewparameterelement-valueexpr.html)

[LabVIEWParameterElement.WireRequirement](labviewparameterelement-wirerequirement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-userdata.html language=enus -->
## TOPIC 01598: LabVIEWParameterElement.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.UserData Data Type PropertyObject Purpose Holds a data item you associate with the parameter object. Remarks Typically, you do not use this property. See Also PropertyObject

### LabVIEWParameterElement.UserData

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).UserData

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Holds a data item you associate with the parameter object.

#### Remarks

Typically, you do not use this property.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-validevaluationtypes.html language=enus -->
## TOPIC 01599: LabVIEWParameterElement.ValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-validevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-validevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ValidEvaluationTypes Data Type EvaluationTypes Purpose Returns the valid types to which this parameter can evaluate. Remarks You can pass the value of this property to the validEvaluationTypes parameter of the Expression.ValidateEvaluationType method to determine wheth

### LabVIEWParameterElement.ValidEvaluationTypes

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ValidEvaluationTypes

#### Data Type

[EvaluationTypes](evaluationtypes.html)

#### Purpose

Returns the valid types to which this parameter can evaluate.

#### Remarks

You can pass the value of this property to the
 validEvaluationTypes
 parameter of the
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method to determine whether the value of the
 [LabVIEWParameterElement.ValueExpr](labviewparameterelement-valueexpr.html)
 property contains errors.

If you are using an ExpressionEdit control to display the value of the
 LabVIEWParameterElement.ValueExpr
 property, pass the value of this property to the
 
 [ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)
 method.

#### See Also

[EvaluationTypes](evaluationtypes.html)

[EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.GetValidEvaluationTypes](../tsuiref/expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-valueexpr.html language=enus -->
## TOPIC 01600: LabVIEWParameterElement.ValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-valueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-valueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ValueExpr Data Type String Purpose Specifies an expression to define the argument to pass for the cluster member or cluster array element when calling the VI. Remarks Each cluster member or cluster array element can be passed to LabVIEW individually, or the entire clus

### LabVIEWParameterElement.ValueExpr

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression to define the argument to pass for the cluster member or cluster array element when calling the VI.

#### Remarks

Each cluster member or cluster array element can be passed to LabVIEW individually, or the entire cluster/array can be passed as a TestStand data type.

Call the
 [LabVIEWModule.LoadVIInfo](labviewmodule-loadviinfo.html)
 method before you get or set this property to ensure that LabVIEW parameters, such as clusters and arrays, are updated with their current definitions.

#### See Also

[LabVIEWParameter.UseDefaultValue](labviewparameter-usedefaultvalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-valueexprisignored.html language=enus -->
## TOPIC 01601: LabVIEWParameterElement.ValueExprIsIgnored

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-valueexprisignored.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-valueexprisignored.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ValueExprIsIgnored Data Type Boolean Purpose Use this property to determine whether the LabVIEW Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameter elements that belong to a parameter t

### LabVIEWParameterElement.ValueExprIsIgnored

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ValueExprIsIgnored

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the LabVIEW Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameter elements that belong to a parameter that uses default values or that has a non-empty value expression.

#### See Also

[LabVIEWParameterElement.UseDefaultValue](labviewparameterelement-usedefaultvalue.html)

[LabVIEWParameterElement.ValueExpr](labviewparameterelement-valueexpr.html)

[LabVIEWParameterElement.ValueExprIsOptional](labviewparameterelement-valueexprisoptional.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-valueexprisoptional.html language=enus -->
## TOPIC 01602: LabVIEWParameterElement.ValueExprIsOptional

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-valueexprisoptional.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-valueexprisoptional.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.ValueExprIsOptional Data Type Boolean Purpose Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for output parameters and value ex

### LabVIEWParameterElement.ValueExprIsOptional

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).ValueExprIsOptional

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for output parameters and value expressions for cluster and array parameters that have parameter elements are optional.

#### See Also

[LabVIEWParameterElement.Direction](labviewparameterelement-direction.html)

[LabVIEWParameterElement.ValueExpr](labviewparameterelement-valueexpr.html)

[LabVIEWParameterElement.ValueExprIsIgnored](labviewparameterelement-valueexprisignored.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement-wirerequirement.html language=enus -->
## TOPIC 01603: LabVIEWParameterElement.WireRequirement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement-wirerequirement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement-wirerequirement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElement.WireRequirement Data Type LabVIEWParameterWireRequirements Use the following constants with this data type: LVParamWireReq_Optional –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value. LVParamWireReq_Recommended

### LabVIEWParameterElement.WireRequirement

#### Syntax

[LabVIEWParameterElement](labviewparameterelement.html).WireRequirement

#### Data Type

[LabVIEWParameterWireRequirements](labviewparameterwirerequirements.html)

Use the following constants with this data type:

- LVParamWireReq_Optional 
 –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value.
- LVParamWireReq_Recommended 
 –(Value: 1) Indicates that the module can use the default value for the parameter. However, passing a value is recommended.
- LVParamWireReq_Required 
 –(Value: 0) Indicates that the module must pass a value for the parameter.

#### Purpose

Indicates whether the parameter is required, recommended, or optional.

#### Remarks

This method is for convenience and returns the same value the
 [LabVIEWParameter.WireRequirement](labviewparameter-wirerequirement.html)
 property returns when called on the parent LabVIEWParameter object.

The LabVIEW Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call
 [Module.LoadPrototype](module-loadprototype.html)
 before retrieving this property.

#### See Also

[LabVIEWParameter.WireRequirement](labviewparameter-wirerequirement.html)

[LabVIEWParameterElement.Direction](labviewparameterelement-direction.html)

[LabVIEWParameterWireRequirements](labviewparameterwirerequirements.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelement.html language=enus -->
## TOPIC 01604: LabVIEWParameterElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWParameterElement class to configure and obtain element-specific information in a cluster or array parameter of a module. Use the LabVIEWParameter.Elements property to obtain the collection of elements for a parameter of a module. Properties ArrayDimensions (Read Only) Arr

### LabVIEWParameterElement

Use objects from the LabVIEWParameterElement class to configure and obtain element-specific information in a cluster or array parameter of a module.

Use the
 [LabVIEWParameter.Elements](labviewparameter-elements.html)
 property to obtain the collection of elements for a parameter of a module.

#### Properties

| ArrayDimensions (Read Only) |
| --- |
| ArrayElementPrototype (Read Only) |
| Category (Read Only) |
| ComplexImaginaryPartElement (Read Only) |
| ComplexRealPartElement (Read Only) |
| DefaultValue (Read Only) |
| Direction (Read Only) |
| DisplayType (Read Only) |
| ElementCaption (Read Only) |
| ElementName (Read Only) |
| Elements (Read Only) |
| IndexString (Read Only) |
| IsNodeUsingDefault |
| PartiallySpecified (Read Only) |
| PassAsBinaryString |
| Type (Read Only) |
| TypeDisplayString (Read Only) |
| UseDefaultValue |
| UserData (Read Only) |
| ValidEvaluationTypes (Read Only) |
| ValueExpr |
| ValueExprIsIgnored (Read Only) |
| ValueExprIsOptional (Read Only) |
| WireRequirement (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| CreateDefaultArrayElements |
| DeleteArrayElement |
| DeleteArrayElements |
| DisplayCreateCustomDataTypeDialog |
| ExprClusterTypeMismatch |
| GetArrayIndex |
| GetDefaultArrayDimensionSize |
| GetEnumValues |
| InsertArrayElement |
| IsClusterMappingInvalid |
| IsParameterMappingValid |
| UpdateClusterMapping |

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWParameter.Elements](labviewparameter-elements.html)

[LabVIEWParameterElements](labviewparameterelements.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelements-count.html language=enus -->
## TOPIC 01605: LabVIEWParameterElements.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelements-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelements-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElements.Count Data Type Long Purpose Returns the number of items in the collection. See Also LabVIEWParameterElement

### LabVIEWParameterElements.Count

#### Syntax

[LabVIEWParameterElements](labviewparameterelements.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[LabVIEWParameterElement](labviewparameterelement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelements-item.html language=enus -->
## TOPIC 01606: LabVIEWParameterElements.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelements-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelements-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameterElements.Item( index) Data Type LabVIEWParameterElement Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index. See Also LabVIEWParameterElement

### LabVIEWParameterElements.Item

#### Syntax

[LabVIEWParameterElements](labviewparameterelements.html).Item( index)

#### Data Type

[LabVIEWParameterElement](labviewparameterelement.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index.

#### See Also

[LabVIEWParameterElement](labviewparameterelement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterelements.html language=enus -->
## TOPIC 01607: LabVIEWParameterElements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterelements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterelements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWParameterElements class to configure and obtain elements for a cluster or array parameter of a module that uses the LabVIEW Adapter. Use the LabVIEWParameter.Elements property to obtain the collection of elements for a parameter of a module and the LabVIEWParameterElement

### LabVIEWParameterElements

Use objects from the LabVIEWParameterElements class to configure and obtain elements for a cluster or array parameter of a module that uses the LabVIEW Adapter. Use the
 [LabVIEWParameter.Elements](labviewparameter-elements.html)
 property to obtain the collection of elements for a parameter of a module and the
 [LabVIEWParameterElement.Elements](labviewparameterelement-elements.html)
 property to obtain the collection of sub-elements for a parameter element.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWParameter.Elements](labviewparameter-elements.html)

[LabVIEWParameterElement](labviewparameterelement.html)

[LabVIEWParameterElement.Elements](labviewparameterelement-elements.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameters-count.html language=enus -->
## TOPIC 01608: LabVIEWParameters.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameters-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameters-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameters.Count Data Type Long Purpose Returns the number of items in the collection. See Also LabVIEWParameter

### LabVIEWParameters.Count

#### Syntax

[LabVIEWParameters](labviewparameters.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[LabVIEWParameter](labviewparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameters-item.html language=enus -->
## TOPIC 01609: LabVIEWParameters.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameters-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameters-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameters.Item( index) Data Type LabVIEWParameter Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the parameter to retrieve. See Also LabVIEWParameter

### LabVIEWParameters.Item

#### Syntax

[LabVIEWParameters](labviewparameters.html).Item( index)

#### Data Type

[LabVIEWParameter](labviewparameter.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to retrieve.

#### See Also

[LabVIEWParameter](labviewparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameters-newarguments.html language=enus -->
## TOPIC 01610: LabVIEWParameters.NewArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameters-newarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameters-newarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWParameters.NewArguments Return Value LabVIEWArguments Purpose Creates and returns a new LabVIEWArguments collection. Use this collection to pass argument values to a LabVIEW module using the LabVIEWModule.Execute method. Remarks The new collection contains the same number of items as t

### LabVIEWParameters.NewArguments

#### Syntax

[LabVIEWParameters](labviewparameters.html).NewArguments

#### Return Value

[LabVIEWArguments](labviewarguments.html)

#### Purpose

Creates and returns a new
 [LabVIEWArguments](labviewarguments.html)
 collection. Use this collection to pass argument values to a LabVIEW module using the
 [LabVIEWModule.Execute](labviewmodule-execute.html)
 method.

#### Remarks

The new collection contains the same number of items as the
 [LabVIEWParameters](labviewparameters.html)
 collection. To pass a argument value to a VI parameter, set the
 [LabVIEWArgument.Value](labviewargument-value.html)
 property on the item in the
 LabVIEWArguments
 collection that has the same index as the parameter in the
 LabVIEWParameters
 collection.

#### See Also

[LabVIEWArgument.Value](labviewargument-value.html)

[LabVIEWArguments](labviewarguments.html)

[LabVIEWModule.Execute](labviewmodule-execute.html)

[LabVIEWParameters](labviewparameters.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameters.html language=enus -->
## TOPIC 01611: LabVIEWParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the LabVIEWParameters class to configure and obtain parameters for a module that uses the LabVIEW Adapter. Use the LabVIEWModule.Parameters property to obtain the collection of parameters for a module. Properties Count (Read Only) Item (Read Only) Method NewArguments See Also Effect

### LabVIEWParameters

Use objects from the LabVIEWParameters class to configure and obtain parameters for a module that uses the LabVIEW Adapter. Use the
 [LabVIEWModule.Parameters](labviewmodule-parameters.html)
 property to obtain the collection of parameters for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Method

| NewArguments |
| --- |

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWModule.Parameters](labviewmodule-parameters.html)

[LabVIEWParameter](labviewparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparametertypes.html language=enus -->
## TOPIC 01612: LabVIEWParameterTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparametertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparametertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEWParameter.Type and LabVIEWParameterElement.Type properties return one of the following constants to indicate the data type of the parameter. Before you get or set the parameter data type, also get or set the category with the LabVIEWParameter.Category or LabVIEWParameterElement.Category p

### LabVIEWParameterTypes

The
 [LabVIEWParameter.Type](labviewparameter-type.html)
 and
 [LabVIEWParameterElement.Type](labviewparameterelement-type.html)
 properties return one of the following constants to indicate the data type of the parameter. Before you get or set the parameter data type, also get or set the category with the
 [LabVIEWParameter.Category](labviewparameter-category.html)
 or
 [LabVIEWParameterElement.Category](labviewparameterelement-category.html)
 property.

- LVParamType_ActiveXRef 
 –(Value: 0x40) Indicates that the parameter is an ActiveX reference.
- LVParamType_AnalogWaveform 
 –(Value: 23) Indicates that the parameter is an Analog Waveform type. For parameters of this LabVIEW data type, use the TestStand LabVIEWAnalogWaveform data type as a parameter value.
 Note 
 If the Y element representation of an analog waveform is set to Quad or Unsigned Quad, do not use the LabVIEWAnalogWaveform data type because the representation of the Y element for the type is set to double-precision, 64-bit floating-point, which cannot store a Quad or unsigned Quad value without the risk of losing precision. In these cases, create a new custom data type and set the representation of the Y element to signed 64-bit integer or unsigned 64-bit integer, respectively.
- LVParamType_Complex128 
 –(Value: 10) Indicates that the parameter is a 128-bit complex number. TestStand treats parameters of this type as two 64-bit floating point numbers.
- LVParamType_Complex64 
 –(Value: 9) Indicates that the parameter is a 64-bit complex number.
- LVParamType_ComplexExt 
 –(Value: 11) Indicates that the parameter is an extended-precision complex number. TestStand treats parameters of this type as two 64-bit floating point numbers.
- LVParamType_DigitalData 
 –(Value: 22) Indicates that the parameter is a Digital Data type. For parameters of this LabVIEW data type, use the TestStand LabVIEWDigitalData data type as a parameter value.
- LVParamType_DigitalWaveform 
 –(Value: 24) Indicates that the parameter is a Digital Waveform type. For parameters of this LabVIEW data type, use the TestStand LabVIEWDigitalWaveform data type as a parameter value.
- LVParamType_DotNetRef 
 –(Value: 0x41) Indicates that the parameter is a .NET reference.
- LVParamType_DynamicData 
 –(Value: 25) Indicates that the parameter is a Dynamic Data type.
- LVParamType_EnumUInt16 
 –(Value: 15) Indicates that the parameter is an enumeration represented by a 16-bit unsigned integer.
- LVParamType_EnumUInt32 
 –(Value: 16) Indicates that the parameter is an enumeration represented by a 32-bit unsigned integer.
- LVParamType_EnumUInt8 
 –(Value: 14) Indicates that the parameter is an enumeration represented by an 8-bit unsigned integer.
- LVParamType_ErrorOut 
 –(Value: 0x22) Indicates that the parameter is an
 error out 
 type. For parameters of this LabVIEW data type, use the TestStand Error data type as a parameter value.
- LVParamType_Ext 
 –(Value: 8) Indicates that the parameter is an extended-precision number. TestStand treats parameters of this type as 64-bit floating point numbers, so some data could be lost.
- LVParamType_Int16 
 –(Value: 2) Indicates that the parameter is a 16-bit integer.
- LVParamType_Int32 
 –(Value: 4) Indicates that the parameter is a 32-bit integer.
- LVParamType_Int64 
 –(Value: 12) Indicates that the parameter is a 64-bit integer.
- LVParamType_Int8 
 –(Value: 0) Indicates that the parameter is an 8-bit integer.
- LVParamType_IO 
 –(Value: 21) Indicates that the parameter is an I/O control reference cluster.
- LVParamType_LVClass 
 –(Value: 0x44) Indicates that the parameter is a LabVIEW class.
- LVParamType_LVObjectRef 
 –(Value: 0x42) Indicates that the parameter is a LabVIEW VI or application reference. TestStand treats such references as unsigned, numeric long values.
- LVParamType_OtherRef 
 –(Value: 0x43) Indicates that the parameter is a LabVIEW reference but not an I/O control reference. TestStand treats such references as unsigned, numeric long values.
- LVParamType_PathString 
 –(Value: 0x62) Indicates that the parameter is a path. TestStand treats paths as C-strings.
- LVParamType_Real32 
 –(Value: 6) Indicates that the parameter is a 32-bit real number.
- LVParamType_Real64 
 –(Value: 7) Indicates that the parameter is a 64-bit real number.
- LVParamType_StandardCluster 
 –(Value: 20) Indicates that the parameter is a standard cluster.
- LVParamType_String 
 –(Value: 0x60) Indicates that the parameter is a string that contains binary data. Use the
 LabVIEWParameter.PassAsBinaryString 
 property to instruct TestStand to preserve
 NUL 
 bytes by unescaping a TestStand string before assigning a value to a LabVIEW control, and by escaping a binary string from a LabVIEW indicator before storing in TestStand.
- LVParamType_TestData 
 –(Value: 0x21) Indicates that the parameter is a legacy TestData data type.
- LVParamType_TimestampString 
 –(Value: 0x63) Indicates that the parameter is a timestamp, which TestStand treats as a C-string.
- LVParamType_UInt16 
 –(Value: 3) Indicates that the parameter is a 16-bit unsigned integer.
- LVParamType_UInt32 
 –(Value: 5) Indicates that the parameter is a 32-bit unsigned integer.
- LVParamType_UInt64 
 –(Value: 13) Indicates that the parameter is a 64-bit unsigned integer.
- LVParamType_UInt8 
 –(Value: 1) Indicates that the parameter is an 8-bit unsigned integer.
- LVParamType_Unspecified 
 –(Value: 200) Indicates that the parameter has an unspecified data type because the category does not have any associated data types.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWParameter.Category](labviewparameter-category.html)

[LabVIEWParameter.PassAsBinaryString](labviewparameter-passasbinarystring.html)

[LabVIEWParameter.Type](labviewparameter-type.html)

[LabVIEWParameterCategories](labviewparametercategories.html)

[LabVIEWParameterElement.Category](labviewparameterelement-category.html)

[LabVIEWParameterElement.Type](labviewparameterelement-type.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewparameterwirerequirements.html language=enus -->
## TOPIC 01613: LabVIEWParameterWireRequirements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewparameterwirerequirements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewparameterwirerequirements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The LabVIEWParameter.WireRequirement property returns one of the following constants to indicate if the module can pass a default value for the parameter. LVParamWireReq_Optional –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value. LVParamWire

### LabVIEWParameterWireRequirements

The
 [LabVIEWParameter.WireRequirement](labviewparameter-wirerequirement.html)
 property returns one of the following constants to indicate if the module can pass a default value for the parameter.

- LVParamWireReq_Optional 
 –(Value: 2) Indicates that the module can use the default value for the parameter instead of passing a value.
- LVParamWireReq_Recommended 
 –(Value: 1) Indicates that the module can use the default value for the parameter. However, passing a value is recommended.
- LVParamWireReq_Required 
 –(Value: 0) Indicates that the module must pass a value for the parameter.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWParameter.WireRequirement](labviewparameter-wirerequirement.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewprojectpathtypes.html language=enus -->
## TOPIC 01614: LabVIEWProjectPathTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewprojectpathtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewprojectpathtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWModule.DisplaySelectVIFromProjectDialog , LabVIEWModule.GetProjectUrlPathsForVIs , and LabVIEWModule.FindVIUrlUsingVIPath methods to specify the LabVIEW project path property to use. LVProjectPathType_Local –(Value: 0) Indicates to use the LabVIEWModule.ProjectPat

### LabVIEWProjectPathTypes

Use these constants with the
 [LabVIEWModule.DisplaySelectVIFromProjectDialog](labviewmodule-displayselectvifromprojectdialo2.html)
 ,
 [LabVIEWModule.GetProjectUrlPathsForVIs](labviewmodule-getprojecturlpathsforvis.html)
 , and
 [LabVIEWModule.FindVIUrlUsingVIPath](labviewmodule-findviurlusingvipath.html)
 methods to specify the LabVIEW project path property to use.

- LVProjectPathType_Local 
 –(Value: 0) Indicates to use the
 LabVIEWModule.ProjectPath 
 property.
- LVProjectPathType_Remote 
 –(Value: 1) Indicates to use the
 LabVIEWModule.RemoteProjectPath 
 property.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEWModule.DisplaySelectVIFromProjectDialog](labviewmodule-displayselectvifromprojectdialo2.html)

[LabVIEWModule.GetProjectUrlPathsForVIs](labviewmodule-getprojecturlpathsforvis.html)

[LabVIEWModule.FindVIUrlUsingVIPath](labviewmodule-findviurlusingvipath.html)

[LabVIEWModule.ProjectPath](labviewmodule-projectpath.html)

[LabVIEWModule.RemoteProjectPath](labviewmodule-remoteprojectpath.html)

[Organizing Test Program Files with LabVIEW Projects](/csh?context=ts_tslabview_project)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewpropertyoptions.html language=enus -->
## TOPIC 01615: LabVIEWPropertyOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewpropertyoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewpropertyoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWAdapter.GetPropertiesForNodeClass and LabVIEWAdapter.GetPropertiesForLabVIEWClass methods to obtain options for the properties. LVPropertyOption_Default –(Value: 0x4) Indicates that the property can use the default value. LVPropertyOption_Read –(Value: 0x1) Indica

### LabVIEWPropertyOptions

Use these constants with the
 [LabVIEWAdapter.GetPropertiesForNodeClass](labviewadapter-getpropertiesfornodeclass.html)
 and
 [LabVIEWAdapter.GetPropertiesForLabVIEWClass](labviewadapter-getpropertiesforlabviewclass.html)
 methods to obtain options for the properties.

- LVPropertyOption_Default 
 –(Value: 0x4) Indicates that the property can use the default value.
- LVPropertyOption_Read 
 –(Value: 0x1) Indicates that you can read the property.
- LVPropertyOption_Write 
 –(Value: 0x2) Indicates that you can write to the property.

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewservertypes.html language=enus -->
## TOPIC 01616: LabVIEWServerTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewservertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewservertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the serverType parameter of the LabVIEWAdapter.GetServerInfo method to determine the type of server the LabVIEW Adapter is using. LabVIEWServer_ExecServer –(Value: 0x0) Specifies to use a LabVIEW executable server. LabVIEW executable servers include a LabVIEW development env

### LabVIEWServerTypes

Use these constants with the
 serverType
 parameter of the
 [LabVIEWAdapter.GetServerInfo](labviewadapter-getserverinfo.html)
 method to determine the type of server the LabVIEW Adapter is using.

- LabVIEWServer_ExecServer 
 –(Value: 0x0) Specifies to use a LabVIEW executable server. LabVIEW executable servers include a LabVIEW development environment or a LabVIEW application that registers itself as a LabVIEW ActiveX Automation server.
- LabVIEWServer_ExecServerDeferred 
 –(Value: 0x2) Specifies to use the LabVIEW executable server. If the server selected is the LabVIEW Development System, LabVIEW will only launch on first use, rather than when the
 LabVIEWAdapter.SetServerInfo 
 method is called.
- LabVIEWServer_RTEServer 
 –(Value: 0x1) Specifies to use a LabVIEW run-time server.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEW Adapter Configuration dialog box](../tsref/labview-adapter-configuration-dialog-box.html)

[LabVIEWAdapter.GetServerInfo](labviewadapter-getserverinfo.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewvitypes.html language=enus -->
## TOPIC 01617: LabVIEWVITypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewvitypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewvitypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWModule.VIType property to specify the type of VI the LabVIEW module calls. LVVIType_Express –(Value: 1) Indicates that the VI module calls an Express VI. LVVIType_Standard –(Value: 0) Indicates that the VI module calls a standard VI. See Also Effectively Using Lab

### LabVIEWVITypes

Use these constants with the
 [LabVIEWModule.VIType](labviewmodule-vitype.html)
 property to specify the type of VI the LabVIEW module calls.

- LVVIType_Express 
 –(Value: 1) Indicates that the VI module calls an Express VI.
- LVVIType_Standard 
 –(Value: 0) Indicates that the VI module calls a standard VI.

#### See Also

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

[LabVIEW Adapter](/csh?context=ts_tsref_labview)

[LabVIEWModule.VIType](labviewmodule-vitype.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/licensetypes.html language=enus -->
## TOPIC 01618: LicenseTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/licensetypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/licensetypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Engine.LicenseType property to determine the type of license the TestStand Engine is using. LicenseType_BaseDeploymentEngine –(Value: 3) Indicates that TestStand is using a TestStand Base Deployment Engine License. LicenseType_CustomEditorDeployment –(Value: 9) Indicates

### LicenseTypes

Use these constants with the
 [Engine.LicenseType](engine-licensetype.html)
 property to determine the type of
 
 [license](/csh?context=ts_9050)
 the TestStand Engine is using.

- LicenseType_BaseDeploymentEngine 
 –(Value: 3) Indicates that TestStand is using a TestStand Base Deployment Engine License.
- LicenseType_CustomEditorDeployment 
 –(Value: 9) Indicates that TestStand is using a TestStand Custom Sequence Editor License.
- LicenseType_DebugDeploymentEnv 
 –(Value: 2) Indicates that TestStand is using a TestStand Debug Deployment Environment License.
- LicenseType_DevelopmentSystem 
 –(Value: 1) Indicates that TestStand is using a TestStand Development System License.
- LicenseType_Evaluation 
 –(Value: 5) Indicates that TestStand is using an Evaluation license.
- LicenseType_NoLicense 
 –(Value: 6) Indicates that TestStand is using no license.
- LicenseType_OEM 
 –(Value: 4) Indicates that TestStand is using an OEM license.
- LicenseType_Other 
 –(Value: 8) Indicates that TestStand cannot determine the type of license.
- LicenseType_Temporary 
 –(Value: 7) Indicates that TestStand is using a temporary license. TestStand acquires a temporary license when NI License Manager cannot access the Volume License server.

#### See Also

[Engine.LicenseType](engine-licensetype.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/loadmoduleoptions.html language=enus -->
## TOPIC 01619: LoadModuleOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/loadmoduleoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/loadmoduleoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the loadOptions parameter of the SequenceFile.LoadModules , Sequence.LoadModules , and Step.LoadModule methods. Use the bitwise-OR operator to specify more than one option. LoadModule_DoNotPromptToFindFile –(Value: 0x20) If this option is set an

### LoadModuleOptions

These constants represent the options you can use with the
 loadOptions
 parameter of the
 [SequenceFile.LoadModules](sequencefile-loadmodules.html)
 ,
 [Sequence.LoadModules](sequence-loadmodules.html)
 , and
 [Step.LoadModule](step-loadmodule.html)
 methods. Use the bitwise-OR operator to specify more than one option.

- LoadModule_DoNotPromptToFindFile 
 –(Value: 0x20) If this option is set and the method cannot find the module file, the method does not launch a file dialog box to find the module file.
- LoadModule_DoNotRunLoadCallbacks 
 –(Value: 0x40) If this option is set and the module is a
 SequenceCallModule 
 , the method loads the sequence file without running the SequenceFileLoad callback sequence. Only the SequenceCallModule uses this option.
- LoadModule_EvaluateExpressions 
 –(Value: 0x4) Loads modules of Sequence Call steps that specify the module by expression. Pass a sequence context to the method when using this option.
- LoadModule_IgnoreErrors 
 –(Value: 0x1) Ignores errors that occur when loading modules. If this option is not set, each error is reported in a dialog box.
- LoadModule_IgnoreSkippedSteps 
 –(Value: 0x8) Does not load the modules for steps that have a run mode of anything but
 RunMode_Normal 
 .
- LoadModule_LoadModulesInSubSequences 
 –(Value: 0x2) Loads modules in subsequences when their corresponding Sequence Call step is loaded.
- LoadModule_NoOptions 
 –(Value: 0x0) No options.
- LoadModule_ThrowExceptionOnError 
 –(Value: 0x10) If this option is set and
 LoadModule_IgnoreErrors 
 is not set, the method throws an exception if an error occurs loading the module.

#### See Also

[GetSeqFileOptions](getseqfileoptions.html)

[RunModes](runmodes.html)

[Sequence.LoadModules](sequence-loadmodules.html)

[SequenceCallModule](sequencecallmodule.html)

[SequenceFile.LoadModules](sequencefile-loadmodules.html)

[Step.LoadModule](step-loadmodule.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/loadprototypeoptions.html language=enus -->
## TOPIC 01620: LoadPrototypeOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/loadprototypeoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/loadprototypeoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the Module.LoadPrototype , SequenceCallModule.LoadPrototypeFromSequence and DotNetCall.LoadPrototypeFromSignature methods. LoadPrototypeOption_MapExistingParameters –(value: 0x1) If this flag is set, the Module.LoadProto

### LoadPrototypeOptions

These constants represent the options you can use with the
 options
 parameter of the
 [Module.LoadPrototype](module-loadprototype.html)
 ,
 [SequenceCallModule.LoadPrototypeFromSequence](sequencecallmodule-loadprototypefromsequence.html)
 and
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 methods.

- LoadPrototypeOption_MapExistingParameters 
 –(value: 0x1) If this flag is set, the
 Module.LoadPrototype 
 method attempts to keep the existing argument value expressions by mapping them to the parameters in the new prototype. Any arguments that cannot be mapped are added to the
 Module.UnmappedArgumentValues 
 collection.
- LoadPrototypeOption_NoOptions 
 –(Value: 0x0) No Options.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[Module.LoadPrototype](module-loadprototype.html)

[Module.UnmappedArgumentValues](module-unmappedargumentvalues.html)

[SequenceCallModule.LoadPrototypeFromSequence](sequencecallmodule-loadprototypefromsequence.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/loadtypepalettefilesoptions.html language=enus -->
## TOPIC 01621: LoadTypePaletteFilesOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/loadtypepalettefilesoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/loadtypepalettefilesoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you use with the options parameter of the Engine.LoadTypePaletteFilesEx method. LoadTypePaletteOptions_DisplayErrors –(Value: 0x1) Specifies to not return an error and to launch a warning dialog box that contains a description of all errors that occurred while l

### LoadTypePaletteFilesOptions

These constants represent the options you use with the
 options
 parameter of the
 [Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)
 method.

- LoadTypePaletteOptions_DisplayErrors 
 –(Value: 0x1) Specifies to not return an error and to launch a warning dialog box that contains a description of all errors that occurred while loading the type palette files.
- LoadTypePaletteOptions_NoOptions 
 –(Value: 0x0) Specifies the default behavior, which is to return an error to the caller of the method.

#### See Also

[Engine.LoadTypePaletteFilesEx](engine-loadtypepalettefilesex.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-attributespath.html language=enus -->
## TOPIC 01622: Location.AttributesPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-attributespath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-attributespath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.AttributesPath Data Type String Purpose Specifies the portion of the Location.PropertyPath property value that starts with the top-level attribute or top-level type attribute. Remarks If the Location.PropertyPath property does not specify an attribute location, this property is an em

### Location.AttributesPath

#### Syntax

[Location](location.html).AttributesPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the portion of the
 [Location.PropertyPath](location-propertypath.html)
 property value that starts with the top-level attribute or top-level type attribute.

#### Remarks

If the
 Location.PropertyPath
 property does not specify an attribute location, this property is an empty string. If the
 Location.PropertyPath
 property specifies an attribute location, this property always starts with
 Attributes
 or
 TypeAttributes
 .

#### See Also

[Location.BaseAttributesPath](location-baseattributespath.html)

[Location.PropertyPath](location-propertypath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-baseattributespath.html language=enus -->
## TOPIC 01623: Location.BaseAttributesPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-baseattributespath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-baseattributespath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.BaseAttributesPath Data Type String Purpose Specifies the portion of Location.PropertyPath before any top-level attribute or top-level type attribute. Remarks If the Location.PropertyPath property does not specify an attribute location, this property has the same value as the Locatio

### Location.BaseAttributesPath

#### Syntax

[Location](location.html).BaseAttributesPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the portion of Location.PropertyPath before any top-level attribute or top-level type attribute.

#### Remarks

If the
 [Location.PropertyPath](location-propertypath.html)
 property does not specify an attribute location, this property has the same value as the
 Location.PropertyPath
 property.

#### See Also

[Location.AttributesPath](location-attributespath.html)

[Location.PropertyPath](location-propertypath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-contextid.html language=enus -->
## TOPIC 01624: Location.ContextId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-contextid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-contextid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.ContextId Data Type Long Purpose For an execution location, this property specifies the ID of the sequence context to which the Location.PropertyPath property is relative. For a file location, this property specifies the ID of the sequence context which has properties that correspond

### Location.ContextId

#### Syntax

[Location](location.html).ContextId

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

For an execution location, this property specifies the ID of the sequence context to which the
 [Location.PropertyPath](location-propertypath.html)
 property is relative. For a file location, this property specifies the ID of the sequence context which has properties that correspond to properties of this location.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[SequenceContext.Id](sequencecontext-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-element.html language=enus -->
## TOPIC 01625: Location.Element

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-element.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-element.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.Element Data Type PropertyObjectElements Use the following constants with this data type: PropertyObjectElement_Attributes –(Value: 7) Specifies the attributes of the PropertyObject , which you access through the PropertyObject.Attributes property. PropertyObjectElement_Comment –(Val

### Location.Element

#### Syntax

[Location](location.html).Element

#### Data Type

[PropertyObjectElements](propertyobjectelements.html)

Use the following constants with this data type:

- PropertyObjectElement_Attributes 
 –(Value: 7) Specifies the attributes of the
 PropertyObject 
 , which you access through the
 PropertyObject.Attributes 
 property.
- PropertyObjectElement_Comment 
 –(Value: 3) Specifies the comment of a PropertyObject, which you access through the
 PropertyObject.Comment 
 property.
- PropertyObjectElement_Flags 
 –(Value: 4) Specifies the flags of a PropertyObject, which you access through the
 PropertyObject.GetFlags 
 and
 PropertyObject.SetFlags 
 methods.
- PropertyObjectElement_Name 
 –(Value: 2) Specifies the name of a PropertyObject, which you access through the
 PropertyObject.Name 
 property.
- PropertyObjectElement_None 
 –(Value: 0) Does not specify any part of a PropertyObject.
- PropertyObjectElement_NumericFormat 
 –(Value: 5) Specifies the numeric format of a PropertyObject, which you access through the
 PropertyObject.NumericFormat 
 property.
- PropertyObjectElement_Representation 
 –(Value: 6) Specifies the representation of PropertyObject, which you access with the
 PropertyObjectType.Representation 
 property.
- PropertyObjectElement_Value 
 –(Value: 1) Specifies the value of a PropertyObject, which you access with GetVal and SetVal methods.

#### Purpose

Specifies a part of the property object which the
 [Location.PropertyPath](location-propertypath.html)
 property specifies.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[PropertyObject.Comment](propertyobject-comment.html)

[PropertyObject.GetFlags](propertyobject-getflags.html)

[PropertyObject.Name](propertyobject-name.html)

[PropertyObject.NumericFormat](propertyobject-numericformat.html)

[PropertyObject.SetFlags](propertyobject-setflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-executiondisplayname.html language=enus -->
## TOPIC 01626: Location.ExecutionDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-executiondisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-executiondisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.ExecutionDisplayName Data Type String Purpose For an execution location, specifies the display name of the execution. See Also Execution.DisplayName Location.ExecutionId SequenceContext.Execution

### Location.ExecutionDisplayName

#### Syntax

[Location](location.html).ExecutionDisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

For an execution location, specifies the display name of the execution.

#### See Also

[Execution.DisplayName](execution-displayname.html)

[Location.ExecutionId](location-executionid.html)

[SequenceContext.Execution](sequencecontext-execution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-executionid.html language=enus -->
## TOPIC 01627: Location.ExecutionId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-executionid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-executionid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.ExecutionId Data Type Long Purpose For an execution location, specifies the ID of the execution. See Also Execution.Id Location.ExecutionDisplayName SequenceContext.Execution

### Location.ExecutionId

#### Syntax

[Location](location.html).ExecutionId

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

For an execution location, specifies the ID of the execution.

#### See Also

[Execution.Id](execution-id.html)

[Location.ExecutionDisplayName](location-executiondisplayname.html)

[SequenceContext.Execution](sequencecontext-execution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-filedisplayname.html language=enus -->
## TOPIC 01628: Location.FileDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-filedisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-filedisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.FileDisplayName Data Type String Purpose For a file location, specifies the display name of the file of which the Location.PropertyPath property is a subproperty. For an execution location, specifies the display name of the sequence file of the executing sequence. For a type location

### Location.FileDisplayName

#### Syntax

[Location](location.html).FileDisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

For a file location, specifies the display name of the file of which the
 [Location.PropertyPath](location-propertypath.html)
 property is a subproperty. For an execution location, specifies the display name of the sequence file of the executing sequence. For a type location, specifies the display name of the file in which you saved the type.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[PropertyObjectFile.DisplayName](propertyobjectfile-displayname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-fileid.html language=enus -->
## TOPIC 01629: Location.FileId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-fileid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-fileid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.FileId Data Type Long Purpose For a file location, this property specifies the ID of the file of which the Location.PropertyPath property is a subproperty. For an execution location, this property specifies the ID of the sequence file of the executing sequence. For a type location, t

### Location.FileId

#### Syntax

[Location](location.html).FileId

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

For a file location, this property specifies the ID of the file of which the
 [Location.PropertyPath](location-propertypath.html)
 property is a subproperty. For an execution location, this property specifies the ID of the sequence file of the executing sequence. For a type location, this property specifies the ID of the file in which the type is saved.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[PropertyObjectFile.Id](propertyobjectfile-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-filepath.html language=enus -->
## TOPIC 01630: Location.FilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-filepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-filepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.FilePath Data Type String Purpose For a file location, this property specifies the absolute path of the file of which the Location.PropertyPath property is a subproperty. For an execution location, this property specifies the absolute path of the sequence file of the executing sequen

### Location.FilePath

#### Syntax

[Location](location.html).FilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

For a file location, this property specifies the absolute path of the file of which the
 [Location.PropertyPath](location-propertypath.html)
 property is a subproperty. For an execution location, this property specifies the absolute path of the sequence file of the executing sequence. For a type location, this property specifies the absolute path of the file in which the type is saved.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[PropertyObjectFile.Path](propertyobjectfile-path.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-ioconfigurationname.html language=enus -->
## TOPIC 01631: Location.IOConfigurationName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-ioconfigurationname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-ioconfigurationname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.IOConfigurationName Data Type String Purpose Specifies the name of the IOConfiguration that is activated. See Also Location.ThreadDisplayName Location.StepName

### Location.IOConfigurationName

#### Syntax

[Location](location.html).IOConfigurationName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the IOConfiguration that is activated.

#### See Also

[Location.ThreadDisplayName](location-threaddisplayname.html)

[Location.StepName](location-stepname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-kind.html language=enus -->
## TOPIC 01632: Location.Kind

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-kind.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-kind.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.Kind Data Type LocationKinds Use the following constants with this data type: LocationKind_Execution –(Value: 2) Specifies a location in a SequenceContext . LocationKind_File –(Value: 1) Specifies a location in a file. LocationKind_Type –(Value: 3) Specifies a location in a type. Pur

### Location.Kind

#### Syntax

[Location](location.html).Kind

#### Data Type

[LocationKinds](locationkinds.html)

Use the following constants with this data type:

- LocationKind_Execution 
 –(Value: 2) Specifies a location in a
 SequenceContext 
 .
- LocationKind_File 
 –(Value: 1) Specifies a location in a file.
- LocationKind_Type 
 –(Value: 3) Specifies a location in a type.

#### Purpose

Specifies whether the location is a file, execution, or type location.

#### See Also

[SequenceContext](sequencecontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-propertypath.html language=enus -->
## TOPIC 01633: Location.PropertyPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-propertypath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-propertypath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.PropertyPath Data Type String Purpose Specifies the lookup string for this location. Remarks For a file location, this property is relative to the file the Location.FileId and Location.FilePath properties specify. For an execution location, this property is relative to the sequence c

### Location.PropertyPath

#### Syntax

[Location](location.html).PropertyPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the lookup string for this location.

#### Remarks

For a file location, this property is relative to the file the
 [Location.FileId](location-fileid.html)
 and
 [Location.FilePath](location-filepath.html)
 properties specify. For an execution location, this property is relative to the sequence context the
 [Location.ContextId](location-contextid.html)
 property specifies. For a type location, this property is relative to the type the
 [Location.TypeName](location-typename.html)
 property specifies. For a workspace file location, this property is relative to the WorkspaceObject the
 [WorkspaceFile.RootWorkspaceObject](workspacefile-rootworkspaceobject.html)
 property returns.

#### See Also

[Location.ContextId](location-contextid.html)

[Location.FileId](location-fileid.html)

[Location.FilePath](location-filepath.html)

[Location.Kind](location-kind.html)

[Location.TypeName](location-typename.html)

[WorkspaceFile.RootWorkspaceObject](workspacefile-rootworkspaceobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-propertypathwithnames.html language=enus -->
## TOPIC 01634: Location.PropertyPathWithNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-propertypathwithnames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-propertypathwithnames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.PropertyPathWithNames Data Type String Purpose Specifies the lookup string for this location. The lookup string includes names instead of a numeric index for elements of object arrays if the name is not empty. Remarks The name of an object element in an array is not guaranteed to be

### Location.PropertyPathWithNames

#### Syntax

[Location](location.html).PropertyPathWithNames

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the lookup string for this location. The lookup string includes names instead of a numeric index for elements of object arrays if the name is not empty.

#### Remarks

The name of an object element in an array is not guaranteed to be unique within the array. Do not use this property with methods that have a lookup string parameter, such as the
 [PropertyObject.GetPropertyObject](propertyobject-getpropertyobject.html)
 method and the
 [PropertyObject.Exists](propertyobject-exists.html)
 method. Use the
 [Location.PropertyPath](location-propertypath.html)
 property if you want an unambiguous lookup string.

For a file location, this property is relative to the file the
 [Location.FileId](location-fileid.html)
 and the
 [Location.FilePath](location-filepath.html)
 properties specify. For an execution location, this property is relative to the sequence context the
 [Location.ContextId](location-contextid.html)
 property specifies. For a type location, this property is relative to the type the
 [Location.TypeName](location-typename.html)
 property specifies. For a workspace file location, this property is relative to the WorkspaceObject the
 [WorkspaceFile.RootWorkspaceObject](workspacefile-rootworkspaceobject.html)
 property returns.

#### See Also

[Location.ContextId](location-contextid.html)

[Location.FileId](location-fileid.html)

[Location.FilePath](location-filepath.html)

[Location.Kind](location-kind.html)

[Location.PropertyPath](location-propertypath.html)

[Location.TypeName](location-typename.html)

[PropertyObject.Exists](propertyobject-exists.html)

[PropertyObject.GetPropertyObject](propertyobject-getpropertyobject.html)

[WorkspaceFile.RootWorkspaceObject](workspacefile-rootworkspaceobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-sellength.html language=enus -->
## TOPIC 01635: Location.SelLength

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-sellength.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-sellength.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.SelLength Data Type Long Purpose Specifies the number of selected characters of the text that the Location.Element property refers to. Remarks A user interface only uses this property if Element specifies a value, name, comment, or numeric format. See Also Location.Element Location.S

### Location.SelLength

#### Syntax

[Location](location.html).SelLength

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of selected characters of the text that the
 [Location.Element](location-element.html)
 property refers to.

#### Remarks

A user interface only uses this property if Element specifies a value, name, comment, or numeric format.

#### See Also

[Location.Element](location-element.html)

[Location.SelStart](location-selstart.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-selstart.html language=enus -->
## TOPIC 01636: Location.SelStart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-selstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-selstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.SelStart Data Type Long Purpose Specifies the zero-based starting index of the selection of the text that the Location.Element property refers to. Remarks A user interface only uses this property if Element specifies a value, name, comment, or numeric format. See Also Location.Elemen

### Location.SelStart

#### Syntax

[Location](location.html).SelStart

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the zero-based starting index of the selection of the text that the
 [Location.Element](location-element.html)
 property refers to.

#### Remarks

A user interface only uses this property if Element specifies a value, name, comment, or numeric format.

#### See Also

[Location.Element](location-element.html)

[Location.SelLength](location-sellength.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-sequencename.html language=enus -->
## TOPIC 01637: Location.SequenceName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-sequencename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-sequencename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.SequenceName Data Type String Purpose For a file location, this property specifies the name of the sequence of which the Location.PropertyPath property is a subproperty. This property is empty if the Location.PropertyPath property is not a subproperty of a sequence. For an execution

### Location.SequenceName

#### Syntax

[Location](location.html).SequenceName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

For a file location, this property specifies the name of the sequence of which the
 [Location.PropertyPath](location-propertypath.html)
 property is a subproperty. This property is empty if the
 Location.PropertyPath
 property is not a subproperty of a sequence. For an execution location, this property specifies the name of the executing sequence.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[Sequence.Name](sequence-name.html)

[SequenceContext.Sequence](sequencecontext-sequence.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-stepgroup.html language=enus -->
## TOPIC 01638: Location.StepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-stepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.StepGroup Data Type StepGroups Use the following constants with this data type: StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step group. Purpose For a file loc

### Location.StepGroup

#### Syntax

[Location](location.html).StepGroup

#### Data Type

[StepGroups](stepgroups.html)

Use the following constants with this data type:

- StepGroup_Cleanup 
 –(Value: 2) Specifies the Cleanup step group.
- StepGroup_Main 
 –(Value: 1) Specifies the Main step group.
- StepGroup_Setup 
 –(Value: 0) Specifies the Setup step group.

#### Purpose

For a file location, this property specifies the step group of which the
 [Location.PropertyPath](location-propertypath.html)
 property is a subproperty. The value is
 -1
 if the
 Location.PropertyPath
 property is not a subproperty of a step group. For an execution location, this property specifies the step group of the executing step.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[SequenceContext.StepGroup](sequencecontext-stepgroup.html)

[Step.StepGroup](step-stepgroup.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-stepid.html language=enus -->
## TOPIC 01639: Location.StepId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-stepid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-stepid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.StepId Data Type String Purpose For a file location, this property specifies the unique step ID of the step of which the Location.PropertyPath property is a subproperty. This property is empty if the Location.PropertyPath property is not a subproperty of a step. For an execution loca

### Location.StepId

#### Syntax

[Location](location.html).StepId

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

For a file location, this property specifies the unique step ID of the step of which the
 [Location.PropertyPath](location-propertypath.html)
 property is a subproperty. This property is empty if the
 Location.PropertyPath
 property is not a subproperty of a step. For an execution location, this property specifies the unique step ID of the executing step.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[SequenceContext.Step](sequencecontext-step.html)

[Step.UniqueStepId](step-uniquestepid.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-stepindex.html language=enus -->
## TOPIC 01640: Location.StepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-stepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-stepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.StepIndex Data Type Long Purpose For a file location, this property specifies the index of the step of which the Location.PropertyPath property is a subproperty. This property is -1 if the Location.PropertyPath property is not a subproperty of a step. For an execution location, this

### Location.StepIndex

#### Syntax

[Location](location.html).StepIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

For a file location, this property specifies the index of the step of which the
 [Location.PropertyPath](location-propertypath.html)
 property is a subproperty. This property is -1 if the
 Location.PropertyPath
 property is not a subproperty of a step. For an execution location, this property specifies the step index of the executing step.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[SequenceContext.StepIndex](sequencecontext-stepindex.html)

[Step.StepIndex](step-stepindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-stepname.html language=enus -->
## TOPIC 01641: Location.StepName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-stepname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-stepname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.StepName Data Type String Purpose For a file location, this property specifies the name of the step of which the Location.PropertyPath property is a subproperty. This property is empty if the Location.PropertyPath property is not a subproperty of a step. For an execution location, th

### Location.StepName

#### Syntax

[Location](location.html).StepName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

For a file location, this property specifies the name of the step of which the
 [Location.PropertyPath](location-propertypath.html)
 property is a subproperty. This property is empty if the
 Location.PropertyPath
 property is not a subproperty of a step. For an execution location, this property specifies the step name of the executing step.

#### See Also

[Location.PropertyPath](location-propertypath.html)

[SequenceContext.Step](sequencecontext-step.html)

[Step.Name](step-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-threaddisplayname.html language=enus -->
## TOPIC 01642: Location.ThreadDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-threaddisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-threaddisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.ThreadDisplayName Data Type String Purpose For an execution location, specifies the display name of the thread. See Also Location.ThreadId SequenceContext.Thread Thread.DisplayName

### Location.ThreadDisplayName

#### Syntax

[Location](location.html).ThreadDisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

For an execution location, specifies the display name of the thread.

#### See Also

[Location.ThreadId](location-threadid.html)

[SequenceContext.Thread](sequencecontext-thread.html)

[Thread.DisplayName](thread-displayname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-threadid.html language=enus -->
## TOPIC 01643: Location.ThreadId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-threadid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-threadid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.ThreadId Data Type Long Purpose For an execution location, specifies the ID of the executing thread. See Also SequenceContext.Thread Thread.Id

### Location.ThreadId

#### Syntax

[Location](location.html).ThreadId

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

For an execution location, specifies the ID of the executing thread.

#### See Also

[SequenceContext.Thread](sequencecontext-thread.html)

[Thread.Id](thread-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-typecategory.html language=enus -->
## TOPIC 01644: Location.TypeCategory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-typecategory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-typecategory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.TypeCategory Data Type TypeCategories Use the following constants with this data type: TypeCategory_BuiltinDataTypes –(Value: 3) Specifies a built-in data type. TypeCategory_CustomDataTypes –(Value: 2) Specifies a custom data type. TypeCategory_None –(Value: 0) Specifies no data type

### Location.TypeCategory

#### Syntax

[Location](location.html).TypeCategory

#### Data Type

[TypeCategories](typecategories.html)

Use the following constants with this data type:

- TypeCategory_BuiltinDataTypes 
 –(Value: 3) Specifies a built-in data type.
- TypeCategory_CustomDataTypes 
 –(Value: 2) Specifies a custom data type.
- TypeCategory_None 
 –(Value: 0) Specifies no data type.
- TypeCategory_StepTypes 
 –(Value: 1) Specifies a step type.

#### Purpose

For a type location, specifies the type category of the root type definition the
 [Location.TypeName](location-typename.html)
 property specifies.

#### See Also

[Location.TypeName](location-typename.html)

[PropertyObject.TypeCategory](propertyobject-typecategory.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location-typename.html language=enus -->
## TOPIC 01645: Location.TypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location-typename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location-typename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Location.TypeName Data Type String Purpose For a type location, this property specifies the name of a root type definition. Location.PropertyPath specifies a subproperty of the root type definition this property specifies. See Also Location.PropertyPath

### Location.TypeName

#### Syntax

[Location](location.html).TypeName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

For a type location, this property specifies the name of a root type definition.
 [Location.PropertyPath](location-propertypath.html)
 specifies a subproperty of the root type definition this property specifies.

#### See Also

[Location.PropertyPath](location-propertypath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/location.html language=enus -->
## TOPIC 01646: Location

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/location.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/location.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The properties of a Location object contain enough information for a user interface to find a specific piece of data the user interface displays. Properties AttributesPath BaseAttributesPath ContextId Element ExecutionDisplayName ExecutionId FileDisplayName FileId FilePath IOConfigurationName Kind P

### Location

The properties of a Location object contain enough information for a user interface to find a specific piece of data the user interface displays.

#### Properties

| AttributesPath |
| --- |
| BaseAttributesPath |
| ContextId |
| Element |
| ExecutionDisplayName |
| ExecutionId |
| FileDisplayName |
| FileId |
| FilePath |
| IOConfigurationName |
| Kind |
| PropertyPath |
| PropertyPathWithNames |
| SelLength |
| SelStart |
| SequenceName |
| StepGroup |
| StepId |
| StepIndex |
| StepName |
| ThreadDisplayName |
| ThreadId |
| TypeCategory |
| TypeName |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locationkinds.html language=enus -->
## TOPIC 01647: LocationKinds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locationkinds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locationkinds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration with the Location.Kind property. LocationKind_Execution –(Value: 2) Specifies a location in a SequenceContext . LocationKind_File –(Value: 1) Specifies a location in a file. LocationKind_IOConfiguration –(Value: 4) Specifies a location in an IO Configuration. LocationKind_Type –

### LocationKinds

Use this enumeration with the
 [Location.Kind](location-kind.html)
 property.

- LocationKind_Execution 
 –(Value: 2) Specifies a location in a
 SequenceContext 
 .
- LocationKind_File 
 –(Value: 1) Specifies a location in a file.
- LocationKind_IOConfiguration 
 –(Value: 4) Specifies a location in an IO Configuration.
- LocationKind_Type 
 –(Value: 3) Specifies a location in a type.

#### See Also

[Location.Kind](location-kind.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addapilocation.html language=enus -->
## TOPIC 01648: Locations.AddAPILocation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addapilocation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addapilocation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddAPILocation( baseObj, apiLocation, objFile = NULL) Return Value Location Purpose Use this method to add a new file location from an API call to the collection. Parameters baseObj As PropertyObject [In] Specifies the base object to use with the apiLocation parameter as the locatio

### Locations.AddAPILocation

#### Syntax

[Locations](locations.html).AddAPILocation( baseObj, apiLocation, objFile = NULL)

#### Return Value

[Location](location.html)

#### Purpose

Use this method to add a new file location from an API call to the collection.

#### Parameters

baseObj
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the base object to use with the
 apiLocation
 parameter as the location to add.

apiLocation
 As
 [APILocations](apilocations.html)

[In] Pass the
 
 [APILocations](apilocations.html)
 enumeration to use as the location to add.

objFile
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies the file associated with the base object. Use this parameter only if the
 baseObj
 parameter is a type definition. TestStand ignores this parameter if the
 baseObj
 parameter is not a type definition.

This parameter has a default value of
 NULL
 .

#### See Also

[Locations.AddExecutionLocation](locations-addexecutionlocation.html)

[Locations.AddExecutionLocationByObject](locations-addexecutionlocationbyobject.html)

[Locations.AddFileLocation](locations-addfilelocation.html)

[Locations.AddFileLocationByObject](locations-addfilelocationbyobject.html)

[Locations.AddTypeLocation](locations-addtypelocation.html)

[Locations.AddTypeLocationByObject](locations-addtypelocationbyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addexecutionlocation.html language=enus -->
## TOPIC 01649: Locations.AddExecutionLocation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addexecutionlocation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addexecutionlocation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddExecutionLocation( seqContext, lookupString, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1) Return Value Location The Location added to the collection. Purpose Adds a new execution location to the collection. Parameters seqContext As SequenceContext

### Locations.AddExecutionLocation

#### Syntax

[Locations](locations.html).AddExecutionLocation( seqContext, lookupString, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1)

#### Return Value

[Location](location.html)

The Location added to the collection.

#### Purpose

Adds a new execution location to the collection.

#### Parameters

seqContext
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context to initialize the
 [Location.ContextId](location-contextid.html)
 ,
 [Location.ExecutionId](location-executionid.html)
 , and
 [Location.ThreadId](location-threadid.html)
 properties.

lookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the path to a subproperty of the
 seqContext
 parameter. This method sets the
 [Location.PropertyPath](location-propertypath.html)
 property of the new Location using the lookup string you pass. This method also sets as many properties of the new Location as this method can obtain from the subproperty this parameter specifies.

elem
 As
 [PropertyObjectElements](propertyobjectelements.html)

[In] Specifies the value of the
 [Location.Element](location-element.html)
 property of the new location.

This parameter has a default value of
 PropertyObjectElement_None
 .

selectionStart
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelStart](location-selstart.html)
 property of the new location.

This parameter has a default value of
 0
 .

selectionLength
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelLength](location-sellength.html)
 property of the new location.

This parameter has a default value of
 -1
 .

#### See Also

[Location](location.html)

[Location.ContextId](location-contextid.html)

[Location.Element](location-element.html)

[Location.ExecutionId](location-executionid.html)

[Location.Kind](location-kind.html)

[Location.PropertyPath](location-propertypath.html)

[Location.SelLength](location-sellength.html)

[Location.SelStart](location-selstart.html)

[Location.ThreadId](location-threadid.html)

[Locations.AddExecutionLocation](locations-addexecutionlocation.html)

[Locations.AddTypeLocation](locations-addtypelocation.html)

[PropertyObjectElements](propertyobjectelements.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addexecutionlocationbyobject.html language=enus -->
## TOPIC 01650: Locations.AddExecutionLocationByObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addexecutionlocationbyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addexecutionlocationbyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddExecutionLocationByObject( seqContext, obj, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1) Return Value Location The Location added to the collection. Purpose Adds a new execution location to the collection. Parameters seqContext As SequenceContext [

### Locations.AddExecutionLocationByObject

#### Syntax

[Locations](locations.html).AddExecutionLocationByObject( seqContext, obj, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1)

#### Return Value

[Location](location.html)

The Location added to the collection.

#### Purpose

Adds a new execution location to the collection.

#### Parameters

seqContext
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context to initialize the
 [Location.ContextId](location-contextid.html)
 ,
 [Location.ExecutionId](location-executionid.html)
 , and
 [Location.ThreadId](location-threadid.html)
 properties.

obj
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a subproperty of the
 seqContext
 parameter. This method sets the
 [Location.PropertyPath](location-propertypath.html)
 property of the new Location to the lookup string to obj from seqContext. This method also sets as many properties of the new Location as this method can obtain from the object which you pass.

elem
 As
 [PropertyObjectElements](propertyobjectelements.html)

[In] Specifies the value of the
 [Location.Element](location-element.html)
 property of the new location.

This parameter has a default value of
 PropertyObjectElement_None
 .

selectionStart
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelStart](location-selstart.html)
 property of the new location.

This parameter has a default value of
 0
 .

selectionLength
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelLength](location-sellength.html)
 property of the new location.

This parameter has a default value of
 -1
 .

#### See Also

[Location](location.html)

[Location.ContextId](location-contextid.html)

[Location.Element](location-element.html)

[Location.ExecutionId](location-executionid.html)

[Location.Kind](location-kind.html)

[Location.PropertyPath](location-propertypath.html)

[Location.SelLength](location-sellength.html)

[Location.SelStart](location-selstart.html)

[Location.ThreadId](location-threadid.html)

[Locations.AddExecutionLocation](locations-addexecutionlocation.html)

[Locations.AddTypeLocation](locations-addtypelocation.html)

[PropertyObject](propertyobject.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addfilelocation.html language=enus -->
## TOPIC 01651: Locations.AddFileLocation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addfilelocation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addfilelocation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddFileLocation( file, lookupString, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1) Return Value Location The Location added to the collection. Purpose Adds a new file location to the collection. Parameters file As PropertyObjectFile [In] Specifies ss t

### Locations.AddFileLocation

#### Syntax

[Locations](locations.html).AddFileLocation( file, lookupString, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1)

#### Return Value

[Location](location.html)

The Location added to the collection.

#### Purpose

Adds a new file location to the collection.

#### Parameters

file
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies ss the file to initialize the
 [Location.FileDisplayName](location-filedisplayname.html)
 ,
 [Location.FileId](location-fileid.html)
 , and
 [Location.FilePath](location-filepath.html)
 properties.

lookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies a subproperty of the file parameter. This method sets the
 [Location.PropertyPath](location-propertypath.html)
 property of the new Location to the lookup string to lookupString from file. This method also sets as many properties of the new Location as this method can obtain from the object you pass. This method specifies the
 lookupString
 parameter relative to the root of the
 [PropertyObjectFile](propertyobjectfile.html)
 object. For example, if the location is underneath the
 PropertyObjectFile.Data
 element, the lookup string must use the
 Data.
 prefix.

elem
 As
 [PropertyObjectElements](propertyobjectelements.html)

[In] Specifies the value of the
 [Location.Element](location-element.html)
 property of the new location.

This parameter has a default value of
 PropertyObjectElement_None
 .

selectionStart
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelStart](location-selstart.html)
 property of the new location.

This parameter has a default value of
 0
 .

selectionLength
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelLength](location-sellength.html)
 property of the new location.

This parameter has a default value of
 -1
 .

#### See Also

[Location](location.html)

[Location.Element](location-element.html)

[Location.FileDisplayName](location-filedisplayname.html)

[Location.FileId](location-fileid.html)

[Location.FilePath](location-filepath.html)

[Location.Kind](location-kind.html)

[Location.PropertyPath](location-propertypath.html)

[Location.SelLength](location-sellength.html)

[Location.SelStart](location-selstart.html)

[Locations.AddExecutionLocation](locations-addexecutionlocation.html)

[Locations.AddTypeLocation](locations-addtypelocation.html)

[PropertyObjectElements](propertyobjectelements.html)

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addfilelocationbyobject.html language=enus -->
## TOPIC 01652: Locations.AddFileLocationByObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addfilelocationbyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addfilelocationbyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddFileLocationByObject( obj, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1) Return Value Location The Location added to the collection. Purpose Adds a new file location to the collection. Parameters obj As PropertyObject [In] Specifies any PropertyObje

### Locations.AddFileLocationByObject

#### Syntax

[Locations](locations.html).AddFileLocationByObject( obj, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1)

#### Return Value

[Location](location.html)

The Location added to the collection.

#### Purpose

Adds a new file location to the collection.

#### Parameters

obj
 As
 [PropertyObject](propertyobject.html)

[In] Specifies any PropertyObject, such as step, sequence, variable, or sequence context. This method sets as many properties of the new Location object as this method can obtain from the object you pass.

elem
 As
 [PropertyObjectElements](propertyobjectelements.html)

[In] Specifies the value of the
 [Location.Element](location-element.html)
 property of the new location.

This parameter has a default value of
 PropertyObjectElement_None
 .

selectionStart
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelStart](location-selstart.html)
 property of the new location.

This parameter has a default value of
 0
 .

selectionLength
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelLength](location-sellength.html)
 property of the new location.

This parameter has a default value of
 -1
 .

#### See Also

[Location](location.html)

[Location.Element](location-element.html)

[Location.Kind](location-kind.html)

[Location.PropertyPath](location-propertypath.html)

[Location.SelLength](location-sellength.html)

[Location.SelStart](location-selstart.html)

[Locations.AddExecutionLocation](locations-addexecutionlocation.html)

[Locations.AddTypeLocation](locations-addtypelocation.html)

[PropertyObject](propertyobject.html)

[PropertyObjectElements](propertyobjectelements.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addioconfiguraionlocation.html language=enus -->
## TOPIC 01653: Locations.AddIOConfiguraionLocation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addioconfiguraionlocation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addioconfiguraionlocation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddIOConfiguraionLocation( ioConfigurationName ) Return Value Location The Location added to the collection. Purpose Adds a new IOConfiguration location to the collection. Parameters ioConfigurationName As String [In] Specifies the name of the IOConfiguration pane that is activated.

### Locations.AddIOConfiguraionLocation

#### Syntax

[Locations](locations.html).AddIOConfiguraionLocation( ioConfigurationName )

#### Return Value

[Location](location.html)

The Location added to the collection.

#### Purpose

Adds a new IOConfiguration location to the collection.

#### Parameters

ioConfigurationName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the IOConfiguration pane that is activated.

#### See Also

[Locations](locations.html)

[Locations.GotoLocation](locations-gotolocation.html)

[Locations.LocationFound](locations-locationfound.html)

[Locations.LocationNotFoundMessage](locations-locationnotfoundmessage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addlocations.html language=enus -->
## TOPIC 01654: Locations.AddLocations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addlocations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addlocations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddLocations( locationsToAdd, copyLocationOption) Purpose Adds the Location objects from a specified Locations to the end of this Locations. Parameters locationsToAdd As Locations [In] Specifies Locations to append to this Locations. copyLocationOption As CopyLocationsOptions [In] S

### Locations.AddLocations

#### Syntax

[Locations](locations.html).AddLocations( locationsToAdd, copyLocationOption)

#### Purpose

Adds the
 [Location](location.html)
 objects from a specified Locations to the end of this Locations.

#### Parameters

locationsToAdd
 As
 [Locations](locations.html)

[In] Specifies Locations to append to this Locations.

copyLocationOption
 As
 [CopyLocationsOptions](copylocationsoptions.html)

[In] Specifies whether this method copies locationsToAdd before adding them to the collection.

#### See Also

[CopyLocationsOptions](copylocationsoptions.html)

[Location](location.html)

[Locations](locations.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addtypelocation.html language=enus -->
## TOPIC 01655: Locations.AddTypeLocation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addtypelocation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addtypelocation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddTypeLocation( file, rootTypeDef, lookupString, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1) Return Value Location The Location added to the collection. Purpose Adds a new type location to the collection. Parameters file As PropertyObjectFile [In] S

### Locations.AddTypeLocation

#### Syntax

[Locations](locations.html).AddTypeLocation( file, rootTypeDef, lookupString, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1)

#### Return Value

[Location](location.html)

The Location added to the collection.

#### Purpose

Adds a new type location to the collection.

#### Parameters

file
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies the file in which the type you pass to the
 rootTypeDef
 parameter is saved.

rootTypeDef
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a type definition. This method sets the
 [Location.TypeName](location-typename.html)
 and
 [Location.TypeCategory](location-typecategory.html)
 properties of the new Location from the root type definition this parameter specifies. This method also sets the
 [Location.PropertyPath](location-propertypath.html)
 property of the new Location using the
 lookupString
 parameter.

lookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the path to a subproperty of the
 rootTypeDef
 parameter. This method sets the
 [Location.PropertyPath](location-propertypath.html)
 property of the new Location using the lookup string you pass. This method also sets as many properties of the new Location as this method can obtain from the subproperty this parameter specifies.

elem
 As
 [PropertyObjectElements](propertyobjectelements.html)

[In] Specifies the value of the
 [Location.Element](location-element.html)
 property of the new location.

This parameter has a default value of
 PropertyObjectElement_None
 .

selectionStart
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelStart](location-selstart.html)
 property of the new location.

This parameter has a default value of
 0
 .

selectionLength
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelLength](location-sellength.html)
 property of the new location.

This parameter has a default value of
 -1
 .

#### See Also

[Location](location.html)

[Location.Element](location-element.html)

[Location.Kind](location-kind.html)

[Location.PropertyPath](location-propertypath.html)

[Location.SelLength](location-sellength.html)

[Location.SelStart](location-selstart.html)

[Location.ThreadId](location-threadid.html)

[Location.TypeCategory](location-typecategory.html)

[Location.TypeName](location-typename.html)

[Locations.AddExecutionLocation](locations-addexecutionlocation.html)

[Locations.AddTypeLocation](locations-addtypelocation.html)

[PropertyObject](propertyobject.html)

[PropertyObject.IsRootTypeDefinition](propertyobject-isroottypedefinition.html)

[PropertyObject.IsTypeDefinition](propertyobject-istypedefinition.html)

[PropertyObjectElements](propertyobjectelements.html)

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-addtypelocationbyobject.html language=enus -->
## TOPIC 01656: Locations.AddTypeLocationByObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-addtypelocationbyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-addtypelocationbyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.AddTypeLocationByObject( file, obj, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1) Return Value Location The Location added to the collection. Purpose Adds a new type location to the collection. Parameters file As PropertyObjectFile [In] Specifies the f

### Locations.AddTypeLocationByObject

#### Syntax

[Locations](locations.html).AddTypeLocationByObject( file, obj, elem = PropertyObjectElement_None, selectionStart = 0, selectionLength = -1)

#### Return Value

[Location](location.html)

The Location added to the collection.

#### Purpose

Adds a new type location to the collection.

#### Parameters

file
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies the file in which the type you pass to the
 obj
 parameter is saved.

obj
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a type definition. This method sets the
 [Location.TypeName](location-typename.html)
 and
 [Location.TypeCategory](location-typecategory.html)
 properties of the new Location from the root type definition that contains the type definition you pass. This method sets the
 [Location.PropertyPath](location-propertypath.html)
 property of the new Location to the lookup string to obj from the root type definition of obj.

elem
 As
 [PropertyObjectElements](propertyobjectelements.html)

[In] Specifies the value of the
 [Location.Element](location-element.html)
 property of the new location.

This parameter has a default value of
 PropertyObjectElement_None
 .

selectionStart
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelStart](location-selstart.html)
 property of the new location.

This parameter has a default value of
 0
 .

selectionLength
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the value of the
 [Location.SelLength](location-sellength.html)
 property of the new location.

This parameter has a default value of
 -1
 .

#### See Also

[Location](location.html)

[Location.Element](location-element.html)

[Location.Kind](location-kind.html)

[Location.PropertyPath](location-propertypath.html)

[Location.SelLength](location-sellength.html)

[Location.SelStart](location-selstart.html)

[Location.ThreadId](location-threadid.html)

[Location.TypeCategory](location-typecategory.html)

[Location.TypeName](location-typename.html)

[Locations.AddExecutionLocation](locations-addexecutionlocation.html)

[Locations.AddTypeLocation](locations-addtypelocation.html)

[PropertyObject](propertyobject.html)

[PropertyObject.IsRootTypeDefinition](propertyobject-isroottypedefinition.html)

[PropertyObject.IsTypeDefinition](propertyobject-istypedefinition.html)

[PropertyObjectElements](propertyobjectelements.html)

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-applicationsite.html language=enus -->
## TOPIC 01657: Locations.ApplicationSite

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-applicationsite.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-applicationsite.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.ApplicationSite Data Type ApplicationSites Use the following constants with this data type: ApplicationSite_DefaultSite –(Value: 0) Specifies that the user interface determines where to display the location. ApplicationSite_ItemList –(Value: 1) Specifies that the user interface disp

### Locations.ApplicationSite

#### Syntax

[Locations](locations.html).ApplicationSite

#### Data Type

[ApplicationSites](applicationsites.html)

Use the following constants with this data type:

- ApplicationSite_DefaultSite 
 –(Value: 0) Specifies that the user interface determines where to display the location.
- ApplicationSite_ItemList 
 –(Value: 1) Specifies that the user interface displays the location in a list control, such as a list of steps or a list of sequences.
- ApplicationSite_PropertyBrowser 
 –(Value: 3) Specifies that the user interface displays the location in a control that displays a hierarchy of properties and subproperties.
- ApplicationSite_Settings 
 –(Value: 4) Specifies that the user interface displays the location in a settings panel or dialog.
- ApplicationSite_Variables 
 –(Value: 2) Specifies that the user interface displays the location in a variables control.

#### Purpose

Specifies where to display a location in a user interface when the user interface can display the location in more than one place.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-candisplaydialog.html language=enus -->
## TOPIC 01658: Locations.CanDisplayDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-candisplaydialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-candisplaydialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.CanDisplayDialog Data Type Boolean Purpose This property specifies if calling the Locations.GotoLocation method can display the location in a dialog box. If you handle the UIMsg_GotoLocation user interface message, check the value of this property before displaying a location in a d

### Locations.CanDisplayDialog

#### Syntax

[Locations](locations.html).CanDisplayDialog

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

This property specifies if calling the
 [Locations.GotoLocation](locations-gotolocation.html)
 method can display the location in a dialog box. If you handle the
 UIMsg_GotoLocation
 user interface message, check the value of this property before displaying a location in a dialog box. The default value of this property is
 True
 .

#### Remarks

If the user interface cannot go to the location, the
 Locations.GotoLocation
 method uses the
 options
 parameter to determine whether to launch a dialog box to inform the user that the user interface could not go to the location.

#### See Also

[Locations.GotoLocation](locations-gotolocation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-clear.html language=enus -->
## TOPIC 01659: Locations.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.Clear Purpose Removes all items from this collection. See Also Locations.Remove

### Locations.Clear

#### Syntax

[Locations](locations.html).Clear

#### Purpose

Removes all items from this collection.

#### See Also

[Locations.Remove](locations-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-count.html language=enus -->
## TOPIC 01660: Locations.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.Count Data Type Long Purpose Returns the number of items in the collection.

### Locations.Count

#### Syntax

[Locations](locations.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-frompropertyobject.html language=enus -->
## TOPIC 01661: Locations.FromPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-frompropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-frompropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.FromPropertyObject( val) Purpose Restores the Locations state the Locations.ToPropertyObject method stores in the PropertyObject . Parameters val As PropertyObject [In] Specifies the PropertyObject . See Also Locations Locations.ToPropertyObject PropertyObject

### Locations.FromPropertyObject

#### Syntax

[Locations](locations.html).FromPropertyObject( val)

#### Purpose

Restores the
 [Locations](locations.html)
 state the
 [Locations.ToPropertyObject](locations-topropertyobject.html)
 method stores in the
 [PropertyObject](propertyobject.html)
 .

#### Parameters

val
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the
 PropertyObject
 .

#### See Also

[Locations](locations.html)

[Locations.ToPropertyObject](locations-topropertyobject.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-gotolocation.html language=enus -->
## TOPIC 01662: Locations.GotoLocation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-gotolocation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-gotolocation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.GotoLocation( options = 0) Purpose This method sends this Locations collection to the user interface in a synchronous UIMsg_GotoLocation user interface message. If the user interface supports GotoLocation, the user interface displays this location by updating which controls are visi

### Locations.GotoLocation

#### Syntax

[Locations](locations.html).GotoLocation( options = 0)

#### Purpose

This method sends this Locations collection to the user interface in a synchronous
 UIMsg_GotoLocation
 user interface message. If the user interface supports GotoLocation, the user interface displays this location by updating which controls are visible and active and by updating the selected state of controls.

#### Remarks

After you call this method, you can use the
 [Locations.LocationFound](locations-locationfound.html)
 property to see if the user interface successfully went to the location. If the
 Locations.LocationFound
 property is
 False
 , you can use the
 [Locations.LocationNotFoundMessage](locations-locationnotfoundmessage.html)
 property to obtain a description of why the user interface could not go to the location.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of
 [GotoLocationOptions](gotolocationoptions.html)
 .

This parameter has a default value of
 0
 .

#### See Also

[GotoLocationOptions](gotolocationoptions.html)

[Locations.LocationFound](locations-locationfound.html)

[Locations.LocationNotFoundMessage](locations-locationnotfoundmessage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-gotolocationinapplication.html language=enus -->
## TOPIC 01663: Locations.GotoLocationInApplication

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-gotolocationinapplication.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-gotolocationinapplication.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.GotoLocationInApplication( applicationPath, options = 0) Purpose Sends the Locations collection to the user interface the applicationPath parameter specifies. If the user interface supports the Locations.GotoLocation method, the user interface displays the location by updating which

### Locations.GotoLocationInApplication

#### Syntax

[Locations](locations.html).GotoLocationInApplication( applicationPath, options = 0)

#### Purpose

Sends the
 [Locations](locations.html)
 collection to the user interface the
 applicationPath
 parameter specifies. If the user interface supports the
 [Locations.GotoLocation](locations-gotolocation.html)
 method, the user interface displays the location by updating which controls are visible and active and by updating the selected state of controls.

#### Remarks

If the
 applicationPath
 parameter specifies the path of the currently executing user interface, this method behaves the same as the
 Locations.GotoLocation
 method. Otherwise, this method differs from the
 Locations.GotoLocation
 method in the following ways:

- This method supports only
 Locations 
 of
 LocationKind_File 
 type.
- If the
 applicationPath 
 parameter specifies the path of a user interface that is currently executing, this method attempts to go to the location in that instance of the user interface. Otherwise, this method starts a new instance of the user interface and attempts to go to the location in that instance.
- This method does not set the
 Locations.LocationFound 
 property and does not use the
 Locations.LocationNotFoundMessage 
 property when the
 applicationPath 
 parameter specifies an external user interface.

#### Parameters

applicationPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the user interface application.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of
 [GotoLocationOptions](gotolocationoptions.html)
 . This method does not use the
 GotoLocationOption_DoNotDisplayMessageIfLocationNotFound
 option unless the
 applicationPath
 parameter specifies the path of the currently executing user interface.

This parameter has a default value of
 0
 .

#### See Also

[GotoLocationOptions](gotolocationoptions.html)

[LocationKinds](locationkinds.html)

[Locations](locations.html)

[Locations.GotoLocation](locations-gotolocation.html)

[Locations.LocationFound](locations-locationfound.html)

[Locations.LocationNotFoundMessage](locations-locationnotfoundmessage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-item.html language=enus -->
## TOPIC 01664: Locations.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.Item( index) Data Type Location Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Long [In] Specifies the zero-based index of the item to retrieve. See Also Location

### Locations.Item

#### Syntax

[Locations](locations.html).Item( index)

#### Data Type

[Location](location.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[Location](location.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-locationfound.html language=enus -->
## TOPIC 01665: Locations.LocationFound

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-locationfound.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-locationfound.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.LocationFound Data Type Boolean Purpose When you handle the UIMsg_GotoLocation user interface message, set this property to True to indicate that the user interface selected the Locations collection. If you do not set this property to True , the Locations.GotoLocation method display

### Locations.LocationFound

#### Syntax

[Locations](locations.html).LocationFound

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

When you handle the
 UIMsg_GotoLocation
 user interface message, set this property to
 True
 to indicate that the user interface selected the
 [Locations](locations.html)
 collection. If you do not set this property to
 True
 , the
 [Locations.GotoLocation](locations-gotolocation.html)
 method displays an error to indicate that the user interface could not go to the Locations.

#### See Also

[Locations](locations.html)

[Locations.GotoLocation](locations-gotolocation.html)

[Locations.LocationNotFoundMessage](locations-locationnotfoundmessage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-locationnotfoundmessage.html language=enus -->
## TOPIC 01666: Locations.LocationNotFoundMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-locationnotfoundmessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-locationnotfoundmessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.LocationNotFoundMessage Data Type String Purpose When you handle the UIMsg_GotoLocation user interface message and do not set the Locations.LocationFound property to True , set this property to a message to explain why the user interface could not go to the Locations . The Locations

### Locations.LocationNotFoundMessage

#### Syntax

[Locations](locations.html).LocationNotFoundMessage

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

When you handle the
 UIMsg_GotoLocation
 user interface message and do not set the
 [Locations.LocationFound](locations-locationfound.html)
 property to
 True
 , set this property to a message to explain why the user interface could not go to the
 [Locations](locations.html)
 . The
 [Locations.GotoLocation](locations-gotolocation.html)
 method includes this message in the error it displays when LocationFound is
 False
 .

#### See Also

[Locations](locations.html)

[Locations.GotoLocation](locations-gotolocation.html)

[Locations.LocationFound](locations-locationfound.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-remove.html language=enus -->
## TOPIC 01667: Locations.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.Remove( index) Purpose Removes the specified item from this collection, if it exists. Parameters index As Long [In] Specifies the zero-based index of the item to remove. See Also Locations.Clear

### Locations.Remove

#### Syntax

[Locations](locations.html).Remove( index)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to remove.

#### See Also

[Locations.Clear](locations-clear.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-topropertyobject.html language=enus -->
## TOPIC 01668: Locations.ToPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-topropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-topropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.ToPropertyObject Return Value PropertyObject Purpose Returns a PropertyObject representation of the Locations collection. You can use the PropertyObject to persist the collection. The PropertyObject representation does not store the value of the Locations.UserData property. See Also

### Locations.ToPropertyObject

#### Syntax

[Locations](locations.html).ToPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns a
 [PropertyObject](propertyobject.html)
 representation of the
 [Locations](locations.html)
 collection. You can use the
 PropertyObject
 to persist the collection.

Note

PropertyObject

Locations.UserData

#### See Also

[Locations](locations.html)

[Locations.FromPropertyObject](locations-frompropertyobject.html)

[Locations.UserData](locations-userdata.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations-userdata.html language=enus -->
## TOPIC 01669: Locations.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Locations.UserData Data Type Variant Purpose Holds a data item you associate with the Locations object.

### Locations.UserData

#### Syntax

[Locations](locations.html).UserData

#### Data Type

[Variant](data-types-for-teststand.html)

#### Purpose

Holds a data item you associate with the Locations object.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/locations.html language=enus -->
## TOPIC 01670: Locations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/locations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/locations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Locations is a collection of Location objects. Use Locations to instruct the user interface to update the selection. Follow these steps to set the selection in a user interface: Call the Engine.NewLocations method to create a Locations object. Call the Locations.AddFileLocation , Locations.AddExecut

### Locations

Locations is a collection of
 [Location](location.html)
 objects. Use Locations to instruct the user interface to update the selection. Follow these steps to set the selection in a user interface:

- Call the
 Engine.NewLocations 
 method to create a Locations object.
- Call the
 Locations.AddFileLocation 
 ,
 Locations.AddExecutionLocation 
 , or
 Locations.AddTypeLocation 
 method on a Locations object to specify data for the user interface to select.
- Call the
 Locations.GotoLocation 
 method on the Locations object to send the Locations object to the user interface.
- The user interface receives the Locations object through the
 UIMessage.ActiveXData 
 property of a UIMsg_GotoLocation UIMessage.
- If the user interface supports the Goto location action, it updates the selection to correspond to the Locations object.

#### Properties

| ApplicationSite |
| --- |
| CanDisplayDialog |
| Count (Read Only) |
| Item (Read Only) |
| LocationFound |
| LocationNotFoundMessage |
| UserData |

#### Methods

| AddAPILocation |
| --- |
| AddExecutionLocation |
| AddExecutionLocationByObject |
| AddFileLocation |
| AddFileLocationByObject |
| AddIOConfiguraionLocation |
| AddLocations |
| AddTypeLocation |
| AddTypeLocationByObject |
| Clear |
| FromPropertyObject |
| GotoLocation |
| GotoLocationInApplication |
| Remove |
| ToPropertyObject |

#### See Also

[AddExecutionLocation](locations-addexecutionlocation.html)

[AddFileLocation](locations-addfilelocation.html)

[AddTypeLocation](locations-addtypelocation.html)

[Engine.NewLocations](engine-newlocations.html)

[GotoLocation](locations-gotolocation.html)

[Location](location.html)

[UIMessage.ActiveXData](uimessage-activexdata.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/lockunlockdialogoptions.html language=enus -->
## TOPIC 01671: LockUnlockDialogOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/lockunlockdialogoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/lockunlockdialogoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the Engine.DisplayLockUnlockDialog method. Use the bitwise-OR operator to specify more than one option. LockUnlockDialogOption_HideRememberPasswordControls –(Value: 4) Specifies that the dialog box does not display the c

### LockUnlockDialogOptions

These constants represent the options you can use with the
 options
 parameter of the
 [Engine.DisplayLockUnlockDialog](engine-displaylockunlockdialog.html)
 method. Use the bitwise-OR operator to specify more than one option.

- LockUnlockDialogOption_HideRememberPasswordControls 
 –(Value: 4) Specifies that the dialog box does not display the control that provides the option to remember the password when unlocking a file.
- LockUnlockDialogOption_Lock 
 –(Value: 1) Specifies to launch a dialog box that prompts for a password to perform a lock operation. This option is ignored if you are attempting to lock a specific object.
- LockUnlockDialogOption_ModalToAppMainWind 
 –(Value: 0x10000) By default, the dialog box is modal to the last active window of the calling thread, or if none exists, to the last active window from AppMainHwnd. If you enable this option, the dialog box is modal with respect to the window handle of the
 Engine.AppMainHwnd 
 property. Typically, you do not need to set this option.
- LockUnlockDialogOption_None 
 –(Value: 0) Specifies to lock or unlock the object depending on the locked state of the object.
- LockUnlockDialogOption_Unlock 
 –(Value: 2) Specifies to launch a dialog box that prompts for a password to perform an unlock operation. This option is ignored if you are attempting to unlock a specific object.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayLockUnlockDialog](engine-displaylockunlockdialog.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/lvstepadditions.html language=enus -->
## TOPIC 01672: LVStepAdditions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/lvstepadditions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/lvstepadditions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Do not use these constants to access the adapter-specific properties of a step. Use the LabVIEWModule interface for the Module object for the step. Use the Step.Module property to acquire a reference to a Module object. In TestStand 3.0 or later, these string constants are obsolete. These string con

### LVStepAdditions

Note

LabVIEWModule

Step.Module

In TestStand 3.0 or later, these string constants are obsolete.

These string constants were previously used to create
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 to access the adapter-specific properties of a LabVIEW step. The following example code sets the module pathname of a LabVIEW step:

TS_PropertySetValString(propObj, &errorInfo,
 [Step_TSInfoProp](stepproperties.html)
 "."
 [TSInfo_StepAdditions](stepproperties.html)
 "." LVStep_ModulePathProp, 0, testFilePath)
 ;

- LVStep_ModulePathProp 
 –(Value: "ViPath") This constant is obsolete.
- LVStep_PassInBufProp 
 –(Value: "PassInBuf") This constant is obsolete.
- LVStep_PassInvocInfoProp 
 –(Value: "PassInvocInfo") This constant is obsolete.
- LVStep_PassSeqContextProp 
 –(Value: "PassContextPtr") This constant is obsolete.
- LVStep_ShowFrontPanelProp 
 –(Value: "ShowFrntPnl") This constant is obsolete.

#### See Also

[LabVIEWModule](labviewmodule.html)

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[Step.Module](step-module.html)

[StepProperties](stepproperties.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/menuitemproperties.html language=enus -->
## TOPIC 01673: MenuItemProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/menuitemproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/menuitemproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these property names with the property objects the Engine.GetInsertStepMenuStructure , Engine.GetInsertVariableMenuStructure , and Step.GetEditSubstepMenuStructure methods return to access information about menu structures. Menu_EditsSelectedFileProp –(Value: "EditsSelectedFile") Boolean value t

### MenuItemProperties

Use these property names with the property objects the
 [Engine.GetInsertStepMenuStructure](engine-getinsertstepmenustructure.html)
 ,
 [Engine.GetInsertVariableMenuStructure](engine-getinsertvariablemenustructure.html)
 , and
 [Step.GetEditSubstepMenuStructure](step-geteditsubstepmenustructure.html)
 methods return to access information about menu structures.

- Menu_EditsSelectedFileProp 
 –(Value: "EditsSelectedFile") Boolean value that specifies whether a Tools menu item edits the selected file. Only the
 Engine.GetToolMenuStructure 
 method set this property.
- Menu_HasEditPanelProp 
 –(Value: "HasEditPanel") Boolean value that specifies whether an Edit substep menu item has a corresponding edit panel that displays in the Step Settings pane of the sequence editor. The sequence editor does not invoke an edit substep if the substep has an edit panel.
- Menu_IsDimmedProp 
 –(Value: "IsDimmed") Boolean value that specifies if the menu item is disabled.
- Menu_IsSubmenuProp 
 –(Value: "IsSubMenu") Boolean value that specifies if the menu item is a submenu. Use the
 Menu_MenuItemsProp 
 to access the submenu items.
- Menu_MenuItemsProp 
 –(Value: "MenuItems") Array of property objects that represent the menu items in a submenu.
- Menu_NameProp 
 –(Value: "Name") String value that specifies the text to display for the menu item.
- Menu_SeparatorAboveProp 
 –(Value: "SeparatorAbove") Boolean value that specifies if a separator exists above the menu item.
- Menu_SubstepIndexProp 
 –(Value: "SubstepIndex") Number value that is the index of the substep for this menu item. Only the
 StepType.GetSubstep 
 method sets this property.
- Menu_SupportsReadOnlyProp 
 –(Value: "SupportsReadOnly") Boolean value that specifies if an Edit substep menu item supports launching a dialog box as read-only when the
 Step.EditAsReadOnly 
 property is
 True 
 .
- Menu_ToolIDProp 
 –(Value: "ToolMenuId") Number value that specifies the Tools menu ID for the menu item. Only the
 Engine.GetToolMenuStructure 
 method sets this property.

#### See Also

[Engine.GetInsertStepMenuStructure](engine-getinsertstepmenustructure.html)

[Engine.GetInsertVariableMenuStructure](engine-getinsertvariablemenustructure.html)

[Engine.GetToolMenuStructure](engine-gettoolmenustructure.html)

[Step.EditAsReadOnly](step-editasreadonly.html)

[Step.GetEditSubstepMenuStructure](step-geteditsubstepmenustructure.html)

[StepType.GetSubstep](steptype-getsubstep.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods.html language=enus -->
## TOPIC 01674: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ActiveXAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_10.html language=enus -->
## TOPIC 01675: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_10.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_10.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CVIAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_100.html language=enus -->
## TOPIC 01676: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_100.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_100.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

UndoItems

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_101.html language=enus -->
## TOPIC 01677: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_101.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_101.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

UndoStack

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_102.html language=enus -->
## TOPIC 01678: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_102.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_102.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

UnmappedArgumentValues

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_103.html language=enus -->
## TOPIC 01679: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_103.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_103.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

User

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_104.html language=enus -->
## TOPIC 01680: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_104.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_104.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

UsersFile

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_105.html language=enus -->
## TOPIC 01681: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_105.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_105.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_106.html language=enus -->
## TOPIC 01682: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_106.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_106.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

WatchExpression

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_107.html language=enus -->
## TOPIC 01683: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_107.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_107.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

WatchExpressions

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_108.html language=enus -->
## TOPIC 01684: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_108.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_108.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

WorkspaceFile

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_109.html language=enus -->
## TOPIC 01685: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_109.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_109.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

WorkspaceObject

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_11.html language=enus -->
## TOPIC 01686: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_11.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_11.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CVIModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_12.html language=enus -->
## TOPIC 01687: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_12.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_12.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CVIParameter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_13.html language=enus -->
## TOPIC 01688: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_13.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_13.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CVIParameters

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_14.html language=enus -->
## TOPIC 01689: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_14.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_14.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DllAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_15.html language=enus -->
## TOPIC 01690: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_15.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_15.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DllModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_16.html language=enus -->
## TOPIC 01691: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_16.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_16.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DllParameter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_17.html language=enus -->
## TOPIC 01692: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_17.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_17.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DllParameters

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_18.html language=enus -->
## TOPIC 01693: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_18.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_18.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DotNetAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_19.html language=enus -->
## TOPIC 01694: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_19.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_19.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DotNetCall

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_2.html language=enus -->
## TOPIC 01695: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ActiveXCoClass

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_20.html language=enus -->
## TOPIC 01696: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_20.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_20.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DotNetCalls

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_21.html language=enus -->
## TOPIC 01697: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_21.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_21.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DotNetModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_22.html language=enus -->
## TOPIC 01698: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_22.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_22.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

DotNetParameter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_23.html language=enus -->
## TOPIC 01699: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_23.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_23.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

HTBasicAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_24.html language=enus -->
## TOPIC 01700: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_24.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_24.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

HTBasicModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_25.html language=enus -->
## TOPIC 01701: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_25.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_25.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_26.html language=enus -->
## TOPIC 01702: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_26.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_26.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_27.html language=enus -->
## TOPIC 01703: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_27.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_27.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNodeProperties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_28.html language=enus -->
## TOPIC 01704: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_28.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_28.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNodeProperty

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_29.html language=enus -->
## TOPIC 01705: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_29.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_29.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNXGAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_3.html language=enus -->
## TOPIC 01706: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ActiveXModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_30.html language=enus -->
## TOPIC 01707: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_30.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_30.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNXGModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_31.html language=enus -->
## TOPIC 01708: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_31.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_31.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNXGNodeProperties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_32.html language=enus -->
## TOPIC 01709: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_32.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_32.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNXGNodeProperty

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_33.html language=enus -->
## TOPIC 01710: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_33.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_33.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNXGParameter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_34.html language=enus -->
## TOPIC 01711: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_34.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_34.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNXGParameters

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_35.html language=enus -->
## TOPIC 01712: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_35.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_35.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNXGProject

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_36.html language=enus -->
## TOPIC 01713: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_36.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_36.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWNXGProjectItems

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_37.html language=enus -->
## TOPIC 01714: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_37.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_37.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWParameter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_38.html language=enus -->
## TOPIC 01715: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_38.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_38.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWParameterElement

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_39.html language=enus -->
## TOPIC 01716: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_39.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_39.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

LabVIEWParameters

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_4.html language=enus -->
## TOPIC 01717: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ActiveXParameter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_40.html language=enus -->
## TOPIC 01718: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_40.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_40.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

PythonAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_41.html language=enus -->
## TOPIC 01719: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_41.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_41.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

PythonModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_42.html language=enus -->
## TOPIC 01720: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_42.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_42.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

PythonParameter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_43.html language=enus -->
## TOPIC 01721: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_43.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_43.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

PythonParameters

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_44.html language=enus -->
## TOPIC 01722: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_44.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_44.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceAdapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_45.html language=enus -->
## TOPIC 01723: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_45.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_45.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceCallModule

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_46.html language=enus -->
## TOPIC 01724: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_46.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_46.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

SequenceCallParameter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_47.html language=enus -->
## TOPIC 01725: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_47.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_47.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Adapter

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_48.html language=enus -->
## TOPIC 01726: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_48.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_48.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

AdditionalResults

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_49.html language=enus -->
## TOPIC 01727: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_49.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_49.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ArrayDimensions

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_5.html language=enus -->
## TOPIC 01728: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ActiveXServer

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_50.html language=enus -->
## TOPIC 01729: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_50.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_50.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CsvFileInputRecordStream

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_51.html language=enus -->
## TOPIC 01730: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_51.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_51.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CsvFileOutputRecordStream

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_52.html language=enus -->
## TOPIC 01731: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_52.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_52.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

EditArgs

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_53.html language=enus -->
## TOPIC 01732: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_53.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_53.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

EditTimeMenuItems

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_54.html language=enus -->
## TOPIC 01733: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_54.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_54.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Engine

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_55.html language=enus -->
## TOPIC 01734: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_55.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_55.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

EngineEnvironment

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_56.html language=enus -->
## TOPIC 01735: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_56.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_56.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

EngineInitializationSettings

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_57.html language=enus -->
## TOPIC 01736: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_57.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_57.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

EngineInitializer

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_58.html language=enus -->
## TOPIC 01737: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_58.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_58.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Execution

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_59.html language=enus -->
## TOPIC 01738: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_59.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_59.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExecutionOutputRecordStream

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_6.html language=enus -->
## TOPIC 01739: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_6.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_6.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ActiveXServers

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_60.html language=enus -->
## TOPIC 01740: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_60.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_60.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExecutionOutputRecordStreams

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_61.html language=enus -->
## TOPIC 01741: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_61.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_61.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Expression

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_62.html language=enus -->
## TOPIC 01742: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_62.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_62.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

ExternalReportViewers

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_63.html language=enus -->
## TOPIC 01743: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_63.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_63.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

FileInformation

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_64.html language=enus -->
## TOPIC 01744: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_64.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_64.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Images

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_65.html language=enus -->
## TOPIC 01745: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_65.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_65.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

InputRecordStream

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_66.html language=enus -->
## TOPIC 01746: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_66.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_66.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

InputStream

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_67.html language=enus -->
## TOPIC 01747: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_67.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_67.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

InteractiveArgs

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_68.html language=enus -->
## TOPIC 01748: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_68.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_68.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

InteractiveContext

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_69.html language=enus -->
## TOPIC 01749: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_69.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_69.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

Locations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/methods_7.html language=enus -->
## TOPIC 01750: Methods

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/methods_7.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/methods_7.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the methods in this class.

### Methods

This book contains the methods in this class.

Parent topic:

CommonCAdapter
