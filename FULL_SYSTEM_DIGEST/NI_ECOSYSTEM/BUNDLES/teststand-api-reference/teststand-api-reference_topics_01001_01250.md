# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=1001 end=1250 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineinitializer-setenvironmentpath.html language=enus -->
## TOPIC 01001: EngineInitializer.SetEnvironmentPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineinitializer-setenvironmentpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineinitializer-setenvironmentpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EngineInitializer.SetEnvironmentPath Purpose Specify the environment configuration (.tsenv) file to use to initialize the TestStand engine. Pass an empty string to specify the global environment. Remarks Calling SetEnvironmentPath is unnecessary if you wish to run in the global environment. I

### EngineInitializer.SetEnvironmentPath

#### Syntax

[EngineInitializer](engineinitializer.html).SetEnvironmentPath

#### Purpose

Specify the environment configuration (.tsenv) file to use to initialize the TestStand engine. Pass an empty string to specify the global environment.

#### Remarks

Calling SetEnvironmentPath is unnecessary if you wish to run in the global environment. If no call to SetEnvironmentPath has been made prior to startup, the engine defaults to the global environment. You may call SetEnvironmentPath multiple times before creating the TestStand engine. Each call supersedes the prior calls.

SetEnvironmentPath throws an exception if you call it after the engine has already been created.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engineinitializer.html language=enus -->
## TOPIC 01002: EngineInitializer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engineinitializer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engineinitializer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Methods CanSetEnvironmentPath SetEnvironmentPath

### EngineInitializer

#### Methods

| CanSetEnvironmentPath |
| --- |
| SetEnvironmentPath |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/escapingoptions.html language=enus -->
## TOPIC 01003: EscapingOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/escapingoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/escapingoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the options parameter of the Utility.Escape and Utility.Unescape methods. The options parameter specifies to add quotation marks or to remove quotation marks while escaping or unescaping. EscapingOption_NoOptions –(Value: 0) Default behavior. TestStand does not add or

### EscapingOptions

Use these constants to specify the
 options
 parameter of the
 [Utility.Escape](utility-escape.html)
 and
 [Utility.Unescape](utility-unescape.html)
 methods. The
 options
 parameter specifies to add quotation marks or to remove quotation marks while escaping or unescaping.

- EscapingOption_NoOptions 
 –(Value: 0) Default behavior. TestStand does not add or remove quotation marks after escaping or unescaping.
- EscapingOption_SurroundedByQuotes 
 –(Value: 1) For the
 Utility.Escape 
 method, TestStand surrounds the returned string with quotation marks after escaping the string. For the
 Utility.Unescape 
 method, TestStand removes the surrounding quotation marks before unescaping the string. The
 Utility.Unescape 
 method returns an error if you use this option and the string to unescape is not surrounded by quotation marks.

#### See Also

[Engine.Utility](engine-utility.html)

[Utility.Escape](utility-escape.html)

[Utility.Unescape](utility-unescape.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/evalprecondoptions.html language=enus -->
## TOPIC 01004: EvalPrecondOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/evalprecondoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/evalprecondoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the EvalPrecondOptions parameter of the Step.EvalPrecondForInteractiveExecution and StepType.EvalPrecondForInteractiveExecution properties. EvalPrecondOption_EvaluatePrecond –(Value: 1) Evaluates the precondition. EvalPrecondOption_NoEvaluatePrecond –(Value: 2) Does no

### EvalPrecondOptions

Use these constants to specify the
 EvalPrecondOptions
 parameter of the
 [Step.EvalPrecondForInteractiveExecution](step-evalprecondforinteractiveexecution.html)
 and
 [StepType.EvalPrecondForInteractiveExecution](steptype-evalprecondforinteractiveexecution.html)
 properties.

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

#### See Also

[Execution tab](../tsref/execution-tab-station-options-dialog-box.html)

[ExecutionMask](executionmask.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[StationOptions.ExecutionMask](stationoptions-executionmask.html)

[Step.EvalPrecondForInteractiveExecution](step-evalprecondforinteractiveexecution.html)

[StepType.EvalPrecondForInteractiveExecution](steptype-evalprecondforinteractiveexecution.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/evaluationoptions.html language=enus -->
## TOPIC 01005: EvaluationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/evaluationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/evaluationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the evaluationOptions parameter of the PropertyObject.EvaluateEx , Expression.Evaluate , Expression.Validate , ExpressionEdit.Evaluate , and Engine.CheckExpression methods. Use the bitwise-OR operator to specify more than one option. EvalOption_

### EvaluationOptions

These constants represent the options you can use with the
 evaluationOptions
 parameter of the
 [PropertyObject.EvaluateEx](propertyobject-evaluateex.html)
 ,
 [Expression.Evaluate](expression-evaluate.html)
 ,
 [Expression.Validate](expression-validate.html)
 ,
 
 [ExpressionEdit.Evaluate](../tsuiref/expressionedit-evaluate.html)
 , and
 [Engine.CheckExpression](engine-checkexpression.html)
 methods. Use the bitwise-OR operator to specify more than one option.

- EvalOption_AllowEmptyExpression 
 –(Value: 0x2) Use this option to prevent TestStand from treating empty expressions as syntax errors.
- EvalOption_AllowIndexingEmptyArrays 
 –(Value: 0x4) Use this option to direct TestStand to return a value with a type that is the array element type for empty arrays with subscripts. If you do not specify this option, TestStand treats an empty array with subscripts as an error.
- EvalOption_CreateNonExistentVariables 
 –(Value: 0x8) Use this option to have TestStand create temporary objects for variables that do not exist in an expression. This option is useful when evaluating an expression for error checking if the expression might contain dynamically created variables.
- EvalOption_DoNotAlterValues 
 –(Value: 0x1) Use this option to prevent TestStand from altering the value of any variable or property the expression contains. The
 Expression.Validate 
 and
 Engine.CheckExpression 
 methods do not use this value because these methods never alter values.
- EvalOption_ForErrorChecking 
 –(Value: 0x10) Use this option to direct TestStand to evaluate the expression in order to check the expression for errors. This option makes errors reported at edit time more closely match errors that might occur at run time. For example, when using this option, expressions do not use short-circuit evaluation, ensuring that TestStand checks the entire expression for errors. This option also enables the behavior of the
 #NoValidation 
 directive. Expression validation methods, such as
 Engine.CheckExpression 
 and
 Expression.ValidateEvaluationType 
 , automatically include this option.
- EvalOption_IgnoreNoValidationDirective 
 –(Value: 0x20) This option disables the behavior of the
 #NoValidation 
 directive when checking an expression for errors. Use this option to find errors the
 #NoValidation 
 directive normally suppresses.
- EvalOption_NoOptions 
 –(Value: 0x0) No options.

#### See Also

[Engine.CheckExpression](engine-checkexpression.html)

[Expression.Evaluate](expression-evaluate.html)

[Expression.Validate](expression-validate.html)

[ExpressionEdit.Evaluate](../tsuiref/expressionedit-evaluate.html)

[PropertyObject.EvaluateEx](propertyobject-evaluateex.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/evaluationtypes-allowedarrayrepresentations.html language=enus -->
## TOPIC 01006: EvaluationTypes.AllowedArrayRepresentations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/evaluationtypes-allowedarrayrepresentations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/evaluationtypes-allowedarrayrepresentations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EvaluationTypes.AllowedArrayRepresentations Data Type PropertyRepresentations Use the following constants with this data type: PropertyRepresentation_Float64 –(Value: 1) Specifies double-precision, 64-bit floating-point representation. PropertyRepresentation_Int64 –(Value: 2) Specifies signed

### EvaluationTypes.AllowedArrayRepresentations

#### Syntax

[EvaluationTypes](evaluationtypes.html).AllowedArrayRepresentations

#### Data Type

[PropertyRepresentations](propertyrepresentations.html)

Use the following constants with this data type:

- PropertyRepresentation_Float64 
 –(Value: 1) Specifies double-precision, 64-bit floating-point representation.
- PropertyRepresentation_Int64 
 –(Value: 2) Specifies signed 64-bit integer representation.
- PropertyRepresentation_None 
 –(Value: 0) This is the default representation for non-numeric property objects.
- PropertyRepresentation_UInt64 
 –(Value: 3) Specifies unsigned 64-bit integer representation.

#### Purpose

Specifies the expected representation for an expression. The
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method returns
 TS_Err_NoError
 if the expression evaluates to a numeric array property with a representation that any element of this property specifies.

#### Remarks

The
 [EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)
 property must include
 PropValTypeFlag_NumberArray
 to use this property.

#### See Also

[EvaluationTypes.AllowedRepresentations](evaluationtypes-allowedrepresentations.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[PropertyValueTypeFlags](propertyvaluetypeflags.html)

[TSError](tserror.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/evaluationtypes-allowedrepresentations.html language=enus -->
## TOPIC 01007: EvaluationTypes.AllowedRepresentations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/evaluationtypes-allowedrepresentations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/evaluationtypes-allowedrepresentations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EvaluationTypes.AllowedRepresentations Data Type PropertyRepresentations Use the following constants with this data type: PropertyRepresentation_Float64 –(Value: 1) Specifies double-precision, 64-bit floating-point representation. PropertyRepresentation_Int64 –(Value: 2) Specifies signed 64-b

### EvaluationTypes.AllowedRepresentations

#### Syntax

[EvaluationTypes](evaluationtypes.html).AllowedRepresentations

#### Data Type

[PropertyRepresentations](propertyrepresentations.html)

Use the following constants with this data type:

- PropertyRepresentation_Float64 
 –(Value: 1) Specifies double-precision, 64-bit floating-point representation.
- PropertyRepresentation_Int64 
 –(Value: 2) Specifies signed 64-bit integer representation.
- PropertyRepresentation_None 
 –(Value: 0) This is the default representation for non-numeric property objects.
- PropertyRepresentation_UInt64 
 –(Value: 3) Specifies unsigned 64-bit integer representation.

#### Purpose

Specifies the expected representation for an expression. The
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method returns
 TS_Err_NoError
 if the expression evaluates to a numeric property with a representation that any element of this property specifies.

#### Remarks

The
 [EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)
 property must include
 PropValTypeFlag_Number
 to use this property.

#### See Also

[EvaluationTypes.AllowedArrayRepresentations](evaluationtypes-allowedarrayrepresentations.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[PropertyValueTypeFlags](propertyvaluetypeflags.html)

[TSError](tserror.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/evaluationtypes-arrayofnamedtypes.html language=enus -->
## TOPIC 01008: EvaluationTypes.ArrayOfNamedTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/evaluationtypes-arrayofnamedtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/evaluationtypes-arrayofnamedtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EvaluationTypes.ArrayOfNamedTypes Data Type String Array Purpose Represents an array of named types. An expression expects an array of these types. the Expression.ValidateEvaluationType method returns TS_Err_NoError if the expression evaluates to an array of a named type specified by any elem

### EvaluationTypes.ArrayOfNamedTypes

#### Syntax

[EvaluationTypes](evaluationtypes.html).ArrayOfNamedTypes

#### Data Type

[String Array](data-types-for-teststand.html)

#### Purpose

Represents an array of named types. An expression expects an array of these types. the
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method returns
 TS_Err_NoError
 if the expression evaluates to an array of a named type specified by any element of this property. For example, if the elements of this property are CommonResults and Error, the
 Expression.ValidateEvaluationType
 method returns
 TS_Err_NoError
 if the expression evaluates to PropertyObject using an array of CommonResults type or an array of Error type.

#### Remarks

The
 [EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)
 property must include
 PropValTypeFlag_ArrayOfNamedType
 to use this property.

#### See Also

[EvaluationTypes.NamedTypes](evaluationtypes-namedtypes.html)

[EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/evaluationtypes-namedtypes.html language=enus -->
## TOPIC 01009: EvaluationTypes.NamedTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/evaluationtypes-namedtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/evaluationtypes-namedtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EvaluationTypes.NamedTypes Data Type String Array Purpose Specifies the expected named types for an expression. the Expression.ValidateEvaluationType method returns TS_Err_NoError if the expression evaluates to a named type specified by any element of this property. For example, if the elemen

### EvaluationTypes.NamedTypes

#### Syntax

[EvaluationTypes](evaluationtypes.html).NamedTypes

#### Data Type

[String Array](data-types-for-teststand.html)

#### Purpose

Specifies the expected named types for an expression. the
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method returns
 TS_Err_NoError
 if the expression evaluates to a named type specified by any element of this property. For example, if the elements of this property are CommonResults and Error, the
 Expression.ValidateEvaluationType
 method returns
 TS_Err_NoError
 if the expression evaluates to PropertyObject using a CommonResults or Error type.

#### Remarks

The
 [EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)
 property must include
 PropValTypeFlag_NamedType
 to use this property.

#### See Also

[EvaluationTypes.ArrayOfNamedTypes](evaluationtypes-arrayofnamedtypes.html)

[EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[TSError](tserror.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/evaluationtypes-propertyvaluetypeflags.html language=enus -->
## TOPIC 01010: EvaluationTypes.PropertyValueTypeFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/evaluationtypes-propertyvaluetypeflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/evaluationtypes-propertyvaluetypeflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EvaluationTypes.PropertyValueTypeFlags Data Type Long Purpose Specifies the expected types for an expression. Use any combination of property value type flags with this property. The Expression.ValidateEvaluationType method returns TS_Err_NoError if the expression evaluates to any type this p

### EvaluationTypes.PropertyValueTypeFlags

#### Syntax

[EvaluationTypes](evaluationtypes.html).PropertyValueTypeFlags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the expected types for an expression. Use any combination of property value type flags with this property. The
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method returns
 TS_Err_NoError
 if the expression evaluates to any type this property specifies.

#### See Also

[EvaluationTypes.ArrayOfNamedTypes](evaluationtypes-arrayofnamedtypes.html)

[EvaluationTypes.NamedTypes](evaluationtypes-namedtypes.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[PropertyValueTypeFlags](propertyvaluetypeflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/evaluationtypes.html language=enus -->
## TOPIC 01011: EvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/evaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/evaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This interface specifies expected types for evaluating an expression. Obtain an EvaluationTypes object by calling the Engine.NewEvaluationTypes method or through a property of a parameter for a module call such as the LabVIEWParameter.ValidEvaluationTypes property. Pass an instance of EvaluationType

### EvaluationTypes

This interface specifies expected types for evaluating an expression. Obtain an EvaluationTypes object by calling the
 [Engine.NewEvaluationTypes](engine-newevaluationtypes.html)
 method or through a property of a parameter for a module call such as the
 [LabVIEWParameter.ValidEvaluationTypes](labviewparameter-validevaluationtypes.html)
 property. Pass an instance of EvaluationTypes to the
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method to perform type checking on an expression.

#### Properties

| AllowedArrayRepresentations |
| --- |
| AllowedRepresentations |
| ArrayOfNamedTypes |
| NamedTypes |
| PropertyValueTypeFlags |

#### See Also

[ActiveXParameter.ValidEvaluationTypes](activexparameter-validevaluationtypes.html)

[CommonCParameter.ValidEvaluationTypes](commoncparameter-validevaluationtypes.html)

[DotNetParameter.ValidEvaluationTypes](dotnetparameter-validevaluationtypes.html)

[Engine.NewEvaluationTypes](engine-newevaluationtypes.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.GetValidEvaluationTypes](../tsuiref/expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)

[LabVIEWParameter.ValidEvaluationTypes](labviewparameter-validevaluationtypes.html)

[LabVIEWParameterElement.ValidEvaluationTypes](labviewparameterelement-validevaluationtypes.html)

[SequenceCallParameter.ValidEvaluationTypes](sequencecallparameter-validevaluationtypes.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/events.html language=enus -->
## TOPIC 01012: Events

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/events.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/events.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This book contains the events in this class.

### Events

This book contains the events in this class.

Parent topic:

Engine

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-abort.html language=enus -->
## TOPIC 01013: Execution.Abort

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-abort.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-abort.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.Abort Purpose Aborts the execution. Remarks Cleanup step groups do not execute as part of the abort process. If a call to a step module is active, the execution waits for the step module to return. The execution state does not change immediately after the call to this method returns

### Execution.Abort

#### Syntax

[Execution](execution.html).Abort

#### Purpose

Aborts the execution.

#### Remarks

Cleanup step groups do not execute as part of the abort process.

If a call to a step module is active, the execution waits for the step module to return.

The execution state does not change immediately after the call to this method returns, but the state will change before the next step within the execution executes.

#### See Also

[Engine.AbortAll](engine-abortall.html)

[Engine.TerminateAll](engine-terminateall.html)

[Execution.Terminate](execution-terminate.html)

[StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)

[StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-addextraresult.html language=enus -->
## TOPIC 01014: Execution.AddExtraResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-addextraresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-addextraresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.AddExtraResult( propertyName, resultPropertyName) Purpose Specifies a step property for TestStand to copy to the results list after the execution of each step. Remarks TestStand always copies each subproperty within the Result property of each step to the result list. If the step ha

### Execution.AddExtraResult

#### Syntax

[Execution](execution.html).AddExtraResult( propertyName, resultPropertyName)

#### Purpose

Specifies a step property for TestStand to copy to the results list after the execution of each step.

#### Remarks

TestStand always copies each subproperty within the Result property of each step to the result list. If the step has a result property, you can use this function to specify an additional step property to include in the result list. If a step does not have the property you specify, TestStand does not add the property to the result list element for that step. You can add any number of extra results by calling this method repeatedly.

#### Parameters

propertyName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the property name of the property to add to the results. For example, to add the upper limit of Numeric Limit Test steps, pass the name
 "Step.Limits.High"
 .

resultPropertyName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name with which to store the copy of the property in the results list entry for each step.

#### See Also

[Execution.ClearExtraResultList](execution-clearextraresultlist.html)

[Execution.DeleteExtraResult](execution-deleteextraresult.html)

[Execution.ResultObject](execution-resultobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-addpoststepcustomuimessage.html language=enus -->
## TOPIC 01015: Execution.AddPostStepCustomUIMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-addpoststepcustomuimessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-addpoststepcustomuimessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.AddPostStepCustomUIMessage( MsgCode, Expression, CustomUIMessageOptions = kCustomUIMsg_NoOptions) Purpose Associates a new custom user interface message with an execution. Remarks Use this function when you want TestStand to send a custom user interface message based on a user-defin

### Execution.AddPostStepCustomUIMessage

#### Syntax

[Execution](execution.html).AddPostStepCustomUIMessage( MsgCode, Expression, CustomUIMessageOptions = kCustomUIMsg_NoOptions)

#### Purpose

Associates a new custom user interface message with an execution.

#### Remarks

Use this function when you want TestStand to send a custom user interface message based on a user-defined expression. You define the Boolean expression to evaluate after each step executes. If the expression is
 True
 , TestStand sends the custom user interface message.

This message is synchronous. The thread that sends this message suspends until you process it.

This message is sent regardless of the Enable Tracing setting, Disable Result Recording for All Sequences setting, Step Run Mode setting, or Step Result Recording option.

#### Parameters

MsgCode
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the custom user interface message code. You can use more than one custom user interface message associated with the same code. TestStand sends the custom user interface messages when the associated expression evaluates to
 True
 .

Expression
 As
 [String](data-types-for-teststand.html)

[In] Specifies the valid expression to evaluate after each step executes.

CustomUIMessageOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the flags found in
 [CustomPostStepUIMsgOptions](custompoststepuimsgoptions.html)
 .

This parameter has a default value of
 kCustomUIMsg_NoOptions
 .

#### See Also

[CustomPostStepUIMsgOptions](custompoststepuimsgoptions.html)

[Engine.RegisterUIMessage](engine-registeruimessage.html)

[Execution.RemovePostStepCustomUIMessage](execution-removepoststepcustomuimessage.html)

[UIMessage](uimessage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-aspropertyobject.html language=enus -->
## TOPIC 01016: Execution.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the Execution object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### Execution.AsPropertyObject

#### Syntax

[Execution](execution.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the Execution object.

#### Remarks

Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-break.html language=enus -->
## TOPIC 01017: Execution.Break

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-break.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-break.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.Break Purpose Suspends the execution. See Also Engine.BreakAll Execution.BreakOnEntry Execution.Resume Execution.RTEOptionForThisExecution

### Execution.Break

#### Syntax

[Execution](execution.html).Break

#### Purpose

Suspends the execution.

#### See Also

[Engine.BreakAll](engine-breakall.html)

[Execution.BreakOnEntry](execution-breakonentry.html)

[Execution.Resume](execution-resume.html)

[Execution.RTEOptionForThisExecution](execution-rteoptionforthisexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-breakonentry.html language=enus -->
## TOPIC 01018: Execution.BreakOnEntry

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-breakonentry.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-breakonentry.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.BreakOnEntry Data Type Boolean Purpose Returns the value of the breakOnEntry parameter of the method call that started the most recent execution. Remarks Use this read-only property to determine whether the execution was created with the breakAtFirstStep parameter set to True . The

### Execution.BreakOnEntry

#### Syntax

[Execution](execution.html).BreakOnEntry

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns the value of the
 breakOnEntry
 parameter of the method call that started the most recent execution.

#### Remarks

Use this read-only property to determine whether the execution was created with the
 breakAtFirstStep
 parameter set to
 True
 .

The methods that start executions are
 [Engine.NewExecution](engine-newexecution.html)
 ,
 [Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)
 , and
 [RestartEx](execution-restartex.html)
 . If the most recent call was the
 Engine.NewExecution
 or the
 Engine.NewHierarchicalExecution
 method, this property returns the value specified for the
 breakOnFirstStep
 parameter. If the most recent call was the
 Execution.Restart
 method, this property returns the value of the
 breakOnEntryParam
 parameter. If the most recent call was the
 Execution.RestartEx
 method, this property returns
 True
 if the
 restartOptionsParam
 parameter included the
 [RestartOption_BreakOnEntry](restartoptions.html)
 value.

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

[Execution.RestartEx](execution-restartex.html)

[RestartOptions](restartoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-breakonrteforthisexecution.html language=enus -->
## TOPIC 01019: Execution.BreakOnRTEForThisExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-breakonrteforthisexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-breakonrteforthisexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.BreakOnRTEForThisExecution Data Type Boolean Purpose This property is obsolete. Use the Execution.RTEOptionForThisExecution property instead. Remarks Set this property to False if you do not want to receive a break event on run-time errors for the execution. If you set this property

### Execution.BreakOnRTEForThisExecution

#### Syntax

[Execution](execution.html).BreakOnRTEForThisExecution

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.RTEOptionForThisExecution

#### Remarks

Set this property to
 False
 if you do not want to receive a break event on run-time errors for the execution. If you set this property to
 False
 , the next run-time error causes the execution to terminate. Cleanup step groups of the active sequences run as part of the termination procedure.

#### See Also

[Execution.RTEOptionForThisExecution](execution-rteoptionforthisexecution.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-canceltermination.html language=enus -->
## TOPIC 01020: Execution.CancelTermination

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-canceltermination.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-canceltermination.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.CancelTermination Purpose Cancels the termination of a currently terminating execution. Remarks Call this method from within a step. Calling this method from the main thread of the user interface or from within an edit substep of a step type results in deadlock. See Also Engine.Term

### Execution.CancelTermination

#### Syntax

[Execution](execution.html).CancelTermination

#### Purpose

Cancels the termination of a currently terminating execution.

#### Remarks

Call this method from within a step. Calling this method from the main thread of the user interface or from within an edit substep of a step type results in deadlock.

#### See Also

[Engine.TerminateAll](engine-terminateall.html)

[Execution.Terminate](execution-terminate.html)

[Execution.TerminateInteractiveExecution](execution-terminateinteractiveexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-childexecutionids.html language=enus -->
## TOPIC 01021: Execution.ChildExecutionIds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-childexecutionids.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-childexecutionids.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ChildExecutionIds Data Type Long Array Purpose Returns the child execution IDs for a given execution object. See Also Engine.GetExecution Execution.ParentExecutionId

### Execution.ChildExecutionIds

#### Syntax

[Execution](execution.html).ChildExecutionIds

#### Data Type

[Long Array](data-types-for-teststand.html)

#### Purpose

Returns the child execution IDs for a given execution object.

#### See Also

[Engine.GetExecution](engine-getexecution.html)

[Execution.ParentExecutionId](execution-parentexecutionid.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-clearextraresultlist.html language=enus -->
## TOPIC 01022: Execution.ClearExtraResultList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-clearextraresultlist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-clearextraresultlist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ClearExtraResultList Purpose Clears the list of properties to add to the results list. See Also Execution.AddExtraResult Execution.DeleteExtraResult Execution.ResultObject

### Execution.ClearExtraResultList

#### Syntax

[Execution](execution.html).ClearExtraResultList

#### Purpose

Clears the list of properties to add to the results list.

#### See Also

[Execution.AddExtraResult](execution-addextraresult.html)

[Execution.DeleteExtraResult](execution-deleteextraresult.html)

[Execution.ResultObject](execution-resultobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-clearsequencedefaultvalues.html language=enus -->
## TOPIC 01023: Execution.ClearSequenceDefaultValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-clearsequencedefaultvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-clearsequencedefaultvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ClearSequenceDefaultValues( origSequence, defaultValueType) Purpose Removes a specific default value sequence or all default value sequences. Remarks This method operates on either the list of default value sequences for the execution or the hierarchy of executions associated with t

### Execution.ClearSequenceDefaultValues

#### Syntax

[Execution](execution.html).ClearSequenceDefaultValues( origSequence, defaultValueType)

#### Purpose

Removes a specific default value sequence or all default value sequences.

#### Remarks

This method operates on either the list of default value sequences for the execution or the hierarchy of executions associated with this execution.

#### Parameters

origSequence
 As
 [Sequence](sequence.html)

[In] Specifies the sequences that indicate the default value to remove. Passing
 NULL
 removes all default value sequences.

defaultValueType
 As
 [SequenceDefaultValueScopes](sequencedefaultvaluescopes.html)

[In] Specifies whether the method operates on the list of default value sequences for the execution or the hierarchy of executions associated with the execution.

#### See Also

[Sequence](sequence.html)

[SequenceDefaultValueScopes](sequencedefaultvaluescopes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-cleartemporarybreakpoints.html language=enus -->
## TOPIC 01024: Execution.ClearTemporaryBreakpoints

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-cleartemporarybreakpoints.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-cleartemporarybreakpoints.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ClearTemporaryBreakpoints Purpose Clears the temporary breakpoints on all threads. Remarks You can set temporary breakpoints by calling the Execution.StepInto , Execution.StepOut , or Execution.StepOver methods. See Also Execution.StepInto Execution.StepOut Execution.StepOver Thread

### Execution.ClearTemporaryBreakpoints

#### Syntax

[Execution](execution.html).ClearTemporaryBreakpoints

#### Purpose

Clears the temporary breakpoints on all threads.

#### Remarks

You can set temporary breakpoints by calling the
 [Execution.StepInto](execution-stepinto.html)
 ,
 [Execution.StepOut](execution-stepout.html)
 , or
 [Execution.StepOver](execution-stepover.html)
 methods.

#### See Also

[Execution.StepInto](execution-stepinto.html)

[Execution.StepOut](execution-stepout.html)

[Execution.StepOver](execution-stepover.html)

[Thread.ClearTemporaryBreakpoint](thread-cleartemporarybreakpoint.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-clientfile.html language=enus -->
## TOPIC 01025: Execution.ClientFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-clientfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-clientfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ClientFile Data Type SequenceFile Purpose Specifies the client sequence file when executing with a process model. Remarks Typically, you set this property in the process model to dynamically specify which client sequence file the process model invokes. When the execution first uses

### Execution.ClientFile

#### Syntax

[Execution](execution.html).ClientFile

#### Data Type

[SequenceFile](sequencefile.html)

#### Purpose

Specifies the client sequence file when executing with a process model.

#### Remarks

Typically, you set this property in the process model to dynamically specify which client sequence file the process model invokes.

When the execution first uses the client sequence file, it locks the file so that it cannot be unloaded from the sequence file cache of the engine until the execution completes or until this property is set to a different sequence file. Additionally, when you set this property to a different sequence file or a
 NULL
 reference to clear out the execution reference to the previous client sequence file, ensure you have disabled the
 Optimize Non-Reentrant Calls to This Sequence
 sequence property setting in all sequences of the client sequence file, or the execution maintains a reference to the client sequence file until it completes.

#### See Also

[SequenceContext.ProcessModelClient](sequencecontext-processmodelclient.html)

[SequenceFile](sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-deleteextraresult.html language=enus -->
## TOPIC 01026: Execution.DeleteExtraResult

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-deleteextraresult.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-deleteextraresult.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.DeleteExtraResult( propertyName) Purpose Removes a specific property from the list of properties to add to the results. Parameters propertyName As String [In] Specifies the property name of the property to remove from the list of properties to add to the results. Use the same name t

### Execution.DeleteExtraResult

#### Syntax

[Execution](execution.html).DeleteExtraResult( propertyName)

#### Purpose

Removes a specific property from the list of properties to add to the results.

#### Parameters

propertyName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the property name of the property to remove from the list of properties to add to the results. Use the same name that you passed as the first parameter to the
 [Execution.AddExtraResult](execution-addextraresult.html)
 method, such as
 Step.Limits.High
 .

#### See Also

[Execution.AddExtraResult](execution-addextraresult.html)

[Execution.ClearExtraResultList](execution-clearextraresultlist.html)

[Execution.ResultObject](execution-resultobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-disableresults.html language=enus -->
## TOPIC 01027: Execution.DisableResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-disableresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-disableresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.DisableResults Data Type Boolean Purpose Records results for steps running in the execution. Remarks When this property is True , TestStand does not record results for any steps that run in the execution. When this property is False , TestStand records results based on the setting o

### Execution.DisableResults

#### Syntax

[Execution](execution.html).DisableResults

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Records results for steps running in the execution.

#### Remarks

When this property is
 True
 , TestStand does not record results for any steps that run in the execution. When this property is
 False
 , TestStand records results based on the setting of the
 ResultRecordingOption
 property of each individual step or based on the
 DisableResults
 property of both the engine and the sequence.

#### See Also

[Execution.ResultObject](execution-resultobject.html)

[Sequence.DisableResults](sequence-disableresults.html)

[StationOptions.DisableResults](stationoptions-disableresults.html)

[Step.RecordLoopIterationResults](step-recordloopiterationresults.html)

[Step.ResultRecordingOption](step-resultrecordingoption.html)

[Step.ResultStatus](step-resultstatus.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-discardresults.html language=enus -->
## TOPIC 01028: Execution.DiscardResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-discardresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-discardresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.DiscardResults Data Type Boolean Purpose When you set this property to True , each step in the execution does not add its results to the corresponding Locals.ResultList array. Regardless of the value of this property, TestStand passes results to the PostResults and the PostResultLis

### Execution.DiscardResults

#### Syntax

[Execution](execution.html).DiscardResults

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

When you set this property to
 True
 , each step in the execution does not add its results to the corresponding
 Locals.ResultList
 array. Regardless of the value of this property, TestStand passes results to the PostResults and the PostResultListEntry Engine callbacks.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-displayname.html language=enus -->
## TOPIC 01029: Execution.DisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-displayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-displayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.DisplayName Data Type String Purpose Returns the name to display for the execution. See Also Thread.DisplayName

### Execution.DisplayName

#### Syntax

[Execution](execution.html).DisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name to display for the execution.

#### See Also

[Thread.DisplayName](thread-displayname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-enablecallback.html language=enus -->
## TOPIC 01030: Execution.EnableCallback

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-enablecallback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-enablecallback.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.EnableCallback( callbackType, newValue) Purpose Enables or disables the callback sequence that corresponds to the callback type passed as the input parameter. Remarks If the newValue parameter is set to False , TestStand disables the callback. Otherwise, TestStand enables the callba

### Execution.EnableCallback

#### Syntax

[Execution](execution.html).EnableCallback( callbackType, newValue)

#### Purpose

Enables or disables the callback sequence that corresponds to the callback type passed as the input parameter.

#### Remarks

If the
 newValue
 parameter is set to
 False
 , TestStand disables the callback. Otherwise, TestStand enables the callback. Use the
 [Execution.IsCallbackEnabled](execution-iscallbackenabled.html)
 method to determine whether a callback is enabled.

#### Parameters

callbackType
 As
 [CallbackTypes](callbacktypes.html)

[In] Specifies the
 [callback type](callbacktypes.html)
 .

newValue
 As
 [Boolean](data-types-for-teststand.html)

[In] If this value is
 False
 , TestStand disables the callback. Otherwise, TestStand enables the callback.

#### See Also

[CallbackTypes](callbacktypes.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-errorobject.html language=enus -->
## TOPIC 01031: Execution.ErrorObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-errorobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-errorobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ErrorObject Data Type PropertyObject Purpose Returns the error PropertyObject that contains the error reporting properties for this execution. Remarks The subproperties of the error object include Code , Msg , and Occurred . See Also Execution.DisableResults Execution.ResultObject P

### Execution.ErrorObject

#### Syntax

[Execution](execution.html).ErrorObject

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the error PropertyObject that contains the error reporting properties for this execution.

#### Remarks

The subproperties of the error object include
 Code
 ,
 Msg
 , and
 Occurred
 .

#### See Also

[Execution.DisableResults](execution-disableresults.html)

[Execution.ResultObject](execution-resultobject.html)

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-foregroundthread.html language=enus -->
## TOPIC 01032: Execution.ForegroundThread

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-foregroundthread.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-foregroundthread.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ForegroundThread Data Type Thread Purpose Specifies the foreground thread of the execution. Remarks The foreground thread is the thread that the sequence editor or user interface displays as active for the execution. See Also Execution.ForegroundThreadIndex Execution.NumThreads Thre

### Execution.ForegroundThread

#### Syntax

[Execution](execution.html).ForegroundThread

#### Data Type

[Thread](thread.html)

#### Purpose

Specifies the foreground thread of the execution.

#### Remarks

The foreground thread is the thread that the sequence editor or user interface displays as active for the execution.

#### See Also

[Execution.ForegroundThreadIndex](execution-foregroundthreadindex.html)

[Execution.NumThreads](execution-numthreads.html)

[Thread](thread.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-foregroundthreadindex.html language=enus -->
## TOPIC 01033: Execution.ForegroundThreadIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-foregroundthreadindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-foregroundthreadindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ForegroundThreadIndex Data Type Long Purpose Specifies the foreground thread of the execution. Remarks The foreground thread is the thread the sequence editor or user interface displays as active for the execution. You specify the thread with a zero-based index into the list of thre

### Execution.ForegroundThreadIndex

#### Syntax

[Execution](execution.html).ForegroundThreadIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the foreground thread of the execution.

#### Remarks

The foreground thread is the thread the sequence editor or user interface displays as active for the execution. You specify the thread with a zero-based index into the list of threads in the execution.

Do not access this property when handling a
 [UIMsg_Trace](uimessagecodes.html)
 message. TestStand allows non-foreground threads to run and complete while TestStand handles trace events. As a result, getting and setting thread indexes is unreliable during trace event handling. Use the
 [Execution.ForegroundThread](execution-foregroundthread.html)
 method instead.

#### See Also

[Execution.ForegroundThread](execution-foregroundthread.html)

[Execution.NumThreads](execution-numthreads.html)

[Thread](thread.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-getfileglobals.html language=enus -->
## TOPIC 01034: Execution.GetFileGlobals

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-getfileglobals.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-getfileglobals.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.GetFileGlobals( sequenceFileParam) Return Value PropertyObject Returns a PropertyObject that contains the file globals for the particular sequence file you pass as the sequenceFileParam parameter. It returns the run-time copy of the file globals. If a run-time copy has not yet been

### Execution.GetFileGlobals

#### Syntax

[Execution](execution.html).GetFileGlobals( sequenceFileParam)

#### Return Value

[PropertyObject](propertyobject.html)

Returns a PropertyObject that contains the file globals for the particular sequence file you pass as the
 sequenceFileParam
 parameter. It returns the run-time copy of the file globals. If a run-time copy has not yet been created, a new one is created and returned.

#### Purpose

Gets the run-time copy of the sequence file globals for a particular execution and sequence file.

#### Remarks

Sequence file globals are per execution and per sequence. All steps in a particular sequence file within a particular execution share the same copy of the sequence file globals at run time.

#### Parameters

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the sequence file that contains the file globals you want returned.

#### See Also

[PropertyObject](propertyobject.html)

[SequenceContext.FileGlobals](sequencecontext-fileglobals.html)

[SequenceFile](sequencefile.html)

[SequenceFile.FileGlobalsDefaultValues](sequencefile-fileglobalsdefaultvalues.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-getmodelsequencefile.html language=enus -->
## TOPIC 01035: Execution.GetModelSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-getmodelsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-getmodelsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.GetModelSequenceFile Return Value SequenceFile Purpose Returns the SequenceFile object for the process model file the execution is using. Remarks Returns a NULL object reference if the execution is not using a process model. Do not call the Engine.ReleaseSequenceFileEx method for a

### Execution.GetModelSequenceFile

#### Syntax

[Execution](execution.html).GetModelSequenceFile

#### Return Value

[SequenceFile](sequencefile.html)

#### Purpose

Returns the SequenceFile object for the process model file the execution is using.

#### Remarks

Returns a
 NULL
 object reference if the execution is not using a process model.

Note

Engine.ReleaseSequenceFileEx

#### See Also

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[Execution.ClientFile](execution-clientfile.html)

[Execution.GetSequenceFile](execution-getsequencefile.html)

[Execution.ModelSequenceFilePath](execution-modelsequencefilepath.html)

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-getsequencedefaultvalues.html language=enus -->
## TOPIC 01036: Execution.GetSequenceDefaultValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-getsequencedefaultvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-getsequencedefaultvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.GetSequenceDefaultValues( origSequence, defaultValueType) Return Value Sequence Returns a Sequence object that represents the default values an execution is using to create run-time copies of the sequence. Purpose Returns the default value copy of the sequence, if it exists. Otherwi

### Execution.GetSequenceDefaultValues

#### Syntax

[Execution](execution.html).GetSequenceDefaultValues( origSequence, defaultValueType)

#### Return Value

[Sequence](sequence.html)

Returns a Sequence object that represents the default values an execution is using to create run-time copies of the sequence.

#### Purpose

Returns the default value copy of the sequence, if it exists. Otherwise, this method returns
 NULL
 .

#### Remarks

Use this method to return default value sequences the
 [Execution.SetSequenceDefaultValues](execution-setsequencedefaultvalues.html)
 method previously specified.

If a sequence specifies to optimize non-reentrant calls, changes to the default value sequence this method returns do not apply to run-time sequences that the execution caches. Call the
 [Execution.SetSequenceDefaultValues](execution-setsequencedefaultvalues.html)
 method to ensure the execution uses any changes to the sequence in all subsequent invocations.

#### Parameters

origSequence
 As
 [Sequence](sequence.html)

[In] Specifies which default value sequence the method returns.

defaultValueType
 As
 [SequenceDefaultValueScopes](sequencedefaultvaluescopes.html)

[In] Specifies whether the method operates on the list of default value sequences for the execution or the hierarchy of executions with which the execution is associated.

#### See Also

[Execution.ClearSequenceDefaultValues](execution-clearsequencedefaultvalues.html)

[Execution.SetSequenceDefaultValues](execution-setsequencedefaultvalues.html)

[Sequence](sequence.html)

[Sequence.OptimizeNonReentrantCalls](sequence-optimizenonreentrantcalls.html)

[SequenceDefaultValueScopes](sequencedefaultvaluescopes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-getsequencefile.html language=enus -->
## TOPIC 01037: Execution.GetSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-getsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-getsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.GetSequenceFile Return Value SequenceFile Purpose Returns the SequenceFile object that contains the sequence in which the execution began. Remarks If the execution is using a process model, the method returns the SequenceFile object for the client sequence file. Do not call the Engi

### Execution.GetSequenceFile

#### Syntax

[Execution](execution.html).GetSequenceFile

#### Return Value

[SequenceFile](sequencefile.html)

#### Purpose

Returns the SequenceFile object that contains the sequence in which the execution began.

#### Remarks

If the execution is using a process model, the method returns the SequenceFile object for the client sequence file.

Note

Engine.ReleaseSequenceFileEx

#### See Also

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[Execution.ClientFile](execution-clientfile.html)

[Execution.GetModelSequenceFile](execution-getmodelsequencefile.html)

[Execution.ModelSequenceFilePath](execution-modelsequencefilepath.html)

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-getstates.html language=enus -->
## TOPIC 01038: Execution.GetStates

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-getstates.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-getstates.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.GetStates( runState, termState) Purpose Returns the current state of the execution. Remarks When a user interface that uses TestStand UI Controls needs to obtain the state of the execution, National Instruments recommends using the ApplicationMgr.GetRunState method or the ExecutionV

### Execution.GetStates

#### Syntax

[Execution](execution.html).GetStates( runState, termState)

#### Purpose

Returns the current state of the execution.

#### Remarks

Note

ApplicationMgr.GetRunState

ExecutionViewMgr.RunState

Execution.GetStates

#### Parameters

runState
 As
 [ExecutionRunStates](executionrunstates.html)

[Out] Returns the running state of the execution.

termState
 As
 [ExecutionTerminationStates](executionterminationstates.html)

[Out] If the execution is terminating, this value indicates how it is terminating.

#### See Also

[ApplicationMgr.GetRunState](../tsuiref/applicationmgr-getrunstate.html)

[Execution.CancelTermination](execution-canceltermination.html)

[Execution.GetTerminationMonitorStatus](execution-getterminationmonitorstatus.html)

[Execution.InitTerminationMonitor](execution-initterminationmonitor.html)

[ExecutionRunStates](executionrunstates.html)

[ExecutionTerminationStates](executionterminationstates.html)

[ExecutionViewMgr.RunState](../tsuiref/executionviewmgr-runstate.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-getterminationmonitorstatus.html language=enus -->
## TOPIC 01039: Execution.GetTerminationMonitorStatus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-getterminationmonitorstatus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-getterminationmonitorstatus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.GetTerminationMonitorStatus( terminationMonitorData, [sequenceContextParam]) Return Value Boolean Returns True if the execution is terminating or aborting. Purpose Monitors an execution so the calling code can abort what it is doing and exit if the user requests that the execution t

### Execution.GetTerminationMonitorStatus

#### Syntax

[Execution](execution.html).GetTerminationMonitorStatus( terminationMonitorData, [sequenceContextParam])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the execution is terminating or aborting.

#### Purpose

Monitors an execution so the calling code can abort what it is doing and exit if the user requests that the execution terminate or abort.

#### Remarks

Use this method with the
 [Execution.InitTerminationMonitor](execution-initterminationmonitor.html)
 method to monitor the state of the execution when performing a task inside of a step that takes a long time or requires user input to continue, such as launching a dialog box. When performing such a task, first call the
 Execution.InitTerminationMonitor
 method and hold on to the PropertyObject it returns. Then, while performing the task or inside of the message processing loop, periodically call this method and pass the PropertyObject you got from the
 Execution.InitTerminationMonitor
 method. If the method returns
 True
 , the execution is terminating and you should abort the task you are performing.

This method calls the
 [Execution.GetStates](execution-getstates.html)
 method to update the state information it stores in terminationMonitorData. The
 Execution.GetTerminationMonitorStatus
 method uses the state information to determine whether to exit an execution under various conditions, such as when a Cleanup step launches a dialog box while the sequence is already terminating.

Use the
 Execution.InitTerminationMonitor
 and
 Execution.GetTerminationMonitorStatus
 methods to monitor whether the execution receives a request to terminate or abort the execution. The monitor only recognizes requests to terminate or abort while monitoring, so a code module that executes in a Cleanup step group of an already terminating execution monitors for a subsequent request to terminate the step or abort the execution. Use the
 Execution.GetStates
 method to determine the execution state of the code module.

#### Parameters

terminationMonitorData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a property object you obtain by calling the
 [Execution.InitTerminationMonitor](execution-initterminationmonitor.html)
 method. The data this property object contains is not meant to be accessed directly.

sequenceContextParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you are monitoring an execution from a step that is running as part of the execution so you can abort the step when the execution terminates or aborts, pass the
 [SequenceContext](sequencecontext.html)
 object of the step. If you are monitoring an execution from a step in a different execution or from code that is not part of a step, leave this parameter unspecified. When you specify this parameter, TestStand uses other information about the execution of the step that is monitoring the execution to determine whether to abort.

#### See Also

[Execution.GetStates](execution-getstates.html)

[Execution.InitTerminationMonitor](execution-initterminationmonitor.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[PropertyObject](propertyobject.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-getthread.html language=enus -->
## TOPIC 01040: Execution.GetThread

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-getthread.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-getthread.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.GetThread( index) Return Value Thread Purpose Returns a Thread object for the thread that you identify by index. Remarks Do not call this method when handling a UIMsg_Trace message because TestStand allows non-foreground threads to run and complete while TestStand handles trace even

### Execution.GetThread

#### Syntax

[Execution](execution.html).GetThread( index)

#### Return Value

[Thread](thread.html)

#### Purpose

Returns a Thread object for the thread that you identify by index.

#### Remarks

Do not call this method when handling a
 [UIMsg_Trace](uimessagecodes.html)
 message because TestStand allows non-foreground threads to run and complete while TestStand handles trace events. As a result, obtaining a thread by index is unreliable during trace event handling.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the list of threads in the execution.

#### See Also

[Execution.ForegroundThread](execution-foregroundthread.html)

[Execution.ForegroundThreadIndex](execution-foregroundthreadindex.html)

[Execution.NumThreads](execution-numthreads.html)

[PropertyObject](propertyobject.html)

[Thread](thread.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-id.html language=enus -->
## TOPIC 01041: Execution.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.Id Data Type Long Purpose Returns a unique ID number for the execution. The ID number is never zero. Remarks The ID number is unique with respect to all executions you can initiate before you shut down the TestStand Engine. Use this ID number to compare two Execution object referenc

### Execution.Id

#### Syntax

[Execution](execution.html).Id

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique ID number for the execution.

Note

#### Remarks

The ID number is unique with respect to all executions you can initiate before you shut down the TestStand Engine.

Use this ID number to compare two Execution object references to determine whether they refer to the same underlying execution.

#### See Also

[Execution.DisplayName](execution-displayname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-ininteractivemode.html language=enus -->
## TOPIC 01042: Execution.InInteractiveMode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-ininteractivemode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-ininteractivemode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.InInteractiveMode Data Type Boolean Purpose Returns True if the execution is executing steps interactively. Remarks This property is always True for executions that you create as interactive executions. For executions that you start as normal executions, this property is only True w

### Execution.InInteractiveMode

#### Syntax

[Execution](execution.html).InInteractiveMode

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the execution is executing steps interactively.

#### Remarks

This property is always
 True
 for executions that you create as interactive executions. For executions that you start as normal executions, this property is only
 True
 when you interactively execute steps while at a breakpoint state. If you run the sequence using the Run Selected Steps Interactive Execution entry point, this property is
 True
 .

#### See Also

[Execution.TerminateInteractiveExecution](execution-terminateinteractiveexecution.html)

[InteractiveArgs](interactiveargs.html)

[SequenceContext.InteractiveContext](sequencecontext-interactivecontext.html)

[StationOptions.InteractiveBranchMode](stationoptions-interactivebranchmode.html)

[Thread.DoInteractiveExecution](thread-dointeractiveexecution.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-initterminationmonitor.html language=enus -->
## TOPIC 01043: Execution.InitTerminationMonitor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-initterminationmonitor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-initterminationmonitor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.InitTerminationMonitor Return Value PropertyObject A property object that contains data the Execution.GetTerminationMonitorStatus method uses to determine whether a particular execution is terminating and, therefore, whether a particular operation (that is, a code module of a step w

### Execution.InitTerminationMonitor

#### Syntax

[Execution](execution.html).InitTerminationMonitor

#### Return Value

[PropertyObject](propertyobject.html)

A property object that contains data the
 Execution.GetTerminationMonitorStatus
 method uses to determine whether a particular execution is terminating and, therefore, whether a particular operation (that is, a code module of a step within the execution) needs to abort what it is doing.

Note

#### Purpose

Creates the initial termination monitor data property object the
 [Execution.GetTerminationMonitorStatus](execution-getterminationmonitorstatus.html)
 method uses.

#### Remarks

Only call this method once, when you want to begin monitoring the status of the execution.

Use this method with the
 Execution.GetTerminationMonitorStatus
 method to monitor the state of an execution when performing a task inside of a step that takes a long time or requires user input to continue, such as launching a dialog box. When performing such a task, first call this method and hold on to the PropertyObject it returns. Then, while performing the task or inside of the message processing loop, periodically call the
 Execution.GetTerminationMonitorStatus
 method and pass the PropertyObject this method returns. If the method returns
 True
 , the execution is terminating and you should abort the task you are performing.

Use the
 Execution.InitTerminationMonitor
 and
 Execution.GetTerminationMonitorStatus
 methods to monitor whether the execution receives a request to terminate or abort the execution. The monitor only recognizes requests to terminate or abort while monitoring, so a code module that executes in a Cleanup step group of an already terminating execution monitors for a subsequent request to terminate the step or abort the execution. Use the
 Execution.GetStates
 method to determine the execution state of the code module.

#### See Also

[Execution.GetStates](execution-getstates.html)

[Execution.GetTerminationMonitorStatus](execution-getterminationmonitorstatus.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-iscallbackenabled.html language=enus -->
## TOPIC 01044: Execution.IsCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-iscallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-iscallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.IsCallbackEnabled( callbackType) Return Value Boolean Purpose Determines whether the callback type the parameter passes is enabled. Parameters callbackType As CallbackTypes [In] Specifies the callback type. Refer to CallbackTypes for the possible values. See Also CallbackTypes Execu

### Execution.IsCallbackEnabled

#### Syntax

[Execution](execution.html).IsCallbackEnabled( callbackType)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Determines whether the callback type the parameter passes is enabled.

#### Parameters

callbackType
 As
 [CallbackTypes](callbacktypes.html)

[In] Specifies the callback type. Refer to
 [CallbackTypes](callbacktypes.html)
 for the possible values.

#### See Also

[CallbackTypes](callbacktypes.html)

[Execution.EnableCallback](execution-enablecallback.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-iscontroller.html language=enus -->
## TOPIC 01045: Execution.IsController

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-iscontroller.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-iscontroller.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.IsController Data Type Boolean Purpose Indicates whether an execution is a process model controller. Remarks Process models set this property to True for their controlling execution. The controlling execution for the Batch and Parallel models creates an additional execution for each

### Execution.IsController

#### Syntax

[Execution](execution.html).IsController

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates whether an execution is a process model controller.

#### Remarks

Process models set this property to
 True
 for their controlling execution. The controlling execution for the Batch and Parallel models creates an additional execution for each test socket. The Sequential Model uses a single execution, which serves as both the controlling execution and the socket execution.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-maximumresultsperpostresultscallbac.html language=enus -->
## TOPIC 01046: Execution.MaximumResultsPerPostResultsCallback

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-maximumresultsperpostresultscallbac.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-maximumresultsperpostresultscallbac.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.MaximumResultsPerPostResultsCallback Data Type Long Purpose Specifies the maximum number of results a thread accumulates before calling its PostResults callbacks. See Also Execution.PostResultsCallback_PostFlushMask Execution.PostResultsCallback_PreFlushMask Execution.PostResultsCal

### Execution.MaximumResultsPerPostResultsCallback

#### Syntax

[Execution](execution.html).MaximumResultsPerPostResultsCallback

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the maximum number of results a thread accumulates before calling its PostResults callbacks.

#### See Also

[Execution.PostResultsCallback_PostFlushMask](execution-postresultscallback-postflushmask.html)

[Execution.PostResultsCallback_PreFlushMask](execution-postresultscallback-preflushmask.html)

[Execution.PostResultsCallbackMask](execution-postresultscallbackmask.html)

[Execution.PostResultsCallbackOptions](execution-postresultscallbackoptions.html)

[PostResultsCallbackMaskOptions](postresultscallbackmaskoptions.html)

[PostResultsCallbackOptions](postresultscallbackoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-modelposterrorcallbackenabled.html language=enus -->
## TOPIC 01047: Execution.ModelPostErrorCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-modelposterrorcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-modelposterrorcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ModelPostErrorCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the ProcessModelPostError ca

### Execution.ModelPostErrorCallbackEnabled

#### Syntax

[Execution](execution.html).ModelPostErrorCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the ProcessModelPostError callback. Set this property to
 False
 to disable the ProcessModelPostError callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-modelpostfailcallbackenabled.html language=enus -->
## TOPIC 01048: Execution.ModelPostFailCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-modelpostfailcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-modelpostfailcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ModelPostFailCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the ProcessModelPostFail call

### Execution.ModelPostFailCallbackEnabled

#### Syntax

[Execution](execution.html).ModelPostFailCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the ProcessModelPostFail callback. Set this property to
 False
 to disable the ProcessModelPostFail callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-modelpostinteractivecallbackenabled.html language=enus -->
## TOPIC 01049: Execution.ModelPostInteractiveCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-modelpostinteractivecallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-modelpostinteractivecallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ModelPostInteractiveCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the ProcessModelPostIn

### Execution.ModelPostInteractiveCallbackEnabled

#### Syntax

[Execution](execution.html).ModelPostInteractiveCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the ProcessModelPostInteractive callback. Set this property to
 False
 to disable the ProcessModelPostInteractive callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-modelpostresultcallbackenabled.html language=enus -->
## TOPIC 01050: Execution.ModelPostResultCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-modelpostresultcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-modelpostresultcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ModelPostResultCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the ProcessModelPostResult

### Execution.ModelPostResultCallbackEnabled

#### Syntax

[Execution](execution.html).ModelPostResultCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the ProcessModelPostResult callback. Set this property to
 False
 to disable the ProcessModelPostResult callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-modelpoststepcallbackenabled.html language=enus -->
## TOPIC 01051: Execution.ModelPostStepCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-modelpoststepcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-modelpoststepcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ModelPostStepCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the ProcessModelPostStep call

### Execution.ModelPostStepCallbackEnabled

#### Syntax

[Execution](execution.html).ModelPostStepCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the ProcessModelPostStep callback. Set this property to
 False
 to disable the ProcessModelPostStep callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-modelpreinteractivecallbackenabled.html language=enus -->
## TOPIC 01052: Execution.ModelPreInteractiveCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-modelpreinteractivecallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-modelpreinteractivecallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ModelPreInteractiveCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the ProcessModelPreInte

### Execution.ModelPreInteractiveCallbackEnabled

#### Syntax

[Execution](execution.html).ModelPreInteractiveCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the ProcessModelPreInteractive callback. Set this property to
 False
 to disable the ProcessModelPreInteractive callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-modelprestepcallbackenabled.html language=enus -->
## TOPIC 01053: Execution.ModelPreStepCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-modelprestepcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-modelprestepcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ModelPreStepCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the ProcessModelPreStep callba

### Execution.ModelPreStepCallbackEnabled

#### Syntax

[Execution](execution.html).ModelPreStepCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the ProcessModelPreStep callback. Set this property to
 False
 to disable the ProcessModelPreStep callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-modelsequencefilepath.html language=enus -->
## TOPIC 01054: Execution.ModelSequenceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-modelsequencefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-modelsequencefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ModelSequenceFilePath Data Type String Purpose Returns the absolute pathname of the model sequence file for this execution. See Also Execution.ClientFile Execution.SequenceFilePath SequenceContext.IsProcessModel SequenceFile.ModelPath StationOptions.StationModelSequenceFilePath

### Execution.ModelSequenceFilePath

#### Syntax

[Execution](execution.html).ModelSequenceFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute pathname of the model sequence file for this execution.

#### See Also

[Execution.ClientFile](execution-clientfile.html)

[Execution.SequenceFilePath](execution-sequencefilepath.html)

[SequenceContext.IsProcessModel](sequencecontext-isprocessmodel.html)

[SequenceFile.ModelPath](sequencefile-modelpath.html)

[StationOptions.StationModelSequenceFilePath](stationoptions-stationmodelsequencefilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-newsequencedefaultvalues.html language=enus -->
## TOPIC 01055: Execution.NewSequenceDefaultValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-newsequencedefaultvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-newsequencedefaultvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.NewSequenceDefaultValues( origSequence) Return Value Sequence Returns a Sequence object that represents default values an execution can use to create run-time copies of the sequence during execution. Typically, you update the local variables and step properties in the sequence this

### Execution.NewSequenceDefaultValues

#### Syntax

[Execution](execution.html).NewSequenceDefaultValues( origSequence)

#### Return Value

[Sequence](sequence.html)

Returns a Sequence object that represents default values an execution can use to create run-time copies of the sequence during execution. Typically, you update the local variables and step properties in the sequence this method returns, and use the
 [Execution.SetSequenceDefaultValues](execution-setsequencedefaultvalues.html)
 method to instruct the execution to use the sequence to create run-time sequences.

#### Purpose

Creates a default value copy of the sequence.

#### Remarks

Whenever TestStand begins executing a sequence, it makes a run-time copy of the sequence. Normally, TestStand creates the run-time copy from the edit-time copy of the sequence in the sequence file. You can use this method in conjunction with the
 [Execution.SetSequenceDefaultValues](execution-setsequencedefaultvalues.html)
 method to instruct the execution to use different default values for the local variables and step properties. Changes to the default value sequence this method returns do not update the edit-time copy of the sequence.

#### Parameters

origSequence
 As
 [Sequence](sequence.html)

[In] Specifies which default value sequence the method creates.

#### See Also

[Execution.ClearSequenceDefaultValues](execution-clearsequencedefaultvalues.html)

[Execution.GetSequenceDefaultValues](execution-getsequencedefaultvalues.html)

[Execution.SetSequenceDefaultValues](execution-setsequencedefaultvalues.html)

[Sequence](sequence.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-newthread.html language=enus -->
## TOPIC 01056: Execution.NewThread

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-newthread.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-newthread.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.NewThread( sequenceFileParam, sequenceNameParam, options, sequenceContextParam = NULL, sequenceArgsParam = NULL) Return Value Thread The thread created by this method. Purpose Creates and returns a new Thread object. Remarks When you call this method, the thread begins executing imm

### Execution.NewThread

#### Syntax

[Execution](execution.html).NewThread( sequenceFileParam, sequenceNameParam, options, sequenceContextParam = NULL, sequenceArgsParam = NULL)

#### Return Value

[Thread](thread.html)

The thread created by this method.

#### Purpose

Creates and returns a new
 [Thread](thread.html)
 object.

#### Remarks

When you call this method, the thread begins executing immediately. This method behaves similar to a Sequence Call step you configure to run in a new thread.

#### Parameters

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the SequenceFile object that contains the sequence to execute.

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the sequence to execute.

options
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for the default behavior or pass one or more
 [NewThreadOptions](newthreadoptions.html)
 constants. Use the bitwise-OR operator to pass multiple constants.

sequenceContextParam
 As
 [SequenceContext](sequencecontext.html)

[In] If you call this method from a code module for a step inside of an execution, pass the sequence context of the step. This allows this method to behave similar to a Sequence Call step and to set the
 [SequenceContext.Caller](sequencecontext-caller.html)
 property correctly.

This parameter has a default value of
 NULL
 .

sequenceArgsParam
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a PropertyObject object that contains the arguments to the sequence you want to execute. Each subproperty of PropertyObject represents a parameter to the sequence. The subproperties must appear in the same order as the sequence parameters.

This parameter has a default value of
 NULL
 .

#### See Also

[NewThreadOptions](newthreadoptions.html)

[PropertyObject](propertyobject.html)

[SequenceContext](sequencecontext.html)

[SequenceContext.Caller](sequencecontext-caller.html)

[SequenceFile](sequencefile.html)

[Thread](thread.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-numthreads.html language=enus -->
## TOPIC 01057: Execution.NumThreads

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-numthreads.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-numthreads.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.NumThreads Data Type Long Purpose Returns the current number of threads in the execution. Remarks Do not access this property when handling a UIMsg_Trace message. TestStand allows non-foreground threads to run and complete while TestStand handles trace events. As a result, obtaining

### Execution.NumThreads

#### Syntax

[Execution](execution.html).NumThreads

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the current number of threads in the execution.

#### Remarks

Do not access this property when handling a
 [UIMsg_Trace](uimessagecodes.html)
 message. TestStand allows non-foreground threads to run and complete while TestStand handles trace events. As a result, obtaining the number of threads is unreliable during trace event handling.

#### See Also

[Execution.ForegroundThread](execution-foregroundthread.html)

[Execution.ForegroundThreadIndex](execution-foregroundthreadindex.html)

[Execution.GetThread](execution-getthread.html)

[Thread](thread.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-outputrecordstreams.html language=enus -->
## TOPIC 01058: Execution.OutputRecordStreams

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-outputrecordstreams.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-outputrecordstreams.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.OutputRecordStreams Data Type ExecutionOutputRecordStreams Purpose Returns the collection of ExecutionOutputRecordStream objects associated with this Execution. See Also ExecutionOutputRecordStreams ExecutionOutputRecordStream

### Execution.OutputRecordStreams

#### Syntax

[Execution](execution.html).OutputRecordStreams

#### Data Type

[ExecutionOutputRecordStreams](executionoutputrecordstreams.html)

#### Purpose

Returns the collection of
 ExecutionOutputRecordStream
 objects associated with this Execution.

#### See Also

[ExecutionOutputRecordStreams](executionoutputrecordstreams.html)

[ExecutionOutputRecordStream](executionoutputrecordstream.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-overridenonterminatablethreads.html language=enus -->
## TOPIC 01059: Execution.OverrideNonTerminatableThreads

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-overridenonterminatablethreads.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-overridenonterminatablethreads.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.OverrideNonTerminatableThreads Data Type Boolean Purpose Overrides the value you set in the Thread.TerminationOption property. When an execution terminates, threads with a TerminationOption of ThreadTerminationOptions_Normal stop. If the Execution.OverrideNonTerminatableThreads prop

### Execution.OverrideNonTerminatableThreads

#### Syntax

[Execution](execution.html).OverrideNonTerminatableThreads

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Overrides the value you set in the
 [Thread.TerminationOption](thread-terminationoption.html)
 property. When an execution terminates, threads with a
 TerminationOption
 of
 [ThreadTerminationOptions_Normal](threadterminationoptions.html)
 stop. If the
 Execution.OverrideNonTerminatableThreads
 property is set, threads with a
 TerminationOption
 of
 [ThreadTerminationOptions_Prompt](threadterminationoptions.html)
 also stop without prompting. This option does not affect threads with a
 TerminationOption
 of
 [ThreadTerminationOptions_Never](threadterminationoptions.html)
 .

#### See Also

[Execution.TerminateNonTerminatableThreadsPrompt](execution-terminatenonterminatablethreadsprom.html)

[Thread.TerminationOption](thread-terminationoption.html)

[ThreadTerminationOptions](threadterminationoptions.html)

[UIMsg_NonTerminatableThreadsArePreventingTermination](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-parentexecutionid.html language=enus -->
## TOPIC 01060: Execution.ParentExecutionId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-parentexecutionid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-parentexecutionid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ParentExecutionId Data Type Long Purpose Specifies the parent execution ID. When setting the parent ID, this execution's ID is added to the parent's child ID list. See Also Engine.GetExecution Execution.ChildExecutionIds

### Execution.ParentExecutionId

#### Syntax

[Execution](execution.html).ParentExecutionId

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the parent execution ID. When setting the parent ID, this execution's ID is added to the parent's child ID list.

#### See Also

[Engine.GetExecution](engine-getexecution.html)

[Execution.ChildExecutionIds](execution-childexecutionids.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-postresultscallback-postflushmask.html language=enus -->
## TOPIC 01061: Execution.PostResultsCallback_PostFlushMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-postresultscallback-postflushmask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-postresultscallback-postflushmask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.PostResultsCallback_PostFlushMask Data Type Long Purpose TestStand calls PostResults callbacks with all accumulated results before exiting any sequence you specify using this property. Remarks You typically specify the pre-flush mask and post-flush mask when a Model Plugin – OnTheFl

### Execution.PostResultsCallback_PostFlushMask

#### Syntax

[Execution](execution.html).PostResultsCallback_PostFlushMask

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

TestStand calls PostResults callbacks with all accumulated results before exiting any sequence you specify using this property.

#### Remarks

You typically specify the
 [pre-flush mask and post-flush mask](postresultscallbackmaskoptions.html)
 when a Model Plugin – OnTheFly Step Results entry point requires that the
 Context
 parameter of the entry point refer to the same sequence stack frame that executes all the steps in the
 Steps
 parameter of the entry point. Otherwise, the
 Steps
 parameter of the entry point can contain steps from multiple stack frames. Using this technique results in fewer steps for each invocation of the OnTheFly Step Results entry point, which can affect performance.

#### See Also

[Execution.MaximumResultsPerPostResultsCallback](execution-maximumresultsperpostresultscallbac.html)

[Execution.PostResultsCallback_PreFlushMask](execution-postresultscallback-preflushmask.html)

[Execution.PostResultsCallbackInterval](execution-postresultscallbackinterval.html)

[Execution.PostResultsCallbackMask](execution-postresultscallbackmask.html)

[Execution.PostResultsCallbackOptions](execution-postresultscallbackoptions.html)

[PostResultsCallbackMaskOptions](postresultscallbackmaskoptions.html)

[PostResultsCallbackOptions](postresultscallbackoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-postresultscallback-preflushmask.html language=enus -->
## TOPIC 01062: Execution.PostResultsCallback_PreFlushMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-postresultscallback-preflushmask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-postresultscallback-preflushmask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.PostResultsCallback_PreFlushMask Data Type Long Purpose TestStand calls PostResults callbacks with all accumulated results before entering any sequence you specify using this property. Remarks You typically set the pre-flush mask and post-flush mask when a Model Plugin – OnTheFly St

### Execution.PostResultsCallback_PreFlushMask

#### Syntax

[Execution](execution.html).PostResultsCallback_PreFlushMask

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

TestStand calls PostResults callbacks with all accumulated results before entering any sequence you specify using this property.

#### Remarks

You typically set the
 [pre-flush mask and post-flush mask](postresultscallbackmaskoptions.html)
 when a Model Plugin – OnTheFly Step Results entry point requires that the
 Context
 parameter of the entry point refer to the same sequence stack frame that executes all the steps in the
 Steps
 parameter of the entry point. Otherwise, the
 Steps
 parameter of the entry point can contain steps from multiple stack frames. Using this technique results in fewer steps for each invocation of the OnTheFly Step Results entry point, which can affect performance.

#### See Also

[Execution.MaximumResultsPerPostResultsCallback](execution-maximumresultsperpostresultscallbac.html)

[Execution.PostResultsCallback_PostFlushMask](execution-postresultscallback-postflushmask.html)

[Execution.PostResultsCallbackInterval](execution-postresultscallbackinterval.html)

[Execution.PostResultsCallbackMask](execution-postresultscallbackmask.html)

[Execution.PostResultsCallbackOptions](execution-postresultscallbackoptions.html)

[PostResultsCallbackMaskOptions](postresultscallbackmaskoptions.html)

[PostResultsCallbackOptions](postresultscallbackoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-postresultscallbackinterval.html language=enus -->
## TOPIC 01063: Execution.PostResultsCallbackInterval

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-postresultscallbackinterval.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-postresultscallbackinterval.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.PostResultsCallbackInterval Data Type Double Purpose Specifies the interval at which threads in the execution call PostResults callbacks. Remarks If the time since a thread last called the PostResults callback equals or exceeds the value of this property, the thread calls the PostRe

### Execution.PostResultsCallbackInterval

#### Syntax

[Execution](execution.html).PostResultsCallbackInterval

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Specifies the interval at which threads in the execution call PostResults callbacks.

#### Remarks

If the time since a thread last called the PostResults callback equals or exceeds the value of this property, the thread calls the PostResults callback when TestStand next generates a result.

If the interval is a negative number, the absolute value determines the interval. In this case, threads call PostResults callbacks if the number of results accumulated exceeds the estimate of how many results TestStand can process within the interval based on the duration of previous PostResults callbacks. This mechanism provides more of a balance between result generation and result processing tasks if result generation is much faster than result processing.

#### See Also

[Execution.PostResultsCallback_PostFlushMask](execution-postresultscallback-postflushmask.html)

[Execution.PostResultsCallback_PreFlushMask](execution-postresultscallback-preflushmask.html)

[Execution.PostResultsCallbackMask](execution-postresultscallbackmask.html)

[Execution.PostResultsCallbackOptions](execution-postresultscallbackoptions.html)

[PostResultsCallbackMaskOptions](postresultscallbackmaskoptions.html)

[PostResultsCallbackOptions](postresultscallbackoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-postresultscallbackmask.html language=enus -->
## TOPIC 01064: Execution.PostResultsCallbackMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-postresultscallbackmask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-postresultscallbackmask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.PostResultsCallbackMask Data Type Long Purpose Specifies the mask of the sequences in which TestStand accumulates step results to transfer as a parameter to the PostResults callbacks sequence. Remarks You typically specify the callback mask if a custom process model plug-in processe

### Execution.PostResultsCallbackMask

#### Syntax

[Execution](execution.html).PostResultsCallbackMask

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the mask of the sequences in which TestStand accumulates step results to transfer as a parameter to the PostResults callbacks sequence.

#### Remarks

You typically specify the callback mask if a custom process model plug-in processes results on-the-fly.

#### See Also

[Execution.MaximumResultsPerPostResultsCallback](execution-maximumresultsperpostresultscallbac.html)

[Execution.PostResultsCallback_PostFlushMask](execution-postresultscallback-postflushmask.html)

[Execution.PostResultsCallback_PreFlushMask](execution-postresultscallback-preflushmask.html)

[Execution.PostResultsCallbackInterval](execution-postresultscallbackinterval.html)

[Execution.PostResultsCallbackOptions](execution-postresultscallbackoptions.html)

[PostResultsCallbackMaskOptions](postresultscallbackmaskoptions.html)

[PostResultsCallbackOptions](postresultscallbackoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-postresultscallbackoptions.html language=enus -->
## TOPIC 01065: Execution.PostResultsCallbackOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-postresultscallbackoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-postresultscallbackoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.PostResultsCallbackOptions Data Type Long Purpose Specifies the options for when TestStand calls PostResults callbacks. See Also Execution.MaximumResultsPerPostResultsCallback Execution.PostResultsCallback_PostFlushMask Execution.PostResultsCallback_PreFlushMask Execution.PostResult

### Execution.PostResultsCallbackOptions

#### Syntax

[Execution](execution.html).PostResultsCallbackOptions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the
 [options](postresultscallbackoptions.html)
 for when TestStand calls PostResults callbacks.

#### See Also

[Execution.MaximumResultsPerPostResultsCallback](execution-maximumresultsperpostresultscallbac.html)

[Execution.PostResultsCallback_PostFlushMask](execution-postresultscallback-postflushmask.html)

[Execution.PostResultsCallback_PreFlushMask](execution-postresultscallback-preflushmask.html)

[Execution.PostResultsCallbackInterval](execution-postresultscallbackinterval.html)

[Execution.PostResultsCallbackMask](execution-postresultscallbackmask.html)

[PostResultsCallbackMaskOptions](postresultscallbackmaskoptions.html)

[PostResultsCallbackOptions](postresultscallbackoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-removepoststepcustomuimessage.html language=enus -->
## TOPIC 01066: Execution.RemovePostStepCustomUIMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-removepoststepcustomuimessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-removepoststepcustomuimessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.RemovePostStepCustomUIMessage( MsgCode) Purpose Removes a custom user interface message associated with an execution. Remarks Use this method to remove any custom user interface messages previously associated with an execution by calling the Execution.AddPostStepCustomUIMessage meth

### Execution.RemovePostStepCustomUIMessage

#### Syntax

[Execution](execution.html).RemovePostStepCustomUIMessage( MsgCode)

#### Purpose

Removes a custom user interface message associated with an execution.

#### Remarks

Use this method to remove any custom user interface messages previously associated with an execution by calling the
 [Execution.AddPostStepCustomUIMessage](execution-addpoststepcustomuimessage.html)
 method.

#### Parameters

MsgCode
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the custom UI message code. This method does not return an error when the message code is not associated with an execution.

#### See Also

[Engine.RegisterUIMessage](engine-registeruimessage.html)

[Execution.AddPostStepCustomUIMessage](execution-addpoststepcustomuimessage.html)

[UIMessage](uimessage.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-report.html language=enus -->
## TOPIC 01067: Execution.Report

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-report.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-report.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.Report Data Type Report Purpose Returns the Report object for the execution. See Also Report SequenceContext.Report

### Execution.Report

#### Syntax

[Execution](execution.html).Report

#### Data Type

[Report](report.html)

#### Purpose

Returns the Report object for the execution.

#### See Also

[Report](report.html)

[SequenceContext.Report](sequencecontext-report.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-reports.html language=enus -->
## TOPIC 01068: Execution.Reports

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-reports.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.Reports Data Type Reports Purpose Returns the collection of reports for the execution.

### Execution.Reports

#### Syntax

[Execution](execution.html).Reports

#### Data Type

[Reports](reports.html)

#### Purpose

Returns the collection of reports for the execution.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-restart.html language=enus -->
## TOPIC 01069: Execution.Restart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-restart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-restart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.Restart( breakOnEntryParam) Purpose This method is obsolete. Use the Execution.RestartEx method instead. Remarks Execution restarts from the beginning. Parameters breakOnEntryParam As Boolean [In] Pass True to stop at the first step in the execution. See Also Execution.RestartEx

### Execution.Restart

#### Syntax

[Execution](execution.html).Restart( breakOnEntryParam)

#### Purpose

Note

Execution.RestartEx

#### Remarks

Execution restarts from the beginning.

#### Parameters

breakOnEntryParam
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to stop at the first step in the execution.

#### See Also

[Execution.RestartEx](execution-restartex.html)

Parent topic:

Obsolete Execution Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-restartex.html language=enus -->
## TOPIC 01070: Execution.RestartEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-restartex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-restartex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.RestartEx( restartOptionsParam) Purpose Restarts a completed execution. Remarks Use this method instead of the Execution.Restart method when you require the new functionality the RestartOptions constants provide. For example, use this method if you need to restart an execution creat

### Execution.RestartEx

#### Syntax

[Execution](execution.html).RestartEx( restartOptionsParam)

#### Purpose

Restarts a completed execution.

#### Remarks

Use this method instead of the
 Execution.Restart
 method when you require the new functionality the
 [RestartOptions](restartoptions.html)
 constants provide. For example, use this method if you need to restart an execution created as non-restartable.

#### Parameters

restartOptionsParam
 As
 [Long](data-types-for-teststand.html)

[In] Specifies which
 [RestartOptions](restartoptions.html)
 to use. You can specify more than one RestartOption by combining the constants using the bitwise-OR operator.

#### See Also

[Execution.RestartWithNewArguments](execution-restartwithnewarguments.html)

[RestartOptions](restartoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-restartwithnewarguments.html language=enus -->
## TOPIC 01071: Execution.RestartWithNewArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-restartwithnewarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-restartwithnewarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.RestartWithNewArguments( restartOptionsParam, sequenceArgsParam) Purpose Restarts a completed execution and passes the arguments you specify to the restarted execution. Remarks Use this method instead of the Execution.RestartEx method when you want to pass new arguments to an execut

### Execution.RestartWithNewArguments

#### Syntax

[Execution](execution.html).RestartWithNewArguments( restartOptionsParam, sequenceArgsParam)

#### Purpose

Restarts a completed execution and passes the arguments you specify to the restarted execution.

#### Remarks

Use this method instead of the
 [Execution.RestartEx](execution-restartex.html)
 method when you want to pass new arguments to an execution you restart. You most commonly use this method in combination with the
 [ExecTypeMask_DiscardArgumentsWhenDone](executiontypemask.html)
 option, but you can use this method with any execution. This method discards any arguments an execution already holds and replaces them with the arguments you specify.

#### Parameters

restartOptionsParam
 As
 [Long](data-types-for-teststand.html)

[In] Specifies which
 [RestartOptions](restartoptions.html)
 constant to use. You can specify more than one restart option by combining the constants using the bitwise-OR operator.

sequenceArgsParam
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a
 PropertyObject
 object that contains the arguments to the sequence you want to execute. Each subproperty of the
 PropertyObject
 object represents a parameter for the sequence. The subproperties must appear in the same order in which the sequence parameters appear. You can pass a
 NULL
 reference if you do not want to pass any arguments. Passing
 NULL
 discards any arguments an execution already holds. If you want to reuse the arguments an execution already holds, use the
 [Execution.RestartEx](execution-restartex.html)
 method instead of this method.

#### See Also

[Execution.RestartEx](execution-restartex.html)

[ExecutionTypeMask](executiontypemask.html)

[RestartOptions](restartoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-resultobject.html language=enus -->
## TOPIC 01072: Execution.ResultObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-resultobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-resultobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ResultObject Data Type PropertyObject Purpose Returns the Result PropertyObject for the execution. Remarks Typically, the Result PropertyObject contains at least the Error, Status, ReportText, and Common subproperties. Error —Property object that contains the error information for t

### Execution.ResultObject

#### Syntax

[Execution](execution.html).ResultObject

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the Result PropertyObject for the execution.

#### Remarks

Typically, the Result PropertyObject contains at least the Error, Status, ReportText, and Common subproperties.

- Error 
 —Property object that contains the error information for the execution.
- ResultList 
 —Array that contains the combined results for all the steps in the execution.
- SequenceFile 
 —String that contains the path of the sequence file associated with the execution.
- Sequence 
 —String that contains the name of the sequence associated with the execution.
- Status 
 —String that contains the status of the execution.

You can also obtain the Error subproperty of the Result PropertyObject by using the
 [ErrorObject](execution-errorobject.html)
 property. You can access the Status subproperty by using the
 [ResultStatus](execution-resultstatus.html)
 property.

#### See Also

[Execution.ErrorObject](execution-errorobject.html)

[Execution.ResultStatus](execution-resultstatus.html)

[PropertyObject](propertyobject.html)

[StepProperties](stepproperties.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-resultstatus.html language=enus -->
## TOPIC 01073: Execution.ResultStatus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-resultstatus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-resultstatus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ResultStatus Data Type String Purpose Specifies the result status string for the execution. Remarks You cannot use this property to determine if a completed execution encountered an error. Instead, access the Occurred sub-property of Execution.ErrorObject. Although you can define cu

### Execution.ResultStatus

#### Syntax

[Execution](execution.html).ResultStatus

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the result status string for the execution.

#### Remarks

Note

ResultStatus_

StepProperties

#### See Also

[Execution.ResultObject](execution-resultobject.html)

[StepProperties](stepproperties.html)

[Execution.ErrorObject](execution-errorobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-resume.html language=enus -->
## TOPIC 01074: Execution.Resume

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-resume.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-resume.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.Resume Purpose Resumes the execution from a suspended state. Remarks The execution state does not change immediately after the call to this method returns, but the state will change before the next step within the execution executes. See Also Engine.BreakAll Execution.Break

### Execution.Resume

#### Syntax

[Execution](execution.html).Resume

#### Purpose

Resumes the execution from a suspended state.

#### Remarks

The execution state does not change immediately after the call to this method returns, but the state will change before the next step within the execution executes.

#### See Also

[Engine.BreakAll](engine-breakall.html)

[Execution.Break](execution-break.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-rteoptionforthisexecution.html language=enus -->
## TOPIC 01075: Execution.RTEOptionForThisExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-rteoptionforthisexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-rteoptionforthisexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.RTEOptionForThisExecution Data Type RTEOptions Use the following constants with this data type: RTEOption_Abort –(Value: 3) Instructs the execution to abort the execution. RTEOption_Continue –(Value: 1) Instructs the execution to process the error by propagating the error to the cal

### Execution.RTEOptionForThisExecution

#### Syntax

[Execution](execution.html).RTEOptionForThisExecution

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

Specifies the current setting that indicates how TestStand responds to a run-time error.

#### Remarks

The original setting for this property is the value of the
 [StationOptions.RTEOption](stationoptions-rteoption.html)
 property when the execution is created.

#### See Also

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[StationOptions.RTEOption](stationoptions-rteoption.html)

[Thread.SetBatchRTEOption](thread-setbatchrteoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-runtimevariables.html language=enus -->
## TOPIC 01076: Execution.RunTimeVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-runtimevariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-runtimevariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.RunTimeVariables Data Type PropertyObject Purpose Use this property object to create and access variables you want to exist only for the current run of the execution. Remarks TestStand destroys these variables when the execution completes, terminates, or aborts. See Also Engine.Temp

### Execution.RunTimeVariables

#### Syntax

[Execution](execution.html).RunTimeVariables

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Use this property object to create and access variables you want to exist only for the current run of the execution.

#### Remarks

TestStand destroys these variables when the execution completes, terminates, or aborts.

#### See Also

[Engine.TemporaryGlobals](engine-temporaryglobals.html)

[PropertyObject](propertyobject.html)

[Thread.RunTimeVariables](thread-runtimevariables.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-secondsatstart.html language=enus -->
## TOPIC 01077: Execution.SecondsAtStart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-secondsatstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-secondsatstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SecondsAtStart Data Type Double Purpose Returns the number of seconds between the creation of the engine and the beginning of the execution. Remarks This property returns the value of the Engine.SecondsSinceStart property when the execution starts. Restarting the execution resets th

### Execution.SecondsAtStart

#### Syntax

[Execution](execution.html).SecondsAtStart

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the number of seconds between the creation of the engine and the beginning of the execution.

#### Remarks

This property returns the value of the
 [Engine.SecondsSinceStart](engine-secondssincestart.html)
 property when the execution starts. Restarting the execution resets the value of this property.

#### See Also

[Engine.SecondsSince1970UniversalCoordinatedTime](engine-secondssince1970universalcoordinatedti.html)

[Engine.SecondsSinceStart](engine-secondssincestart.html)

[Execution.SecondsExecuting](execution-secondsexecuting.html)

[Execution.SecondsSuspended](execution-secondssuspended.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-secondsexecuting.html language=enus -->
## TOPIC 01078: Execution.SecondsExecuting

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-secondsexecuting.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-secondsexecuting.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SecondsExecuting Data Type Double Purpose Returns the total number of seconds for which the execution has been running. Remarks The value returned does not include time spent while the execution is suspended at a breakpoint. Restarting the execution resets the value of this property

### Execution.SecondsExecuting

#### Syntax

[Execution](execution.html).SecondsExecuting

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the total number of seconds for which the execution has been running.

#### Remarks

The value returned does not include time spent while the execution is suspended at a breakpoint. Restarting the execution resets the value of this property.

#### See Also

[Engine.SecondsSince1970UniversalCoordinatedTime](engine-secondssince1970universalcoordinatedti.html)

[Engine.SecondsSinceStart](engine-secondssincestart.html)

[Execution.SecondsAtStart](execution-secondsatstart.html)

[Execution.SecondsSuspended](execution-secondssuspended.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-secondssuspended.html language=enus -->
## TOPIC 01079: Execution.SecondsSuspended

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-secondssuspended.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-secondssuspended.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SecondsSuspended Data Type Double Purpose Returns the total number of seconds for which the execution has been suspended at breakpoints. Remarks Restarting the execution resets the value of this property. See Also Engine.SecondsSince1970UniversalCoordinatedTime Engine.SecondsSinceSt

### Execution.SecondsSuspended

#### Syntax

[Execution](execution.html).SecondsSuspended

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the total number of seconds for which the execution has been suspended at breakpoints.

#### Remarks

Restarting the execution resets the value of this property.

#### See Also

[Engine.SecondsSince1970UniversalCoordinatedTime](engine-secondssince1970universalcoordinatedti.html)

[Engine.SecondsSinceStart](engine-secondssincestart.html)

[Execution.SecondsAtStart](execution-secondsatstart.html)

[Execution.SecondsExecuting](execution-secondsexecuting.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-seqfileposterrorcallbackenabled.html language=enus -->
## TOPIC 01080: Execution.SeqFilePostErrorCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-seqfileposterrorcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-seqfileposterrorcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SeqFilePostErrorCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the SequenceFilePostError callback.

### Execution.SeqFilePostErrorCallbackEnabled

#### Syntax

[Execution](execution.html).SeqFilePostErrorCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the SequenceFilePostError callback. Set this property to
 False
 to disable the SequenceFilePostError callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-seqfilepostfailcallbackenabled.html language=enus -->
## TOPIC 01081: Execution.SeqFilePostFailCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-seqfilepostfailcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-seqfilepostfailcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SeqFilePostFailCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the SequenceFilePostFail callback. S

### Execution.SeqFilePostFailCallbackEnabled

#### Syntax

[Execution](execution.html).SeqFilePostFailCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the SequenceFilePostFail callback. Set this property to
 False
 to disable the SequenceFilePostFail callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-seqfilepostinteractivecallbackenabl.html language=enus -->
## TOPIC 01082: Execution.SeqFilePostInteractiveCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-seqfilepostinteractivecallbackenabl.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-seqfilepostinteractivecallbackenabl.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SeqFilePostInteractiveCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the SequenceFilePost

### Execution.SeqFilePostInteractiveCallbackEnabled

#### Syntax

[Execution](execution.html).SeqFilePostInteractiveCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the SequenceFilePostInteractive callback. Set this property to
 False
 to disable the SequenceFilePostInteractive callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-seqfilepostresultcallbackenabled.html language=enus -->
## TOPIC 01083: Execution.SeqFilePostResultCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-seqfilepostresultcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-seqfilepostresultcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SeqFilePostResultCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the SequenceFilePostResul

### Execution.SeqFilePostResultCallbackEnabled

#### Syntax

[Execution](execution.html).SeqFilePostResultCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the SequenceFilePostResult callback. Set this property to
 False
 to disable the SequenceFilePostResult callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-seqfilepoststepcallbackenabled.html language=enus -->
## TOPIC 01084: Execution.SeqFilePostStepCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-seqfilepoststepcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-seqfilepoststepcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SeqFilePostStepCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the SequenceFilePostStep ca

### Execution.SeqFilePostStepCallbackEnabled

#### Syntax

[Execution](execution.html).SeqFilePostStepCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the SequenceFilePostStep callback. Set this property to
 False
 to disable the SequenceFilePostStep callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-seqfilepreinteractivecallbackenable.html language=enus -->
## TOPIC 01085: Execution.SeqFilePreInteractiveCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-seqfilepreinteractivecallbackenable.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-seqfilepreinteractivecallbackenable.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SeqFilePreInteractiveCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the SequenceFilePreIn

### Execution.SeqFilePreInteractiveCallbackEnabled

#### Syntax

[Execution](execution.html).SeqFilePreInteractiveCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the SequenceFilePreInteractive callback. Set this property to
 False
 to disable the SequenceFilePreInteractive callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-seqfileprestepcallbackenabled.html language=enus -->
## TOPIC 01086: Execution.SeqFilePreStepCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-seqfileprestepcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-seqfileprestepcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SeqFilePreStepCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the SequenceFilePreStep call

### Execution.SeqFilePreStepCallbackEnabled

#### Syntax

[Execution](execution.html).SeqFilePreStepCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the SequenceFilePreStep callback. Set this property to
 False
 to disable the SequenceFilePreStep callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-sequencefilepath.html language=enus -->
## TOPIC 01087: Execution.SequenceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-sequencefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-sequencefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SequenceFilePath Data Type String Returns the sequence file pathname. Returns an empty string for unsaved sequence files. Purpose Returns the absolute pathname of the sequence file for this execution. Remarks If the execution is using a process model, the method returns the pathname

### Execution.SequenceFilePath

#### Syntax

[Execution](execution.html).SequenceFilePath

#### Data Type

[String](data-types-for-teststand.html)

Returns the sequence file pathname. Returns an empty string for unsaved sequence files.

#### Purpose

Returns the absolute pathname of the sequence file for this execution.

#### Remarks

If the execution is using a process model, the method returns the pathname of the client sequence file.

#### See Also

[Execution.ClientFile](execution-clientfile.html)

[Execution.GetSequenceFile](execution-getsequencefile.html)

[Execution.ModelSequenceFilePath](execution-modelsequencefilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-setsequencedefaultvalues.html language=enus -->
## TOPIC 01088: Execution.SetSequenceDefaultValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-setsequencedefaultvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-setsequencedefaultvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.SetSequenceDefaultValues( defValSequence, defaultValueType) Purpose Instructs the execution to use a default value copy of the sequence to create run-time copies of the sequence. Remarks Whenever TestStand begins executing a sequence, it makes a run-time copy of the sequence. Normal

### Execution.SetSequenceDefaultValues

#### Syntax

[Execution](execution.html).SetSequenceDefaultValues( defValSequence, defaultValueType)

#### Purpose

Instructs the execution to use a default value copy of the sequence to create run-time copies of the sequence.

#### Remarks

Whenever TestStand begins executing a sequence, it makes a run-time copy of the sequence. Normally, TestStand creates the run-time copy from the edit-time copy of the sequence in the sequence file. You can use this method in conjunction with the
 [Execution.NewSequenceDefaultValues](execution-newsequencedefaultvalues.html)
 method to instruct the execution to use different default values for the local variables and step properties.

You can associate default value sequences with either a specific execution or the hierarchy of executions with which the execution is associated. For example, setting a default value sequence on the hierarchy of execution associated with a Batch model applies the default value sequence to the controlling batch execution and all test socket executions. If an execution and the execution hierarchy both specify a default value sequence, TestStand uses the default value sequence the execution specifies.

#### Parameters

defValSequence
 As
 [Sequence](sequence.html)

[In] Specifies the default value sequence the execution uses to create run-time sequences. Use the
 [Execution.NewSequenceDefaultValues](execution-newsequencedefaultvalues.html)
 method to create a default value sequence and update the local variables and step properties in the sequence before calling this method.

defaultValueType
 As
 [SequenceDefaultValueScopes](sequencedefaultvaluescopes.html)

[In] Specifies whether the method operates on the list of default value sequences for the execution or the hierarchy of executions associated with the execution.

#### See Also

[Execution.ClearSequenceDefaultValues](execution-clearsequencedefaultvalues.html)

[Execution.GetSequenceDefaultValues](execution-getsequencedefaultvalues.html)

[Execution.NewSequenceDefaultValues](execution-newsequencedefaultvalues.html)

[Sequence](sequence.html)

[SequenceDefaultValueScopes](sequencedefaultvaluescopes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-standardresultsenabled.html language=enus -->
## TOPIC 01089: Execution.StandardResultsEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-standardresultsenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-standardresultsenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StandardResultsEnabled Data Type Boolean Purpose Stores all the standard results for steps in the execution. Standard results include properties that specify basic step execution information. Remarks Set this property to False to disable storing the standard results for the executio

### Execution.StandardResultsEnabled

#### Syntax

[Execution](execution.html).StandardResultsEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Stores all the standard results for steps in the execution. Standard results include properties that specify basic step execution information.

#### Remarks

Set this property to
 False
 to disable storing the standard results for the execution.

The
 [standard results](/csh?context=ts_tsfundamentals_standard_result_props)
 are the subproperties in the
 TS
 property of the result list entry for each step.

#### See Also

[Execution.DisableResults](execution-disableresults.html)

[Execution.TimeResultsEnabled](execution-timeresultsenabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-startcount.html language=enus -->
## TOPIC 01090: Execution.StartCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-startcount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-startcount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StartCount Data Type Long Purpose Returns the number of times the execution has been started. Remarks This count increments after TestStand sends the UIMsg_StartExecution message to the user interface. Calling this property while handling the UIMsg_StartExecution message returns 0 t

### Execution.StartCount

#### Syntax

[Execution](execution.html).StartCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of times the execution has been started.

#### Remarks

This count increments after TestStand sends the
 [UIMsg_StartExecution](uimessagecodes.html)
 message to the user interface. Calling this property while handling the
 UIMsg_StartExecution
 message returns
 0
 the first time the execution starts.

#### See Also

[Execution.RestartEx](execution-restartex.html)

[UIMessageCodes](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stationposterrorcallbackenabled.html language=enus -->
## TOPIC 01091: Execution.StationPostErrorCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stationposterrorcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stationposterrorcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StationPostErrorCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the StationPostError callb

### Execution.StationPostErrorCallbackEnabled

#### Syntax

[Execution](execution.html).StationPostErrorCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the StationPostError callback. Set this property to
 False
 to disable the StationPostError callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stationpostfailcallbackenabled.html language=enus -->
## TOPIC 01092: Execution.StationPostFailCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stationpostfailcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stationpostfailcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StationPostFailCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the StationPostFail callbac

### Execution.StationPostFailCallbackEnabled

#### Syntax

[Execution](execution.html).StationPostFailCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the StationPostFail callback. Set this property to
 False
 to disable the StationPostFail callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stationpostinteractivecallbackenabl.html language=enus -->
## TOPIC 01093: Execution.StationPostInteractiveCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stationpostinteractivecallbackenabl.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stationpostinteractivecallbackenabl.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StationPostInteractiveCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the StationPostInter

### Execution.StationPostInteractiveCallbackEnabled

#### Syntax

[Execution](execution.html).StationPostInteractiveCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the StationPostInteractive callback. Set this property to
 False
 to disable the StationPostInteractive callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stationpostresultcallbackenabled.html language=enus -->
## TOPIC 01094: Execution.StationPostResultCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stationpostresultcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stationpostresultcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StationPostResultCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the StationPostResult cal

### Execution.StationPostResultCallbackEnabled

#### Syntax

[Execution](execution.html).StationPostResultCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the StationPostResult callback. Set this property to
 False
 to disable the StationPostResult callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stationpoststepcallbackenabled.html language=enus -->
## TOPIC 01095: Execution.StationPostStepCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stationpoststepcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stationpoststepcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StationPostStepCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the StationPostStep callbac

### Execution.StationPostStepCallbackEnabled

#### Syntax

[Execution](execution.html).StationPostStepCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the StationPostStep callback. Set this property to
 False
 to disable the StationPostStep callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stationpreinteractivecallbackenable.html language=enus -->
## TOPIC 01096: Execution.StationPreInteractiveCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stationpreinteractivecallbackenable.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stationpreinteractivecallbackenable.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StationPreInteractiveCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the StationPreInterac

### Execution.StationPreInteractiveCallbackEnabled

#### Syntax

[Execution](execution.html).StationPreInteractiveCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the StationPreInteractive callback. Set this property to
 False
 to disable the StationPreInteractive callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stationprestepcallbackenabled.html language=enus -->
## TOPIC 01097: Execution.StationPreStepCallbackEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stationprestepcallbackenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stationprestepcallbackenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StationPreStepCallbackEnabled Data Type Boolean Purpose This property is obsolete. Use the Execution.EnableCallback method to enable the callback sequence. Use the Execution.IsCallbackEnabled method to verify that the callback is enabled. Remarks Enables the StationPreStep callback.

### Execution.StationPreStepCallbackEnabled

#### Syntax

[Execution](execution.html).StationPreStepCallbackEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Execution.EnableCallback

Execution.IsCallbackEnabled

#### Remarks

Enables the StationPreStep callback. Set this property to
 False
 to disable the StationPreStep callback.

#### See Also

[Execution.EnableCallback](execution-enablecallback.html)

[Execution.IsCallbackEnabled](execution-iscallbackenabled.html)

Parent topic:

Obsolete Execution Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stepinto.html language=enus -->
## TOPIC 01098: Execution.StepInto

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stepinto.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stepinto.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StepInto Purpose Resumes the execution from a suspended state and then suspends the execution again at the earliest possible point. Remarks If the step module adapter for the next step can step into the step module in debug mode, execution suspends at the beginning of the step modul

### Execution.StepInto

#### Syntax

[Execution](execution.html).StepInto

#### Purpose

Resumes the execution from a suspended state and then suspends the execution again at the earliest possible point.

#### Remarks

If the step module adapter for the next step can step into the step module in debug mode, execution suspends at the beginning of the step module code. If the step is a Sequence Call step, this method suspends execution at the first step in the subsequence.

#### See Also

[Execution.Break](execution-break.html)

[Execution.StepOut](execution-stepout.html)

[Execution.StepOver](execution-stepover.html)

[Thread.SetStepInto](thread-setstepinto.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stepout.html language=enus -->
## TOPIC 01099: Execution.StepOut

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stepout.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stepout.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StepOut Purpose Resumes the execution from a suspended state and then suspends the execution again after execution of the current sequence completes. See Also Execution.Break Execution.StepInto Execution.StepOver Thread.SetStepOut

### Execution.StepOut

#### Syntax

[Execution](execution.html).StepOut

#### Purpose

Resumes the execution from a suspended state and then suspends the execution again after execution of the current sequence completes.

#### See Also

[Execution.Break](execution-break.html)

[Execution.StepInto](execution-stepinto.html)

[Execution.StepOver](execution-stepover.html)

[Thread.SetStepOut](thread-setstepout.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-stepover.html language=enus -->
## TOPIC 01100: Execution.StepOver

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-stepover.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-stepover.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.StepOver Purpose Resumes the execution from a suspended state and then suspends the execution again after execution of the next step completes. See Also Execution.Break Execution.StepInto Execution.StepOver Thread.SetStepOver

### Execution.StepOver

#### Syntax

[Execution](execution.html).StepOver

#### Purpose

Resumes the execution from a suspended state and then suspends the execution again after execution of the next step completes.

#### See Also

[Execution.Break](execution-break.html)

[Execution.StepInto](execution-stepinto.html)

[Execution.StepOver](execution-stepover.html)

[Thread.SetStepOver](thread-setstepover.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-terminate.html language=enus -->
## TOPIC 01101: Execution.Terminate

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-terminate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-terminate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.Terminate Purpose Terminates the execution. Remarks Cleanup step groups execute as part of the termination process. If the execution is an interactive execution, use the Execution.TerminateInteractiveExecution method instead. If a call to a step module is active, the execution waits

### Execution.Terminate

#### Syntax

[Execution](execution.html).Terminate

#### Purpose

Terminates the execution.

#### Remarks

Cleanup step groups execute as part of the termination process. If the execution is an interactive execution, use the
 [Execution.TerminateInteractiveExecution](execution-terminateinteractiveexecution.html)
 method instead.

If a call to a step module is active, the execution waits for the step module to return.

The execution state does not change immediately after the call to this method returns, but the state will change before the next step within the execution executes.

#### See Also

[Engine.AbortAll](engine-abortall.html)

[Engine.TerminateAll](engine-terminateall.html)

[Execution.Abort](execution-abort.html)

[Execution.TerminateInteractiveExecution](execution-terminateinteractiveexecution.html)

[StationOptions.GetTimeLimitAction](stationoptions-gettimelimitaction.html)

[StationOptions.SetTimeLimitAction](stationoptions-settimelimitaction.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-terminateinteractiveexecution.html language=enus -->
## TOPIC 01102: Execution.TerminateInteractiveExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-terminateinteractiveexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-terminateinteractiveexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.TerminateInteractiveExecution Purpose Terminates an interactive execution. Remarks If you started the interactive execution while suspended in a normal execution, execution suspends at the point in the original execution at which you started the interactive execution. The Cleanup st

### Execution.TerminateInteractiveExecution

#### Syntax

[Execution](execution.html).TerminateInteractiveExecution

#### Purpose

Terminates an interactive execution.

#### Remarks

If you started the interactive execution while suspended in a normal execution, execution suspends at the point in the original execution at which you started the interactive execution.

The Cleanup step group for the sequence in which you started the interactive execution only runs if you created the execution as an interactive execution and if the user enables the Run Setup and Cleanup option on the
 [Execution tab](../tsref/execution-tab-station-options-dialog-box.html)
 of the
 [Station Options](../tsref/station-options-dialog-box.html)
 dialog box.

If a call to a step module is active, the execution waits for the step module to return.

The execution state does not change immediately after the call to this method returns, but the state will change before the next step within the execution executes.

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[Execution tab](../tsref/execution-tab-station-options-dialog-box.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[Execution.Terminate](execution-terminate.html)

[Thread.DoInteractiveExecution](thread-dointeractiveexecution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-terminatenonterminatablethreadsprom.html language=enus -->
## TOPIC 01103: Execution.TerminateNonTerminatableThreadsPrompt

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-terminatenonterminatablethreadsprom.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-terminatenonterminatablethreadsprom.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.TerminateNonTerminatableThreadsPrompt Data Type String Purpose Specifies the prompt message for a user interface to display in response to the UIMsg_NonTerminatableThreadsArePreventingTermination event. For example, a process model that spawns threads with a Thread.TerminationOption

### Execution.TerminateNonTerminatableThreadsPrompt

#### Syntax

[Execution](execution.html).TerminateNonTerminatableThreadsPrompt

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the prompt message for a user interface to display in response to the
 [UIMsg_NonTerminatableThreadsArePreventingTermination](uimessagecodes.html)
 event. For example, a process model that spawns threads with a
 [Thread.TerminationOption](thread-terminationoption.html)
 property set to
 [ThreadTerminationOptions_Prompt](threadterminationoptions.html)
 might set this property to inform users of the specific work they might lose if they terminate the threads. A user interface can display a different prompt message, but this behavior typically is not necessary.

#### See Also

[Execution.OverrideNonTerminatableThreads](execution-overridenonterminatablethreads.html)

[Thread.TerminationOption](thread-terminationoption.html)

[ThreadTerminationOptions](threadterminationoptions.html)

[UIMessageCodes](uimessagecodes.html)

[UIMsg_NonTerminatableThreadsArePreventingTermination](uimessagecodes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-threadids.html language=enus -->
## TOPIC 01104: Execution.ThreadIds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-threadids.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-threadids.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.ThreadIds Data Type Long Array Purpose Returns an array that contains the thread ID of each thread in the execution.

### Execution.ThreadIds

#### Syntax

[Execution](execution.html).ThreadIds

#### Data Type

[Long Array](data-types-for-teststand.html)

#### Purpose

Returns an array that contains the thread ID of each thread in the execution.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-timeresultsenabled.html language=enus -->
## TOPIC 01105: Execution.TimeResultsEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-timeresultsenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-timeresultsenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.TimeResultsEnabled Data Type Boolean Purpose Stores timing results for steps in the execution. Remarks Set this property to False to disable the storing of timing results for steps. TestStand stores time results only when the Execution.StandardResultsEnabled property is True . See A

### Execution.TimeResultsEnabled

#### Syntax

[Execution](execution.html).TimeResultsEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Stores timing results for steps in the execution.

#### Remarks

Set this property to
 False
 to disable the storing of timing results for steps. TestStand stores time results only when the
 [Execution.StandardResultsEnabled](execution-standardresultsenabled.html)
 property is
 True
 .

#### See Also

[Execution.StandardResultsEnabled](execution-standardresultsenabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-tracingdisabled.html language=enus -->
## TOPIC 01106: Execution.TracingDisabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-tracingdisabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-tracingdisabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.TracingDisabled Data Type Boolean Purpose Disables tracing on a per-execution basis. Remarks If tracing is globally disabled, enabling this property does nothing. This property is meant to disable tracing only when it would otherwise be enabled based on the StationOptions.TracingEna

### Execution.TracingDisabled

#### Syntax

[Execution](execution.html).TracingDisabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Disables tracing on a per-execution basis.

#### Remarks

If tracing is globally disabled, enabling this property does nothing. This property is meant to disable tracing only when it would otherwise be enabled based on the
 [StationOptions.TracingEnabled](stationoptions-tracingenabled.html)
 property, since this property overrides the enable setting on the station.

#### See Also

[SequenceContext.CanTrace](sequencecontext-cantrace.html)

[StationOptions.TracingEnabled](stationoptions-tracingenabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-typemask.html language=enus -->
## TOPIC 01107: Execution.TypeMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-typemask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-typemask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.TypeMask Data Type Long Purpose Specifies the ExecutionTypeMask constants with which you created the execution. See Also Engine.NewExecution ExecutionTypeMask

### Execution.TypeMask

#### Syntax

[Execution](execution.html).TypeMask

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the
 [ExecutionTypeMask](executiontypemask.html)
 constants with which you created the execution.

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[ExecutionTypeMask](executiontypemask.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-waitforend.html language=enus -->
## TOPIC 01108: Execution.WaitForEnd

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-waitforend.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-waitforend.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.WaitForEnd( millisecondTimeOut, processWindowsMsgs = True, [callingExecution]) Return Value Boolean Returns True when the execution ends or False when the timeout occurs. Purpose This method is obsolete. Use the Execution.WaitForEndEx method instead. Remarks Waits for an execution t

### Execution.WaitForEnd

#### Syntax

[Execution](execution.html).WaitForEnd( millisecondTimeOut, processWindowsMsgs = True, [callingExecution])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when the execution ends or
 False
 when the timeout occurs.

#### Purpose

Note

Execution.WaitForEndEx

#### Remarks

Waits for an execution to end. This method is not meant to be used by a user interface or sequence editor as it does not process UIMessages. Instead, use this method from a step to synchronize with another execution.

#### Parameters

millisecondTimeOut
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the maximum number of milliseconds to wait. Specify -1 for no timeout.

processWindowsMsgs
 As
 [Boolean](data-types-for-teststand.html)

[In] Specify
 True
 to process Microsoft Windows messages while waiting or
 False
 to wait without processing Windows messages.

This parameter has a default value of
 True
 .

callingExecution
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you call this method from a step, pass a reference to the execution of the step to allow this method to return immediately when the step execution is terminated or aborted.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Thread.WaitForEnd](thread-waitforend.html)

[Execution.WaitForEndEx](execution-waitforendex.html)

Parent topic:

Obsolete Execution Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution-waitforendex.html language=enus -->
## TOPIC 01109: Execution.WaitForEndEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution-waitforendex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution-waitforendex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Execution.WaitForEndEx( millisecondTimeOut, processWindowsMsgs = True, [stepToStoreResultsIn], [callingSequenceContext]) Return Value Boolean Returns True when the execution ends or False when the timeout occurs. Purpose Waits for an execution to end. Remarks This method is not meant to be us

### Execution.WaitForEndEx

#### Syntax

[Execution](execution.html).WaitForEndEx( millisecondTimeOut, processWindowsMsgs = True, [stepToStoreResultsIn], [callingSequenceContext])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when the execution ends or
 False
 when the timeout occurs.

#### Purpose

Waits for an execution to end.

#### Remarks

This method is not meant to be used by a user interface or sequence editor, as it does not process UIMessages. Instead, use this method from a step to synchronize with another execution. If you need to call this method from a user interface, you must call this method from a non-UI thread.

#### Parameters

millisecondTimeOut
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the maximum number of milliseconds to wait. Specify
 -1
 for no timeout.

If you pass a value for the callingSequenceContext parameter, TestStand suspends the timeout while the calling execution is suspended at a breakpoint so that the time spent at a breakpoint does not count towards the elapsed timeout time.

processWindowsMsgs
 As
 [Boolean](data-types-for-teststand.html)

[In] Specify
 True
 to process Microsoft Windows messages while waiting or
 False
 to wait without processing Windows messages.

This parameter has a default value of
 True
 .

stepToStoreResultsIn
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a step in which to store the results of the execution. If you specify a step, the result status of the step reflects that of the execution, and TestStand stores the result list for the execution in the
 TS.AsyncSequenceCall
 result property for the step.

callingSequenceContext
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If you are calling this method from inside of an execution, pass the current sequence context of the execution you are calling the method from for this parameter so TestStand can monitor the execution and abort the method if the calling execution is terminated or aborted.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/execution.html language=enus -->
## TOPIC 01110: Execution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/execution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/execution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An execution is an object TestStand creates to contain all the information it uses to run the sequences and subsequences it calls. Use objects of this class to control and get information about executions. For example, you can use methods to suspend, resume, or terminate execution, and you can use p

### Execution

An
 [execution](/csh?context=ts_tsfundamentals_executions)
 is an object TestStand creates to contain all the information it uses to run the sequences and subsequences it calls. Use objects of this class to control and get information about executions. For example, you can use methods to suspend, resume, or terminate execution, and you can use properties to determine whether the execution is an interactive execution or whether the execution is in the process of terminating.

#### Properties

| BreakOnEntry (Read Only) |
| --- |
| ClientFile |
| DisableResults |
| DiscardResults |
| DisplayName (Read Only) |
| ErrorObject (Read Only) |
| ForegroundThread |
| ForegroundThreadIndex |
| Id (Read Only) |
| InInteractiveMode (Read Only) |
| IsController |
| MaximumResultsPerPostResultsCallback |
| ModelSequenceFilePath (Read Only) |
| NumThreads (Read Only) |
| OutputRecordStreams (Read Only) |
| OverrideNonTerminatableThreads |
| PostResultsCallback_PostFlushMask |
| PostResultsCallback_PreFlushMask |
| PostResultsCallbackInterval |
| PostResultsCallbackMask |
| PostResultsCallbackOptions |
| Report (Read Only) |
| Reports (Read Only) |
| ResultObject (Read Only) |
| ResultStatus |
| RTEOptionForThisExecution |
| RunTimeVariables (Read Only) |
| SecondsAtStart (Read Only) |
| SecondsExecuting (Read Only) |
| SecondsSuspended (Read Only) |
| SequenceFilePath (Read Only) |
| StandardResultsEnabled |
| StartCount (Read Only) |
| TerminateNonTerminatableThreadsPrompt |
| ThreadIds (Read Only) |
| TimeResultsEnabled |
| TracingDisabled |
| TypeMask |

#### Methods

| Abort |
| --- |
| AddExtraResult |
| AddPostStepCustomUIMessage |
| AsPropertyObject |
| Break |
| CancelTermination |
| ClearExtraResultList |
| ClearSequenceDefaultValues |
| ClearTemporaryBreakpoints |
| DeleteExtraResult |
| EnableCallback |
| GetFileGlobals |
| GetModelSequenceFile |
| GetSequenceDefaultValues |
| GetSequenceFile |
| GetStates |
| GetTerminationMonitorStatus |
| GetThread |
| InitTerminationMonitor |
| IsCallbackEnabled |
| NewSequenceDefaultValues |
| NewThread |
| RemovePostStepCustomUIMessage |
| RestartEx |
| RestartWithNewArguments |
| Resume |
| SetSequenceDefaultValues |
| StepInto |
| StepOut |
| StepOver |
| Terminate |
| TerminateInteractiveExecution |
| WaitForEndEx |

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

[SequenceContext.Execution](sequencecontext-execution.html)

[Thread.Execution](thread-execution.html)

[UIMessage.Execution](uimessage-execution.html)

[WatchExpression.ExecutionScope](watchexpression-executionscope.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionmask.html language=enus -->
## TOPIC 01111: ExecutionMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionmask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionmask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the StationOptions.ExecutionMask property. Each constant corresponds to an Execution option. The user typically sets these options on the Execution tab of the Station Options dialog box. ExecMask_AllowBreakWhileInCodeModules –(Value: 0x8000) Enables TestStand to displa

### ExecutionMask

Use these constants to specify the
 [StationOptions.ExecutionMask](stationoptions-executionmask.html)
 property.

Each constant corresponds to an Execution option. The user typically sets these options on the
 [Execution tab](../tsref/execution-tab-station-options-dialog-box.html)
 of the
 [Station Options](../tsref/station-options-dialog-box.html)
 dialog box.

- ExecMask_AllowBreakWhileInCodeModules 
 –(Value: 0x8000) Enables TestStand to display an execution as suspended so you can debug it even if one or more threads are executing code inside a code module, which can be useful when code modules take a long time to complete, are blocked waiting for something, or are running continuously in the background. While the execution is suspended, steps with running code modules show a status of
 Running 
 . If the code module completes while the execution is suspended, the thread suspends immediately after returning from the code module until you resume the execution.
- ExecMask_BreakOnRunTimeError 
 –(Value: 0x4) Specifies that the message,
 UIMsg_BreakOnRunTimeError 
 , is sent when an error occurs and the value of the
 StationOptions.RTEOption 
 property is
 RTEOption_ShowDialog 
 .
- ExecMask_BreakpointsEnabled 
 –(Value: 0x1) Honors breakpoints.
- ExecMask_BreakWhileTerminating 
 –(Value: 0x2) Honors breakpoints when terminating an execution.
- ExecMask_DefaultExecutionMask 
 –(Value: 0x801D) Bitwise-OR combination of the
 ExecMask_BreakpointsEnabled 
 ,
 ExecMask_BreakOnRunTimeError 
 ,
 ExecMask_TraceIntoSetupCleanup 
 , and
 ExecMask_TracingEnabled 
 flags.
- ExecMask_InteractiveEvaluatePreconditions 
 –(Value: 0x4000) Specifies whether to evaluate preconditions for steps you run interactively.
- ExecMask_InteractiveRecordResults 
 –(Value: 0x1000) Records the results of steps you run interactively.
- ExecMask_InteractiveRunSetupCleanup 
 –(Value: 0x2000) Specifies whether to run the Setup and Cleanup step groups for the sequence that contains the selected steps. This option applies only when you initiate the interactive execution as an independent, top-level execution.
- ExecMask_TraceAllThreads 
 –(Value: 0x800) Generates trace events for all running threads in an execution. If you do not set this option, TestStand generates trace events only for the active thread.
 Note 
 The TestStand User Interface (UI) Controls display only the active thread and do not support enabling this constant.
- ExecMask_TraceIntoEntryPoints 
 –(Value: 0x100) Generates trace events for steps in Process Model entry point sequences.
- ExecMask_TraceIntoPostActionCallbacks 
 –(Value: 0x40) Generates trace events for steps in Post Action callbacks.
- ExecMask_TraceIntoPrePostCallbacks 
 –(Value: 0x20) Generates trace events for steps in any of the Pre-Step and Post-Step Engine callbacks.
- ExecMask_TraceIntoSeparateExecutionCallbacks 
 –(Value: 0x80) Specifies to generate trace events for steps in callbacks that run as executions separate from the top-level sequence execution. Examples include Front-End callbacks and callbacks you execute from the Tools menu.
- ExecMask_TraceIntoSequenceCallsMarkedAsTraceOff 
 –(Value: 0x200) Enables tracing into all subsequences when tracing is enabled for the calling sequence.
- ExecMask_TraceIntoSetupCleanup 
 –(Value: 0x10) Enables tracing of steps in the Setup and Cleanup step groups of each sequence.
- ExecMask_TraceWhileTerminating 
 –(Value: 0x400) Generates trace events for steps that run while execution is terminating. Examples of steps that can run when an execution is terminating are steps in the Cleanup step groups that run when you terminate execution in the middle of a sequence.
- ExecMask_TracingEnabled 
 –(Value: 0x8) Enables tracing. When tracing is enabled, the sequence editor or user interface displays each step as it executes. This option is useful for debugging but adds significant performance overhead to the execution of test programs.

#### See Also

[Execution tab](../tsref/execution-tab-station-options-dialog-box.html)

[StationOptions.ExecutionMask](stationoptions-executionmask.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[StationOptions.RTEOption](stationoptions-rteoption.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-clearrecordsfromr.html language=enus -->
## TOPIC 01112: ExecutionOutputRecordStream.ClearRecordsFromReportView

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-clearrecordsfromr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-clearrecordsfromr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.ClearRecordsFromReportView Purpose Clear records for this ExecutionOutputRecordStream from the Report View. See Also ExecutionOutputRecordStream.NumRecordsToDisplayInReportView

### ExecutionOutputRecordStream.ClearRecordsFromReportView

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).ClearRecordsFromReportView

#### Purpose

Clear records for this
 ExecutionOutputRecordStream
 from the Report View.

#### See Also

[ExecutionOutputRecordStream.NumRecordsToDisplayInReportView](executionoutputrecordstream-numrecordstodispl.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-close.html language=enus -->
## TOPIC 01113: ExecutionOutputRecordStream.Close

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-close.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-close.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.Close Purpose Close the OutputRecordStream objects contained in this ExecutionOutputRecordStream . Remarks ExecutionOutputRecordStream.Close invokes OutputRecordStream.Close on all of the OutputRecordStream objects contained by this ExecutionOutputRecordStream . Se

### ExecutionOutputRecordStream.Close

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).Close

#### Purpose

Close the
 OutputRecordStream
 objects contained in this
 ExecutionOutputRecordStream
 .

#### Remarks

ExecutionOutputRecordStream.Close
 invokes
 OutputRecordStream.Close
 on all of the
 OutputRecordStream
 objects contained by this
 ExecutionOutputRecordStream
 .

#### See Also

[OutputRecordStream](outputrecordstream.html)

[ExecutionOutputRecordStream.Close](executionoutputrecordstream-close.html)

[ExecutionOutputRecordStream](executionoutputrecordstream.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-closeatnextuutorb.html language=enus -->
## TOPIC 01114: ExecutionOutputRecordStream.CloseAtNextUUTOrBatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-closeatnextuutorb.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-closeatnextuutorb.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.CloseAtNextUUTOrBatch Data Type Boolean True if the process model should close this ExecutionOutputRecordStream and remove it from the execution before beginning the next UUT (for test sockets) or batch (for the controller socket in the batch model). False if the p

### ExecutionOutputRecordStream.CloseAtNextUUTOrBatch

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).CloseAtNextUUTOrBatch

#### Data Type

[Boolean](data-types-for-teststand.html)

True
 if the process model should close this
 ExecutionOutputRecordStream
 and remove it from the execution before beginning the next UUT (for test sockets) or batch (for the controller socket in the batch model).
 False
 if the process model should not clean up this
 ExecutionOutputRecordStream
 .

#### Purpose

Indicate to the process model if it should clean up this
 ExecutionOutputRecordStream
 before starting the next UUT or batch.

#### Remarks

CloseAtNextUUTOrBatch
 indicates whether
 ExecutionOutputRecordStreams.BeginNextUUTOrBatch
 should close and remove this
 ExecutionOutputRecordStream
 .

Note

ExecutionOutputRecordStream

ExecutionOutputRecordStreams.BeginNextUUTOrBatch

ExecutionOutputRecordStreams

#### See Also

[ExecutionOutputRecordStream](executionoutputrecordstream.html)

[ExecutionOutputRecordStreams.BeginNextUUTOrBatch](executionoutputrecordstreams-beginnextuutorba.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-definefields.html language=enus -->
## TOPIC 01115: ExecutionOutputRecordStream.DefineFields

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-definefields.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-definefields.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.DefineFields( fieldDefinitions, mapping = "") Purpose Define the field names for records displayed in the Report View. Remarks Defining the fields names for the ExecutionOutputRecordStream does not define them for the contained OutputRecordStream objects. It only s

### ExecutionOutputRecordStream.DefineFields

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).DefineFields( fieldDefinitions, mapping = "")

#### Purpose

Define the field names for records displayed in the Report View.

#### Remarks

Defining the fields names for the
 ExecutionOutputRecordStream
 does not define them for the contained
 OutputRecordStream
 objects. It only specifies names for display in the Report View. Field names are not a part of the base
 OutputRecordStream
 interface, and may or may not be applicable for a specific
 OutputRecordStream
 implementation. To define the field names for a
 CsvFileOutputRecordStream
 , call
 CsvFileOutputRecordStream.WriteFieldHeaders()
 .

#### Parameters

fieldDefinitions
 As
 [PropertyObject](propertyobject.html)

[In] A container or array defining the field names. If the fields parameter is a container, the container is the record, and each subproperty is a field. The names of the subproperties are the field names. If the record parameter is an array, the entire array is the record, and each array element is a field. The values of the array elements coerced to strings are the field names.

mapping
 As
 [String](data-types-for-teststand.html)

[In] Specifies the mapping from elements (either subproperties or array elements) in the fields parameter to fields in the stream.

The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that elements 0, 3, 4, 5, 8, and 7 specify the field names. The final range in the list may be open-ended. For example, "2, 3-" indicates that elements 2, 3, and all elements beyond 3 specify the field names. For convenience, you may specify an empty string to specify all elements be used in order. That is, an empty string is equivalent to "0-". The default value is an empty string.

This parameter has a default value of
 ""
 .

#### See Also

[CsvFileOutputRecordStream.WriteFieldHeaders](csvfileoutputrecordstream-writefieldheaders.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-flush.html language=enus -->
## TOPIC 01116: ExecutionOutputRecordStream.Flush

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-flush.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-flush.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.Flush Purpose Flush the OutputRecordStream objects contained in this ExecutionOutputRecordStream . Remarks ExecutionOutputRecordStream.Flush invokes OutputRecordStream.Flush on all of its contained OutputRecordStream objects. See Also OutputRecordStream.Flush

### ExecutionOutputRecordStream.Flush

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).Flush

#### Purpose

Flush the
 OutputRecordStream
 objects contained in this
 ExecutionOutputRecordStream
 .

#### Remarks

ExecutionOutputRecordStream.Flush
 invokes
 OutputRecordStream.Flush
 on all of its contained
 OutputRecordStream
 objects.

#### See Also

[OutputRecordStream.Flush](outputrecordstream-flush2.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-format.html language=enus -->
## TOPIC 01117: ExecutionOutputRecordStream.Format

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-format.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-format.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.Format Data Type String Purpose Sets or retrieves the display format in the Report View. Remarks Allowed values are: "txt" –(default) Plain ASCII text format "html" –HTML format that displays CSV data as a table. See Also Report Pane Report Tab ExecutionOutputRecor

### ExecutionOutputRecordStream.Format

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).Format

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Sets or retrieves the display format in the Report View.

#### Remarks

Allowed values are:

- "txt" 
 –(default) Plain ASCII text format
- "html" 
 –HTML format that displays CSV data as a table.

#### See Also

[Report Pane](../tsref/report-pane-execution-window.html)

[Report Tab](../tsref/report-tab.html)

[ExecutionOutputRecordStream.NumRecordsToDisplayInReportView](executionoutputrecordstream-numrecordstodispl.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-insert.html language=enus -->
## TOPIC 01118: ExecutionOutputRecordStream.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.Insert( stream) Purpose Add an OutputRecordStream to this ExecutionOutputRecordStream . Parameters stream As OutputRecordStream [In] A non-null reference to an OutputRecordStream to add to this ExecutionOutputRecordStream . See Also OutputRecordStream ExecutionOutp

### ExecutionOutputRecordStream.Insert

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).Insert( stream)

#### Purpose

Add an
 OutputRecordStream
 to this
 ExecutionOutputRecordStream
 .

#### Parameters

stream
 As
 [OutputRecordStream](outputrecordstream.html)

[In] A non-null reference to an
 OutputRecordStream
 to add to this
 ExecutionOutputRecordStream
 .

#### See Also

[OutputRecordStream](outputrecordstream.html)

[ExecutionOutputRecordStream](executionoutputrecordstream.html)

[ExecutionOutputRecordStream.Remove](executionoutputrecordstream-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-name.html language=enus -->
## TOPIC 01119: ExecutionOutputRecordStream.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.Name Data Type String The name of this ExecutionOutputRecordStream . Purpose Get the name of this ExecutionOutputRecordStream . Remarks You can specify an ExecutionOutputRecordStream by name in the Write Record step type . You can also retrieve an ExecutionOutputRe

### ExecutionOutputRecordStream.Name

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).Name

#### Data Type

[String](data-types-for-teststand.html)

The name of this
 ExecutionOutputRecordStream
 .

#### Purpose

Get the name of this
 ExecutionOutputRecordStream
 .

#### Remarks

You can specify an
 ExecutionOutputRecordStream
 by name in the
 [Write Record step type](../tsref/write-record-step.html)
 . You can also retrieve an
 ExecutionOutputRecordStream
 from the current execution by name by calling
 ExecutionOutputRecordStreams.GetStream()
 .

#### See Also

[ExecutionOutputRecordStreams.GetStream](executionoutputrecordstreams-getstream.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-numrecordstodispl.html language=enus -->
## TOPIC 01120: ExecutionOutputRecordStream.NumRecordsToDisplayInReportView

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-numrecordstodispl.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-numrecordstodispl.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.NumRecordsToDisplayInReportView Data Type Long The number of records to display in the Report View. Purpose Get or set the number of records to display in the Report View. Remarks A value greater than 0 specifies the upper limit to the number of records to display

### ExecutionOutputRecordStream.NumRecordsToDisplayInReportView

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).NumRecordsToDisplayInReportView

#### Data Type

[Long](data-types-for-teststand.html)

The number of records to display in the Report View.

#### Purpose

Get or set the number of records to display in the Report View.

#### Remarks

A value greater than
 0
 specifies the upper limit to the number of records to display in the Report View. Once this limit is reached, each new record written to the Report View causes the oldest record to be removed. Specify a value greater than
 0
 to display recently written records while bounding the memory used by the Report View.

A value of
 0
 disables updates to the Report View. Specify
 0
 for maximum performance when you do not need to view records in the Report View.

A value of
 -1
 specifies no limit to the number of records displayed in the Report View. Specify
 -1
 when you are not concerned about memory use and wish to review all records written to the Report View.

Note

-1

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-remove.html language=enus -->
## TOPIC 01121: ExecutionOutputRecordStream.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.Remove( stream) Purpose Remove an OutputRecordStream from this ExecutionOutputRecordStream . Remarks The OutputRecordStream is not automatically closed when it is removed. To close the OutputRecordStream , call OutputRecordStream.Close() on the stream itself. Param

### ExecutionOutputRecordStream.Remove

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).Remove( stream)

#### Purpose

Remove an
 OutputRecordStream
 from this
 ExecutionOutputRecordStream
 .

#### Remarks

The
 OutputRecordStream
 is not automatically closed when it is removed. To close the
 OutputRecordStream
 , call
 OutputRecordStream.Close()
 on the stream itself.

#### Parameters

stream
 As
 [OutputRecordStream](outputrecordstream.html)

[In] A non-null reference to an
 OutputRecordStream
 to remove from this
 ExecutionOutputRecordStream
 .

#### See Also

[ExecutionOutputRecordStream.Insert](executionoutputrecordstream-insert.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-removeallstreams.html language=enus -->
## TOPIC 01122: ExecutionOutputRecordStream.RemoveAllStreams

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-removeallstreams.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-removeallstreams.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.RemoveAllStreams Purpose Remove all OutputRecordStream objects from this ExecutionOutputRecordStream . Remarks Streams are not automatically closed when they are removed. To close the streams, call ExecutionOutputRecordStream.Close before removing them. See Also Ex

### ExecutionOutputRecordStream.RemoveAllStreams

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).RemoveAllStreams

#### Purpose

Remove all
 OutputRecordStream
 objects from this
 ExecutionOutputRecordStream
 .

#### Remarks

Streams are not automatically closed when they are removed. To close the streams, call
 ExecutionOutputRecordStream.Close
 before removing them.

#### See Also

[ExecutionOutputRecordStream.Insert](executionoutputrecordstream-insert.html)

[ExecutionOutputRecordStream.Remove](executionoutputrecordstream-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-setactivereport.html language=enus -->
## TOPIC 01123: ExecutionOutputRecordStream.SetActiveReport

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-setactivereport.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-setactivereport.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.SetActiveReport Purpose Make this ExecutionOutputRecordStream the active (displayed) report in the Report View. Remarks SetActiveReport can conflict with the settings for the active report in TestStand process models. National Instruments recommends against calling

### ExecutionOutputRecordStream.SetActiveReport

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).SetActiveReport

#### Purpose

Make this
 ExecutionOutputRecordStream
 the active (displayed) report in the Report View.

#### Remarks

SetActiveReport
 can conflict with the settings for the active report in TestStand process models. National Instruments recommends against calling
 SetActiveReport
 from process model callbacks.

#### See Also

[ExecutionOutputRecordStream.NumRecordsToDisplayInReportView](executionoutputrecordstream-numrecordstodispl.html)

[ExecutionOutputRecordStream.ClearRecordsFromReportView](executionoutputrecordstream-clearrecordsfromr.html)

[Reports.ActiveReport](reports-activereport.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-writerecord.html language=enus -->
## TOPIC 01124: ExecutionOutputRecordStream.WriteRecord

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-writerecord.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-writerecord.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.WriteRecord( record, mapping = "") Purpose Write a record to the ExecutionOutputRecordStream . Remarks ExecutionOutputRecordStream.WriteRecord invokes OutputRecordStream.WriteRecord on each OutputRecordStream it contains, using the specified parameters. In addition

### ExecutionOutputRecordStream.WriteRecord

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).WriteRecord( record, mapping = "")

#### Purpose

Write a record to the
 ExecutionOutputRecordStream
 .

#### Remarks

ExecutionOutputRecordStream.WriteRecord
 invokes
 OutputRecordStream.WriteRecord
 on each
 OutputRecordStream
 it contains, using the specified parameters. In addition, it updates the Report View with data from the new record.

#### Parameters

record
 As
 [PropertyObject](propertyobject.html)

[In] The record to write. The record parameter may be either a container or an array. If the record parameter is a container, the container represents the record, and each subproperty is a field. If the record parameter is an array, the entire array represents the record, and each array element is a field.

mapping
 As
 [String](data-types-for-teststand.html)

[In] Specifies the mapping from elements (either subproperties or array elements) in the record parameter to fields in the stream. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that elements 0, 3, 4, 5, 8, and 7 be written as the fields to the stream. The final range in the list may be open-ended. For example, "2, 3-" indicates that elements 2, 3, and all elements beyond 3 be written to the stream. If the record parameter is a container, the range list may include individual subproperty names. For example, "Temperature, Pressure, 0-1" specifies that the subproperties "Temperature" and "Pressure" as well as elements 0 and 1 be written as fields to the stream. For convenience, you may specify an empty string to specify all elements be written in order. That is, an empty string is equivalent to "0-". The default value is an empty string.

This parameter has a default value of
 ""
 .

#### See Also

[ExecutionOutputRecordStream.WriteRecordFrom](executionoutputrecordstream-writerecordfrom.html)

[OutputRecordStream.WriteRecord](outputrecordstream-writerecord.html)

[ExecutionOutputRecordStream.NumRecordsToDisplayInReportView](executionoutputrecordstream-numrecordstodispl.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream-writerecordfrom.html language=enus -->
## TOPIC 01125: ExecutionOutputRecordStream.WriteRecordFrom

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream-writerecordfrom.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream-writerecordfrom.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStream.WriteRecordFrom( context, record) Purpose Write a record to the ExecutionOutputRecordStream . Remarks ExecutionOutputRecordStream.WriteRecordFrom() invokes OutputRecordStream.WriteRecordFrom() on each OutputRecordStream it contains, using the specified parameters.

### ExecutionOutputRecordStream.WriteRecordFrom

#### Syntax

[ExecutionOutputRecordStream](executionoutputrecordstream.html).WriteRecordFrom( context, record)

#### Purpose

Write a record to the
 ExecutionOutputRecordStream
 .

#### Remarks

ExecutionOutputRecordStream.WriteRecordFrom()
 invokes
 OutputRecordStream.WriteRecordFrom()
 on each
 OutputRecordStream
 it contains, using the specified parameters. In addition, it updates the Report View with data from the new record.

#### Parameters

context
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 against which to evaluate the lookup strings specified by the record parameter.

record
 As
 [Object Array](data-types-for-teststand.html)

[In] An array of lookup strings specifying the fields to write to the stream. The lookup strings are evaluated relative to the
 SequenceContext
 specified by the context parameter.

#### See Also

[ExecutionOutputRecordStream.WriteRecord](executionoutputrecordstream-writerecord.html)

[OutputRecordStream.WriteRecordFrom](outputrecordstream-writerecordfrom.html)

[ExecutionOutputRecordStream.NumRecordsToDisplayInReportView](executionoutputrecordstream-numrecordstodispl.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstream.html language=enus -->
## TOPIC 01126: ExecutionOutputRecordStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Properties CloseAtNextUUTOrBatch Format Name (Read Only) NumRecordsToDisplayInReportView Methods ClearRecordsFromReportView Close DefineFields Flush Insert Remove RemoveAllStreams SetActiveReport WriteRecord WriteRecordFrom

### ExecutionOutputRecordStream

#### Properties

| CloseAtNextUUTOrBatch |
| --- |
| Format |
| Name (Read Only) |
| NumRecordsToDisplayInReportView |

#### Methods

| ClearRecordsFromReportView |
| --- |
| Close |
| DefineFields |
| Flush |
| Insert |
| Remove |
| RemoveAllStreams |
| SetActiveReport |
| WriteRecord |
| WriteRecordFrom |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstreams-beginnextuutorba.html language=enus -->
## TOPIC 01127: ExecutionOutputRecordStreams.BeginNextUUTOrBatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstreams-beginnextuutorba.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstreams-beginnextuutorba.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStreams.BeginNextUUTOrBatch Purpose Clean up this ExecutionOutputRecordStreams object before beginning the next UUT or batch. Remarks BeginNextUUTOrBatch iterates over all ExecutionOutputRecordStream objects contained in this collection. Any streams with the ExecutionOutp

### ExecutionOutputRecordStreams.BeginNextUUTOrBatch

#### Syntax

[ExecutionOutputRecordStreams](executionoutputrecordstreams.html).BeginNextUUTOrBatch

#### Purpose

Clean up this
 ExecutionOutputRecordStreams
 object before beginning the next UUT or batch.

#### Remarks

BeginNextUUTOrBatch
 iterates over all
 ExecutionOutputRecordStream
 objects contained in this collection. Any streams with the
 ExecutionOutputRecordStream.CloseAtNextUUTOrBatch
 property set to true are closed and removed from the collection. Streams with this property set to false are left unchanged.

#### See Also

[ExecutionOutputRecordStream.CloseAtNextUUTOrBatch](executionoutputrecordstream-closeatnextuutorb.html)

[ExecutionOutputRecordStreams.CloseAndRemoveStream](executionoutputrecordstreams-closeandremovest.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstreams-closeall.html language=enus -->
## TOPIC 01128: ExecutionOutputRecordStreams.CloseAll

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstreams-closeall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstreams-closeall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStreams.CloseAll Purpose Close all ExecutionOutputRecordStream objects in this collection. Remarks Note: The streams are not removed from the collection. Call ExecutionOutputRecordStreams.RemoveAll to remove them. See Also ExecutionOutputRecordStreams.RemoveAll

### ExecutionOutputRecordStreams.CloseAll

#### Syntax

[ExecutionOutputRecordStreams](executionoutputrecordstreams.html).CloseAll

#### Purpose

Close all
 ExecutionOutputRecordStream
 objects in this collection.

#### Remarks

Note

ExecutionOutputRecordStreams.RemoveAll

#### See Also

[ExecutionOutputRecordStreams.RemoveAll](executionoutputrecordstreams-removeall.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstreams-closeandremovest.html language=enus -->
## TOPIC 01129: ExecutionOutputRecordStreams.CloseAndRemoveStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstreams-closeandremovest.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstreams-closeandremovest.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStreams.CloseAndRemoveStream( streamName) Purpose Close the specified stream and remove it from this collection. Parameters streamName As String [In] The name of the stream to close and remove. The name is case sensitive. Specifying a stream that does not exist causes a r

### ExecutionOutputRecordStreams.CloseAndRemoveStream

#### Syntax

[ExecutionOutputRecordStreams](executionoutputrecordstreams.html).CloseAndRemoveStream( streamName)

#### Purpose

Close the specified stream and remove it from this collection.

#### Parameters

streamName
 As
 [String](data-types-for-teststand.html)

[In] The name of the stream to close and remove. The name is case sensitive.

Specifying a stream that does not exist causes a run-time error.

#### See Also

[ExecutionOutputRecordStreams.NewStream](executionoutputrecordstreams-newstream.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstreams-getstream.html language=enus -->
## TOPIC 01130: ExecutionOutputRecordStreams.GetStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstreams-getstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstreams-getstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStreams.GetStream( streamName) Return Value ExecutionOutputRecordStream Purpose Get the ExecutionOutputRecordStream with the specified name. Remarks ExecutionOutputRecordStreams.GetStream throws a run-time error if the specified stream does not exist. Parameters streamNam

### ExecutionOutputRecordStreams.GetStream

#### Syntax

[ExecutionOutputRecordStreams](executionoutputrecordstreams.html).GetStream( streamName)

#### Return Value

[ExecutionOutputRecordStream](executionoutputrecordstream.html)

#### Purpose

Get the
 ExecutionOutputRecordStream
 with the specified name.

#### Remarks

ExecutionOutputRecordStreams.GetStream
 throws a run-time error if the specified stream does not exist.

#### Parameters

streamName
 As
 [String](data-types-for-teststand.html)

[In] The name of the stream to get. The name is case sensitive.

#### See Also

[ExecutionOutputRecordStreams.NewStream](executionoutputrecordstreams-newstream.html)

[ExecutionOutputRecordStreams.CloseAndRemoveStream](executionoutputrecordstreams-closeandremovest.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstreams-newstream.html language=enus -->
## TOPIC 01131: ExecutionOutputRecordStreams.NewStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstreams-newstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstreams-newstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStreams.NewStream( streamName) Return Value ExecutionOutputRecordStream Purpose Create a new ExecutionOutputRecordStream attached to the execution associated with this ExecutionOutputRecordStreams collection. Remarks Attempting to create a new stream with the same name as

### ExecutionOutputRecordStreams.NewStream

#### Syntax

[ExecutionOutputRecordStreams](executionoutputrecordstreams.html).NewStream( streamName)

#### Return Value

[ExecutionOutputRecordStream](executionoutputrecordstream.html)

#### Purpose

Create a new
 ExecutionOutputRecordStream
 attached to the execution associated with this
 ExecutionOutputRecordStreams
 collection.

#### Remarks

Attempting to create a new stream with the same name as an existing stream that is already part of this
 ExecutionOutputRecordStreams
 collection causes a run-time error.

#### Parameters

streamName
 As
 [String](data-types-for-teststand.html)

[In] The name of the stream to create. The name must be unique within this
 ExecutionOutputRecordStreams
 collection. Names are case sensitive.

#### See Also

[ExecutionOutputRecordStreams.GetStream](executionoutputrecordstreams-getstream.html)

[ExecutionOutputRecordStreams.CloseAndRemoveStream](executionoutputrecordstreams-closeandremovest.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstreams-removeall.html language=enus -->
## TOPIC 01132: ExecutionOutputRecordStreams.RemoveAll

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstreams-removeall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstreams-removeall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExecutionOutputRecordStreams.RemoveAll Purpose Remove all ExecutionOutputRecordStream objects from this collection. Remarks Note: The streams are not automatically closed when you remove them. Call ExecutionOutputRecordStreams.CloseAll first to close them. See Also ExecutionOutputRecordStream

### ExecutionOutputRecordStreams.RemoveAll

#### Syntax

[ExecutionOutputRecordStreams](executionoutputrecordstreams.html).RemoveAll

#### Purpose

Remove all
 ExecutionOutputRecordStream
 objects from this collection.

#### Remarks

Note

ExecutionOutputRecordStreams.CloseAll

#### See Also

[ExecutionOutputRecordStreams.CloseAll](executionoutputrecordstreams-closeall.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionoutputrecordstreams.html language=enus -->
## TOPIC 01133: ExecutionOutputRecordStreams

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionoutputrecordstreams.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionoutputrecordstreams.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Methods BeginNextUUTOrBatch CloseAll CloseAndRemoveStream GetStream NewStream RemoveAll

### ExecutionOutputRecordStreams

#### Methods

| BeginNextUUTOrBatch |
| --- |
| CloseAll |
| CloseAndRemoveStream |
| GetStream |
| NewStream |
| RemoveAll |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionrunstates.html language=enus -->
## TOPIC 01134: ExecutionRunStates

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionrunstates.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionrunstates.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Execution.GetStates method returns one of these values to indicate the running state of the execution. ExecRunState_Paused –(Value: 2) The execution is suspended. ExecRunState_Running –(Value: 1) The execution is running. ExecRunState_Stopped –(Value: 3) The execution has finished executing. See

### ExecutionRunStates

The
 [Execution.GetStates](execution-getstates.html)
 method returns one of these values to indicate the running state of the execution.

- ExecRunState_Paused 
 –(Value: 2) The execution is suspended.
- ExecRunState_Running 
 –(Value: 1) The execution is running.
- ExecRunState_Stopped 
 –(Value: 3) The execution has finished executing.

#### See Also

[Execution.Break](execution-break.html)

[Execution.GetStates](execution-getstates.html)

[Execution.RestartEx](execution-restartex.html)

[Execution.Resume](execution-resume.html)

[Execution.StepInto](execution-stepinto.html)

[Execution.StepOver](execution-stepover.html)

[Execution.Terminate](execution-terminate.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executionterminationstates.html language=enus -->
## TOPIC 01135: ExecutionTerminationStates

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executionterminationstates.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executionterminationstates.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Execution.GetStates method returns one of these values to indicate whether the execution is terminating. If the execution is terminating, these values indicate how it is terminating. ExecTermState_Aborting –(Value: 4) TestStand is aborting the running execution. ExecTermState_KillingThreads –(Va

### ExecutionTerminationStates

The
 [Execution.GetStates](execution-getstates.html)
 method returns one of these values to indicate whether the execution is terminating. If the execution is terminating, these values indicate how it is terminating.

- ExecTermState_Aborting 
 –(Value: 4) TestStand is aborting the running execution.
- ExecTermState_KillingThreads 
 –(Value: 5) TestStand is ending the threads in the execution.
- ExecTermState_Normal 
 –(Value: 1) The execution is not terminating.
- ExecTermState_Terminating 
 –(Value: 2) TestStand is terminating the running execution.
- ExecTermState_TerminatingInteractive 
 –(Value: 3) TestStand is terminating the running interactive execution.

#### See Also

[Execution.GetStates](execution-getstates.html)

[Execution.RestartEx](execution-restartex.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/executiontypemask.html language=enus -->
## TOPIC 01136: ExecutionTypeMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/executiontypemask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/executiontypemask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the executionTypeMaskParam parameter of the Engine.NewExecution , Engine.NewHierarchicalExecution , and SequenceContext.NewExecution methods. ExecTypeMask_AutoWaitAtEndOfSequence –(Value: 0x80) Use this option to have the calling sequence wait for the launching executi

### ExecutionTypeMask

Use these constants to specify the
 executionTypeMaskParam
 parameter of the
 [Engine.NewExecution](engine-newexecution.html)
 ,
 [Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)
 , and
 [SequenceContext.NewExecution](sequencecontext-newexecution.html)
 methods.

- ExecTypeMask_AutoWaitAtEndOfSequence 
 –(Value: 0x80) Use this option to have the calling sequence wait for the launching execution to complete before the calling sequence returns. This constant applies only to the
 SequenceContext.NewExecution 
 method.
- ExecTypeMask_BreakOnSequenceFailure 
 –(Value: 0x40) Specifies whether the sequence editor and user interfaces suspend when a failing step causes a sequence failure to first occur. TestStand does not suspend on failing
 Sequence Call 
 steps already in the stack. If the sequence failure setting is reset, TestStand suspends when the next failing step causes sequence failure. When this constant is not set, TestStand suspends execution based on the value of the setting in the
 StationOptions.BreakOnSequenceFailure 
 property.
- ExecTypeMask_BreakOnStepFailure 
 –(Value: 0x20) Specifies whether the sequence editor and user interfaces suspend when a step fails. TestStand does not suspend an execution on a failing Sequence Call step if the step that caused the sequence failure already suspended execution. When this constant is not set, TestStand suspends execution based on the value of the setting in the
 StationOptions.BreakOnStepFailure 
 property.
- ExecTypeMask_CloseWindowWhenDone 
 –(Value: 0x10) Directs the sequence editor and user interfaces to close the Execution window when it finishes executing.
- ExecTypeMask_DiscardArgumentsWhenDone 
 –(Value: 0x400) Directs the execution to discard its arguments when it finishes executing. Executions normally hold arguments until the execution is destroyed so the execution can use the arguments again if the execution restarts. However, because the execution holds the arguments, arguments that contain a reference to a .NET object prevent TestStand from unloading .NET assemblies until the execution is destroyed. Use this option to avoid this situation and to ensure that TestStand more promptly cleans up arguments. When using this option, if you restart the execution, the execution no longer uses any arguments unless you use the
 Execution.RestartWithNewArguments 
 method to restart it.
- ExecTypeMask_DisplayPreloadProgress 
 –(Value: 0x200) Specifies to launch the
 Preload Progress 
 dialog box while preloading code modules for the execution of a sequence file. You normally use this flag only for executions you initiate from a user interface.
- ExecTypeMask_InitiallyHidden 
 –(Value: 0x1) Specifies that an execution does not appear in a window unless a trace or break event occurs. Typically, you use this constant for executions you do not want the user to see unless an error occurs. Use this constant with
 ExecTypeMask_TracingInitiallyOff 
 flag to hide the execution even when tracing is on for the application.
- ExecTypeMask_InitiallySuspended 
 –(Value: 0x4) Specifies that the execution is created in a suspended state. You must call the
 Execution.Resume 
 method to continue execution.
- ExecTypeMask_Normal 
 –(Value: 0) Specifies that the execution is visible in the window when it starts.
- ExecTypeMask_NotRestartable 
 –(Value: 0x8) Specifies that the execution cannot be restarted with the
 Execution.RestartEx 
 method.
- ExecTypeMask_TracingInitiallyOff 
 –(Value: 0x2) Disables tracing for the execution. Tracing can be turned back on by either a sequence call setting or by setting the
 RunState.Tracing 
 property of the sequence context to
 True 
 .
- ExecTypeMask_UseSTA 
 –(Value: 0x100) Specifies whether TestStand initializes the concurrency model of the thread as single-threaded apartment (STA) or multi-threaded apartment (MTA). By default, TestStand initializes new executions and threads to use the MTA model. A thread must use the STA model if the thread creates or launches a dialog box that contains ActiveX controls. 

If you use this option to launch a sequence with a step that displays an ActiveX control, you might need to set the Load Option on the
 Run Options tab 
 of the
 Step Properties 
 dialog box to
 Load dynamically 
 . This option ensures that TestStand loads the module the step calls in the thread initialized as STA.

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

[Execution.RestartEx](execution-restartex.html)

[Execution.Resume](execution-resume.html)

[Execution.TypeMask](execution-typemask.html)

[Run Options tab](../tsref/run-options-tab-step-properties-dialog-box.html)

[SequenceContext.NewExecution](sequencecontext-newexecution.html)

[StationOptions.BreakOnSequenceFailure](stationoptions-breakonsequencefailure.html)

[StationOptions.BreakOnStepFailure](stationoptions-breakonstepfailure.html)

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression-evaluate.html language=enus -->
## TOPIC 01137: Expression.Evaluate

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression-evaluate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression-evaluate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Expression.Evaluate( evaluationContext, evaluationOptions = EvalOption_NoOptions) Return Value PropertyObject Returns the result of the expression in the form of a PropertyObject. The PropertyObject can contain a value of any type depending on the expression. Release the result when you finis

### Expression.Evaluate

#### Syntax

[Expression](expression.html).Evaluate( evaluationContext, evaluationOptions = EvalOption_NoOptions)

#### Return Value

[PropertyObject](propertyobject.html)

Returns the result of the expression in the form of a PropertyObject. The PropertyObject can contain a value of any type depending on the expression. Release the result when you finish using it. If the expression is empty and you pass
 EvalOption_AllowEmptyExpression
 , this method returns a
 NULL
 dispatch pointer or object reference.

#### Purpose

Evaluates an expression and returns the result.

#### Parameters

evaluationContext
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the context in which to evaluate the expression. This method uses this object to locate variables the expression specifies.

evaluationOptions
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 to specify the default behavior, or pass one or more
 [EvaluationOptions](evaluationoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options.

This parameter has a default value of
 EvalOption_NoOptions
 .

#### See Also

[Engine.CheckExpression](engine-checkexpression.html)

[Engine.CheckExprSyntax](engine-checkexprsyntax.html)

[EvaluationOptions](evaluationoptions.html)

[Expression.Validate](expression-validate.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[PropertyObject](propertyobject.html)

[PropertyObject.EvaluateEx](propertyobject-evaluateex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression-getconstantvalue.html language=enus -->
## TOPIC 01138: Expression.GetConstantValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression-getconstantvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression-getconstantvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Expression.GetConstantValue Return Value PropertyObject Purpose If the expression is a constant, the method returns the result of the expression in the form of a PropertyObject, otherwise the method returns NULL . Remarks This method evaluates the expression without a context and without alte

### Expression.GetConstantValue

#### Syntax

[Expression](expression.html).GetConstantValue

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

If the expression is a constant, the method returns the result of the expression in the form of a PropertyObject, otherwise the method returns
 NULL
 .

#### Remarks

This method evaluates the expression without a context and without altering values.

#### See Also

[Engine.CheckExpression](engine-checkexpression.html)

[Engine.CheckExprSyntax](engine-checkexprsyntax.html)

[Expression.Evaluate](expression-evaluate.html)

[Expression.Validate](expression-validate.html)

[PropertyObject](propertyobject.html)

[PropertyObject.EvaluateEx](propertyobject-evaluateex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression-gettoken.html language=enus -->
## TOPIC 01139: Expression.GetToken

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression-gettoken.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression-gettoken.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Expression.GetToken( tokenIndex, tokenCode, charIndex, numChars, tokenText) Purpose This method returns information about the token you specify by index. You must call the Expression.Tokenize method before you call this method for the first time and before you call this method after changing

### Expression.GetToken

#### Syntax

[Expression](expression.html).GetToken( tokenIndex, tokenCode, charIndex, numChars, tokenText)

#### Purpose

This method returns information about the token you specify by index. You must call the
 [Expression.Tokenize](expression-tokenize.html)
 method before you call this method for the first time and before you call this method after changing the value the
 [Expression.Text](expression-text.html)
 property.

#### Parameters

tokenIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of a token in the expression.

tokenCode
 As
 [TokenCode](tokencode.html)

[Out] Returns a code that specifies which expression element the token represents.

charIndex
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the zero-based index within the expression string of the first character in the token.

numChars
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the number of characters in the token.

tokenText
 As
 [String](data-types-for-teststand.html)

[Out] Returns the characters in the token.

#### See Also

[Expression.NumTokens](expression-numtokens.html)

[Expression.Text](expression-text.html)

[Expression.Tokenize](expression-tokenize.html)

[TokenCode](tokencode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression-numtokens.html language=enus -->
## TOPIC 01140: Expression.NumTokens

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression-numtokens.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression-numtokens.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Expression.NumTokens Data Type Long Purpose Returns the number of tokens the expression contains. A token is a set of contiguous characters in the expression text that represent an identifier, operator, or constant. A token does not include surrounding white space characters. You must call th

### Expression.NumTokens

#### Syntax

[Expression](expression.html).NumTokens

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of tokens the expression contains. A token is a set of contiguous characters in the expression text that represent an identifier, operator, or constant. A token does not include surrounding white space characters.

Note

Expression.Tokenize

Expression.Text

#### See Also

[Expression.GetToken](expression-gettoken.html)

[Expression.Text](expression-text.html)

[Expression.Tokenize](expression-tokenize.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression-text.html language=enus -->
## TOPIC 01141: Expression.Text

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression-text.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression-text.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Expression.Text Data Type String Purpose Specifies the text of the expression the Expression object evaluates. The following are example expressions: Local.frequency / 2 "DMM" + Str(RunState.TestSockets.MyIndex) See Also Evaluate NumTokens Validate

### Expression.Text

#### Syntax

[Expression](expression.html).Text

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the text of the expression the
 Expression
 object evaluates. The following are example expressions:

Local.frequency / 2

"DMM" + Str(RunState.TestSockets.MyIndex)

#### See Also

[Evaluate](expression-evaluate.html)

[NumTokens](expression-numtokens.html)

[Validate](expression-validate.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression-tokenize.html language=enus -->
## TOPIC 01142: Expression.Tokenize

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression-tokenize.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression-tokenize.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Expression.Tokenize( options, initialParseState) Return Value Long The return value represents the parsing state at the end of the expression. If you individually tokenize each displayed line of an expression wrapped to multiple lines by a user interface control, pass this value to the initia

### Expression.Tokenize

#### Syntax

[Expression](expression.html).Tokenize( options, initialParseState)

#### Return Value

[Long](data-types-for-teststand.html)

The return value represents the parsing state at the end of the expression.

If you individually tokenize each displayed line of an expression wrapped to multiple lines by a user interface control, pass this value to the
 initialParseState
 parameter of this method when you tokenize the next visible line.

#### Purpose

This method parses the expression text to identify the tokens that represent operators, identifiers, and constants. The capability to parse the expression into component tokens is useful for specialized purposes, such as implementing expression syntax coloring. Typically, you do not call this method.

Note

Expression.GetToken

Expression.NumTokens

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 TokenizeOptions_NoOptions
 to specify the default behavior, or pass one or more
 [TokenizeOptions](tokenizeoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options. The Expression object retains the options you specify to use whenever it must tokenize the expression in the
 [Expression.Validate](expression-validate.html)
 and
 [Expression.Evaluate](expression-evaluate.html)
 methods.

initialParseState
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 if you are tokenizing a complete expression. Typically, you pass
 0
 to this parameter.

If you separately tokenize each visible line in an expression, pass
 0
 to tokenize the first visible line and pass the return value of this method from tokenizing the previous line to tokenize a subsequent line.

Note

#### See Also

[Expression.Evaluate](expression-evaluate.html)

[Expression.GetToken](expression-gettoken.html)

[Expression.NumTokens](expression-numtokens.html)

[Expression.Validate](expression-validate.html)

[TokenizeOptions](tokenizeoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression-validate.html language=enus -->
## TOPIC 01143: Expression.Validate

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression-validate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression-validate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Expression.Validate( evaluationContext, checkSyntaxOnly, evaluationOptions, errMsg, errorCharIndex, errorEndCharIndex) Return Value Boolean Returns True if the expression is valid. Returns False if the expression contains an error. Purpose Checks the validity of an expression and returns erro

### Expression.Validate

#### Syntax

[Expression](expression.html).Validate( evaluationContext, checkSyntaxOnly, evaluationOptions, errMsg, errorCharIndex, errorEndCharIndex)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the expression is valid. Returns
 False
 if the expression contains an error.

#### Purpose

Checks the validity of an expression and returns error information.

#### Parameters

evaluationContext
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the context in which to evaluate the expression. This method uses this object to determine whether the variables in the expression are valid.

checkSyntaxOnly
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to check the expression syntax only. Pass
 False
 to also verify that the variables in the expression are valid.

evaluationOptions
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 to specify the default behavior, or pass one or more
 [EvaluationOptions](evaluationoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options.

errMsg
 As
 [String](data-types-for-teststand.html)

[Out] If the expression is invalid, this parameter returns a description of the error.

errorCharIndex
 As
 [Long](data-types-for-teststand.html)

[Out] If the expression is invalid, this parameter returns the character index of the start of the invalid portion of the expression.

errorEndCharIndex
 As
 [Long](data-types-for-teststand.html)

[Out] If the expression is invalid, this parameter returns the character index of the end of the invalid portion of the expression.

#### See Also

[Engine.CheckExpression](engine-checkexpression.html)

[Engine.CheckExprSyntax](engine-checkexprsyntax.html)

[EvaluationOptions](evaluationoptions.html)

[Expression.Evaluate](expression-evaluate.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[PropertyObject](propertyobject.html)

[PropertyObject.EvaluateEx](propertyobject-evaluateex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression-validateevaluationtype.html language=enus -->
## TOPIC 01144: Expression.ValidateEvaluationType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression-validateevaluationtype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression-validateevaluationtype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Expression.ValidateEvaluationType( validEvaluationTypes, additionalConstants, evaluationContext, evaluationOptions, errMsg, errorStartIndex, errorEndIndex) Return Value TSError Purpose Checks that the expression evaluates to a specified type and returns error information if the expression doe

### Expression.ValidateEvaluationType

#### Syntax

[Expression](expression.html).ValidateEvaluationType( validEvaluationTypes, additionalConstants, evaluationContext, evaluationOptions, errMsg, errorStartIndex, errorEndIndex)

#### Return Value

[TSError](tserror.html)

#### Purpose

Checks that the expression evaluates to a specified type and returns error information if the expression does not.

#### Remarks

This method returns
 TS_Err_NoError
 if the expression evaluates to a type the
 validEvaluationTypes
 parameter specifies. This method returns the corresponding TSError if the expression has a syntax or evaluation error. This method returns
 TS_Err_UnexpectedType
 if the expression evaluates without an error, but does not evaluate to a type the
 validEvaluationTypes
 parameter specifies.

#### Parameters

validEvaluationTypes
 As
 [EvaluationTypes](evaluationtypes.html)

[In] Specifies the type(s) to which you expect the expression to evaluate.

additionalConstants
 As
 [Object Array](data-types-for-teststand.html)

[In] Specifies additional variables the expression might contain that are not part of the
 evaluationContext
 . This parameter is useful if the expression can contain a constant from an enumeration, such as a parameter value of a module call when the parameter type is an enumeration. You can pass
 NULL
 for this parameter if there are no additional constants you want to use when evaluating the expression.

evaluationContext
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the context in which to evaluate the expression. This method uses this object to locate variables the expression specifies.

evaluationOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies any combination of the
 [EvaluationOptions](evaluationoptions.html)
 constants. It is not necessary to pass the
 EvalOption_DoNotAlterValues
 constant because this method never alters values.

errMsg
 As
 [String](data-types-for-teststand.html)

[Out] If the expression does not evaluate to the specified type, this parameter returns a description of the error.

errorStartIndex
 As
 [Long](data-types-for-teststand.html)

[Out] If the expression does not evaluate to the specified type, this parameter returns the character index of the start of the invalid portion of the expression.

errorEndIndex
 As
 [Long](data-types-for-teststand.html)

[Out] If the expression does not evaluate to the specified type, this parameter returns the character index of the end of the invalid portion of the expression.

#### See Also

[EvaluationOptions](evaluationoptions.html)

[EvaluationTypes](evaluationtypes.html)

[Expression.Evaluate](expression-evaluate.html)

[Expression.Validate](expression-validate.html)

[PropertyObject](propertyobject.html)

[TSError](tserror.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expression.html language=enus -->
## TOPIC 01145: Expression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An Expression object holds an expression string. You can check the validity of the expression string or you can evaluate the expression string to obtain the result of the expression. The Expression object provides the same functionality as the PropertyObject.EvaluateEx , Engine.CheckExpression , and

### Expression

An Expression object holds an expression string. You can check the validity of the expression string or you can evaluate the expression string to obtain the result of the expression.

The Expression object provides the same functionality as the
 [PropertyObject.EvaluateEx](propertyobject-evaluateex.html)
 ,
 [Engine.CheckExpression](engine-checkexpression.html)
 , and
 [Engine.CheckExprSyntax](engine-checkexprsyntax.html)
 methods. However, if you are repeatedly evaluating the same expression, it is more efficient to use an Expression object because it only parses the expression string when you first evaluate the expression. Because the Expression object retains the parsed form of the expression, it does not re-parse the expression when you reevaluate the same string.

The Expression object also provides the
 [NumTokens](expression-numtokens.html)
 property and the
 [Tokenize](expression-tokenize.html)
 and
 [GetToken](expression-gettoken.html)
 methods, which you can use to identify the operators, identifiers, and constants that comprise an expression. The capability to parse the expression into component tokens is useful for specialized purposes, such as implementing expression syntax coloring. Because TestStand provides an ActiveX Expression control that features syntax coloring, you typically do not need to identify the tokens in an expression.

#### Properties

| NumTokens (Read Only) |
| --- |
| Text |

#### Methods

| Evaluate |
| --- |
| GetConstantValue |
| GetToken |
| Tokenize |
| Validate |
| ValidateEvaluationType |

#### See Also

[Engine.CheckExpression](engine-checkexpression.html)

[Engine.CheckExprSyntax](engine-checkexprsyntax.html)

[Expression.GetToken](expression-gettoken.html)

[Expression.NumTokens](expression-numtokens.html)

[Expression.Tokenize](expression-tokenize.html)

[PropertyObject.EvaluateEx](propertyobject-evaluateex.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/expressvimenuitemproperties.html language=enus -->
## TOPIC 01146: ExpressVIMenuItemProperties

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/expressvimenuitemproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/expressvimenuitemproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these property names with the property objects the LabVIEWAdapter.GetExpressVIMenuStructure method returns to access information about menu structures. ExpressVIMenu_IconProp –(Value: IconHandle) Numeric value that is the handle in a metafile that contains the icon of the Express VI. ExpressVIMe

### ExpressVIMenuItemProperties

Use these property names with the property objects the
 [LabVIEWAdapter.GetExpressVIMenuStructure](labviewadapter-getexpressvimenustructure.html)
 method returns to access information about menu structures.

- ExpressVIMenu_IconProp 
 –(Value: IconHandle) Numeric value that is the handle in a metafile that contains the icon of the Express VI.
- ExpressVIMenu_IsSubmenuProp 
 –(Value: IsSubMenu) Boolean value that specifies whether the menu item is a submenu. Use
 ExpressVIMenu_MenuItemsProp 
 to access the submenu items.
- ExpressVIMenu_MenuItemsProp 
 –(Value: MenuItems) PropertyObject array that represents the menu items in a submenu.
- ExpressVIMenu_NameProp 
 –(Value: ItemName) String value that specifies the text to display for the menu item.
- ExpressVIMenu_PathProp 
 –Value: ItemPath) String value that specifies the absolute path to the Express VI.
- ExpressVIMenu_SeparatorAboveProp 
 –(Value: SeparatorAbove) Boolean value that specifies whether a separator exists above the menu item.

#### See Also

[LabVIEWAdapter.GetExpressVIMenuStructure](labviewadapter-getexpressvimenustructure.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewer-arguments.html language=enus -->
## TOPIC 01147: ExternalReportViewer.Arguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewer-arguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewer-arguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewer.Arguments Data Type String Purpose Specifies optional arguments that indicate to the external viewer which file to open and how to open it. For example, "%filename" indicates to the external viewer the name of the file to open. See Also ExternalReportViewer.Path

### ExternalReportViewer.Arguments

#### Syntax

[ExternalReportViewer](externalreportviewer.html).Arguments

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies optional arguments that indicate to the external viewer which file to open and how to open it. For example,
 "%filename"
 indicates to the external viewer the name of the file to open.

#### See Also

[ExternalReportViewer.Path](externalreportviewer-path.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewer-autolaunch.html language=enus -->
## TOPIC 01148: ExternalReportViewer.AutoLaunch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewer-autolaunch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewer-autolaunch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewer.AutoLaunch Data Type Boolean Purpose Specifies the external report viewer to launch automatically when the report is generated. Set this property to True to automatically launch the external report viewer and show the report. See Also ExternalReportViewers.AutoLaunchDefau

### ExternalReportViewer.AutoLaunch

#### Syntax

[ExternalReportViewer](externalreportviewer.html).AutoLaunch

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies the external report viewer to launch automatically when the report is generated.

Set this property to
 True
 to automatically launch the external report viewer and show the report.

#### See Also

[ExternalReportViewers.AutoLaunchDefaultExternalViewers](externalreportviewers-autolaunchdefaultextern.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewer-format.html language=enus -->
## TOPIC 01149: ExternalReportViewer.Format

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewer-format.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewer-format.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewer.Format Data Type String Purpose Specifies the report format for the external report viewer to display. For example, txt for text files or HTML for HTML files. See Also Report.Format

### ExternalReportViewer.Format

#### Syntax

[ExternalReportViewer](externalreportviewer.html).Format

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the report format for the external report viewer to display. For example,
 txt
 for text files or
 HTML
 for HTML files.

#### See Also

[Report.Format](report-format.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewer-path.html language=enus -->
## TOPIC 01150: ExternalReportViewer.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewer-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewer-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewer.Path Data Type String Purpose Specifies the filename the external report viewer executes. See Also ExternalReportViewer.Arguments

### ExternalReportViewer.Path

#### Syntax

[ExternalReportViewer](externalreportviewer.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the filename the external report viewer executes.

#### See Also

[ExternalReportViewer.Arguments](externalreportviewer-arguments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewer.html language=enus -->
## TOPIC 01151: ExternalReportViewer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: An ExternalReportViewer represents relationships between a specific report format and the application used to open it. TestStand keeps a list of report viewers. If you do not specify an external viewer for a format, the file opens in the application Microsoft Windows associates with the file extensi

### ExternalReportViewer

An ExternalReportViewer represents relationships between a specific report format and the application used to open it. TestStand keeps a list of report viewers. If you do not specify an external viewer for a format, the file opens in the application Microsoft Windows associates with the file extension of the report file.

#### Properties

| Arguments |
| --- |
| AutoLaunch |
| Format |
| Path |

#### See Also

[ExternalReportViewers](externalreportviewers.html)

[Report](report.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewers-add.html language=enus -->
## TOPIC 01152: ExternalReportViewers.Add

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewers-add.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewers-add.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewers.Add( format, path, arguments, autoLaunch) Purpose Adds a new external report viewer to the collection. Parameters format As String [In] When you specify an external report viewer, you must indicate the external report viewer name and the report format, such as Microsoft

### ExternalReportViewers.Add

#### Syntax

[ExternalReportViewers](externalreportviewers.html).Add( format, path, arguments, autoLaunch)

#### Purpose

Adds a new external report viewer to the collection.

#### Parameters

format
 As
 [String](data-types-for-teststand.html)

[In] When you specify an external report viewer, you must indicate the external report viewer name and the report format, such as Microsoft Notepad (
 txt
 ) or Google Chrome (
 html
 ).

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name for the external report viewer to launch.

arguments
 As
 [String](data-types-for-teststand.html)

[In] Specifies the optional command-line arguments required to launch the external report viewer.

autoLaunch
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies the external report viewer to automatically launch when the report is generated. Pass
 True
 to automatically launch the external report viewer and show the report.

#### See Also

[ExternalReportViewers.Remove](externalreportviewers-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewers-autolaunchdefaultextern.html language=enus -->
## TOPIC 01153: ExternalReportViewers.AutoLaunchDefaultExternalViewers

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewers-autolaunchdefaultextern.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewers-autolaunchdefaultextern.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewers.AutoLaunchDefaultExternalViewers Data Type Boolean Purpose Specifies whether TestStand launches default external viewers Microsoft Windows associates with file extensions.

### ExternalReportViewers.AutoLaunchDefaultExternalViewers

#### Syntax

[ExternalReportViewers](externalreportviewers.html).AutoLaunchDefaultExternalViewers

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether TestStand launches default external viewers Microsoft Windows associates with file extensions.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewers-count.html language=enus -->
## TOPIC 01154: ExternalReportViewers.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewers-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewers-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewers.Count Data Type Long Purpose Returns the number of items in the collection. See Also ExternalReportViewers.Item

### ExternalReportViewers.Count

#### Syntax

[ExternalReportViewers](externalreportviewers.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[ExternalReportViewers.Item](externalreportviewers-item.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewers-item.html language=enus -->
## TOPIC 01155: ExternalReportViewers.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewers-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewers-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewers.Item( index) Data Type ExternalReportViewer Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also ExternalReportViewer ExternalReportViewers.Count

### ExternalReportViewers.Item

#### Syntax

[ExternalReportViewers](externalreportviewers.html).Item( index)

#### Data Type

[ExternalReportViewer](externalreportviewer.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[ExternalReportViewer](externalreportviewer.html)

[ExternalReportViewers.Count](externalreportviewers-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewers-remove.html language=enus -->
## TOPIC 01156: ExternalReportViewers.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewers-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewers-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ExternalReportViewers.Remove( index) Purpose Removes the specified item from this collection, if it exists. Parameters index As Long [In] Specifies the zero-based index of the item to remove. See Also ExternalReportViewers.Add

### ExternalReportViewers.Remove

#### Syntax

[ExternalReportViewers](externalreportviewers.html).Remove( index)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to remove.

#### See Also

[ExternalReportViewers.Add](externalreportviewers-add.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/externalreportviewers.html language=enus -->
## TOPIC 01157: ExternalReportViewers

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/externalreportviewers.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/externalreportviewers.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Collection that contains elements using the ExternalReportViewer type. Represents the list of external report viewers used to open the different report file types TestStand supports. Properties AutoLaunchDefaultExternalViewers Count (Read Only) Item (Read Only) Methods Add Remove See Also Engine.Ext

### ExternalReportViewers

Collection that contains elements using the ExternalReportViewer type.

Represents the list of external report viewers used to open the different report file types TestStand supports.

#### Properties

| AutoLaunchDefaultExternalViewers |
| --- |
| Count (Read Only) |
| Item (Read Only) |

#### Methods

| Add |
| --- |
| Remove |

#### See Also

[Engine.ExternalReportViewers](engine-externalreportviewers.html)

[ExternalReportViewer](externalreportviewer.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/failureactions.html language=enus -->
## TOPIC 01158: FailureActions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/failureactions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/failureactions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these options to specify whether execution proceeds to the Cleanup step group when a step sets the status property of the sequence to Failed . FailureAction_GotoCleanup –(Value: 1) Specifies that execution flow proceeds to the Cleanup step group if the step sets the status property of the sequen

### FailureActions

Use these options to specify whether execution proceeds to the Cleanup step group when a step sets the status property of the sequence to
 Failed
 .

- FailureAction_GotoCleanup 
 –(Value: 1) Specifies that execution flow proceeds to the Cleanup step group if the step sets the status property of the sequence to
 Failed 
 .
- FailureAction_None 
 –(Value: 0) Specifies that execution flow does not proceed to the Cleanup step group if the step sets the status property of the sequence to
 Failed 
 .
- FailureAction_UseStationOption 
 –(Value: 2) Specifies that execution flow proceeds to the Cleanup step group if the step sets the status property of the sequence to
 Failed 
 and the value of the
 StationOptions.AlwaysGotoCleanupOnFailure 
 property is
 True 
 .

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileglobalsscopeoptions.html language=enus -->
## TOPIC 01159: FileGlobalsScopeOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileglobalsscopeoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileglobalsscopeoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SequenceFile.FileGlobalsScope property to specify the scope of the sequence file global variables. FileGlobalsScopeOption_AllExecutionsShare –(Value: 1) Specifies that the first execution that runs the sequence file creates a run-time copy of the global variables and ini

### FileGlobalsScopeOptions

Use these constants with the
 [SequenceFile.FileGlobalsScope](sequencefile-fileglobalsscope.html)
 property to specify the scope of the sequence file global variables.

- FileGlobalsScopeOption_AllExecutionsShare 
 –(Value: 1) Specifies that the first execution that runs the sequence file creates a run-time copy of the global variables and initializes the variables to the default values. Any other execution that runs the sequence file concurrently uses the same global variables. When the last execution that uses the sequence file global variables completes, TestStand discards the file global variables. A common use case for selecting this option might be when you want to share variables among multiple executions you start with the Batch or Parallel process model.
- FileGlobalsScopeOption_SeparateForEachExecution 
 –(Value: 0) Specifies that each execution that runs the sequence file creates a separate run-time copy of the global variables and initializes the variables to the default values. Threads within an execution share the run-time copy of the variables for the execution.

#### See Also

[SequenceFile.FileGlobalsScope](sequencefile-fileglobalsscope.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-fileexists.html language=enus -->
## TOPIC 01160: FileInformation.FileExists

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-fileexists.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-fileexists.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.FileExists Data Type Boolean Purpose Returns True if a file exists and is accessible at the path specified for this FileInformation object. This property is not cached. TestStand attempts to locate the file on disk every time you call this property. Remarks Use this property t

### FileInformation.FileExists

#### Syntax

[FileInformation](fileinformation.html).FileExists

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if a file exists and is accessible at the path specified for this
 [FileInformation](fileinformation.html)
 object. This property is not cached. TestStand attempts to locate the file on disk every time you call this property.

#### Remarks

Use this property to determine whether you can use the other properties and methods on the
 FileInformation
 object.

#### See Also

[FileInformation](fileinformation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-filewritingformat.html language=enus -->
## TOPIC 01161: FileInformation.FileWritingFormat

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-filewritingformat.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-filewritingformat.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.FileWritingFormat Data Type FileWritingFormats Use the following constants with this data type: FileWritingFormat_Binary –(Value: 2) Specifies that TestStand writes the file in a binary format. This format is the fastest and most memory-efficient format. FileWritingFormat_Ini

### FileInformation.FileWritingFormat

#### Syntax

[FileInformation](fileinformation.html).FileWritingFormat

#### Data Type

[FileWritingFormats](filewritingformats.html)

Use the following constants with this data type:

- FileWritingFormat_Binary 
 –(Value: 2) Specifies that TestStand writes the file in a binary format. This format is the fastest and most memory-efficient format.
- FileWritingFormat_Ini 
 –(Value: 1) Specifies that TestStand writes the file in an INI format. This format is used by previous versions of TestStand (3.
 x 
 or earlier). Use this format when necessary to support existing code that reads the INI file directly.
- FileWritingFormat_Xml 
 –(Value: 3) Specifies that TestStand writes the file in an XML format. Use this format if you want to read, parse, or create files as XML. This option is the most readable and parseable format.

#### Purpose

Returns the format in which TestStand wrote a property object file, such as binary, INI, or XML.

#### Remarks

This method is valid only for native TestStand files. Use the
 [FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)
 property to determine whether you can safely access this property.

This property throws an exception if TestStand cannot locate the file when it is first accessed. Use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### See Also

[FileInformation.FileExists](fileinformation-fileexists.html)

[FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)

[PropertyObjectFile.FileWritingFormat](propertyobjectfile-filewritingformat.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-getfileformatdisplayversion.html language=enus -->
## TOPIC 01162: FileInformation.GetFileFormatDisplayVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-getfileformatdisplayversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-getfileformatdisplayversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.GetFileFormatDisplayVersion Return Value String Purpose Returns the format display version of the file if the FileInformation.IsPropertyObjectFile property is True for the file, otherwise this method returns the value from the FileInformation.GetFileFormatVersion method. If no

### FileInformation.GetFileFormatDisplayVersion

#### Syntax

[FileInformation](fileinformation.html).GetFileFormatDisplayVersion

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the format display version of the file if the
 [FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)
 property is
 True
 for the file, otherwise this method returns the value from the
 [FileInformation.GetFileFormatVersion](fileinformation-getfileformatversion.html)
 method. If no format version is available, the method returns an empty string.

#### Remarks

For a property object file, this method returns the TestStand version in which the file was created.

This method returns an error if TestStand cannot locate the file when it is first accessed. Use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### See Also

[FileInformation.FileExists](fileinformation-fileexists.html)

[FileInformation.GetFileFormatVersion](fileinformation-getfileformatversion.html)

[FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-getfileformatversion.html language=enus -->
## TOPIC 01163: FileInformation.GetFileFormatVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-getfileformatversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-getfileformatversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.GetFileFormatVersion Return Value String Purpose Returns the format version of the file. If no format version is available, the method returns an empty string. Remarks Generally, the file format version is the format of the file. The method returns the TestStand Engine version

### FileInformation.GetFileFormatVersion

#### Syntax

[FileInformation](fileinformation.html).GetFileFormatVersion

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the format version of the file. If no format version is available, the method returns an empty string.

#### Remarks

Generally, the file format version is the format of the file. The method returns the TestStand Engine version that saved a TestStand file, the LabVIEW server version that saved a VI file, or the type of binary file for DLL and executable files. For example, the file format version of a Microsoft Windows XP binary executable is usually
 PE
 (Portable Executable), the file format version of a .NET assembly is
 .NET
 , the file format version of a LabVIEW VI is the version of the LabVIEW development system that saved the VI, such as 12.0.0, and the file format version of a TestStand sequence file is the version of the TestStand Engine that saved the file, such as 5.0.0.

This property throws an exception if TestStand cannot locate the file when it is first accessed. Use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### See Also

[FileInformation.FileExists](fileinformation-fileexists.html)

[FileInformation.GetFileVersion](fileinformation-getfileversion.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-getfileversion.html language=enus -->
## TOPIC 01164: FileInformation.GetFileVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-getfileversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-getfileversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.GetFileVersion( val) Return Value Boolean Returns True if the file has a file version. Otherwise, returns False . Purpose Obtains the version of the file. The method returns True if the file has a file version. Otherwise it returns False . Remarks Generally, the file version i

### FileInformation.GetFileVersion

#### Syntax

[FileInformation](fileinformation.html).GetFileVersion( val)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the file has a file version. Otherwise, returns
 False
 .

#### Purpose

Obtains the version of the file. The method returns
 True
 if the file has a file version. Otherwise it returns
 False
 .

#### Remarks

Generally, the file version is the version or revision of the file. The method returns the
 [PropertyObjectFile.Version](propertyobjectfile-version.html)
 property value for TestStand files, the revision from a LabVIEW VI, and file version value in the resource of DLL and executable files.

The version number usually appears in the
 MajorVersion.MinorVersion.RevisionVersion
 format, such as
 1.0.2
 .

This method throws an exception if the file cannot be located when it is first accessed. Use the
 [FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### Parameters

val
 As
 [String](data-types-for-teststand.html)

[Out] Returns the version of the file. If no version is available, the method returns an empty string.

#### See Also

[FileInformation.FileExists](fileinformation-fileexists.html)

[FileInformation.GetFileFormatVersion](fileinformation-getfileformatversion.html)

[PropertyObjectFile.Version](propertyobjectfile-version.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-iscustomfile.html language=enus -->
## TOPIC 01165: FileInformation.IsCustomFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-iscustomfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-iscustomfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.IsCustomFile Data Type Boolean Purpose Returns True if the file is a custom format file TestStand can load using a custom sequence file translator. Remarks Files in native TestStand formats always return False for this property. This property throws an exception if TestStand c

### FileInformation.IsCustomFile

#### Syntax

[FileInformation](fileinformation.html).IsCustomFile

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the file is a custom format file TestStand can load using a custom sequence file translator.

#### Remarks

Files in native TestStand formats always return
 False
 for this property.

This property throws an exception if TestStand cannot locate the file when it is first accessed. Use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### See Also

[FileInformation.FileExists](fileinformation-fileexists.html)

[FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)

[FileInformation.IsSequenceFile](fileinformation-issequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-iscvidll.html language=enus -->
## TOPIC 01166: FileInformation.IsCVIDll

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-iscvidll.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-iscvidll.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.IsCVIDll Data Type Boolean Purpose Returns True if the file is a LabWindows/CVI DLL. Remarks This property returns an error if TestStand cannot locate the file when TestStand first attempts to access the file. Use the FileInformation.FileExists property to determine whether th

### FileInformation.IsCVIDll

#### Syntax

[FileInformation](fileinformation.html).IsCVIDll

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the file is a LabWindows/CVI DLL.

#### Remarks

This property returns an error if TestStand cannot locate the file when TestStand first attempts to access the file. Use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### See Also

[FileInformation.FileExists](fileinformation-fileexists.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-isdotnetassembly.html language=enus -->
## TOPIC 01167: FileInformation.IsDotNetAssembly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-isdotnetassembly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-isdotnetassembly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.IsDotNetAssembly Data Type Boolean Purpose Returns True if the file is a .NET assembly. Remarks Use this property to determine whether you can use the file to specify the assembly for a DotNetModule object. This property returns an error if TestStand cannot locate the file whe

### FileInformation.IsDotNetAssembly

#### Syntax

[FileInformation](fileinformation.html).IsDotNetAssembly

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the file is a .NET assembly.

#### Remarks

Use this property to determine whether you can use the file to specify the assembly for a
 [DotNetModule](dotnetmodule.html)
 object.

This property returns an error if TestStand cannot locate the file when TestStand first attempts to access the file. Use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### See Also

[DotNetModule](dotnetmodule.html)

[DotNetModule.SetAssembly](dotnetmodule-setassembly.html)

[Engine.GetFileInformation](engine-getfileinformation.html)

[FileInformation.FileExists](fileinformation-fileexists.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-ispropertyobjectfile.html language=enus -->
## TOPIC 01168: FileInformation.IsPropertyObjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-ispropertyobjectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-ispropertyobjectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.IsPropertyObjectFile Data Type Boolean Purpose Returns True if the file is a TestStand PropertyObjectFile . Remarks Use this property to determine whether you can load the file using the PropertyObjectFile.ReadFile method. This property throws an exception if TestStand cannot

### FileInformation.IsPropertyObjectFile

#### Syntax

[FileInformation](fileinformation.html).IsPropertyObjectFile

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the file is a TestStand
 [PropertyObjectFile](propertyobjectfile.html)
 .

#### Remarks

Use this property to determine whether you can load the file using the
 [PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)
 method.

This property throws an exception if TestStand cannot locate the file when it is first accessed. Use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### See Also

[FileInformation.FileExists](fileinformation-fileexists.html)

[FileInformation.IsCustomFile](fileinformation-iscustomfile.html)

[FileInformation.IsSequenceFile](fileinformation-issequencefile.html)

[PropertyObjectFile](propertyobjectfile.html)

[PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-issequencefile.html language=enus -->
## TOPIC 01169: FileInformation.IsSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-issequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-issequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.IsSequenceFile Data Type Boolean Purpose Returns True if the file is a TestStand sequence file or a custom sequence file TestStand can load with a custom sequence file translator. Remarks Use this property to determine whether you can load the file using the Engine.GetSequence

### FileInformation.IsSequenceFile

#### Syntax

[FileInformation](fileinformation.html).IsSequenceFile

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the file is a TestStand sequence file or a custom sequence file TestStand can load with a custom sequence file translator.

#### Remarks

Use this property to determine whether you can load the file using the
 [Engine.GetSequenceFileEx](engine-getsequencefileex.html)
 method.

This property throws an exception if TestStand cannot locate the file when it is first accessed. Use the
 [FileExists](fileinformation-fileexists.html)
 property to determine whether the file is available.

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[FileInformation.FileExists](fileinformation-fileexists.html)

[FileInformation.IsCustomFile](fileinformation-iscustomfile.html)

[FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation-propertyobjectfiletype.html language=enus -->
## TOPIC 01170: FileInformation.PropertyObjectFileType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation-propertyobjectfiletype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation-propertyobjectfiletype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax FileInformation.PropertyObjectFileType Data Type PropertyObjectFileTypes Use the following constants with this data type: FileType_AdaptersConfigFile –(Value: 11) An adapters configuration file. FileType_ConfigFile –(Value: 0) The Engine.ConfigFile file. FileType_CustomConfigFile –(Value: 13)

### FileInformation.PropertyObjectFileType

#### Syntax

[FileInformation](fileinformation.html).PropertyObjectFileType

#### Data Type

[PropertyObjectFileTypes](propertyobjectfiletypes.html)

Use the following constants with this data type:

- FileType_AdaptersConfigFile 
 –(Value: 11) An adapters configuration file.
- FileType_ConfigFile 
 –(Value: 0) The
 Engine.ConfigFile 
 file.
- FileType_CustomConfigFile 
 –(Value: 13) A custom configuration file.
- FileType_GeneralEngineConfigFile 
 –(Value: 9) A general engine configuration file.
- FileType_ProjectFile 
 –(Value: 6) A TestStand project file.
- FileType_PropertyObjectFile 
 –(Value: 7) A generic PropertyObjectFile.
- FileType_SearchDirectoriesConfigFile 
 –(Value: 10) A search directories configuration file.
- FileType_SequenceFile 
 –(Value: 1) A sequence file.
- FileType_StationGlobalsFile 
 –(Value: 3) The
 Engine.GlobalsFile 
 file.
- FileType_TemplatesFile 
 –(Value: 8) The
 Engine.GetTemplatesFile 
 file.
- FileType_TypePaletteFile 
 –(Value: 2) A type palette file.
- FileType_TypePalettesConfigFile 
 –(Value: 12) A type palettes configuration file.
- FileType_UsersFile 
 –(Value: 4) The
 Engine.UsersFile 
 file.
- FileType_WorkspaceFile 
 –(Value: 5) A
 WorkspaceFile 
 file.

#### Purpose

Returns the file type of the file.

#### Remarks

Use this property to determine the type of file to create before using the
 [PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)
 method.

This property returns an error if TestStand cannot locate the file when it is first accessed or if the file is not a
 [PropertyObjectFile](propertyobjectfile.html)
 . Use the
 [FileInformation.FileExists](fileinformation-fileexists.html)
 property to determine if the file is available and the
 [FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)
 property to determine if the file is a
 PropertyObjectFile
 .

#### See Also

[Engine.NewPropertyObjectFile](engine-newpropertyobjectfile.html)

[Engine.ReadPropertyObjectFile](engine-readpropertyobjectfile.html)

[FileInformation.FileExists](fileinformation-fileexists.html)

[FileInformation.IsPropertyObjectFile](fileinformation-ispropertyobjectfile.html)

[PropertyObjectFile](propertyobjectfile.html)

[PropertyObjectFile.ReadFile](propertyobjectfile-readfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileinformation.html language=enus -->
## TOPIC 01171: FileInformation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileinformation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileinformation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use FileInformation objects to obtain file information, such as file version, file format version, and file type, on files TestStand recognizes without fully loading the files into memory. When you call methods and properties on a FileInformation object, TestStand can cache the information. For chan

### FileInformation

Use FileInformation objects to obtain file information, such as file version, file format version, and file type, on files TestStand recognizes without fully loading the files into memory. When you call methods and properties on a FileInformation object, TestStand can cache the information. For changes made to a file on disk to be reflected in a FileInformation object, you must release the object and use the
 [Engine.GetFileInformation](engine-getfileinformation.html)
 method to obtain a new FileInformation object.

#### Properties

| FileExists (Read Only) |
| --- |
| FileWritingFormat (Read Only) |
| IsCustomFile (Read Only) |
| IsCVIDll (Read Only) |
| IsDotNetAssembly (Read Only) |
| IsPropertyObjectFile (Read Only) |
| IsSequenceFile (Read Only) |
| PropertyObjectFileType (Read Only) |

#### Methods

| GetFileFormatDisplayVersion |
| --- |
| GetFileFormatVersion |
| GetFileVersion |

#### See Also

[Engine.GetFileInformation](engine-getfileinformation.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/filemodificationindicatorpolicies.html language=enus -->
## TOPIC 01172: FileModificationIndicatorPolicies

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/filemodificationindicatorpolicies.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/filemodificationindicatorpolicies.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the constants with the StationOptions.FileModificationIndicatorPolicy property. FileModificationIndicatorPolicy_DefaultPolicy –(Value: 0x0) TestStand indicates that any file with modifications is modified. FileModificationIndicatorPolicy_ExcludeTestStandVersionUpgrade –(Value: 0x1) TestStand doe

### FileModificationIndicatorPolicies

Use the constants with the
 [StationOptions.FileModificationIndicatorPolicy](stationoptions-filemodificationindicatorpolic.html)
 property.

- FileModificationIndicatorPolicy_DefaultPolicy 
 –(Value: 0x0) TestStand indicates that any file with modifications is modified.
- FileModificationIndicatorPolicy_ExcludeTestStandVersionUpgrade 
 –(Value: 0x1) TestStand does not indicate that a file is modified if the only changes are from non-editable NI type upgrades, or file data format upgrades.

#### See Also

[StationOptions.FileModificationIndicatorPolicy](stationoptions-filemodificationindicatorpolic.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileopenmodes.html language=enus -->
## TOPIC 01173: FileOpenModes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileopenmodes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileopenmodes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify different methods of opening files. FileOpenMode_Append –(Value: 0x2) Append to the end of an existing file. FileOpenMode_NoOptions –(Value 0x0) No options. FileOpenMode_Truncate –(Value 0x1) Overwrite an existing file, deleting its contents. FileOpenMode_Uniquify –(Va

### FileOpenModes

Use these constants to specify different methods of opening files.

- FileOpenMode_Append 
 –(Value: 0x2) Append to the end of an existing file.
- FileOpenMode_NoOptions 
 –(Value 0x0) No options.
- FileOpenMode_Truncate 
 –(Value 0x1) Overwrite an existing file, deleting its contents.
- FileOpenMode_Uniquify 
 –(Value 0x4) Create a new file it does not exist. If the file already exists, attempt to make the file name unique. The algorithm for creating a unique filename depends on the specific function being invoked.

#### See Also

[CsvFileOutputRecordStream.Open](csvfileoutputrecordstream-open.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileopenstatusflags.html language=enus -->
## TOPIC 01174: FileOpenStatusFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileopenstatusflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileopenstatusflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the PropertyObjectFile.OpenStatus property. Generally, only user interfaces need to set this property. OpenStatus_InWindow –(Value: 0x1) Specifies that the file is open and displayed in a window. See Also PropertyObjectFile.OpenStatus

### FileOpenStatusFlags

Use these constants to specify the
 [PropertyObjectFile.OpenStatus](propertyobjectfile-openstatus.html)
 property. Generally, only user interfaces need to set this property.

- OpenStatus_InWindow 
 –(Value: 0x1) Specifies that the file is open and displayed in a window.

#### See Also

[PropertyObjectFile.OpenStatus](propertyobjectfile-openstatus.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/fileversionautoincrement.html language=enus -->
## TOPIC 01175: FileVersionAutoIncrement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/fileversionautoincrement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/fileversionautoincrement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the StationOptions.SeqFileVersionAutoIncrementOpt property to specify whether to automatically increment a component of the sequence file version when the file is saved. Versions have four components: Major, Minor, Revision and Build. TestStand displays versions using decima

### FileVersionAutoIncrement

Use these constants with the
 [StationOptions.SeqFileVersionAutoIncrementOpt](stationoptions-seqfileversionautoincrementopt.html)
 property to specify whether to automatically increment a component of the sequence file version when the file is saved. Versions have four components: Major, Minor, Revision and Build. TestStand displays versions using decimal points to separate the components, such as "1.2.3.4".

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

#### See Also

[StationOptions.SeqFileVersionAutoIncrementOpt](stationoptions-seqfileversionautoincrementopt.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/filewritingformats.html language=enus -->
## TOPIC 01176: FileWritingFormats

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/filewritingformats.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/filewritingformats.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the PropertyObjectFile.FileWritingFormat property, the StationOptions.DefaultFileWritingFormat property, and the return value to the FileInformation.GetFileFormatVersion method. FileWritingFormat_Binary –(Value: 2) Specifies that TestStand writes the file in a binary format.

### FileWritingFormats

Use these constants with the
 [PropertyObjectFile.FileWritingFormat](propertyobjectfile-filewritingformat.html)
 property, the
 [StationOptions.DefaultFileWritingFormat](stationoptions-defaultfilewritingformat.html)
 property, and the return value to the
 [FileInformation.GetFileFormatVersion](fileinformation-getfileformatversion.html)
 method.

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

#### See Also

[FileInformation.GetFileFormatVersion](fileinformation-getfileformatversion.html)

[PropertyObjectFile.FileWritingFormat](propertyobjectfile-filewritingformat.html)

[StationOptions.DefaultFileWritingFormat](stationoptions-defaultfilewritingformat.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/findfilepromptoptions.html language=enus -->
## TOPIC 01177: FindFilePromptOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/findfilepromptoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/findfilepromptoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the promptOption parameter of the Engine.FindFileEx method. The promptOption parameter specifies whether to prompt the user for a file location when TestStand cannot find the file in the search directory paths . FindFile_PromptDisable –(Value: 3) Do not prompt the user

### FindFilePromptOptions

Use these constants to specify the
 promptOption
 parameter of the
 [Engine.FindFileEx](engine-findfileex.html)
 method.

The
 promptOption
 parameter specifies whether to prompt the user for a file location when TestStand cannot find the file in the
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

- FindFile_PromptDisable 
 –(Value: 3) Do not prompt the user to locate the file.
- FindFile_PromptEnable 
 –(Value: 2) Prompt the user to locate the file.
- FindFile_PromptHonorUserPreference 
 –(Value: 1) Prompt the user to locate the file if the Prompt to Find Files option on the
 Preferences tab 
 of the
 Station Options 
 dialog box is enabled.

#### See Also

[Engine.FindFileEx](engine-findfileex.html)

[Preferences tab](../tsref/preferences-tab-station-options-dialog-box.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[StationOptions.PromptToFindFiles](stationoptions-prompttofindfiles.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/findfilesearchlistoptions.html language=enus -->
## TOPIC 01178: FindFileSearchListOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/findfilesearchlistoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/findfilesearchlistoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the srchListOption parameter of the Engine.FindFileEx method. The FindFile_AddDirSearchList constants specify whether TestStand adds the directory of the file you select to the search directory paths . It also changes the dimmed state of the Add Directory to Search Dir

### FindFileSearchListOptions

Use these constants to specify the
 srchListOption
 parameter of the
 [Engine.FindFileEx](engine-findfileex.html)
 method.

The
 FindFile_AddDirSearchList
 constants specify whether TestStand adds the directory of the file you select to the
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 . It also changes the dimmed state of the
 Add Directory to Search Directory List
 option.

- FindFile_AddDirToSrchList_Ask 
 –(Value: 1) Enables the Add Directory to Search Directory List option so you can choose whether to append the directory that contains the file to the list of search directories. If the current user does not have configured engine privileges, the
 Engine.FindFileEx 
 method behaves as if you passed
 FindFile_AddDirToSrchList_No 
 .
- FindFile_AddDirToSrchList_Ask_IgnorePrivileges 
 –(Value: 4) The same as
 FindFile_AddDirToSrchList_Ask 
 but does not check user privileges.
- FindFile_AddDirToSrchList_No 
 –(Value: 2) Does not add the directory to the search path and disables and dims the Add Directory to Search Directory List option.
- FindFile_AddDirToSrchList_Yes 
 –(Value: 3) Adds the directory to the search paths and dims the Add Directory to Search Directory List option. If the current user does not have configure engine privileges, the
 Engine.FindFileEx 
 method behaves as if you passed
 FindFile_AddDirToSrchList_No 
 .
- FindFile_AddDirToSrchList_Yes_IgnorePrivileges 
 –(Value: 5) The same as
 FindFile_AddDirToSrchList_Yes 
 but does not check user privileges.

#### See Also

[Engine.DisplaySearchDirDialog](engine-displaysearchdirdialog.html)

[Engine.FindFileEx](engine-findfileex.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/findpathstatusvalues.html language=enus -->
## TOPIC 01179: FindPathStatusValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/findpathstatusvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/findpathstatusvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Engine.FindPath method returns one of these constants to indicate the results of the path search. FindPath_PathIsDir –(Value: 2) The FindPath method returned the path of a directory. FindPath_PathIsFile –(Value: 1) The FindPath method returned the path of a file. FindPath_PathNotFound –(Value: 3

### FindPathStatusValues

The
 [Engine.FindPath](engine-findpath.html)
 method returns one of these constants to indicate the results of the path search.

- FindPath_PathIsDir 
 –(Value: 2) The FindPath method returned the path of a directory.
- FindPath_PathIsFile 
 –(Value: 1) The FindPath method returned the path of a file.
- FindPath_PathNotFound 
 –(Value: 3) The FindPath method failed to locate a directory or file with the name you specified.
- FindPath_PathNotValid 
 –(Value: 4) The pathname you passed to the FindPath method is not valid.

#### See Also

[Engine.DisplaySearchDirDialog](engine-displaysearchdirdialog.html)

[Engine.FindPath](engine-findpath.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/flexcstepadditions.html language=enus -->
## TOPIC 01180: FlexCStepAdditions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/flexcstepadditions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/flexcstepadditions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Do not use these constants to access the adapter-specific properties of a step. Use the DllModule interface for the Module object for the step. Use the Step.Module property to acquire a reference to a Module object. In TestStand 3.0 or later, these string constants are obsolete. These string constan

### FlexCStepAdditions

Note

DllModule

Step.Module

In TestStand 3.0 or later, these string constants are obsolete.

These string constants were previously used to create
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 to access the C/C++ DLL Adapter-specific properties of a step. Notice that the
 FlexCStep_ExternalCallProp
 constant refers to the property that contains the properties which have constants that begin with the
 ExternalCall_
 prefix. The
 ExternalCall_ParametersProp
 constant represents the property that contains an array of objects that describe the return value and parameters for the function. Constants that have names that begin with
 FCParam_
 apply to the return value and each parameter.

- ExternalCall_CallConvProp 
 –(Value: "Conv") This constant is obsolete.
- ExternalCall_FunctionNameProp 
 –(Value: "Func") This constant is obsolete.
- ExternalCall_LibPathProp 
 –(Value: "LibPath") This constant is obsolete.
- ExternalCall_ParametersProp 
 –(Value: "Params") This constant is obsolete.
- FCParam_ArgValueProp 
 –(Value: "ArgVal") This constant is obsolete.
- FCParam_ArrayElemPassingProp 
 –(Value: "ElemPass") This constant is obsolete.
- FCParam_FlagsProp 
 –(Value: "Flags") This constant is obsolete.
- FCParam_NameProp 
 –(Value: "Name") This constant is obsolete.
- FCParam_NumArrayElementsProp 
 –(Value: "NumEls") This constant is obsolete.
- FCParam_NumericPassingProp 
 –(Value: "NumPass") This constant is obsolete.
- FCParam_NumericTypeProp 
 –(Value: "NumType") This constant is obsolete.
- FCParam_ObjectTypeProp 
 –(Value: "ObjType") This constant is obsolete.
- FCParam_ResultActionProp 
 –(Value: "ResultAct") This constant is obsolete.
- FCParam_StringPassingProp 
 –(Value: "StrPass") This constant is obsolete.
- FCParam_StringSizeProp 
 –(Value: "StrSize") This constant is obsolete.
- FCParam_TypeProp 
 –(Value: "Type") This constant is obsolete.
- FlexCStep_ExternalCallProp 
 –(Value: "Call") This constant is obsolete.

#### See Also

[DllModule](dllmodule.html)

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[Step.Module](step-module.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/font.html language=enus -->
## TOPIC 01181: Font

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/font.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/font.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Font object specifies a wrapper around a Microsoft Windows font. Microsoft defines this standard Font object implementation in the Object Linking and Embedding (OLE) Automation version 2.0 type library file, stdole2.tlb . Refer to Microsoft documentation for more information about this interface.

### Font

A Font object specifies a wrapper around a Microsoft Windows font. Microsoft defines this standard Font object implementation in the Object Linking and Embedding (OLE) Automation version 2.0 type library file,
 stdole2.tlb
 . Refer to Microsoft documentation for more information about this interface.

The Font interface specifies the following properties and methods:

#### Properties

- Name 
 —Name for the font.
- Size 
 —Point size for the font.
- Bold 
 —Bold property for the font.
- Italic 
 —Italic property for the font.
- Underline 
 —Underline property for the font.
- Strikethrough 
 —Strikethrough property for the font.
- Weight 
 —Weight (bold) for the font.
- Charset 
 —Character set of the font.
- hFont 
 —Returns a Windows HFONT handle for the font this Font object describes.

#### Methods

- Clone 
 —Creates a duplicate Font object with a state identical to the current font.
- IsEqual 
 —Compares this Font object to another for equality.
- SetRatio 
 —Converts the scaling factor for this font between logical units and HIMETRIC units, which the point size in the Size property specifies.
- QueryTextMetrics 
 —Fills a TEXTMETRIC structure describing the font.
- AddRefHfont 
 —Notifies the Font object that the previously realized font hFont identified remains valid until the ReleaseHfont method is called or the Font object itself is released.
- ReleaseHfont 
 —Notifies the Font object that the caller that previously locked this font in the cache with AddRefHfont no longer requires the lock.
- SetHdc 
 —Provides a device context handle to the font that describes the logical mapping mode.

LabVIEW

The LabVIEW development environment automatically recognizes Font ActiveX references. Use the Invoke Node and Property Node VIs to access the methods and properties of a Font ActiveX reference.

Note

LabWindows/CVI

LabWindows/CVI creates and accesses ActiveX objects using functions in a LabWindows/CVI-generated driver. You must create a driver for the OLE Automation ActiveX server using the ActiveX Controller Wizard. Select
 Tools»Create ActiveX Controller
 to launch the wizard. Select
 OLE Automation
 in the ActiveX Server list control and proceed to build the driver. Use the functions for the Font class to access the methods and properties.

Microsoft Visual Basic .NET

In Microsoft Visual Basic .NET, you can access Font objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

Imports stdole.StdFontClass

The IFontDisp class methods and properties are available in the Microsoft Visual Studio object browser and are accessible from the Visual Basic .NET source code.

C#

In C#, you can access Font objects by first adding the OLE Automation COM component as a reference in a project and then adding the following directive at the top of the source file:

using stdole.StdFontClass;

The IFontDisp class methods and properties are available in the Visual Studio object browser and are accessible from the C# source code.

Microsoft Visual C++/#import

In C++, you can access Font objects by adding the include file
 ocidl.h
 and using the CComPtr template to manage IFontDisp COM interface pointers.

Parent topic:

Data Types for TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/frontendcallbacks.html language=enus -->
## TOPIC 01182: FrontEndCallbacks

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/frontendcallbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/frontendcallbacks.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This constant represents the name of a Front-End callback sequence. Use this constant to specify the sequenceName parameter of the Engine.CallFrontEndCallbackEx method. FrontEndCback_LoginLogout –(Value: "LoginLogout") Specifies the callback used to log in and log out the current user. See Also Defa

### FrontEndCallbacks

This constant represents the name of a Front-End callback sequence. Use this constant to specify the
 sequenceName
 parameter of the
 [Engine.CallFrontEndCallbackEx](engine-callfrontendcallbackex.html)
 method.

- FrontEndCback_LoginLogout 
 –(Value: "LoginLogout") Specifies the callback used to log in and log out the current user.

#### See Also

[DefaultModelCallbacks](defaultmodelcallbacks.html)

[Engine.CallFrontEndCallbackEx](engine-callfrontendcallbackex.html)

[SeqFileCallbacks](seqfilecallbacks.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/getmodulefromprojectoptions.html language=enus -->
## TOPIC 01183: GetModuleFromProjectOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/getmodulefromprojectoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/getmodulefromprojectoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: GetModuleFromProjectOption_NoOptions –(Value: 0) GetModuleFromProjectOption_NoPrompts –(Value: 1)

### GetModuleFromProjectOptions

- GetModuleFromProjectOption_NoOptions 
 –(Value: 0)
- GetModuleFromProjectOption_NoPrompts 
 –(Value: 1)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/getseqfileoptions.html language=enus -->
## TOPIC 01184: GetSeqFileOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/getseqfileoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/getseqfileoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the getSeqFileFlags parameter of the Engine.GetSequenceFileEx method. Use the bitwise-OR operator to specify more than one option. GetSeqFile_AllowTypeConflicts –(Value: 0x4) If this flag is set, conflicts TestStand encounters between the sequen

### GetSeqFileOptions

These constants represent the options you can use with the
 getSeqFileFlags
 parameter of the
 [Engine.GetSequenceFileEx](engine-getsequencefileex.html)
 method. Use the bitwise-OR operator to specify more than one option.

- GetSeqFile_AllowTypeConflicts 
 –(Value: 0x4) If this flag is set, conflicts TestStand encounters between the sequence and types currently in memory do not prevent TestStand from loading the sequence. If this flag is not set, TestStand returns an error as soon as it encounters a type conflict.
 Note 
 The
 [Engine.GetSequenceFileEx](engine-getsequencefileex.html)
 method ignores this value.
- GetSeqFile_CheckModelOptions 
 –(Value: 0x8) If this flag is set, TestStand verifies that the sequence file does not refer to a specific process model file that conflicts with the current settings on the
 Model tab 
 of the
 Station Options 
 dialog box.
- GetSeqFile_DoNotRunLoadCallback 
 –(Value: 0x10) If this flag is set, TestStand does not run the SequenceFileLoad callback sequence. Even if you use this option, TestStand executes the SequenceFileLoad callback for subsequent calls to the
 Engine.GetSequenceFileEx 
 method that do not use this option. TestStand does not execute the SequenceFileUnload callback when you release the sequence file with the
 Engine.ReleaseSequenceFileEx 
 method if all calls to obtain the sequence file use this option.
- GetSeqFile_FindFile 
 –(Value: 0x20) If this flag is set, TestStand attempts to find a relative pathname using the
 Engine.FindFileEx 
 method.
- GetSeqFile_GetFileOnlyIfInCache 
 –(Value: 0x200) If this flag is set, the
 Engine.GetSequenceFileEx 
 method returns a sequence file only if the file is already in the engine internal cache. If the file is not in the cache, the
 Engine.GetSequenceFileEx 
 method returns a NULL reference.
- GetSeqFile_NoOptions 
 –(Value: 0x0) No options.
- GetSeqFile_OperatorInterfaceFlags 
 –(Value: 0x6B) The standard set of flags a user interface uses. This is the combination of the
 GetSeqFile_CheckModelOptions 
 ,
 GetSeqFile_PreloadModules 
 ,
 GetSeqFile_FindFile 
 ,
 GetSeqFile_SearchCurrentDir 
 , and
 GetSeqFile_UpdateFromDisk 
 flags.
- GetSeqFile_PreloadModules 
 –(Value: 0x1) If this flag is set, TestStand honors the Module Load options for the sequence and launches the preload progress dialog box when opening the file. Otherwise, it does not preload any of the modules the steps in the sequence use or display the preload progress dialog box.
- GetSeqFile_SearchCurrentDir 
 –(Value: 0x40) If this flag is set, TestStand attempts to find a relative pathname by searching the current directory first.
- GetSeqFile_UpdateFromDisk 
 –(Value: 0x2) If this flag is set and the sequence is currently in memory, TestStand checks the date of the file on disk and reloads it if it is newer. If the flag is not set and the sequence is currently in memory, TestStand does not load the file.

#### See Also

[Engine.FindFileEx](engine-findfileex.html)

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[Model tab](../tsref/model-tab-station-options-dialog-box.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/gettemplatesfileoptions.html language=enus -->
## TOPIC 01185: GetTemplatesFileOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/gettemplatesfileoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/gettemplatesfileoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these options to specify whether the Engine.GetTemplatesFile method creates the templates file if the templates file does not exist. GetTemplatesFileOption_LoadIfNotLoaded –(Value: 0x1) Specifies that the engine loads the templates file if it has not been loaded. If no templates file exists, the

### GetTemplatesFileOptions

Use these options to specify whether the
 [Engine.GetTemplatesFile](engine-gettemplatesfile.html)
 method creates the templates file if the templates file does not exist.

- GetTemplatesFileOption_LoadIfNotLoaded 
 –(Value: 0x1) Specifies that the engine loads the templates file if it has not been loaded. If no templates file exists, the engine creates a default templates file. Omit this option to determine whether a templates file has been previously loaded. When you omit this option, the
 Engine.GetTemplatesFile 
 method returns
 NULL 
 if no templates file is loaded.
- GetTemplatesFileOption_NoOptions 
 –(Value: 0x0) Specifies that the
 Engine.GetTemplatesFile 
 method returns a value of
 NULL 
 for
 PropertyObjectFile 
 if the templates file does not exist.

#### See Also

[Engine.GetTemplatesFile](engine-gettemplatesfile.html)

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/getupdatedstatusoptions.html language=enus -->
## TOPIC 01186: GetUpdatedStatusOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/getupdatedstatusoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/getupdatedstatusoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the values you can use with the changedProperties parameter of the LabVIEWNXGModule.HavePropertiesChanged method. Use these constants with the bitwise-OR operator on the value returned in the changedProperties parameter to determine what has changed in module. If the bitwis

### GetUpdatedStatusOptions

These constants represent the values you can use with the
 changedProperties
 parameter of the
 LabVIEWNXGModule.HavePropertiesChanged
 method. Use these constants with the
 bitwise-OR
 operator on the value returned in the
 changedProperties
 parameter to determine what has changed in module. If the
 bitwise-OR
 returns
 true
 , then that property or value has changed in the module.

- GetUpdatedStatusOption_ExpectedGLLPathChanged 
 –(Value: 0x8) The GLL specified by the GLL Path property does not match the GLL output path of the component selected in the Module Qualified Name. The GLL specified in the step should exactly match the GLL output determined by the project, target and component selected in the step, if any. A mismatch could mean that two different GVIs are being run when the module is executed in the LabVIEW NXG Development System vs when the module is executed in the Runtime Engine.
- GetUpdatedStatusOption_GVIChecksumChanged 
 –(Value: 0x2) The checksum of the GVI has changed. This indicates that the parameters or namespace of the GVI has changed from when the step was last configured.
- GetUpdatedStatusOption_GVIDescriptionChanged 
 –(Value: 0x1) The GVI description has changed.
- GetUpdatedStatusOption_GVIStateChanged 
 –(Value: 0x4) The GVI is broken or not in a runnable state.
- GetUpdatedStatusOption_None 
 –(Value: 0x0) None of the validations specified by the
 options 
 parameter in
 LabVIEWNXgModule.HavePropertiesChanged 
 failed.
- GetUpdatedStatusOption_QualifiedNamePresentInGLL 
 –(Value: 0x10) The GVI selected in the Module Name property is absent in the GLL specified in the step.

#### See Also

[LabVIEWNXGModule.HavePropertiesChanged](labviewnxgmodule-havepropertieschanged.html)

[CheckUpdatedStatusOptions](checkupdatedstatusoptions.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/gotolocationoptions.html language=enus -->
## TOPIC 01187: GotoLocationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/gotolocationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/gotolocationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the Locations.GotoLocation method. GotoLocationOption_DoNotDisplayMessageIfLocationNotFound –(Value: 0x1) Use this option to specify that the Locations.GotoLocation method takes no action instead of launching an information dialog box when the user interface cannot go to the

### GotoLocationOptions

Use these constants with the
 [Locations.GotoLocation](locations-gotolocation.html)
 method.

- GotoLocationOption_DoNotDisplayMessageIfLocationNotFound 
 –(Value: 0x1) Use this option to specify that the
 Locations.GotoLocation 
 method takes no action instead of launching an information dialog box when the user interface cannot go to the location.
- GotoLocationOption_NoOptions 
 –(Value: 0x0) No options.

#### See Also

[Locations.GotoLocation](locations-gotolocation.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/hierarchicalexecutionflags.html language=enus -->
## TOPIC 01188: HierarchicalExecutionFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/hierarchicalexecutionflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/hierarchicalexecutionflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the hierarchicalExecutionFlags parameter of the Engine.NewHierarchicalExecution method. HierarchicalExecMask_DontRunSetupAndCleanup –(Value: 0x2) Specifies that a hierarchical execution does not run setup or Cleanup steps when it generates a call stack. This flag appli

### HierarchicalExecutionFlags

Use these constants to specify the
 hierarchicalExecutionFlags
 parameter of the
 [Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)
 method.

- HierarchicalExecMask_DontRunSetupAndCleanup 
 –(Value: 0x2) Specifies that a hierarchical execution does not run setup or Cleanup steps when it generates a call stack. This flag applies to the sequences that contain the Sequence Call steps you pass to the
 sequenceCallSteps 
 parameter of the
 Engine.NewHierarchicalExecution 
 method.
- HierarchicalExecMask_IgnorePreconditions 
 –(Value: 0x8): Specifies that when
 Engine.NewHierarchicalExecution 
 creates the call stack the arguments specify, it does not check the preconditions of the Sequence Call steps that comprise the call stack.
- HierarchicalExecMask_RunRemainingSequence 
 –(Value: 0x4) Specifies that the execution continues normally when the call stack unwinds. When the Sequence Call steps return from the call stack the execution generates, the remaining steps execute normally in the sequences that contain the calls.

#### See Also

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicadapter-asadapter.html language=enus -->
## TOPIC 01189: HTBasicAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicadapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicadapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicAdapter.AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter object that represents the HTBasicAdapter object. Remarks Use the adapter to access properties and methods common to all adapters. See Also Adapter

### HTBasicAdapter.AsAdapter

#### Syntax

[HTBasicAdapter](htbasicadapter.html).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter object that represents the HTBasicAdapter object.

#### Remarks

Use the adapter to access properties and methods common to all adapters.

#### See Also

[Adapter](adapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicadapter-defaultworkingdirectory.html language=enus -->
## TOPIC 01190: HTBasicAdapter.DefaultWorkingDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicadapter-defaultworkingdirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicadapter-defaultworkingdirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicAdapter.DefaultWorkingDirectory Data Type HTBasicDefaultWorkingDirTypes Use the following constants with this data type: HTBasicDefaultWorkingDir_DoNotChange –(Value: 1) Do not change the working directory before calling the module. HTBasicDefaultWorkingDir_HTBasicServer –(Value: 2) Se

### HTBasicAdapter.DefaultWorkingDirectory

#### Syntax

[HTBasicAdapter](htbasicadapter.html).DefaultWorkingDirectory

#### Data Type

[HTBasicDefaultWorkingDirTypes](htbasicdefaultworkingdirtypes.html)

Use the following constants with this data type:

- HTBasicDefaultWorkingDir_DoNotChange 
 –(Value: 1) Do not change the working directory before calling the module.
- HTBasicDefaultWorkingDir_HTBasicServer 
 –(Value: 2) Set the current working directory to the location of the HTBasic server before calling the module.
- HTBasicDefaultWorkingDir_Specific 
 –(Value: 4) Set the current working directory to the location the
 HTBasicAdapter.SpecWorkingDirectoryPath 
 property defines.
- HTBasicDefaultWorkingDir_SubroutineFile 
 –(Value: 3) Set the current working directory to the location of the subroutine before calling the module.

#### Purpose

Specifies whether the HTBasic Adapter sets the working directory prior to invoking a subroutine. This setting applies only to HTBasic steps when you set the Working Directory option of the step to
 Use Adapter Default
 .

#### Remarks

The default value is the subroutine file directory.

#### See Also

[HTBasicAdapter.DevelopmentServerPath](htbasicadapter-developmentserverpath.html)

[HTBasicAdapter.RunTimeServerPath](htbasicadapter-runtimeserverpath.html)

[HTBasicAdapter.SpecWorkingDirectoryPath](htbasicadapter-specworkingdirectorypath.html)

[HTBasicModule.WorkingDirectory](htbasicmodule-workingdirectory.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicadapter-developmentserverpath.html language=enus -->
## TOPIC 01191: HTBasicAdapter.DevelopmentServerPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicadapter-developmentserverpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicadapter-developmentserverpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicAdapter.DevelopmentServerPath Data Type String Purpose Specifies the location of the development version of the HTBasic server. Remarks The specified location must be a valid path. See Also HTBasicAdapter.RunTimeServerPath HTBasicAdapter.UseDevelopmentServer

### HTBasicAdapter.DevelopmentServerPath

#### Syntax

[HTBasicAdapter](htbasicadapter.html).DevelopmentServerPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the location of the development version of the HTBasic server.

#### Remarks

The specified location must be a valid path.

#### See Also

[HTBasicAdapter.RunTimeServerPath](htbasicadapter-runtimeserverpath.html)

[HTBasicAdapter.UseDevelopmentServer](htbasicadapter-usedevelopmentserver.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicadapter-runtimeserverpath.html language=enus -->
## TOPIC 01192: HTBasicAdapter.RunTimeServerPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicadapter-runtimeserverpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicadapter-runtimeserverpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicAdapter.RunTimeServerPath Data Type String Purpose Specifies the location of the run-time version of the HTBasic server. Remarks The specified location must be a valid path. See Also HTBasicAdapter.DevelopmentServerPath HTBasicAdapter.UseDevelopmentServer

### HTBasicAdapter.RunTimeServerPath

#### Syntax

[HTBasicAdapter](htbasicadapter.html).RunTimeServerPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the location of the run-time version of the HTBasic server.

#### Remarks

The specified location must be a valid path.

#### See Also

[HTBasicAdapter.DevelopmentServerPath](htbasicadapter-developmentserverpath.html)

[HTBasicAdapter.UseDevelopmentServer](htbasicadapter-usedevelopmentserver.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicadapter-specworkingdirectorypath.html language=enus -->
## TOPIC 01193: HTBasicAdapter.SpecWorkingDirectoryPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicadapter-specworkingdirectorypath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicadapter-specworkingdirectorypath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicAdapter.SpecWorkingDirectoryPath Data Type String Purpose Specifies the working directory used for the HTBasic Adapter. The specified working directory must be a valid path. Remarks This path is only used when you select Use Specified Directory as the Default Working Directory option.

### HTBasicAdapter.SpecWorkingDirectoryPath

#### Syntax

[HTBasicAdapter](htbasicadapter.html).SpecWorkingDirectoryPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the working directory used for the HTBasic Adapter. The specified working directory must be a valid path.

#### Remarks

This path is only used when you select
 Use Specified Directory
 as the Default Working Directory option.

#### See Also

[HTBasicAdapter.DefaultWorkingDirectory](htbasicadapter-defaultworkingdirectory.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicadapter-usedevelopmentserver.html language=enus -->
## TOPIC 01194: HTBasicAdapter.UseDevelopmentServer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicadapter-usedevelopmentserver.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicadapter-usedevelopmentserver.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicAdapter.UseDevelopmentServer Data Type Boolean Purpose Specifies whether the HTBasic Adapter uses the development or run-time version of the HTBasic server. Remarks If this property is True , the adapter uses the development version. Otherwise, the adapter uses the run-time version. Se

### HTBasicAdapter.UseDevelopmentServer

#### Syntax

[HTBasicAdapter](htbasicadapter.html).UseDevelopmentServer

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether the HTBasic Adapter uses the development or run-time version of the HTBasic server.

#### Remarks

If this property is
 True
 , the adapter uses the development version. Otherwise, the adapter uses the run-time version.

#### See Also

[HTBasicAdapter.DevelopmentServerPath](htbasicadapter-developmentserverpath.html)

[HTBasicAdapter.RunTimeServerPath](htbasicadapter-runtimeserverpath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicadapter.html language=enus -->
## TOPIC 01195: HTBasicAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the HTBasicAdapter class to configure and obtain HTBasic Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use

### HTBasicAdapter

Use objects from the HTBasicAdapter class to configure and obtain HTBasic Adapter-specific information about the module adapter. Call the
 
 [Engine.GetAdapter](engine-getadapter.html)
 or
 
 [Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)
 method to obtain a reference to the adapter object.

To access the properties and methods of the Adapter class, use the
 [HTBasicAdapter.AsAdapter](htbasicadapter-asadapter.html)
 method to obtain an object.

#### Properties

| DefaultWorkingDirectory |
| --- |
| DevelopmentServerPath |
| RunTimeServerPath |
| SpecWorkingDirectoryPath |
| UseDevelopmentServer |

#### Method

| AsAdapter |
| --- |

#### See Also

[Adapter](adapter.html)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicdefaultworkingdirtypes.html language=enus -->
## TOPIC 01196: HTBasicDefaultWorkingDirTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicdefaultworkingdirtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicdefaultworkingdirtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the HTBasicAdapter.DefaultWorkingDirectory property. HTBasicDefaultWorkingDir_DoNotChange –(Value: 1) Do not change the working directory before calling the module. HTBasicDefaultWorkingDir_HTBasicServer –(Value: 2) Set the current working directory to the location of the HT

### HTBasicDefaultWorkingDirTypes

Use these constants with the
 [HTBasicAdapter.DefaultWorkingDirectory](htbasicadapter-defaultworkingdirectory.html)
 property.

- HTBasicDefaultWorkingDir_DoNotChange 
 –(Value: 1) Do not change the working directory before calling the module.
- HTBasicDefaultWorkingDir_HTBasicServer 
 –(Value: 2) Set the current working directory to the location of the HTBasic server before calling the module.
- HTBasicDefaultWorkingDir_Specific 
 –(Value: 4) Set the current working directory to the location the
 HTBasicAdapter.SpecWorkingDirectoryPath 
 property defines.
- HTBasicDefaultWorkingDir_SubroutineFile 
 –(Value: 3) Set the current working directory to the location of the subroutine before calling the module.

#### See Also

[HTBasicAdapter.DefaultWorkingDirectory](htbasicadapter-defaultworkingdirectory.html)

[HTBasicAdapter.SpecWorkingDirectoryPath](htbasicadapter-specworkingdirectorypath.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicmodule-asmodule.html language=enus -->
## TOPIC 01197: HTBasicModule.AsModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicmodule-asmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicmodule-asmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicModule.AsModule Return Value Module Purpose Returns the underlying module that represents the HTBasicModule object. Remarks Use the module to access properties and methods that are common to all modules. See Also Module

### HTBasicModule.AsModule

#### Syntax

[HTBasicModule](htbasicmodule.html).AsModule

#### Return Value

[Module](module.html)

#### Purpose

Returns the underlying module that represents the HTBasicModule object.

#### Remarks

Use the module to access properties and methods that are common to all modules.

#### See Also

[Module](module.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicmodule-showhtbasicapp.html language=enus -->
## TOPIC 01198: HTBasicModule.ShowHTBasicApp

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicmodule-showhtbasicapp.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicmodule-showhtbasicapp.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicModule.ShowHTBasicApp Data Type Boolean Purpose Specifies if the HTBasic Adapter activates the HTBasic application when it executes a step that calls a HTBasic subroutine.

### HTBasicModule.ShowHTBasicApp

#### Syntax

[HTBasicModule](htbasicmodule.html).ShowHTBasicApp

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the HTBasic Adapter activates the HTBasic application when it executes a step that calls a HTBasic subroutine.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicmodule-subroutinefilepath.html language=enus -->
## TOPIC 01199: HTBasicModule.SubroutineFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicmodule-subroutinefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicmodule-subroutinefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicModule.SubroutineFilePath Data Type String Purpose Specifies the pathname of the code module file that contains the subroutine the step calls. You can specify an absolute or relative pathname for the module file. Relative pathnames are relative to the TestStand search directory paths .

### HTBasicModule.SubroutineFilePath

#### Syntax

[HTBasicModule](htbasicmodule.html).SubroutineFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the code module file that contains the subroutine the step calls. You can specify an absolute or relative pathname for the module file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[HTBasicModule.SubroutineName](htbasicmodule-subroutinename.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicmodule-subroutinename.html language=enus -->
## TOPIC 01200: HTBasicModule.SubroutineName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicmodule-subroutinename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicmodule-subroutinename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicModule.SubroutineName Data Type String The subroutine name. Purpose Specifies the name of the subroutine the step calls. See Also HTBasicModule.SubroutineFilePath

### HTBasicModule.SubroutineName

#### Syntax

[HTBasicModule](htbasicmodule.html).SubroutineName

#### Data Type

[String](data-types-for-teststand.html)

The subroutine name.

#### Purpose

Specifies the name of the subroutine the step calls.

#### See Also

[HTBasicModule.SubroutineFilePath](htbasicmodule-subroutinefilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicmodule-workingdirectory.html language=enus -->
## TOPIC 01201: HTBasicModule.WorkingDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicmodule-workingdirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicmodule-workingdirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicModule.WorkingDirectory Data Type HTBasicWorkingDirTypes Use the following constants with this data type: HTBasicWorkingDir_AdapterDefault –(Value: 0) Use the setting specified for the HTBasic Adapter. HTBasicWorkingDir_DoNotChange –(Value: 1) Do not change the working directory for th

### HTBasicModule.WorkingDirectory

#### Syntax

[HTBasicModule](htbasicmodule.html).WorkingDirectory

#### Data Type

[HTBasicWorkingDirTypes](htbasicworkingdirtypes.html)

Use the following constants with this data type:

- HTBasicWorkingDir_AdapterDefault 
 –(Value: 0) Use the setting specified for the HTBasic Adapter.
- HTBasicWorkingDir_DoNotChange 
 –(Value: 1) Do not change the working directory for the HTBasic server.
- HTBasicWorkingDir_HTBasicServer 
 –(Value: 2) Use the directory in which the HTBasic server is located.
- HTBasicWorkingDir_Specify 
 –(Value: 4) Use the directory specified in the
 HTBasicModule.WorkingDirectorySpecifiedPath 
 property.
- HTBasicWorkingDir_SubroutineFileDir 
 –(Value: 3) Use the directory in which the subroutine file is located.

#### Purpose

Specifies whether the adapter sets the working directory of the HTBasic server before invoking the subroutine of the module.

#### Remarks

Set this property if the test code assumes a particular
 [working directory path](htbasicworkingdirtypes.html)
 . The default value of this property is
 HTBasicWorkingDir_AdapterDefault
 . If this property has the value
 HTBasicWorkingDir_Specify
 , ensure the
 HTBasicModule.WorkingDirectorySpecifiedPath
 property contains a path that specifies the desired working directory.

#### See Also

[HTBasicModule.WorkingDirectorySpecifiedPath](htbasicmodule-workingdirectoryspecifiedpath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicmodule-workingdirectoryspecifiedpath.html language=enus -->
## TOPIC 01202: HTBasicModule.WorkingDirectorySpecifiedPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicmodule-workingdirectoryspecifiedpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicmodule-workingdirectoryspecifiedpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax HTBasicModule.WorkingDirectorySpecifiedPath Data Type String The desired working directory. Purpose Specifies a working directory to set for the HTBasic server before invoking the subroutine of the module. Remarks The module ignores this property unless the value of HTBasicModule.WorkingDirec

### HTBasicModule.WorkingDirectorySpecifiedPath

#### Syntax

[HTBasicModule](htbasicmodule.html).WorkingDirectorySpecifiedPath

#### Data Type

[String](data-types-for-teststand.html)

The desired working directory.

#### Purpose

Specifies a working directory to set for the HTBasic server before invoking the subroutine of the module.

#### Remarks

The module ignores this property unless the value of
 [HTBasicModule.WorkingDirectory](htbasicmodule-workingdirectory.html)
 is
 HTBasicWorkingDir_Specify
 .

#### See Also

[HTBasicModule.WorkingDirectory](htbasicmodule-workingdirectory.html)

[HTBasicWorkingDirTypes](htbasicworkingdirtypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicmodule.html language=enus -->
## TOPIC 01203: HTBasicModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the HTBasicModule class to specify and obtain HTBasic Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to an HTBasicModule object. To access the properties and methods of a specific module

### HTBasicModule

Use objects from the HTBasicModule class to specify and obtain HTBasic Adapter-specific information about the code module that steps or step type substeps execute. Use the
 
 [Step.Module](step-module.html)
 property to obtain a reference to an HTBasicModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the Module class, use the
 [HTBasicModule.AsModule](htbasicmodule-asmodule.html)
 method to obtain an object.

#### Properties

| ShowHTBasicApp |
| --- |
| SubroutineFilePath |
| SubroutineName |
| WorkingDirectory |
| WorkingDirectorySpecifiedPath |

#### Method

| AsModule |
| --- |

#### See Also

[Module](module.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicstepadditions.html language=enus -->
## TOPIC 01204: HTBasicStepAdditions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicstepadditions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicstepadditions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Do not use the following constants to access the adapter-specific properties of a step. Use the HTBasicModule interface for the Module object for the step. Use the Step.Module property to acquire a reference to a Module object. In TestStand 3.0 or later, these string constants are obsolete. These st

### HTBasicStepAdditions

Note

HTBasicModule

Step.Module

In TestStand 3.0 or later, these string constants are obsolete.

These string constants were previously used to create
 [lookup strings](/csh?context=ts_tsapiref_api_lookupstring)
 to access the adapter-specific properties of an HTBasic step.

- HTBasicStep_FunctionNameProp 
 –(Value: "SubName") String that contains the name of the HTBasic subroutine to call.
- HTBasicStep_ModulePathProp 
 –(Value: "ModulePath") String that contains the pathname of the module that contains the HTBasic subroutine to call.
- HTBasicStep_SetWorkingDirProp 
 –(Value: "SetWorkingDirType") Number property that specifies how to set the working directory when calling the subroutine.
 0
 Use adapter default
 1
 Do not set working directory
 2
 Set to HTBasic server directory
 3
 Set to subroutine file directory
 4
 Use specific directory stored in
 HTBasicStep_WorkingDirPathProp
- HTBasicStep_ShowAppProp 
 –(Value: "ShowApp") Boolean property that determines whether the adapter displays the HTBasic application when calling the subroutine.
- HTBasicStep_WorkingDirPathProp 
 –(Value "WorkingDirPath") String that contains the specific working directory the adapter sets when calling the subroutine. This is used only if
 HTBasicStep_SetWorkingDirProp 
 is set to the specific value.

#### See Also

[Lookup Strings](/csh?context=ts_tsapiref_api_lookupstring)

[Step.Module](step-module.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/htbasicworkingdirtypes.html language=enus -->
## TOPIC 01205: HTBasicWorkingDirTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/htbasicworkingdirtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/htbasicworkingdirtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the HTBasicModule.WorkingDirectory property to specify the working directory for the HTBasic server before invoking the subroutine. Enable this option if the test code assumes a particular working directory path. HTBasicWorkingDir_AdapterDefault –(Value: 0) Use the setting s

### HTBasicWorkingDirTypes

Use these constants with the
 [HTBasicModule.WorkingDirectory](htbasicmodule-workingdirectory.html)
 property to specify the working directory for the HTBasic server before invoking the subroutine. Enable this option if the test code assumes a particular working directory path.

- HTBasicWorkingDir_AdapterDefault 
 –(Value: 0) Use the setting specified for the HTBasic Adapter.
- HTBasicWorkingDir_DoNotChange 
 –(Value: 1) Do not change the working directory for the HTBasic server.
- HTBasicWorkingDir_HTBasicServer 
 –(Value: 2) Use the directory in which the HTBasic server is located.
- HTBasicWorkingDir_Specify 
 –(Value: 4) Use the directory specified in the
 HTBasicModule.WorkingDirectorySpecifiedPath 
 property.
- HTBasicWorkingDir_SubroutineFileDir 
 –(Value: 3) Use the directory in which the subroutine file is located.

#### See Also

[HTBasicModule.WorkingDirectory](htbasicmodule-workingdirectory.html)

[HTBasicModule.WorkingDirectorySpecifiedPath](htbasicmodule-workingdirectoryspecifiedpath.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/images-count.html language=enus -->
## TOPIC 01206: Images.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/images-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/images-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Images.Count Data Type Long Purpose Returns the number of items in the collection.

### Images.Count

#### Syntax

[Images](images.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/images-findimage.html language=enus -->
## TOPIC 01207: Images.FindImage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/images-findimage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/images-findimage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Images.FindImage( iconName, desiredWidth, desiredHeight) Return Value Picture Purpose Searches the collection for an image with a specific name. Remarks Returns the image in a Picture object. This method errors if the image is not found. Parameters iconName As String [In] Specifies the name o

### Images.FindImage

#### Syntax

[Images](images.html).FindImage( iconName, desiredWidth, desiredHeight)

#### Return Value

[Picture](data-types-for-teststand.html)

#### Purpose

Searches the collection for an image with a specific name.

#### Remarks

Returns the image in a Picture object. This method errors if the image is not found.

#### Parameters

iconName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the image to find. Typically, the name includes the filename and file extension. Icon files are located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories.

desiredWidth
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the width, in pixels, of the image to return.

desiredHeight
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the height, in pixels, of the image to return.

#### See Also

[Adapter.IconName](adapter-iconname.html)

[ApplicationMgr.GetImageName](../tsuiref/applicationmgr-getimagename.html)

[ExecutionViewMgr.GetImageName](../tsuiref/executionviewmgr-getimagename.html)

[ListBarPageItem.IconName](../tsuiref/listbarpageitem-iconname.html)

[SequenceFileViewMgr.GetImageName](../tsuiref/sequencefileviewmgr-getimagename.html)

[StatusBarPane.IconName](../tsuiref/statusbarpane-iconname.html)

[Step.IconName](step-iconname.html)

[StepType.IconName](steptype-iconname.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/images-item.html language=enus -->
## TOPIC 01208: Images.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/images-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/images-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Images.Item( imageIndex) Data Type Picture Purpose Returns a reference to an item at the specified index in the collection. Parameters imageIndex As Long [In] Specifies a zero-based index.

### Images.Item

#### Syntax

[Images](images.html).Item( imageIndex)

#### Data Type

[Picture](data-types-for-teststand.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

imageIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/images.html language=enus -->
## TOPIC 01209: Images

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/images.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/images.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This collection class contains objects of the Picture data type. Use the Engine.Images property to acquire the collection object. The collection specifies the images TestStand loads from the <TestStand> \Components\Icons and <TestStand Public>\Components\Icons directories and images you add using th

### Images

This collection class contains objects of the
 [Picture](picture.html)
 data type. Use the
 [Engine.Images](engine-images.html)
 property to acquire the collection object. The collection specifies the images TestStand loads from the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories and images you add using the
 [Engine.AddImage](engine-addimage.html)
 method. Use the
 [Images.FindImage](images-findimage.html)
 method to find an image using an image name.

Use the
 Images
 collection as an alternative to using the
 [Engine.LargeImageListEx](engine-largeimagelistex.html)
 and
 [Engine.SmallImageListEx](engine-smallimagelistex.html)
 properties.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Method

| FindImage |
| --- |

#### See Also

[Engine.AddImage](engine-addimage.html)

[Engine.Images](engine-images.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

[Images.FindImage](images-findimage.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/importvioptions.html language=enus -->
## TOPIC 01210: ImportVIOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/importvioptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/importvioptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the options parameter of the LabVIEWModule.ImportVI method. Use the bitwise-OR operator to specify more than one option. ImportVIOption_ConfigureExpressVI –(Value: 0x1) Specifies to configure the Express VI before importing it into the code module. This option is valid only

### ImportVIOptions

Use these constants with the
 options
 parameter of the
 [LabVIEWModule.ImportVI](labviewmodule-importvi.html)
 method. Use the bitwise-OR operator to specify more than one option.

- ImportVIOption_ConfigureExpressVI 
 –(Value: 0x1) Specifies to configure the Express VI before importing it into the code module. This option is valid only when you pass the
 ImportVIType_ExpressVITemplate 
 enumeration for the
 type 
 parameter of the
 LabVIEWModule.ImportVI 
 method.
- ImportVIOption_NoOptions 
 –(Value: 0) No options.

#### See Also

[LabVIEWModule.ImportVI](labviewmodule-importvi.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/importvitypes.html language=enus -->
## TOPIC 01211: ImportVITypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/importvitypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/importvitypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the LabVIEWModule.ImportVI method to specify the type of VI to import to the module. ImportVIType_ExpressVITemplate –(Value: 1) Indicates that the VI to import is an Express VI template. When you use this option, TestStand generates a wrapper VI to call the given Express VI

### ImportVITypes

Use these constants with the
 [LabVIEWModule.ImportVI](labviewmodule-importvi.html)
 method to specify the type of VI to import to the module.

- ImportVIType_ExpressVITemplate 
 –(Value: 1) Indicates that the VI to import is an Express VI template. When you use this option, TestStand generates a wrapper VI to call the given Express VI template and imports the generated wrapper VI into the module.
- ImportVIType_ExpressVIWrapper 
 –(Value: 0) Indicates that the VI to import is a TestStand-generated Express VI wrapper.
- ImportVIType_PropertyNodeVICreate 
 –(Value: 3) When you use this option, TestStand generates a wrapper VI to call the LabVIEW Property Node and selected properties already configured in the step. TestStand imports the generated wrapper VI into the code module.
- ImportVIType_PropertyNodeVIWrapper 
 –(Value: 2) Indicates that the VI to import is a TestStand-generated LabVIEW Property Node VI wrapper.

#### See Also

[LabVIEWModule.ImportVI](labviewmodule-importvi.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputrecordstream-close.html language=enus -->
## TOPIC 01212: InputRecordStream.Close

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputrecordstream-close.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputrecordstream-close.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputRecordStream.Close Purpose Close this InputRecordStream . Remarks The exact behavior of Close depends on the implementation details of the class that implements the InputRecordStream interface. See Also CsvFileInputRecordStream.Close

### InputRecordStream.Close

#### Syntax

[InputRecordStream](inputrecordstream.html).Close

#### Purpose

Close this
 InputRecordStream
 .

#### Remarks

The exact behavior of
 Close
 depends on the implementation details of the class that implements the
 InputRecordStream
 interface.

#### See Also

[CsvFileInputRecordStream.Close](csvfileinputrecordstream-readrecord.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputrecordstream-fieldmapping.html language=enus -->
## TOPIC 01213: InputRecordStream.FieldMapping

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputrecordstream-fieldmapping.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputrecordstream-fieldmapping.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputRecordStream.FieldMapping Data Type String Specifies which fields to read from the InputRecordStream . Purpose Specifies which fields to read from the InputRecordStream . Remarks The mapping is a comma-separated list of index ranges. For example, 0, 3-5, 8-7 specifies that fields 0, 3, 4

### InputRecordStream.FieldMapping

#### Syntax

[InputRecordStream](inputrecordstream.html).FieldMapping

#### Data Type

[String](data-types-for-teststand.html)

Specifies which fields to read from the
 InputRecordStream
 .

#### Purpose

Specifies which fields to read from the
 InputRecordStream
 .

#### Remarks

The mapping is a comma-separated list of index ranges. For example,
 0, 3-5, 8-7
 specifies that fields 0, 3, 4, 5, 8, and 7 of each record in the stream be stored to fields 0-5 of each read record output from
 InputRecordStream.ReadRecord
 or
 InputRecordStream.ReadRecordTo
 . The last range in the list may be open-ended. For example,
 2, 3-
 specifies that fields 2, 3, and fields beyond 3 will be stored to fields 0, 1, and fields beyond 1 of each read record.

Note

ReadRecord

#### See Also

[CsvFileInputRecordStream.FieldMapping](csvfileinputrecordstream-fieldmapping.html)

[InputRecordStream.ReadRecord](inputrecordstream-readrecord.html)

[InputRecordStream.ReadRecordTo](inputrecordstream-readrecordto.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputrecordstream-readrecord.html language=enus -->
## TOPIC 01214: InputRecordStream.ReadRecord

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputrecordstream-readrecord.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputrecordstream-readrecord.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputRecordStream.ReadRecord( record, mapping = "") Return Value Long Returns 0 if a record was successfully read. Returns non-zero if end of file was encountered before reading a record. Purpose Read the next record from the stream. Parameters record As PropertyObject [In/Out] Specifies wher

### InputRecordStream.ReadRecord

#### Syntax

[InputRecordStream](inputrecordstream.html).ReadRecord( record, mapping = "")

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if a record was successfully read. Returns non-zero if end of file was encountered before reading a record.

#### Purpose

Read the next record from the stream.

#### Parameters

record
 As
 [PropertyObject](propertyobject.html)

[In/Out] Specifies where to store the incoming record. The record parameter may be a container, array, or string. If it is a container, the container represents the record, and each subproperty is a field. If the record parameter is an array, the array represents the record, and each array element is a field. If the record parameter is a string, the fields are written to the string as a comma-separated list.

mapping
 As
 [String](data-types-for-teststand.html)

[In] Specifies the mapping to elements (subproperties or array elements) in the record parameter from fields in the
 InputRecordStream
 . Mapping is not supported if the record parameter is a string. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that fields from the incoming record be stored to elements 0, 3, 4, 5, 8, and 7 of the container or array. The last range in the list may be open-ended. For example, "2, 3-" specifies that fields from the incoming record be written to elements 2, 3, and all elements beyond 3 of the container or array. If the record parameter is a container, the range list may include individual subproperty names. For example, "Temperature, Pressure, 0-1" specifies that fields from the incoming record be written to the subproperties "Temperature" and "Pressure" followed by elements 0 and 1. For convenience, you may specify an empty string to specify all elements be written in order. That is, an empty string is equivalent to "0-". The default value is an empty string.

This parameter has a default value of
 ""
 .

#### See Also

[CsvFileInputRecordStream.ReadRecord](csvfileinputrecordstream-readrecord.html)

[InputRecordStream.ReadRecordTo](inputrecordstream-readrecordto.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputrecordstream-readrecordto.html language=enus -->
## TOPIC 01215: InputRecordStream.ReadRecordTo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputrecordstream-readrecordto.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputrecordstream-readrecordto.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputRecordStream.ReadRecordTo( context, record) Return Value Long Returns 0 if a record was successfully read. Returns non-zero if end of file was encountered before reading a record. Purpose Read the next record from this stream. Parameters context As SequenceContext [In] Specifies the Sequ

### InputRecordStream.ReadRecordTo

#### Syntax

[InputRecordStream](inputrecordstream.html).ReadRecordTo( context, record)

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if a record was successfully read. Returns non-zero if end of file was encountered before reading a record.

#### Purpose

Read the next record from this stream.

#### Parameters

context
 As
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 against which to evaluate the lookup strings specified by the record parameter.

record
 As
 [String Array](data-types-for-teststand.html)

[In/Out] An array of lookup strings specifying where to store the fields from the incoming record. The lookup strings are evaluated relative to the
 SequenceContext
 specified by the context parameter.

#### See Also

[CsvFileInputRecordStream.ReadRecordTo](csvfileinputrecordstream-readrecordto.html)

[InputRecordStream.ReadRecord](inputrecordstream-readrecord.html)

[OutputRecordStream.WriteRecordFrom](outputrecordstream-writerecordfrom.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputrecordstream-skiprecords.html language=enus -->
## TOPIC 01216: InputRecordStream.SkipRecords

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputrecordstream-skiprecords.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputrecordstream-skiprecords.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputRecordStream.SkipRecords( numRecords) Return Value Long Returns 0 if numRecords were successfully skipped. Returns non-zero if end of file was encountered before numRecords were skipped. Purpose Skip the specified number of records. Parameters numRecords As Long [In] The number of record

### InputRecordStream.SkipRecords

#### Syntax

[InputRecordStream](inputrecordstream.html).SkipRecords( numRecords)

#### Return Value

[Long](data-types-for-teststand.html)

Returns
 0
 if
 numRecords
 were successfully skipped. Returns non-zero if end of file was encountered before numRecords were skipped.

#### Purpose

Skip the specified number of records.

#### Parameters

numRecords
 As
 [Long](data-types-for-teststand.html)

[In] The number of records to skip. If numRecords is
 0
 ,
 InputRecordStream.SkipRecords
 returns successfully without modifying the stream. Classes that implement the
 InputRecordStream
 interface are not required to support negative values for
 numRecords
 .

#### See Also

[CsvFileInputRecordStream.SkipRecords](csvfileinputrecordstream-skiprecords.html)

[InputRecordStream.ReadRecord](inputrecordstream-readrecord.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputrecordstream.html language=enus -->
## TOPIC 01217: InputRecordStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputrecordstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputrecordstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Property FieldMapping Methods Close ReadRecord ReadRecordTo SkipRecords See Also CsvFileInputRecordStream

### InputRecordStream

#### Property

| FieldMapping |
| --- |

#### Methods

| Close |
| --- |
| ReadRecord |
| ReadRecordTo |
| SkipRecords |

#### See Also

[CsvFileInputRecordStream](csvfileinputrecordstream.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputstream-isendofstream.html language=enus -->
## TOPIC 01218: InputStream.IsEndofStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputstream-isendofstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputstream-isendofstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputStream.IsEndofStream Data Type Boolean Purpose Indicates if the end of the stream has been reached. Remarks Use this property to determine whether the end of stream has been reached.

### InputStream.IsEndofStream

#### Syntax

[InputStream](inputstream.html).IsEndofStream

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Indicates if the end of the stream has been reached.

#### Remarks

Use this property to determine whether the end of stream has been reached.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputstream-length.html language=enus -->
## TOPIC 01219: InputStream.Length

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputstream-length.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputstream-length.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputStream.Length Data Type Long Purpose Returns the size of the stream in bytes. Remarks Use this property to obtain the size of the stream. You can use this value to determine how many characters to allocate for a buffer or to read from the stream.

### InputStream.Length

#### Syntax

[InputStream](inputstream.html).Length

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the size of the stream in bytes.

#### Remarks

Use this property to obtain the size of the stream. You can use this value to determine how many characters to allocate for a buffer or to read from the stream.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputstream-offset.html language=enus -->
## TOPIC 01220: InputStream.Offset

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputstream-offset.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputstream-offset.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputStream.Offset Data Type Long Purpose Specifies the current position of the reader in the stream. The offset is always from the start of the stream. Remarks Use this property to query the current position in the stream or to move the reader to a different position in the stream. The Input

### InputStream.Offset

#### Syntax

[InputStream](inputstream.html).Offset

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the current position of the reader in the stream. The offset is always from the start of the stream.

#### Remarks

Use this property to query the current position in the stream or to move the reader to a different position in the stream. The
 [InputStream.ReadBytes](inputstream-readbytes.html)
 method updates the stream reader position by using the number of bytes read from the stream.

#### See Also

[InputStream.ReadBytes](inputstream-readbytes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputstream-path.html language=enus -->
## TOPIC 01221: InputStream.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputstream-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputstream-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputStream.Path Data Type String Purpose Returns the pathname TestStand used when it loaded the user file.

### InputStream.Path

#### Syntax

[InputStream](inputstream.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the pathname TestStand used when it loaded the user file.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputstream-readbytes.html language=enus -->
## TOPIC 01222: InputStream.ReadBytes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputstream-readbytes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputstream-readbytes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InputStream.ReadBytes( numBytes) Return Value Byte Array An array of bytes that contains the data read from the stream. Purpose Obtains an array of bytes that contains the data read from the stream. This method reads the specified number of bytes from the stream and stores them in a byte arra

### InputStream.ReadBytes

#### Syntax

[InputStream](inputstream.html).ReadBytes( numBytes)

#### Return Value

[Byte Array](data-types-for-teststand.html)

An array of bytes that contains the data read from the stream.

#### Purpose

Obtains an array of bytes that contains the data read from the stream. This method reads the specified number of bytes from the stream and stores them in a byte array.

#### Remarks

This method increments the
 [Offset](inputstream-offset.html)
 of the stream reader by using the number of bytes read from the stream.

The actual number of bytes read from the stream can be less than the number of bytes specified for reading. You can use the stream reader Offset before and after the read to determine the actual number of bytes read.

#### Parameters

numBytes
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the maximum number of bytes to read from the stream.

#### See Also

[InputStream.Offset](inputstream-offset.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/inputstream.html language=enus -->
## TOPIC 01223: InputStream

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/inputstream.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/inputstream.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the InputStream class represent an abstract stream of data. In a sequence file translator, this stream reads the content of a user file. The InputStream class allows the translators to read, seek, and query the size of a file. You cannot create an InputStream object externally, and you ca

### InputStream

Objects of the InputStream class represent an abstract stream of data. In a sequence file translator, this stream reads the content of a user file. The InputStream class allows the translators to read, seek, and query the size of a file.

You cannot create an InputStream object externally, and you can obtain a reference only in the DLL interface exposed to a sequence file translator. The TestStand Engine creates an InputStream object and passes the object to various callbacks in the DLL interface.

#### Properties

| IsEndofStream (Read Only) |
| --- |
| Length (Read Only) |
| Offset |
| Path (Read Only) |

#### Method

| ReadBytes |
| --- |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-addstepindex.html language=enus -->
## TOPIC 01224: InteractiveArgs.AddStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-addstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-addstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.AddStepIndex( stepIndexParam) Purpose Adds a step to the list of steps to execute interactively Parameters stepIndexParam As Long [In] Specifies a zero-based index for a step in the list of steps for the sequence in which you are running steps interactively. See Also Interacti

### InteractiveArgs.AddStepIndex

#### Syntax

[InteractiveArgs](interactiveargs.html).AddStepIndex( stepIndexParam)

#### Purpose

Adds a step to the list of steps to execute interactively

#### Parameters

stepIndexParam
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for a step in the list of steps for the sequence in which you are running steps interactively.

#### See Also

[InteractiveArgs.Sequence](interactiveargs-sequence.html)

[InteractiveArgs.StepGroup](interactiveargs-stepgroup.html)

[Step.StepIndex](step-stepindex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-aspropertyobject.html language=enus -->
## TOPIC 01225: InteractiveArgs.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the InteractiveArgs object. Remarks Use the PropertyObject to modify, add, or remove custom properties for the object. Do not use this function to remove or modify the dy

### InteractiveArgs.AsPropertyObject

#### Syntax

[InteractiveArgs](interactiveargs.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the InteractiveArgs object.

#### Remarks

Use the PropertyObject to modify, add, or remove custom properties for the object.

Note

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-clearsteplist.html language=enus -->
## TOPIC 01226: InteractiveArgs.ClearStepList

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-clearsteplist.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-clearsteplist.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.ClearStepList Purpose Clears the list of steps to execute interactively. See Also InteractiveArgs.AddStepIndex

### InteractiveArgs.ClearStepList

#### Syntax

[InteractiveArgs](interactiveargs.html).ClearStepList

#### Purpose

Clears the list of steps to execute interactively.

#### See Also

[InteractiveArgs.AddStepIndex](interactiveargs-addstepindex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-containsstep.html language=enus -->
## TOPIC 01227: InteractiveArgs.ContainsStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-containsstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-containsstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.ContainsStep( stepIndexParam) Return Value Boolean Purpose Returns True if the step you specify is in the list of steps to run interactively. Parameters stepIndexParam As Long [In] Specifies a zero-based index for a step in the list of steps for the sequence in which you are r

### InteractiveArgs.ContainsStep

#### Syntax

[InteractiveArgs](interactiveargs.html).ContainsStep( stepIndexParam)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the step you specify is in the list of steps to run interactively.

#### Parameters

stepIndexParam
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for a step in the list of steps for the sequence in which you are running steps interactively.

#### See Also

[Step.StepIndex](step-stepindex.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-getstepindex.html language=enus -->
## TOPIC 01228: InteractiveArgs.GetStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-getstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-getstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.GetStepIndex( arrayIndexParam) Return Value Long Purpose Returns a step index stored at a specific position in the list of steps to run interactively. Remarks The step index that the method returns is a zero-based index into the list of steps for the sequence. Parameters array

### InteractiveArgs.GetStepIndex

#### Syntax

[InteractiveArgs](interactiveargs.html).GetStepIndex( arrayIndexParam)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Returns a step index stored at a specific position in the list of steps to run interactively.

#### Remarks

The step index that the method returns is a zero-based index into the list of steps for the sequence.

#### Parameters

arrayIndexParam
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index for the list of steps to run interactively.

#### See Also

[InteractiveArgs.Sequence](interactiveargs-sequence.html)

[InteractiveArgs.StepGroup](interactiveargs-stepgroup.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-loopcount.html language=enus -->
## TOPIC 01229: InteractiveArgs.LoopCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-loopcount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-loopcount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.LoopCount Data Type Long Purpose Returns or specifies the number of times to execute the list of selected steps. Remarks If the value of this property is -1, the execution loops indefinitely on the selected steps.

### InteractiveArgs.LoopCount

#### Syntax

[InteractiveArgs](interactiveargs.html).LoopCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns or specifies the number of times to execute the list of selected steps.

#### Remarks

If the value of this property is -1, the execution loops indefinitely on the selected steps.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-numsteps.html language=enus -->
## TOPIC 01230: InteractiveArgs.NumSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-numsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-numsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.NumSteps Data Type Long Purpose Returns the number of step indexes added to the InteractiveArgs object.

### InteractiveArgs.NumSteps

#### Syntax

[InteractiveArgs](interactiveargs.html).NumSteps

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of step indexes added to the InteractiveArgs object.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-sequence.html language=enus -->
## TOPIC 01231: InteractiveArgs.Sequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-sequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.Sequence Data Type Sequence Purpose Specifies the sequence that contains the steps the InteractiveArgs object lists by index. Remarks Set this property before passing the InteractiveArgs to a method that starts an execution. If you do not set this property, TestStand assumes t

### InteractiveArgs.Sequence

#### Syntax

[InteractiveArgs](interactiveargs.html).Sequence

#### Data Type

[Sequence](sequence.html)

#### Purpose

Specifies the sequence that contains the steps the InteractiveArgs object lists by index.

#### Remarks

Set this property before passing the InteractiveArgs to a method that starts an execution. If you do not set this property, TestStand assumes that InteractiveArgs specifies steps in the first sequence the execution runs. If you specify a process model, the first sequence an execution runs is the Process Model entry point.

#### See Also

[InteractiveArgs.StepGroup](interactiveargs-stepgroup.html)

[Sequence](sequence.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-stepgroup.html language=enus -->
## TOPIC 01232: InteractiveArgs.StepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-stepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.StepGroup Data Type StepGroups Use the following constants with this data type: StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step group. Purpose Returns

### InteractiveArgs.StepGroup

#### Syntax

[InteractiveArgs](interactiveargs.html).StepGroup

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

Returns or specifies the step group containing the steps to execute interactively.

#### See Also

[InteractiveArgs.Sequence](interactiveargs-sequence.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs-stopexpression.html language=enus -->
## TOPIC 01233: InteractiveArgs.StopExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs-stopexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs-stopexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveArgs.StopExpression Data Type String Purpose Gets or sets an expression with a value that indicates when to stop an execution that specifies a loop count. Remarks If the expression evaluates to True , the interactive execution stops. If the expression is an empty string, it is not

### InteractiveArgs.StopExpression

#### Syntax

[InteractiveArgs](interactiveargs.html).StopExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Gets or sets an expression with a value that indicates when to stop an execution that specifies a loop count.

#### Remarks

If the expression evaluates to
 True
 , the interactive execution stops. If the expression is an empty string, it is not evaluated.

#### See Also

[InteractiveArgs.LoopCount](interactiveargs-loopcount.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactiveargs.html language=enus -->
## TOPIC 01234: InteractiveArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactiveargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactiveargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you call the Engine.NewExecution or Thread.DoInteractiveExecution methods to create an interactive execution, use an object of this class to pass information about the current state of the user interface. These methods use the object to determine which steps are currently selected in the user i

### InteractiveArgs

When you call the
 [Engine.NewExecution](engine-newexecution.html)
 or
 [Thread.DoInteractiveExecution](thread-dointeractiveexecution.html)
 methods to create an interactive execution, use an object of this class to pass information about the current state of the user interface. These methods use the object to determine which steps are currently selected in the user interface.

Create objects for this class using the
 [Engine.NewInteractiveArgs](engine-newinteractiveargs.html)
 method.

#### Properties

| LoopCount |
| --- |
| NumSteps (Read Only) |
| Sequence |
| StepGroup |
| StopExpression |

#### Methods

| AddStepIndex |
| --- |
| AsPropertyObject |
| ClearStepList |
| ContainsStep |
| GetStepIndex |

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

[Engine.NewInteractiveArgs](engine-newinteractiveargs.html)

[Thread.DoInteractiveExecution](thread-dointeractiveexecution.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactivebranchmodes.html language=enus -->
## TOPIC 01235: InteractiveBranchModes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactivebranchmodes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactivebranchmodes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with StationOptions.InteractiveBranchMode property. InteractiveBranchMode_AllowAll –(Value: 4) The interactive execution allows branching to selected and non-selected steps. When TestStand executes a selected step and no branch occurs, the next step is the next selected step. Whe

### InteractiveBranchModes

Use these constants with
 [StationOptions.InteractiveBranchMode](stationoptions-interactivebranchmode.html)
 property.

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

#### See Also

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[StationOptions.InteractiveBranchMode](stationoptions-interactivebranchmode.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactivecontext-aspropertyobject.html language=enus -->
## TOPIC 01236: InteractiveContext.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactivecontext-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactivecontext-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveContext.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the InteractiveContext object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### InteractiveContext.AsPropertyObject

#### Syntax

[InteractiveContext](interactivecontext.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the InteractiveContext object.

#### Remarks

Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactivecontext-interactiveargs.html language=enus -->
## TOPIC 01237: InteractiveContext.InteractiveArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactivecontext-interactiveargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactivecontext-interactiveargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveContext.InteractiveArgs Data Type InteractiveArgs Purpose Returns the InteractiveArgs object for the current interactive execution. Remarks Use this property to obtain a reference to the InteractiveArgs object used to initiate the currently executing interactive execution. See Also

### InteractiveContext.InteractiveArgs

#### Syntax

[InteractiveContext](interactivecontext.html).InteractiveArgs

#### Data Type

[InteractiveArgs](interactiveargs.html)

#### Purpose

Returns the InteractiveArgs object for the current interactive execution.

#### Remarks

Use this property to obtain a reference to the InteractiveArgs object used to initiate the currently executing interactive execution.

#### See Also

[InteractiveArgs](interactiveargs.html)

[SequenceContext.InteractiveContext](sequencecontext-interactivecontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactivecontext-isrootexecution.html language=enus -->
## TOPIC 01238: InteractiveContext.IsRootExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactivecontext-isrootexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactivecontext-isrootexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveContext.IsRootExecution Data Type Boolean Purpose Returns True if the execution is a root interactive execution. Returns False if the execution is a nested interactive execution. Remarks A root interactive execution is a new, independent execution the user initiates on selected ste

### InteractiveContext.IsRootExecution

#### Syntax

[InteractiveContext](interactivecontext.html).IsRootExecution

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the execution is a root interactive execution. Returns
 False
 if the execution is a nested interactive execution.

#### Remarks

A root interactive execution is a new, independent execution the user initiates on selected steps from a Sequence File window.

The user starts a nested interactive execution from an Execution window for a normal execution suspended at a breakpoint. The nested interactive execution runs within the context of the normal execution.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactivecontext-savednextstepindex.html language=enus -->
## TOPIC 01239: InteractiveContext.SavedNextStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactivecontext-savednextstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactivecontext-savednextstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveContext.SavedNextStepIndex Data Type Long Purpose Applies only to nested interactive executions. Returns the index of the step ready to execute next in the normal execution when the user began the current interactive execution. Remarks If the InteractiveContext.IsRootExecution prop

### InteractiveContext.SavedNextStepIndex

#### Syntax

[InteractiveContext](interactivecontext.html).SavedNextStepIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Applies only to nested interactive executions. Returns the index of the step ready to execute next in the normal execution when the user began the current interactive execution.

#### Remarks

If the
 [InteractiveContext.IsRootExecution](interactivecontext-isrootexecution.html)
 property is
 False
 , this property returns the value of the
 [SequenceContext.NextStepIndex](sequencecontext-nextstepindex.html)
 property at the time the interactive execution began. This value is purely informational and is provided so you can display information to the user when writing a user interface.

Returns
 -1
 if the
 InteractiveContext.IsRootExecution
 property is
 True
 .

#### See Also

[InteractiveContext.IsRootExecution](interactivecontext-isrootexecution.html)

[SequenceContext.NextStepIndex](sequencecontext-nextstepindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactivecontext-savedpreviousstepindex.html language=enus -->
## TOPIC 01240: InteractiveContext.SavedPreviousStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactivecontext-savedpreviousstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactivecontext-savedpreviousstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveContext.SavedPreviousStepIndex Data Type Long Purpose Applies only to nested interactive executions. Returns the index of the last step that executed in the normal execution before the user began the current interactive execution. Remarks If the InteractiveContext.IsRootExecution p

### InteractiveContext.SavedPreviousStepIndex

#### Syntax

[InteractiveContext](interactivecontext.html).SavedPreviousStepIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Applies only to nested interactive executions. Returns the index of the last step that executed in the normal execution before the user began the current interactive execution.

#### Remarks

If the
 [InteractiveContext.IsRootExecution](interactivecontext-isrootexecution.html)
 property is
 False
 , this property returns the value of the
 [SequenceContext.PreviousStepIndex](sequencecontext-previousstepindex.html)
 property at the time the interactive execution began. This value is purely informational and is provided so you can display information to the user when writing a user interface.

Returns
 -1
 if the
 InteractiveContext.IsRootExecution
 property is
 True
 .

#### See Also

[InteractiveContext.IsRootExecution](interactivecontext-isrootexecution.html)

[SequenceContext.PreviousStepIndex](sequencecontext-previousstepindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactivecontext-savedstepindex.html language=enus -->
## TOPIC 01241: InteractiveContext.SavedStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactivecontext-savedstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactivecontext-savedstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InteractiveContext.SavedStepIndex Data Type Long Purpose Applies only to nested interactive executions. Returns the index of the active step in the normal execution when the user began the current interactive execution. Remarks If the IsRootExecution property is False , this property returns

### InteractiveContext.SavedStepIndex

#### Syntax

[InteractiveContext](interactivecontext.html).SavedStepIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Applies only to nested interactive executions. Returns the index of the active step in the normal execution when the user began the current interactive execution.

#### Remarks

If the
 [IsRootExecution](interactivecontext-isrootexecution.html)
 property is
 False
 , this property returns the state of the
 [SequenceContext.StepIndex](sequencecontext-stepindex.html)
 property before the interactive execution began.

Currently, because you can only begin an interactive execution between steps in the currently executing sequence, this property always returns -1.

Returns
 -1
 if the IsRootExecution property is
 True
 .

#### See Also

[InteractiveContext.IsRootExecution](interactivecontext-isrootexecution.html)

[SequenceContext.StepIndex](sequencecontext-stepindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/interactivecontext.html language=enus -->
## TOPIC 01242: InteractiveContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/interactivecontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/interactivecontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects of this class to obtain additional information about a currently executing interactive execution. Obtain objects of this class using the SequenceContext.InteractiveContext property of the sequence context in which the interactive execution began. Properties InteractiveArgs (Read Only) Is

### InteractiveContext

Use objects of this class to obtain additional information about a currently executing interactive execution. Obtain objects of this class using the
 [SequenceContext.InteractiveContext](sequencecontext-interactivecontext.html)
 property of the sequence context in which the interactive execution began.

#### Properties

| InteractiveArgs (Read Only) |
| --- |
| IsRootExecution (Read Only) |
| SavedNextStepIndex (Read Only) |
| SavedPreviousStepIndex (Read Only) |
| SavedStepIndex (Read Only) |

#### Method

| AsPropertyObject |
| --- |

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[SequenceContext.InteractiveContext](sequencecontext-interactivecontext.html)

[Thread.DoInteractiveExecution](thread-dointeractiveexecution.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/internaloptions.html language=enus -->
## TOPIC 01243: InternalOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/internaloptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/internaloptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the internal options you can access through the Engine.GetInternalOption and Engine.SetInternalOption methods. InternalOption_ApplicationManager –(Value: 5) Returns an IUnknown interface to the Application Manager user interface control for the current process. Returns a NULL interface if

### InternalOptions

Specifies the internal options you can access through the
 [Engine.GetInternalOption](engine-getinternaloption.html)
 and
 [Engine.SetInternalOption](engine-setinternaloption.html)
 methods.

- InternalOption_ApplicationManager 
 –(Value: 5) Returns an IUnknown interface to the
 
 Application Manager 
 user interface control for the current process. Returns a
 NULL 
 interface if no Application Manager user interface control exists in the current process.
- InternalOption_AutomationAdapterUsesDispatchForDualInterfaces 
 –(Value: 2) Specifies a Boolean value that determines whether the
 ActiveX/COM Adapter 
 calls the dispatch portion of a dual interface instead of the vtable portion of the interface. Use this property to exercise both the vtable and dispatch portions of a dual server interface when you perform software testing on a server. The default value of this property is
 False 
 .
- InternalOption_DisableFloatingWindowsForModalDialogs 
 –(Value: 10) Specifies a Boolean value that determines whether TestStand disables all windows in the same thread as the thread that launches an engine dialog box. This is useful for applications that have multiple modeless windows to disable while a modal dialog box launches. The default value of the option is
 True 
 .
- InternalOption_UpdateExternalEnvironments 
 –(Value: 3) Specifies a Boolean value that determines whether TestStand installs development support items at engine start up. Development support items include TestStand palettes and toolbox items for application development environments (ADEs) that support them, such as LabVIEW and Microsoft Visual Studio. Although the TestStand installer also installs these items, this option ensures that the items are installed to an ADE if the ADE is installed or upgraded after TestStand is installed. At startup, TestStand checks whether it has already installed the support items for a particular ADE so startup time does not increase unnecessarily. If you disable this option, you can manually update the support items for a particular ADE by running the TestStand Version Selector and specifying
 "/ver current" 
 on the command line or by switching to the current version in the
 Version Selector 
 dialog box. The default value of the option is
 True 
 .

TestStand persists the setting for this option between invocations of the TestStand Engine.
- InternalOption_WarnOnAPICallThroughDispatchInterface 
 –(Value: 1) Specifies a Boolean value that determines whether TestStand launches a warning dialog box for each TestStand API call you make through a dispatch interface. If you intend to use only the vtable interface for the TestStand API, use this property to determine whether the code unintentionally uses a dispatch interface to the TestStand API. The default value of this property is
 False 
 . This option does not apply to the
 Engine 
 object. TestStand does not warn you for calls you make through a dispatch interface to the
 Engine 
 object.

#### See Also

[Engine.GetInternalOption](engine-getinternaloption.html)

[Engine.SetInternalOption](engine-setinternaloption.html)

[Version Selector dialog box](../tsref/teststand-version-selector.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/internalstartupoptions.html language=enus -->
## TOPIC 01244: InternalStartupOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/internalstartupoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/internalstartupoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the internal startup options you can set through the EngineInitializationSettings.SetInternalStartupOption method. InternalStartupOption_TestStandReserved1 –(Value: 0x1) This option is reserved for internal use by National Instruments. Specifying this option in a user-built application has

### InternalStartupOptions

Specifies the internal startup options you can set through the
 EngineInitializationSettings.SetInternalStartupOption
 method.

- InternalStartupOption_TestStandReserved1 
 –(Value: 0x1) This option is reserved for internal use by National Instruments. Specifying this option in a user-built application has no effect.

#### See Also

[EngineInitializationSettings.SetInternalStartupOption](engineinitializationsettings-setinternalstart.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-additionalthreadsinheritcallin.html language=enus -->
## TOPIC 01245: LabVIEWAdapter.AdditionalThreadsInheritCallingThreadsCPUAffinity

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-additionalthreadsinheritcallin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-additionalthreadsinheritcallin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.AdditionalThreadsInheritCallingThreadsCPUAffinity Data Type Boolean Purpose Specifies if the CPU affinity for the additional threads used to execute VIs with the LabVIEW Run-Time Engine (RTE) inherit the CPU affinity of the TestStand execution thread. The LabVIEW Adapter uses t

### LabVIEWAdapter.AdditionalThreadsInheritCallingThreadsCPUAffinity

#### Syntax

[LabVIEWAdapter](labviewadapter.html).AdditionalThreadsInheritCallingThreadsCPUAffinity

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the
 [CPU affinity](/csh?context=ts_tsfundamentals_smp_clarification)
 for the additional threads used to execute VIs with the LabVIEW Run-Time Engine (RTE) inherit the CPU affinity of the TestStand execution thread.

Note

same as caller

#### Remarks

Changes to this property do not take effect until you restart the TestStand Engine.

#### See Also

[LabVIEWAdapter.NumberofThreadsUsedWhenExecutingVIsWithRTE](labviewadapter-numberofthreadsusedwhenexecuti.html)

[LabVIEWAdapter.UseMultipleThreadsWhenExecutingVIsWithRTE](labviewadapter-usemultiplethreadswhenexecutin.html)

[Symmetric Multiprocessing in VIs Executed from TestStand](/csh?context=ts_tslabview_smp)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-asadapter.html language=enus -->
## TOPIC 01246: LabVIEWAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter object that represents the LabVIEWAdapter object. Remarks Use the underlying module Adapter object to access properties and methods that are common to all adapters. See Also Adapter

### LabVIEWAdapter.AsAdapter

#### Syntax

[LabVIEWAdapter](labviewadapter.html).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter object that represents the LabVIEWAdapter object.

#### Remarks

Use the underlying module Adapter object to access properties and methods that are common to all adapters.

#### See Also

[Adapter](adapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-autodeploysharedvariables.html language=enus -->
## TOPIC 01247: LabVIEWAdapter.AutoDeploySharedVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-autodeploysharedvariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-autodeploysharedvariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.AutoDeploySharedVariables Data Type Boolean Purpose Set this property to True for TestStand to deploy shared variables defined in LabVIEW libraries within the LabVIEW projects you use in TestStand. This occurs the first time a loading LabVIEW step references the project. Remark

### LabVIEWAdapter.AutoDeploySharedVariables

#### Syntax

[LabVIEWAdapter](labviewadapter.html).AutoDeploySharedVariables

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 for TestStand to deploy shared variables defined in LabVIEW libraries within the LabVIEW projects you use in TestStand. This occurs the first time a loading LabVIEW step references the project.

#### Remarks

The LabVIEW library to deploy should contain only shared variables.

TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the
 LabVIEW Help
 for more information about deploying shared variables and NI-PSP URLs.

#### See Also

[Deploying Network-Published Shared Variables](/csh?context=ts_tslabview_variable)

[LabVIEWAdapter.AutoUndeploySharedVariables](labviewadapter-autoundeploysharedvariables.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-autoundeploysharedvariables.html language=enus -->
## TOPIC 01248: LabVIEWAdapter.AutoUndeploySharedVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-autoundeploysharedvariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-autoundeploysharedvariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.AutoUndeploySharedVariables Data Type Boolean Purpose Set this property to True for TestStand to undeploy the shared variables defined in LabVIEW libraries within the LabVIEW project once the last LabVIEW step that references the LabVIEW Project is unloaded. Remarks TestStand c

### LabVIEWAdapter.AutoUndeploySharedVariables

#### Syntax

[LabVIEWAdapter](labviewadapter.html).AutoUndeploySharedVariables

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 for TestStand to undeploy the shared variables defined in LabVIEW libraries within the LabVIEW project once the last LabVIEW step that references the LabVIEW Project is unloaded.

#### Remarks

TestStand can deploy a shared variable bound to another shared variable only when you use an NI Publish-Subscribe Protocol (NI-PSP) URL to bind the shared variable to deploy to another shared variable. If you attempt to use a Deploy Library step to deploy a shared variable to a variable in a LabVIEW project, the deployment fails. Refer to the
 LabVIEW Help
 for more information about deploying shared variables and NI-PSP URLs.

#### See Also

[Deploying Network-Published Shared Variables](/csh?context=ts_tslabview_variable)

[LabVIEWAdapter.AutoDeploySharedVariables](labviewadapter-autodeploysharedvariables.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-buildandexecuteatstartofexecut.html language=enus -->
## TOPIC 01249: LabVIEWAdapter.BuildAndExecuteAtStartOfExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-buildandexecuteatstartofexecut.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-buildandexecuteatstartofexecut.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.BuildAndExecuteAtStartOfExecution Data Type Boolean Purpose Specifies the current value of the 'Enable Build Source Files and Execute' option in the LabVIEW adapter configuration. Remarks Changes to this property do not take effect until you restart the TestStand engine. Even i

### LabVIEWAdapter.BuildAndExecuteAtStartOfExecution

#### Syntax

[LabVIEWAdapter](labviewadapter.html).BuildAndExecuteAtStartOfExecution

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies the current value of the 'Enable Build Source Files and Execute' option in the LabVIEW adapter configuration.

#### Remarks

Changes to this property do not take effect until you restart the TestStand engine.

Even if this option is enabled, the Build Source Files and Execute feature might not be enabled since some requirements for using the feature are not satisfied. The
 [IsBuildAndExecuteEnabled](labviewadapter-isbuildandexecuteenabled.html)
 method can be used to determine if the feature is enabled or not.

#### See Also

[Build Source Files and Execute](/csh?context=ts_tsref_build_and_execute)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/labviewadapter-buildpplsatstartofexecution.html language=enus -->
## TOPIC 01250: LabVIEWAdapter.BuildPPLsAtStartOfExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/labviewadapter-buildpplsatstartofexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/labviewadapter-buildpplsatstartofexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax LabVIEWAdapter.BuildPPLsAtStartOfExecution Data Type Boolean Purpose Specifies whether the LabVIEW Adapter must build the packed project library during execution if the step is configured to use the override settings and the packed project library is missing or out-of-date. Remarks This optio

### LabVIEWAdapter.BuildPPLsAtStartOfExecution

#### Syntax

[LabVIEWAdapter](labviewadapter.html).BuildPPLsAtStartOfExecution

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether the LabVIEW Adapter must build the packed project library during execution if the step is configured to use the override settings and the packed project library is missing or out-of-date.

#### Remarks

This option is available if the LabVIEW development system is installed.

Parent topic:

Properties
