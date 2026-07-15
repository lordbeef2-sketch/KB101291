# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=2501 end=2750 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-type.html language=enus -->
## TOPIC 02501: SequenceCallParameter.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.Type Data Type PropertyValueTypes Use the following constants with this data type: PropValType_Array –(Value: 6) Specifies an array. This is not a valid value for PropertyObject creation methods such as Engine.NewPropertyObject and PropertyObject.NewSubProperty . PropVal

### SequenceCallParameter.Type

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).Type

#### Data Type

[PropertyValueTypes](propertyvaluetypes.html)

Use the following constants with this data type:

- PropValType_Array 
 –(Value: 6) Specifies an array. This is not a valid value for PropertyObject creation methods such as
 Engine.NewPropertyObject 
 and
 PropertyObject.NewSubProperty 
 .
- PropValType_Boolean 
 –(Value: 2) Specifies a Boolean type.
- PropValType_Container 
 –(Value: 0) Specifies a container.
- PropValType_Enum 
 –(Value: 7) Specifies an enumeration.
- PropValType_NamedType 
 –(Value: 4) Use this value with PropertyObject creation methods such as
 Engine.NewPropertyObject 
 and
 PropertyObject.NewSubProperty 
 to create an instance of a named type. This is not a valid value for the
 PropertyObjectType.ValueType 
 property.
- PropValType_Number 
 –(Value: 3) Specifies a number.
- PropValType_Reference 
 –(Value: 5) Specifies an object reference.
- PropValType_String 
 –(Value: 1) Specifies a string.

#### Purpose

Note

SequenceCallParameter.PropertyObjectType

PropertyObjectType.ValueType

#### Remarks

Returns the type of the parameter.

#### See Also

[Engine.NewPropertyObject](engine-newpropertyobject.html)

[PropertyObject.NewSubProperty](propertyobject-newsubproperty.html)

[PropertyObjectType.ValueType](propertyobjecttype-valuetype.html)

[SequenceCallParameter.PropertyObjectType](sequencecallparameter-propertyobjecttype.html)

[SequenceCallParameter.Name](sequencecallparameter-name.html)

[SequenceCallParameter.TypeDisplayString](sequencecallparameter-typedisplaystring.html)

Parent topic:

Obsolete SequenceCallParameter Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-typedisplaystring.html language=enus -->
## TOPIC 02502: SequenceCallParameter.TypeDisplayString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-typedisplaystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-typedisplaystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.TypeDisplayString Data Type String Purpose Returns the display string used to describe the parameter type. See Also SequenceCallParameter.Type

### SequenceCallParameter.TypeDisplayString

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).TypeDisplayString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the display string used to describe the parameter type.

#### See Also

[SequenceCallParameter.Type](sequencecallparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-usedefaultvalue.html language=enus -->
## TOPIC 02503: SequenceCallParameter.UseDefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-usedefaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-usedefaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.UseDefaultValue Data Type Boolean Purpose Specifies whether to use the default value of the parameter when calling the subsequence. See Also SequenceCallParameter.ValueExpr

### SequenceCallParameter.UseDefaultValue

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).UseDefaultValue

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to use the default value of the parameter when calling the subsequence.

#### See Also

[SequenceCallParameter.ValueExpr](sequencecallparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-userdata.html language=enus -->
## TOPIC 02504: SequenceCallParameter.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.UserData Data Type PropertyObject Purpose Holds a data item you associate with the parameter object. Remarks Typically, you do not use this property. See Also PropertyObject

### SequenceCallParameter.UserData

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).UserData

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

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-validevaluationtypes.html language=enus -->
## TOPIC 02505: SequenceCallParameter.ValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-validevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-validevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.ValidEvaluationTypes Data Type EvaluationTypes Purpose Returns the valid types to which this parameter can evaluate. Remarks You can pass the value of this property to the validEvaluationTypes parameter of the Expression.ValidateEvaluationType method to determine whether

### SequenceCallParameter.ValidEvaluationTypes

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).ValidEvaluationTypes

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
 [SequenceCallParameter.ValueExpr](sequencecallparameter-valueexpr.html)
 property contains errors.

If you are using an ExpressionEdit control to display the value of the
 SequenceCallParameter.ValueExpr
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

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-valueexpr.html language=enus -->
## TOPIC 02506: SequenceCallParameter.ValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-valueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-valueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.ValueExpr Data Type String Purpose An expression defining the argument to pass for the parameter when calling the subsequence. See Also SequenceCallParameter.UseDefaultValue

### SequenceCallParameter.ValueExpr

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).ValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

An expression defining the argument to pass for the parameter when calling the subsequence.

#### See Also

[SequenceCallParameter.UseDefaultValue](sequencecallparameter-usedefaultvalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter.html language=enus -->
## TOPIC 02507: SequenceCallParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the SequenceCallParameter class to configure and obtain SequenceCallParameter-specific information for an item in the SequenceCallParameters collection class. Properties ArgumentObject (Read Only) Comment (Read Only) Name (Read Only) PassByReference (Read Only) PropertyObjectType (R

### SequenceCallParameter

Use objects from the SequenceCallParameter class to configure and obtain SequenceCallParameter-specific information for an item in the SequenceCallParameters collection class.

#### Properties

| ArgumentObject (Read Only) |
| --- |
| Comment (Read Only) |
| Name (Read Only) |
| PassByReference (Read Only) |
| PropertyObjectType (Read Only) |
| TypeDisplayString (Read Only) |
| UseDefaultValue |
| UserData (Read Only) |
| ValidEvaluationTypes (Read Only) |
| ValueExpr |

#### Method

#### See Also

[SequenceCallParameters](sequencecallparameters.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameters-count.html language=enus -->
## TOPIC 02508: SequenceCallParameters.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameters-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameters-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameters.Count Data Type Long Purpose Returns the number of items in the collection. See Also SequenceCallParameter

### SequenceCallParameters.Count

#### Syntax

[SequenceCallParameters](sequencecallparameters.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[SequenceCallParameter](sequencecallparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameters-item.html language=enus -->
## TOPIC 02509: SequenceCallParameters.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameters-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameters-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameters.Item( index) Data Type SequenceCallParameter Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the parameter to retrieve. See Also SequenceCallParameter

### SequenceCallParameters.Item

#### Syntax

[SequenceCallParameters](sequencecallparameters.html).Item( index)

#### Data Type

[SequenceCallParameter](sequencecallparameter.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to retrieve.

#### See Also

[SequenceCallParameter](sequencecallparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameters.html language=enus -->
## TOPIC 02510: SequenceCallParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the SequenceCallParameters class to configure and obtain parameters for a module that uses the Sequence Adapter. Use the SequenceCallModule.Parameters property to obtain the collection of parameters for a module. Properties Count (Read Only) Item (Read Only) See Also SequenceCallMod

### SequenceCallParameters

Use objects from the SequenceCallParameters class to configure and obtain parameters for a module that uses the Sequence Adapter.

Use the
 [SequenceCallModule.Parameters](sequencecallmodule-parameters.html)
 property to obtain the collection of parameters for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[SequenceCallModule.Parameters](sequencecallmodule-parameters.html)

[SequenceCallParameter](sequencecallparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallstepadditions.html language=enus -->
## TOPIC 02511: SequenceCallStepAdditions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallstepadditions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallstepadditions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Do not use the following constants to access the adapter-specific properties of a step. Use the SequenceCallModule interface for the Module object for the step. Use the Step.Module property to acquire a reference to a Module object. In TestStand 3.0 or later, these string constants are obsolete. The

### SequenceCallStepAdditions

Note

SequenceCallModule

Step.Module

In TestStand 3.0 or later, these string constants are obsolete.

These string constants were previously used to create
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 when using the PropertyObject class to access the adapter-specific properties of a Sequence Call step.

- SCStep_ActualArgsProp 
 –(Value: "ActualArgs") An object that contains a list of arguments to the subsequence. If the subsequence has fewer parameters than the number of arguments, the subsequence ignores the extra arguments. If the subsequence has more parameters than the number of arguments, the subsequences uses the default values of the extra parameters.
- SCStep_ArgPrototypeProp 
 –(Value: "Prototype") An object that contains a list of parameters. TestStand uses the parameter list only for displaying the arguments in the
 Specify Module 
 dialog box. The Specify Module dialog box sets this property when you select a sequence with the Load Prototype button. The value of this property is meaningful only when
 SCStep_UseArgPrototypeProp 
 is
 True 
 .
- SCStep_IgnoreTerminateProp 
 –(Value: "IgnoreTerminate") If this Boolean property is
 True 
 and the user or a step module attempts to terminate the subsequence before it completes, the execution continues with the next step.
- SCStep_SeqFilePathExprProp 
 –(Value: "SFPathExpr") An expression that must evaluate to a string which obtains the pathname of the sequence file that contains the subsequence. The value of this property is meaningful only when
 SCStep_SpecifyByExprProp 
 is
 True 
 and
 Step_UseCurrentFileProp 
 is
 False 
 .
- SCStep_SeqFilePathProp 
 –(Value: "SFPath") Pathname of the sequence file that contains the subsequence. The value of this property is meaningful only when
 SCStep_SpecifyByExprProp 
 and
 SCStep_UseCurrentFileProp 
 are
 False 
 .
- SCStep_SeqNameExprProp 
 –(Value: "SeqNameExpr") An expression, that must evaluate to a string, to obtain the name of the subsequence to be called. The value of this property is meaningful only when
 SCStep_SpecifyByExprProp 
 is
 True 
 .
- SCStep_SeqNameProp 
 –(Value: "SeqName") Name of the subsequence. The value of this property is meaningful only when
 SCStep_SpecifyByExprProp 
 is
 False 
 .
- SCStep_SpecifyByExprProp 
 –(Value: "SpecifyByExpr") If this Boolean property is
 True 
 , TestStand evaluates the
 SCStep_SeqFilePathExprProp 
 expression property to determine the pathname of the sequence file that contains the subsequence. TestStand also evaluates the
 SCStep_SeqNameExprProp 
 expression property to determine the name of the subsequence.
- SCStep_TraceSettingProp 
 –(Value: "Trace") A property that controls if tracing occurs while the subsequence executes. Following are the three possible values:
 SCStep_TraceSettingValOff 
 ,
 Step_TraceSettingValOn 
 , and
 SCStep_TraceSettingValDontChange 
 .
- SCStep_TraceSettingValDontChange 
 –(Value: "Don't Change") A value of the
 SCStep_TraceSettingProp 
 property. When tracing is enabled in the Sequence Call step that calls the subsequence, tracing only occurs while the subsequence executes.
- SCStep_TraceSettingValOff 
 –(Value: "Off") A value of the
 SCStep_TraceSettingProp 
 property. It disables tracing while the subsequence executes.
- SCStep_TraceSettingValOn 
 –(Value: "On") A value of the
 SCStep_TraceSettingProp 
 property. It enables tracing while the subsequence executes.
- SCStep_UseArgPrototypeProp 
 –(Value: "UsePrototype") If this Boolean property is
 True 
 , the prototype for displaying arguments in the Specify Module dialog box is taken from the
 SCStep_ArgPrototypeProp 
 property. If this property is
 False 
 , the prototype is taken from the selected sequence, if any. The Specify Module dialog box sets this property to
 True 
 when you enable the
 Specify Expressions for Pathname and Sequence 
 option or when you disable the
 Use Prototype of Selected Sequence 
 option.
- SCStep_UseCurrentFileProp 
 –(Value: "UseCurFile") A Boolean property that is
 True 
 when the file that contains the Sequence Call step also contains the subsequence.

#### See Also

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[SequenceCallModule](sequencecallmodule.html)

[Specify Module dialog box](../tsref/edit-activex-com-call-dialog-box.html)

[Step.Module](step-module.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-applicationiseditor.html language=enus -->
## TOPIC 02512: SequenceContext.ApplicationIsEditor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-applicationiseditor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-applicationiseditor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.ApplicationIsEditor Data Type Boolean Purpose Returns True if the current application is a sequence editor. See Also Engine.ApplicationIsEditor

### SequenceContext.ApplicationIsEditor

#### Syntax

[SequenceContext](sequencecontext.html).ApplicationIsEditor

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the current application is a sequence editor.

#### See Also

[Engine.ApplicationIsEditor](engine-applicationiseditor.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-aspropertyobject.html language=enus -->
## TOPIC 02513: SequenceContext.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### SequenceContext.AsPropertyObject

#### Syntax

[SequenceContext](sequencecontext.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-caller.html language=enus -->
## TOPIC 02514: SequenceContext.Caller

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-caller.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-caller.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Caller Data Type SequenceContext Purpose Returns the sequence context of the calling sequence. To access additional levels of the call stack, such as the caller of the calling sequence, use the Thread.GetSequenceContext method to specify the desired call stack level as a param

### SequenceContext.Caller

#### Syntax

[SequenceContext](sequencecontext.html).Caller

#### Data Type

[SequenceContext](sequencecontext.html)

#### Purpose

Returns the sequence context of the calling sequence.

Note

Thread.GetSequenceContext

#### Remarks

Returns a
 NULL
 reference if no calling sequence exists. For asynchronously called sequences, this property might reference a sequence context that is no longer running steps.

#### See Also

[SequenceContext](sequencecontext.html)

[SequenceContext.CallingStep](sequencecontext-callingstep.html)

[SequenceContext.CallStackDepth](sequencecontext-callstackdepth.html)

[SequenceContext.Root](sequencecontext-root.html)

[Thread.GetSequenceContext](thread-getsequencecontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-callerdiscardsresults.html language=enus -->
## TOPIC 02515: SequenceContext.CallerDiscardsResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-callerdiscardsresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-callerdiscardsresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.CallerDiscardsResults Data Type Boolean Purpose Returns a value that indicates whether any sequence in the call stack instructs TestStand to disable results or if any calling step higher in the call stack instructs TestStand to not record results. Remarks This property does no

### SequenceContext.CallerDiscardsResults

#### Syntax

[SequenceContext](sequencecontext.html).CallerDiscardsResults

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether any sequence in the call stack instructs TestStand to disable results or if any calling step higher in the call stack instructs TestStand to not record results.

#### Remarks

This property does not consider whether the execution or the engine specified to discard the results. A PostStepResult callback typically uses this property to determine whether the callback processes a step result.

#### See Also

[Execution.DisableResults](execution-disableresults.html)

[StationOptions.DisableResults](stationoptions-disableresults.html)

[Sequence.DisableResults](sequence-disableresults.html)

[Step.ResultRecordingOption](step-resultrecordingoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-callingstep.html language=enus -->
## TOPIC 02516: SequenceContext.CallingStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-callingstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-callingstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.CallingStep Data Type Step Purpose Returns a run-time copy of the Step object for the step that called the current sequence. Remarks This property is valid when the current sequence is called synchronously or asynchronously. This property does not exist in the root SequenceCon

### SequenceContext.CallingStep

#### Syntax

[SequenceContext](sequencecontext.html).CallingStep

#### Data Type

[Step](step.html)

#### Purpose

Returns a run-time copy of the Step object for the step that called the current sequence.

#### Remarks

This property is valid when the current sequence is called synchronously or asynchronously. This property does not exist in the root SequenceContext. Any changes to property values in the returned Step object only modify the execution version of the object.

#### See Also

[SequenceContext.Caller](sequencecontext-caller.html)

[SequenceContext.CallStackDepth](sequencecontext-callstackdepth.html)

[SequenceContext.Root](sequencecontext-root.html)

[Step](step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-callstackdepth.html language=enus -->
## TOPIC 02517: SequenceContext.CallStackDepth

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-callstackdepth.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-callstackdepth.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.CallStackDepth Data Type Long Purpose Returns the zero-based sequence call depth of the sequence context in the current execution. The call depth refers to the number of nested sequences called before reaching the currently executing sequence. The call stack depth of the first

### SequenceContext.CallStackDepth

#### Syntax

[SequenceContext](sequencecontext.html).CallStackDepth

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the zero-based sequence call depth of the sequence context in the current execution. The call depth refers to the number of nested sequences called before reaching the currently executing sequence. The call stack depth of the first sequence an execution calls is zero, and the call stack depth increases with each call to a subsequence.

#### See Also

[SequenceContext.Caller](sequencecontext-caller.html)

[SequenceContext.CallingStep](sequencecontext-callingstep.html)

[SequenceContext.CallStackName](sequencecontext-callstackname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-callstackname.html language=enus -->
## TOPIC 02518: SequenceContext.CallStackName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-callstackname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-callstackname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.CallStackName Data Type String Purpose Returns the name to display in the call stack list for the sequence context. See Also SequenceContext.Caller SequenceContext.CallingStep SequenceContext.CallStackDepth

### SequenceContext.CallStackName

#### Syntax

[SequenceContext](sequencecontext.html).CallStackName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name to display in the call stack list for the sequence context.

#### See Also

[SequenceContext.Caller](sequencecontext-caller.html)

[SequenceContext.CallingStep](sequencecontext-callingstep.html)

[SequenceContext.CallStackDepth](sequencecontext-callstackdepth.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-cantrace.html language=enus -->
## TOPIC 02519: SequenceContext.CanTrace

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-cantrace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-cantrace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.CanTrace Data Type Boolean Purpose Returns a value that indicates whether the SequenceContext can trace. The return value depends on the current values of SequenceContext.Tracing , Execution.TracingDisabled , whether steps in the current sequence are viewable, and all other fa

### SequenceContext.CanTrace

#### Syntax

[SequenceContext](sequencecontext.html).CanTrace

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the SequenceContext can trace. The return value depends on the current values of
 [SequenceContext.Tracing](sequencecontext-tracing.html)
 ,
 [Execution.TracingDisabled](execution-tracingdisabled.html)
 , whether steps in the current sequence are viewable, and all other factors that affect tracing.

#### See Also

[Execution.TracingDisabled](execution-tracingdisabled.html)

[SequenceContext.Tracing](sequencecontext-tracing.html)

[StationOptions.TracingEnabled](stationoptions-tracingenabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-engine.html language=enus -->
## TOPIC 02520: SequenceContext.Engine

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-engine.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-engine.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Engine Data Type Engine Purpose Returns a reference to the Engine object. See Also Engine

### SequenceContext.Engine

#### Syntax

[SequenceContext](sequencecontext.html).Engine

#### Data Type

[Engine](engine.html)

#### Purpose

Returns a reference to the
 [Engine](engine.html)
 object.

#### See Also

[Engine](engine.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-engineasdispatch.html language=enus -->
## TOPIC 02521: SequenceContext.EngineAsDispatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-engineasdispatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-engineasdispatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.EngineAsDispatch Data Type Object Purpose This property is obsolete. Use the SequenceContext.Engine property instead. Remarks Returns a reference to the Engine object. See Also SequenceContext.Engine

### SequenceContext.EngineAsDispatch

#### Syntax

[SequenceContext](sequencecontext.html).EngineAsDispatch

#### Data Type

[Object](data-types-for-teststand.html)

#### Purpose

Note

SequenceContext.Engine

#### Remarks

Returns a reference to the Engine object.

#### See Also

[SequenceContext.Engine](sequencecontext-engine.html)

Parent topic:

Obsolete SequenceContext Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-errorreported.html language=enus -->
## TOPIC 02522: SequenceContext.ErrorReported

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-errorreported.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-errorreported.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.ErrorReported Data Type Boolean Purpose Set this property to True from within a SequenceFilePostStepRuntimeError, ProcessModelPostStepRuntimeError, or StationPostStepRuntimeError callback sequence to prevent TestStand from sending a UIMsg_BreakOnRunTimeError message to the use

### SequenceContext.ErrorReported

#### Syntax

[SequenceContext](sequencecontext.html).ErrorReported

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 from within a SequenceFilePostStepRuntimeError, ProcessModelPostStepRuntimeError, or StationPostStepRuntimeError callback sequence to prevent TestStand from sending a
 [UIMsg_BreakOnRunTimeError](uimessagecodes.html)
 message to the user interface. The
 UIMsg_BreakOnRunTimeError
 message tells the user interface to launch the
 [Run-Time Error](../tsref/run-time-error-dialog-box.html)
 dialog box. By setting this property to
 True
 in the callback, you are telling TestStand that the callback has already handled the run-time error.

#### Remarks

You can set this property from within an expression such as
 RunState.Caller.RunState.ErrorReported = True
 . Also, when you implement the callback, National Instruments recommends that you verify that this property is already
 True
 before continuing because a different run-time error callback might have already handled the error. Outside of run-time error callbacks, this property is always
 False
 , and the value has no meaning. Refer to the
 Overriding SequenceFilePostStepRuntimeError Callback
 example located in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Examples\Modifying Process Models\Overriding Engine Callbacks
 directory for more information about how to use this property.

#### See Also

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[SequenceContext.GetRunTimeErrorMessageEx](sequencecontext-getruntimeerrormessageex.html)

[SequenceContext.SequenceErrorCode](sequencecontext-sequenceerrorcode.html)

[SequenceContext.SequenceErrorMessage](sequencecontext-sequenceerrormessage.html)

[SequenceContext.SequenceErrorOccurred](sequencecontext-sequenceerroroccurred.html)

[SequenceContext.SequenceFailed](sequencecontext-sequencefailed.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-execution.html language=enus -->
## TOPIC 02523: SequenceContext.Execution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-execution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Execution Data Type Execution Purpose Returns a reference to the currently executing execution. See Also Execution Thread.Execution UIMessage.Execution

### SequenceContext.Execution

#### Syntax

[SequenceContext](sequencecontext.html).Execution

#### Data Type

[Execution](execution.html)

#### Purpose

Returns a reference to the currently executing execution.

#### See Also

[Execution](execution.html)

[Thread.Execution](thread-execution.html)

[UIMessage.Execution](uimessage-execution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-fileglobals.html language=enus -->
## TOPIC 02524: SequenceContext.FileGlobals

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-fileglobals.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-fileglobals.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.FileGlobals Data Type PropertyObject Purpose Returns a reference to the object that contains the globals for the currently executing sequence file. Remarks Changes made to the structure or values of properties in globals for the currently executing sequence file do not affect

### SequenceContext.FileGlobals

#### Syntax

[SequenceContext](sequencecontext.html).FileGlobals

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns a reference to the object that contains the globals for the currently executing sequence file.

#### Remarks

Changes made to the structure or values of properties in globals for the currently executing sequence file do not affect the default file globals defined in the sequence file.

#### See Also

[PropertyObject](propertyobject.html)

[SequenceContext.Locals](sequencecontext-locals.html)

[SequenceContext.StationGlobals](sequencecontext-stationglobals.html)

[SequenceFile.FileGlobalsDefaultValues](sequencefile-fileglobalsdefaultvalues.html)

[SequenceFile.FileGlobalsScope](sequencefile-fileglobalsscope.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-getmultiplevalues.html language=enus -->
## TOPIC 02525: SequenceContext.GetMultipleValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-getmultiplevalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-getmultiplevalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.GetMultipleValues( lookupString, elem) Return Value Long Returns 0 if the value of the property element is the same for all steps in the context. If you pass in PropertyObjectElement_Flags for the elem parameter, the return value represents the bits of the PropertyFlags consta

### SequenceContext.GetMultipleValues

#### Syntax

[SequenceContext](sequencecontext.html).GetMultipleValues( lookupString, elem)

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if the value of the property element is the same for all steps in the context. If you pass in
 [PropertyObjectElement_Flags](propertyobjectelements.html)
 for the
 elem
 parameter, the return value represents the bits of the
 [PropertyFlags](propertyflags.html)
 constant. A bit value is
 0
 if the flag value is the same for all steps.

#### Purpose

This method determines if the value of an element of a subproperty of multiple steps, such as the value, comment, format, or flags, represents the shared element value for all the steps in the array. Use this method with a SequenceContext that was created by passing an array of step references to the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method, where the
 [SequenceContext.Step](sequencecontext-step.html)
 property in the context contains the subset of properties all steps contain. This method returns zero if the Step subproperty element specified by
 lookupString
 and
 elem
 parameters has the same value for all steps.

#### Remarks

Use this method and the
 [SequenceContext.SetMultipleValues](sequencecontext-setmultiplevalues.html)
 method if you are writing a sequence editor in which you can select multiple steps. Display
 Multiple Values
 for an element when the value of the step property element is not the same.

You can create a SequenceContext with a Step property that represents multiple steps by calling the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method and passing an array of object references to steps as the first parameter.

#### Parameters

lookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of a subproperty within the SequenceContext you want to obtain the multiple values of. You can also pass
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 to this parameter.

elem
 As
 [PropertyObjectElements](propertyobjectelements.html)

[In] Specifies the element of the subproperty that you want to obtain the multiple values of.

#### See Also

[Engine.NewEditContext](engine-neweditcontext.html)

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[PropertyFlags](propertyflags.html)

[PropertyObjectElements](propertyobjectelements.html)

[SequenceContext.SetMultipleValues](sequencecontext-setmultiplevalues.html)

[SequenceContext.Step](sequencecontext-step.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-getruntimeerrormessageex.html language=enus -->
## TOPIC 02526: SequenceContext.GetRunTimeErrorMessageEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-getruntimeerrormessageex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-getruntimeerrormessageex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.GetRunTimeErrorMessageEx( detailsMsg, errorCodeMsg, locationMsg) Purpose Returns the display strings that contain the run-time error details for the current step the context specifies. Remarks If a run-time error occurs, use this method to obtain the error message display stri

### SequenceContext.GetRunTimeErrorMessageEx

#### Syntax

[SequenceContext](sequencecontext.html).GetRunTimeErrorMessageEx( detailsMsg, errorCodeMsg, locationMsg)

#### Purpose

Returns the display strings that contain the run-time error details for the current step the context specifies.

#### Remarks

If a run-time error occurs, use this method to obtain the error message display strings. Typically, you use this method in a user interface to launch a custom
 [Run-Time Error](../tsref/run-time-error-dialog-box.html)
 dialog box. To obtain a reference to a failing context from an Engine callback, such as the PostStepRunTimeError callback, access the context specified by the lookup string
 "RunState.Caller.ThisContext"
 .

#### Parameters

detailsMsg
 As
 [String](data-types-for-teststand.html)

[Out] Returns a string that describes the specific cause of the error.

errorCodeMsg
 As
 [String](data-types-for-teststand.html)

[Out] Returns a string with the error code number and the general meaning.

locationMsg
 As
 [String](data-types-for-teststand.html)

[Out] Returns a string that describes where the error occurred.

#### See Also

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[SequenceContext.SequenceErrorMessage](sequencecontext-sequenceerrormessage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-getruntimeerrorwinhelpinfo.html language=enus -->
## TOPIC 02527: SequenceContext.GetRunTimeErrorWinHelpInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-getruntimeerrorwinhelpinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-getruntimeerrorwinhelpinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.GetRunTimeErrorWinHelpInfo( helpID, helpFile) Purpose Obtains the help ID and help file for the run-time error. Use the help ID and help file when you call the Engine.DisplayHelpTopic method. Remarks If a run-time error occurs, use this method to obtain the associated help fil

### SequenceContext.GetRunTimeErrorWinHelpInfo

#### Syntax

[SequenceContext](sequencecontext.html).GetRunTimeErrorWinHelpInfo( helpID, helpFile)

#### Purpose

Obtains the help ID and help file for the run-time error. Use the help ID and help file when you call the
 [Engine.DisplayHelpTopic](engine-displayhelptopic.html)
 method.

#### Remarks

If a run-time error occurs, use this method to obtain the associated help file and/or help ID.

Note

#### Parameters

helpID
 As
 [Long](data-types-for-teststand.html)

[Out] Returns a help ID for a topic in a help file to provide context-sensitive help for the object.

helpFile
 As
 [String](data-types-for-teststand.html)

[Out] Returns the help file path.

#### See Also

[Engine.DisplayHelpTopic](engine-displayhelptopic.html)

[SequenceContext.GetRunTimeErrorMessageEx](sequencecontext-getruntimeerrormessageex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-gotocleanup.html language=enus -->
## TOPIC 02528: SequenceContext.GotoCleanup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-gotocleanup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-gotocleanup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.GotoCleanup Data Type Boolean Purpose Specifies the Goto cleanup state of the currently executing sequence. See Also Sequence.FailureAction SequenceContext.SequenceErrorOccurred SequenceContext.SequenceFailed

### SequenceContext.GotoCleanup

#### Syntax

[SequenceContext](sequencecontext.html).GotoCleanup

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies the Goto cleanup state of the currently executing sequence.

#### See Also

[Sequence.FailureAction](sequence-failureaction.html)

[SequenceContext.SequenceErrorOccurred](sequencecontext-sequenceerroroccurred.html)

[SequenceContext.SequenceFailed](sequencecontext-sequencefailed.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-id.html language=enus -->
## TOPIC 02529: SequenceContext.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Id Data Type Long Purpose Returns the unique ID that distinguishes this sequence context from all other sequence contexts. The ID number is never zero. See Also Execution.Id Thread.Id

### SequenceContext.Id

#### Syntax

[SequenceContext](sequencecontext.html).Id

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the unique ID that distinguishes this sequence context from all other sequence contexts.

Note

#### See Also

[Execution.Id](execution-id.html)

[Thread.Id](thread-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-ininteractivemode.html language=enus -->
## TOPIC 02530: SequenceContext.InInteractiveMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-ininteractivemode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-ininteractivemode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.InInteractiveMode Data Type Boolean Purpose Returns True if the sequence context is for an interactive execution. See Also SequenceContext.InteractiveContext SequenceContext.IsInteractiveStep SequenceContext.IsStepExcludedFromExecution

### SequenceContext.InInteractiveMode

#### Syntax

[SequenceContext](sequencecontext.html).InInteractiveMode

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the sequence context is for an interactive execution.

#### See Also

[SequenceContext.InteractiveContext](sequencecontext-interactivecontext.html)

[SequenceContext.IsInteractiveStep](sequencecontext-isinteractivestep.html)

[SequenceContext.IsStepExcludedFromExecution](sequencecontext-isstepexcludedfromexecution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-interactivecontext.html language=enus -->
## TOPIC 02531: SequenceContext.InteractiveContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-interactivecontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-interactivecontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.InteractiveContext Data Type InteractiveContext Purpose If the sequence context is for an interactive execution, this property returns a reference to an InteractiveContext object. Remarks Returns a NULL reference if the sequence context is not for an interactive execution. See

### SequenceContext.InteractiveContext

#### Syntax

[SequenceContext](sequencecontext.html).InteractiveContext

#### Data Type

[InteractiveContext](interactivecontext.html)

#### Purpose

If the sequence context is for an interactive execution, this property returns a reference to an InteractiveContext object.

#### Remarks

Returns a
 NULL
 reference if the sequence context is not for an interactive execution.

#### See Also

[InteractiveContext](interactivecontext.html)

[SequenceContext.InInteractiveMode](sequencecontext-ininteractivemode.html)

[SequenceContext.IsInteractiveStep](sequencecontext-isinteractivestep.html)

[SequenceContext.IsStepExcludedFromExecution](sequencecontext-isstepexcludedfromexecution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-isinteractivestep.html language=enus -->
## TOPIC 02532: SequenceContext.IsInteractiveStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-isinteractivestep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-isinteractivestep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.IsInteractiveStep( stepIndexParam) Return Value Boolean Purpose Returns True if the execution that the sequence context represents is in interactive mode and if the step you specify is selected for interactive execution. Remarks User interfaces dim excluded steps during an int

### SequenceContext.IsInteractiveStep

#### Syntax

[SequenceContext](sequencecontext.html).IsInteractiveStep( stepIndexParam)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the execution that the sequence context represents is in interactive mode and if the step you specify is selected for interactive execution.

#### Remarks

User interfaces dim excluded steps during an interactive execution. The
 [StationOptions.InteractiveBranchMode](stationoptions-interactivebranchmode.html)
 property setting determines if excluded steps execute.

#### Parameters

stepIndexParam
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the step within the current step group.

#### See Also

[SequenceContext.InInteractiveMode](sequencecontext-ininteractivemode.html)

[SequenceContext.IsStepExcludedFromExecution](sequencecontext-isstepexcludedfromexecution.html)

[StationOptions.InteractiveBranchMode](stationoptions-interactivebranchmode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-isprocessmodel.html language=enus -->
## TOPIC 02533: SequenceContext.IsProcessModel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-isprocessmodel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-isprocessmodel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.IsProcessModel Data Type Boolean Purpose Returns True if the sequence that is executing for the sequence context is within a process model sequence file. See Also SequenceContext.ProcessModelClient SequenceContext.Sequence SequenceContext.SequenceFile

### SequenceContext.IsProcessModel

#### Syntax

[SequenceContext](sequencecontext.html).IsProcessModel

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the sequence that is executing for the sequence context is within a process model sequence file.

#### See Also

[SequenceContext.ProcessModelClient](sequencecontext-processmodelclient.html)

[SequenceContext.Sequence](sequencecontext-sequence.html)

[SequenceContext.SequenceFile](sequencecontext-sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-isstepexcludedfromexecution.html language=enus -->
## TOPIC 02534: SequenceContext.IsStepExcludedFromExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-isstepexcludedfromexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-isstepexcludedfromexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.IsStepExcludedFromExecution( step) Return Value Boolean Returns True if the step was not selected as part of the interactive execution or the hierarchical execution in progress. Purpose Specifies whether the step was selected as part of the interactive execution or the hierarc

### SequenceContext.IsStepExcludedFromExecution

#### Syntax

[SequenceContext](sequencecontext.html).IsStepExcludedFromExecution( step)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the step was not selected as part of the interactive execution or the hierarchical execution in progress.

#### Purpose

Specifies whether the step was selected as part of the interactive execution or the hierarchical execution in progress.

#### Remarks

User interfaces dim excluded steps during an interactive execution. The
 [StationOptions.InteractiveBranchMode](stationoptions-interactivebranchmode.html)
 property setting determines if excluded steps execute.

#### Parameters

step
 As
 [Step](step.html)

[In] Specifies the step to verify.

#### See Also

[SequenceContext.InInteractiveMode](sequencecontext-ininteractivemode.html)

[SequenceContext.IsInteractiveStep](sequencecontext-isinteractivestep.html)

[StationOptions.InteractiveBranchMode](stationoptions-interactivebranchmode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-locals.html language=enus -->
## TOPIC 02535: SequenceContext.Locals

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-locals.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-locals.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Locals Data Type PropertyObject Purpose Returns a reference to the object that contains the locals for the currently executing sequence. Remarks Changes made to the structure or values of properties in locals for the currently executing sequence file do not affect the default

### SequenceContext.Locals

#### Syntax

[SequenceContext](sequencecontext.html).Locals

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns a reference to the object that contains the locals for the currently executing sequence.

#### Remarks

Changes made to the structure or values of properties in locals for the currently executing sequence file do not affect the default file locals defined in the sequence file.

#### See Also

[PropertyObject](propertyobject.html)

[Sequence.Locals](sequence-locals.html)

[SequenceContext.FileGlobals](sequencecontext-fileglobals.html)

[SequenceContext.StationGlobals](sequencecontext-stationglobals.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-loopindex.html language=enus -->
## TOPIC 02536: SequenceContext.LoopIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-loopindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-loopindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.LoopIndex Data Type Long Purpose Specifies the value of the loop index at a given point as a step loops. The value of the loop index depends on the looping construct you select for the step. Remarks This property returns the value of the loop index truncated to a 32-bit intege

### SequenceContext.LoopIndex

#### Syntax

[SequenceContext](sequencecontext.html).LoopIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the value of the loop index at a given point as a step loops. The value of the loop index depends on the looping construct you select for the step.

#### Remarks

Note

SequenceContext.AsPropertyObject().GetValNumber("RunState.LoopIndex", 0)

#### See Also

[SequenceContext.LoopNumFailed](sequencecontext-loopnumfailed.html)

[SequenceContext.LoopNumIterations](sequencecontext-loopnumiterations.html)

[SequenceContext.LoopNumPassed](sequencecontext-loopnumpassed.html)

[Step](sequencecontext-step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-loopnumfailed.html language=enus -->
## TOPIC 02537: SequenceContext.LoopNumFailed

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-loopnumfailed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-loopnumfailed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.LoopNumFailed Data Type Long Purpose Specifies the number of failed iterations when a step loops. See Also SequenceContext.LoopIndex SequenceContext.LoopNumIterations SequenceContext.LoopNumPassed SequenceContext.Step

### SequenceContext.LoopNumFailed

#### Syntax

[SequenceContext](sequencecontext.html).LoopNumFailed

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of failed iterations when a step loops.

#### See Also

[SequenceContext.LoopIndex](sequencecontext-loopindex.html)

[SequenceContext.LoopNumIterations](sequencecontext-loopnumiterations.html)

[SequenceContext.LoopNumPassed](sequencecontext-loopnumpassed.html)

[SequenceContext.Step](sequencecontext-step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-loopnumiterations.html language=enus -->
## TOPIC 02538: SequenceContext.LoopNumIterations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-loopnumiterations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-loopnumiterations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.LoopNumIterations Data Type Long Purpose Specifies the number of iterations completed at a given point as a step loops. See Also SequenceContext.LoopIndex SequenceContext.LoopNumFailed SequenceContext.LoopNumPassed

### SequenceContext.LoopNumIterations

#### Syntax

[SequenceContext](sequencecontext.html).LoopNumIterations

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of iterations completed at a given point as a step loops.

#### See Also

[SequenceContext.LoopIndex](sequencecontext-loopindex.html)

[SequenceContext.LoopNumFailed](sequencecontext-loopnumfailed.html)

[SequenceContext.LoopNumPassed](sequencecontext-loopnumpassed.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-loopnumpassed.html language=enus -->
## TOPIC 02539: SequenceContext.LoopNumPassed

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-loopnumpassed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-loopnumpassed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.LoopNumPassed Data Type Long Purpose Specifies the number of passed iterations when a step loops. See Also SequenceContext.LoopIndex SequenceContext.LoopNumFailed SequenceContext.LoopNumIterations SequenceContext.Step

### SequenceContext.LoopNumPassed

#### Syntax

[SequenceContext](sequencecontext.html).LoopNumPassed

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of passed iterations when a step loops.

#### See Also

[SequenceContext.LoopIndex](sequencecontext-loopindex.html)

[SequenceContext.LoopNumFailed](sequencecontext-loopnumfailed.html)

[SequenceContext.LoopNumIterations](sequencecontext-loopnumiterations.html)

[SequenceContext.Step](sequencecontext-step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-main.html language=enus -->
## TOPIC 02540: SequenceContext.Main

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-main.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-main.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Main Data Type SequenceContext Purpose Returns the MainSequence context of the execution with which this sequence context is associated. Remarks If you start an execution using a Process Model entry point, the MainSequence context is the sequence context of the MainSequence in

### SequenceContext.Main

#### Syntax

[SequenceContext](sequencecontext.html).Main

#### Data Type

[SequenceContext](sequencecontext.html)

#### Purpose

Returns the
 MainSequence
 context of the execution with which this sequence context is associated.

#### Remarks

If you start an execution using a Process Model entry point, the
 MainSequence
 context is the sequence context of the
 MainSequence
 in the client sequence file. If you start an execution without using an Execution entry point by executing a sequence or steps directly the
 MainSequence
 context is the same as the root sequence context stored in the
 [SequenceContext.Root](sequencecontext-root.html)
 property.

#### See Also

[SequenceContext](sequencecontext.html)

[SequenceContext.CallStackDepth](sequencecontext-callstackdepth.html)

[SequenceContext.ProcessModelClient](sequencecontext-processmodelclient.html)

[SequenceContext.Root](sequencecontext-root.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-newexecution.html language=enus -->
## TOPIC 02541: SequenceContext.NewExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-newexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-newexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.NewExecution( sequenceFileParam, sequenceNameParam, processModelParam, breakAtFirstStep, synchronous, executionTypeMaskParam, sequenceArgsParam = NULL) Return Value Execution The execution created by this method. Purpose Creates and returns a new Execution object. Remarks When

### SequenceContext.NewExecution

#### Syntax

[SequenceContext](sequencecontext.html).NewExecution( sequenceFileParam, sequenceNameParam, processModelParam, breakAtFirstStep, synchronous, executionTypeMaskParam, sequenceArgsParam = NULL)

#### Return Value

[Execution](execution.html)

The execution created by this method.

#### Purpose

Creates and returns a new
 [Execution](execution.html)
 object.

#### Remarks

When you call this method, the execution begins immediately. This method behaves similar to a Sequence Call step that you configure to run in a new execution

#### Parameters

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the SequenceFile object that contains the sequence to execute. If the execution uses a process model, pass the client SequenceFile object.

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the sequence or Process Model entry point to execute.

processModelParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the process model SequenceFile object if you want to execute a Process Model entry point. Otherwise, a
 NULL
 object reference in LabVIEW,
 0
 in LabWindows/CVI, or the
 Nothing
 keyword in Visual Basic, pass a
 NULL
 dispatch pointer in Microsoft Foundation Classes.

breakAtFirstStep
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to suspend execution before executing the first step.

synchronous
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to force this method to wait until the execution completes.

executionTypeMaskParam
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for the default behavior or pass one or more
 [ExecutionTypeMask](executiontypemask.html)
 constants. Use the bitwise-OR operator to pass multiple constants.

sequenceArgsParam
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a PropertyObject object that contains the arguments to the sequence you want to execute. Each subproperty of the PropertyObject object represents a parameter to the sequence. The subproperties must appear in the same order as the sequence parameters.

This parameter has a default value of
 NULL
 .

#### See Also

[Execution](execution.html)

[ExecutionTypeMask](executiontypemask.html)

[PropertyObject](propertyobject.html)

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-nextstep.html language=enus -->
## TOPIC 02542: SequenceContext.NextStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-nextstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-nextstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.NextStep Data Type Step Purpose Returns a reference to the next step to execute. Remarks Returns a run-time error if no next step exists. See Also SequenceContext.NextStepIndex SequenceContext.PreviousStep SequenceContext.Step Step

### SequenceContext.NextStep

#### Syntax

[SequenceContext](sequencecontext.html).NextStep

#### Data Type

[Step](step.html)

#### Purpose

Returns a reference to the next step to execute.

#### Remarks

Returns a run-time error if no next step exists.

#### See Also

[SequenceContext.NextStepIndex](sequencecontext-nextstepindex.html)

[SequenceContext.PreviousStep](sequencecontext-previousstep.html)

[SequenceContext.Step](sequencecontext-step.html)

[Step](step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-nextstepindex.html language=enus -->
## TOPIC 02543: SequenceContext.NextStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-nextstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-nextstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.NextStepIndex Data Type Long Purpose Specifies the zero-based index of the next step to execute. The index indicates the position of the step in the step group the SequenceContext.StepGroup property identifies. Remarks This property returns -1 if the step group contains no add

### SequenceContext.NextStepIndex

#### Syntax

[SequenceContext](sequencecontext.html).NextStepIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the zero-based index of the next step to execute. The index indicates the position of the step in the step group the
 [SequenceContext.StepGroup](sequencecontext-stepgroup.html)
 property identifies.

#### Remarks

This property returns
 -1
 if the step group contains no additional steps to execute.

#### See Also

[SequenceContext.NextStep](sequencecontext-nextstep.html)

[SequenceContext.PreviousStepIndex](sequencecontext-previousstepindex.html)

[SequenceContext.StepGroup](sequencecontext-stepgroup.html)

[SequenceContext.StepIndex](sequencecontext-stepindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-numstepsexecuted.html language=enus -->
## TOPIC 02544: SequenceContext.NumStepsExecuted

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-numstepsexecuted.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-numstepsexecuted.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.NumStepsExecuted Data Type Long Purpose Specifies the number of steps that have completed execution in the stack frame the context represents.

### SequenceContext.NumStepsExecuted

#### Syntax

[SequenceContext](sequencecontext.html).NumStepsExecuted

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of steps that have completed execution in the stack frame the context represents.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-parameters.html language=enus -->
## TOPIC 02545: SequenceContext.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Parameters Data Type PropertyObject Purpose Returns a reference to the object that contains the parameters for the currently executing sequence. See Also PropertyObject SequenceContext.Caller SequenceContext.CallingStep SequenceContext.Locals

### SequenceContext.Parameters

#### Syntax

[SequenceContext](sequencecontext.html).Parameters

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns a reference to the object that contains the parameters for the currently executing sequence.

#### See Also

[PropertyObject](propertyobject.html)

[SequenceContext.Caller](sequencecontext-caller.html)

[SequenceContext.CallingStep](sequencecontext-callingstep.html)

[SequenceContext.Locals](sequencecontext-locals.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-previousstep.html language=enus -->
## TOPIC 02546: SequenceContext.PreviousStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-previousstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-previousstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.PreviousStep Data Type Step Purpose Returns a reference to the step that executed last. Remarks Returns a run-time error if no previous step exists. See Also SequenceContext.NextStep SequenceContext.PreviousStepIndex SequenceContext.Step Step

### SequenceContext.PreviousStep

#### Syntax

[SequenceContext](sequencecontext.html).PreviousStep

#### Data Type

[Step](step.html)

#### Purpose

Returns a reference to the step that executed last.

#### Remarks

Returns a run-time error if no previous step exists.

#### See Also

[SequenceContext.NextStep](sequencecontext-nextstep.html)

[SequenceContext.PreviousStepIndex](sequencecontext-previousstepindex.html)

[SequenceContext.Step](sequencecontext-step.html)

[Step](step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-previousstepindex.html language=enus -->
## TOPIC 02547: SequenceContext.PreviousStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-previousstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-previousstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.PreviousStepIndex Data Type Long Purpose Specifies the zero-based index of the step that executed last. The index indicates the position of the step in the step group the SequenceContext.StepGroup property identifies. Remarks This property returns -1 if no step executed previo

### SequenceContext.PreviousStepIndex

#### Syntax

[SequenceContext](sequencecontext.html).PreviousStepIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the zero-based index of the step that executed last. The index indicates the position of the step in the step group the
 [SequenceContext.StepGroup](sequencecontext-stepgroup.html)
 property identifies.

#### Remarks

This property returns
 -1
 if no step executed previously.

#### See Also

[SequenceContext.NextStepIndex](sequencecontext-nextstepindex.html)

[SequenceContext.PreviousStep](sequencecontext-previousstep.html)

[SequenceContext.StepGroup](sequencecontext-stepgroup.html)

[SequenceContext.StepIndex](sequencecontext-stepindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-processmodelclient.html language=enus -->
## TOPIC 02548: SequenceContext.ProcessModelClient

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-processmodelclient.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-processmodelclient.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.ProcessModelClient Data Type SequenceFile Purpose Specifies a reference to the client sequence file of a process model execution. See Also SequenceContext.Main SequenceContext.Root SequenceFile

### SequenceContext.ProcessModelClient

#### Syntax

[SequenceContext](sequencecontext.html).ProcessModelClient

#### Data Type

[SequenceFile](sequencefile.html)

#### Purpose

Specifies a reference to the client sequence file of a process model execution.

#### See Also

[SequenceContext.Main](sequencecontext-main.html)

[SequenceContext.Root](sequencecontext-root.html)

[SequenceFile](sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-report.html language=enus -->
## TOPIC 02549: SequenceContext.Report

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-report.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Report Data Type Report Purpose Returns a reference to the current report. See Also Execution.Report Report

### SequenceContext.Report

#### Syntax

[SequenceContext](sequencecontext.html).Report

#### Data Type

[Report](report.html)

#### Purpose

Returns a reference to the current report.

#### See Also

[Execution.Report](execution-report.html)

[Report](report.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-root.html language=enus -->
## TOPIC 02550: SequenceContext.Root

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-root.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-root.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Root Data Type SequenceContext Purpose Returns the root sequence context of the execution with which this sequence context is associated. Remarks The root sequence context is the first sequence context of the execution. See Also SequenceContext SequenceContext.CallStackDepth S

### SequenceContext.Root

#### Syntax

[SequenceContext](sequencecontext.html).Root

#### Data Type

[SequenceContext](sequencecontext.html)

#### Purpose

Returns the root sequence context of the execution with which this sequence context is associated.

#### Remarks

The root sequence context is the first sequence context of the execution.

#### See Also

[SequenceContext](sequencecontext.html)

[SequenceContext.CallStackDepth](sequencecontext-callstackdepth.html)

[SequenceContext.Main](sequencecontext-main.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-runtimeerrormessage.html language=enus -->
## TOPIC 02551: SequenceContext.RunTimeErrorMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-runtimeerrormessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-runtimeerrormessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.RunTimeErrorMessage Data Type String Purpose This property is obsolete. Use the SequenceContext.GetRunTimeErrorMessageEx method instead. Remarks Returns a display string that contains the run-time error message for the current step the context specifies. See Also SequenceConte

### SequenceContext.RunTimeErrorMessage

#### Syntax

[SequenceContext](sequencecontext.html).RunTimeErrorMessage

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

SequenceContext.GetRunTimeErrorMessageEx

#### Remarks

Returns a display string that contains the run-time error message for the current step the context specifies.

#### See Also

[SequenceContext.ErrorReported](sequencecontext-errorreported.html)

[SequenceContext.GetRunTimeErrorMessageEx](sequencecontext-getruntimeerrormessageex.html)

[SequenceContext.SequenceErrorOccurred](sequencecontext-sequenceerroroccurred.html)

Parent topic:

Obsolete SequenceContext Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-selectedexecution.html language=enus -->
## TOPIC 02552: SequenceContext.SelectedExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-selectedexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-selectedexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SelectedExecution Data Type Execution Purpose Returns a reference to the execution, if any, selected when this execution began. Remarks TestStand sets this property only for the root context in an execution. See Also EditArgs Execution SequenceContext.Root SequenceContext.Sele

### SequenceContext.SelectedExecution

#### Syntax

[SequenceContext](sequencecontext.html).SelectedExecution

#### Data Type

[Execution](execution.html)

#### Purpose

Returns a reference to the execution, if any, selected when this execution began.

#### Remarks

TestStand sets this property only for the root context in an execution.

#### See Also

[EditArgs](editargs.html)

[Execution](execution.html)

[SequenceContext.Root](sequencecontext-root.html)

[SequenceContext.SelectedFile](sequencecontext-selectedfile.html)

[SequenceContext.SelectedPropertyObjectFile](sequencecontext-selectedpropertyobjectfile.html)

[SequenceContext.SelectedPropertyObjects](sequencecontext-selectedpropertyobjects.html)

[SequenceContext.SelectedSequences](sequencecontext-selectedsequences.html)

[SequenceContext.SelectedStepGroup](sequencecontext-selectedstepgroup.html)

[SequenceContext.SelectedSteps](sequencecontext-selectedsteps.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-selectedfile.html language=enus -->
## TOPIC 02553: SequenceContext.SelectedFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-selectedfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-selectedfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SelectedFile Data Type SequenceFile Purpose Returns a reference to the selected sequence file, if any, when this execution began. Remarks TestStand sets this property only for the root context in an execution. See Also EditArgs SequenceContext.Root SequenceContext.SelectedExec

### SequenceContext.SelectedFile

#### Syntax

[SequenceContext](sequencecontext.html).SelectedFile

#### Data Type

[SequenceFile](sequencefile.html)

#### Purpose

Returns a reference to the selected sequence file, if any, when this execution began.

#### Remarks

TestStand sets this property only for the root context in an execution.

#### See Also

[EditArgs](editargs.html)

[SequenceContext.Root](sequencecontext-root.html)

[SequenceContext.SelectedExecution](sequencecontext-selectedexecution.html)

[SequenceContext.SelectedPropertyObjectFile](sequencecontext-selectedpropertyobjectfile.html)

[SequenceContext.SelectedPropertyObjects](sequencecontext-selectedpropertyobjects.html)

[SequenceContext.SelectedSequences](sequencecontext-selectedsequences.html)

[SequenceContext.SelectedStepGroup](sequencecontext-selectedstepgroup.html)

[SequenceContext.SelectedSteps](sequencecontext-selectedsteps.html)

[SequenceFile](sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-selectedpropertyobjectfile.html language=enus -->
## TOPIC 02554: SequenceContext.SelectedPropertyObjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-selectedpropertyobjectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-selectedpropertyobjectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SelectedPropertyObjectFile Data Type PropertyObjectFile Purpose Returns the PropertyObjectFile object for the file that was active when the execution started. Remarks When the initially active file is a sequence file, this property is identical to the SequenceContext.SelectedF

### SequenceContext.SelectedPropertyObjectFile

#### Syntax

[SequenceContext](sequencecontext.html).SelectedPropertyObjectFile

#### Data Type

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the PropertyObjectFile object for the file that was active when the execution started.

#### Remarks

When the initially active file is a sequence file, this property is identical to the
 [SequenceContext.SelectedFile](sequencecontext-selectedfile.html)
 property. TestStand sets this property only for the root context in an execution.

#### See Also

[PropertyObjectFile](propertyobjectfile.html)

[SequenceContext.SelectedExecution](sequencecontext-selectedexecution.html)

[SequenceContext.SelectedFile](sequencecontext-selectedfile.html)

[SequenceContext.SelectedPropertyObjects](sequencecontext-selectedpropertyobjects.html)

[SequenceContext.SelectedSequences](sequencecontext-selectedsequences.html)

[SequenceContext.SelectedStepGroup](sequencecontext-selectedstepgroup.html)

[SequenceContext.SelectedSteps](sequencecontext-selectedsteps.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-selectedpropertyobjects.html language=enus -->
## TOPIC 02555: SequenceContext.SelectedPropertyObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-selectedpropertyobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-selectedpropertyobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SelectedPropertyObjects Data Type Variant Purpose Returns an array of references to the selected PropertyObjects, if any, when the execution began. Remarks TestStand sets this property only for the root context in an execution. See Also SequenceContext.SelectedExecution Sequen

### SequenceContext.SelectedPropertyObjects

#### Syntax

[SequenceContext](sequencecontext.html).SelectedPropertyObjects

#### Data Type

[Variant](data-types-for-teststand.html)

#### Purpose

Returns an array of references to the selected PropertyObjects, if any, when the execution began.

#### Remarks

TestStand sets this property only for the root context in an execution.

#### See Also

[SequenceContext.SelectedExecution](sequencecontext-selectedexecution.html)

[SequenceContext.SelectedFile](sequencecontext-selectedfile.html)

[SequenceContext.SelectedPropertyObjectFile](sequencecontext-selectedpropertyobjectfile.html)

[SequenceContext.SelectedSequences](sequencecontext-selectedsequences.html)

[SequenceContext.SelectedStepGroup](sequencecontext-selectedstepgroup.html)

[SequenceContext.SelectedSteps](sequencecontext-selectedsteps.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-selectedsequences.html language=enus -->
## TOPIC 02556: SequenceContext.SelectedSequences

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-selectedsequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-selectedsequences.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SelectedSequences Data Type Variant Purpose Returns an array of references to the selected sequences, if any, when this execution began. Remarks TestStand sets this property only for the root context in an execution. Returns an empty array if no sequences were selected. See Al

### SequenceContext.SelectedSequences

#### Syntax

[SequenceContext](sequencecontext.html).SelectedSequences

#### Data Type

[Variant](data-types-for-teststand.html)

#### Purpose

Returns an array of references to the selected sequences, if any, when this execution began.

#### Remarks

TestStand sets this property only for the root context in an execution.

Returns an empty array if no sequences were selected.

#### See Also

[Sequence](sequence.html)

[SequenceContext.SelectedExecution](sequencecontext-selectedexecution.html)

[SequenceContext.SelectedFile](sequencecontext-selectedfile.html)

[SequenceContext.SelectedPropertyObjectFile](sequencecontext-selectedpropertyobjectfile.html)

[SequenceContext.SelectedPropertyObjects](sequencecontext-selectedpropertyobjects.html)

[SequenceContext.SelectedStepGroup](sequencecontext-selectedstepgroup.html)

[SequenceContext.SelectedSteps](sequencecontext-selectedsteps.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-selectedstepgroup.html language=enus -->
## TOPIC 02557: SequenceContext.SelectedStepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-selectedstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-selectedstepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SelectedStepGroup Data Type StepGroups Use the following constants with this data type: StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step group. Purpose

### SequenceContext.SelectedStepGroup

#### Syntax

[SequenceContext](sequencecontext.html).SelectedStepGroup

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

Specifies the index of the step group selected when the execution started.

#### Remarks

TestStand sets this property only for the root context in an execution.

#### See Also

[SequenceContext.SelectedExecution](sequencecontext-selectedexecution.html)

[SequenceContext.SelectedFile](sequencecontext-selectedfile.html)

[SequenceContext.SelectedPropertyObjectFile](sequencecontext-selectedpropertyobjectfile.html)

[SequenceContext.SelectedPropertyObjects](sequencecontext-selectedpropertyobjects.html)

[SequenceContext.SelectedSequences](sequencecontext-selectedsequences.html)

[SequenceContext.SelectedSteps](sequencecontext-selectedsteps.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-selectedsteps.html language=enus -->
## TOPIC 02558: SequenceContext.SelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-selectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-selectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SelectedSteps Data Type Variant Purpose Returns an array of references to the selected steps, if any, when this execution began. Remarks Returns an empty array if no steps were selected. TestStand sets this property only for the root context in an execution. See Also SequenceC

### SequenceContext.SelectedSteps

#### Syntax

[SequenceContext](sequencecontext.html).SelectedSteps

#### Data Type

[Variant](data-types-for-teststand.html)

#### Purpose

Returns an array of references to the selected steps, if any, when this execution began.

#### Remarks

Returns an empty array if no steps were selected. TestStand sets this property only for the root context in an execution.

#### See Also

[SequenceContext.SelectedExecution](sequencecontext-selectedexecution.html)

[SequenceContext.SelectedFile](sequencecontext-selectedfile.html)

[SequenceContext.SelectedPropertyObjectFile](sequencecontext-selectedpropertyobjectfile.html)

[SequenceContext.SelectedPropertyObjects](sequencecontext-selectedpropertyobjects.html)

[SequenceContext.SelectedSequences](sequencecontext-selectedsequences.html)

[SequenceContext.SelectedStepGroup](sequencecontext-selectedstepgroup.html)

[Step](step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-sequence.html language=enus -->
## TOPIC 02559: SequenceContext.Sequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-sequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Sequence Data Type Sequence Purpose Returns a reference to the run-time copy of the currently executing sequence. See Also Sequence SequenceContext.SequenceFile

### SequenceContext.Sequence

#### Syntax

[SequenceContext](sequencecontext.html).Sequence

#### Data Type

[Sequence](sequence.html)

#### Purpose

Returns a reference to the run-time copy of the currently executing sequence.

#### See Also

[Sequence](sequence.html)

[SequenceContext.SequenceFile](sequencecontext-sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-sequenceerrorcode.html language=enus -->
## TOPIC 02560: SequenceContext.SequenceErrorCode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-sequenceerrorcode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-sequenceerrorcode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SequenceErrorCode Data Type Long Purpose Reports the sequence error code to the step that calls the sequence. See Also SequenceContext.ErrorReported SequenceContext.SequenceErrorMessage SequenceContext.SequenceErrorOccurred

### SequenceContext.SequenceErrorCode

#### Syntax

[SequenceContext](sequencecontext.html).SequenceErrorCode

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Reports the sequence error code to the step that calls the sequence.

#### See Also

[SequenceContext.ErrorReported](sequencecontext-errorreported.html)

[SequenceContext.SequenceErrorMessage](sequencecontext-sequenceerrormessage.html)

[SequenceContext.SequenceErrorOccurred](sequencecontext-sequenceerroroccurred.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-sequenceerrormessage.html language=enus -->
## TOPIC 02561: SequenceContext.SequenceErrorMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-sequenceerrormessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-sequenceerrormessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SequenceErrorMessage Data Type String Purpose Reports the sequence error message to the step that calls the sequence. See Also SequenceContext.ErrorReported SequenceContext.SequenceErrorCode SequenceContext.SequenceErrorOccurred

### SequenceContext.SequenceErrorMessage

#### Syntax

[SequenceContext](sequencecontext.html).SequenceErrorMessage

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Reports the sequence error message to the step that calls the sequence.

#### See Also

[SequenceContext.ErrorReported](sequencecontext-errorreported.html)

[SequenceContext.SequenceErrorCode](sequencecontext-sequenceerrorcode.html)

[SequenceContext.SequenceErrorOccurred](sequencecontext-sequenceerroroccurred.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-sequenceerroroccurred.html language=enus -->
## TOPIC 02562: SequenceContext.SequenceErrorOccurred

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-sequenceerroroccurred.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-sequenceerroroccurred.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SequenceErrorOccurred Data Type Boolean Purpose Reports the sequence error occurred flag to the step that calls the sequence. See Also SequenceContext.ErrorReported SequenceContext.SequenceErrorCode SequenceContext.SequenceErrorMessage

### SequenceContext.SequenceErrorOccurred

#### Syntax

[SequenceContext](sequencecontext.html).SequenceErrorOccurred

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Reports the sequence error occurred flag to the step that calls the sequence.

#### See Also

[SequenceContext.ErrorReported](sequencecontext-errorreported.html)

[SequenceContext.SequenceErrorCode](sequencecontext-sequenceerrorcode.html)

[SequenceContext.SequenceErrorMessage](sequencecontext-sequenceerrormessage.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-sequencefailed.html language=enus -->
## TOPIC 02563: SequenceContext.SequenceFailed

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-sequencefailed.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-sequencefailed.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SequenceFailed Data Type Boolean Purpose Specifies the failure state of the currently executing sequence. Remarks Setting this property to True does not cause the currently executing sequence to go to the Cleanup step group when the Sequence.FailureAction property or StationOp

### SequenceContext.SequenceFailed

#### Syntax

[SequenceContext](sequencecontext.html).SequenceFailed

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies the failure state of the currently executing sequence.

#### Remarks

Setting this property to
 True
 does not cause the currently executing sequence to go to the Cleanup step group when the
 [Sequence.FailureAction](sequence-failureaction.html)
 property or
 [StationOptions.AlwaysGotoCleanupOnFailure](stationoptions-alwaysgotocleanuponfailure.html)
 property are
 True
 . Set the
 [SequenceContext.GotoCleanup](sequencecontext-gotocleanup.html)
 property to
 True
 to force a sequence to go to the Cleanup step group.

#### See Also

[Sequence.FailureAction](sequence-failureaction.html)

[SequenceContext.GotoCleanup](sequencecontext-gotocleanup.html)

[SequenceContext.SequenceErrorOccurred](sequencecontext-sequenceerroroccurred.html)

[StationOptions.AlwaysGotoCleanupOnFailure](stationoptions-alwaysgotocleanuponfailure.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-sequencefile.html language=enus -->
## TOPIC 02564: SequenceContext.SequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-sequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-sequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SequenceFile Data Type SequenceFile Purpose Returns a reference to the sequence file of the currently executing sequence. See Also SequenceContext.Sequence SequenceFile

### SequenceContext.SequenceFile

#### Syntax

[SequenceContext](sequencecontext.html).SequenceFile

#### Data Type

[SequenceFile](sequencefile.html)

#### Purpose

Returns a reference to the sequence file of the currently executing sequence.

#### See Also

[SequenceContext.Sequence](sequencecontext-sequence.html)

[SequenceFile](sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-sequenceindex.html language=enus -->
## TOPIC 02565: SequenceContext.SequenceIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-sequenceindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-sequenceindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SequenceIndex Data Type Long Purpose Returns the zero-based index of the currently executing sequence in the sequence file. See Also SequenceContext.Sequence SequenceContext.SequenceFile

### SequenceContext.SequenceIndex

#### Syntax

[SequenceContext](sequencecontext.html).SequenceIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the zero-based index of the currently executing sequence in the sequence file.

#### See Also

[SequenceContext.Sequence](sequencecontext-sequence.html)

[SequenceContext.SequenceFile](sequencecontext-sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-setmultiplevalues.html language=enus -->
## TOPIC 02566: SequenceContext.SetMultipleValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-setmultiplevalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-setmultiplevalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.SetMultipleValues( lookupString, elem, multipleValues) Purpose Use this method to update the multiple value state for property elements under SequenceContext.Step in a context that Engine.NewEditContext created. You create a SequenceContext that represents multiple steps by pa

### SequenceContext.SetMultipleValues

#### Syntax

[SequenceContext](sequencecontext.html).SetMultipleValues( lookupString, elem, multipleValues)

#### Purpose

Use this method to update the multiple value state for property elements under
 [SequenceContext.Step](sequencecontext-step.html)
 in a context that
 [Engine.NewEditContext](engine-neweditcontext.html)
 created. You create a SequenceContext that represents multiple steps by passing an array of object references to steps as the first parameter. When you set the value of a property element of the steps the context represents, you must use this method to update the context so that
 [SequenceContext.GetMultipleValues](sequencecontext-getmultiplevalues.html)
 returns correct values.

#### Remarks

Use this method if you are writing a sequence editor in which you can select multiple steps and the editor displays
 Multiple Values
 for step property elements.

Calling this method does not update any object in the sequence context or any object you used to create the sequence context.

#### Parameters

lookupString
 As
 [String](data-types-for-teststand.html)

[In] Pass the name of a subproperty within the SequenceContext you want to set the multiple values of. You can also pass
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 to this parameter.

elem
 As
 [PropertyObjectElements](propertyobjectelements.html)

[In] Specifies the element of the subproperty that you want to set the multiple value state of.

multipleValues
 As
 [Long](data-types-for-teststand.html)

[In] For the
 [PropertyObjectElement_Flags](propertyobjectelements.html)
 element of a subproperty, specify the bits of the
 [PropertyFlags](propertyflags.html)
 constant where each bit is zero if the corresponding flags have the same value. For all other elements, pass
 0
 if the element contains the same value and
 1
 if the element contains multiple values.

#### See Also

[Engine.NewEditContext](engine-neweditcontext.html)

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[PropertyFlags](propertyflags.html)

[PropertyObjectElements](propertyobjectelements.html)

[SequenceContext.GetMultipleValues](sequencecontext-getmultiplevalues.html)

[SequenceContext.Step](sequencecontext-step.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-stationglobals.html language=enus -->
## TOPIC 02567: SequenceContext.StationGlobals

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-stationglobals.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-stationglobals.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.StationGlobals Data Type PropertyObject Purpose Returns a reference to the object that contains the globals for the current installation of TestStand. Remarks You can use this property to store temporary station globals. Updating temporary station globals does not update the s

### SequenceContext.StationGlobals

#### Syntax

[SequenceContext](sequencecontext.html).StationGlobals

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns a reference to the object that contains the globals for the current installation of TestStand.

#### Remarks

You can use this property to store temporary station globals. Updating temporary station globals does not update the station globals file.

#### See Also

[Engine.Globals](engine-globals.html)

[PropertyObject](propertyobject.html)

[SequenceContext.FileGlobals](sequencecontext-fileglobals.html)

[SequenceContext.Locals](sequencecontext-locals.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-step.html language=enus -->
## TOPIC 02568: SequenceContext.Step

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Step Data Type Step Purpose Returns a reference to the currently executing step. Remarks Returns a run-time error if the execution is currently suspended at a breakpoint. See Also SequenceContext.NextStep SequenceContext.PreviousStep SequenceContext.StepIndex Step

### SequenceContext.Step

#### Syntax

[SequenceContext](sequencecontext.html).Step

#### Data Type

[Step](step.html)

#### Purpose

Returns a reference to the currently executing step.

#### Remarks

Returns a run-time error if the execution is currently suspended at a breakpoint.

#### See Also

[SequenceContext.NextStep](sequencecontext-nextstep.html)

[SequenceContext.PreviousStep](sequencecontext-previousstep.html)

[SequenceContext.StepIndex](sequencecontext-stepindex.html)

[Step](step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-stepgroup.html language=enus -->
## TOPIC 02569: SequenceContext.StepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-stepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.StepGroup Data Type StepGroups Use the following constants with this data type: StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step group. Purpose Specifi

### SequenceContext.StepGroup

#### Syntax

[SequenceContext](sequencecontext.html).StepGroup

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

Specifies the step group of the currently executing step.

#### See Also

[SequenceContext.SelectedStepGroup](sequencecontext-selectedstepgroup.html)

[SequenceContext.Sequence](sequencecontext-sequence.html)

[SequenceContext.Step](sequencecontext-step.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-stepgroupstartedinteractiveex.html language=enus -->
## TOPIC 02570: SequenceContext.StepGroupStartedInteractiveExe

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-stepgroupstartedinteractiveex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-stepgroupstartedinteractiveex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.StepGroupStartedInteractiveExe Data Type Boolean Purpose Returns True if the current step group is the one in which an interactive execution was started and this is the sequence context for that execution. See Also SequenceContext.InInteractiveMode

### SequenceContext.StepGroupStartedInteractiveExe

#### Syntax

[SequenceContext](sequencecontext.html).StepGroupStartedInteractiveExe

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the current step group is the one in which an interactive execution was started and this is the sequence context for that execution.

#### See Also

[SequenceContext.InInteractiveMode](sequencecontext-ininteractivemode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-stepindex.html language=enus -->
## TOPIC 02571: SequenceContext.StepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-stepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-stepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.StepIndex Data Type Long Purpose Specifies the zero-based index of the currently executing step. The index indicates the position of the step in the step group the SequenceContext.StepGroup property identifies. If execution is suspended between steps, this property returns -1

### SequenceContext.StepIndex

#### Syntax

[SequenceContext](sequencecontext.html).StepIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the zero-based index of the currently executing step. The index indicates the position of the step in the step group the
 [SequenceContext.StepGroup](sequencecontext-stepgroup.html)
 property identifies. If execution is suspended between steps, this property returns
 -1
 .

#### See Also

[SequenceContext.SequenceIndex](sequencecontext-sequenceindex.html)

[SequenceContext.Step](sequencecontext-step.html)

[SequenceContext.StepGroup](sequencecontext-stepgroup.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-thread.html language=enus -->
## TOPIC 02572: SequenceContext.Thread

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-thread.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-thread.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Thread Data Type Thread Purpose Returns a reference to the currently executing thread. See Also SequenceContext.Execution Thread

### SequenceContext.Thread

#### Syntax

[SequenceContext](sequencecontext.html).Thread

#### Data Type

[Thread](thread.html)

#### Purpose

Returns a reference to the currently executing thread.

#### See Also

[SequenceContext.Execution](sequencecontext-execution.html)

[Thread](thread.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext-tracing.html language=enus -->
## TOPIC 02573: SequenceContext.Tracing

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext-tracing.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext-tracing.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceContext.Tracing Data Type Boolean Purpose Specifies whether to trace the execution of steps to which this sequence context applies. See Also Execution.TracingDisabled SequenceContext.CanTrace StationOptions.TracingEnabled

### SequenceContext.Tracing

#### Syntax

[SequenceContext](sequencecontext.html).Tracing

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to trace the execution of steps to which this sequence context applies.

#### See Also

[Execution.TracingDisabled](execution-tracingdisabled.html)

[SequenceContext.CanTrace](sequencecontext-cantrace.html)

[StationOptions.TracingEnabled](stationoptions-tracingenabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontext.html language=enus -->
## TOPIC 02574: SequenceContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A SequenceContext object contains complete information about an execution at a particular point during the execution. You can use the sequence context to access all the objects, variables, and properties in the execution. From the sequence context, you also can obtain references to all the steps in

### SequenceContext

A SequenceContext object contains complete information about an execution at a particular point during the execution. You can use the sequence context to access all the objects, variables, and properties in the execution. From the sequence context, you also can obtain references to all the steps in the current sequence, the sequence contexts for the calling sequences, the Process Model entry point sequence, and the
 MainSequence
 in the client sequence file. You can pass the current sequence context or subproperties to code modules you call from steps.

#### Properties

| ApplicationIsEditor (Read Only) |
| --- |
| Caller (Read Only) |
| CallerDiscardsResults (Read Only) |
| CallingStep (Read Only) |
| CallStackDepth (Read Only) |
| CallStackName (Read Only) |
| CanTrace (Read Only) |
| Engine (Read Only) |
| ErrorReported |
| Execution (Read Only) |
| FileGlobals (Read Only) |
| GotoCleanup |
| Id (Read Only) |
| InInteractiveMode (Read Only) |
| InteractiveContext (Read Only) |
| IsProcessModel (Read Only) |
| Locals (Read Only) |
| LoopIndex |
| LoopNumFailed |
| LoopNumIterations |
| LoopNumPassed |
| Main (Read Only) |
| NextStep (Read Only) |
| NextStepIndex |
| NumStepsExecuted |
| Parameters (Read Only) |
| PreviousStep (Read Only) |
| PreviousStepIndex |
| ProcessModelClient |
| Report (Read Only) |
| Root (Read Only) |
| SelectedExecution (Read Only) |
| SelectedFile (Read Only) |
| SelectedPropertyObjectFile (Read Only) |
| SelectedPropertyObjects (Read Only) |
| SelectedSequences (Read Only) |
| SelectedStepGroup |
| SelectedSteps (Read Only) |
| Sequence (Read Only) |
| SequenceErrorCode |
| SequenceErrorMessage |
| SequenceErrorOccurred |
| SequenceFailed |
| SequenceFile (Read Only) |
| SequenceIndex (Read Only) |
| StationGlobals |
| Step (Read Only) |
| StepGroup |
| StepGroupStartedInteractiveExe (Read Only) |
| StepIndex |
| Thread (Read Only) |
| Tracing |

#### Methods

| AsPropertyObject |
| --- |
| GetMultipleValues |
| GetRunTimeErrorMessageEx |
| GetRunTimeErrorWinHelpInfo |
| IsInteractiveStep |
| IsStepExcludedFromExecution |
| NewExecution |
| SetMultipleValues |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecontextproperties.html language=enus -->
## TOPIC 02575: SequenceContextProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecontextproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecontextproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to create lookup strings to access some of the commonly used and built-in properties of a sequence context using the PropertyObject class. RunState_LoopIndex –(Value: "LoopIndex") RunState_LoopNumFailed –(Value: "LoopNumFailed") RunState_LoopNumPassed –(Value: "LoopNumPassed") Ru

### SequenceContextProperties

Use these constants to create
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 to access some of the commonly used and built-in properties of a sequence context using the PropertyObject class.

- RunState_LoopIndex 
 –(Value: "LoopIndex")
- RunState_LoopNumFailed 
 –(Value: "LoopNumFailed")
- RunState_LoopNumPassed 
 –(Value: "LoopNumPassed")
- RunState_SeqFileProp 
 –(Value: "SequenceFile")
- RunState_SeqProp 
 –(Value: "Sequence")
- RunState_StepProp 
 –(Value: "Step")
- SeqContext_RunStateProp 
 –(Value: "RunState")

#### See Also

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[SequenceContext](sequencecontext.html)

[SequenceContext.AsPropertyObject](sequencecontext-aspropertyobject.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencedefaultvaluescopes.html language=enus -->
## TOPIC 02576: SequenceDefaultValueScopes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencedefaultvaluescopes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencedefaultvaluescopes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Execution.GetSequenceDefaultValues , Execution.SetSequenceDefaultValues , and Execution.ClearSequenceDefaultValues methods to specify whether the method operates on the list of default value sequences for the execution or hierarchy of executions with which the execution

### SequenceDefaultValueScopes

Use these constants with the
 [Execution.GetSequenceDefaultValues](execution-getsequencedefaultvalues.html)
 ,
 [Execution.SetSequenceDefaultValues](execution-setsequencedefaultvalues.html)
 , and
 [Execution.ClearSequenceDefaultValues](execution-clearsequencedefaultvalues.html)
 methods to specify whether the method operates on the list of default value sequences for the execution or hierarchy of executions with which the execution is associated.

You can associate default value sequences with either a specific execution or the hierarchy of executions with which this execution is associated. For example, setting a default value sequence on the hierarchy of executions associated with a Batch model applies the default value sequence to the controlling batch execution and all test socket executions. If an execution and the execution hierarchy both specify a default value sequence, TestStand uses the default value sequence the execution specifies.

- SeqDefValueScope_Execution 
 –(Value: 1) Specifies to operate on the list of default value sequences for the execution.
- SeqDefValueScope_ExecutionTree 
 –(Value: 2) Specifies to operate on the list of default value sequences for the hierarchy of executions with which the execution is associated.

#### See Also

[Execution.ClearSequenceDefaultValues](execution-clearsequencedefaultvalues.html)

[Execution.GetSequenceDefaultValues](execution-getsequencedefaultvalues.html)

[Execution.SetSequenceDefaultValues](execution-setsequencedefaultvalues.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-addloadreference.html language=enus -->
## TOPIC 02577: SequenceFile.AddLoadReference

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-addloadreference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-addloadreference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.AddLoadReference Purpose Adds a load reference that keeps the file in the internal cache of the engine. Remarks Call this method to add an additional load reference to the sequence file. TestStand uses the load reference count to determine when to unload the sequence file from th

### SequenceFile.AddLoadReference

#### Syntax

[SequenceFile](sequencefile.html).AddLoadReference

#### Purpose

Adds a load reference that keeps the file in the internal cache of the engine.

#### Remarks

Call this method to add an additional load reference to the sequence file. TestStand uses the load reference count to determine when to unload the sequence file from the internal cache of the engine. In addition to this method, the
 [Engine.GetSequenceFileEx](engine-getsequencefileex.html)
 and
 [Engine.NewSequenceFile](engine-newsequencefile.html)
 methods also add a load reference to the sequence file. The
 [Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)
 method removes a load reference.

You must call the
 Engine.ReleaseSequenceFileEx
 method for each load reference you add to the sequence file. When you release the last load reference, TestStand unloads the file from the internal cache of the engine, TestStand executes the SequenceFileUnload callback sequence, if applicable.

This method generates an error if the sequence file does not have any load references initially.

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.NewSequenceFile](engine-newsequencefile.html)

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-aspropertyobject.html language=enus -->
## TOPIC 02578: SequenceFile.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the SequenceFile object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### SequenceFile.AsPropertyObject

#### Syntax

[SequenceFile](sequencefile.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the SequenceFile object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-aspropertyobjectfile.html language=enus -->
## TOPIC 02579: SequenceFile.AsPropertyObjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-aspropertyobjectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-aspropertyobjectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.AsPropertyObjectFile Return Value PropertyObjectFile Purpose Returns the underlying PropertyObjectFile that represents the SequenceFile object. See Also PropertyObjectFile

### SequenceFile.AsPropertyObjectFile

#### Syntax

[SequenceFile](sequencefile.html).AsPropertyObjectFile

#### Return Value

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Returns the underlying PropertyObjectFile that represents the SequenceFile object.

#### See Also

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-batchsyncoption.html language=enus -->
## TOPIC 02580: SequenceFile.BatchSyncOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-batchsyncoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-batchsyncoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.BatchSyncOption Data Type SeqFileBatchSynchronizationOptions Use the following constants with this data type: SeqFileBatchSyncOption_NoSync –(Value: 2) Batch synchronization is not used on this step. SeqFileBatchSyncOption_OneThreadOnly –(Value: 5) Use a One Thread Only section t

### SequenceFile.BatchSyncOption

#### Syntax

[SequenceFile](sequencefile.html).BatchSyncOption

#### Data Type

[SeqFileBatchSynchronizationOptions](seqfilebatchsynchronizationoptions.html)

Use the following constants with this data type:

- SeqFileBatchSyncOption_NoSync 
 –(Value: 2) Batch synchronization is not used on this step.
- SeqFileBatchSyncOption_OneThreadOnly 
 –(Value: 5) Use a One Thread Only section to specify that only one thread in the batch executes the step in the section. Typically, you use this type of section to perform an operation that applies to the batch as a whole, such as raising the temperature in a test chamber. When all threads in a batch arrive at their respective instances of an Enter step for a One Thread Only section, TestStand releases only the thread with the lowest Order Number. When that thread arrives at Exit step for the section, all remaining threads in the batch jump from the Enter step to the Exit step, skipping the steps within the section. The threads in the batch then exit the section together.
- SeqFileBatchSyncOption_Parallel 
 –(Value: 4) When all threads in a batch arrive at their respective instances of an Enter step for a Parallel section, TestStand releases all the threads at once. Each thread waits at the Exit step for the section until all threads in the batch reach that step.
- SeqFileBatchSyncOption_Serial 
 –(Value: 3) Use a Serial section to ensure that each thread in the batch executes the steps in the section sequentially and in the order you specify when you create the batch. When all threads in a batch arrive at their respective instances of an Enter step for a Serial section, TestStand releases one thread at a time in ascending order according to the order number you assign to the threads when you add them to the batch using the Batch Specification step. As each thread reaches the Exit step for the section, the next thread in the batch proceeds from the Enter step. After all the threads in the batch arrive at the Exit step, they exit the section together.
- SeqFileBatchSyncOption_UseModelSetting 
 –(Value: 1) Uses the same option the model uses.

#### Purpose

Specifies the batch synchronization operation corresponding to all the steps contained in the sequence file when the synchronization setting is
 BatchSyncOption_UseSeqFileSetting
 .

#### See Also

[BatchSynchronizationOptions](batchsynchronizationoptions.html)

[Step.BatchSyncOption](step-batchsyncoption.html)

[StepType.BatchSyncOption](steptype-batchsyncoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-canunload.html language=enus -->
## TOPIC 02581: SequenceFile.CanUnload

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-canunload.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-canunload.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.CanUnload Data Type Boolean Purpose Returns a value that indicates whether the sequence file can be removed from the internal cache of the engine. Remarks The engine cannot unload a sequence file from the internal cache if multiple load references to it exist or if it is currentl

### SequenceFile.CanUnload

#### Syntax

[SequenceFile](sequencefile.html).CanUnload

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the sequence file can be removed from the internal cache of the engine.

#### Remarks

The engine cannot unload a sequence file from the internal cache if multiple load references to it exist or if it is currently executing. Use this method to determine whether calling the
 [Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)
 method would remove the file from the internal cache and return
 True
 .

Note

True

Engine.ReleaseSequenceFileEx

False

Engine.ReleaseSequenceFileEx

#### See Also

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[SequenceFile.IsExecuting](sequencefile-isexecuting.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-changecount.html language=enus -->
## TOPIC 02582: SequenceFile.ChangeCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-changecount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-changecount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.ChangeCount Data Type Long Purpose Returns the number of modifications that have been made to the sequence file since it was loaded into memory. Remarks The sequence editor and user interfaces use this count to determine when to refresh sequence displays and when to indicate to t

### SequenceFile.ChangeCount

#### Syntax

[SequenceFile](sequencefile.html).ChangeCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of modifications that have been made to the sequence file since it was loaded into memory.

#### Remarks

The sequence editor and user interfaces use this count to determine when to refresh sequence displays and when to indicate to the user that a sequence file has been modified.

This property returns the same value as the
 [PropertyObjectFile.ChangeCount](propertyobjectfile-changecount.html)
 property.

#### See Also

[PropertyObjectFile.ChangeCount](propertyobjectfile-changecount.html)

[PropertyObjectFile.IncChangeCount](propertyobjectfile-incchangecount.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-createcallbackoverridesequence.html language=enus -->
## TOPIC 02583: SequenceFile.CreateCallbackOverrideSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-createcallbackoverridesequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-createcallbackoverridesequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.CreateCallbackOverrideSequence( callbackName, allowCopyDefaultSteps) Return Value Sequence Specifies a reference to the callback the method creates. Release this reference when you are finished with it. Purpose Use this method to create a callback sequence in the sequence file. T

### SequenceFile.CreateCallbackOverrideSequence

#### Syntax

[SequenceFile](sequencefile.html).CreateCallbackOverrideSequence( callbackName, allowCopyDefaultSteps)

#### Return Value

[Sequence](sequence.html)

Specifies a reference to the callback the method creates. Release this reference when you are finished with it.

#### Purpose

Use this method to create a
 [callback sequence](/csh?context=ts_tsfundamentals_customize_process_models_callbacks)
 in the sequence file. The callback sequence you create overrides the Model, Engine, or Front-End callback of the same name as the callback you create.

#### Parameters

callbackName
 As
 [String](data-types-for-teststand.html)

[In] The name of the callback sequence to override. Specify the sequence name of a Model, Engine, or Front-End callback. Refer to
 [DefaultModelCallbacks](defaultmodelcallbacks.html)
 and
 [SeqFileCallbacks](seqfilecallbacks.html)
 constants for possible values for this parameter.

allowCopyDefaultSteps
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to copy the steps of the sequence you are overriding into the new sequence.

#### See Also

[DefaultModelCallbacks](defaultmodelcallbacks.html)

[SeqFileCallbacks](seqfilecallbacks.html)

[Sequence](sequence.html)

[SequenceFile.GetModelCallbackNames](sequencefile-getmodelcallbacknames.html)

[SequenceFile.GetReservedCallbackNames](sequencefile-getreservedcallbacknames.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-deletesequence.html language=enus -->
## TOPIC 02584: SequenceFile.DeleteSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-deletesequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-deletesequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.DeleteSequence( index) Purpose Deletes the specified sequence from the sequence file. Parameters index As Long [In] Specifies a zero-based index to indicate the sequence to delete. See Also SequenceFile.InsertSequenceEx SequenceFile.NumSequences SequenceFile.RemoveSequence

### SequenceFile.DeleteSequence

#### Syntax

[SequenceFile](sequencefile.html).DeleteSequence( index)

#### Purpose

Deletes the specified sequence from the sequence file.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index to indicate the sequence to delete.

#### See Also

[SequenceFile.InsertSequenceEx](sequencefile-insertsequenceex.html)

[SequenceFile.NumSequences](sequencefile-numsequences.html)

[SequenceFile.RemoveSequence](sequencefile-removesequence.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-fileglobalsdefaultvalues.html language=enus -->
## TOPIC 02585: SequenceFile.FileGlobalsDefaultValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-fileglobalsdefaultvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-fileglobalsdefaultvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.FileGlobalsDefaultValues Data Type PropertyObject Purpose Returns the PropertyObject that contains the default values of the global variables for the sequence file. See Also PropertyObject SequenceContext.FileGlobals SequenceFile.FileGlobalsScope

### SequenceFile.FileGlobalsDefaultValues

#### Syntax

[SequenceFile](sequencefile.html).FileGlobalsDefaultValues

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the PropertyObject that contains the default values of the global variables for the sequence file.

#### See Also

[PropertyObject](propertyobject.html)

[SequenceContext.FileGlobals](sequencecontext-fileglobals.html)

[SequenceFile.FileGlobalsScope](sequencefile-fileglobalsscope.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-fileglobalsscope.html language=enus -->
## TOPIC 02586: SequenceFile.FileGlobalsScope

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-fileglobalsscope.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-fileglobalsscope.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.FileGlobalsScope Data Type FileGlobalsScopeOptions Use the following constants with this data type: FileGlobalsScopeOption_AllExecutionsShare –(Value: 1) Specifies that the first execution that runs the sequence file creates a run-time copy of the global variables and initializes

### SequenceFile.FileGlobalsScope

#### Syntax

[SequenceFile](sequencefile.html).FileGlobalsScope

#### Data Type

[FileGlobalsScopeOptions](fileglobalsscopeoptions.html)

Use the following constants with this data type:

- FileGlobalsScopeOption_AllExecutionsShare 
 –(Value: 1) Specifies that the first execution that runs the sequence file creates a run-time copy of the global variables and initializes the variables to the default values. Any other execution that runs the sequence file concurrently uses the same global variables. When the last execution that uses the sequence file global variables completes, TestStand discards the file global variables. A common use case for selecting this option might be when you want to share variables among multiple executions you start with the Batch or Parallel process model.
- FileGlobalsScopeOption_SeparateForEachExecution 
 –(Value: 0) Specifies that each execution that runs the sequence file creates a separate run-time copy of the global variables and initializes the variables to the default values. Threads within an execution share the run-time copy of the variables for the execution.

#### Purpose

Specifies the lifetime of the sequence file global variables and whether multiple executions share the sequence file global variable values.

#### Remarks

If a sequence file unloads from memory and an execution later reloads the sequence file, the execution creates a new run-time copy of the file global variables and initializes the variables to the default values.

#### See Also

[SequenceContext.FileGlobals](sequencecontext-fileglobals.html)

[SequenceFile.FileGlobalsDefaultValues](sequencefile-fileglobalsdefaultvalues.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-getmodelabsolutepath.html language=enus -->
## TOPIC 02587: SequenceFile.GetModelAbsolutePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-getmodelabsolutepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-getmodelabsolutepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.GetModelAbsolutePath( modelExists) Return Value String Purpose Returns the absolute pathname of the process model sequence file associated with this sequence file. Remarks Returns an empty string if the file has no model or if the model file could not be found. Parameters modelEx

### SequenceFile.GetModelAbsolutePath

#### Syntax

[SequenceFile](sequencefile.html).GetModelAbsolutePath( modelExists)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute pathname of the process model sequence file associated with this sequence file.

#### Remarks

Returns an empty string if the file has no model or if the model file could not be found.

#### Parameters

modelExists
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns
 True
 if the model file was found.

#### See Also

[SequenceFile.GetModelSequenceFile](sequencefile-getmodelsequencefile.html)

[SequenceFile.HasModel](sequencefile-hasmodel.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-getmodelcallbacknames.html language=enus -->
## TOPIC 02588: SequenceFile.GetModelCallbackNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-getmodelcallbacknames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-getmodelcallbacknames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.GetModelCallbackNames Return Value String Array Array of Model callback names the function returns. Purpose Obtains the list of Model callback names based on the model assigned to the sequence file. See Also Customizing Process Models and Callbacks SequenceFile.GetReservedCallbac

### SequenceFile.GetModelCallbackNames

#### Syntax

[SequenceFile](sequencefile.html).GetModelCallbackNames

#### Return Value

[String Array](data-types-for-teststand.html)

Array of Model callback names the function returns.

#### Purpose

Obtains the list of Model callback names based on the model assigned to the sequence file.

#### See Also

[Customizing Process Models and Callbacks](/csh?context=ts_tsfundamentals_customize_process_models_callbacks)

[SequenceFile.GetReservedCallbackNames](sequencefile-getreservedcallbacknames.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-getmodelsequencefile.html language=enus -->
## TOPIC 02589: SequenceFile.GetModelSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-getmodelsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-getmodelsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.GetModelSequenceFile( modelDescriptionString) Return Value SequenceFile Purpose Returns a reference to the process model sequence file that TestStand associates with the sequence file on which you call the method. Release this reference when you are finished using it. Remarks Ret

### SequenceFile.GetModelSequenceFile

#### Syntax

[SequenceFile](sequencefile.html).GetModelSequenceFile( modelDescriptionString)

#### Return Value

[SequenceFile](sequencefile.html)

#### Purpose

Returns a reference to the process model sequence file that TestStand associates with the sequence file on which you call the method. Release this reference when you are finished using it.

#### Remarks

Returns a
 NULL
 reference if the sequence file on which you call the method does not have a process model associated with it. The
 modelDescriptionString
 parameter contains a descriptive message even if this method returns
 NULL
 .

#### Parameters

modelDescriptionString
 As
 [String](data-types-for-teststand.html)

[Out] Returns a string that describes the process model file.

#### See Also

[Engine.GetStationModelSequenceFile](engine-getstationmodelsequencefile.html)

[SequenceFile](sequencefile.html)

[SequenceFile.GetModelAbsolutePath](sequencefile-getmodelabsolutepath.html)

[SequenceFile.HasModel](sequencefile-hasmodel.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-getreservedcallbacknames.html language=enus -->
## TOPIC 02590: SequenceFile.GetReservedCallbackNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-getreservedcallbacknames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-getreservedcallbacknames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.GetReservedCallbackNames Return Value String Array Array of reserved callback names the function returns. Purpose Obtains the list of reserved Engine callback names. See Also SequenceFile.CreateCallbackOverrideSequence SequenceFile.GetModelCallbackNames

### SequenceFile.GetReservedCallbackNames

#### Syntax

[SequenceFile](sequencefile.html).GetReservedCallbackNames

#### Return Value

[String Array](data-types-for-teststand.html)

Array of reserved callback names the function returns.

#### Purpose

Obtains the list of reserved Engine
 [callback](/csh?context=ts_tsfundamentals_customize_process_models_callbacks)
 names.

#### See Also

[SequenceFile.CreateCallbackOverrideSequence](sequencefile-createcallbackoverridesequence.html)

[SequenceFile.GetModelCallbackNames](sequencefile-getmodelcallbacknames.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-getsequence.html language=enus -->
## TOPIC 02591: SequenceFile.GetSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-getsequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-getsequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.GetSequence( index) Return Value Sequence Purpose Obtains a reference to a Sequence object that you specify by an index. Parameters index As Long [In] Specifies a zero-based index to indicate the sequence. See Also Sequence SequenceFile.NumSequences SequenceFile.RemoveSequence

### SequenceFile.GetSequence

#### Syntax

[SequenceFile](sequencefile.html).GetSequence( index)

#### Return Value

[Sequence](sequence.html)

#### Purpose

Obtains a reference to a Sequence object that you specify by an index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index to indicate the sequence.

#### See Also

[Sequence](sequence.html)

[SequenceFile.NumSequences](sequencefile-numsequences.html)

[SequenceFile.RemoveSequence](sequencefile-removesequence.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-getsequencebyname.html language=enus -->
## TOPIC 02592: SequenceFile.GetSequenceByName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-getsequencebyname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-getsequencebyname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.GetSequenceByName( sequenceNameParam) Return Value Sequence Purpose Returns a reference to a Sequence object you specify by name. Remarks Sequence names are case-insensitive. Parameters sequenceNameParam As String [In] Specifies the name of the Sequence object to which you want a

### SequenceFile.GetSequenceByName

#### Syntax

[SequenceFile](sequencefile.html).GetSequenceByName( sequenceNameParam)

#### Return Value

[Sequence](sequence.html)

#### Purpose

Returns a reference to a Sequence object you specify by name.

#### Remarks

Sequence names are case-insensitive.

#### Parameters

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the Sequence object to which you want a reference. If the sequence name does not exist, the method reports an error.

#### See Also

[Sequence](sequence.html)

[SequenceFile.GetSequenceIndex](sequencefile-getsequenceindex.html)

[SequenceFile.SequenceNameExists](sequencefile-sequencenameexists.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-getsequenceindex.html language=enus -->
## TOPIC 02593: SequenceFile.GetSequenceIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-getsequenceindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-getsequenceindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.GetSequenceIndex( sequenceNameParam) Return Value Long Returns the index of the sequence for which you specify a name. Returns -1 if no such sequence exists. Purpose Returns the index of the sequence in the sequence file that has the name you specify. Parameters sequenceNameParam

### SequenceFile.GetSequenceIndex

#### Syntax

[SequenceFile](sequencefile.html).GetSequenceIndex( sequenceNameParam)

#### Return Value

[Long](data-types-for-teststand.html)

Returns the index of the sequence for which you specify a name. Returns
 -1
 if no such sequence exists.

#### Purpose

Returns the index of the sequence in the sequence file that has the name you specify.

#### Parameters

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of a sequence in the sequence file.

#### See Also

[SequenceFile.GetSequenceByName](sequencefile-getsequencebyname.html)

[SequenceFile.SequenceNameExists](sequencefile-sequencenameexists.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-hasmodel.html language=enus -->
## TOPIC 02594: SequenceFile.HasModel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-hasmodel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-hasmodel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.HasModel Data Type Boolean Purpose Returns True if TestStand associates a process model sequence file with the sequence file on which you call the method. See Also SequenceFile.GetModelSequenceFile SequenceFile.ModelOption

### SequenceFile.HasModel

#### Syntax

[SequenceFile](sequencefile.html).HasModel

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if TestStand associates a process model sequence file with the sequence file on which you call the method.

#### See Also

[SequenceFile.GetModelSequenceFile](sequencefile-getmodelsequencefile.html)

[SequenceFile.ModelOption](sequencefile-modeloption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-id.html language=enus -->
## TOPIC 02595: SequenceFile.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.Id Data Type Long Purpose Returns a unique ID number for the sequence file. The ID number is never zero. Remarks The ID number is unique with respect to all sequence files that you open before you shut down the TestStand Engine. Use this ID number to compare two SequenceFile obje

### SequenceFile.Id

#### Syntax

[SequenceFile](sequencefile.html).Id

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique ID number for the sequence file.

Note

#### Remarks

The ID number is unique with respect to all sequence files that you open before you shut down the TestStand Engine.

Use this ID number to compare two SequenceFile object references to determine whether they refer to the same underlying sequence file.

#### See Also

[SequenceFile.Path](sequencefile-path.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-incchangecount.html language=enus -->
## TOPIC 02596: SequenceFile.IncChangeCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-incchangecount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-incchangecount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.IncChangeCount Purpose Increments the file change count. Remarks Increment the change count when making changes to the file to indicate to the sequence editor or user interface that the file was modified. Calling this method has the same effect as calling the PropertyObjectFile.I

### SequenceFile.IncChangeCount

#### Syntax

[SequenceFile](sequencefile.html).IncChangeCount

#### Purpose

Increments the file change count.

#### Remarks

Increment the change count when making changes to the file to indicate to the sequence editor or user interface that the file was modified.

Calling this method has the same effect as calling the
 [PropertyObjectFile.IncChangeCount](propertyobjectfile-incchangecount.html)
 method.

#### See Also

[PropertyObjectFile.ChangeCount](propertyobjectfile-changecount.html)

[PropertyObjectFile.IncChangeCount](propertyobjectfile-incchangecount.html)

[PropertyObjectFile.IsModified](propertyobjectfile-ismodified.html)

[PropertyObjectFile.SaveFileIfModified](propertyobjectfile-savefileifmodified.html)

[SequenceFile.ChangeCount](sequencefile-changecount.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-insertsequence.html language=enus -->
## TOPIC 02597: SequenceFile.InsertSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-insertsequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-insertsequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.InsertSequence( sequenceToInsert) Purpose This method is obsolete. Use the SequenceFile.InsertSequenceEx method instead. Remarks Adds a sequence to the end of the sequences list in the sequence file. The name of a sequence must be unique if it is contained within a sequence file.

### SequenceFile.InsertSequence

#### Syntax

[SequenceFile](sequencefile.html).InsertSequence( sequenceToInsert)

#### Purpose

Note

SequenceFile.InsertSequenceEx

#### Remarks

Adds a sequence to the end of the sequences list in the sequence file.

Note

#### Parameters

sequenceToInsert
 As
 [Sequence](sequence.html)

[In] Specifies the sequence to insert.

#### See Also

[Engine.NewSequence](engine-newsequence.html)

[Sequence](sequence.html)

[SequenceFile.InsertSequenceEx](sequencefile-insertsequenceex.html)

[SequenceFile.RemoveSequence](sequencefile-removesequence.html)

Parent topic:

Obsolete SequenceFile Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-insertsequenceex.html language=enus -->
## TOPIC 02598: SequenceFile.InsertSequenceEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-insertsequenceex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-insertsequenceex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.InsertSequenceEx( index, sequenceToInsert) Purpose Inserts a sequence at the specified index. Remarks Do not insert a sequence into a sequence file when the sequence resides in another sequence file. The sequence reference that you pass must be the only reference to the sequence.

### SequenceFile.InsertSequenceEx

#### Syntax

[SequenceFile](sequencefile.html).InsertSequenceEx( index, sequenceToInsert)

#### Purpose

Inserts a sequence at the specified index.

#### Remarks

Do not insert a sequence into a sequence file when the sequence resides in another sequence file. The sequence reference that you pass must be the only reference to the sequence. You can obtain the sole reference to a sequence by calling the
 [Engine.NewSequence](engine-newsequence.html)
 or
 [SequenceFile.RemoveSequence](sequencefile-removesequence.html)
 methods.

Note

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index at which to insert the sequence.

sequenceToInsert
 As
 [Sequence](sequence.html)

[In] Specifies the sequence to insert.

#### See Also

[Engine.NewSequence](engine-newsequence.html)

[Sequence](sequence.html)

[SequenceFile.DeleteSequence](sequencefile-deletesequence.html)

[SequenceFile.NumSequences](sequencefile-numsequences.html)

[SequenceFile.RemoveSequence](sequencefile-removesequence.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-isexecuting.html language=enus -->
## TOPIC 02599: SequenceFile.IsExecuting

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-isexecuting.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-isexecuting.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.IsExecuting Data Type Boolean Purpose Returns True if the sequence file contains one or more currently active sequences in an execution. Remarks If this property returns True , do not edit the sequence file. See Also SequenceFile.CanUnload

### SequenceFile.IsExecuting

#### Syntax

[SequenceFile](sequencefile.html).IsExecuting

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the sequence file contains one or more currently active sequences in an execution.

#### Remarks

If this property returns
 True
 , do not edit the sequence file.

#### See Also

[SequenceFile.CanUnload](sequencefile-canunload.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-loadmodules.html language=enus -->
## TOPIC 02600: SequenceFile.LoadModules

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-loadmodules.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-loadmodules.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.LoadModules( loadOptions = 0, [sequenceContextParam]) Return Value Boolean Returns True on success or False if a module fails to load. Purpose Loads the code modules for all steps in all sequences of the sequence file. Parameters loadOptions As Long [In] Specifies one or more Loa

### SequenceFile.LoadModules

#### Syntax

[SequenceFile](sequencefile.html).LoadModules( loadOptions = 0, [sequenceContextParam])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 on success or
 False
 if a module fails to load.

#### Purpose

Loads the code modules for all steps in all sequences of the sequence file.

#### Parameters

loadOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [LoadModuleOptions](loadmoduleoptions.html)
 using the bitwise-OR operator to modify the behavior of this method.

This parameter has a default value of
 0
 .

sequenceContextParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you are passing the
 [LoadModule_EvaluateExpressions](loadmoduleoptions.html)
 flag to the
 loadOptions
 parameter, pass a
 [SequenceContext](sequencecontext.html)
 object for this parameter to use when evaluating the expressions. Also, if you are calling this method from a step in an execution, pass the sequence context of the execution.

#### See Also

[LoadModuleOptions](loadmoduleoptions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceContext](sequencecontext.html)

[SequenceFile.UnloadModules](sequencefile-unloadmodules.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-modeloption.html language=enus -->
## TOPIC 02601: SequenceFile.ModelOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-modeloption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-modeloption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.ModelOption Data Type ModelOptions Use the following constants with this data type: ModelOption_NoModel –(Value: 1) Specifies that the sequence file does not use a process model. ModelOption_RequireSpecificModel –(Value: 2) Specifies a particular process model file. If you select

### SequenceFile.ModelOption

#### Syntax

[SequenceFile](sequencefile.html).ModelOption

#### Data Type

[ModelOptions](modeloptions.html)

Use the following constants with this data type:

- ModelOption_NoModel 
 –(Value: 1) Specifies that the sequence file does not use a process model.
- ModelOption_RequireSpecificModel 
 –(Value: 2) Specifies a particular process model file. If you select this value, you must use the
 SequenceFile.ModelPath 
 property to specify the location of the process model file.
- ModelOption_UseStationModel 
 –(Value: 0) Instructs TestStand to use the process model file the Station Model option on the
 Model tab 
 of the
 Station Options 
 dialog box specifies.

#### Purpose

Specifies the process model file to use for the sequence file.

#### Remarks

This setting is valid only when you enable the Allow Other Model Settings option in the Station Options dialog box. Refer to
 [StationOptions.AllowOtherModels](stationoptions-allowothermodels.html)
 for more information about allowing sequence files to specify a process model file other than the current station model file.

#### See Also

[Model tab](../tsref/model-tab-station-options-dialog-box.html)

[SequenceFile.HasModel](sequencefile-hasmodel.html)

[SequenceFile.ModelPath](sequencefile-modelpath.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[StationOptions.AllowOtherModels](stationoptions-allowothermodels.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-modelpath.html language=enus -->
## TOPIC 02602: SequenceFile.ModelPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-modelpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-modelpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.ModelPath Data Type String Purpose Specifies the file path of a particular model file. Remarks Specifies the file path to a model file when the value of the SequenceFile.ModelOption property is ModelOption_RequireSpecificModel . See Also SequenceFile.ModelOption SequenceFile.Path

### SequenceFile.ModelPath

#### Syntax

[SequenceFile](sequencefile.html).ModelPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the file path of a particular model file.

#### Remarks

Specifies the file path to a model file when the value of the
 [SequenceFile.ModelOption](sequencefile-modeloption.html)
 property is
 ModelOption_RequireSpecificModel
 .

#### See Also

[SequenceFile.ModelOption](sequencefile-modeloption.html)

[SequenceFile.Path](sequencefile-path.html)

[StationOptions.AllowOtherModels](stationoptions-allowothermodels.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-modelplugindescription.html language=enus -->
## TOPIC 02603: SequenceFile.ModelPluginDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-modelplugindescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-modelplugindescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.ModelPluginDescription Data Type PropertyObject Purpose Returns the FileGlobals.ModelPluginComponentDescription variable, if it exists. Otherwise, returns null. This property is accessible even if the file is locked. See Also SequenceContext.FileGlobals

### SequenceFile.ModelPluginDescription

#### Syntax

[SequenceFile](sequencefile.html).ModelPluginDescription

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the FileGlobals.ModelPluginComponentDescription variable, if it exists. Otherwise, returns null. This property is accessible even if the file is locked.

#### See Also

[SequenceContext.FileGlobals](sequencecontext-fileglobals.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-moduleloadoption.html language=enus -->
## TOPIC 02604: SequenceFile.ModuleLoadOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-moduleloadoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-moduleloadoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.ModuleLoadOption Data Type ModuleLoadOptions Use the following constants with this data type: LoadOption_DynamicLoad –(Value: 3) Does not load the code module for a step until the step is ready to call it. LoadOption_PreloadWhenExecuted –(Value: 2) Loads the code module for a ste

### SequenceFile.ModuleLoadOption

#### Syntax

[SequenceFile](sequencefile.html).ModuleLoadOption

#### Data Type

[ModuleLoadOptions](moduleloadoptions.html)

Use the following constants with this data type:

- LoadOption_DynamicLoad 
 –(Value: 3) Does not load the code module for a step until the step is ready to call it.
- LoadOption_PreloadWhenExecuted 
 –(Value: 2) Loads the code module for a step when any sequence in the sequence file containing the step begins executing.
- LoadOption_PreloadWhenOpened 
 –(Value: 1) Loads the code module for a step when TestStand loads the sequence file containing the step into memory.
- LoadOption_UseStepLoadOption 
 –(Value: 4) Loads each code module according to the load option for the step that uses it. This option is valid only for the
 SequenceFile.ModuleLoadOption 
 property.

#### Purpose

This property instructs TestStand when to load the code modules the steps in the sequence file call. You can use this property to override the load option of all steps in the sequence file, or you can defer to the load option contained in each individual step.

#### See Also

[SequenceFile.ModuleUnloadOption](sequencefile-moduleunloadoption.html)

[Step.ModuleLoadOption](step-moduleloadoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-moduleunloadoption.html language=enus -->
## TOPIC 02605: SequenceFile.ModuleUnloadOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-moduleunloadoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-moduleunloadoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.ModuleUnloadOption Data Type ModuleUnloadOptions Use the following constants with this data type: UnloadOption_AfterSequenceExecution –(Value: 3) Unloads the code module for a step after the sequence containing the step finishes executing. UnloadOption_AfterStepExecution –(Value:

### SequenceFile.ModuleUnloadOption

#### Syntax

[SequenceFile](sequencefile.html).ModuleUnloadOption

#### Data Type

[ModuleUnloadOptions](moduleunloadoptions.html)

Use the following constants with this data type:

- UnloadOption_AfterSequenceExecution 
 –(Value: 3) Unloads the code module for a step after the sequence containing the step finishes executing.
- UnloadOption_AfterStepExecution 
 –(Value: 2) Unloads the code module for a step after the step finishes executing.
- UnloadOption_OnPreconditionFailure 
 –(Value: 1) Unloads the code module for a step if the precondition for the step evaluates to
 False 
 .
- UnloadOption_UseStepUnloadOption 
 –(Value: 5) Unloads the code module for a step according to the unload option for the step. This option is valid only for the
 SequenceFile.ModuleUnloadOption 
 property.
- UnloadOption_WithSequenceFile 
 –(Value: 4) Unloads the code module for a step when TestStand unloads the sequence file from memory that contains the step.

#### Purpose

This property instructs TestStand when to unload the code modules the steps in the sequence file call. You can use this property to override the unload option of all steps in the sequence file, or you can defer to the unload option contained in each individual step.

#### See Also

[SequenceFile.ModuleLoadOption](sequencefile-moduleloadoption.html)

[Step.ModuleUnloadOption](step-moduleunloadoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-neweditcontext.html language=enus -->
## TOPIC 02606: SequenceFile.NewEditContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-neweditcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-neweditcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.NewEditContext Return Value SequenceContext A reference to a SequenceContext object. Release this reference when you are finished using it. Purpose Returns a sequence context that approximates the sequence context TestStand creates when you run a sequence in the sequence file. Re

### SequenceFile.NewEditContext

#### Syntax

[SequenceFile](sequencefile.html).NewEditContext

#### Return Value

[SequenceContext](sequencecontext.html)

A reference to a SequenceContext object. Release this reference when you are finished using it.

#### Purpose

Returns a sequence context that approximates the sequence context TestStand creates when you run a sequence in the sequence file.

#### Remarks

You can pass the object this method returns as a parameter to the
 [Engine.DisplayBrowseExprDialogEx](engine-displaybrowseexprdialogex.html)
 and
 [Engine.DisplayBrowsePropertyObjectDialog](engine-displaybrowsepropertyobjectdialog.html)
 methods.

#### See Also

[Engine.DisplayBrowseExprDialogEx](engine-displaybrowseexprdialogex.html)

[Engine.DisplayBrowsePropertyObjectDialog](engine-displaybrowsepropertyobjectdialog.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-numsequences.html language=enus -->
## TOPIC 02607: SequenceFile.NumSequences

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-numsequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-numsequences.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.NumSequences Data Type Long Purpose Returns the number of sequences contained in the sequence file. See Also SequenceFile.GetSequence SequenceFile.GetSequenceByName

### SequenceFile.NumSequences

#### Syntax

[SequenceFile](sequencefile.html).NumSequences

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of sequences contained in the sequence file.

#### See Also

[SequenceFile.GetSequence](sequencefile-getsequence.html)

[SequenceFile.GetSequenceByName](sequencefile-getsequencebyname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-path.html language=enus -->
## TOPIC 02608: SequenceFile.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.Path Data Type String Purpose Returns the pathname TestStand used when the sequence file was last saved or loaded. Remarks This property returns the same value as the PropertyObjectFile.Path property. See Also SequenceFile.ModelPath PropertyObjectFile.Path

### SequenceFile.Path

#### Syntax

[SequenceFile](sequencefile.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the pathname TestStand used when the sequence file was last saved or loaded.

#### Remarks

This property returns the same value as the
 [PropertyObjectFile.Path](propertyobjectfile-path.html)
 property.

#### See Also

[SequenceFile.ModelPath](sequencefile-modelpath.html)

[PropertyObjectFile.Path](propertyobjectfile-path.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-removesequence.html language=enus -->
## TOPIC 02609: SequenceFile.RemoveSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-removesequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-removesequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.RemoveSequence( index) Return Value Sequence Purpose Removes a sequence from a sequence file and returns a reference to it. Parameters index As Long [In] Specifies a zero-based index to indicate the sequence to remove. See Also Sequence SequenceFile.DeleteSequence SequenceFile.In

### SequenceFile.RemoveSequence

#### Syntax

[SequenceFile](sequencefile.html).RemoveSequence( index)

#### Return Value

[Sequence](sequence.html)

#### Purpose

Removes a sequence from a sequence file and returns a reference to it.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index to indicate the sequence to remove.

#### See Also

[Sequence](sequence.html)

[SequenceFile.DeleteSequence](sequencefile-deletesequence.html)

[SequenceFile.InsertSequenceEx](sequencefile-insertsequenceex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-save.html language=enus -->
## TOPIC 02610: SequenceFile.Save

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-save.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-save.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.Save( pathString) Purpose Saves the sequence file to disk. Remarks Calling this method with an empty string argument has the same effect as calling the PropertyObjectFile.WriteFile method. Ensure the pathString provided is an absolute path and not relative. Parameters pathString

### SequenceFile.Save

#### Syntax

[SequenceFile](sequencefile.html).Save( pathString)

#### Purpose

Saves the sequence file to disk.

#### Remarks

Calling this method with an empty string argument has the same effect as calling the
 [PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)
 method.

Ensure the
 pathString
 provided is an absolute path and not relative.

#### Parameters

pathString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute pathname with which to save the file. Pass an empty string to save the file using the same pathname with which TestStand last loaded or saved it.

#### See Also

[SequenceFile.Path](sequencefile-path.html)

[PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-sequencefiletype.html language=enus -->
## TOPIC 02611: SequenceFile.SequenceFileType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-sequencefiletype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-sequencefiletype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.SequenceFileType Data Type SequenceFileTypes Use the following constants with this data type: SeqFileType_FrontEndCBacks –(Value: 2) The sequence file containing Front-End callbacks. SeqFileType_Model –(Value: 1) A process model sequence file. SeqFileType_Normal –(Value: 0) A nor

### SequenceFile.SequenceFileType

#### Syntax

[SequenceFile](sequencefile.html).SequenceFileType

#### Data Type

[SequenceFileTypes](sequencefiletypes.html)

Use the following constants with this data type:

- SeqFileType_FrontEndCBacks 
 –(Value: 2) The sequence file containing Front-End callbacks.
- SeqFileType_Model 
 –(Value: 1) A process model sequence file.
- SeqFileType_Normal 
 –(Value: 0) A normal sequence file.
- SeqFileType_StationCBacks 
 –(Value: 3) The sequence file containing the Test Station callbacks.
- SeqFileType_Template 
 –(Value: 4) The sequence file containing the templates for callback sequences.

#### Purpose

Specifies the type of sequence file.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-sequencenameexists.html language=enus -->
## TOPIC 02612: SequenceFile.SequenceNameExists

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-sequencenameexists.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-sequencenameexists.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.SequenceNameExists( sequenceNameParam) Return Value Boolean Purpose Returns True if a sequence with the name you specify already exists in the sequence file. Parameters sequenceNameParam As String [In] Specifies a sequence name to search for. Sequence names are case-insensitive.

### SequenceFile.SequenceNameExists

#### Syntax

[SequenceFile](sequencefile.html).SequenceNameExists( sequenceNameParam)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if a sequence with the name you specify already exists in the sequence file.

#### Parameters

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies a sequence name to search for. Sequence names are case-insensitive.

#### See Also

[SequenceFile.GetSequenceByName](sequencefile-getsequencebyname.html)

[SequenceFile.GetSequenceIndex](sequencefile-getsequenceindex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-unloadcallbackenabled.html language=enus -->
## TOPIC 02613: SequenceFile.UnloadCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-unloadcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-unloadcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.UnloadCallbackEnabled Data Type Boolean Purpose Specifies if TestStand calls the SequenceFileUnload callback sequence when unloading the sequence file. Set this property to False to prevent TestStand from calling the SequenceFileUnload callback for the sequence file. See Also Eng

### SequenceFile.UnloadCallbackEnabled

#### Syntax

[SequenceFile](sequencefile.html).UnloadCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if TestStand calls the SequenceFileUnload callback sequence when unloading the sequence file. Set this property to
 False
 to prevent TestStand from calling the SequenceFileUnload callback for the sequence file.

#### See Also

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[ReleaseSeqFileOptions](releaseseqfileoptions.html)

[SequenceFile.CanUnload](sequencefile-canunload.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile-unloadmodules.html language=enus -->
## TOPIC 02614: SequenceFile.UnloadModules

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile-unloadmodules.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile-unloadmodules.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceFile.UnloadModules Return Value Boolean Returns True if all modules were successfully unloaded. If any sequences in the file are executing when you call this method, the method returns False . Purpose Unloads the code modules from all steps in all sequences of the sequence file. See A

### SequenceFile.UnloadModules

#### Syntax

[SequenceFile](sequencefile.html).UnloadModules

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if all modules were successfully unloaded. If any sequences in the file are executing when you call this method, the method returns
 False
 .

#### Purpose

Unloads the code modules from all steps in all sequences of the sequence file.

#### See Also

[SequenceFile.IsExecuting](sequencefile-isexecuting.html)

[SequenceFile.LoadModules](sequencefile-loadmodules.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefile.html language=enus -->
## TOPIC 02615: SequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the SequenceFile class represent a sequence file that can contain sequences. You can obtain a reference to a SequenceFile object by using the Engine.GetSequenceFileEx or Engine.NewSequenceFile methods. Use the reference to examine or modify sequence file settings and to examine or modify

### SequenceFile

Objects of the SequenceFile class represent a sequence file that can contain sequences. You can obtain a reference to a SequenceFile object by using the
 [Engine.GetSequenceFileEx](engine-getsequencefileex.html)
 or
 [Engine.NewSequenceFile](engine-newsequencefile.html)
 methods. Use the reference to examine or modify sequence file settings and to examine or modify the list of sequences in the sequence file.

#### Properties

| BatchSyncOption |
| --- |
| CanUnload (Read Only) |
| ChangeCount (Read Only) |
| FileGlobalsDefaultValues (Read Only) |
| FileGlobalsScope |
| HasModel (Read Only) |
| Id (Read Only) |
| IsExecuting (Read Only) |
| ModelOption |
| ModelPath |
| ModelPluginDescription (Read Only) |
| ModuleLoadOption |
| ModuleUnloadOption |
| NumSequences (Read Only) |
| Path |
| SequenceFileType |
| UnloadCallbackEnabled |

#### Methods

| AddLoadReference |
| --- |
| AsPropertyObject |
| AsPropertyObjectFile |
| CreateCallbackOverrideSequence |
| DeleteSequence |
| GetModelAbsolutePath |
| GetModelCallbackNames |
| GetModelSequenceFile |
| GetReservedCallbackNames |
| GetSequence |
| GetSequenceByName |
| GetSequenceIndex |
| IncChangeCount |
| InsertSequenceEx |
| LoadModules |
| NewEditContext |
| RemoveSequence |
| Save |
| SequenceNameExists |
| UnloadModules |

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.NewSequenceFile](engine-newsequencefile.html)

[PropertyObjectFile.Comment](propertyobjectfile-comment.html)

[PropertyObjectFile.Version](propertyobjectfile-version.html)

[Sequence](sequence.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencefiletypes.html language=enus -->
## TOPIC 02616: SequenceFileTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencefiletypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencefiletypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify the type of a sequence file. The constants represent the possible values for the SequenceFile.SequenceFileType property. SeqFileType_FrontEndCBacks –(Value: 2) The sequence file containing Front-End callbacks. SeqFileType_Model –(Value: 1) A process model

### SequenceFileTypes

This data type contains values that specify the type of a sequence file. The constants represent the possible values for the
 [SequenceFile.SequenceFileType](sequencefile-sequencefiletype.html)
 property.

- SeqFileType_FrontEndCBacks 
 –(Value: 2) The sequence file containing Front-End callbacks.
- SeqFileType_Model 
 –(Value: 1) A process model sequence file.
- SeqFileType_Normal 
 –(Value: 0) A normal sequence file.
- SeqFileType_StationCBacks 
 –(Value: 3) The sequence file containing the Test Station callbacks.
- SeqFileType_Template 
 –(Value: 4) The sequence file containing the templates for callback sequences.

#### See Also

[SequenceFile.SequenceFileType](sequencefile-sequencefiletype.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequenceproperties.html language=enus -->
## TOPIC 02617: SequenceProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequenceproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequenceproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these string constants to create lookup strings when using the PropertyObject class to access the built-in properties of a sequence. Seq_CleanupProp –(Value: "Cleanup") Seq_MainProp –(Value: "Main") Seq_SetupProp –(Value: "Setup") See Also Lookup Strings PropertyObject StepGroups

### SequenceProperties

Use these string constants to create
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 when using the PropertyObject class to access the built-in properties of a sequence.

- Seq_CleanupProp 
 –(Value: "Cleanup")
- Seq_MainProp 
 –(Value: "Main")
- Seq_SetupProp 
 –(Value: "Setup")

#### See Also

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[PropertyObject](propertyobject.html)

[StepGroups](stepgroups.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencetypes.html language=enus -->
## TOPIC 02618: SequenceTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencetypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencetypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify the sequence type. Use the values of this enumeration with the Sequence.Type property. SeqType_Callback –(Value: 1) The sequence is a Process Model callback. SeqType_CfgEntryPoint –(Value: 5) The sequence is a Configuration entry point. SeqType_ExeEntryPoi

### SequenceTypes

This data type contains values that specify the sequence type. Use the values of this enumeration with the
 [Sequence.Type](sequence-type.html)
 property.

- SeqType_Callback 
 –(Value: 1) The sequence is a Process Model callback.
- SeqType_CfgEntryPoint 
 –(Value: 5) The sequence is a Configuration entry point.
- SeqType_ExeEntryPoint 
 –(Value: 3) The sequence is an Execution entry point.
- SeqType_Normal 
 –(Value: 0) The sequence is not a callback or an entry point.
- SeqType_ReservedCallback 
 –(Value: 7) Only the
 Sequence.GetEffectiveType 
 method returns this value. The sequence is one of the predefined callbacks TestStand reserves.

#### See Also

[Sequence](sequence.html)

[Sequence.GetEffectiveType](sequence-geteffectivetype.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/serializationoptions.html language=enus -->
## TOPIC 02619: SerializationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/serializationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/serializationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Engine.SerializeObjects method. SerializationOption_NoOptions –(Value: 0) TestStand uses the INI format by default if you specify no options. SerializationOption_SupportNonTypedefMatchingInstances –(Value: 4) Normally, type instances must match the structure of the under

### SerializationOptions

Use these constants with the
 [Engine.SerializeObjects](engine-serializeobjects.html)
 method.

- SerializationOption_NoOptions 
 –(Value: 0) TestStand uses the INI format by default if you specify no options.
- SerializationOption_SupportNonTypedefMatchingInstances 
 –(Value: 4) Normally, type instances must match the structure of the underlying type definitions. Although you can use the
 PropertyObject 
 properties and methods to modify a type instance so it no longer matches the structure of the underlying type definition, National Instruments does not recommend doing so even though it can be useful in some limited cases. Use the
 SerializationOption_SupportNonTypedefMatchingInstances 
 option only when you must serialize objects that contain these types of instances to preserve the modifications during unserialization. 

If you do not use this option when you serialize objects, TestStand makes the type instances conform to the underlying type definition during unserialization. You do not need to use this option when unserializing the data. TestStand makes type instances conform to type definitions and removes any structural modifications you programmatically make in the following situations, even when you use the
 SerializationOption_SupportNonTypedefMatchingInstances 
 option:
 
 Instead of creating type instances that do not match type definitions, create a container property in the type definition, set the
 PropFlags_UnstructuredProperty 
 property flag, and place all the custom, per-instance properties in the container. National Instruments recommends that you use unstructured containers to hold properties that do not match the definition to use type instances that differ from type definitions.
 Note 
 The
 SerializationOption_SupportNonTypedefMatchingInstances
 option does not support the
 .ini
 format. You must use this option with the bitwise-OR operator with the
 SerializationOption_UseXml
 or
 SerializationOption_UseBinary
 option.
  - When you modify the structure of a type definition or use the Apply to All Loaded Instances of the Type option to modify a type definition, TestStand makes all type instances in memory conform to the type definition.
  - When you load a file and use automatic or manual type conflict resolution to replace the existing global definition of the type with a new version of the type definition, TestStand makes all instances of the type in memory conform to the new version of the type definition.
- SerializationOption_UseBinary 
 –(Value: 1) Use this option to greatly enhance the speed of both serialization and unserialization. This option is the fastest and most memory efficient format.
- SerializationOption_UseXml 
 –(Value: 2) Use this option if you want to read or parse the data as XML. This option is the most readable and parseable format. Normally, the data from the
 Engine.SerializeObjects 
 method is passed as input to the
 Engine.UnserializeObjects 
 and
 Engine.UnserializeObjectsAndTypes 
 methods. In this case, National Instruments recommends using
 SerializationOption_UseBinary 
 because that option is faster and more memory efficient.

#### See Also

[Engine.SerializeObjects](engine-serializeobjects.html)

[Engine.UnserializeObjects](engine-unserializeobjects.html)

[Engine.UnserializeObjectsAndTypes](engine-unserializeobjectsandtypes.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/settempfiledirectoryoptions.html language=enus -->
## TOPIC 02620: SetTempFileDirectoryOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/settempfiledirectoryoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/settempfiledirectoryoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration with the Report.SetTempFileDirectoryEx method. SetTempFileDirectoryOption_Default –(Value: 0) Specifies the default option. When you use this value with the Report.SetTempFileDirectoryEx method, calling the Report.Load or Report.Save method modifies the directory path where Test

### SetTempFileDirectoryOptions

Use this enumeration with the
 [Report.SetTempFileDirectoryEx](report-settempfiledirectoryex.html)
 method.

- SetTempFileDirectoryOption_Default 
 –(Value: 0) Specifies the default option. When you use this value with the
 Report.SetTempFileDirectoryEx 
 method, calling the
 Report.Load 
 or
 Report.Save 
 method modifies the directory path where TestStand saves the file the
 Report.GetTempFile 
 method creates.

Using this value with the
 Report.SetTempFileDirectoryEx 
 method results in the same behavior as using the
 Report.TempFileDirectory 
 property to specify the directory path where TestStand saves the file the
 Report.GetTempFile 
 method creates.
- SetTempFileDirectoryOption_NeverOverride 
 –(Value: 1) Specifies to never override the directory path the
 Report.SetTempFileDirectoryEx 
 method specifies when you call the
 Report.Load 
 or
 Report.Save 
 method. You can override the directory path by calling the
 Report.SetTempFileDirectoryEx 
 method again.

#### See Also

[Report.SetTempFileDirectoryEx](report-settempfiledirectoryex.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sourcecontrolcommandoptions.html language=enus -->
## TOPIC 02621: SourceControlCommandOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sourcecontrolcommandoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sourcecontrolcommandoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the WorkspaceObject.DoSourceControlCommand , WorkspaceObject.CanDoSourceControlCommand , and WorkspaceObject.UpdateStatus methods. Use the bitwise-OR operator to specify more than one option. SCCmdOption_DoNotRecurse –(V

### SourceControlCommandOptions

These constants represent the options you can use with the
 options
 parameter of the
 [WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)
 ,
 [WorkspaceObject.CanDoSourceControlCommand](workspaceobject-candosourcecontrolcommand.html)
 , and
 [WorkspaceObject.UpdateStatus](workspaceobject-updatestatus.html)
 methods. Use the bitwise-OR operator to specify more than one option.

- SCCmdOption_DoNotRecurse 
 –(Value: 0x1) Does not apply the operation recursively on items in the container.
- SCCmdOption_NoOptions 
 –(Value: 0x0) No options.
- SCCmdOption_ShowPromptDialog 
 –(Value: 0x4) Launches a dialog box with a list of files before performing the operation on the files. You cannot combine this option with
 SCCmdOption_SkipPromptDialog 
 . If you do not specify this option or
 SCCmdOption_SkipPromptDialog 
 , the engine Configuration option determines whether the dialog box is launched.
 Note 
 This constant applies only to the
 SCCmd_CheckOut
 and
 SSCmd_GetLatest
 commands for the
 [WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)
 method.
- SCCmdOption_SkipErrorDialog 
 –(Value: 0x8) Does not launch a dialog box for errors.
- SCCmdOption_SkipPromptDialog 
 –(Value: 0x2) Does not launch a dialog box with a list of files before performing the operation on the files. You cannot combine this option with
 SCCmdOption_ShowPromptDialog 
 . If you do not specify this option or
 SCCmdOption_ShowPromptDialog 
 , the engine Configuration option determines whether the dialog box is launched.
 Note 
 This constant applies only to the
 SCCmd_CheckOut
 and
 SSCmd_GetLatest
 commands for the
 WorkspaceObject.DoSourceControlCommand
 method.

#### See Also

[WorkspaceObject.CanDoSourceControlCommand](workspaceobject-candosourcecontrolcommand.html)

[WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)

[WorkspaceObject.UpdateStatus](workspaceobject-updatestatus.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sourcecontrolcommands.html language=enus -->
## TOPIC 02622: SourceControlCommands

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sourcecontrolcommands.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sourcecontrolcommands.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify source code control commands. Use one of these values to specify the scCommand parameter of the WorkspaceObject.DoSourceControlCommand and WorkspaceObject.CanDoSourceControlCommand methods. SCCmd_AddToSC –(Value: 1) Adds the specified files to source code

### SourceControlCommands

This data type contains values that specify source code control commands. Use one of these values to specify the
 scCommand
 parameter of the
 [WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)
 and
 [WorkspaceObject.CanDoSourceControlCommand](workspaceobject-candosourcecontrolcommand.html)
 methods.

- SCCmd_AddToSC 
 –(Value: 1) Adds the specified files to source code control.
- SCCmd_CheckIn 
 –(Value: 4) Checks in the specified files to source code control.
- SCCmd_CheckOut 
 –(Value: 3) Checks out the specified files from source code control.
- SCCmd_GetLatest 
 –(Value: 5) Obtains the latest version of the specified files from source code control.
- SCCmd_RemoveFromSC 
 –(Value: 2) Removes the specified files from source code control.
- SCCmd_ShowDifferences 
 –(Value: 7) Shows the differences between the latest version in source code control and the local version of the specified file.
- SCCmd_ShowHistory 
 –(Value: 8) Shows the source code control history of the specified file.
- SCCmd_ShowProperties 
 –(Value: 9) Shows the source code control properties of the specified file.
- SCCmd_ShowProviderOptions 
 –(Value: 10) Launches the source code control provider options dialog box.
- SCCmd_UndoCheckOut 
 –(Value: 6) Undoes the check out of the specified files from source code control.

#### See Also

[WorkspaceObject.CanDoSourceControlCommand](workspaceobject-candosourcecontrolcommand.html)

[WorkspaceObject.DoSourceControlCommand](workspaceobject-dosourcecontrolcommand.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sourcecontrolstatuses.html language=enus -->
## TOPIC 02623: SourceControlStatuses

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sourcecontrolstatuses.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sourcecontrolstatuses.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the return values of the WorkspaceObject.SourceControlStatus property. Use the bitwise-AND operator with the return value to determine whether any of these flags are set. SCStatus_CheckedOut –(Value: 0x2) Specifies that the file is checked out by you to a directory where Te

### SourceControlStatuses

These constants represent the return values of the
 [WorkspaceObject.SourceControlStatus](workspaceobject-sourcecontrolstatus.html)
 property. Use the bitwise-AND operator with the return value to determine whether any of these flags are set.

- SCStatus_CheckedOut 
 –(Value: 0x2) Specifies that the file is checked out by you to a directory where TestStand expects the file to be. The
 SCStatus_CheckedOutByUser 
 flag must also be on for this flag to be on. If
 SCStatus_CheckedOutByUser 
 is on but
 SCStatus_CheckedOut 
 is off, the file is checked out to a different directory.
- SCStatus_CheckedOutByUser 
 –(Value: 0x1000) Specifies that the file is checked out by you independent of the directory location.
- SCStatus_CheckedOutMultiple 
 –(Value: 0x10) Specifies that the file is checked out by multiple users. The file might or might not be checked out by you.
- SCStatus_CheckedOutOther 
 –(Value: 0x4) Specifies that the file is checked out by a user other than you. If this flag is on and
 SCStatus_CheckedOutMultiple 
 and
 SCStatus_CheckedOutByUser 
 are also on, both the current user and some other user have the file checked out. If this flag and
 SCStatus_CheckedOutMultiple 
 are on but
 SCStatus_CheckedOutByUser 
 is off, the current user does not have the file checked out, but several other users do.
- SCStatus_Deleted 
 –(Value: 0x40) Specifies that the file has been deleted from the project under source code control.
- SCStatus_InSC 
 –(Value: 0x1) Specifies that the file is under source code control.
- SCStatus_NotInSC 
 –(Value: 0x0) Specifies that the file is not under source code control.
- SCStatus_OutOfDate 
 –(Value: 0x20) Specifies that the version you have is not the latest version of the file.

#### See Also

[WorkspaceObject.SourceControlStatus](workspaceobject-sourcecontrolstatus.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/specifymoduleoptions.html language=enus -->
## TOPIC 02624: SpecifyModuleOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/specifymoduleoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/specifymoduleoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the Step.SpecifyModule method. Use the bitwise-OR operator to specify more than one option. SpecMod_AllowPrototypeChanges –(Value: 0x4) Use this option to change the function prototype of the module. SpecMod_NoOptions –(Value: 0x0) No options. S

### SpecifyModuleOptions

These constants represent the options you can use with the
 [Step.SpecifyModule](step-specifymodule.html)
 method. Use the bitwise-OR operator to specify more than one option.

- SpecMod_AllowPrototypeChanges 
 –(Value: 0x4) Use this option to change the function prototype of the module.
- SpecMod_NoOptions 
 –(Value: 0x0) No options.
- SpecMod_NoParameterLogging 
 –(Value: 0x10) Use this option to prevent specifying parameters to log as additional results in the Specify Module dialog box. When you use this option, the parameters control does not include a Log column and does not include an Advanced Logging menu item in the context menu.
- SpecMod_NoSyntaxChecking 
 –(Value: 0x2) Use this option to disable expression syntax checking when closing the
 Specify Module 
 dialog box.
- SpecMod_ReadOnly 
 –(Value: 0x1) Use this option to create a read-only version of the Specify Module dialog box.

#### See Also

[Specify Module dialog box](../tsref/edit-activex-com-call-dialog-box.html)

[Step.SpecifyModule](step-specifymodule.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/specifystepsbyuniqueidoptions.html language=enus -->
## TOPIC 02625: SpecifyStepsByUniqueIdOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/specifystepsbyuniqueidoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/specifystepsbyuniqueidoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the StationOptions.SpecifyStepsByUniqueIdInExpressions property. SpecifyStepsByUniqueIdOption_Ask –(Value: 1) TestStand prompts you to use a unique step ID. SpecifyStepsByUniqueIdOption_No –(Value: 3) Use step names. SpecifyStepsByUniqueIdOption_Yes –(Value: 2) Use u

### SpecifyStepsByUniqueIdOptions

Use the following constants with the
 [StationOptions.SpecifyStepsByUniqueIdInExpressions](stationoptions-specifystepsbyuniqueidinexpres.html)
 property.

- SpecifyStepsByUniqueIdOption_Ask 
 –(Value: 1) TestStand prompts you to use a unique step ID.
- SpecifyStepsByUniqueIdOption_No 
 –(Value: 3) Use step names.
- SpecifyStepsByUniqueIdOption_Yes 
 –(Value: 2) Use unique step IDs.

#### See Also

[StationOptions.SpecifyStepsByUniqueIdInExpressions](stationoptions-specifystepsbyuniqueidinexpres.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-allowallusersaccessfromremotem.html language=enus -->
## TOPIC 02626: StationOptions.AllowAllUsersAccessFromRemoteMachine

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-allowallusersaccessfromremotem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-allowallusersaccessfromremotem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.AllowAllUsersAccessFromRemoteMachine Data Type Boolean Purpose Specifies whether all users from remote machines can call sequences on this computer. Remarks If you set this property to True , you do not have to configure the remote TestStand server using the dcomcnfg applicatio

### StationOptions.AllowAllUsersAccessFromRemoteMachine

#### Syntax

[StationOptions](stationoptions.html).AllowAllUsersAccessFromRemoteMachine

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether all users from remote machines can call sequences on this computer.

#### Remarks

If you set this property to
 True
 , you do not have to
 [configure the remote TestStand server](/csh?context=ts_tsfundamentals_setting_ts_asserver_remote_executions)
 using the dcomcnfg application. When you set this property, TestStand modifies the registry in the same manner as dcomcnfg.

Note

StationOptions.AllowSequenceCallFromRemoteMachine

True

#### See Also

[Engine.IsRemote](engine-isremote.html)

[StationOptions.AllowSequenceCallsFromRemoteMachine](stationoptions-allowsequencecallsfromremotema.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-allowautomatictypeconflictreso.html language=enus -->
## TOPIC 02627: StationOptions.AllowAutomaticTypeConflictResolution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-allowautomatictypeconflictreso.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-allowautomatictypeconflictreso.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.AllowAutomaticTypeConflictResolution Data Type AllowAutomaticTypeConflictResolutionOptions Use the following constants with this data type: AllowAutomaticTypeConflictResolutionOption_Always –(Value: 0) Always allows automatic type conflict resolution, which can cause unintended

### StationOptions.AllowAutomaticTypeConflictResolution

#### Syntax

[StationOptions](stationoptions.html).AllowAutomaticTypeConflictResolution

#### Data Type

[AllowAutomaticTypeConflictResolutionOptions](allowautomatictypeconflictresolutionoptions.html)

Use the following constants with this data type:

- AllowAutomaticTypeConflictResolutionOption_Always 
 –(Value: 0) Always allows automatic type conflict resolution, which can cause unintended propagation of types between files. For example, if you open a sequence file with a version of a type that is higher than the version of the type currently in a type palette file, TestStand updates the type palette file and every file you subsequently open to use the higher version. The updated type propagates to other files without warning or notifying you. This behavior is the default behavior in TestStand 4.0.
 x 
 or earlier.
- AllowAutomaticTypeConflictResolutionOption_Never 
 –(Value: 3) Disallows all automatic type conflict resolution. When TestStand loads two different versions of a type, TestStand always prompts you or reports a type conflict error. When you select this option, opening files from TestStand versions earlier than the current version almost always results in type conflict prompts. Use this option only for debugging purposes or to ensure that all files have exactly the same version of every type.
- AllowAutomaticTypeConflictResolutionOption_OnlyIfATypePaletteFileHasTheHigherVersion 
 –(Value: 2) Includes the same restrictions as the Only if Type Palette Files will not be Modified (default) option, but also includes the restriction that the type must be in a type palette file for automatic type conflict resolution to occur. Effectively, this option allows automatic type conflict resolution only when a type palette file has the higher version of the type and a non-type palette file has the lower version of the type.

For example, this option does not allow automatic type conflict resolution between two sequence files for types that are not in type palette files, but the Only if Type Palette Files will not be Modified (default) option does allow this.
- AllowAutomaticTypeConflictResolutionOption_OnlyIfTypePaletteFilesWillNotBeModified 
 –(Value: 1) Disallows automatic type conflict resolution when the outcome of the resolution modifies a type palette file. This ensures that the application never uses a version of a type that is different than the version of the type in the type palette file without your explicit confirmation. This is the default behavior.

#### Purpose

Specifies how TestStand automatically resolves type conflicts. TestStand normally resolves type conflicts when TestStand loads a file with a version of a type that differs from the version of the type currently in memory and when the Use the definition that has the highest version number option on the
 [Version tab](../tsref/version-tab-type-properties-dialog-box.html)
 of the
 [Type Properties](../tsref/type-properties-dialog-box.html)
 dialog box or on the
 [Version tab](../tsref/version-tab-type-properties-dialog-box.html)
 of the Step
 [Type Properties](../tsref/type-properties-dialog-box.html)
 dialog box is enabled for both versions of the type. In this case, TestStand updates the file with the lower version of the type to use the higher version.

#### See Also

[Step Type Properties dialog box](../tsref/step-type-properties-dialog-box.html)

[Type Properties dialog box](../tsref/type-properties-dialog-box.html)

Version tab of
 [Step Type Properties dialog box](../tsref/step-type-properties-dialog-box.html)

Version tab of
 [Type Properties dialog box](../tsref/type-properties-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-allowcancellingpreloadexpressi.html language=enus -->
## TOPIC 02628: StationOptions.AllowCancellingPreloadExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-allowcancellingpreloadexpressi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-allowcancellingpreloadexpressi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.AllowCancellingPreloadExpression Data Type String Purpose When this Boolean expression is empty or evaluates to True , the Preload Progress dialog box includes a Cancel button so users can cancel preloading files. When this property evaluates to False , the dialog box does not

### StationOptions.AllowCancellingPreloadExpression

#### Syntax

[StationOptions](stationoptions.html).AllowCancellingPreloadExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

When this Boolean expression is empty or evaluates to
 True
 , the Preload Progress dialog box includes a
 Cancel
 button so users can cancel preloading files. When this property evaluates to
 False
 , the dialog box does not contain a
 Cancel
 button to prevent users from cancelling preloading files.

#### Remarks

If you cancel preloading a file when you open a sequence file, the sequence file opens without preloading the code modules. If you cancel preloading files when you execute a sequence file, the execution does not initiate.

You can use the
 [CurrentUserHasPrivilege](../tsfundamentals/expression-functions.html)
 expression function to allow users to cancel preloading files based on privileges. For example, set this property to
 CurrentUserHasPrivilege(Priv_Terminate) || CurrentUserHasPrivilege(Priv_Abort)
 to allow users to cancel preloading files only when the user has terminate or abort
 [privileges](../tsref/user-and-group-privileges.html)
 .

This property only affects cancelling preloading files directly from the Preload Progress dialog box. If TestStand cannot find a file during preloading and launches a Find File dialog box, you can cancel the Find File dialog box to cancel preloading files regardless of the value of this property.

#### See Also

[StationOptions.PreloadProgressDelay](stationoptions-preloadprogressdelay.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-allowothermodels.html language=enus -->
## TOPIC 02629: StationOptions.AllowOtherModels

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-allowothermodels.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-allowothermodels.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.AllowOtherModels Data Type Boolean Purpose Specifies if sequence files can specify a process model file other than the current station model file. Remarks When you set this property to False , you can only load the following sequence files: Sequence files that do not specify a

### StationOptions.AllowOtherModels

#### Syntax

[StationOptions](stationoptions.html).AllowOtherModels

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if sequence files can specify a process model file other than the current station model file.

#### Remarks

When you set this property to
 False
 , you can only load the following sequence files:

- Sequence files that do not specify a process model file
- Sequence files that specify the current station model as their process model file

#### See Also

[SequenceFile.ModelOption](sequencefile-modeloption.html)

[StationOptions.StationModelSequenceFilePath](stationoptions-stationmodelsequencefilepath.html)

[StationOptions.UseStationModel](stationoptions-usestationmodel.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-allowsequencecallsfromremotema.html language=enus -->
## TOPIC 02630: StationOptions.AllowSequenceCallsFromRemoteMachine

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-allowsequencecallsfromremotema.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-allowsequencecallsfromremotema.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.AllowSequenceCallsFromRemoteMachine Data Type Boolean Purpose Specifies if a remote computer can run a sequence on the current station. See Also Engine.IsRemote StationOptions.AllowAllUsersAccessFromRemoteMachine StationOptions.ShowEngineTrayIconOnRemoteStations

### StationOptions.AllowSequenceCallsFromRemoteMachine

#### Syntax

[StationOptions](stationoptions.html).AllowSequenceCallsFromRemoteMachine

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if a remote computer can run a sequence on the current station.

#### See Also

[Engine.IsRemote](engine-isremote.html)

[StationOptions.AllowAllUsersAccessFromRemoteMachine](stationoptions-allowallusersaccessfromremotem.html)

[StationOptions.ShowEngineTrayIconOnRemoteStations](stationoptions-showenginetrayicononremotestat.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-alwaysgotocleanuponfailure.html language=enus -->
## TOPIC 02631: StationOptions.AlwaysGotoCleanupOnFailure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-alwaysgotocleanuponfailure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-alwaysgotocleanuponfailure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.AlwaysGotoCleanupOnFailure Data Type Boolean Purpose Overrides the Sequence.FailureAction property setting when this property is True . See Also Sequence.FailureAction SequenceContext.GotoCleanup

### StationOptions.AlwaysGotoCleanupOnFailure

#### Syntax

[StationOptions](stationoptions.html).AlwaysGotoCleanupOnFailure

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Overrides the
 [Sequence.FailureAction](sequence-failureaction.html)
 property setting when this property is
 True
 .

#### See Also

[Sequence.FailureAction](sequence-failureaction.html)

[SequenceContext.GotoCleanup](sequencecontext-gotocleanup.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-autocreatevariablelocation.html language=enus -->
## TOPIC 02632: StationOptions.AutoCreateVariableLocation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-autocreatevariablelocation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-autocreatevariablelocation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.AutoCreateVariableLocation Data Type AutoCreateVariableLocationOptions Use the following constants with this data type: AutoCreateVariableLocationOption_FileGlobals –(Value: 3) Use FileGlobals as the location. AutoCreateVariableLocationOption_Locals –(Value: 1) Use Locals as th

### StationOptions.AutoCreateVariableLocation

#### Syntax

[StationOptions](stationoptions.html).AutoCreateVariableLocation

#### Data Type

[AutoCreateVariableLocationOptions](autocreatevariablelocationoptions.html)

Use the following constants with this data type:

- AutoCreateVariableLocationOption_FileGlobals 
 –(Value: 3) Use FileGlobals as the location.
- AutoCreateVariableLocationOption_Locals 
 –(Value: 1) Use Locals as the location.
- AutoCreateVariableLocationOption_Parameters 
 –(Value: 2) Use Parameters as the location.
- AutoCreateVariableLocationOption_StationGlobals 
 –(Value: 4) Use StationGlobals as the location.

#### Purpose

Specifies the location where automatically generated variables are created.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-autologinsystemuser.html language=enus -->
## TOPIC 02633: StationOptions.AutoLoginSystemUser

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-autologinsystemuser.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-autologinsystemuser.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.AutoLoginSystemUser Data Type Boolean Purpose Specifies if the LoginLogout callback sequence uses the current user login for the operating system as the login for TestStand when first launching a user interface or sequence editor. Remarks If the user login for the operating sys

### StationOptions.AutoLoginSystemUser

#### Syntax

[StationOptions](stationoptions.html).AutoLoginSystemUser

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the LoginLogout callback sequence uses the current user login for the operating system as the login for TestStand when first launching a user interface or sequence editor.

#### Remarks

If the user login for the operating system does not exist in TestStand, the Login dialog box launches. If the user login for the operating system exists in TestStand, TestStand automatically logs in the user using the operating system login.

Note

#### See Also

[Engine.CallFrontEndCallbackEx](engine-callfrontendcallbackex.html)

[StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)

[StationOptions.RequireUserLogin](stationoptions-requireuserlogin.html)

[StationOptions.UserFilePath](stationoptions-userfilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-breakonsequencefailure.html language=enus -->
## TOPIC 02634: StationOptions.BreakOnSequenceFailure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-breakonsequencefailure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-breakonsequencefailure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.BreakOnSequenceFailure Data Type Boolean Purpose If this property is True , TestStand suspends an execution on sequence failure. If this property is False , TestStand suspends execution based on whether the ExecTypeMask_BreakOnSequenceFailure option is enabled for the execution

### StationOptions.BreakOnSequenceFailure

#### Syntax

[StationOptions](stationoptions.html).BreakOnSequenceFailure

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If this property is
 True
 , TestStand suspends an execution on sequence failure. If this property is
 False
 , TestStand suspends execution based on whether the ExecTypeMask_BreakOnSequenceFailure option is enabled for the execution.

#### Remarks

If a step in a process model sequence file causes the sequence to fail, TestStand only suspends the execution if tracing is enabled for the sequence or if a previous suspend occurred within the sequence context. TestStand also suspends an execution if the
 [SequenceContext.SequenceFailed](sequencecontext-sequencefailed.html)
 property is set during the execution of a step even when the step does not fail.

#### See Also

[ExecutionTypeMask](executiontypemask.html)

[SequenceContext.SequenceFailed](sequencecontext-sequencefailed.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-breakonstepfailure.html language=enus -->
## TOPIC 02635: StationOptions.BreakOnStepFailure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-breakonstepfailure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-breakonstepfailure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.BreakOnStepFailure Data Type Boolean Purpose If this property is True , TestStand suspends an execution for any step that fails. If this property is False , TestStand suspends execution based on whether the ExecTypeMask_BreakOnStepFailure option is enabled for the execution. Re

### StationOptions.BreakOnStepFailure

#### Syntax

[StationOptions](stationoptions.html).BreakOnStepFailure

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If this property is
 True
 , TestStand suspends an execution for any step that fails. If this property is
 False
 , TestStand suspends execution based on whether the
 ExecTypeMask_BreakOnStepFailure
 option is enabled for the execution.

#### Remarks

If a step in a process model sequence file fails, TestStand only suspends the execution if tracing is enabled for the sequence or if a previous suspend occurred within the sequence context.

#### See Also

[ExecutionTypeMask](executiontypemask.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-breakpointsenabled.html language=enus -->
## TOPIC 02636: StationOptions.BreakpointsEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-breakpointsenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-breakpointsenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.BreakpointsEnabled Data Type Boolean Purpose Specifies whether to stop on breakpoints in all executions. Remarks Set this property to True to stop on breakpoints. Set this property to False to ignore breakpoints. See Also StationOptions.TracingEnabled

### StationOptions.BreakpointsEnabled

#### Syntax

[StationOptions](stationoptions.html).BreakpointsEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to stop on breakpoints in all executions.

#### Remarks

Set this property to
 True
 to stop on breakpoints. Set this property to
 False
 to ignore breakpoints.

#### See Also

[StationOptions.TracingEnabled](stationoptions-tracingenabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-checkoutfileswhenedited.html language=enus -->
## TOPIC 02637: StationOptions.CheckOutFilesWhenEdited

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-checkoutfileswhenedited.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-checkoutfileswhenedited.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.CheckOutFilesWhenEdited Data Type Boolean Purpose Specifies if the sequence editor checks a file out from source code control when you attempt to modify the file in the sequence editor. Remarks The default value is True . If this property is True and a current workspace is spec

### StationOptions.CheckOutFilesWhenEdited

#### Syntax

[StationOptions](stationoptions.html).CheckOutFilesWhenEdited

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the sequence editor checks a file out from source code control when you attempt to modify the file in the sequence editor.

#### Remarks

The default value is
 True
 . If this property is
 True
 and a current workspace is specified when you attempt to edit a checked-in file, the sequence editor prompts you to check the file out from source code control. If this property is
 False
 , you can edit a read-only file in the sequence editor only when you enable the
 Allow Editing of Read-Only Files
 option in the sequence editor.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[StationOptions.CheckOutOnlySelectedFiles](stationoptions-checkoutonlyselectedfiles.html)

[StationOptions.PromptWhenAddingFilesToSC](stationoptions-promptwhenaddingfilestosc.html)

[StationOptions.UseDialogForCheckOut](stationoptions-usedialogforcheckout.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-checkoutonlyselectedfiles.html language=enus -->
## TOPIC 02638: StationOptions.CheckOutOnlySelectedFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-checkoutonlyselectedfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-checkoutonlyselectedfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.CheckOutOnlySelectedFiles Data Type Boolean Purpose Specifies if the sequence editor checks out only selected files in the workspace from source code control. Remarks A workspace file contains a list of project files, each project file contains a lists of sequence files, and a

### StationOptions.CheckOutOnlySelectedFiles

#### Syntax

[StationOptions](stationoptions.html).CheckOutOnlySelectedFiles

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the sequence editor checks out only selected files in the workspace from source code control.

#### Remarks

A workspace file contains a list of project files, each project file contains a lists of sequence files, and a sequence file can contain lists of code modules and other files. When you set this option to
 True
 , the sequence editor only displays the selected file, such as a project file, in the source code control dialog boxes. When this property is
 False
 , the sequence editor displays the selected item and all the items it contains in the source code control dialog boxes.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[StationOptions.CheckOutFilesWhenEdited](stationoptions-checkoutfileswhenedited.html)

[StationOptions.PromptWhenAddingFilesToSC](stationoptions-promptwhenaddingfilestosc.html)

[StationOptions.UseDialogForCheckOut](stationoptions-usedialogforcheckout.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-debugoptions.html language=enus -->
## TOPIC 02639: StationOptions.DebugOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-debugoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-debugoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.DebugOptions Data Type Long Purpose Specifies the type of debug features that TestStand performs. Specify one or more DebugOptions constants. Use the bitwise-OR operator to specify multiple options. See Also DebugOptions

### StationOptions.DebugOptions

#### Syntax

[StationOptions](stationoptions.html).DebugOptions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the type of debug features that TestStand performs. Specify one or more
 [DebugOptions](debugoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options.

#### See Also

[DebugOptions](debugoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-defaultcpuaffinityforthreads.html language=enus -->
## TOPIC 02640: StationOptions.DefaultCPUAffinityForThreads

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-defaultcpuaffinityforthreads.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-defaultcpuaffinityforthreads.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.DefaultCPUAffinityForThreads Data Type Long Purpose This property is obsolete. Use the StationOptions.DefaultCPUAffinityForThreadsEx property instead. Getting this property on a 64-bit instance of the TestStand Engine results in an error. Setting this property on 32-bit archite

### StationOptions.DefaultCPUAffinityForThreads

#### Syntax

[StationOptions](stationoptions.html).DefaultCPUAffinityForThreads

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.DefaultCPUAffinityForThreadsEx

#### Remarks

Specifies which CPUs to use for threads TestStand creates and the user interface thread.

This property is a number in which each bit represents a CPU. The lowest-order bit represents the first CPU. For example, a value of
 12
 , which is
 1100
 in binary, represents CPUs 3 and 4 on a quad-core computer. A value of
 -1
 specifies to use all CPUs available to the process.

TestStand does not update the CPU affinity of threads for currently executing sequences when you change this property.

Refer to
 [Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)
 for more information about optimizing TestStand performance on symmetric multiprocessing (SMP) systems for multithreaded applications.

#### See Also

[SequenceCallModule.CPUAffinityForNewThreadOption](sequencecallmodule-cpuaffinityfornewthreadopt.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Obsolete StationOptions Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-defaultcpuaffinityforthreadsex.html language=enus -->
## TOPIC 02641: StationOptions.DefaultCPUAffinityForThreadsEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-defaultcpuaffinityforthreadsex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-defaultcpuaffinityforthreadsex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.DefaultCPUAffinityForThreadsEx Data Type unsigned long long Purpose Specifies which CPUs to use for threads TestStand creates and the user interface thread. Remarks This property is a number in which each bit represents a CPU. The lowest-order bit represents the first CPU. For

### StationOptions.DefaultCPUAffinityForThreadsEx

#### Syntax

[StationOptions](stationoptions.html).DefaultCPUAffinityForThreadsEx

#### Data Type

[unsigned long long](data-types-for-teststand.html)

#### Purpose

Specifies which CPUs to use for threads TestStand creates and the user interface thread.

#### Remarks

This property is a number in which each bit represents a CPU. The lowest-order bit represents the first CPU. For example, a value of
 12
 , which is
 1100
 in binary, represents CPUs 3 and 4 on a quad-core computer. A value of
 -1
 specifies to use all CPUs available to the process.

TestStand does not update the CPU affinity of threads for currently executing sequences when you change this property.

Refer to
 [Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)
 for more information about optimizing TestStand performance on symmetric multiprocessing (SMP) systems for multithreaded applications.

#### See Also

[SequenceCallModule.CPUAffinityForNewThreadOption](sequencecallmodule-cpuaffinityfornewthreadopt.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-defaultfilewritingformat.html language=enus -->
## TOPIC 02642: StationOptions.DefaultFileWritingFormat

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-defaultfilewritingformat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-defaultfilewritingformat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.DefaultFileWritingFormat Data Type FileWritingFormats Use the following constants with this data type: FileWritingFormat_Binary –(Value: 2) Specifies that TestStand writes the file in a binary format. This format is the fastest and most memory-efficient format. FileWritingForma

### StationOptions.DefaultFileWritingFormat

#### Syntax

[StationOptions](stationoptions.html).DefaultFileWritingFormat

#### Data Type

[FileWritingFormats](filewritingformats.html)

Use the following constants with this data type:

- FileWritingFormat_Binary 
 –(Value: 2) Specifies that TestStand writes the file in a binary format. This format is the fastest and most memory-efficient format.
- FileWritingFormat_Ini 
 –(Value: 1) Specifies that TestStand writes the file in an INI format. This format is used by previous versions of TestStand (3.
 x 
 or earlier). Use this format when necessary to support existing code that reads the INI file directly.
 Note 
 The INI format is deprecated in TestStand 2019 and may not be supported in future releases.
- FileWritingFormat_Xml 
 –(Value: 3) Specifies that TestStand writes the file in an XML format. Use this format if you want to read, parse, or create files as XML. This option is the most readable and parseable format.

#### Purpose

Specifies the format in which TestStand writes new files.

#### Remarks

Attempting to set to INI (or any other unsupported value) will throw an exception.

#### See Also

[PropertyObjectFile.FileWritingFormat](propertyobjectfile-filewritingformat.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-disableresults.html language=enus -->
## TOPIC 02643: StationOptions.DisableResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-disableresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-disableresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.DisableResults Data Type Boolean Purpose Specifies whether to disable recording of results for all steps. Remarks When this property is True , TestStand does not record results for steps. When this property is False , TestStand records results based on the setting of the Step.R

### StationOptions.DisableResults

#### Syntax

[StationOptions](stationoptions.html).DisableResults

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to disable recording of results for all steps.

#### Remarks

When this property is
 True
 , TestStand does not record results for steps. When this property is
 False
 , TestStand records results based on the setting of the
 [Step.ResultRecordingOption](step-resultrecordingoption.html)
 property of each individual step or based on the
 [Sequence.DisableResults](sequence-disableresults.html)
 property and the
 [Execution.DisableResults](execution-disableresults.html)
 property.

Note

#### See Also

[Execution.DisableResults](execution-disableresults.html)

[Sequence.DisableResults](sequence-disableresults.html)

[Step.ResultRecordingOption](step-resultrecordingoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-enableuserprivilegechecking.html language=enus -->
## TOPIC 02644: StationOptions.EnableUserPrivilegeChecking

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-enableuserprivilegechecking.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-enableuserprivilegechecking.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.EnableUserPrivilegeChecking Data Type Boolean Purpose Specifies whether the sequence editor or user interface verify user privileges. Remarks When this property is False , the sequence editor or user interface do not verify that the user has the privileges necessary for perform

### StationOptions.EnableUserPrivilegeChecking

#### Syntax

[StationOptions](stationoptions.html).EnableUserPrivilegeChecking

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether the sequence editor or user interface verify user privileges.

#### Remarks

When this property is
 False
 , the sequence editor or user interface do not verify that the user has the privileges necessary for performing specific operations. Instead, all operations that depend on user privileges are always available.

#### See Also

[Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)

[StationOptions.AutoLoginSystemUser](stationoptions-autologinsystemuser.html)

[StationOptions.RequireUserLogin](stationoptions-requireuserlogin.html)

[StationOptions.UserFilePath](stationoptions-userfilepath.html)

[User.HasPrivilege](user-hasprivilege.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-executionmask.html language=enus -->
## TOPIC 02645: StationOptions.ExecutionMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-executionmask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-executionmask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.ExecutionMask Data Type Long Purpose Specifies execution options. Remarks Specifies the execution options using ExecutionMask constants. To specify multiple execution options, use the bitwise-OR operator. See Also Engine.NewExecution ExecutionMask

### StationOptions.ExecutionMask

#### Syntax

[StationOptions](stationoptions.html).ExecutionMask

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies execution options.

#### Remarks

Specifies the execution options using
 [ExecutionMask](executionmask.html)
 constants. To specify multiple execution options, use the bitwise-OR operator.

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[ExecutionMask](executionmask.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-filemodificationindicatorpolic.html language=enus -->
## TOPIC 02646: StationOptions.FileModificationIndicatorPolicy

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-filemodificationindicatorpolic.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-filemodificationindicatorpolic.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.FileModificationIndicatorPolicy Data Type Long Purpose Specifies the policy for when to indicate that a file being opened is modified. When you open a file, TestStand must modify the file in memory when a version of a type defined in the file is updated as a result of an automa

### StationOptions.FileModificationIndicatorPolicy

#### Syntax

[StationOptions](stationoptions.html).FileModificationIndicatorPolicy

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the policy for when to indicate that a file being opened is modified. When you open a file, TestStand must modify the file in memory when a version of a type defined in the file is updated as a result of an automatic type conflict resolution, or if the data format of the file changes as a result of opening the file in a newer version of TestStand. In such cases, TestStand modifies the file in memory even if the policy specifies not to indicate that the file is modified.

Specify one or more
 [FileModificationIndicatorPolicies](filemodificationindicatorpolicies.html)
 constants. Use the bitwise-OR operator to specify multiple policies.

#### See Also

[FileModificationIndicatorPolicies](filemodificationindicatorpolicies.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-getlanguages.html language=enus -->
## TOPIC 02647: StationOptions.GetLanguages

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-getlanguages.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-getlanguages.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.GetLanguages Return Value String Array Purpose Obtains a list of languages TestStand supports. Remarks This method obtains an array of strings containing the list of directories that correspond to the possible language configurations supported. See Also StationOptions.Language

### StationOptions.GetLanguages

#### Syntax

[StationOptions](stationoptions.html).GetLanguages

#### Return Value

[String Array](data-types-for-teststand.html)

#### Purpose

Obtains a list of languages TestStand supports.

#### Remarks

This method obtains an array of strings containing the list of directories that correspond to the possible language configurations supported.

#### See Also

[StationOptions.Language](stationoptions-language.html)

[StationOptions.RecognizeMBChars](stationoptions-recognizembchars.html)

[StationOptions.UseLocalizedDecimalPoint](stationoptions-uselocalizeddecimalpoint.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-gettimelimit.html language=enus -->
## TOPIC 02648: StationOptions.GetTimeLimit

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-gettimelimit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-gettimelimit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.GetTimeLimit( type, operation) Return Value Double Returns the time limit in seconds. Purpose Returns the time limit value in seconds for a specific type of time limit and operation. Remarks TestStand maintains a set of time limit settings that determine whether TestStand takes

### StationOptions.GetTimeLimit

#### Syntax

[StationOptions](stationoptions.html).GetTimeLimit( type, operation)

#### Return Value

[Double](data-types-for-teststand.html)

Returns the time limit in seconds.

#### Purpose

Returns the time limit value in seconds for a specific type of time limit and operation.

#### Remarks

TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an execution state does not change for a specified amount of time. For example, TestStand could attempt to abort an execution if a terminating execution takes longer than 10 seconds to shut down.

TestStand maintains unique time limit settings for normal executions and for executions that run while the engine is exiting. For each type of execution, TestStand maintains different time limit settings for aborting, executing, and terminating executions.

#### Parameters

type
 As
 [TimeLimitTypes](timelimittypes.html)

[In] Specifies the type of time limit for the setting the method returns.

operation
 As
 [TimeLimitOperations](timelimitoperations.html)

[In] Specifies the operation type for the setting that the method returns.

#### See Also

[StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)

[StationOptions.GetTimeLimitEnabled](stationoptions-gettimelimitenabled.html)

[StationOptions.SetTimeLimit](stationoptions-settimelimit.html)

[TimeLimitOperations](timelimitoperations.html)

[TimeLimitTypes](timelimittypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-gettimelimitaction.html language=enus -->
## TOPIC 02649: StationOptions.GetTimeLimitAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-gettimelimitaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-gettimelimitaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.GetTimeLimitAction( type, operation) Return Value TimeLimitActions Use the following constants with this data type: TimeLimitAction_Abort –(Value: 0) Initiates an abort of a running execution. TimeLimitAction_KillThreads –(Value: 1) Ends the thread for a running, terminating, o

### StationOptions.GetTimeLimitAction

#### Syntax

[StationOptions](stationoptions.html).GetTimeLimitAction( type, operation)

#### Return Value

[TimeLimitActions](timelimitactions.html)

Use the following constants with this data type:

- TimeLimitAction_Abort 
 –(Value: 0) Initiates an abort of a running execution.
- TimeLimitAction_KillThreads 
 –(Value: 1) Ends the thread for a running, terminating, or aborting execution.
- TimeLimitAction_Prompt 
 –(Value: 2) Launches a dialog box with the option to terminate, abort, or kill the execution.
- TimeLimitAction_Terminate 
 –(Value: 3) Initiates a termination of a running execution.

Returns the action TestStand takes when the time limit expires.

#### Purpose

Returns the action for a specific type of time limit and operation TestStand takes if the time limit expires.

#### Remarks

TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an execution state does not change for a specified amount of time. For example, TestStand could attempt to abort an execution if, while TestStand is attempting to shut down, a terminating execution takes longer than 10 seconds.

TestStand maintains unique time limit settings for normal executions and for executions that run while the engine is exiting. For each type of execution, TestStand maintains different time limit settings for when an execution is aborting, executing, and terminating.

Note

TimeLimitAction_Prompt

#### Parameters

type
 As
 [TimeLimitTypes](timelimittypes.html)

[In] Specifies the type of time limit for the setting the method returns.

operation
 As
 [TimeLimitOperations](timelimitoperations.html)

[In] Specifies the operation type for the setting the method returns.

#### See Also

[StationOptions.GetTimeLimit](stationoptions-gettimelimit.html)

[StationOptions.GetTimeLimitEnabled](stationoptions-gettimelimitenabled.html)

[StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)

[TimeLimitOperations](timelimitoperations.html)

[TimeLimitTypes](timelimittypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-gettimelimitenabled.html language=enus -->
## TOPIC 02650: StationOptions.GetTimeLimitEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-gettimelimitenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-gettimelimitenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.GetTimeLimitEnabled( type, operation) Return Value Boolean Returns a value that indicates whether the time limit is enabled. Purpose Returns a value that indicates whether a time limit for an execution is enabled for a specific type of time limit and operation. Remarks TestStan

### StationOptions.GetTimeLimitEnabled

#### Syntax

[StationOptions](stationoptions.html).GetTimeLimitEnabled( type, operation)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the time limit is enabled.

#### Purpose

Returns a value that indicates whether a time limit for an execution is enabled for a specific type of time limit and operation.

#### Remarks

TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an execution state does not change for a specified amount of time. For example, TestStand could attempt to abort an execution if, while TestStand is attempting to shut down, a terminating execution takes longer than 10 seconds.

TestStand maintains unique time limit settings for normal executions and for executions that run while the engine is exiting. For each type of execution, TestStand maintains different time limit settings for when an execution is aborting, executing, and terminating.

#### Parameters

type
 As
 [TimeLimitTypes](timelimittypes.html)

[In] Specifies the type of time limit for the setting the method returns.

operation
 As
 [TimeLimitOperations](timelimitoperations.html)

[In] Specifies the operation type for the setting the method returns.

#### See Also

[StationOptions.GetTimeLimit](stationoptions-gettimelimit.html)

[StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)

[StationOptions.SetTimeLimitEnabled](stationoptions-settimelimitenabled.html)

[TimeLimitOperations](timelimitoperations.html)

[TimeLimitTypes](timelimittypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-interactivebranchmode.html language=enus -->
## TOPIC 02651: StationOptions.InteractiveBranchMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-interactivebranchmode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-interactivebranchmode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.InteractiveBranchMode Data Type InteractiveBranchModes Use the following constants with this data type: InteractiveBranchMode_AllowAll –(Value: 4) The interactive execution allows branching to selected and non-selected steps. When TestStand executes a selected step and no branc

### StationOptions.InteractiveBranchMode

#### Syntax

[StationOptions](stationoptions.html).InteractiveBranchMode

#### Data Type

[InteractiveBranchModes](interactivebranchmodes.html)

Use the following constants with this data type:

- InteractiveBranchMode_AllowAll 
 –(Value: 4) The interactive execution allows branching to selected and non-selected steps. When TestStand executes a selected step and no branch occurs, the next step is the next selected step. When TestStand executes a non-selected step and no branch occurs, the next step is the step after the non-selected step.
- InteractiveBranchMode_GotoEnd 
 –(Value: 2) The interactive execution allows branching within selected steps. All branches to non-selected steps automatically go to the end step and start the next interactive loop iteration, if specified.
- InteractiveBranchMode_Ignore 
 –(Value: 1) The interactive execution allows branching within the selected steps, and all branching to non-selected steps is ignored.
- InteractiveBranchMode_None 
 –(Value: 0) The interactive execution ignores all branches and executes selected steps in the order the sequence editor or user interface specifies.
- InteractiveBranchMode_RaiseRTE 
 –(Value: 3) The interactive execution allows branching within selected steps. All branches to non-selected steps cause a run-time error. If enabled, the
 Run-Time Error 
 dialog box launches.

#### Purpose

Specifies the action TestStand takes when executing a Goto step or evaluating a post action that specifies a new destination step while running in an interactive execution.

#### See Also

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-interactiveexepropagatestatus.html language=enus -->
## TOPIC 02652: StationOptions.InteractiveExePropagateStatus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-interactiveexepropagatestatus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-interactiveexepropagatestatus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.InteractiveExePropagateStatus Data Type Boolean Purpose Specifies if TestStand allows sequence failure, Goto cleanup, and error settings from a nested interactive execution to propagate to the invoking execution. Remarks When this property is False , TestStand saves the values

### StationOptions.InteractiveExePropagateStatus

#### Syntax

[StationOptions](stationoptions.html).InteractiveExePropagateStatus

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if TestStand allows sequence failure, Goto cleanup, and error settings from a nested interactive execution to propagate to the invoking execution.

#### Remarks

When this property is
 False
 , TestStand saves the values of the
 [SequenceContext.SequenceFailed](sequencecontext-sequencefailed.html)
 ,
 [SequenceContext.GotoCleanup](sequencecontext-gotocleanup.html)
 , and
 [SequenceContext.SequenceErrorOccurred](sequencecontext-sequenceerroroccurred.html)
 properties before executing a nested interactive execution, and restores the values after executing a nested interactive execution. When this property is
 True
 , TestStand allows the nested interactive execution changes to affect the execution that invokes the nested interactive execution.

#### See Also

[SequenceContext.GotoCleanup](sequencecontext-gotocleanup.html)

[SequenceContext.SequenceErrorOccurred](sequencecontext-sequenceerroroccurred.html)

[SequenceContext.SequenceFailed](sequencecontext-sequencefailed.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-language.html language=enus -->
## TOPIC 02653: StationOptions.Language

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-language.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-language.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.Language Data Type String Purpose Specifies the language TestStand uses to display text. Remarks Changes to this property do not take effect until the next time you start the engine or call the Engine.ReloadStringResourceFiles method. See Also Engine.ReloadStringResourceFiles S

### StationOptions.Language

#### Syntax

[StationOptions](stationoptions.html).Language

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the language TestStand uses to display text.

#### Remarks

Changes to this property do not take effect until the next time you start the engine or call the
 [Engine.ReloadStringResourceFiles](engine-reloadstringresourcefiles.html)
 method.

#### See Also

[Engine.ReloadStringResourceFiles](engine-reloadstringresourcefiles.html)

[StationOptions.GetLanguages](stationoptions-getlanguages.html)

[StationOptions.RecognizeMBChars](stationoptions-recognizembchars.html)

[StationOptions.UseLocalizedDecimalPoint](stationoptions-uselocalizeddecimalpoint.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-loginonstart.html language=enus -->
## TOPIC 02654: StationOptions.LoginOnStart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-loginonstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-loginonstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.LoginOnStart Data Type Boolean Purpose When this property is True and the ApplicationMgr.LoginOnStart property is True , the LoginLogout Front-End callback sequence runs when you call the ApplicationMgr.Start method.

### StationOptions.LoginOnStart

#### Syntax

[StationOptions](stationoptions.html).LoginOnStart

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

When this property is
 True
 and the
 
 [ApplicationMgr.LoginOnStart](../tsuiref/applicationmgr-loginonstart.html)
 property is
 True
 , the LoginLogout Front-End callback sequence runs when you call the
 
 [ApplicationMgr.Start](../tsuiref/applicationmgr-start.html)
 method.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-preloadprogressdelay.html language=enus -->
## TOPIC 02655: StationOptions.PreloadProgressDelay

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-preloadprogressdelay.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-preloadprogressdelay.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.PreloadProgressDelay Data Type Double Purpose Specifies the delay in seconds before the Preload Progress dialog box launches while preloading code modules. Specify a negative value to disable the Preload Progress dialog box but continue to preload code modules. See Also Executi

### StationOptions.PreloadProgressDelay

#### Syntax

[StationOptions](stationoptions.html).PreloadProgressDelay

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Specifies the delay in seconds before the
 [Preload Progress](../tsref/preload-progress-dialog-box.html)
 dialog box launches while preloading code modules. Specify a negative value to disable the Preload Progress dialog box but continue to preload code modules.

#### See Also

[ExecutionTypeMask](executiontypemask.html)

[GetSeqFileOptions](getseqfileoptions.html)

[Preload Progress dialog box](../tsref/preload-progress-dialog-box.html)

[StationOptions.AllowCancellingPreloadExpression](stationoptions-allowcancellingpreloadexpressi.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-prompttofindfiles.html language=enus -->
## TOPIC 02656: StationOptions.PromptToFindFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-prompttofindfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-prompttofindfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.PromptToFindFiles Data Type Boolean Purpose Specifies if TestStand launches a File dialog box when it cannot find the necessary files in the current search directory paths .

### StationOptions.PromptToFindFiles

#### Syntax

[StationOptions](stationoptions.html).PromptToFindFiles

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if TestStand launches a File dialog box when it cannot find the necessary files in the current
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-promptwhenaddingfilestosc.html language=enus -->
## TOPIC 02657: StationOptions.PromptWhenAddingFilesToSC

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-promptwhenaddingfilestosc.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-promptwhenaddingfilestosc.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.PromptWhenAddingFilesToSC Data Type Boolean Purpose Specifies if the sequence editor prompts you to add files to source code control when you add files to a workspace. Remarks When this option is True and a current workspace file is specified, the sequence editor launches a dia

### StationOptions.PromptWhenAddingFilesToSC

#### Syntax

[StationOptions](stationoptions.html).PromptWhenAddingFilesToSC

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the sequence editor prompts you to add files to source code control when you add files to a workspace.

#### Remarks

When this option is
 True
 and a current workspace file is specified, the sequence editor launches a dialog box, in which you can add files to source code control whenever you add them to a workspace file. When this option is
 False
 , the sequence editor does not launch a dialog box.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[StationOptions.CheckOutFilesWhenEdited](stationoptions-checkoutfileswhenedited.html)

[StationOptions.CheckOutOnlySelectedFiles](stationoptions-checkoutonlyselectedfiles.html)

[StationOptions.UseDialogForCheckOut](stationoptions-usedialogforcheckout.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-recognizembchars.html language=enus -->
## TOPIC 02658: StationOptions.RecognizeMBChars

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-recognizembchars.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-recognizembchars.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.RecognizeMBChars Data Type Boolean Purpose Indicates whether TestStand recognizes extended character code sequences when it compares and processes strings. Remarks The TestStand Engine determines this based on the current system code page at launch. As of TestStand 2019, this p

### StationOptions.RecognizeMBChars

#### Syntax

[StationOptions](stationoptions.html).RecognizeMBChars

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates whether TestStand recognizes extended character code sequences when it compares and processes strings.

#### Remarks

The TestStand Engine determines this based on the current system code page at launch.

Note

#### See Also

[StationOptions.GetLanguages](stationoptions-getlanguages.html)

[StationOptions.Language](stationoptions-language.html)

[StationOptions.UseLocalizedDecimalPoint](stationoptions-uselocalizeddecimalpoint.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-reloaddocswhenopeningworkspace.html language=enus -->
## TOPIC 02659: StationOptions.ReloadDocsWhenOpeningWorkspace

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-reloaddocswhenopeningworkspace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-reloaddocswhenopeningworkspace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.ReloadDocsWhenOpeningWorkspace Data Type Boolean Purpose Specifies if the sequence editor opens the documents that were open when the workspace was unloaded. Remarks When this property is True and you open a workspace file, the sequence editor opens the documents that were open

### StationOptions.ReloadDocsWhenOpeningWorkspace

#### Syntax

[StationOptions](stationoptions.html).ReloadDocsWhenOpeningWorkspace

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the sequence editor opens the documents that were open when the workspace was unloaded.

#### Remarks

When this property is
 True
 and you open a workspace file, the sequence editor opens the documents that were open when the workspace file was last closed.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[StationOptions.ReloadWorkspaceAtStartup](stationoptions-reloadworkspaceatstartup.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-reloadworkspaceatstartup.html language=enus -->
## TOPIC 02660: StationOptions.ReloadWorkspaceAtStartup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-reloadworkspaceatstartup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-reloadworkspaceatstartup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.ReloadWorkspaceAtStartup Data Type Boolean Purpose Specifies if the sequence editor opens the last workspace file loaded when it launches. Remarks If this option is True when the sequence editor launches, the sequence editor loads the workspace file the Engine.LastWorkspacePath

### StationOptions.ReloadWorkspaceAtStartup

#### Syntax

[StationOptions](stationoptions.html).ReloadWorkspaceAtStartup

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the sequence editor opens the last workspace file loaded when it launches.

#### Remarks

If this option is
 True
 when the sequence editor launches, the sequence editor loads the workspace file the
 [Engine.LastWorkspacePath](engine-lastworkspacepath.html)
 property specifies.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[Engine.LastWorkspacePath](engine-lastworkspacepath.html)

[StationOptions.ReloadDocsWhenOpeningWorkspace](stationoptions-reloaddocswhenopeningworkspace.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-requireuserlogin.html language=enus -->
## TOPIC 02661: StationOptions.RequireUserLogin

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-requireuserlogin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-requireuserlogin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.RequireUserLogin Data Type Boolean Purpose Specifies if the sequence editor or user interfaces require that a user be logged in. Remarks TestStand only uses this property when the StationOptions.EnableUserPrivilegeChecking property is False . When this property is True , the us

### StationOptions.RequireUserLogin

#### Syntax

[StationOptions](stationoptions.html).RequireUserLogin

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the sequence editor or user interfaces require that a user be logged in.

#### Remarks

TestStand only uses this property when the
 [StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)
 property is
 False
 . When this property is
 True
 , the user interfaces are disabled until a user successfully logs in.

#### See Also

[StationOptions.AutoLoginSystemUser](stationoptions-autologinsystemuser.html)

[StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)

[StationOptions.UserFilePath](stationoptions-userfilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-rteoption.html language=enus -->
## TOPIC 02662: StationOptions.RTEOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-rteoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-rteoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.RTEOption Data Type RTEOptions Use the following constants with this data type: RTEOption_Abort –(Value: 3) Instructs the execution to abort the execution. RTEOption_Continue –(Value: 1) Instructs the execution to process the error by propagating the error to the calling sequen

### StationOptions.RTEOption

#### Syntax

[StationOptions](stationoptions.html).RTEOption

#### Data Type

[RTEOptions](rteoptions.html)

Use the following constants with this data type:

- RTEOption_Abort 
 –(Value: 3) Instructs the execution to abort the execution.
- RTEOption_Continue 
 –(Value: 1) Instructs the execution to process the error by propagating the error to the calling sequence, if one exists. If the current step group is Setup or Main, the execution jumps directly to the Cleanup step group.
- RTEOption_Ignore 
 –(Value: 2) Instructs the execution to ignore the error and continue normal execution.
- RTEOption_Retry 
 –(Value: 4) Instructs the execution to ignore the error and re-execute the step that caused the error condition. For the
 StationOptions.RTEOption 
 property, the
 Execution.RTEOptionForThisExecution 
 property, and the
 Thread.SetBatchRTEOption 
 method, TestStand interprets the
 RTEOption_Retry 
 value as
 RTEOption_Continue 
 .
- RTEOption_ShowDialog 
 –(Value: 0) Instructs the execution to launch the
 Run-Time Error 
 dialog box when an error occurs.

#### Purpose

Specifies the default behavior of TestStand when a run-time error occurs in an execution.

#### Remarks

This property replaced the more limited property
 Engine.BreakOnRTE
 and offers a superset of the functionality.

#### See Also

[Engine.DisplayRunTimeErrorDialogEx](engine-displayruntimeerrordialogex.html)

[Execution.RTEOptionForThisExecution](execution-rteoptionforthisexecution.html)

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[StationOptions.RTEOption](stationoptions-rteoption.html)

[Thread.SetBatchRTEOption](thread-setbatchrteoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-seqfileversionautoincrementopt.html language=enus -->
## TOPIC 02663: StationOptions.SeqFileVersionAutoIncrementOpt

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-seqfileversionautoincrementopt.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-seqfileversionautoincrementopt.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.SeqFileVersionAutoIncrementOpt Data Type FileVersionAutoIncrement Use the following constants with this data type: FileVersionInc_Build –(Value: 4) Specifies that the build version number is incremented. FileVersionInc_Major –(Value: 1) Specifies that the major version number i

### StationOptions.SeqFileVersionAutoIncrementOpt

#### Syntax

[StationOptions](stationoptions.html).SeqFileVersionAutoIncrementOpt

#### Data Type

[FileVersionAutoIncrement](fileversionautoincrement.html)

Use the following constants with this data type:

- FileVersionInc_Build 
 –(Value: 4) Specifies that the build version number is incremented.
- FileVersionInc_Major 
 –(Value: 1) Specifies that the major version number is incremented.
- FileVersionInc_Minor 
 –(Value: 2) Specifies that the minor version number is incremented.
- FileVersionInc_None 
 –(Value: 0) Specifies that sequence file versions are not automatically incremented.
- FileVersionInc_Revision 
 –(Value: 3) Specifies that the revision version number is incremented.

#### Purpose

Specifies if sequence file versions are automatically incremented when the file is saved.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-settimelimit.html language=enus -->
## TOPIC 02664: StationOptions.SetTimeLimit

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-settimelimit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-settimelimit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.SetTimeLimit( type, operation, timeLimit) Purpose Specifies the time limit value in seconds for a specific type of time limit operation. Remarks TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an execution state does not ch

### StationOptions.SetTimeLimit

#### Syntax

[StationOptions](stationoptions.html).SetTimeLimit( type, operation, timeLimit)

#### Purpose

Specifies the time limit value in seconds for a specific type of time limit operation.

#### Remarks

TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an execution state does not change for a specified amount of time. For example, TestStand could attempt to abort an execution if, while TestStand is attempting to shut down, a terminating execution takes longer than 10 seconds.

TestStand maintains unique time limit settings for normal executions and for executions that run while the engine is exiting. For each type of execution, TestStand maintains different time limit settings for when an execution is aborting, executing, and terminating.

#### Parameters

type
 As
 [TimeLimitTypes](timelimittypes.html)

[In] Specifies the type of time limit for the setting the method sets.

operation
 As
 [TimeLimitOperations](timelimitoperations.html)

[In] Specifies the operation type for the setting the method sets.

timeLimit
 As
 [Double](data-types-for-teststand.html)

[In] Specifies the time limit in seconds.

#### See Also

[StationOptions.GetTimeLimit](stationoptions-gettimelimit.html)

[StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)

[StationOptions.SetTimeLimitEnabled](stationoptions-settimelimitenabled.html)

[TimeLimitOperations](timelimitoperations.html)

[TimeLimitTypes](timelimittypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-settimelimitaction.html language=enus -->
## TOPIC 02665: StationOptions.SetTimeLimitAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-settimelimitaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-settimelimitaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.SetTimeLimitAction( type, operation, action) Purpose Specifies an action for a specific type of time limit and operation TestStand takes if the time limit expires. Remarks TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an

### StationOptions.SetTimeLimitAction

#### Syntax

[StationOptions](stationoptions.html).SetTimeLimitAction( type, operation, action)

#### Purpose

Specifies an action for a specific type of time limit and operation TestStand takes if the time limit expires.

#### Remarks

TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an execution state does not change for a specified amount of time. For example, TestStand could attempt to abort an execution if, while TestStand is attempting to shut down, a terminating execution takes longer than 10 seconds.

TestStand maintains unique time limit settings for normal executions and for executions that run while the engine is exiting. For each type of execution, TestStand maintains different time limit settings for when an execution is aborting, executing, and terminating.

Note

StationOptions.SetTimeLimitEnabled

TimeLimitAction_Prompt

#### Parameters

type
 As
 [TimeLimitTypes](timelimittypes.html)

[In] Specifies the type of time limit for the setting the method sets.

operation
 As
 [TimeLimitOperations](timelimitoperations.html)

[In] Specifies the operation type for the setting the method sets.

action
 As
 [TimeLimitActions](timelimitactions.html)

[In] Specifies the action TestStand takes when the time limit expires.

#### See Also

[StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)

[StationOptions.SetTimeLimit](stationoptions-settimelimit.html)

[StationOptions.SetTimeLimitEnabled](stationoptions-settimelimitenabled.html)

[TimeLimitActions](timelimitactions.html)

[TimeLimitOperations](timelimitoperations.html)

[TimeLimitTypes](timelimittypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-settimelimitenabled.html language=enus -->
## TOPIC 02666: StationOptions.SetTimeLimitEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-settimelimitenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-settimelimitenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.SetTimeLimitEnabled( type, operation, enabled) Purpose Specifies whether a time limit for an execution is enabled for a specific type of time limit and operation. Remarks TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an e

### StationOptions.SetTimeLimitEnabled

#### Syntax

[StationOptions](stationoptions.html).SetTimeLimitEnabled( type, operation, enabled)

#### Purpose

Specifies whether a time limit for an execution is enabled for a specific type of time limit and operation.

#### Remarks

TestStand maintains a set of time limit settings that determine whether TestStand takes an action when an execution state does not change for a specified amount of time. For example, TestStand could attempt to abort an execution if, while TestStand is attempting to shut down, a terminating execution takes longer than 10 seconds.

TestStand maintains unique time limit settings for normal executions and for executions that run while the engine is exiting. For each type of execution, TestStand maintains different time limit settings for when an execution is aborting, executing, and terminating.

#### Parameters

type
 As
 [TimeLimitTypes](timelimittypes.html)

[In] Specifies the type of time limit for the setting the method sets.

operation
 As
 [TimeLimitOperations](timelimitoperations.html)

[In] Specifies the operation type for the setting the method sets.

enabled
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies if the time limit is enabled.

#### See Also

[StationOptions.GetTimeLimitEnabled](stationoptions-gettimelimitenabled.html)

[StationOptions.SetTimeLimit](stationoptions-settimelimit.html)

[StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)

[TimeLimitOperations](timelimitoperations.html)

[TimeLimitTypes](timelimittypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-showenginetrayicononremotestat.html language=enus -->
## TOPIC 02667: StationOptions.ShowEngineTrayIconOnRemoteStations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-showenginetrayicononremotestat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-showenginetrayicononremotestat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.ShowEngineTrayIconOnRemoteStations Data Type Boolean Purpose Specifies whether to show the system tray icon when the TestStand remote engine is active on this computer. See Also Engine.MasterEngine StationOptions.AllowAllUsersAccessFromRemoteMachine StationOptions.AllowSequence

### StationOptions.ShowEngineTrayIconOnRemoteStations

#### Syntax

[StationOptions](stationoptions.html).ShowEngineTrayIconOnRemoteStations

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to show the system tray icon when the TestStand remote engine is active on this computer.

#### See Also

[Engine.MasterEngine](engine-masterengine.html)

[StationOptions.AllowAllUsersAccessFromRemoteMachine](stationoptions-allowallusersaccessfromremotem.html)

[StationOptions.AllowSequenceCallsFromRemoteMachine](stationoptions-allowsequencecallsfromremotema.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-showhiddenproperties.html language=enus -->
## TOPIC 02668: StationOptions.ShowHiddenProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-showhiddenproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-showhiddenproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.ShowHiddenProperties Data Type Boolean Purpose Specifies whether to display in user interfaces properties marked as hidden. Remarks When this property is True , TestStand applications display all the subproperties of property objects in dialog boxes and variables views. When th

### StationOptions.ShowHiddenProperties

#### Syntax

[StationOptions](stationoptions.html).ShowHiddenProperties

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to display in user interfaces properties marked as hidden.

#### Remarks

When this property is
 True
 , TestStand applications display all the subproperties of property objects in dialog boxes and variables views. When this property is
 False
 , TestStand applications do not display the subproperties marked with the
 [PropFlags_Hidden](propertyflags.html)
 flag.

#### See Also

[PropertyFlags](propertyflags.html)

[PropertyObject.GetFlags](propertyobject-getflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-specifystepsbyuniqueidinexpres.html language=enus -->
## TOPIC 02669: StationOptions.SpecifyStepsByUniqueIdInExpressions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-specifystepsbyuniqueidinexpres.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-specifystepsbyuniqueidinexpres.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.SpecifyStepsByUniqueIdInExpressions Data Type SpecifyStepsByUniqueIdOptions Use the following constants with this data type: SpecifyStepsByUniqueIdOption_Ask –(Value: 1) TestStand prompts you to use a unique step ID. SpecifyStepsByUniqueIdOption_No –(Value: 3) Use step names. S

### StationOptions.SpecifyStepsByUniqueIdInExpressions

#### Syntax

[StationOptions](stationoptions.html).SpecifyStepsByUniqueIdInExpressions

#### Data Type

[SpecifyStepsByUniqueIdOptions](specifystepsbyuniqueidoptions.html)

Use the following constants with this data type:

- SpecifyStepsByUniqueIdOption_Ask 
 –(Value: 1) TestStand prompts you to use a unique step ID.
- SpecifyStepsByUniqueIdOption_No 
 –(Value: 3) Use step names.
- SpecifyStepsByUniqueIdOption_Yes 
 –(Value: 2) Use unique step IDs.

#### Purpose

Specifies how the
 [Expression Browser](../tsref/expression-browser-dialog-box.html)
 dialog box specifies steps in expressions.

#### Remarks

TestStand uses this option to determine whether to replace the step name with the step ID when you construct an expression in the Expression Browser dialog box, as follows:
 Sequence.Main["step name"].Property
 .

#### See Also

[Engine.DisplayBrowseExprDialogEx](engine-displaybrowseexprdialogex.html)

[Expression Browser dialog box](../tsref/expression-browser-dialog-box.html)

[Step.UniqueStepId](step-uniquestepid.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-stationid.html language=enus -->
## TOPIC 02670: StationOptions.StationID

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-stationid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-stationid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.StationID Data Type String Purpose Specifies a test station identification string for this instance of the TestStand Engine. This property never returns an empty string. If you set this property to an empty string, this property returns the same value as the Engine.ComputerName

### StationOptions.StationID

#### Syntax

[StationOptions](stationoptions.html).StationID

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a test station identification string for this instance of the TestStand Engine.

This property never returns an empty string. If you set this property to an empty string, this property returns the same value as the
 [Engine.ComputerName](engine-computername.html)
 property.

#### See Also

[Engine.ComputerName](engine-computername.html)

[Engine.UniqueEngineId](engine-uniqueengineid.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-stationmodelsequencefilepath.html language=enus -->
## TOPIC 02671: StationOptions.StationModelSequenceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-stationmodelsequencefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-stationmodelsequencefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.StationModelSequenceFilePath Data Type String Purpose Specifies the pathname of the station model sequence file. Remarks If this property is a relative pathname, TestStand uses the Engine.FindFileEx method to determine the absolute pathname of the station model sequence file. S

### StationOptions.StationModelSequenceFilePath

#### Syntax

[StationOptions](stationoptions.html).StationModelSequenceFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the station model sequence file.

#### Remarks

If this property is a relative pathname, TestStand uses the
 [Engine.FindFileEx](engine-findfileex.html)
 method to determine the absolute pathname of the station model sequence file.

#### See Also

[Engine.FindFileEx](engine-findfileex.html)

[StationOptions.AllowOtherModels](stationoptions-allowothermodels.html)

[StationOptions.UseStationModel](stationoptions-usestationmodel.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-systemdefaultsourcecodecontrol.html language=enus -->
## TOPIC 02672: StationOptions.SystemDefaultSourceCodeControlProvider

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-systemdefaultsourcecodecontrol.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-systemdefaultsourcecodecontrol.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.SystemDefaultSourceCodeControlProvider Data Type String Purpose Specifies the default system source code control provider. If you do not want to specify a default source code control provider, pass an empty string as the value of this property. Remarks This is a system property

### StationOptions.SystemDefaultSourceCodeControlProvider

#### Syntax

[StationOptions](stationoptions.html).SystemDefaultSourceCodeControlProvider

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the default system source code control provider.

If you do not want to specify a default source code control provider, pass an empty string as the value of this property.

#### Remarks

Note

Note

This property reflects the value stored in the Windows registry for the system source code control settings located in the string key
 HKEY_LOCAL_MACHINE\Software\SourceCodeControlProvider\ProviderRegKey
 . The key specifies the name of the
 HKEY_LOCAL_MACHINE\Software
 registry key that contains the source code control provider server name and path.
 (32-bit TestStand)
 On 64-bit operating systems, this registry key appears only in the 32-bit registry. Use the path
 HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\SourceCodeControlProvider\ProviderRegKey
 to access the key in the registry editor.

If the
 [Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)
 property is not empty and the
 [WorkspaceFile.ProviderName](workspacefile-providername.html)
 property for the current workspace is empty, TestStand connects to the system default source code control provider to perform source code control operations.

If the value of this property is empty, TestStand only connects to a source code control provider if the
 WorkspaceFile.ProviderName
 property for the current workspace is not empty.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[StationOptions.CheckOutFilesWhenEdited](stationoptions-checkoutfileswhenedited.html)

[StationOptions.CheckOutOnlySelectedFiles](stationoptions-checkoutonlyselectedfiles.html)

[StationOptions.PromptWhenAddingFilesToSC](stationoptions-promptwhenaddingfilestosc.html)

[StationOptions.UseDialogForCheckout](stationoptions-usedialogforcheckout.html)

[WorkspaceFile.ProviderName](workspacefile-providername.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-tracingenabled.html language=enus -->
## TOPIC 02673: StationOptions.TracingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-tracingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-tracingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.TracingEnabled Data Type Boolean Purpose Specifies if tracing is enabled for the sequence editor and user interfaces. See Also Execution.TracingDisabled SequenceContext.CanTrace StationOptions.BreakpointsEnabled

### StationOptions.TracingEnabled

#### Syntax

[StationOptions](stationoptions.html).TracingEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if tracing is enabled for the sequence editor and user interfaces.

#### See Also

[Execution.TracingDisabled](execution-tracingdisabled.html)

[SequenceContext.CanTrace](sequencecontext-cantrace.html)

[StationOptions.BreakpointsEnabled](stationoptions-breakpointsenabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-typeversionautoincrementopt.html language=enus -->
## TOPIC 02674: StationOptions.TypeVersionAutoIncrementOpt

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-typeversionautoincrementopt.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-typeversionautoincrementopt.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.TypeVersionAutoIncrementOpt Data Type TypeVersionAutoIncrement Use the following constants with this data type: TypeVersionInc_Build –(Value: 4) Auto-increment build version number. TypeVersionInc_Major –(Value: 1) Auto-increment major version number. TypeVersionInc_Minor –(Val

### StationOptions.TypeVersionAutoIncrementOpt

#### Syntax

[StationOptions](stationoptions.html).TypeVersionAutoIncrementOpt

#### Data Type

[TypeVersionAutoIncrement](typeversionautoincrement.html)

Use the following constants with this data type:

- TypeVersionInc_Build 
 –(Value: 4) Auto-increment build version number.
- TypeVersionInc_Major 
 –(Value: 1) Auto-increment major version number.
- TypeVersionInc_Minor 
 –(Value: 2) Auto-increment minor version number.
- TypeVersionInc_None 
 –(Value: 0) Do not increment type versions.
- TypeVersionInc_Revision 
 –(Value: 3) Auto-increment revision version number.

#### Purpose

Specifies if the sequence editor automatically increments type versions before saving modified types.

#### Remarks

The type version number is composed of the following four things in this format:
 Major.Minor.Revision.Build
 .

#### See Also

[PropertyObject.TypeVersion](propertyobject-typeversion.html)

[PropertyObjectFile.CheckForModifiedTypes](propertyobjectfile-checkformodifiedtypes.html)

[StationOptions.TypeVersionAutoIncrementPromptOpt](stationoptions-typeversionautoincrementprompt.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-typeversionautoincrementprompt.html language=enus -->
## TOPIC 02675: StationOptions.TypeVersionAutoIncrementPromptOpt

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-typeversionautoincrementprompt.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-typeversionautoincrementprompt.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.TypeVersionAutoIncrementPromptOpt Data Type Boolean Purpose Specifies if the sequence editor prompts the user to increment the type version before saving the modified types. See Also PropertyObject.TypeVersion PropertyObjectFile.CheckForModifiedTypes StationOptions.TypeVersionA

### StationOptions.TypeVersionAutoIncrementPromptOpt

#### Syntax

[StationOptions](stationoptions.html).TypeVersionAutoIncrementPromptOpt

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the sequence editor prompts the user to increment the type version before saving the modified types.

#### See Also

[PropertyObject.TypeVersion](propertyobject-typeversion.html)

[PropertyObjectFile.CheckForModifiedTypes](propertyobjectfile-checkformodifiedtypes.html)

[StationOptions.TypeVersionAutoIncrementOpt](stationoptions-typeversionautoincrementopt.html)

[TypeVersionAutoIncrement](typeversionautoincrement.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-uimessagedelay.html language=enus -->
## TOPIC 02676: StationOptions.UIMessageDelay

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-uimessagedelay.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-uimessagedelay.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.UIMessageDelay Data Type Long Purpose Specifies how many milliseconds must pass between postings of UIMsg_Trace events. Remarks Set this property to specify how many milliseconds must pass before you receive the next UIMsg_Trace event. This property is useful for slowing down t

### StationOptions.UIMessageDelay

#### Syntax

[StationOptions](stationoptions.html).UIMessageDelay

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies how many milliseconds must pass between postings of
 UIMsg_Trace
 events.

#### Remarks

Set this property to specify how many milliseconds must pass before you receive the next
 UIMsg_Trace
 event. This property is useful for slowing down the posting of trace messages to the user interface or sequence editor to allow time for processing mouse events and/or to display the trace of an execution more slowly.

Note

StationOptions.UIMessageMinDelay

StationOptions.UIMessageMinDelay

#### See Also

[StationOptions.UIMessageMinDelay](stationoptions-uimessagemindelay.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-uimessagemindelay.html language=enus -->
## TOPIC 02677: StationOptions.UIMessageMinDelay

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-uimessagemindelay.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-uimessagemindelay.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.UIMessageMinDelay Data Type Long Purpose Specifies the minimum value allowed for the StationOptions.UIMessageDelay property. This setting is not persisted like most StationOptions. The setting lasts only for the lifetime of the Engine. Remarks Default value is 0. Use this prope

### StationOptions.UIMessageMinDelay

#### Syntax

[StationOptions](stationoptions.html).UIMessageMinDelay

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the minimum value allowed for the
 [StationOptions.UIMessageDelay](stationoptions-uimessagedelay.html)
 property. This setting is not persisted like most StationOptions. The setting lasts only for the lifetime of the Engine.

#### Remarks

Default value is 0.

Use this property to specify the minimum value allowed for the
 StationOptions.UIMessageDelay
 property for the sequence editor or user interface.

#### See Also

[StationOptions.UIMessageDelay](stationoptions-uimessagedelay.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-usedialogforcheckout.html language=enus -->
## TOPIC 02678: StationOptions.UseDialogForCheckOut

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-usedialogforcheckout.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-usedialogforcheckout.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.UseDialogForCheckOut Data Type Boolean Purpose Specifies if the sequence editor launches a dialog box to check out files from source code control. Remarks When this property is True , the sequence editor always launches a dialog box when you check out files from source code con

### StationOptions.UseDialogForCheckOut

#### Syntax

[StationOptions](stationoptions.html).UseDialogForCheckOut

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the sequence editor launches a dialog box to check out files from source code control.

#### Remarks

When this property is
 True
 , the sequence editor always launches a dialog box when you check out files from source code control. When this property is
 False
 , the sequence editor checks out the files without launching the dialog box.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[StationOptions.CheckOutFilesWhenEdited](stationoptions-checkoutfileswhenedited.html)

[StationOptions.PromptWhenAddingFilesToSC](stationoptions-promptwhenaddingfilestosc.html)

[StationOptions.UseDialogForCheckOut](stationoptions-usedialogforcheckout.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-uselocalizeddecimalpoint.html language=enus -->
## TOPIC 02679: StationOptions.UseLocalizedDecimalPoint

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-uselocalizeddecimalpoint.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-uselocalizeddecimalpoint.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.UseLocalizedDecimalPoint Data Type Boolean Purpose Specifies whether to use the operating system setting to determine the character used as a decimal point. Remarks When this property is True , TestStand uses the operating system setting to determine the character it uses as th

### StationOptions.UseLocalizedDecimalPoint

#### Syntax

[StationOptions](stationoptions.html).UseLocalizedDecimalPoint

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to use the operating system setting to determine the character used as a decimal point.

#### Remarks

When this property is
 True
 , TestStand uses the operating system setting to determine the character it uses as the localized decimal point. When this property is
 False
 , TestStand uses the period character to represent decimal points.

#### See Also

[StationOptions.GetLanguages](stationoptions-getlanguages.html)

[StationOptions.Language](stationoptions-language.html)

[StationOptions.RecognizeMBChars](stationoptions-recognizembchars.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-userfilepath.html language=enus -->
## TOPIC 02680: StationOptions.UserFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-userfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-userfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.UserFilePath Data Type String Purpose Specifies the location of the current user manager file. Remarks Pass an empty path to this property to instruct TestStand to use the default user manager file. A change to this property does not take effect until you restart the engine. Se

### StationOptions.UserFilePath

#### Syntax

[StationOptions](stationoptions.html).UserFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the location of the current user manager file.

#### Remarks

Pass an empty path to this property to instruct TestStand to use the default user manager file.

A change to this property does not take effect until you restart the engine.

#### See Also

[Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)

[StationOptions.AutoLoginSystemUser](stationoptions-autologinsystemuser.html)

[StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)

[StationOptions.RequireUserLogin](stationoptions-requireuserlogin.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions-usestationmodel.html language=enus -->
## TOPIC 02681: StationOptions.UseStationModel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions-usestationmodel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions-usestationmodel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax StationOptions.UseStationModel Data Type Boolean Purpose Specifies if client sequence files use the station model. Remarks When you set this property to True , the station model specified by StationModelSequenceFilePath is used when the model option for a client sequence file specifies to use

### StationOptions.UseStationModel

#### Syntax

[StationOptions](stationoptions.html).UseStationModel

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if client sequence files use the station model.

#### Remarks

When you set this property to
 True
 , the station model specified by
 [StationModelSequenceFilePath](stationoptions-stationmodelsequencefilepath.html)
 is used when the model option for a client sequence file specifies to use the station model.

When you set this property to
 False
 , sequence files only have a process model file associated with them if they explicitly specify one. Typically, sequence files do not explicitly specify a process model file.

#### See Also

[AllowOtherModels](stationoptions-allowothermodels.html)

[SequenceFile.ModelOption](sequencefile-modeloption.html)

[StationModelSequenceFilePath](stationoptions-stationmodelsequencefilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/stationoptions.html language=enus -->
## TOPIC 02682: StationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/stationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/stationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the StationOptions class to set preferences for TestStand. The settings affect all sequence editor and user interface sessions. Use the Engine.DisplayOptionsDialog method to launch the Station Options dialog box. Properties AllowAllUsersAccessFromRemoteMachine AllowAutomaticTypeConflictResolutio

### StationOptions

Use the StationOptions class to set preferences for TestStand. The settings affect all sequence editor and user interface sessions. Use the
 [Engine.DisplayOptionsDialog](engine-displayoptionsdialog.html)
 method to launch the
 [Station Options](../tsref/station-options-dialog-box.html)
 dialog box.

#### Properties

| AllowAllUsersAccessFromRemoteMachine |
| --- |
| AllowAutomaticTypeConflictResolution |
| AllowCancellingPreloadExpression |
| AllowOtherModels |
| AllowSequenceCallsFromRemoteMachine |
| AlwaysGotoCleanupOnFailure |
| AutoCreateVariableLocation |
| AutoLoginSystemUser |
| BreakOnSequenceFailure |
| BreakOnStepFailure |
| BreakpointsEnabled |
| CheckOutFilesWhenEdited |
| CheckOutOnlySelectedFiles |
| DebugOptions |
| DefaultCPUAffinityForThreadsEx |
| DefaultFileWritingFormat |
| DisableResults |
| EnableUserPrivilegeChecking |
| ExecutionMask |
| FileModificationIndicatorPolicy |
| InteractiveBranchMode |
| InteractiveExePropagateStatus |
| Language |
| LoginOnStart |
| PreloadProgressDelay |
| PromptToFindFiles |
| PromptWhenAddingFilesToSC |
| RecognizeMBChars |
| ReloadDocsWhenOpeningWorkspace |
| ReloadWorkspaceAtStartup |
| RequireUserLogin |
| RTEOption |
| SeqFileVersionAutoIncrementOpt |
| ShowEngineTrayIconOnRemoteStations |
| ShowHiddenProperties |
| SpecifyStepsByUniqueIdInExpressions |
| StationID |
| StationModelSequenceFilePath |
| SystemDefaultSourceCodeControlProvider |
| TracingEnabled |
| TypeVersionAutoIncrementOpt |
| TypeVersionAutoIncrementPromptOpt |
| UIMessageDelay |
| UIMessageMinDelay |
| UseDialogForCheckOut |
| UseLocalizedDecimalPoint |
| UserFilePath |
| UseStationModel |

#### Methods

| GetLanguages |
| --- |
| GetTimeLimit |
| GetTimeLimitAction |
| GetTimeLimitEnabled |
| SetTimeLimit |
| SetTimeLimitAction |
| SetTimeLimitEnabled |

#### See Also

[Engine.DisplayOptionsDialog](engine-displayoptionsdialog.html)

[Engine.StationOptions](engine-stationoptions.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-adapterkeyname.html language=enus -->
## TOPIC 02683: Step.AdapterKeyName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-adapterkeyname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-adapterkeyname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.AdapterKeyName Data Type String Purpose Returns the key name of the module adapter the step uses. Remarks If the step does not use a module adapter, this property returns None Adapter , which is the value of the constant NoneAdapterKeyName . See Also Adapter.KeyName AdapterKeyNames

### Step.AdapterKeyName

#### Syntax

[Step](step.html).AdapterKeyName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the key name of the module adapter the step uses.

#### Remarks

If the step does not use a module adapter, this property returns
 None Adapter
 , which is the value of the constant
 [NoneAdapterKeyName](adapterkeynames.html)
 .

#### See Also

[Adapter.KeyName](adapter-keyname.html)

[AdapterKeyNames](adapterkeynames.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-additionalresults.html language=enus -->
## TOPIC 02684: Step.AdditionalResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-additionalresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-additionalresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.AdditionalResults Data Type StepAdditionalResults Purpose Accesses the parameter additional results and custom additional results of a step. See Also StepAdditionalResults

### Step.AdditionalResults

#### Syntax

[Step](step.html).AdditionalResults

#### Data Type

[StepAdditionalResults](stepadditionalresults.html)

#### Purpose

Accesses the parameter additional results and custom additional results of a step.

#### See Also

[StepAdditionalResults](stepadditionalresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-additionalresultshints.html language=enus -->
## TOPIC 02685: Step.AdditionalResultsHints

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-additionalresultshints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-additionalresultshints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.AdditionalResultsHints Data Type AdditionalResults Purpose Returns a list of additional result hints associated with a step instance. Use this property when step types support multiple operations and you want to specify different additional result hints for different step operations. Rem

### Step.AdditionalResultsHints

#### Syntax

[Step](step.html).AdditionalResultsHints

#### Data Type

[AdditionalResults](additionalresults.html)

#### Purpose

Returns a list of additional result hints associated with a step instance. Use this property when step types support multiple operations and you want to specify different additional result hints for different step operations.

#### Remarks

The combined members of
 [StepType.AdditionalResultsHints](steptype-additionalresultshints.html)
 and
 "Step.AdditionalResultsHints"
 define a list of preconfigured custom additional results you can choose to log when you edit the additional results of a step in a user interface.

You normally edit the
 Step.AdditionalResultsHints
 collection in an Edit substep.

#### See Also

[AdditionalResults](additionalresults.html)

[StepType.AdditionalResultsHints](steptype-additionalresultshints.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-aspropertyobject.html language=enus -->
## TOPIC 02686: Step.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the Step object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### Step.AsPropertyObject

#### Syntax

[Step](step.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the Step object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-batchsyncoption.html language=enus -->
## TOPIC 02687: Step.BatchSyncOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-batchsyncoption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-batchsyncoption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BatchSyncOption Data Type BatchSynchronizationOptions Use the following constants with this data type: BatchSyncOption_NoSync –(Value: 2) No batch synchronization is used on this step. BatchSyncOption_OneThreadOnly –(Value: 5) Use a One Thread Only section to specify that only one thread

### Step.BatchSyncOption

#### Syntax

[Step](step.html).BatchSyncOption

#### Data Type

[BatchSynchronizationOptions](batchsynchronizationoptions.html)

Use the following constants with this data type:

- BatchSyncOption_NoSync 
 –(Value: 2) No batch synchronization is used on this step.
- BatchSyncOption_OneThreadOnly 
 –(Value: 5) Use a One Thread Only section to specify that only one thread in the batch executes the single step or the steps in the section. Typically, you use this type of section to perform an operation that applies to the batch as a whole, such as raising the temperature in a test chamber. When all threads in a batch arrive at their respective instances of the single step or an Enter step for a One Thread Only section, TestStand releases only the thread with the lowest order number. When that thread executes the single step or arrives at the Exit step for the section, all remaining threads in the batch skip the single step or jump from the Enter step to the Exit step, skipping steps within the section. The threads in the batch then continue and exit the section together.
- BatchSyncOption_Parallel 
 –(Value: 4) When all threads in the batch arrive at their respective instances of a single step or an Enter step for a Parallel section, TestStand releases all the threads at once. Each thread blocks after executing the single step or after reaching the Exit step for the section until all threads can continue and exit the section together.
- BatchSyncOption_Serial 
 –(Value: 3) Use a Serial section to ensure that each thread in the batch executes a single step sequentially or the steps in a section sequentially and in the order you specified when you created the batch. When all threads in a batch arrive at their respective instances of a single step or an Enter step for a Serial section, TestStand releases one thread at a time in ascending order according to the order number you assign to threads when you added them to the batch using the Batch Specification step type. As each thread executes the single step or reaches the Exit step for the section, the next thread in the batch executes the single step or proceeds from the Enter step. After all threads in the batch execute the single step or arrive at the Exit step, they continue and exit the section together.
- BatchSyncOption_UseModelSetting 
 –(Value: 1) Uses the same option the model is using.
- BatchSyncOption_UseSeqFileSetting 
 –(Value: 0) Uses the same option the sequence file is using.

#### Purpose

Specifies the Batch Synchronization operation that the step enters before it executes and exits after it completes.

#### See Also

[Step.MutexNameOrRefExpr](step-mutexnameorrefexpr.html)

[Step.UseMutex](step-usemutex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-blockendindex.html language=enus -->
## TOPIC 02688: Step.BlockEndIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-blockendindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-blockendindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BlockEndIndex Data Type Long Purpose Returns the index of the step that closes the block this step opens. Returns -1 if this step does not open a matched block.

### Step.BlockEndIndex

#### Syntax

[Step](step.html).BlockEndIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the index of the step that closes the block this step opens. Returns
 -1
 if this step does not open a matched block.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-blockflags.html language=enus -->
## TOPIC 02689: Step.BlockFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-blockflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-blockflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BlockFlags Data Type Long Purpose Specifies flags that indicate how the step affects the block structure of the sequence. See Also BlockFlags

### Step.BlockFlags

#### Syntax

[Step](step.html).BlockFlags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies flags that indicate how the step affects the block structure of the sequence.

#### See Also

[BlockFlags](blockflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-blocklevel.html language=enus -->
## TOPIC 02690: Step.BlockLevel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-blocklevel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-blocklevel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BlockLevel Data Type Long Purpose Specifies the number of blocks that enclose the step. Specifies 0 for top-level steps.

### Step.BlockLevel

#### Syntax

[Step](step.html).BlockLevel

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of blocks that enclose the step. Specifies
 0
 for top-level steps.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-blocklevelsunmatched.html language=enus -->
## TOPIC 02691: Step.BlockLevelsUnmatched

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-blocklevelsunmatched.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-blocklevelsunmatched.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BlockLevelsUnmatched Data Type Long Purpose Specifies the number of unterminated blocks that enclose the step.

### Step.BlockLevelsUnmatched

#### Syntax

[Step](step.html).BlockLevelsUnmatched

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the number of unterminated blocks that enclose the step.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-blocknextindex.html language=enus -->
## TOPIC 02692: Step.BlockNextIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-blocknextindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-blocknextindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BlockNextIndex Data Type Long Purpose Specifies the index of the nearest following step that starts a block, regardless of the level of the next block. Specifies -1 if this step does not start a block or if no subsequent block exists.

### Step.BlockNextIndex

#### Syntax

[Step](step.html).BlockNextIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the index of the nearest following step that starts a block, regardless of the level of the next block. Specifies
 -1
 if this step does not start a block or if no subsequent block exists.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-blockparentindex.html language=enus -->
## TOPIC 02693: Step.BlockParentIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-blockparentindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-blockparentindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BlockParentIndex Data Type Long Purpose Specifies the index of the step that starts the enclosing block. Specifies -1 if this step does not reside in an enclosing block.

### Step.BlockParentIndex

#### Syntax

[Step](step.html).BlockParentIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the index of the step that starts the enclosing block. Specifies
 -1
 if this step does not reside in an enclosing block.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-blockpreviousindex.html language=enus -->
## TOPIC 02694: Step.BlockPreviousIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-blockpreviousindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-blockpreviousindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BlockPreviousIndex Data Type Long Purpose Specifies the index of the nearest previous step that starts a block, regardless of the level of the preceding block. Specifies -1 if this step does not also start a block or if no previous block exists.

### Step.BlockPreviousIndex

#### Syntax

[Step](step.html).BlockPreviousIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the index of the nearest previous step that starts a block, regardless of the level of the preceding block. Specifies
 -1
 if this step does not also start a block or if no previous block exists.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-blockstartindex.html language=enus -->
## TOPIC 02695: Step.BlockStartIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-blockstartindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-blockstartindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BlockStartIndex Data Type Long Purpose Specifies the index of the step that opens the block this step closes. Specifies -1 if this step does not close a matched block.

### Step.BlockStartIndex

#### Syntax

[Step](step.html).BlockStartIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the index of the step that opens the block this step closes. Specifies
 -1
 if this step does not close a matched block.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-breakonstep.html language=enus -->
## TOPIC 02696: Step.BreakOnStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-breakonstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-breakonstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.BreakOnStep Data Type Boolean Purpose This property is obsolete. Use the Step.GetBreakSettings and Step.SetBreakSettings methods instead. Remarks If this property is True , TestStand suspends execution before executing the step. This property is now equivalent to setting or getting the s

### Step.BreakOnStep

#### Syntax

[Step](step.html).BreakOnStep

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Step.GetBreakSettings

Step.SetBreakSettings

#### Remarks

If this property is
 True
 , TestStand suspends execution before executing the step. This property is now equivalent to setting or getting the sequence file version of the breakpoint.

#### See Also

[Step.GetBreakSettings](step-getbreaksettings.html)

[Step.SetBreakSettings](step-setbreaksettings.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-cancelcurrentexecution.html language=enus -->
## TOPIC 02697: Step.CancelCurrentExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-cancelcurrentexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-cancelcurrentexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CancelCurrentExecution Data Type Boolean Purpose When this property is True , TestStand does not evaluate the pre-expression and does not call the Pre-Step substeps, step module, subsequent Post-Step substeps, or the Post-Step callbacks for the step, nor does it evaluate the post express

### Step.CancelCurrentExecution

#### Syntax

[Step](step.html).CancelCurrentExecution

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

When this property is
 True
 , TestStand does not evaluate the pre-expression and does not call the Pre-Step substeps, step module, subsequent Post-Step substeps, or the Post-Step callbacks for the step, nor does it evaluate the post expression or status expression.

#### Remarks

This property is reset to
 False
 after TestStand uses it so that the step runs normally the next time it executes. The property is also reset to
 False
 before the start of the next iteration when performing step looping. You can set this property from the Pre-Step Engine callbacks, the step pre- or post-expression, or the Pre- or Post-Step substep of a step type. By setting this property to
 True
 , you can use this property to impose additional conditions that a step must meet before it can execute.

Setting this property to
 True
 in an
 OnNewStep
 substep for the inserted step instructs TestStand to cancel the insertion of the step.

#### See Also

[Step.CancelCurrentModuleExecution](step-cancelcurrentmoduleexecution.html)

[Step.CancelStepCallback](step-cancelstepcallback.html)

[Using Substeps](/csh?context=ts_tsfundamentals_step_type_prop_substeps)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-cancelcurrentmoduleexecution.html language=enus -->
## TOPIC 02698: Step.CancelCurrentModuleExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-cancelcurrentmoduleexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-cancelcurrentmoduleexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CancelCurrentModuleExecution Data Type Boolean Purpose When this property is True , TestStand does not call the code module for the step. Remarks This property is reset to False after TestStand uses it so that the step runs normally the next time it executes. The property is also reset t

### Step.CancelCurrentModuleExecution

#### Syntax

[Step](step.html).CancelCurrentModuleExecution

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

When this property is
 True
 , TestStand does not call the code module for the step.

#### Remarks

This property is reset to
 False
 after TestStand uses it so that the step runs normally the next time it executes. The property is also reset to
 False
 before the start of the next iteration when looping on a step. You can set this property from the Pre-Step Engine callbacks, the step pre-expression, or the Pre-Step substep of a step type. By setting this property to
 True
 , you can use this property to impose additional conditions that a step must meet before it can execute the code module.

#### See Also

[Step.CancelCurrentExecution](step-cancelcurrentexecution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-cancelstepcallback.html language=enus -->
## TOPIC 02699: Step.CancelStepCallback

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-cancelstepcallback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-cancelstepcallback.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CancelStepCallback Data Type Boolean Purpose Specifies that TestStand does not call any further Engine callbacks for the same event. Remarks In an Engine callback sequence, set this property on the step that triggers the callback to specify that TestStand does not call any further Engine

### Step.CancelStepCallback

#### Syntax

[Step](step.html).CancelStepCallback

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that TestStand does not call any further Engine callbacks for the same event.

#### Remarks

In an Engine callback sequence, set this property on the step that triggers the callback to specify that TestStand does not call any further Engine callbacks for the same triggering event. For example, a SequenceFilePostStepRuntimeError callback that completely handles a run-time error might set this property to prevent TestStand from also executing a ProcessModelPostStepRuntimeError callback for the same step error.

#### See Also

[CallbackTypes](callbacktypes.html)

[Step.CancelCurrentExecution](step-cancelcurrentexecution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-canchangeadapter.html language=enus -->
## TOPIC 02700: Step.CanChangeAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-canchangeadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-canchangeadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CanChangeAdapter( adapterName = "") Return Value Boolean Returns True if the step allows changing to the specified adapter. Otherwise, returns False . Purpose Returns a value that indicates whether the step allows changing the adapter. Remarks Call CanChangeAdapter before calling the Ste

### Step.CanChangeAdapter

#### Syntax

[Step](step.html).CanChangeAdapter( adapterName = "")

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the step allows changing to the specified adapter. Otherwise, returns
 False
 .

#### Purpose

Returns a value that indicates whether the step allows changing the adapter.

#### Remarks

Call CanChangeAdapter before calling the
 [Step.ChangeAdapter](step-changeadapter.html)
 method to ensure that no errors occur.

#### Parameters

adapterName
 As
 [String](data-types-for-teststand.html)

[In] Specifies an adapter key name that determines whether the step allows changing to that specific adapter. Pass the default value of the empty string to check if the step allows changing to any adapter.

This parameter has a default value of
 ""
 .

#### See Also

[AdapterKeyNames](adapterkeynames.html)

[Step.CanChangeStepType](step-canchangesteptype.html)

[Step.ChangeAdapter](step-changeadapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-canchangesteptype.html language=enus -->
## TOPIC 02701: Step.CanChangeStepType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-canchangesteptype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-canchangesteptype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CanChangeStepType( stepTypePtr = NULL) Return Value Boolean Returns True if the step allows changing to the specified step type. Otherwise, returns False . Purpose Returns a value that indicates whether the step allows changing the step type. Remarks Call this method before calling the S

### Step.CanChangeStepType

#### Syntax

[Step](step.html).CanChangeStepType( stepTypePtr = NULL)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the step allows changing to the specified step type. Otherwise, returns
 False
 .

#### Purpose

Returns a value that indicates whether the step allows changing the step type.

#### Remarks

Call this method before calling the
 [Step.ChangeStepType](step-changesteptype.html)
 method to ensure that an error does not occur.

#### Parameters

stepTypePtr
 As
 [StepType](steptype.html)

[In] Specifies a step type that checks if the step allows changing to that specific step type. Pass the default value of
 NULL
 to check if the step allows changing to any step type.

This parameter has a default value of
 NULL
 .

#### See Also

[Step.CanChangeAdapter](step-canchangeadapter.html)

[Step.ChangeStepType](step-changesteptype.html)

[StepType](steptype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-cancreatecode.html language=enus -->
## TOPIC 02702: Step.CanCreateCode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-cancreatecode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-cancreatecode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CanCreateCode Data Type Boolean Purpose Returns a value that indicates whether the step supports the Step.CreateCode method. This property returns False if the Module.CanCreateCode property is False , or if the Step.TS.CanCreateCode PropertyObject is False , or if the step has a step typ

### Step.CanCreateCode

#### Syntax

[Step](step.html).CanCreateCode

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the step supports the
 [Step.CreateCode](step-createcode.html)
 method. This property returns
 False
 if the
 [Module.CanCreateCode](module-cancreatecode.html)
 property is
 False
 , or if the
 Step.TS.CanCreateCode
 PropertyObject is
 False
 , or if the step has a step type and Edit Code is enabled on the
 [Disable Properties tab](../tsref/disable-properties-tab-step-type-properties-d.html)
 of the
 [Step Type Properties](../tsref/step-type-properties-dialog-box.html)
 dialog box for the step type.

#### See Also

[Disable Properties tab](../tsref/disable-properties-tab-step-type-properties-d.html)

[Module.CanCreateCode](module-cancreatecode.html)

[Step Type Properties dialog box](../tsref/step-type-properties-dialog-box.html)

[Step.CanEditCode](step-caneditcode.html)

[Step.CanSpecifyModule](step-canspecifymodule.html)

[Step.CreateCode](step-createcode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-caneditcode.html language=enus -->
## TOPIC 02703: Step.CanEditCode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-caneditcode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-caneditcode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CanEditCode Data Type Boolean Purpose Returns a value that indicates whether this step supports the Step.EditCode method. This property returns False if the Module.CanEditCode property is False , if the Step.TS.CanEditCode PropertyObject is False , or if the step has a step type and Edit

### Step.CanEditCode

#### Syntax

[Step](step.html).CanEditCode

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether this step supports the
 [Step.EditCode](step-editcode.html)
 method. This property returns
 False
 if the
 [Module.CanEditCode](module-caneditcode.html)
 property is
 False
 , if the
 Step.TS.CanEditCode
 PropertyObject is
 False
 , or if the step has a step type and Edit Code is enabled on the
 [Disable Properties tab](../tsref/disable-properties-tab-step-type-properties-d.html)
 of the
 [Step Type Properties](../tsref/step-type-properties-dialog-box.html)
 dialog box for the step type.

#### See Also

[Disable Properties tab](../tsref/disable-properties-tab-step-type-properties-d.html)

[Module.CanEditCode](module-caneditcode.html)

[Step.CanCreateCode](step-cancreatecode.html)

[Step.CanSpecifyModule](step-canspecifymodule.html)

[Step.EditCode](step-editcode.html)

[Step Type Properties dialog box](../tsref/step-type-properties-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-canexecuteeditsubstep.html language=enus -->
## TOPIC 02704: Step.CanExecuteEditSubstep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-canexecuteeditsubstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-canexecuteeditsubstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CanExecuteEditSubstep Data Type Boolean Purpose This property is obsolete. Use the Step.CanExecuteSubstep method instead. Remarks Returns a value that indicates whether you can execute the specified substep. See Also Step.CanExecuteSubstep Step.ExecuteSubstep

### Step.CanExecuteEditSubstep

#### Syntax

[Step](step.html).CanExecuteEditSubstep

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Step.CanExecuteSubstep

#### Remarks

Returns a value that indicates whether you can execute the specified substep.

#### See Also

[Step.CanExecuteSubstep](step-canexecutesubstep.html)

[Step.ExecuteSubstep](step-executesubstep.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-canexecutesubstep.html language=enus -->
## TOPIC 02705: Step.CanExecuteSubstep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-canexecutesubstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-canexecutesubstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CanExecuteSubstep( substepIndex, [sequenceContextParam]) Return Value Boolean Purpose Returns a value that indicates whether you can execute the specified substep. Remarks Call this method before calling the Step.ExecuteSubstep method. Parameters substepIndex As Long [In] Specifies the z

### Step.CanExecuteSubstep

#### Syntax

[Step](step.html).CanExecuteSubstep( substepIndex, [sequenceContextParam])

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether you can execute the specified substep.

#### Remarks

Call this method before calling the
 [Step.ExecuteSubstep](step-executesubstep.html)
 method.

#### Parameters

substepIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the substep.

sequenceContextParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you call this method from a step, you must pass a
 [SequenceContext](sequencecontext.html)
 . For executing substeps from a user interface, do not pass any value for this parameter.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceContext](sequencecontext.html)

[Step.ExecuteSubstep](step-executesubstep.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-canspecifymodule.html language=enus -->
## TOPIC 02706: Step.CanSpecifyModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-canspecifymodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-canspecifymodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CanSpecifyModule Data Type Boolean Purpose Returns a value that indicates whether this step supports the Step.SpecifyModule method. This property returns False if the Module.CanSpecify property is False , if the Step.TS.CanSpecifyModule PropertyObject is False , or if the step has a step

### Step.CanSpecifyModule

#### Syntax

[Step](step.html).CanSpecifyModule

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether this step supports the
 [Step.SpecifyModule](step-specifymodule.html)
 method. This property returns
 False
 if the
 [Module.CanSpecify](module-canspecify.html)
 property is
 False
 , if the
 Step.TS.CanSpecifyModule
 PropertyObject is
 False
 , or if the step has a step type and Specify Module is enabled on the
 [Disable Properties tab](../tsref/disable-properties-tab-step-type-properties-d.html)
 of the
 [Step Type Properties](../tsref/step-type-properties-dialog-box.html)
 dialog box for the step type.

#### See Also

[Disable Properties tab](../tsref/disable-properties-tab-step-type-properties-d.html)

[Module.CanSpecify](module-canspecify.html)

[Step Type Properties dialog box](../tsref/step-type-properties-dialog-box.html)

[Step.CanCreateCode](step-cancreatecode.html)

[Step.SpecifyModule](step-specifymodule.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-causedsequencefailure.html language=enus -->
## TOPIC 02707: Step.CausedSequenceFailure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-causedsequencefailure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-causedsequencefailure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CausedSequenceFailure Data Type Boolean Purpose Specifies if this step caused the sequence to fail. See Also Sequence.FailureAction Step.StepFailCausesSequenceFail

### Step.CausedSequenceFailure

#### Syntax

[Step](step.html).CausedSequenceFailure

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if this step caused the sequence to fail.

#### See Also

[Sequence.FailureAction](sequence-failureaction.html)

[Step.StepFailCausesSequenceFail](step-stepfailcausessequencefail.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-changeadapter.html language=enus -->
## TOPIC 02708: Step.ChangeAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-changeadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-changeadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.ChangeAdapter( adapterName) Purpose Changes the adapter a step uses. ChangeAdapter replaces the module of the step with a new module associated with the specified adapter. Remarks Returns an error if the step does not allow you to change the adapter. To avoid this error, call this method

### Step.ChangeAdapter

#### Syntax

[Step](step.html).ChangeAdapter( adapterName)

#### Purpose

Changes the adapter a step uses. ChangeAdapter replaces the module of the step with a new module associated with the specified adapter.

#### Remarks

Returns an error if the step does not allow you to change the adapter. To avoid this error, call this method only if the
 [Step.CanChangeAdapter](step-canchangeadapter.html)
 method returns
 True
 .

#### Parameters

adapterName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the adapter key name of the new adapter for the step. If the step does not specify a module adapter, pass an empty string.

#### See Also

[AdapterKeyNames](adapterkeynames.html)

[Step.CanChangeAdapter](step-canchangeadapter.html)

[Step.ChangeStepType](step-changesteptype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-changesteptype.html language=enus -->
## TOPIC 02709: Step.ChangeStepType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-changesteptype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-changesteptype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.ChangeStepType( stepTypePtr) Purpose Changes the step type of a step. Remarks Returns an error if the step does not allow changing the step type. To avoid this error, call this method only if the Step.CanChangeStepType method returns True . To acquire a step type to pass as a parameter,

### Step.ChangeStepType

#### Syntax

[Step](step.html).ChangeStepType( stepTypePtr)

#### Purpose

Changes the step type of a step.

#### Remarks

Returns an error if the step does not allow changing the step type. To avoid this error, call this method only if the
 [Step.CanChangeStepType](step-canchangesteptype.html)
 method returns
 True
 .

To acquire a step type to pass as a parameter, call
 [Engine.GetTypeDefinition](engine-gettypedefinition.html)
 and pass the name of the desired step type, then query the returned PropertyObject for the StepType interface.

#### Parameters

stepTypePtr
 As
 [StepType](steptype.html)

[In] Specifies the step type to which you want to convert the step.

#### See Also

[Engine.GetTypeDefinition](engine-gettypedefinition.html)

[Step.CanChangeStepType](step-canchangesteptype.html)

[Step.ChangeAdapter](step-changeadapter.html)

[Step.StepType](step-steptype.html)

[StepType](steptype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-createcode.html language=enus -->
## TOPIC 02710: Step.CreateCode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-createcode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-createcode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CreateCode Return Value Boolean Indicates if the step was modified. Purpose Creates a code module for this step. Remarks The contents of the code module depend on the adapter used to create this step, the module settings for this step, and the code templates configured for the step type.

### Step.CreateCode

#### Syntax

[Step](step.html).CreateCode

#### Return Value

[Boolean](data-types-for-teststand.html)

Indicates if the step was modified.

#### Purpose

Creates a code module for this step.

#### Remarks

The contents of the code module depend on the adapter used to create this step, the module settings for this step, and the code templates configured for the step type.

For adapters that use Microsoft Visual Studio, calling this method can result in prompts to the user if any of the following conditions exist:

- Multiple versions of Visual Studio exist on the computer and you select the
 Always Prompt for Version 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the
 Adapter Configuration 
 dialog box.
- Multiple versions of Visual Studio exist on the computer and you select the
 Use the Version that Matches the Project File 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the Adapter Configuration dialog box, and TestStand cannot match the version of the file.
- A method already exists with the same name.
- The specified solution does not contain the specified project.
- The specified project does not contain the specified source file.

Note

Step.CanCreateCode

#### See Also

[Adapter Configuration dialog box](../tsref/adapter-configuration-dialog-box.html)

[Step.CanCreateCode](step-cancreatecode.html)

[Step.EditCode](step-editcode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-createnewuniquestepid.html language=enus -->
## TOPIC 02711: Step.CreateNewUniqueStepId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-createnewuniquestepid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-createnewuniquestepid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CreateNewUniqueStepId Purpose Replaces the unique step ID with a new unique step ID. See Also Step.UniqueStepId

### Step.CreateNewUniqueStepId

#### Syntax

[Step](step.html).CreateNewUniqueStepId

#### Purpose

Replaces the unique step ID with a new unique step ID.

#### See Also

[Step.UniqueStepId](step-uniquestepid.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-currentloopresult.html language=enus -->
## TOPIC 02712: Step.CurrentLoopResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-currentloopresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-currentloopresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CurrentLoopResult Data Type PropertyObject Purpose Specifies the PropertyObject object that holds the result for the loop iteration the step is running. Remarks You can set this property to NULL (Nothing) in a step or substep module to remove the step iteration result from the result lis

### Step.CurrentLoopResult

#### Syntax

[Step](step.html).CurrentLoopResult

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Specifies the PropertyObject object that holds the result for the loop iteration the step is running.

#### Remarks

You can set this property to
 NULL
 (Nothing) in a step or substep module to remove the step iteration result from the result list. If you set this property to a value other than
 NULL
 or if you set the property when the step is not executing, the result list does not change.

Returns a
 NULL
 reference if the step is not looping.

#### See Also

[PropertyObject](propertyobject.html)

[Step.LastStepResult](step-laststepresult.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-customactionexpression.html language=enus -->
## TOPIC 02713: Step.CustomActionExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-customactionexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-customactionexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CustomActionExpression Data Type String Purpose Specifies the custom post action condition expression for the step. See Also Step.CustomFalseAction Step.CustomFalseActionTargetByExpr Step.CustomTrueAction Step.CustomTrueActionTargetByExpr

### Step.CustomActionExpression

#### Syntax

[Step](step.html).CustomActionExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the custom post action condition expression for the step.

#### See Also

[Step.CustomFalseAction](step-customfalseaction.html)

[Step.CustomFalseActionTargetByExpr](step-customfalseactiontargetbyexpr.html)

[Step.CustomTrueAction](step-customtrueaction.html)

[Step.CustomTrueActionTargetByExpr](step-customtrueactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-customfalseaction.html language=enus -->
## TOPIC 02714: Step.CustomFalseAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-customfalseaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-customfalseaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CustomFalseAction Data Type String Purpose Specifies the type of action you want to occur when the custom post action expression evaluates to False . Remarks Assign a PostActionValues string constant to the property to specify the type of post action to perform. See Also PostActionValues

### Step.CustomFalseAction

#### Syntax

[Step](step.html).CustomFalseAction

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the type of action you want to occur when the custom post action expression evaluates to
 False
 .

#### Remarks

Assign a
 [PostActionValues](postactionvalues.html)
 string constant to the property to specify the type of post action to perform.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.CustomActionExpression](step-customactionexpression.html)

[Step.CustomFalseActionTargetByExpr](step-customfalseactiontargetbyexpr.html)

[Step.CustomTrueAction](step-customtrueaction.html)

[Step.CustomTrueActionTargetByExpr](step-customtrueactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-customfalseactiontarget.html language=enus -->
## TOPIC 02715: Step.CustomFalseActionTarget

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-customfalseactiontarget.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-customfalseactiontarget.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CustomFalseActionTarget Data Type String Purpose This property is obsolete. Use the Step.CustomFalseActionTargetByExpr property instead. Remarks Specifies the target for the post action the Step.CustomFalseAction property specifies. Post action targets are now expressions. If you set the

### Step.CustomFalseActionTarget

#### Syntax

[Step](step.html).CustomFalseActionTarget

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Step.CustomFalseActionTargetByExpr

#### Remarks

Specifies the target for the post action the
 [Step.CustomFalseAction](step-customfalseaction.html)
 property specifies. Post action targets are now expressions. If you set the target using this property, TestStand converts the target into a string constant expression before storing it. If you attempt to obtain the target using this property and the target is a string constant expression, TestStand converts it back into the string it represents and returns the string to you. If the target is not a string constant but is a more complex expression, TestStand returns an error if you try to obtain the value using this property.

- If the
 Step.CustomFalseAction 
 property is
 PostAction_GotoStep 
 , the target is the name of the step or the ID of the step. If you specify the target by name, the target step must reside in the same step group. If you specify the target by ID, the target step can reside in any step group in the sequence.
- If the
 Step.CustomFalseAction 
 property is
 PostAction_CallCallback 
 , the target is the name of the callback sequence.
- For all other types of post actions, the target property is not used.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.CustomActionExpression](step-customactionexpression.html)

[Step.CustomFalseAction](step-customfalseaction.html)

[Step.CustomFalseActionTargetByExpr](step-customfalseactiontargetbyexpr.html)

[Step.CustomTrueAction](step-customtrueaction.html)

[Step.CustomTrueActionTargetByExpr](step-customtrueactiontargetbyexpr.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-customfalseactiontargetbyexpr.html language=enus -->
## TOPIC 02716: Step.CustomFalseActionTargetByExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-customfalseactiontargetbyexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-customfalseactiontargetbyexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CustomFalseActionTargetByExpr Data Type String Purpose Specifies the target for the post action the Step.CustomFalseAction property specifies. Remarks If the Step.CustomFalseAction property is PostAction_GotoStep , the target is the name of the step or the ID of the step. If you specify

### Step.CustomFalseActionTargetByExpr

#### Syntax

[Step](step.html).CustomFalseActionTargetByExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for the post action the
 [Step.CustomFalseAction](step-customfalseaction.html)
 property specifies.

#### Remarks

- If the
 Step.CustomFalseAction 
 property is
 PostAction_GotoStep 
 , the target is the name of the step or the ID of the step. If you specify the target by name, the target step must reside in the same step group. If you specify the target by ID, the target step can reside in any step group in the sequence.
- If the
 Step.CustomFalseAction 
 property is
 PostAction_CallCallback 
 , the target is the name of the callback sequence.
- For all other types of post actions, the target property is not used.

This value is an expression. You can set the value with the name of the property that stores the name of the target or with a string constant. A string constant is the name of the target enclosed in double quotation marks.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.CustomActionExpression](step-customactionexpression.html)

[Step.CustomFalseAction](step-customfalseaction.html)

[Step.CustomTrueAction](step-customtrueaction.html)

[Step.CustomTrueActionTargetByExpr](step-customtrueactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-customtrueaction.html language=enus -->
## TOPIC 02717: Step.CustomTrueAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-customtrueaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-customtrueaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CustomTrueAction Data Type String Purpose Specifies the type of action you want to occur when the custom post action expression evaluates to True . Remarks Assign a PostActionValues string constant to the property to specify the type of post action to perform. See Also PostActionValues S

### Step.CustomTrueAction

#### Syntax

[Step](step.html).CustomTrueAction

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the type of action you want to occur when the custom post action expression evaluates to
 True
 .

#### Remarks

Assign a
 [PostActionValues](postactionvalues.html)
 string constant to the property to specify the type of post action to perform.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.CustomActionExpression](step-customactionexpression.html)

[Step.CustomFalseAction](step-customfalseaction.html)

[Step.CustomFalseActionTargetByExpr](step-customfalseactiontargetbyexpr.html)

[Step.CustomTrueActionTargetByExpr](step-customtrueactiontargetbyexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-customtrueactiontarget.html language=enus -->
## TOPIC 02718: Step.CustomTrueActionTarget

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-customtrueactiontarget.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-customtrueactiontarget.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CustomTrueActionTarget Data Type String Purpose This property is obsolete. Use the Step.CustomTrueActionTargetByExpr property instead. Remarks Specifies the target for the post action the Step.CustomTrueAction property specifies. Post action targets are now expressions. If you set the ta

### Step.CustomTrueActionTarget

#### Syntax

[Step](step.html).CustomTrueActionTarget

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Step.CustomTrueActionTargetByExpr

#### Remarks

Specifies the target for the post action the
 [Step.CustomTrueAction](step-customtrueaction.html)
 property specifies. Post action targets are now expressions. If you set the target using this property, TestStand converts the target into a string constant expression before storing it. If you attempt to obtain the target using this property and the target is a string constant expression, TestStand converts it back into the string it represents and returns the string to you. If the target is not a string constant but is a more complex expression, TestStand returns an error if you try to obtain the value using this property.

- If the
 Step.CustomTrueAction 
 property is
 PostAction_GotoStep 
 , the target is the name of the step or the ID of the step. If you specify the target by name, the target step must reside in the same step group. If you specify the target by ID, the target step can reside in any step group in the sequence.
- If the
 Step.CustomTrueAction 
 property is
 PostAction_CallCallback 
 , the target is the name of the callback sequence.
- For all other types of post actions, the target property is not used.

#### See Also

[Step.CustomActionExpression](step-customactionexpression.html)

[Step.CustomFalseAction](step-customfalseaction.html)

[Step.CustomFalseActionTargetByExpr](step-customfalseactiontargetbyexpr.html)

[Step.CustomTrueAction](step-customtrueaction.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-customtrueactiontargetbyexpr.html language=enus -->
## TOPIC 02719: Step.CustomTrueActionTargetByExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-customtrueactiontargetbyexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-customtrueactiontargetbyexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.CustomTrueActionTargetByExpr Data Type String Purpose Specifies the target for the post action the Step.CustomTrueAction property specifies. Remarks If the Step.CustomTrueAction property is PostAction_GotoStep , the target is the name of the step or the ID of the step. If you specify the

### Step.CustomTrueActionTargetByExpr

#### Syntax

[Step](step.html).CustomTrueActionTargetByExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for the post action the
 [Step.CustomTrueAction](step-customtrueaction.html)
 property specifies.

#### Remarks

- If the
 Step.CustomTrueAction 
 property is
 PostAction_GotoStep 
 , the target is the name of the step or the ID of the step. If you specify the target by name, the target step must reside in the same step group. If you specify the target by ID, the target step can reside in any step group in the sequence.
- If the
 Step.CustomTrueAction 
 is
 PostAction_CallCallback 
 , the target is the name of the callback sequence.
- For all other types of post actions, the target property is not used.

This value is an expression. You can set the value with the name of the property that stores the name of the target or with a string constant. A string constant is the name of the target enclosed in double quotation marks.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.CustomActionExpression](step-customactionexpression.html)

[Step.CustomFalseAction](step-customfalseaction.html)

[Step.CustomFalseActionTargetByExpr](step-customfalseactiontargetbyexpr.html)

[Step.CustomTrueAction](step-customtrueaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-description.html language=enus -->
## TOPIC 02720: Step.Description

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-description.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-description.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.Description Data Type String Purpose This property is obsolete. Use the Step.GetDescriptionEx method instead. Remarks Describes the step. You can change this string whenever you modify the step settings. See Also Step.GetDescriptionEx

### Step.Description

#### Syntax

[Step](step.html).Description

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Step.GetDescriptionEx

#### Remarks

Describes the step. You can change this string whenever you modify the step settings.

#### See Also

[Step.GetDescriptionEx](step-getdescriptionex.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-displayadditionalresultsdialog.html language=enus -->
## TOPIC 02721: Step.DisplayAdditionalResultsDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-displayadditionalresultsdialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-displayadditionalresultsdialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.DisplayAdditionalResultsDialog( dlgTitle = "", dlgOptions = 0) Return Value Boolean Returns True if you click OK in the dialog box. Returns False if you click Cancel . Purpose Launches the Additional Results dialog box, in which you can edit additional results for a step. Parameters dlgT

### Step.DisplayAdditionalResultsDialog

#### Syntax

[Step](step.html).DisplayAdditionalResultsDialog( dlgTitle = "", dlgOptions = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box. Returns
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Additional Results](../tsref/additional-results-dialog-box.html)
 dialog box, in which you can edit additional results for a step.

#### Parameters

dlgTitle
 As
 [String](data-types-for-teststand.html)

[In] Specifies the title of the dialog box. Pass an empty string to use the default title for the dialog box.

This parameter has a default value of
 ""
 .

dlgOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of
 [CommonDialogOptions](commondialogoptions.html)
 .

This parameter has a default value of
 0
 .

#### See Also

[Additional Results dialog box](../tsref/additional-results-dialog-box.html)

[CommonDialogOptions](commondialogoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-editasreadonly.html language=enus -->
## TOPIC 02722: Step.EditAsReadOnly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-editasreadonly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-editasreadonly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.EditAsReadOnly Data Type Boolean Purpose Specifies if dialog boxes that edit the step launch in read-only mode. Implement code for such dialog boxes to obtain the value of this property and launch the Edit dialog box in read-only mode if it returns True . The sequence editor sets this pr

### Step.EditAsReadOnly

#### Syntax

[Step](step.html).EditAsReadOnly

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if dialog boxes that edit the step launch in read-only mode. Implement code for such dialog boxes to obtain the value of this property and launch the Edit dialog box in read-only mode if it returns
 True
 . The sequence editor sets this property if the file that contains the step is read-only, if the user does not have sufficient privileges to edit the step, or if executions are currently running.

#### Remarks

When implementing an Edit substep for a step type, this property works in conjunction with the Supports Edit As Read-Only option for the Edit substep in the

[Step Type Properties](../tsref/step-type-properties-dialog-box.html)
 dialog box. The sequence editor does not call the Edit substep for a read-only step unless Supports Edit As Read-Only is
 True
 for the Edit substep. If you do not want to handle launching the dialog box in read-only mode, leave Supports Edit As Read-Only set to
 False
 .

#### See Also

[Step Type Properties dialog box](../tsref/step-type-properties-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-editcode.html language=enus -->
## TOPIC 02723: Step.EditCode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-editcode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-editcode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.EditCode Return Value Boolean Indicates if the step was modified. Purpose Launches an external application to edit the code module associated with this step. Remarks A different application is launched for each adapter. For example, the EditCode method launches LabVIEW for steps created

### Step.EditCode

#### Syntax

[Step](step.html).EditCode

#### Return Value

[Boolean](data-types-for-teststand.html)

Indicates if the step was modified.

#### Purpose

Launches an external application to edit the code module associated with this step.

#### Remarks

A different application is launched for each adapter. For example, the
 EditCode
 method launches LabVIEW for steps created with the LabVIEW Adapter.

For adapters that use Microsoft Visual Studio, calling this method can result in prompts to the user if any of the following conditions exist:

- Multiple versions of Visual Studio exist on the computer and you select the
 Always Prompt for Version 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the
 Adapter Configuration 
 dialog box.
- Multiple versions of Visual Studio exist on the computer and you select the
 Use the Version that Matches the Project File 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the Adapter Configuration dialog box, and TestStand cannot match the version of the file.
- The specified solution does not contain the specified project.
- The specified project does not contain the specified source file.

#### See Also

[Adapter Configuration dialog box](../tsref/adapter-configuration-dialog-box.html)

[Step.CanEditCode](step-caneditcode.html)

[Step.CreateCode](step-createcode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-evalprecondforinteractiveexecution.html language=enus -->
## TOPIC 02724: Step.EvalPrecondForInteractiveExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-evalprecondforinteractiveexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-evalprecondforinteractiveexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.EvalPrecondForInteractiveExecution Data Type EvalPrecondOptions Use the following constants with this data type: EvalPrecondOption_EvaluatePrecond –(Value: 1) Evaluates the precondition. EvalPrecondOption_NoEvaluatePrecond –(Value: 2) Does not evaluate the precondition. EvalPrecondOption

### Step.EvalPrecondForInteractiveExecution

#### Syntax

[Step](step.html).EvalPrecondForInteractiveExecution

#### Data Type

[EvalPrecondOptions](evalprecondoptions.html)

Use the following constants with this data type:

- EvalPrecondOption_EvaluatePrecond 
 –(Value: 1) Evaluates the precondition.
- EvalPrecondOption_NoEvaluatePrecond 
 –(Value: 2) Does not evaluate the precondition.
- EvalPrecondOption_UseStationOption 
 –(Value: 0) Uses the Evaluate Preconditions in Interactive Mode option on the
 Execution tab 
 of the
 Station Options 
 dialog box.

#### Purpose

Specifies if TestStand evaluates the step precondition when you run the step interactively.

#### See Also

[Execution tab](../tsref/execution-tab-station-options-dialog-box.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[Step.Precondition](step-precondition.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-executeeditsubstep.html language=enus -->
## TOPIC 02725: Step.ExecuteEditSubstep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-executeeditsubstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-executeeditsubstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.ExecuteEditSubstep Return Value Boolean Returns True if the Edit substep modifies the step. Purpose This method is obsolete. Use the Step.ExecuteSubstep method instead. Remarks Executes the first Edit substep for the step, if one exists. Check the Step.CanExecuteEditSubstep property befo

### Step.ExecuteEditSubstep

#### Syntax

[Step](step.html).ExecuteEditSubstep

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the Edit substep modifies the step.

#### Purpose

Note

Step.ExecuteSubstep

#### Remarks

Executes the first Edit substep for the step, if one exists. Check the
 [Step.CanExecuteEditSubstep](step-canexecuteeditsubstep.html)
 property before calling this method.

#### See Also

[Step.CanExecuteSubstep](step-canexecutesubstep.html)

[Step.ExecuteSubstep](step-executesubstep.html)

Parent topic:

Obsolete Step Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-executesubstep.html language=enus -->
## TOPIC 02726: Step.ExecuteSubstep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-executesubstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-executesubstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.ExecuteSubstep( substepIndex, [sequenceContextParam]) Return Value Boolean Returns True if the substep indicates that it modified the step by incrementing the sequence file change count. Typically, only Edit substeps increment the sequence file change count. Purpose Executes a step type

### Step.ExecuteSubstep

#### Syntax

[Step](step.html).ExecuteSubstep( substepIndex, [sequenceContextParam])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the substep indicates that it modified the step by incrementing the sequence file change count. Typically, only Edit substeps increment the sequence file change count.

#### Purpose

Executes a step type substep.

#### Remarks

Call this method to execute a substep from the step type of the specified step. Examine the step type to determine the substeps it provides. This method can execute any type of substep including Pre, Post, Edit, or Custom substeps.

Use the
 [PropertyObject.GetArrayOffset](propertyobject-getarrayoffset.html)
 method to obtain the index from the name of a substep. For example:
 RunState.PreviousStep.ExecuteSubstep(RunState.Engine.GetTypeDefinition("MessagePopup").GetArrayOffset("Substeps", 0, "[\"Post\"]"))

#### Parameters

substepIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the substep. Use the
 PropertyObject.GetArrayOffset
 method to obtain the index from the name of a substep.

sequenceContextParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Typically, you pass the current sequence context when you call this method from within a thread of an execution. If you do not pass any value for this parameter, TestStand approximates the sequence context as if you are running the step in a sequence. When executing substeps from a user interface, do not pass any value for this parameter.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[PropertyObject.GetArrayOffset](propertyobject-getarrayoffset.html)

[SequenceContext](sequencecontext.html)

[SequenceFile.ChangeCount](sequencefile-changecount.html)

[Step.StepType](step-steptype.html)

[StepType.GetSubstep](steptype-getsubstep.html)

[StepType.NumSubsteps](steptype-numsubsteps.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-failaction.html language=enus -->
## TOPIC 02727: Step.FailAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-failaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-failaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.FailAction Data Type String Purpose Specifies the type of post action you want to occur if the step fails. Remarks Assign a PostActionValues string constant to the property to specify the type of post action to perform. See Also PostActionValues Step.FailActionTargetByExpr Step.PassActio

### Step.FailAction

#### Syntax

[Step](step.html).FailAction

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the type of post action you want to occur if the step fails.

#### Remarks

Assign a
 [PostActionValues](postactionvalues.html)
 string constant to the property to specify the type of post action to perform.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.FailActionTargetByExpr](step-failactiontargetbyexpr.html)

[Step.PassAction](step-passaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-failactiontarget.html language=enus -->
## TOPIC 02728: Step.FailActionTarget

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-failactiontarget.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-failactiontarget.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.FailActionTarget Data Type String Purpose This property is obsolete. Use the Step.FailActionTargetByExpr property instead. Remarks Specifies the target for the post action the Step.FailAction property specifies. Post action targets are now expressions. If you set the target using this pr

### Step.FailActionTarget

#### Syntax

[Step](step.html).FailActionTarget

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Step.FailActionTargetByExpr

#### Remarks

Specifies the target for the post action the
 Step.FailAction
 property specifies. Post action targets are now expressions. If you set the target using this property, TestStand converts the target into a string constant expression before storing it. If you attempt to obtain the target using this property and it is a string constant expression, TestStand converts the target back into the string it represents and returns the string to you. If the target is not a string constant but is a more complex expression, TestStand returns an error if you try to obtain the value using this property.

If the
 Step.FailAction
 property is
 [PostAction_GotoStep](postactionvalues.html)
 , the target is the name of the step. If the
 Step.FailAction
 property is
 [PostAction_CallCallback](postactionvalues.html)
 , the target is the name of the callback sequence. For all other types of post actions, the target property is not used.

#### See Also

[PostActionValues](postactionvalues.html)

[Step.FailAction](step-failaction.html)

[Step.FailActionTargetByExpr](step-failactiontargetbyexpr.html)

Parent topic:

Obsolete Step Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-failactiontargetbyexpr.html language=enus -->
## TOPIC 02729: Step.FailActionTargetByExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-failactiontargetbyexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-failactiontargetbyexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.FailActionTargetByExpr Data Type String Purpose Specifies the target for the post action that the Step.FailAction property specifies. Remarks If the Step.FailAction property is PostAction_GotoStep , the target is the name of the step. If the Step.FailAction property is PostAction_CallCal

### Step.FailActionTargetByExpr

#### Syntax

[Step](step.html).FailActionTargetByExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the target for the post action that the
 [Step.FailAction](step-failaction.html)
 property specifies.

#### Remarks

If the
 Step.FailAction
 property is
 [PostAction_GotoStep](postactionvalues.html)
 , the target is the name of the step. If the
 Step.FailAction
 property is
 [PostAction_CallCallback](postactionvalues.html)
 , the target is the name of the callback sequence. For all other types of post actions, the target property is not used.

This value is an expression. You can set the value with the name of the property that stores the name of the target or with a string constant (the name of the target in quotation marks).

#### See Also

[PostActionValues](postactionvalues.html)

[Step.FailAction](step-failaction.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-getbreakonstepex.html language=enus -->
## TOPIC 02730: Step.GetBreakOnStepEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-getbreakonstepex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-getbreakonstepex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.GetBreakOnStepEx( [executionParam]) Return Value Boolean Returns True if a breakpoint is set on the step. Purpose This method is obsolete. Use the Step.GetBreakSettings method instead. Remarks Determines if a breakpoint is set on the step. Parameters executionParam As Variant [In] [ Opti

### Step.GetBreakOnStepEx

#### Syntax

[Step](step.html).GetBreakOnStepEx( [executionParam])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if a breakpoint is set on the step.

#### Purpose

Note

Step.GetBreakSettings

#### Remarks

Determines if a breakpoint is set on the step.

#### Parameters

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a reference to an Execution object to obtain the breakpoint settings on a step, which apply to a particular execution. If there is no execution-specific breakpoint setting or if you do not pass an Execution object, the method returns the breakpoint setting on the step of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Step.GetBreakSettings](step-getbreaksettings.html)

[Step.SetBreakSettings](step-setbreaksettings.html)

Parent topic:

Obsolete Step Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-getbreaksettings.html language=enus -->
## TOPIC 02731: Step.GetBreakSettings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-getbreaksettings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-getbreaksettings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.GetBreakSettings( isSet, enabled, passCount, Condition, [executionParam]) Purpose Returns a value that indicates whether the step of a sequence is set to break. Parameters isSet As Boolean [Out] Returns a value that indicates whether the breakpoint is set. enabled As Boolean [Out] Return

### Step.GetBreakSettings

#### Syntax

[Step](step.html).GetBreakSettings( isSet, enabled, passCount, Condition, [executionParam])

#### Purpose

Returns a value that indicates whether the step of a sequence is set to break.

#### Parameters

isSet
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the breakpoint is set.

enabled
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the breakpoint is enabled. TestStand ignores disabled breakpoints during execution.

passCount
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the number of times the execution must evaluate the condition expression before suspending the execution. Pass
 0
 if you do not want to use a conditional pass count.

Condition
 As
 [String](data-types-for-teststand.html)

[Out] Returns the expression that must evaluate to
 True
 before suspending the execution. An empty value defaults to
 True
 . If you specify a non-zero pass count value and a condition expression for the breakpoint, the pass count only decrements when the expression evaluates to
 True
 .

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a reference to an Execution object to obtain the breakpoint settings on a step, which apply to a particular execution. If there is no execution-specific breakpoint setting or if you do not pass an Execution object, the method returns the breakpoint setting on the step of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Sequence.GetBreakOnEndSettings](sequence-getbreakonendsettings.html)

[Sequence.SetBreakOnEndSettings](sequence-setbreakonendsettings.html)

[Step.SetBreakSettings](step-setbreaksettings.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-getdescriptionex.html language=enus -->
## TOPIC 02732: Step.GetDescriptionEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-getdescriptionex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-getdescriptionex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.GetDescriptionEx( options = 0) Return Value String Purpose Returns a description string for the step. Remarks This string can change whenever you modify any of the step settings. Parameters options As Long [In] Specifies one or more StepDescriptionOptions constants. Use the bitwise-OR op

### Step.GetDescriptionEx

#### Syntax

[Step](step.html).GetDescriptionEx( options = 0)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns a description string for the step.

#### Remarks

This string can change whenever you modify any of the step settings.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [StepDescriptionOptions](stepdescriptionoptions.html)
 constants. Use the bitwise-OR operator to specify multiple sequence file flags.

This parameter has a default value of
 0
 .

#### See Also

[StepDescriptionOptions](stepdescriptionoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-geteditsubstepmenustructure.html language=enus -->
## TOPIC 02733: Step.GetEditSubstepMenuStructure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-geteditsubstepmenustructure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-geteditsubstepmenustructure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.GetEditSubstepMenuStructure Return Value PropertyObject The object that specifies the menu structure. See MenuItemProperties for a description of this property object. Purpose Returns the menu structure for the Edit substeps associated with the step type of the step. Remarks A step type

### Step.GetEditSubstepMenuStructure

#### Syntax

[Step](step.html).GetEditSubstepMenuStructure

#### Return Value

[PropertyObject](propertyobject.html)

The object that specifies the menu structure. See
 [MenuItemProperties](menuitemproperties.html)
 for a description of this property object.

#### Purpose

Returns the menu structure for the Edit substeps associated with the step type of the step.

#### Remarks

A step type can have more than one Edit substep associated with it. This function returns an object that describes the menu used to select an Edit substep to execute.

#### See Also

[MenuItemProperties](menuitemproperties.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-getexecutionflowstring.html language=enus -->
## TOPIC 02734: Step.GetExecutionFlowString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-getexecutionflowstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-getexecutionflowstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.GetExecutionFlowString( options = 0, [executionParam]) Return Value String Purpose This method is obsolete. Use the Step.GetStepSettingsString method instead. Remarks Returns a string description of the execution flow settings for this step. Execution flow settings include preconditions,

### Step.GetExecutionFlowString

#### Syntax

[Step](step.html).GetExecutionFlowString( options = 0, [executionParam])

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Note

Step.GetStepSettingsString

#### Remarks

Returns a string description of the execution flow settings for this step.

Execution flow settings include preconditions, post actions, loop settings, and run mode. This string can change whenever you modify any of the step settings.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a
 [StepDescriptionOptions](stepdescriptionoptions.html)
 constant. Use the bitwise-OR operator to specify multiple StepDescriptionOptions constants.

This parameter has a default value of
 0
 .

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a reference to an Execution object if you want to obtain the run mode that applies to a particular execution. If there is no execution-specific run mode for the step or if you do not pass an Execution object, the method returns the run mode setting of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Step.GetDescriptionEx](step-getdescriptionex.html)

[Step.GetStepSettingsString](step-getstepsettingsstring.html)

[Step.Name](step-name.html)

[StepDescriptionOptions](stepdescriptionoptions.html)

Parent topic:

Obsolete Step Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-getresultstatusdisplaystring.html language=enus -->
## TOPIC 02735: Step.GetResultStatusDisplayString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-getresultstatusdisplaystring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-getresultstatusdisplaystring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.GetResultStatusDisplayString Return Value String Purpose Returns a localized string description of the step result. See Also Step.ResultStatus

### Step.GetResultStatusDisplayString

#### Syntax

[Step](step.html).GetResultStatusDisplayString

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns a localized string description of the step result.

#### See Also

[Step.ResultStatus](step-resultstatus.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-getrunmodeex.html language=enus -->
## TOPIC 02736: Step.GetRunModeEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-getrunmodeex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-getrunmodeex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.GetRunModeEx( [executionParam]) Return Value String Returns a run mode string. The RunModes constants define the valid return values for this method. Purpose Obtains the run mode of a step. Remarks You can get the run mode for either the sequence file or for a particular execution. If yo

### Step.GetRunModeEx

#### Syntax

[Step](step.html).GetRunModeEx( [executionParam])

#### Return Value

[String](data-types-for-teststand.html)

Returns a run mode string. The
 [RunModes](runmodes.html)
 constants define the valid return values for this method.

#### Purpose

Obtains the run mode of a step.

#### Remarks

You can get the run mode for either the sequence file or for a particular execution. If you pass an Execution object for the
 executionParam
 parameter, the run mode the method returns is the one that you set for that execution. If no execution-specific run mode exists or if you do not pass an Execution object, this method returns the run mode of the sequence file.

#### Parameters

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a reference to an Execution object if you want to obtain the run mode that applies to a particular execution.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[RunModes](runmodes.html)

[Step.SetRunModeEx](step-setrunmodeex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-getstepsettingsstring.html language=enus -->
## TOPIC 02737: Step.GetStepSettingsString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-getstepsettingsstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-getstepsettingsstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.GetStepSettingsString( options = 0, executionParam = NULL) Return Value String Purpose Returns a string description of the step settings. Remarks The string description includes information about settings such as synchronization, switching, run mode, looping, post actions, preconditions,

### Step.GetStepSettingsString

#### Syntax

[Step](step.html).GetStepSettingsString( options = 0, executionParam = NULL)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns a string description of the step settings.

#### Remarks

The string description includes information about settings such as synchronization, switching, run mode, looping, post actions, preconditions, pre/post/status expressions, module specification, breakpoint options, window activation, result recording, module loading and unloading, ignoring of run-time errors and termination, subsequence tracing, and whether a step failure causes a sequence failure. This property returns a string that can change whenever you modify any of the step settings.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a
 [StepDescriptionOptions](stepdescriptionoptions.html)
 constant. Use the bitwise-OR operator to specify multiple
 StepDescriptionOptions
 constants.

This parameter has a default value of
 0
 .

executionParam
 As
 [Execution](execution.html)

[In] Specifies a reference to an Execution object to retrieve execution specific settings for a running instance of the step.

This parameter has a default value of
 NULL
 .

#### See Also

[Execution](execution.html)

[StepDescriptionOptions](stepdescriptionoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-iconname.html language=enus -->
## TOPIC 02738: Step.IconName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-iconname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-iconname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.IconName Data Type String Purpose Specifies the filename of the icon for the step. Remarks If the step type has no icon file, the property returns the icon filename for the module adapter the step uses. Icon files are located in the <TestStand> \Components\Icons and <TestStand Public>\Co

### Step.IconName

#### Syntax

[Step](step.html).IconName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the filename of the icon for the step.

#### Remarks

If the step type has no icon file, the property returns the icon filename for the module adapter the step uses.

Icon files are located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories.

#### See Also

[Adapter](adapter.html)

[Step.LargeIcon](step-largeicon.html)

[Step.SmallIcon](step-smallicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-ignorerte.html language=enus -->
## TOPIC 02739: Step.IgnoreRTE

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-ignorerte.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-ignorerte.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.IgnoreRTE Data Type Boolean Purpose Prevents the step from reporting a run-time error to the sequence. Remarks When a step causes a run-time error, the step stops executing and TestStand sets the status of the step to Error . If you set this property to False , TestStand also sets the in

### Step.IgnoreRTE

#### Syntax

[Step](step.html).IgnoreRTE

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Prevents the step from reporting a run-time error to the sequence.

#### Remarks

When a step causes a run-time error, the step stops executing and TestStand sets the status of the step to
 Error
 .

If you set this property to
 False
 , TestStand also sets the internal status of the sequence to
 Error
 and the execution branches to the Cleanup step group for the sequence.

If you set this property to
 True
 , TestStand does not set the internal status of the sequence to
 Error
 . Instead, TestStand resets the
 Error.Occurred
 property of the step to
 False
 and execution continues normally with the next step. The value of the
 Result.Status
 property remains as
 Error
 for the step.

#### See Also

[RunModes](runmodes.html)

[StationOptions.RTEOption](stationoptions-rteoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-issequencecall.html language=enus -->
## TOPIC 02740: Step.IsSequenceCall

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-issequencecall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-issequencecall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.IsSequenceCall Data Type Boolean Purpose Returns True if the step is a Sequence Call step.

### Step.IsSequenceCall

#### Syntax

[Step](step.html).IsSequenceCall

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the step is a Sequence Call step.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-largeicon.html language=enus -->
## TOPIC 02741: Step.LargeIcon

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-largeicon.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-largeicon.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LargeIcon Data Type Picture Purpose Returns the large version of the icon that represents the step. Remarks The step type of the step defines the icon the property returns. If the step type does not specify an icon, the property returns the icon the Adapter of the step specifies. See Als

### Step.LargeIcon

#### Syntax

[Step](step.html).LargeIcon

#### Data Type

[Picture](data-types-for-teststand.html)

#### Purpose

Returns the large version of the icon that represents the step.

#### Remarks

The step type of the step defines the icon the property returns. If the step type does not specify an icon, the property returns the icon the
 [Adapter](adapter.html)
 of the step specifies.

#### See Also

[Adapter](adapter.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Step.IconName](step-iconname.html)

[Step.LargeIconIndex](step-largeiconindex.html)

[Step.SmallIcon](step-smallicon.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-largeiconindex.html language=enus -->
## TOPIC 02742: Step.LargeIconIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-largeiconindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-largeiconindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LargeIconIndex Data Type Long Purpose Returns a unique index for the large version of the icon that represents the step. You can use this index to retrieve the icon image from the image list you obtain with the Engine.LargeImageListEx property. See Also Engine.LargeImageListEx Step.IconN

### Step.LargeIconIndex

#### Syntax

[Step](step.html).LargeIconIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique index for the large version of the icon that represents the step. You can use this index to retrieve the icon image from the image list you obtain with the
 [Engine.LargeImageListEx](engine-largeimagelistex.html)
 property.

#### See Also

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Step.IconName](step-iconname.html)

[Step.LargeIcon](step-largeicon.html)

[Step.SmallIconIndex](step-smalliconindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-laststepresult.html language=enus -->
## TOPIC 02743: Step.LastStepResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-laststepresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-laststepresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LastStepResult Data Type PropertyObject Purpose Specifies the PropertyObject object that holds the result of the current or most recent step execution. Remarks You can set this property to NULL (Nothing) in a step or substep module to remove the step result from the result list. If you s

### Step.LastStepResult

#### Syntax

[Step](step.html).LastStepResult

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Specifies the PropertyObject object that holds the result of the current or most recent step execution.

#### Remarks

You can set this property to
 NULL
 (Nothing) in a step or substep module to remove the step result from the result list. If you set this property to a value other than
 NULL
 or if you set the property when the step is not executing, the result list does not change.

This property does not return loop iteration results.

#### See Also

[PropertyObject](propertyobject.html)

[Step.CurrentLoopResult](step-currentloopresult.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-loadmodule.html language=enus -->
## TOPIC 02744: Step.LoadModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-loadmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-loadmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LoadModule( loadOptions = 0, [sequenceContextParam]) Return Value Boolean Returns True on success or False if the module fails to load. Purpose Loads the code module for the step. Parameters loadOptions As Long [In] Specifies one or more LoadModuleOptions using the bitwise-OR operator to

### Step.LoadModule

#### Syntax

[Step](step.html).LoadModule( loadOptions = 0, [sequenceContextParam])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 on success or
 False
 if the module fails to load.

#### Purpose

Loads the code module for the step.

#### Parameters

loadOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [LoadModuleOptions](loadmoduleoptions.html)
 using the bitwise-OR operator to modify the behavior of this method.

This parameter has a default value of
 0
 .

sequenceContextParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If passing the
 [LoadModule_EvaluateExpressions](loadmoduleoptions.html)
 flag to the
 loadOptions
 parameter, pass a
 [SequenceContext](sequencecontext.html)
 object for this parameter to use when evaluating the expressions. Also, if you are calling this method from a step in an execution, pass the sequence context of the execution.

#### See Also

[LoadModuleOptions](loadmoduleoptions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[SequenceContext](sequencecontext.html)

[Step.UnloadModule](step-unloadmodule.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-logadditionalresult.html language=enus -->
## TOPIC 02745: Step.LogAdditionalResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-logadditionalresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-logadditionalresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LogAdditionalResult( resultValue, resultName = "", resultPropertyFlags = PropFlags_IncludeInReport) Purpose If the step is currently executing, this method adds a custom additional result to the step results. Remarks If the step is looping, this method adds a custom additional result to

### Step.LogAdditionalResult

#### Syntax

[Step](step.html).LogAdditionalResult( resultValue, resultName = "", resultPropertyFlags = PropFlags_IncludeInReport)

#### Purpose

If the step is currently executing, this method adds a custom additional result to the step results.

#### Remarks

If the step is looping, this method adds a custom additional result to the
 [Step.CurrentLoopResult](step-currentloopresult.html)
 . If the step is not looping, this method adds a custom additional result to
 [Step.LastStepResult](step-laststepresult.html)
 property.

This method returns an error if the step is not executing. This method performs no action if you disable result recording.

This method does not affect the additional result settings of the step that you programmatically configure using the
 [Step.AdditionalResults](step-additionalresults.html)
 property.

#### Parameters

resultValue
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the value of the additional result.

resultName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the additional result. Pass an empty string to use the name of the object you passed for the
 resultValue
 parameter.

This parameter has a default value of
 ""
 .

resultPropertyFlags
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the
 [PropertyFlags](propertyflags.html)
 of the additional result. You must include the
 PropFlags_IncludeInReport
 flag for the additional result to appear in the report.

This parameter has a default value of
 PropFlags_IncludeInReport
 .

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-loopincexpression.html language=enus -->
## TOPIC 02746: Step.LoopIncExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-loopincexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-loopincexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LoopIncExpression Data Type String Purpose Specifies the loop increment expression for the step. See Also Step.LoopInitExpression Step.LoopStatusExpression Step.LoopType Step.LoopWhileExpression

### Step.LoopIncExpression

#### Syntax

[Step](step.html).LoopIncExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the loop increment expression for the step.

#### See Also

[Step.LoopInitExpression](step-loopinitexpression.html)

[Step.LoopStatusExpression](step-loopstatusexpression.html)

[Step.LoopType](step-looptype.html)

[Step.LoopWhileExpression](step-loopwhileexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-loopinitexpression.html language=enus -->
## TOPIC 02747: Step.LoopInitExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-loopinitexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-loopinitexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LoopInitExpression Data Type String Purpose Specifies the loop initialization expression for the step. See Also Step.LoopIncExpression Step.LoopStatusExpression Step.LoopType Step.LoopWhileExpression

### Step.LoopInitExpression

#### Syntax

[Step](step.html).LoopInitExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the loop initialization expression for the step.

#### See Also

[Step.LoopIncExpression](step-loopincexpression.html)

[Step.LoopStatusExpression](step-loopstatusexpression.html)

[Step.LoopType](step-looptype.html)

[Step.LoopWhileExpression](step-loopwhileexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-loopstatusexpression.html language=enus -->
## TOPIC 02748: Step.LoopStatusExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-loopstatusexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-loopstatusexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LoopStatusExpression Data Type String Purpose Specifies the loop status result expression for the step. See Also Step.LoopIncExpression Step.LoopInitExpression Step.LoopType Step.LoopWhileExpression

### Step.LoopStatusExpression

#### Syntax

[Step](step.html).LoopStatusExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the loop status result expression for the step.

#### See Also

[Step.LoopIncExpression](step-loopincexpression.html)

[Step.LoopInitExpression](step-loopinitexpression.html)

[Step.LoopType](step-looptype.html)

[Step.LoopWhileExpression](step-loopwhileexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-looptype.html language=enus -->
## TOPIC 02749: Step.LoopType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-looptype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-looptype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LoopType Data Type String Purpose Specifies the type of looping for the step. Remarks Use the StepLoopTypes constants to specify the value of the property. See Also Step.LoopIncExpression Step.LoopInitExpression Step.LoopStatusExpression Step.LoopWhileExpression StepLoopTypes

### Step.LoopType

#### Syntax

[Step](step.html).LoopType

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the type of looping for the step.

#### Remarks

Use the
 [StepLoopTypes](steplooptypes.html)
 constants to specify the value of the property.

#### See Also

[Step.LoopIncExpression](step-loopincexpression.html)

[Step.LoopInitExpression](step-loopinitexpression.html)

[Step.LoopStatusExpression](step-loopstatusexpression.html)

[Step.LoopWhileExpression](step-loopwhileexpression.html)

[StepLoopTypes](steplooptypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/step-loopwhileexpression.html language=enus -->
## TOPIC 02750: Step.LoopWhileExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/step-loopwhileexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/step-loopwhileexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step.LoopWhileExpression Data Type String Purpose Specifies the While Loop expression for the step. See Also Step.LoopIncExpression Step.LoopInitExpression Step.LoopStatusExpression Step.LoopType

### Step.LoopWhileExpression

#### Syntax

[Step](step.html).LoopWhileExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the While Loop expression for the step.

#### See Also

[Step.LoopIncExpression](step-loopincexpression.html)

[Step.LoopInitExpression](step-loopinitexpression.html)

[Step.LoopStatusExpression](step-loopstatusexpression.html)

[Step.LoopType](step-looptype.html)

Parent topic:

Properties
